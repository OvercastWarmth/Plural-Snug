# Plural-Snug

A python program to manage plural system information locally (with syncing to popular online systems as well)

NOTE: this is in no way done yet, you can technically use it if you want but it's probably not user friendly, and things are likely to change.

## Usage

Configuration is done through a `config.json` file, like this example here:

```json5
{
    "database": "C:/PluralSnug-Database", // Path to your database (can be relative but not recommended)
    "PluralKit": {
        "token": "TOKEN" // Your token from pk;token. DO NOT SHARE THIS WITH ANYONE!
    }
}
```
