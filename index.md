## 概念解析
| SQL 术语 | MongoDB术语/概念 | 解释/说明 |
|----------|------------------|-----------|
|database| database | 数据库 |
| table | collection | 数据库表/集合 |
| row | document | 数据记录行/文档 |
| column | field | 数据字段/域 |
| index | index | 索引 |
| table joins | | 表链接, MongoDB不支持 |
| primary key | primary key | 主键, MongoDB自动将_id字段设置为主键 |
## 数据库
1. 显示所有数据库列表
```shell
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
```
2. 执行`db`命令可以显示当前数据库对象和集合
```shell
> db
config
```
3. 运行`use`命令可以连接到一个指定到数据库
```shell
> use local
switched to db local
> db
local
```
## 数据库命名规则
- 不能是空字符串
- 不得含有空格.$/\和\0
- 应全部小写
- 最多64字节
## 保留数据库
- admin: 从权限的角度来看，这是`root`数据库，要是将一个用户添加到这个数据库，这个用户自动继承所有数据库到权限。
        一些特定到服务端命令也只能从这个数据库运行，比如列出所有到数据库或者关闭服务器。
- local: 这个数据永远不会被复制，可以用了存储限于本地单台服务器到任意集合
- config: 当Mongo用于分片设置时， config数据库在内部使用，用于保存分片相关到信息。
## 文档(Document)
文档是一组键值对(key-value)(即BSON) 关系型数据库(RDBMS)和MongoDB的区别:

| RDBMS | MongoDB |
|-------|---------|
| 数据库 | 数据库 |
| 表格 | 集合 |
| 行 | 文档 |
| 列 | 字段 |
| 表联合 | 嵌入文档 |
| 主键 | 主键(MongoDB提供了key为_id) |

数据库服务端和客户端

| RDBMS | MongoDB |
|-------|---------|
| Mysqlq/Oracle | mongod |
| myslq/sqlplus | mongo |
### 注意:
1. 文档中的键/值对是有序的
2. 文档中的值不仅可以是双引号里的字符串，还可以是其他几种数据库(甚至可以是整个嵌入的文档)
3. MongoDB区分类型和大小写
4. MongoDB的文档不能有重复的键
5. 文档的键是字符串，出来少数例外的情况，键可以是任务utf-8字符

### 文档键命名规范:
- 键不能含有\0(空字符)，这个字符用来表示键的结尾
- .和$有特别的意义，只有在特定环境下才能使用
- 以下划线('_')开头的键是保留的(不是严格要求的)


## 集合

集合就是MongoDB文档组，类似于RDBMS(关系数据库管理系统:Relational Database Managerment System) 中的表格。
集合存在与数据库中，集合没有固定的结构，这意味着你可以在集合中插入不同格式和类型的数据，但是通常情况下我们插入集合的数据都会有一定的关联性。

### 合法的集合名
- 集合名不能是空字符串"".
- 集合名中不能宝航\0(空字符), 这个字符表示集合名的结尾。
- 集合名不能以"system"开头，这是为系统集合保留的前缀。
- 用户创建的集合名字不能哈有保留字符。

### capped collection
Caped collection就是固定大小的collection.
它有很高的**性能**和**队列过期**的特性(过期按照插入顺序)
非常适合日志的功能。你必须要显式的创建一个capped collection, 指定一个colleciton的大小，单位是字节。collection的数据
存储空间值是提前分配的。
#### 注意
- 在capped collection中，你能添加新的对象
- 能进行更新，然而，队形不会增加存储空间，如果增加，更新就会失败
- 使用Capped collection 不能删除一个文档，可以使用drop()方法删除collection所有的行
- 删除之后，你必须显式的重新创建这个collection
- 在32bit的机器中，capped collection最大存储为1e9个字节
## 元数据

数据库的信息是存储在集合中，它们使用了系统的名称空间:`dbname.system.*`
在MongoDB数据库中名字空间`<dbname>.system.*`是包含多种系统信息的特殊集合(collection),如下:

| 集合命名空间 | 描述 |
|--------------|------|
| dbname.system.namespace | 列出所有名字空间 |
| dbname.system.indexes | 列出所有索引 |
| dbname.system.profile | 包含数据库概要(profile)信息 |
| dbname.system.users | 列出所有可访问数据库的用户 |
| dbname.local.sources | 包含复制对端(slave)的服务器信息和状态 |

## MongoDB数据类型

| 数据类型 | 描述 |
|----------|------|
| String | 字符串， 存储数据常用类型，在MongoDB中，UTF-8编码的字符串才是合法的 |
| Integer | 整型数值，用于存储数值，根据你所采用的服务器，可分为32位和64位 |
| Boolean | 布尔值， 用于存储布尔值(真/假) |
| Double | 双精度浮点数，用于存储浮点值 |
| Min/Max keys | 将一个值与BSON(二进制的JSON)元素的最低值和最高值对比 |
| Array | 用于将数组或列表或多个值存储为一个键 |
| Timestamp | 时间戳, 记录文档修改/添加的具体时间 |
| Object | 用于内嵌文档 |
| Null | 用于创建空值 |
| Symbol | 符号，该数据类型基本上等同于字符串类型，但不同的是，他一般采用特殊符号类型的语言 |
| Date | 日期时间，用UNIX实际格式类存储当前日期和时间， 你可以指定自己的日期时间，创建Date队形，传入年月日信息。|
| Object ID | 对象ID, 用于创建文档的ID |
| Binary Data | 二进制数据， 用于存储二进制数据 |
| Code | 代码类型，用于在文档中存储JavaScript代码 |
| Regular expression | 正则表达式， 用于存储正则表达式 |
### ObjectId
ObjectId类似唯一主键，可以很快的去生成和排序，包含12bytes,含义如下:
- 前4个自己表示创建unix时间戳，格林尼治时间，比北京时间晚8个小时
- 接下来的3个字节是机器识别码
- 紧接着的2个字节由进程id组成PID
- 最后三个字节是随机数

