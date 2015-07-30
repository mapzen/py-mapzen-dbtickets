# py-mapzen-dbtickets

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

## See also

* https://code.flickr.net/2010/02/08/ticket-servers-distributed-unique-primary-keys-on-the-cheap/