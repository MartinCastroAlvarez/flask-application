# QA Tests
You can execute these tests in order to test the application end-to-end.
However, you should first execute [this](./README.md) instructions.

### Setup
Make sure you executed the steps described [here](./INSTALL.md).
This setup is required for all types of functional tests.

##### Environment
If running in the development environment:
```
export API="http://0.0.0.0:5000"
```
If running in the production environment:
```
export API="https://maria.martincastroalvarez.com"
```
These variables are commont for all cases:
```
COOKIE_JAR="/tmp/maria.jar"
ADMIN_USERNAME="admin"
ADMIN_PASSWORD="admin"
```

### Misc Tests

##### Health Check Test
```
curl -X GET "${API}/health"
```
Should return:
```
{
  "status": "alive"
}
```

### Authentication Tests
Due to the importance of security testing, it has been moved to a different document [here](./SECURITY.md).
However, you need to follow those instructions in order to generate a cookie jar. Otherwise, you won't be able to access the protected methods.

### People Tests

##### Empty People List Test
```
curl -b "${COOKIE_JAR}" -X GET "${API}/api/v1/people?page=1&limit=1"
```
Should return:
```
{
  "people": []
}
```

##### Person Creation Test
```
curl -b "${COOKIE_JAR}" -X POST "${API}/api/v1/people" -H "Content-Type: application/json" -d '{"first_name": "person1", "last_name": "person1", "aliases": ["test+'$(date +%s)'@test.com"]}'
```
Should return:
```
{
  "person": {
    "aliases": [
      "test+1560147154@test.com"
    ], 
    "created_at": "2019-06-10 06:12:34.207946", 
    "first_name": "person1", 
    "id": 16, 
    "is_active": true, 
    "last_name": "person1", 
    "movies": {
      "actor": [], 
      "director": [], 
      "producer": []
    }
  }
}
```

##### Person Update Test
```
curl -b "${COOKIE_JAR}" -X PUT "${API}/api/v1/people/1" -H "Content-Type: application/json" -d '{"first_name": "updated_'$(date +%s)'", "last_name": "updated_'$(date +%s)'", "aliases": ["test+'$(date +%s)'+1@test.com", "test+'$(date +%s)'+2@test.com"]}'
```
Should return:
```
{
  "person": {
    "aliases": [
      "test+1560147219@test.com",
      "test+1560147221@test.com",
      "test+1560147281+1@test.com",
      "test+1560147281+2@test.com"
    ],
    "created_at": "2019-06-10 06:07:54.629900",
    "first_name": "updated_1560147281",
    "id": 1,
    "is_active": true,
    "last_name": "updated_1560147281",
    "movies": {
      "actor": [],
      "director": [],
      "producer": []
    }
  }
}
```

##### Person Details Test
```
curl -b "${COOKIE_JAR}" -X GET "${API}/api/v1/people/1"
```
Should return:
```
{
  "person": {
    "aliases": [
      "test+1560147219@test.com",
      "test+1560147221@test.com",
      "test+1560147281+1@test.com",
      "test+1560147281+2@test.com"
    ],
    "created_at": "2019-06-10 06:07:54.629900",
    "first_name": "updated_1560147281",
    "id": 1,
    "is_active": true,
    "last_name": "updated_1560147281",
    "movies": {
      "actor": [],
      "director": [],
      "producer": []
    }
  }
}
```

##### Person Deletion Test
```
curl -b "${COOKIE_JAR}" -X DELETE "${API}/api/v1/people/1"
```
Should return:
```
{
  "person": {
    "aliases": [
      "test+1560147219@test.com",
      "test+1560147221@test.com",
      "test+1560147281+1@test.com",
      "test+1560147281+2@test.com"
    ],
    "created_at": "2019-06-10 06:07:54.629900",
    "first_name": "updated_1560147281",
    "id": 1,
    "is_active": false,
    "last_name": "updated_1560147281",
    "movies": {
      "actor": [],
      "director": [],
      "producer": []
    }
  }
}
```

##### Non-Empty People List Test
```
curl -b "${COOKIE_JAR}" -X GET "${API}/api/v1/people"
```
Should return:
```
{
  "people": [
    {
      "aliases": [],
      "created_at": "2019-06-10 06:08:34.842469",
      "first_name": "person1",
      "id": 2,
      "is_active": true,
      "last_name": "person1",
      "movies": {
        "actor": [],
        "director": [],
        "producer": []
      }
    }
  ]
}
```

### Movie Tests

##### Empty Movie List Test
```
curl -b "${COOKIE_JAR}" -X GET "${API}/api/v1/movies?limit=10"
```
Should return:
```
{
  "movies": []
}
```

##### Movie Creation Test
```
curl -b "${COOKIE_JAR}" -X POST "${API}/api/v1/movies" -H "Content-Type: application/json" -d '{"title": "movie1", "released_at": "2019-01-01", "aliases": ["test+'$(date +%s)'@test.com"]}'
```
Should return:
```
{
  "movie": {
    "actors": [],
    "created_at": "2019-06-10 07:01:54.162923",
    "directors": [],
    "id": 12,
    "is_active": true,
    "producers": [],
    "released_at": {
      "date": "2019-01-01",
      "roman": "MMXIX",
      "year": 2019
    },
    "title": "movie1"
  }
}
```

