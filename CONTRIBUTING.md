# Contributing

Thanks for helping improve this list. The goal is to keep it useful, concise, and easy to verify.

## Dataset Entry Format

Use this structure for new entries:

```markdown
### [Dataset Name](https://official-source.example) (ABBR)

One or two sentences describing what the dataset contains and why it is useful for time-series anomaly detection.

- Access: open, request required, login required, or restricted license.
- Domain: short domain description.
- Publication: [Paper title](https://paper.example).
- Repository: [owner/repo](https://github.com/owner/repo).
- **Benchmark caveat:** concise, sourced limitation on benchmark interpretation.
```

Only include the fields that apply. Prefer official dataset pages, archival records, and maintained repositories over mirrors. Use the benchmark-caveat field only for a documented limitation, and link the supporting publication or maintainer note.

## Review Checklist

- The dataset has temporal structure or is widely used as a time-series anomaly/event/fault benchmark.
- The link points to an official source, archival record, or clearly maintained repository.
- Access requirements are stated honestly.
- The description is factual and does not overstate benchmark quality.
- Published benchmark-quality concerns are summarized without turning them into unsupported quality ratings.
- Publications, repositories, and mirrors are labeled as such.
- The entry keeps the **Benchmark caveat** marker and other formatting consistent with the README.

## Scope

Related datasets are welcome when they are useful for rare-event, fraud, event, or fault-detection experiments, but direct anomaly-detection datasets and benchmark collections should be prioritized.
