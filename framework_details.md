## Key Questions

- How often do models produce outputs that are syntactically correct but semantically misaligned with user intent or policy?
- What patterns emerge in these failures across different prompt types (ambiguous, adversarial, underspecified)?
- How do taxonomy design and guideline ambiguity contribute to misclassification and alignment drift?
- Can evaluation methods reliably detect these failures at scale?
  
## Focus Areas
- Meaning drift
- Instruction misinterpretation
- Boundary instability
- Over-refusal / under-refusal

## Motivation
In production environments, many failures are not obvious errors. Outputs may be technically correct while gradually diverging from intended meaning due to:
- Weak or ambiguous taxonomies
- Limited audit coverage
- Incentives favoring throughput over discernment

This work focuses on identifying and making these failure modes more legible so they can be addressed before they scale.

## Approach

This project takes a small-scale, exploratory approach to identifying meaning-level failures:

- Construct targeted prompts designed to induce subtle misalignment
- Apply a simple rubric to distinguish surface correctness from semantic fidelity
- Organize failures into categories that reflect evaluation blind spots
- Analyze how these failures would be missed in typical evaluation pipelines
  
## Notes
This is an exploratory project based on practical experience in high-volume AI evaluation environments.
