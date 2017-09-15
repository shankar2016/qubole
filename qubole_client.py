# qubole_client.py
# Natarajan Shankar

# This program is free software: you can redistribute it and/or modify it

# This program is distributed in the hope that it will be useful,
# it is only intended as a template for a qubole python client, and is
# provided WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

# JPype allows Python programs to have access to Java class libraries 
# through interfacing at the native level in both virtual machines.
import jpype

# Allows Python code to connect to databases using Java JDBC
import jaydebeapi

# UPDATE only the API key, a username can be left blank ("").
USERNAME = ""
PASSWORD = "API_KEY"

# DOWNLOAD THE QUBOLE PROVIDED QuboleJDBCxx.jar file
# Assuming that it has been downloaded to the /Users/<username>/Downloads directory
# Set the classpath to point to the classes that are needed to connect to Qubole 
classpath="$CLASSPATH:/Users/<username>/Downloads/QuboleJDBC41.jar"

# Get the path to a Java runtime installation
jvm_path=jpype.getDefaultJVMPath()

# Start the JVM, if it is not already running
if not jpype.isJVMStarted():
    jpype.startJVM(jvm_path, "-Djava.class.path=%s" % classpath)

# now include the Qubole specific Java driver class
driver = 'com/qubole/jdbc/jdbc41/core/QDriver'

# Connect to the Presto database
conn = jaydebeapi.connect(driver, "jdbc:qubole://presto/Presto/default?endpoint=https://azure.qubole.com", {"user" : USERNAME, "password" : PASSWORD}) 

# Ensure that connection non-NULL
conn

# Once a Connection has been established, a Cursor object must be instantiated and call 
# its execute() method to perform SQL commands
cursor = conn.cursor()

# Check that the Curor object is not NULL
cursor

# Now, perform a sample SQL command
# ** NOTE - The first time around, a response from cursor.execute takes about a minute
# as the cluster needs to be brought up and made functional
cursor.execute("show tables")
cursor.fetchall()

# When done, sshut down the JVM
if jpype.isJVMStarted():
    jpype.shutdownJVM() 
