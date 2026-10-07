# Processing Flow

```text
                    Incoming CSV
                         |
                         v
                    Landing Zone
                         |
                         v
                    Read / Parse
                         |
                         v
                  Duplicate Check
                         |
              +----------+----------+
              |                     |
            FAIL                   PASS
              |                     |
              v                     v
          Rejected             Date Validation
                                    |
                             +------+------+
                             |             |
                           FAIL          PASS
                             |             |
                             v             v
                         Rejected       Staging
                                           |
                                           v
                                      Delta Table
```

The complete file is accepted only when all mandatory validation checks pass.
