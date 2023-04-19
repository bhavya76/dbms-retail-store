-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: flipmart
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `Username` varchar(255) DEFAULT NULL,
  `Pass_word` varchar(255) DEFAULT NULL,
  `Pincode` int DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `Username` (`Username`),
  KEY `Pincode` (`Pincode`),
  CONSTRAINT `admin_ibfk_1` FOREIGN KEY (`Pincode`) REFERENCES `branch` (`Pincode`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'Martina','Dunlap',860000),(2,'Rodolph','Rene',751554),(3,'Blakeley','Antyukhin',404434),(4,'Mathew','Olpin',851978),(5,'Magda','Tytterton',441113),(6,'Xaviera','Rowes',863622),(7,'Jeane','McTavy',312554),(8,'Heath','Giercke',543807),(9,'Lorine','Karpychev',952970),(10,'Griffie','Srutton',152737),(11,'Tymothy','Szabo',356345),(12,'Kitty','Albery',336837),(13,'Byrann','Bend',213308),(14,'Dilan','Scollard',219977),(15,'Axe','Fortun',185797),(16,'Lotta','Mouatt',389412),(17,'Charlot','Janos',596998),(18,'Jeni','Destouche',318378),(19,'Kurtis','Grassett',437261),(20,'Sandor','Beharrell',267157),(21,'Storm','Hardington',656107),(22,'Lennie','Ripsher',359084),(23,'Cathrin','Guerner',293448),(24,'Ginevra','Linguard',681439),(25,'Gene','Borghese',823220);
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `available`
--

