
# Func Flasker

## Overview
Creates a container that generates endpoints for Python functions for access by HTTP posts through Flask. The utility can parse multiple Python files containing one or more functions and generate a Flask app to expose the collected items, including their parameters, for consumption. 

```
                                          ┌──────────────────────┐          ┌─────────────┐
                                          │  Flask App Template  │          │ Docker File │
                                          │                      │          │             │
                                          │                      │          │             │
                                          │                      │          │             │
                                          └──────────┬───────────┘          │             │
                                                     │                      └──────┬──────┘
                                                     │                             │
                                                     │                             │
                                                     │                             │
                                                     ▼                             ▼
                                      ┌────────────────────────────┐       ┌───────────────┐
                                      │  Ansible Playbook          │       │    Podman     │
                                      │                            │       │               │
                                      │                            ├──────►│               │
                                      │                            │       │               │
                                      └───────────────────────┬────┘       │               │
       Directory                           ▲                  │            └───────┬───────┘
┌──────────────────────┐                   │                  │                    │
│    Function Files    │                   │                  │                    │
│                      │       ┌───────────┴──────┐           ▼                    ▼
│                      │       │ Function Parser  │     ┌─────────────┐    ┌──────────────┐
│                      ├──────►│                  │     │  Flask App  │    │  Container   │
│                      │       │                  │     │             │    │              │
│                      │       └──────────────────┘     └─────────────┘    │              │
│                      │                                                   │              │
└──────────────────────┘                                                   │              │
                                                                           └──────────────┘
```
## Prerequisites
- Python 3.8.6 or higher

## Running the utility
1. Place any functions you want to expose in ```flaskr/functions``` making sure that function names are unique across all the files. It's also recommended that these files only reference the functions being exposed. Helper or additional functions can be referenced by the files.

2. Launch the utility by running the Python script: ```get_the_funcs.py```. The script will parse all the scripts in ```flaskr/functions``` and extract all functions and parameters. These are then used to generate the main Flask file from the Jinja2 template which is then injected into a container along with the functions and anything else you want in the ```flaskr``` directory. 

Once complete, the container should be accessible by accessing port ```5000``` on the host or the container directly. As configured, the utility will expose the application to all interfaces on the host. This can be changes by modifying the Dockerfile entrypoint. 

# Changelog
## v0.0
- Initial release

## v0.1
- Minor cleanup
- Removed unused files
- Removed unused variables

## v0.1.1
- Added TODOs to README file
- Added crates to sample functions

## v0.2
- Separated ansible scripts from python scripts
- Flask app generated through jinja template from python script

# TODO's
- Parse scripts for library imports
- Replace POST form requests with json
- Storing static variable for service