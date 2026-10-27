# Test Cases: Wikipedia Search

**Application under test:** https://en.wikipedia.org (desktop site)
**Feature:** Search field in the page header
**Automated in:** `tests/test_search.py` (each test name contains its TC id)

| ID    | Title                                         | Priority |
|-------|-----------------------------------------------|----------|
| TC-01 | Search for an existing article opens it       | High     |
| TC-02 | Search ignores lowercase first letter         | Medium   |
| TC-03 | Suggestions appear while typing               | Medium   |
| TC-04 | Search with no exact match shows result list  | High     |
| TC-05 | Nonsense search shows "no results" message    | Medium   |
| TC-06 | Script text in search is not executed         | High     |

---

### TC-01: Search for an existing article opens it

**Preconditions:** Wikipedia main page is open.

| Step | Action                                  | Expected result                                   |
|------|-----------------------------------------|---------------------------------------------------|
| 1    | Click the search field                  | Field is focused                                  |
| 2    | Type `Software testing`                 | Text appears in the field                         |
| 3    | Press Enter                             | The "Software testing" article opens (page title is "Software testing") |

### TC-02: Search ignores lowercase first letter

**Preconditions:** Wikipedia main page is open.

| Step | Action                                  | Expected result                                   |
|------|-----------------------------------------|---------------------------------------------------|
| 1    | Type `software testing` (all lowercase) | Text appears in the field                         |
| 2    | Press Enter                             | The same "Software testing" article opens         |

### TC-03: Suggestions appear while typing

**Preconditions:** Wikipedia main page is open.

| Step | Action                                  | Expected result                                   |
|------|-----------------------------------------|---------------------------------------------------|
| 1    | Type `Software test` (don't press Enter)| A suggestion list opens under the field           |
| 2    | Look at the suggestions                 | "Software testing" is one of the suggestions      |

### TC-04: Search with no exact match shows result list

**Preconditions:** Wikipedia main page is open.

| Step | Action                                  | Expected result                                   |
|------|-----------------------------------------|---------------------------------------------------|
| 1    | Type `automation testing tools`         | Text appears in the field                         |
| 2    | Press Enter                             | "Search results" page opens                       |
| 3    | Look at the results                     | At least one result is listed                     |

### TC-05: Nonsense search shows "no results" message

**Preconditions:** Wikipedia main page is open.

| Step | Action                                  | Expected result                                   |
|------|-----------------------------------------|---------------------------------------------------|
| 1    | Type `qwxzvbnm plokijuh`                | Text appears in the field                         |
| 2    | Press Enter                             | Page shows "There were no results matching the query." |

### TC-06: Script text in search is not executed (basic security check)

**Preconditions:** Wikipedia main page is open.

| Step | Action                                         | Expected result                            |
|------|------------------------------------------------|--------------------------------------------|
| 1    | Type `<script>alert('hi')</script>`            | Text appears in the field                  |
| 2    | Press Enter                                    | "Search results" page opens normally       |
| 3    | Watch for pop-ups                              | No alert pop-up appears                    |
