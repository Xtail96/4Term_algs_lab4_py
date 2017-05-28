from collections import namedtuple
from math import inf

Seg = namedtuple("Seg", ('x', 'y'))
Sol = namedtuple("Sol", ('sum', 'segs'))
inf_sol = Sol(inf, frozenset())
zero_sol = Sol(0, frozenset())


solve_cache = dict()


def solve(segments, overlay):
    if (segments, overlay) not in solve_cache:
        solve_cache[segments, overlay] = _solve(segments, overlay)
    else:
        print("cached?")
    sol = solve_cache[segments, overlay]
    return sol


def seg_filter(segments, overlay):
    def cond(seg):
        return seg.x <= overlay.x <= seg.y
    return filter(cond, segments)


def _solve(segments, overlay):
    if overlay.x > overlay.y:
        return zero_sol
    segs = seg_filter(segments, overlay)
    if segs:
        solutions = list()
        for s in segs:
            l = s.y - s.x + 1
            p = solve(segments, Seg(s.y + 1, overlay.y))
            solutions.append(
                Sol(l + p.sum, frozenset({s}) | p.segs)
            )
        return min(solutions, key=lambda x: x.sum, default=inf_sol)
    else:
        return inf_sol


def main():
    segments = frozenset({
        Seg(1, 4),
        Seg(4, 9),
        Seg(5, 12)
    })
    overlay = Seg(3, 6)
    # 1234
    #    456789
    #     56789...
    #   3456
    print(solve(segments, overlay))

if __name__ == '__main__':
    main()
