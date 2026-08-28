# Verified online reference seeds

These are starting points, not a complete literature review. Verify bibliographic details and inspect full definitions before relying on them.

## Costly computation / computational games

1. Joseph Y. Halpern, Rafael Pass, **Game Theory with Costly Computation** (arXiv:0809.0024, 2008; conference version 2010).
   - https://arxiv.org/abs/0809.0024

2. Joseph Y. Halpern, Rafael Pass, **Algorithmic Rationality: Game Theory with Costly Computation**, Journal of Economic Theory 156 (2015), 246–268.
   - DOI: 10.1016/j.jet.2014.04.007
   - https://arxiv.org/abs/1412.2993

3. Joseph Y. Halpern, Rafael Pass, **I Don't Want to Think About it Now: Decision Theory With Costly Computation**.
   - https://arxiv.org/abs/1106.2657

## Bounded optimality / metareasoning

4. Stuart Russell, Eric Wefald, **Principles of Metareasoning**, Artificial Intelligence 49 (1991), 361–395.
   - DOI: 10.1016/0004-3702(91)90015-C

5. Stuart J. Russell, Devika Subramanian, **Provably Bounded-Optimal Agents**, JAIR 2 (1995), 575–609.
   - DOI: 10.1613/jair.133
   - https://arxiv.org/abs/cs/9505103

## Sequential constrained resources

6. Eitan Altman, **Constrained Markov Decision Processes** (1999).
   - ISBN/book source; use this as an entry point into occupation-measure CMDP literature.

7. Ehsan Shafieepoorfard, Maxim Raginsky, Sean P. Meyn, **Rationally Inattentive Control of Markov Processes**, SIAM J. Control Optim. 54(2), 2016, 987–1016.
   - DOI: 10.1137/15M1008476
   - https://arxiv.org/abs/1502.03762

## Resource rationality

8. Falk Lieder, Thomas L. Griffiths, **Rational Use of Cognitive Resources: Levels of Analysis Between the Computational and the Algorithmic**, Topics in Cognitive Science (2015).
   - DOI: 10.1111/tops.12142

9. Falk Lieder, Thomas L. Griffiths, **Resource-rational analysis: Understanding human cognition as the optimal use of limited computational resources**, Behavioral and Brain Sciences, published online 2019 / volume 43.
   - DOI: 10.1017/S0140525X1900061X

10. Recent empirical connection: **Time Spent Thinking in Online Chess Reflects the Value of Computation** (Cognitive Science, 2025).
    - Search DOI/current publisher metadata and inspect methods if human validation becomes relevant.

## Adaptive computation

11. Alex Graves, **Adaptive Computation Time for Recurrent Neural Networks** (2016).
    - https://arxiv.org/abs/1603.08983

This is not directly game theory, but it is a useful precedent for input-dependent realized computation.

## Algorithmic complexity attacks

12. Scott A. Crosby, Dan S. Wallach, **Denial of Service via Algorithmic Complexity Attacks**, USENIX Security 2003.
    - https://static.usenix.org/event/sec03/tech/full_papers/crosby/crosby_html/

This literature is relevant because an adversary deliberately selects inputs that induce worst-case resource use.

## Adversarial game search

13. Li-Cheng Lan et al., **Are AlphaZero-like Agents Robust to Adversarial Perturbations?**, NeurIPS 2022.
    - https://arxiv.org/abs/2211.03769

14. Khoi P. N. Nguyen, Raghuram Ramanujan, **Lookahead Pathology in Monte-Carlo Tree Search** (2022/2023).
    - https://arxiv.org/abs/2212.05208

These primarily study decision degradation/pathology, not necessarily induced workload, but can lead to adjacent terminology and references.

## External experiment frameworks

15. **OpenSpiel** — Google DeepMind general game research framework.
    - https://github.com/google-deepmind/open_spiel
    - https://openspiel.readthedocs.io/

16. **python-chess** — UCI engine integration; `chess.engine.Limit(nodes=...)` supports node-limited runs.
    - https://python-chess.readthedocs.io/en/stable/engine.html
    - https://github.com/niklasf/python-chess

17. **Stockfish** — official engine repository / UCI docs.
    - https://github.com/official-stockfish/Stockfish

18. **Ludii** — general game system, useful only after the exact protocol is stable.
    - https://github.com/Ludeme/Ludii
    - https://ludii.games/

## Literature note

The crucial novelty risk is not whether these papers use the phrase “Strategic Exposure Frontier.” It is whether their mathematical object already specializes to the same thing under a change of notation.