MongoDB中存储的文档必须有一个`_id`键，这个键的值可以是任何类型的，默认是个ObjectId对象，
由于ObjectId中保存了创建的时间戳，所以你不需要为你的文档保存时间戳字段，你可以通过`getTimestamp`函数
来获取文档的创建时间:
```JavaScript
var newObject = ObjectId();
newObject.getTimestamp()
// ObjectId转换为字符串
newObject.str
```
## 创建MongoDB数据库
```shell
use DATABASE_NAME
```
### 实例
```shell
> use runoob
switched to db runoob
> db
runoob
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
```
我们创建完数据库后会发现`show dbs`命令并没有`runoob`命令，要显示他需要向`runoob`数据库中插入一些数据.
```shell
> db.runoob.insert({"name":"菜鸟教程"})
WriteResult({ "nInserted" : 1 })
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
runoob  0.000GB
```
**注意:在MongoDB中，集合只有在内容插入后才会创建，也就是说，创建集合后要再插入一个文档记录，集合才真正的创建**

## 删除数据库
语法:
```shell
db.dropDatabase()
```
### 实例
```shell
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
runoob  0.000GB
> db
runoob
> db.dropDatabase()
{ "dropped" : "runoob", "ok" : 1 }
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
> db
runoob
```
## 删除集合
语法:
```shell
do.collection.drop()
```
### 实例
```shell
> use runoob
switched to db runoob
> db.createCollection("runoob")
{ "ok" : 1 }
> show tables
runoob
> db.runoob.drop()
true
> show tables
>
```
## 创建集合
语法:
```shell
db.createCollection(name, options)
```
参数说明:
- name: 要创建的集合的名字
- options: 可选参数，指定有关内存大小及索引的选项

options参数:

| 字段 | 类型 | 描述 |
|------|------|------|
| capped | 布尔 | 如果为true ,则创建固定集合，固定集合是指有着固定大小的集合，当达到最大值时，他会自动覆盖最早的文档。|
| autoIndexed | 布尔 | 如果为true, 自动在_id自动创建索引，默认为false |
| size | 数值 | 为固定集合指定一个最大值(以字节计),如果capped为true,也需要指定该字段 |
| max | 数值 | 指定固定集合中包含文档的最大数量 |

### 实例
```shell
> use test
switched to db test
> db.createCollection("runoob")
{ "ok" : 1 }
> show collections
runoob
> show tables
runoob
> db.createCollection("mycol",{capped : true, autoIndexId: true, size : 6142800, max: 10000})
{
	"note" : "the autoIndexId option is deprecated and will be removed in a future release",
	"ok" : 1
}
> show tables
mycol
runoob
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
test    0.000GB
```
在MongoDB中，你不需要创建集合，当你插入文档时，MongoDB会自动创建集合:
```shell
> db.mycol2.insert({"name": "菜鸟教程"})
WriteResult({ "nInserted" : 1 })
> show tables
mycol
mycol2
runoob
```

## 删除集合
语法:
```shell
db.collection.drop()
```
### 实例
```shell
> show collections
mycol
mycol2
runoob
> db.mycol2.drop()
true
> show collections
mycol
runoob
```

## 插入文档
语法:
MongoDB中用`insert()`或`save()`方法向集合中插入文档:
```shell
db.COLLECITON_NAME.insert(document)
```
### 实例
```shell
> db.col.insert({title:'MongoDB 教程', description: 'MongoDB是一个Nosql数据库', by:'菜鸟教程', url:'http://www.runoob.com', tags:['mongodb','database','NoSQL'], likes:100})
WriteResult({ "nInserted" : 1 })
> db.col.find()
{ "_id" : ObjectId("5d598302de7bfb1757ed9e81"), "title" : "MongoDB 教程", "description" : "MongoDB是一个Nosql数据库", "by" : "菜鸟教程", "url" : "http://www.runoob.com", "tags" : [ "mongodb", "database", "NoSQL" ], "likes" : 100 }
```
```shell
> document = ({title:'MongoDB 教程', description: 'MongoDB是一个Nosql数据库',by: '菜鸟教程', url:'http://www.runoob.com', tags:['mongodb','database','NoSQL'],likes:100})
{
	"title" : "MongoDB 教程",
	"description" : "MongoDB是一个Nosql数据库",
	"by" : "菜鸟教程",
	"url" : "http://www.runoob.com",
	"tags" : [
		"mongodb",
		"database",
		"NoSQL"
	],
	"likes" : 100
}
> db.col.insert(document)
WriteResult({ "nInserted" : 1 })
> db.col.find()
{ "_id" : ObjectId("5d598302de7bfb1757ed9e81"), "title" : "MongoDB 教程", "description" : "MongoDB是一个Nosql数据库", "by" : "菜鸟教程", "url" : "http://www.runoob.com", "tags" : [ "mongodb", "database", "NoSQL" ], "likes" : 100 }
{ "_id" : ObjectId("5d5983aede7bfb1757ed9e82"), "title" : "MongoDB 教程", "description" : "MongoDB是一个Nosql数据库", "by" : "菜鸟教程", "url" : "http://www.runoob.com", "tags" : [ "mongodb", "database", "NoSQL" ], "likes" : 100 }
>
```
