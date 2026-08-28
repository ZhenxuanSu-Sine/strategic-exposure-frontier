# Mandatory novelty audit

The online agent must assume the idea may already exist under different names.

## Primary threat to novelty: costly-computation games

Halpern & Pass explicitly model strategic players whose choices are machines and whose utility can depend on machine complexity. This is much closer than generic “computational game theory.” Determine whether their complexity functions can depend on type, history, runtime, opponent behavior, or realized computation strongly enough to subsume strategic exposure.

Do not merely cite the abstract. Read definitions and examples.

## Other close bodies of work

### Bounded optimality / metareasoning

Check whether optimizing computation sequences, value of computation, or bounded-optimal programs already induces the same peak-vs-realized distinction.

### CMDP / occupation measure theory

Expected trajectory resource cost under policy-induced state visitation is standard. Do not claim endogenous occupancy constraints as novel.

### Rationally inattentive control

Sequential information costs under Markov occupancy are established. Distinguish the general resource axis here from Shannon information cost.

### Average-case / distributional query complexity

Worst-case vs expected decision-tree depth is a direct mathematical analogue of peak vs mean workload. Determine what changes when an adversarial opponent strategically controls the input/state distribution.

### Algorithmic complexity attacks

Security literature studies adversarial inputs intentionally triggering worst-case runtime. Determine whether “opponent-forceable workload” is merely this concept embedded in a game, or whether the payoff-constrained strategic restriction adds a distinct object.

### Adversarial search / game-tree pathology

Search for work where an opponent or game state induces increased tree-search effort, not just worse decisions.

## Required search strings

Search exact and variant queries, including:

- `"game theory with costly computation" runtime history dependent complexity`
- `"machine games" computation cost extensive form`
- `"resource bounded" extensive form games computation`
- `opponent induced computational cost game search`
- `adversarial search computational effort opponent`
- `algorithmic complexity attack strategic game`
- `best response computational burden tie breaking`
- `epsilon best response computation cost`
- `average case query complexity adversarial distribution`
- `distributional decision tree complexity minimax distribution`
- `risk sensitive computation cost MDP CVaR`
- `metareasoning adversarial environment computation`
- `bounded optimality game opponent computation`

Then expand from vocabulary found in the papers.

## Required output: overlap matrix

Create a table with rows for each proposed contribution:

1. peak vs expected exposure;
2. policy-induced occupancy;
3. opponent-controlled occupancy;
4. payoff-preserving exposure forcing;
5. epsilon-best-response exposure curve;
6. mean / CVaR / peak exposure geometry;
7. reward-vs-exposure frontiers;
8. cross-architecture robustness.

Columns:

- nearest source;
- exact source definition;
- identical / special case / related / apparently absent;
- evidence quote/page/equation reference;
- implication for our novelty claim.

## Citation graph requirement

For the 5 closest papers:

- inspect references backward;
- inspect works that cite them forward using Semantic Scholar/OpenAlex/Google Scholar if accessible;
- prioritize papers whose titles/abstracts contain machine, computation, resource, runtime, extensive-form, bounded, metareasoning, cost, adversarial.

## Go/no-go criterion

Do not call the framework novel unless the overlap audit survives this process. If it does not, reframe or pivot.
