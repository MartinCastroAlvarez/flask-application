# Requirements

### Security Requirements
* Safe methods are publicly available, no authentication is required.
* Unsafe methods are only available to authenticated users.

### Normalization Requirements
- Movie documents must include references or full documents to persons in their different roles.
- Person documents must include references or full documents to movies in the different roles the Person has.
- Justification of chosen libraries/frameworks against other popular choices.

### Business Requirements
* Movie documents must include the Release Year in roman numerals. This field should not be stored in the DB, just calculated on the fly.

### Deployment Requirements
* Project is deployed and running online (AWS, Heroku, cloud servers, own servers…)

### Interface Requirements
* User interface to browse items.
* User interface to create/edit/delete items.
