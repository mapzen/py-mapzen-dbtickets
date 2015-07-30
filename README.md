# py-mapzen-dbtickets

Simple Python wrapper for talking to a (MySQL derived) ticket server.

## Usage

### Simple

```
$> python
>>> import mapzen.dbtickets
hosts = [{ 'user': 'dbtickets', 'database': 'dbtickets', 'host': 'localhost', 'password': '****'}]
>>> t = mapzen.dbtickets.dbtickets(*hosts)
>>> t.generate_id()
13
>>> t.generate_id()
15
>>> t.generate_id()
17
>>> t.generate_id()
19
```

Under the hood py-mapzen-dbtickets uses the `mysql.connection` library so the arguments you pass in each host config are the same to mysql.connection.

### Fancier

Some default values are provided for each host config. They are: 

* username: `dbtickets`
* database: `dbtickets`
* host: `localhost`

So you might also write something like this:

```
$> python
>>> import mapzen.dbtickets
>>> hosts = [{ 'password': '***'}]
>>> t = mapzen.dbtickets.dbtickets(*hosts)
>>> t.generate_id()
21
```

### Fiddly

Setting up and [configuring the
database](https://code.flickr.net/2010/02/08/ticket-servers-distributed-unique-primary-keys-on-the-cheap/)
is outside the scope of this document. The setup assumes that you are
able to change the default `auto-increment-increment` and
`auto-increment-offset` values in MySQL.

If you are not able to you to do this yourself (because you don't have
suitable permissions to alter your database or whatever) you can also
specify a `set_auto_increment` flag in your object constructor.

Doing so will tell the library to explicitly set the database's
variables using MySQL's built-in `SET` command. This will incur extra
database commands for each connection but the measure of that cost is
left up to you.

```
import mapzen.dbtickets
hosts = [{ 'password': '***'}]
t = mapzen.dbtickets.dbtickets(*hosts, set_auto_increment=True)
print t.generate_id()
```

## Caveats

* The `setup.py` and dependency stuff is still not finished.

## See also

* https://code.flickr.net/2010/02/08/ticket-servers-distributed-unique-primary-keys-on-the-cheap/