##### Movie Update Test
```
curl -b "${COOKIE_JAR}" -X PUT "${API}/api/v1/movies/1" -H "Content-Type: application/json" -d '{"title": "updated_'$(date +%s)'", "released_at": "2019-10-10", "aliases": ["test+'$(date +%s)'+1@test.com", "test+'$(date +%s)'+2@test.com"]}'
```
Should return:
```
{
  "movie": {
    "actors": [],
    "created_at": "2019-06-10 06:51:14.308844",
    "directors": [],
    "id": 1,
    "is_active": true,
    "producers": [],
    "released_at": {
      "date": "2019-10-10",
      "roman": "MMXIX",
      "year": 2019
    },
    "title": "updated_1560150133"
  }
}
```

##### Movie Details Test
```
curl -b "${COOKIE_JAR}" -X GET "${API}/api/v1/movies/1"
```
Should return:
```
{
  "movie": {
    "actors": [],
    "created_at": "2019-06-10 06:51:14.308844",
    "directors": [],
    "id": 1,
    "is_active": true,
    "producers": [],
    "released_at": {
      "date": "2019-10-10",
      "roman": "MMXIX",
      "year": 2019
    },
    "title": "updated_1560150133"
  }
}
```

##### Movie Deletion Test
```
curl -b "${COOKIE_JAR}" -X DELETE "${API}/api/v1/movies/1"
```
Should return:
```
{
  "movie": {
    "actors": [], 
    "created_at": "2019-06-10 06:51:14.308844", 
    "directors": [], 
    "id": 1, 
    "is_active": false, 
    "producers": [], 
    "released_at": {
      "date": "2019-10-10", 
      "roman": "MMXIX", 
      "year": 2019
    }, 
    "title": "updated_1560150133"
  }
}
```

##### Non-Empty Movies List Test
```
curl -b "${COOKIE_JAR}" -X GET "${API}/api/v1/movies?page=1&limit=1"
```
Should return:
```
{
  "movies": [
    {
      "actors": [],
      "created_at": "2019-06-10 06:51:49.157337",
      "directors": [],
      "id": 2,
      "is_active": true,
      "producers": [],
      "released_at": {
        "date": "2019-01-01",
        "roman": "MMXIX",
        "year": 2019
      },
      "title": "movie1"
    }
  ]
}
```

### Roles Tests

##### Adding Actor to Movie
```
curl -b "${COOKIE_JAR}" -X POST "${API}/api/v1/people/2/movies/actors/2"
```
Should return:
```
{
  "movie": {
    "actors": [
      {
        "aliases": [], 
        "created_at": "2019-06-10 06:08:34.842469", 
        "first_name": "person1", 
        "id": 2, 
        "is_active": true, 
        "last_name": "person1", 
        "movies": {
          "actor": [
            {
              "created_at": "2019-06-10 06:51:49.157337", 
              "id": 2, 
              "is_active": true, 
              "released_at": {
                "date": "2019-01-01", 
                "roman": "MMXIX", 
                "year": 2019
              }, 
              "title": "movie1"
            }
          ], 
          "director": [], 
          "producer": []
        }
      }
    ], 
    "created_at": "2019-06-10 06:51:49.157337", 
    "directors": [], 
    "id": 2, 
    "is_active": true, 
    "producers": [], 
    "released_at": {
      "date": "2019-01-01", 
      "roman": "MMXIX", 
      "year": 2019
    }, 
    "title": "movie1"
  }, 
  "person": {
    "aliases": [], 
    "created_at": "2019-06-10 06:08:34.842469", 
    "first_name": "person1", 
    "id": 2, 
    "is_active": true, 
    "last_name": "person1", 
    "movies": {
      "actor": [
        {
          "created_at": "2019-06-10 06:51:49.157337", 
          "id": 2, 
          "is_active": true, 
          "released_at": {
            "date": "2019-01-01", 
            "roman": "MMXIX", 
            "year": 2019
          }, 
          "title": "movie1"
        }
      ], 
      "director": [], 
      "producer": []
    }
  }
}
```

##### Deleting Actor from Movie
```
curl -b "${COOKIE_JAR}" -X DELETE "${API}/api/v1/people/2/movies/actors/2"
```
Should return:
```
{
  "movie": {
    "actors": [],
    "created_at": "2019-06-10 06:51:49.157337",
    "directors": [],
    "id": 2,
    "is_active": true,
    "producers": [],
    "released_at": {
      "date": "2019-01-01",
      "roman": "MMXIX",
      "year": 2019
    },
    "title": "movie1"
  },
  "person": {
    "aliases": [],
    "created_at": "2019-06-10 06:08:34.842469",
    "first_name": "person1",
    "id": 2,
    "is_active": true,
    "last_name": "person1",
    "movies": {
      "actor": [],
      "director": [],
      "producer": []
    }
  }
}
```

