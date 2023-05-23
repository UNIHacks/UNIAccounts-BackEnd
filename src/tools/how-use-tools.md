# **How Use the Tools of API**

## **Encrypt and Decrypt ENVS.py**

```bash
# From root dir of project
# To Encrypt file
python3 tools/encrypt_env.py src/ENVS.py <key>

# To Decrypt file
python3 tools/decrypt_env.py src/ENVS.py.encrypted <key>
```

### Example
```bash
# From root dir of project
# To Encrypt file
python3 tools/encrypt_env.py src/ENVS.py passwoR0

# To Decrypt file
python3 tools/decrypt_env.py src/ENVS.py.encrypted passwoR0
```

## **Generate Markdown file with API docs**

```bash
# From root dir of project
python3 tools/generate_docs.py <version_api> <type_output> # only only works with markdown
```

### Example
```bash
# From root dir of project
python3 tools/generate_docs.py v1 md
```
