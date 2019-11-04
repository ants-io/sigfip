# User detail plan.

## Data model

```javascript
const model = {
  tabs: {
    titles: [],
    isActive: false
  },
  user: {
    first_name: null,
    last_name: null,
    birth_date: null,
    birth_place: null,
    sex: null,
    registration_number: null,
    registration_date: null,
    cni: null,
    address: null,
    postal_box: null,
    phone: null,
    grade: {},
    ministry: {},
    paying_org: {}
  },
  salary: {
    id: null,
    kind: null,
    amount: null,
    change_at: null
  },
  salaries: [],
  showUserForm: false,
  showSalaryForm: false
};
```

## View Functions

view

- TabView

  - TabTitleView
  - TabContentView

- FormView
  - FieldSet
  - ButtonSet
- UserFormView
- SalaryFormView
- RequestFormView

- TableView
  - TableHeader
  - TableBody
    - Row
      - Cell
- UserTableView
- SalaryTableView

## Middlewares / Interactions

Functions called when interraction happen in the app.

- [ ] click add salary.
- [ ] fields in salary form.
- [ ] click save(add, update) salary.
- [ ] click delete salary.
- [ ] fields in user form.
- [ ] click save(update) user.