DROP TABLE IF EXISTS `available`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `available` (
  `pincode` int NOT NULL,
  `product_id` varchar(5) NOT NULL,
  `quantity` int DEFAULT NULL,
  PRIMARY KEY (`pincode`,`product_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `available_ibfk_1` FOREIGN KEY (`pincode`) REFERENCES `branch` (`Pincode`),
  CONSTRAINT `available_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `available`
--

LOCK TABLES `available` WRITE;
/*!40000 ALTER TABLE `available` DISABLE KEYS */;
INSERT INTO `available` VALUES (152737,'10',200),(152737,'23',100),(152737,'30',200),(152737,'35',200),(152737,'37',200),(152737,'40',200),(152737,'42',200),(152737,'53',200),(152737,'60',200),(152737,'63',94),(152737,'85',200),(185797,'15',902),(185797,'40',474),(185797,'65',328),(185797,'90',697),(213308,'13',153),(213308,'38',634),(213308,'63',35),(213308,'88',170),(219977,'14',886),(219977,'39',952),(219977,'64',151),(219977,'89',460),(267157,'20',903),(267157,'45',547),(267157,'70',506),(267157,'95',148),(293448,'23',602),(293448,'48',95),(293448,'73',55),(293448,'98',449),(312554,'32',639),(312554,'57',536),(312554,'7',457),(312554,'82',765),(318378,'18',428),(318378,'43',758),(318378,'68',310),(318378,'93',601),(336837,'12',622),(336837,'37',762),(336837,'62',498),(336837,'87',696),(356345,'11',712),(356345,'36',47),(356345,'61',46),(356345,'86',765),(359084,'22',327),(359084,'47',857),(359084,'72',544),(359084,'97',528),(389412,'16',299),(389412,'41',668),(389412,'66',996),(389412,'91',186),(404434,'28',740),(404434,'3',22),(404434,'53',120),(404434,'78',108),(437261,'19',754),(437261,'44',381),(437261,'69',111),(437261,'94',449),(441113,'30',529),(441113,'5',367),(441113,'55',230),(441113,'80',728),(543807,'33',381),(543807,'58',638),(543807,'8',770),(543807,'83',858),(596998,'17',585),(596998,'42',360),(596998,'67',436),(596998,'92',138),(656107,'21',198),(656107,'46',876),(656107,'71',299),(656107,'96',869),(681439,'24',161),(681439,'49',430),(681439,'74',372),(681439,'99',28),(751554,'2',163),(751554,'27',159),(751554,'52',132),(751554,'77',83),(823220,'100',950),(823220,'25',337),(823220,'50',493),(823220,'75',533),(851978,'29',519),(851978,'4',387),(851978,'54',209),(851978,'79',986),(860000,'1',162),(860000,'26',41),(860000,'51',888),(860000,'76',826),(863622,'31',753),(863622,'56',298),(863622,'6',106),(863622,'81',838),(952970,'34',892),(952970,'59',372),(952970,'84',151),(952970,'9',91);
/*!40000 ALTER TABLE `available` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `branch`
--

DROP TABLE IF EXISTS `branch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `branch` (
  `area` varchar(255) DEFAULT 'Okhla',
  `Pincode` int NOT NULL,
  PRIMARY KEY (`Pincode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `branch`
--

LOCK TABLES `branch` WRITE;
/*!40000 ALTER TABLE `branch` DISABLE KEYS */;
INSERT INTO `branch` VALUES ('83351 Lakeland Drive',152737),('403 Havey Lane',185797),('8672 Grim Avenue',213308),('410 Carioca Crossing',219977),('98 Mccormick Drive',267157),('748 Forest Dale Way',293448),('3 Lakeland Crossing',312554),('94 Loeprich Plaza',318378),('6278 Warner Street',336837),('539 Esch Hill',356345),('3796 Hanover Alley',359084),('1 Randy Park',389412),('7 Cordelia Road',404434),('9604 Mandrake Place',437261),('0509 Butterfield Place',441113),('0 Clarendon Junction',543807),('84462 Mccormick Park',596998),('77 Kennedy Pass',656107),('86 Colorado Point',681439),('958 Graedel Avenue',751554),('21815 Iowa Park',823220),('19402 Elmside Avenue',851978),('2406 Hagan Plaza',860000),('6 Buell Alley',863622),('6038 Dapin Street',952970);
/*!40000 ALTER TABLE `branch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cart`
--

DROP TABLE IF EXISTS `cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cart` (
  `user_ID` varchar(5) NOT NULL,
  `product_ID` varchar(5) NOT NULL,
  `Quantity` int NOT NULL,
  PRIMARY KEY (`user_ID`,`product_ID`),
  KEY `product_ID` (`product_ID`),
  CONSTRAINT `cart_ibfk_1` FOREIGN KEY (`user_ID`) REFERENCES `customer` (`user_ID`),
  CONSTRAINT `cart_ibfk_2` FOREIGN KEY (`product_ID`) REFERENCES `product` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart`
--

LOCK TABLES `cart` WRITE;
/*!40000 ALTER TABLE `cart` DISABLE KEYS */;
INSERT INTO `cart` VALUES ('100','40',3),('12','23',9),('13','42',5),('16','52',6),('19','61',1),('20','61',8),('22','75',6),('24','53',7),('24','96',2),('25','77',1),('25','80',1),('30','42',10),('30','53',6),('34','39',4),('34','43',6),('35','64',10),('36','71',3),('38','44',10),('39','1',8),('39','46',9),('39','60',4),('4','12',3),('40','11',8),('41','84',8),('41','85',2),('42','26',6),('42','69',1),('44','18',2),('45','68',5),('45','8',2),('46','43',7),('46','68',8),('48','15',6),('48','81',7),('50','27',6),('51','60',2),('51','64',7),('52','20',3),('52','29',9),('52','4',3),('55','6',2),('57','23',1),('58','18',3),('59','12',15),('59','22',15),('59','4',2),('59','50',8),('59','82',6),('6','51',8),('6','97',6),('60','31',5),('60','41',10),('60','50',1),('60','94',4),('61','27',1),('62','32',2),('62','60',6),('63','8',10),('65','75',2),('67','1',6),('69','93',6),('7','3',1),('70','71',3),('71','56',3),('72','4',7),('74','91',1),('75','58',8),('75','73',4),('77','72',10),('77','95',8),('79','10',5),('8','84',7),('81','92',6),('81','94',3),('83','18',9),('83','19',4),('83','6',5),('83','74',3),('84','3',5),('85','22',1),('86','24',5),('86','28',7),('87','96',10),('88','53',6),('89','30',5),('9','33',9),('9','47',5),('9','96',7),('91','54',7),('92','35',9),('93','7',4),('95','34',4),('95','56',2),('99','95',6);
/*!40000 ALTER TABLE `cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coupon`
--

DROP TABLE IF EXISTS `coupon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coupon` (
  `coupon_id` int NOT NULL,
  `min_order_amt` int DEFAULT NULL,
  `valid_until_date` date DEFAULT NULL,
  `discount_offered` int DEFAULT NULL,
  `date_of_issue` date NOT NULL,
  `order_id` varchar(5) DEFAULT NULL,
  `order_date` date DEFAULT NULL,
  `user_ID` varchar(5) NOT NULL,
  PRIMARY KEY (`coupon_id`,`user_ID`),
  KEY `order_id` (`order_id`),
  KEY `user_ID` (`user_ID`),
  KEY `order_date` (`order_date`),
  KEY `d` (`order_date`),
  CONSTRAINT `coupon_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`),
  CONSTRAINT `coupon_ibfk_2` FOREIGN KEY (`user_ID`) REFERENCES `customer` (`user_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coupon`
--

LOCK TABLES `coupon` WRITE;
/*!40000 ALTER TABLE `coupon` DISABLE KEYS */;
INSERT INTO `coupon` VALUES (1,4893,'2022-05-24',18,'2022-05-22',NULL,NULL,'12'),(2,5845,'2022-05-07',35,'2022-12-24',NULL,NULL,'21'),(3,8866,'2022-11-09',90,'2022-07-24',NULL,NULL,'31'),(4,6317,'2023-01-03',14,'2022-09-11',NULL,NULL,'14'),(5,8126,'2022-09-13',88,'2022-05-17',NULL,NULL,'15'),(6,9171,'2022-12-16',87,'2022-10-03',NULL,NULL,'46'),(7,3258,'2022-06-24',55,'2022-08-04',NULL,NULL,'57'),(8,8721,'2022-05-31',66,'2022-03-10',NULL,NULL,'8'),(9,1932,'2022-11-27',28,'2022-08-27',NULL,NULL,'29'),(10,8111,'2023-01-18',19,'2022-10-23',NULL,NULL,'10'),(11,1500,'2023-04-25',20,'2023-02-25',NULL,NULL,'80');
/*!40000 ALTER TABLE `coupon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `user_ID` varchar(5) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `contact_no` varchar(10) DEFAULT NULL,
  `total_no_of_orders` int DEFAULT '0',
  `pincode` int DEFAULT NULL,
  PRIMARY KEY (`user_ID`),
  KEY `pincode` (`pincode`),
  CONSTRAINT `customer_ibfk_1` FOREIGN KEY (`pincode`) REFERENCES `branch` (`Pincode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('1','Pork - Ham, Virginia','4023544916',1,152737),('10','Sprite, Diet - 355ml','5343211899',10,152737),('100','Wine - Carmenere Casillero Del','3588453367',100,152737),('11','Chickensplit Half','6778059883',12,152737),('12','Salt And Pepper Mix - Black','9766873989',12,152737),('13','Veal - Shank, Pieces','3019941254',13,152737),('14','Water - San Pellegrino','5955518395',14,152737),('15','Lemon Balm - Fresh','9967492743',15,152737),('16','Veal - Liver','5158033898',16,152737),('17','Fish - Scallops, Cold Smoked','1834651324',17,152737),('18','Rice - Brown','5621478063',18,219977),('19','Chips - Potato Jalapeno','7565177501',19,219977),('2','Beef - Tender Tips','9968958939',2,219977),('20','Muffin - Mix - Strawberry Rhubarb','1626019778',20,219977),('21','Crackers - Soda / Saltins','7176424285',21,219977),('22','Veal - Shank, Pieces','6565452836',22,219977),('23','Sloe Gin - Mcguinness','4559963111',23,219977),('24','Cheese - Parmigiano Reggiano','3032565975',24,219977),('25','Pepper - Chillies, Crushed','8307193674',25,219977),('26','Beef - Montreal Smoked Brisket','1936009457',26,219977),('27','Beef Cheek Fresh','3266838349',27,267157),('28','Pasta - Bauletti, Chicken White','3106145739',28,267157),('29','Soho Lychee Liqueur','3711600004',29,267157),('3','Cheese - Colby','4819204181',3,267157),('30','Doilies - 8, Paper','3322733257',30,267157),('31','Five Alive Citrus','7321270731',31,267157),('32','Wine - Cava Aria Estate Brut','6877459366',32,267157),('33','Butter - Unsalted','2667494129',33,267157),('34','Peach - Halves','6666285726',34,267157),('35','Beans - Black Bean, Dry','5361592357',35,267157),('36','Wine - Lamancha Do Crianza','8324059378',36,185797),('37','Cheese - Mozzarella, Shredded','3024817484',37,185797),('38','Durian Fruit','4738735684',38,185797),('39','Beets - Mini Golden','3811732919',39,185797),('4','Lychee - Canned','8227938312',4,185797),('40','Energy Drink','8472629932',40,185797),('41','Sambuca Cream','8718924622',41,185797),('42','Ice Cream - Super Sandwich','1506641809',42,185797),('43','Coffee - Cafe Moreno','3894792735',43,185797),('44','Pork - Inside','4638423607',44,185797),('45','Cloves - Whole','3203684449',45,185797),('46','Ham - Cooked','2323049789',46,185797),('47','Pate Pans Yellow','4429847457',47,185797),('48','Bread - Frozen Basket Variety','4431142755',48,185797),('49','Capicola - Hot','5344900561',49,185797),('5','Energy Drink Bawls','7754691282',5,185797),('50','Pasta - Orzo, Dry','5564830222',50,185797),('51','Ostrich - Prime Cut','5074471656',51,185797),('52','Mix - Cocktail Ice Cream','3872407222',52,185797),('53','Boogies','5495372206',53,185797),('54','Appetizer - Veg Assortment','5339013633',54,359084),('55','Compound - Pear','3591508693',55,359084),('56','Ostrich - Fan Fillet','1443193841',56,359084),('57','Cheese - Cambozola','2755891476',57,359084),('58','Yogurt - Plain','8346964569',58,359084),('59','Zucchini - Yellow','8795427081',59,359084),('6','Wine - Prem Select Charddonany','4348156086',6,359084),('60','Jicama','9098257240',60,359084),('61','Broom And Brush Rack Black','6759190091',61,359084),('62','Pepper - Paprika, Spanish','1725375480',62,359084),('63','Veal - Tenderloin, Untrimmed','4824711150',63,359084),('64','Pickle - Dill','7643739368',64,359084),('65','Pasta - Agnolotti - Butternut','6718273250',65,359084),('66','Garlic Powder','7848099599',66,359084),('67','Scotch - Queen Anne','8234570954',67,359084),('68','Melon - Watermelon Yellow','3099990344',68,359084),('69','Wine - Fino Tio Pepe Gonzalez','9998203652',69,359084),('7','Veal Inside - Provimi','6563614370',7,359084),('70','Ham - Cooked Bayonne Tinned','2263759343',70,359084),('71','Potatoes - Idaho 100 Count','5069008818',71,359084),('72','Soap - Hand Soap','1647395884',72,851978),('73','White Fish - Filets','2304892996',73,851978),('74','Creme De Menthe Green','5692270156',74,851978),('75','Pastry - Choclate Baked','9672822332',75,851978),('76','Bread - Triangle White','5336443373',76,851978),('77','Chocolate - Mi - Amere Semi','7855839506',77,851978),('78','Table Cloth 62x120 Colour','6802303921',78,851978),('79','Tomato Paste','4403509179',79,851978),('8','Crackers - Soda / Saltins','5229918416',8,851978),('80','Mushroom - Porcini, Dry','5584293522',80,851978),('81','Contreau','2042928335',81,656107),('82','Cup - 3.5oz, Foam','4598307457',82,656107),('83','Cheese - Provolone','5163264715',83,656107),('84','Beef - Cooked, Corned','1228680936',84,656107),('85','Barley - Pearl','9705582512',85,656107),('86','Veal - Inside, Choice','4294491177',86,656107),('87','Towel Dispenser','1352849588',87,656107),('88','Sausage - Liver','4115033252',88,656107),('89','Vinegar - Sherry','2883843732',89,656107),('9','Mushroom - Morel Frozen','6577271952',9,656107),('90','Sugar - Icing','6101663019',90,952970),('91','Longos - Grilled Veg Sandwiches','4122615692',91,952970),('92','Chicken - Wieners','5734269248',92,952970),('93','Pastry - Trippleberry Muffin - Mini','5643347230',93,952970),('94','Maintenance Removal Charge','5482885652',94,952970),('95','Pepper - Paprika, Spanish','2123435722',95,952970),('96','Yoghurt Tubes','7776778343',96,952970),('97','Cheese - Cottage Cheese','5166702301',97,952970),('98','Crackers - Graham','9124490113',98,952970),('99','Flour - Bread','5229842132',99,952970);
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `order_id` varchar(5) NOT NULL,
  `order_date` date NOT NULL,
  `total_price` float DEFAULT NULL,
  `delivery_date` date DEFAULT NULL,
  `pincode` int DEFAULT NULL,
  `user_id` varchar(5) NOT NULL,
  PRIMARY KEY (`order_id`,`order_date`,`user_id`),
  KEY `pincode` (`pincode`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`pincode`) REFERENCES `branch` (`Pincode`),
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `customer` (`user_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES ('1','2022-06-21',1815,'2022-07-28',860000,'10'),('10','2022-08-15',56.35,'2022-05-16',152737,'22'),('11','2023-03-25',400,'2023-03-26',860000,'80'),('12','2023-03-25',800,'2023-04-25',152737,'10'),('13','2023-03-25',800,'2023-04-25',152737,'10'),('14','2023-03-25',800,'2023-04-25',152737,'10'),('15','2023-03-25',800,'2023-04-25',152737,'10'),('16','2023-03-25',800,'2023-04-25',152737,'12'),('17','2023-01-22',900,'2023-03-22',152737,'10'),('17','2023-03-25',800,'2023-04-25',152737,'12'),('18','2023-01-22',900,'2023-03-22',152737,'23'),('19','2023-03-25',1000,'2023-03-25',152737,'12'),('2','2022-08-27',1509,'2022-07-01',751554,'21'),('3','2022-09-22',4567,'2022-06-19',404434,'30'),('4','2022-08-30',5207,'2022-11-21',851978,'33'),('5','2022-08-29',2858,'2022-07-09',441113,'11'),('6','2022-04-19',8915,'2022-11-22',863622,'6'),('7','2022-05-30',7046,'2022-08-06',312554,'7'),('8','2022-04-12',859,'2022-12-03',543807,'81'),('9','2022-09-06',8787,'2022-07-21',952970,'60');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `product_id` varchar(5) NOT NULL,
  `product_name` varchar(255) DEFAULT NULL,
  `price` int DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES ('1','Mayonnaise - Individual Pkg',9873),('10','Contreau',5130),('100','Spaghetti Squash',5280),('11','Energy Drink Bawls',6027),('12','Icecream Cone - Areo Chocolate',8788),('13','Cheese - Le Cru Du Clocher',131),('14','Syrup - Monin, Swiss Choclate',6507),('15','Parasol Pick Stir Stick',9677),('16','Lime Cordial - Roses',8560),('17','Lamb Tenderloin Nz Fr',24),('18','Lychee',790),('19','Ecolab - Power Fusion',6828),('2','Wine - Two Oceans Cabernet',3945),('20','Beans - French',4227),('21','Squeeze Bottle',2696),('22','Chocolate - Milk Coating',2542),('23','Island Oasis - Magarita Mix',1105),('24','Wine - Barossa Valley Estate',6041),('25','Cleaner - Comet',7199),('26','Icecream Cone - Areo Chocolate',9994),('27','Persimmons',5387),('28','Salt And Pepper Mix - White',3648),('29','Cranberry Foccacia',8767),('3','Longos - Lasagna Beef',288),('30','Venison - Denver Leg Boneless',5252),('31','Chocolate Bar - Smarties',9631),('32','Lemonade - Mandarin, 591 Ml',7276),('33','Chick Peas - Canned',1389),('34','Ocean Spray - Ruby Red',2982),('35','Nut - Cashews, Whole, Raw',5481),('36','Pork - Tenderloin, Fresh',8476),('37','White Baguette',7410),('38','Wine - Red, Colio Cabernet',6825),('39','Bread - Roll, Whole Wheat',4649),('4','Mussels - Frozen',1481),('40','Pasta - Tortellini, Fresh',3645),('41','Spice - Montreal Steak Spice',7583),('42','Dried Peach',9642),('43','Wine - Jackson Triggs Okonagan',4762),('44','Eggroll',3811),('45','Yeast Dry - Fleischman',4783),('46','Strawberries',1692),('47','Energy Drink Bawls',7436),('48','Pepper - Julienne, Frozen',3528),('49','Chocolate - Compound Coating',9391),('5','Flour - Strong',6774),('50','Milk - Chocolate 250 Ml',7835),('51','Coffee - Espresso',6276),('52','Ginger - Crystalized',1857),('53','Beer - Sleemans Cream Ale',4716),('54','Vermouth - White, Cinzano',478),('55','Bread Sour Rolls',9062),('56','Oven Mitts - 15 Inch',5793),('57','Sauce Bbq Smokey',8067),('58','Juice - Tomato, 10 Oz',4137),('59','Chips Potato All Dressed - 43g',1899),('6','Roe - White Fish',1408),('60','Country Roll',7962),('61','Split Peas - Yellow, Dry',5353),('62','Cheese - Camembert',7040),('63','Wine - Sauvignon Blanc Oyster',2007),('64','Turkey - Ground. Lean',8932),('65','Tandoori Curry Paste',1275),('66','Veal - Heart',9272),('67','Pasta - Orecchiette',488),('68','Crab - Claws, Snow 16 - 24',6900),('69','Gatorade - Lemon Lime',5617),('7','Tea - Herbal Sweet Dreams',6686),('70','Nantucket - Kiwi Berry Cktl.',2393),('71','Cheese - Grie Des Champ',6176),('72','Chicken Thigh - Bone Out',3541),('73','Chicken - Thigh, Bone In',514),('74','Turnip - Wax',1974),('75','Wine - Magnotta - Cab Sauv',9865),('76','Carbonated Water - Cherry',8292),('77','Salami - Genova',9509),('78','Turkey - Breast, Double',352),('79','Wine - Zonnebloem Pinotage',1105),('8','Cup - 8oz Coffee Perforated',5446),('80','Coffee Cup 8oz 5338cd',243),('81','Lettuce - Curly Endive',5964),('82','Chocolate - Dark',509),('83','Juice - Apple, 341 Ml',6371),('84','Jam - Raspberry',1448),('85','C - Plus, Orange',7626),('86','Coffee Cup 16oz Foam',9820),('87','Cup Translucent 9 Oz',5835),('88','Coffee - Beans, Whole',6316),('89','Chevril',2624),('9','Icecream - Dibs',3913),('90','Chef Hat 20cm',4435),('91','Pastry - Apple Muffins - Mini',4811),('92','Soup - French Onion',6078),('93','Wine - Redchard Merritt',8360),('94','Ham Black Forest',682),('95','Wine - Rubyport',505),('96','Fond - Neutral',5469),('97','Pastry - Trippleberry Muffin - Mini',1005),('98','Cheese - Roquefort Pappillon',4162),('99','Shrimp - Black Tiger 16/20',1541);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_in_order`
--

DROP TABLE IF EXISTS `products_in_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_in_order` (
  `order_id` varchar(5) NOT NULL,
  `user_id` varchar(5) NOT NULL,
  `product_id` varchar(5) NOT NULL,
  `quantity` int DEFAULT NULL,
  PRIMARY KEY (`order_id`,`user_id`,`product_id`),
  KEY `user_id` (`user_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `products_in_order_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `customer` (`user_ID`),
  CONSTRAINT `products_in_order_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_in_order`
--

LOCK TABLES `products_in_order` WRITE;
/*!40000 ALTER TABLE `products_in_order` DISABLE KEYS */;
INSERT INTO `products_in_order` VALUES ('16','12','23',9),('17','12','23',9),('18','23','63',6),('19','12','23',9),('21','30','42',10),('21','30','53',6),('50','23','63',6),('60','10','30',10),('60','10','40',10),('60','30','42',10),('60','30','53',6);
/*!40000 ALTER TABLE `products_in_order` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-19 19:50:52
