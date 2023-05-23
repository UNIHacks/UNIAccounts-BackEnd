### **Recommended by Development Run use Docker Compose**
**Note:** Only need this commands by run project
Requirements
- [Docker Compose](https://docs.docker.com/compose/)
```bash
# Run and Build Docker Compose
docker-compose build
docker-compose up
```

### **Run Local DataBase With Docker**
```bash
# Run and Build Image with volumes
docker run -d -p 27017:27017 -v $ABS_ROUTE_OF_PROJECT/UNICA-ManagerAccounts-API/DB:/data/db --name database mongo
```

### **Run Server With Docker**

```bash
# Build Image
docker build -t unica-acounts-api .

#Run Image
docker run -it -p 7000:4000 unica-acounts-api
```