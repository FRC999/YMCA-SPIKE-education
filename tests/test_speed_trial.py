"""Offline behavior checks; these do not simulate a real SPIKE robot."""
import asyncio
import ast
from pathlib import Path
import types
import unittest
from unittest.mock import patch


class SpeedTrialTests(unittest.TestCase):
    def setUp(self):
        self.moves = []
        self.stops = []
        self.failure = None

        async def move(*args, **kwargs):
            self.moves.append((args, kwargs))
            if self.failure:
                raise self.failure

        async def noop(*args):
            pass

        modules = {
            'hub': types.SimpleNamespace(
                port=types.SimpleNamespace(A='A', B='B'),
                light_matrix=types.SimpleNamespace(write=noop)),
            'motor_pair': types.SimpleNamespace(
                PAIR_1=1, pair=lambda *args: None,
                move_for_degrees=move, stop=lambda pair: self.stops.append(pair)),
            'runloop': types.SimpleNamespace(sleep_ms=noop),
        }
        source = Path(__file__).resolve().parents[1] / '04_Python/W07_speed_trial.py'
        tree = ast.parse(source.read_text(encoding='utf-8'))
        # Suppress only the final hardware entry point, then call main ourselves.
        last = tree.body.pop()
        self.assertEqual(ast.unparse(last), 'runloop.run(main())')
        self.ns = {}
        with patch.dict('sys.modules', modules):
            exec(compile(tree, str(source), 'exec'), self.ns)

    def run_main(self):
        asyncio.run(self.ns['main']())

    def test_unconfigured_route_refuses_motion_and_stops(self):
        with self.assertRaises(ValueError):
            self.run_main()
        self.assertEqual(self.moves, [])
        self.assertTrue(self.stops)

    def test_one_start_makes_exactly_one_bounded_straight_move(self):
        self.ns['TRAVEL_DEGREES'] = 900
        self.run_main()
        self.assertEqual(self.moves, [((1, 900, 0), {'velocity': 200})])
        self.assertTrue(self.stops)

    def test_unapproved_and_out_of_classroom_speeds_never_move(self):
        self.ns['TRAVEL_DEGREES'] = 900
        for speed in (0, -200, 300, 500, 200.0, True):
            with self.subTest(speed=speed), self.assertRaises(ValueError):
                asyncio.run(self.ns['sprint'](speed))
        self.assertEqual(self.moves, [])

    def test_corrupt_approval_list_does_not_bypass_classroom_cap(self):
        self.ns['TRAVEL_DEGREES'] = 900
        self.ns['APPROVED_SPEEDS'] = (200, 500)
        with self.assertRaises(ValueError):
            self.run_main()
        self.assertEqual(self.moves, [])
        self.assertTrue(self.stops)

    def test_approved_higher_speed_preserves_travel(self):
        self.ns['TRAVEL_DEGREES'] = 900
        self.ns['APPROVED_SPEEDS'] = (200, 300, 400)
        asyncio.run(self.ns['sprint'](300))
        asyncio.run(self.ns['sprint'](400))
        self.assertEqual([args[1] for args, kw in self.moves], [900, 900])
        self.assertEqual([kw['velocity'] for args, kw in self.moves], [300, 400])

    def test_invalid_route_values_refuse_motion(self):
        for distance in (0, -1, 1441, 900.5, True):
            self.ns['TRAVEL_DEGREES'] = distance
            with self.subTest(distance=distance), self.assertRaises(ValueError):
                self.run_main()
        self.assertEqual(self.moves, [])

    def test_motor_exception_still_stops(self):
        self.ns['TRAVEL_DEGREES'] = 900
        self.failure = RuntimeError('simulated motor fault')
        with self.assertRaises(RuntimeError):
            self.run_main()
        self.assertEqual(len(self.moves), 1)
        self.assertTrue(self.stops)


if __name__ == '__main__':
    unittest.main()
