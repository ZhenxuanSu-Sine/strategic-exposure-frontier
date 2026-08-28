"""Strategic Exposure Frontier research utilities."""

from .majority import majority_success_probability
from .frontier import upper_envelope, joint_frontier

__all__ = ["majority_success_probability", "upper_envelope", "joint_frontier"]