##### Adding Director to Movie
```
curl -b "${COOKIE_JAR}" -X POST "${API}/api/v1/people/2/movies/directors/2"
```
Should return:
```
{
  "movie": {
    "actors": [], 
    "created_at": "2019-06-10 06:51:49.157337", 
    "directors": [], 
    "id": 2, 
    "is_active": true, 
    "producers": [
      {
        "aliases": [], 
        "created_at": "2019-06-10 06:08:34.842469", 
        "first_name": "person1", 
        "id": 2, 
        "is_active": true, 
        "last_name": "person1", 
        "movies": {
          "actor": [], 
          "director": [
            {
              "created_at": "2019-06-10 06:51:49.157337", 
              "id": 2, 
              "is_active": true, 
              "released_at": {
                "date": "2019-01-01", 
                "roman": "MMXIX", 
                "year": 2019
              }, 
              "title": "movie1"
            }
          ], 
          "producer": []
        }
      }
    ], 
    "released_at": {
      "date": "2019-01-01", 
      "roman": "MMXIX", 
      "year": 2019
    }, 
    "title": "movie1"
  }, 
  "person": {
    "aliases": [], 
    "created_at": "2019-06-10 06:08:34.842469", 
    "first_name": "person1", 
    "id": 2, 
    "is_active": true, 
    "last_name": "person1", 
    "movies": {
      "actor": [], 
      "director": [
        {
          "created_at": "2019-06-10 06:51:49.157337", 
          "id": 2, 
          "is_active": true, 
          "released_at": {
            "date": "2019-01-01", 
            "roman": "MMXIX", 
            "year": 2019
          }, 
          "title": "movie1"
        }
      ], 
      "producer": []
    }
  }
}
```

##### Deleting Director from Movie
```
curl -b "${COOKIE_JAR}" -X DELETE "${API}/api/v1/people/2/movies/directors/2"
```
Should return:
```
{
  "movie": {
    "actors": [],
    "created_at": "2019-06-10 06:51:49.157337",
    "directors": [],
    "id": 2,
    "is_active": true,
    "producers": [],
    "released_at": {
      "date": "2019-01-01",
      "roman": "MMXIX",
      "year": 2019
    },
    "title": "movie1"
  },
  "person": {
    "aliases": [],
    "created_at": "2019-06-10 06:08:34.842469",
    "first_name": "person1",
    "id": 2,
    "is_active": true,
    "last_name": "person1",
    "movies": {
      "actor": [],
      "director": [],
      "producer": []
    }
  }
}
```

##### Adding Producer to Movie
```
curl -b "${COOKIE_JAR}" -X POST "${API}/api/v1/people/2/movies/producers/2"
```
Should return:
```
{
  "movie": {
    "actors": [],
    "created_at": "2019-06-10 06:51:49.157337",
    "producers": [
      {
        "aliases": [],
        "created_at": "2019-06-10 06:08:34.842469",
        "first_name": "person1",
        "id": 2,
        "is_active": true,
        "last_name": "person1",
        "movies": {
          "actor": [],
          "director": [],
          "producer": [
            {
              "created_at": "2019-06-10 06:51:49.157337",
              "id": 2,
              "is_active": true,
              "released_at": {
                "date": "2019-01-01",
                "roman": "MMXIX",
                "year": 2019
              },
              "title": "movie1"
            }
          ]
        }
      }
    ],
    "id": 2,
    "is_active": true,
    "producers": [],
    "released_at": {
      "date": "2019-01-01",
      "roman": "MMXIX",
      "year": 2019
    },
    "title": "movie1"
  },
  "person": {
    "aliases": [],
    "created_at": "2019-06-10 06:08:34.842469",
    "first_name": "person1",
    "id": 2,
    "is_active": true,
    "last_name": "person1",
    "movies": {
      "actor": [],
      "director": [],
      "producer": [
        {
          "created_at": "2019-06-10 06:51:49.157337",
          "id": 2,
          "is_active": true,
          "released_at": {
            "date": "2019-01-01",
            "roman": "MMXIX",
            "year": 2019
          },
          "title": "movie1"
        }
      ]
    }
  }
}
```

##### Deleting Producer from Movie
```
curl -b "${COOKIE_JAR}" -X DELETE "${API}/api/v1/people/2/movies/producers/2"
```
Should return:
```
{
  "movie": {
    "actors": [],
    "created_at": "2019-06-10 06:51:49.157337",
    "directors": [],
    "id": 2,
    "is_active": true,
    "producers": [],
    "released_at": {
      "date": "2019-01-01",
      "roman": "MMXIX",
      "year": 2019
    },
    "title": "movie1"
  },
  "person": {
    "aliases": [],
    "created_at": "2019-06-10 06:08:34.842469",
    "first_name": "person1",
    "id": 2,
    "is_active": true,
    "last_name": "person1",
    "movies": {
      "actor": [],
      "director": [],
      "producer": []
    }
  }
}
```
