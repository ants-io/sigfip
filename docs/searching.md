# Searching Design Doc

## Model

```ts
interface User {
  id: number,
  number_registration: string,
  first_name: string,
  last_name: string,
  loan_amount: number,
  date_depot: date,
  age:number,
  retired_age:number,
  current_loan_amount: number,
  remaining_loan_amount: number,
  requis: number,
  difference:number
}

interface Loan {
  id: number,
  submission_date: number,
  number_registration: string,
  name: string,
  branch: string,
  state: string,
  amount: number
}

interface Profession {
  id: number,
  name: string
}

interface Branch {
  id: number,
  name: string
}

interface Grade {
  id: number,
  name: string
}

interface Ministry {
  id: number,
  name: string
}

interface PayingOrg {
  id: number,
  name: string
}

const Model = {
  search: {
    query: string,
    dateIntervals: string,
    category: string,
    age: {
      before: number,
      after: number
    },
    submit_date: {
      before: number,
      after: number,
    },
    proceed_date: {
      before: number,
      after: number,
    },
    status: string[],
    professionsId: number[],
    branchIds: number[],
    gradeIds: number[],
    ministryIds: number[],
    payingOrgIds: number[]
  },
  users: User[],
  loans: Loan[],
  professions: Profession[],
  branches: Branch[],
  grades: Grade[],
  ministries: Ministry[],
  payingOrgs: PayingOrg[],
};
```

## Components

```jsx
- <Content>
  - <SearchView />
    - <TextInput name='query' onMoreOptions={this.hanldeMoreOptions} />
    - <DateInput name='dateIntervals' />
    - <SelectInput name='category' />

  - <UsersTableView users={users}/>
  - <LoanTableView loans={loans} />
  - <FilterView
      searchParams={{
        age: {
          before: null,
          after: null
        },
        submit_date: {
          before: null,
          after: null,
        },
        proceed_date: {
          before: null,
          after: null,
        },
        status: [],
        professionsId: [],
        branchIds: [],
        gradeIds: [],
        ministryIds: [],
        payingOrgIds: []
      }}
      onChange={handleOnChange}
    >
</Content>
```

## Reducer Actions

```js
export enum ActionsConstant = {
  SET_SEARCH_QUERY = 'SET_SEARCH_QUERY',
  SET_MORE_OPTIONS = 'SET_MORE_OPTIONS',
  SET_SELECTED_DATES_INTERVALS = 'SET_SELECTED_DATES_INTERVALS',
  SET_SELECTED_CATEGORY = 'SET_SELECTED_CATEGORY',
  SET_FILTER_PARAMS = 'SET_FILTER_PARAMS',
}

const setSearchQuery = (query: string) =>
  action(ActionsConstant.SET_SEARCH_QUERY, { query });

const setMoreOptions = (query: string) =>
  action(ActionsConstant.SET_MORE_OPTIONS, { query });

const setSelectedDatesIntervals = (dates: string[]) =>
  action(ActionsConstant.SET_SELECTED_DATES_INTERVALS, { dates });

const setSelectCategory = (category: string) =>
  action(ActionsConstant.SET_SELECTED_CATEGORY, { category });

const setFilterParams = (params: any) =>
  action(ActionsConstant.SET_FILTER_PARAMS, { params });
```
