# Task 4 — EvidenceIQ Pipeline

The pipeline of the EvidenceIQ system is:

Document
   ↓
Claim
   ↓
Evidence
   ↓
Relationship
   ↓
Verification
   ↓
Report

## 1. Document

A document is the original information that we want to investigate.

It can be a research paper, news article, webpage, image, audio, or
video. The document contains information from which claims can be
identified.

## 2. Claim

A claim is a factual statement extracted from a document that can be
checked or verified.

A single document can contain multiple claims. The system treats each
claim separately so that each statement can be investigated.

For example:

Document:
"Electric vehicles generally produce lower lifetime greenhouse gas
emissions than comparable gasoline vehicles."

Claim:
"Electric vehicles produce fewer lifetime greenhouse gas emissions
than comparable gasoline vehicles."

## 3. Evidence

Evidence is information collected from sources that helps determine
whether a claim is true or false.

Evidence can support a claim or contradict a claim. One claim can have
evidence from multiple sources.

For example:

Claim
  ↓
Evidence 1 → Source 1
Evidence 2 → Source 2
Evidence 3 → Source 3

## 4. Relationship

The relationship connects a claim with the evidence and sources that
are relevant to that claim.

It helps us understand how the evidence relates to the claim, such as
whether the evidence supports or contradicts the claim.

For example:

Claim
  ├── supported by → Evidence 1
  ├── supported by → Evidence 2
  └── contradicted by → Evidence 3

## 5. Verification

Verification uses the claim, evidence, and their relationships to
determine the result of the claim.

The verification produces a verdict, confidence score, and explanation.

The possible verdicts in our model are:

- Supported
- Contradicted
- Mixed
- Insufficient

For example:

Verdict: Supported
Confidence: 0.92

The explanation describes why the system reached that verdict.

## 6. Report

The report presents the verification results in a clear format for
the user.

It can contain:

- The original claim
- Relevant evidence
- Sources
- Verification verdict
- Confidence score
- Explanation

The purpose of the report is to make the verification result
understandable and show the evidence behind the conclusion.