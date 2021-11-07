# Super-rent

This is a system that designed for the people who need the rent management(Actually it's just for my-self🤪).

## Authority

for the customer, it has three different dimensions of permissions： `admin`, `owner`, and `contractor`
we can see it in `/backend/common/schemas.py(class UserAuthority)`

### for the Admin

it is the highest level of authority, In this current design(it's mean that it just use by myself), it can operate all `unit-rent` in the system.

### for the owner

it is the owner of the `unit-rent`,it can only operate the `unit-rent` under his name. in addition, he can assign `contractor` to help him manage his rental units. 

### for the contractor

it is the lowest level of authority, it can only operate the part of the tenant. And each `contractor` must be under a `owner`

