
from arango import ArangoClient



class ArrangoStorage(object):

      def __init__(self, protocol, host, port, username, password, db, collection):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.db = db
        self.collection = collection
        self.protocol = protocol

      def connect(self):

        # Initialize the client for ArangoDB.
        #client = ArangoClient(protocol='http', host='localhost', port=8529)
        client = ArangoClient(protocol=self.protocol,
                              host=self.host, port=self.port)
        sys_db = client.db('_system', username=self.username,
                           password=self.password)

        # Create a new database named "test".
        sys_db.create_database(self.db)

        # Connect to "test" database as root user.
        database = client.db(self.db, username=self.username,
                             password=self.password)
        return database

      def store(self, database,data):
          # Connect to "_system" database as root user.

        # Create a new collection named "students".
        students = database.create_collection(self.collection)
        # Add a hash index to the collection.
        students.add_hash_index(fields=['name'], unique=True)

        # Insert new documents into the collection.
        print(data)
        students.insert(data)

        # Execute an AQL query and iterate through the result cursor.
        cursor = database.aql.execute('FOR doc IN students RETURN doc')
        student_names = [document['source'] for document in cursor]

        print(student_names)
