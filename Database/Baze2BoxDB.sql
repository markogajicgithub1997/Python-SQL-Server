USE [master]
GO
/****** Object:  Database [BOX]    Script Date: 1/28/2021 1:22:12 PM ******/
CREATE DATABASE [BOX]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'BOX', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\BOX.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB ), 
 FILEGROUP [April] 
( NAME = N'Part_April', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\BOX_Part_April.ndf' , SIZE = 5120KB , MAXSIZE = UNLIMITED, FILEGROWTH = 5120KB ), 
 FILEGROUP [Avgust] 
( NAME = N'Part_Avgust', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\BOX_Part_Avgust.ndf' , SIZE = 5120KB , MAXSIZE = UNLIMITED, FILEGROWTH = 5120KB ), 
 FILEGROUP [Decembar] 
( NAME = N'Part_Decembar', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\BOX_Part_Decembar.ndf' , SIZE = 5120KB , MAXSIZE = UNLIMITED, FILEGROWTH = 5120KB ), 
 FILEGROUP [Februar] 
( NAME = N'Part_Februar', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\BOX_Part_Februar.ndf' , SIZE = 5120KB , MAXSIZE = UNLIMITED, FILEGROWTH = 5120KB ), 
 FILEGROUP [Januar] 
( NAME = N'Part_Januar', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\BOX_Part_Januar.ndf' , SIZE = 5120KB , MAXSIZE = UNLIMITED, FILEGROWTH = 5120KB ), 
 FILEGROUP [Jul] 
( NAME = N'Part_Jul', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\BOX_Part_Jul.ndf' , SIZE = 5120KB , MAXSIZE = UNLIMITED, FILEGROWTH = 5120KB ), 
 FILEGROUP [Jun] 
( NAME = N'Part_Jun', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\BOX_Part_Jun.ndf' , SIZE = 5120KB , MAXSIZE = UNLIMITED, FILEGROWTH = 5120KB ), 
 FILEGROUP [Maj] 
( NAME = N'Part_Maj', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\BOX_Part_Maj.ndf' , SIZE = 5120KB , MAXSIZE = UNLIMITED, FILEGROWTH = 5120KB ), 
 FILEGROUP [Mart] 
( NAME = N'Part_Mart', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\BOX_Part_Mart.ndf' , SIZE = 5120KB , MAXSIZE = UNLIMITED, FILEGROWTH = 5120KB ), 
 FILEGROUP [Novembar] 
( NAME = N'Part_Novembar', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\BOX_Part_Novembar.ndf' , SIZE = 5120KB , MAXSIZE = UNLIMITED, FILEGROWTH = 5120KB ), 
 FILEGROUP [Oktobar] 
( NAME = N'Part_Oktobar', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\BOX_Part_Oktobar.ndf' , SIZE = 5120KB , MAXSIZE = UNLIMITED, FILEGROWTH = 5120KB ), 
 FILEGROUP [Septembar] 
( NAME = N'Part_Septembar', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\BOX_Part_Septembar.ndf' , SIZE = 5120KB , MAXSIZE = UNLIMITED, FILEGROWTH = 5120KB )
 LOG ON 
( NAME = N'BOX_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\BOX_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [BOX] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [BOX].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [BOX] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [BOX] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [BOX] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [BOX] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [BOX] SET ARITHABORT OFF 
GO
ALTER DATABASE [BOX] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [BOX] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [BOX] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [BOX] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [BOX] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [BOX] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [BOX] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [BOX] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [BOX] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [BOX] SET  ENABLE_BROKER 
GO
ALTER DATABASE [BOX] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [BOX] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [BOX] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [BOX] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [BOX] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [BOX] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [BOX] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [BOX] SET RECOVERY FULL 
GO
ALTER DATABASE [BOX] SET  MULTI_USER 
GO
ALTER DATABASE [BOX] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [BOX] SET DB_CHAINING OFF 
GO
ALTER DATABASE [BOX] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [BOX] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [BOX] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [BOX] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'BOX', N'ON'
GO
ALTER DATABASE [BOX] SET QUERY_STORE = OFF
GO
USE [BOX]
GO
/****** Object:  PartitionFunction [ParticionisanjePoMesecima]    Script Date: 1/28/2021 1:22:12 PM ******/
CREATE PARTITION FUNCTION [ParticionisanjePoMesecima](date) AS RANGE RIGHT FOR VALUES (N'2020-01-01T00:00:00.000', N'2020-02-01T00:00:00.000', N'2020-03-01T00:00:00.000', N'2020-04-01T00:00:00.000', N'2020-05-01T00:00:00.000', N'2020-06-01T00:00:00.000', N'2020-07-01T00:00:00.000', N'2020-08-01T00:00:00.000', N'2020-09-01T00:00:00.000', N'2020-10-01T00:00:00.000', N'2020-11-01T00:00:00.000', N'2020-12-01T00:00:00.000', N'2021-01-01T00:00:00.000')
GO
/****** Object:  PartitionScheme [ParticionisanjePoMesecima]    Script Date: 1/28/2021 1:22:12 PM ******/
CREATE PARTITION SCHEME [ParticionisanjePoMesecima] AS PARTITION [ParticionisanjePoMesecima] TO ([PRIMARY], [Januar], [Februar], [Mart], [April], [Maj], [Jun], [Jul], [Avgust], [Septembar], [Oktobar], [Novembar], [Decembar], [PRIMARY])
GO
/****** Object:  Rule [PraviloZaProcenat]    Script Date: 1/28/2021 1:22:12 PM ******/
CREATE RULE [dbo].[PraviloZaProcenat] 
AS
@Procenat>=0 and @Procenat<=100
GO
/****** Object:  UserDefinedDataType [dbo].[Procenat]    Script Date: 1/28/2021 1:22:12 PM ******/
CREATE TYPE [dbo].[Procenat] FROM [decimal](5, 2) NOT NULL
GO
/****** Object:  Table [dbo].[StudentOstalo]    Script Date: 1/28/2021 1:22:12 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[StudentOstalo](
	[ID] [int] NOT NULL,
	[Email] [nvarchar](50) NULL,
	[DrzavaID] [int] NOT NULL,
	[GradID] [int] NOT NULL,
	[OpstinaID] [int] NOT NULL,
	[UlicaID] [int] NOT NULL,
	[BrojID] [char](50) NOT NULL,
 CONSTRAINT [PK_StudentOstalo] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Student]    Script Date: 1/28/2021 1:22:12 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Student](
	[ID] [int] NOT NULL,
	[Ime] [nvarchar](50) NOT NULL,
	[Prezime] [nvarchar](50) NOT NULL,
	[Telefon] [nvarchar](50) NULL,
	[BOP] [nvarchar](50) NULL,
	[TekuciRacun] [nvarchar](50) NULL,
 CONSTRAINT [PK_Student] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[Student_View]    Script Date: 1/28/2021 1:22:12 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE VIEW [dbo].[Student_View] AS
	SELECT Student.ID , Student.Ime , Student.Prezime , Student.Telefon , Student.BOP , Student.TekuciRacun , 
		   StudentOstalo.Email , StudentOstalo.DrzavaID , StudentOstalo.GradID , StudentOstalo.OpstinaID , StudentOstalo.UlicaID , StudentOstalo.BrojID
	FROM Student INNER JOIN StudentOstalo ON Student.ID = StudentOstalo.ID
GO
/****** Object:  Table [dbo].[Broj]    Script Date: 1/28/2021 1:22:12 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Broj](
	[DrzavaID] [int] NOT NULL,
	[GradID] [int] NOT NULL,
	[OpstinaID] [int] NOT NULL,
	[UlicaID] [int] NOT NULL,
	[BrojID] [char](50) NOT NULL,
 CONSTRAINT [PK_Broj] PRIMARY KEY CLUSTERED 
(
	[DrzavaID] ASC,
	[GradID] ASC,
	[OpstinaID] ASC,
	[UlicaID] ASC,
	[BrojID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Drzava]    Script Date: 1/28/2021 1:22:12 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Drzava](
	[ID] [int] NOT NULL,
	[Naziv] [nvarchar](50) NULL,
 CONSTRAINT [PK_Drzava] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Faktura]    Script Date: 1/28/2021 1:22:12 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Faktura](
	[ZadrugaID] [int] NOT NULL,
	[ID] [int] NOT NULL,
	[DatumFakture] [date] NOT NULL,
	[OpisFakture] [nvarchar](200) NULL,
	[IznosFakture] [numeric](18, 2) NULL,
	[PoslodavacID] [int] NOT NULL,
	[PDV] [dbo].[Procenat] NULL,
 CONSTRAINT [PK_Faktura] PRIMARY KEY CLUSTERED 
(
	[ZadrugaID] ASC,
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Grad]    Script Date: 1/28/2021 1:22:12 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Grad](
	[DrzavaID] [int] NOT NULL,
	[ID] [int] NOT NULL,
	[Naziv] [nvarchar](50) NOT NULL,
 CONSTRAINT [PK_Grad] PRIMARY KEY CLUSTERED 
(
	[DrzavaID] ASC,
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[IznosPlate]    Script Date: 1/28/2021 1:22:12 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[IznosPlate](
	[KategorijaID] [int] NOT NULL,
	[PodkategorijaID] [int] NOT NULL,
	[PosaoID] [int] NOT NULL,
	[Datum] [date] NOT NULL,
	[JedinicnaCena] [numeric](18, 2) NULL,
 CONSTRAINT [PK_IznosPlate] PRIMARY KEY CLUSTERED 
(
	[KategorijaID] ASC,
	[PodkategorijaID] ASC,
	[PosaoID] ASC,
	[Datum] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Kategorija]    Script Date: 1/28/2021 1:22:12 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Kategorija](
	[ID] [int] NOT NULL,
	[Naziv] [nvarchar](90) NULL,
 CONSTRAINT [PK_Kategorija] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Opstina]    Script Date: 1/28/2021 1:22:12 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Opstina](
	[DrzavaID] [int] NOT NULL,
	[GradID] [int] NOT NULL,
	[ID] [int] NOT NULL,
	[Naziv] [nvarchar](50) NOT NULL,
 CONSTRAINT [PK_Opstina] PRIMARY KEY CLUSTERED 
(
	[DrzavaID] ASC,
	[GradID] ASC,
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[PDV]    Script Date: 1/28/2021 1:22:12 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PDV](
	[UplataID] [int] NOT NULL,
	[ID] [int] NOT NULL,
	[IznosUProcentima] [dbo].[Procenat] NOT NULL,
 CONSTRAINT [PK_PDV] PRIMARY KEY CLUSTERED 
(
	[UplataID] ASC,
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Podkategorija]    Script Date: 1/28/2021 1:22:12 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Podkategorija](
	[KategorijaID] [int] NOT NULL,
	[ID] [int] NOT NULL,
	[Naziv] [varchar](99) NULL,
	[NazivKategorije] [varchar](99) NULL,
 CONSTRAINT [PK_Podkategorija] PRIMARY KEY CLUSTERED 
(
	[KategorijaID] ASC,
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Posao]    Script Date: 1/28/2021 1:22:12 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Posao](
	[KategorijaID] [int] NOT NULL,
	[PodkategorijaID] [int] NOT NULL,
	[ID] [int] NOT NULL,
	[Naziv] [varchar](50) NULL,
	[OpisPosla] [varchar](500) NULL,
	[PoslodavacID] [int] NULL,
	[NazivPoslodavca] [varchar](50) NULL,
	[Plata] [numeric](18, 2) NULL,
 CONSTRAINT [PK_Posao] PRIMARY KEY CLUSTERED 
(
	[KategorijaID] ASC,
	[PodkategorijaID] ASC,
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Poslodavac]    Script Date: 1/28/2021 1:22:12 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Poslodavac](
	[ID] [int] NOT NULL,
	[Naziv] [nvarchar](50) NULL,
	[Telefon] [nvarchar](50) NULL,
	[PIB] [nvarchar](50) NULL,
	[TekuciRacun] [nvarchar](50) NULL,
	[DrzavaID] [int] NULL,
	[GradID] [int] NULL,
	[OpstinaID] [int] NULL,
	[UlicaID] [int] NULL,
	[BrojID] [char](50) NULL,
 CONSTRAINT [PK_Poslodavac] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[PristupniFormular]    Script Date: 1/28/2021 1:22:12 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PristupniFormular](
	[StudentID] [int] NOT NULL,
	[ID] [int] NOT NULL,
	[DatumPopunjavanja] [date] NOT NULL,
	[ZadrugaID] [int] NOT NULL,
 CONSTRAINT [PK_PristupniFormular] PRIMARY KEY CLUSTERED 
(
	[StudentID] ASC,
	[DatumPopunjavanja] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [ParticionisanjePoMesecima]([DatumPopunjavanja])
) ON [ParticionisanjePoMesecima]([DatumPopunjavanja])
GO
/****** Object:  Table [dbo].[StavkaFakture]    Script Date: 1/28/2021 1:22:12 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[StavkaFakture](
	[ZadrugaID] [int] NOT NULL,
	[FakturaID] [int] NOT NULL,
	[ID] [int] NOT NULL,
	[RedniBroj] [int] NOT NULL,
	[OpisStavke] [nvarchar](200) NULL,
	[IznosStavke] [numeric](18, 2) NOT NULL,
 CONSTRAINT [PK_StavkaFakture] PRIMARY KEY CLUSTERED 
(
	[ZadrugaID] ASC,
	[FakturaID] ASC,
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TrojniUgovor]    Script Date: 1/28/2021 1:22:12 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TrojniUgovor](
	[ID] [int] NOT NULL,
	[ZadrugaID] [int] NOT NULL,
	[StudentID] [int] NOT NULL,
	[PoslodavacID] [int] NOT NULL,
	[KategorijaID] [int] NOT NULL,
	[PodkategorijaID] [int] NOT NULL,
	[RadnoMestoID] [int] NOT NULL,
	[PlataIznos] [nvarchar](90) NULL,
	[DatumOD] [date] NOT NULL,
	[DatumDO] [date] NOT NULL,
	[Info] [nvarchar](max) NULL,
 CONSTRAINT [PK_TrojniUgovor] PRIMARY KEY CLUSTERED 
(
	[ID] ASC,
	[ZadrugaID] ASC,
	[StudentID] ASC,
	[PoslodavacID] ASC,
	[KategorijaID] ASC,
	[PodkategorijaID] ASC,
	[RadnoMestoID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Ulica]    Script Date: 1/28/2021 1:22:12 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Ulica](
	[DrzavaID] [int] NOT NULL,
	[GradID] [int] NOT NULL,
	[OpstinaID] [int] NOT NULL,
	[ID] [int] NOT NULL,
	[Naziv] [nvarchar](50) NOT NULL,
 CONSTRAINT [pk_ulica] PRIMARY KEY CLUSTERED 
(
	[DrzavaID] ASC,
	[GradID] ASC,
	[OpstinaID] ASC,
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Zadruga]    Script Date: 1/28/2021 1:22:12 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Zadruga](
	[ID] [int] NOT NULL,
	[Naziv] [nvarchar](90) NOT NULL,
	[Telefon] [nvarchar](90) NULL,
	[PIB] [nvarchar](90) NULL,
	[TekuciRacun] [nvarchar](90) NULL,
	[DrzavaID] [int] NOT NULL,
	[GradID] [int] NOT NULL,
	[OpstinaID] [int] NOT NULL,
	[UlicaID] [int] NOT NULL,
	[BrojID] [char](50) NOT NULL,
 CONSTRAINT [PK_Zadruga] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (1, 1, 1, 1, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (1, 1, 1, 1, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (1, 1, 1, 2, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (1, 1, 1, 2, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (1, 1, 2, 1, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (1, 1, 2, 1, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (1, 1, 2, 2, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (1, 1, 2, 2, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (1, 2, 1, 1, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (1, 2, 1, 1, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (1, 2, 1, 2, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (1, 2, 1, 2, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (1, 2, 2, 1, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (1, 2, 2, 1, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (1, 2, 2, 2, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (1, 2, 2, 2, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (1, 3, 1, 1, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (1, 3, 1, 1, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (1, 3, 1, 2, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (1, 3, 1, 2, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (1, 3, 2, 1, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (1, 3, 2, 1, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (1, 3, 2, 2, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (1, 3, 2, 2, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (2, 1, 1, 1, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (2, 1, 1, 1, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (2, 1, 1, 2, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (2, 1, 1, 2, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (2, 1, 2, 1, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (2, 1, 2, 1, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (2, 1, 2, 2, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (2, 1, 2, 2, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (2, 2, 1, 1, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (2, 2, 1, 1, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (2, 2, 1, 2, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (2, 2, 1, 2, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (2, 2, 2, 1, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (2, 2, 2, 1, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (2, 2, 2, 2, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (2, 2, 2, 2, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (2, 3, 1, 1, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (2, 3, 1, 1, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (2, 3, 1, 2, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (2, 3, 1, 2, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (2, 3, 2, 1, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (2, 3, 2, 1, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (2, 3, 2, 2, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (2, 3, 2, 2, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (3, 1, 1, 1, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (3, 1, 1, 1, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (3, 1, 1, 2, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (3, 1, 1, 2, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (3, 1, 2, 1, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (3, 1, 2, 1, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (3, 1, 2, 2, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (3, 1, 2, 2, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (3, 2, 1, 1, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (3, 2, 1, 1, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (3, 2, 1, 2, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (3, 2, 1, 2, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (3, 2, 2, 1, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (3, 2, 2, 1, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (3, 2, 2, 2, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (3, 2, 2, 2, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (3, 3, 1, 1, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (3, 3, 1, 1, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (3, 3, 1, 2, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (3, 3, 1, 2, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (3, 3, 2, 1, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (3, 3, 2, 1, N'2                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (3, 3, 2, 2, N'1                                                 ')
GO
INSERT [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (3, 3, 2, 2, N'2                                                 ')
GO
INSERT [dbo].[Drzava] ([ID], [Naziv]) VALUES (1, N'Srbija')
GO
INSERT [dbo].[Drzava] ([ID], [Naziv]) VALUES (2, N'Bosna i Hercegovina')
GO
INSERT [dbo].[Drzava] ([ID], [Naziv]) VALUES (3, N'Crna Gora')
GO
INSERT [dbo].[Faktura] ([ZadrugaID], [ID], [DatumFakture], [OpisFakture], [IznosFakture], [PoslodavacID], [PDV]) VALUES (1, 1, CAST(N'2020-12-01' AS Date), N'Faktura1', CAST(30000.00 AS Numeric(18, 2)), 1, CAST(6.00 AS Decimal(5, 2)))
GO
INSERT [dbo].[Faktura] ([ZadrugaID], [ID], [DatumFakture], [OpisFakture], [IznosFakture], [PoslodavacID], [PDV]) VALUES (1, 2, CAST(N'2020-12-10' AS Date), N'Faktura2', CAST(15000.00 AS Numeric(18, 2)), 2, CAST(3.00 AS Decimal(5, 2)))
GO
INSERT [dbo].[Faktura] ([ZadrugaID], [ID], [DatumFakture], [OpisFakture], [IznosFakture], [PoslodavacID], [PDV]) VALUES (1, 3, CAST(N'2020-12-10' AS Date), N'Faktura3', CAST(25000.00 AS Numeric(18, 2)), 3, CAST(25.00 AS Decimal(5, 2)))
GO
INSERT [dbo].[Faktura] ([ZadrugaID], [ID], [DatumFakture], [OpisFakture], [IznosFakture], [PoslodavacID], [PDV]) VALUES (1, 4, CAST(N'2020-12-10' AS Date), N'Faktura4', CAST(41000.00 AS Numeric(18, 2)), 4, CAST(23.00 AS Decimal(5, 2)))
GO
INSERT [dbo].[Faktura] ([ZadrugaID], [ID], [DatumFakture], [OpisFakture], [IznosFakture], [PoslodavacID], [PDV]) VALUES (1, 5, CAST(N'2020-12-10' AS Date), N'Faktura5', CAST(13000.00 AS Numeric(18, 2)), 5, CAST(2.00 AS Decimal(5, 2)))
GO
INSERT [dbo].[Faktura] ([ZadrugaID], [ID], [DatumFakture], [OpisFakture], [IznosFakture], [PoslodavacID], [PDV]) VALUES (1, 6, CAST(N'2020-12-10' AS Date), N'Faktura6', CAST(59200.00 AS Numeric(18, 2)), 6, CAST(14.00 AS Decimal(5, 2)))
GO
INSERT [dbo].[Faktura] ([ZadrugaID], [ID], [DatumFakture], [OpisFakture], [IznosFakture], [PoslodavacID], [PDV]) VALUES (1, 7, CAST(N'2021-01-01' AS Date), N'Faktura7', CAST(334000.00 AS Numeric(18, 2)), 7, CAST(7.00 AS Decimal(5, 2)))
GO
INSERT [dbo].[Faktura] ([ZadrugaID], [ID], [DatumFakture], [OpisFakture], [IznosFakture], [PoslodavacID], [PDV]) VALUES (1, 8, CAST(N'2020-01-03' AS Date), N'Faktura8', NULL, 2, CAST(5.00 AS Decimal(5, 2)))
GO
INSERT [dbo].[Faktura] ([ZadrugaID], [ID], [DatumFakture], [OpisFakture], [IznosFakture], [PoslodavacID], [PDV]) VALUES (1, 9, CAST(N'2021-01-01' AS Date), N'Faktura9', NULL, 6, CAST(2.00 AS Decimal(5, 2)))
GO
INSERT [dbo].[Faktura] ([ZadrugaID], [ID], [DatumFakture], [OpisFakture], [IznosFakture], [PoslodavacID], [PDV]) VALUES (1, 10, CAST(N'2020-01-02' AS Date), N'Faktura10', NULL, 7, CAST(5.00 AS Decimal(5, 2)))
GO
INSERT [dbo].[Faktura] ([ZadrugaID], [ID], [DatumFakture], [OpisFakture], [IznosFakture], [PoslodavacID], [PDV]) VALUES (1, 43, CAST(N'2021-01-20' AS Date), N'JovanaCovicFaktura', CAST(68000.00 AS Numeric(18, 2)), 43, CAST(17.00 AS Decimal(5, 2)))
GO
INSERT [dbo].[Faktura] ([ZadrugaID], [ID], [DatumFakture], [OpisFakture], [IznosFakture], [PoslodavacID], [PDV]) VALUES (1, 221, CAST(N'2020-05-30' AS Date), N'Usluge Marketing Managera', CAST(110000.00 AS Numeric(18, 2)), 331, CAST(20.00 AS Decimal(5, 2)))
GO
INSERT [dbo].[Grad] ([DrzavaID], [ID], [Naziv]) VALUES (1, 1, N'Beograd')
GO
INSERT [dbo].[Grad] ([DrzavaID], [ID], [Naziv]) VALUES (1, 2, N'Nis')
GO
INSERT [dbo].[Grad] ([DrzavaID], [ID], [Naziv]) VALUES (1, 3, N'Novi Sad')
GO
INSERT [dbo].[Grad] ([DrzavaID], [ID], [Naziv]) VALUES (2, 1, N'Banja Luka')
GO
INSERT [dbo].[Grad] ([DrzavaID], [ID], [Naziv]) VALUES (2, 2, N'Sarajevo')
GO
INSERT [dbo].[Grad] ([DrzavaID], [ID], [Naziv]) VALUES (2, 3, N'Mostar')
GO
INSERT [dbo].[Grad] ([DrzavaID], [ID], [Naziv]) VALUES (3, 1, N'Podrogrica')
GO
INSERT [dbo].[Grad] ([DrzavaID], [ID], [Naziv]) VALUES (3, 2, N'Kotor')
GO
INSERT [dbo].[Grad] ([DrzavaID], [ID], [Naziv]) VALUES (3, 3, N'Niksic')
GO
INSERT [dbo].[IznosPlate] ([KategorijaID], [PodkategorijaID], [PosaoID], [Datum], [JedinicnaCena]) VALUES (1, 1, 1, CAST(N'2020-12-01' AS Date), CAST(97000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[IznosPlate] ([KategorijaID], [PodkategorijaID], [PosaoID], [Datum], [JedinicnaCena]) VALUES (1, 1, 1, CAST(N'2020-12-12' AS Date), CAST(98000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[IznosPlate] ([KategorijaID], [PodkategorijaID], [PosaoID], [Datum], [JedinicnaCena]) VALUES (1, 1, 1, CAST(N'2020-12-13' AS Date), CAST(99000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[IznosPlate] ([KategorijaID], [PodkategorijaID], [PosaoID], [Datum], [JedinicnaCena]) VALUES (1, 1, 1, CAST(N'2020-12-14' AS Date), CAST(102000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[IznosPlate] ([KategorijaID], [PodkategorijaID], [PosaoID], [Datum], [JedinicnaCena]) VALUES (1, 1, 1, CAST(N'2021-01-09' AS Date), CAST(150000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[IznosPlate] ([KategorijaID], [PodkategorijaID], [PosaoID], [Datum], [JedinicnaCena]) VALUES (1, 1, 2, CAST(N'2020-12-12' AS Date), CAST(39000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[IznosPlate] ([KategorijaID], [PodkategorijaID], [PosaoID], [Datum], [JedinicnaCena]) VALUES (1, 1, 4, CAST(N'2020-12-10' AS Date), CAST(29000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[IznosPlate] ([KategorijaID], [PodkategorijaID], [PosaoID], [Datum], [JedinicnaCena]) VALUES (1, 1, 5, CAST(N'2020-12-10' AS Date), CAST(37000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[IznosPlate] ([KategorijaID], [PodkategorijaID], [PosaoID], [Datum], [JedinicnaCena]) VALUES (1, 1, 5, CAST(N'2020-12-12' AS Date), CAST(37500.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[IznosPlate] ([KategorijaID], [PodkategorijaID], [PosaoID], [Datum], [JedinicnaCena]) VALUES (1, 1, 7, CAST(N'2020-12-01' AS Date), CAST(90000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[IznosPlate] ([KategorijaID], [PodkategorijaID], [PosaoID], [Datum], [JedinicnaCena]) VALUES (3, 4, 6, CAST(N'2018-03-03' AS Date), CAST(112000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[IznosPlate] ([KategorijaID], [PodkategorijaID], [PosaoID], [Datum], [JedinicnaCena]) VALUES (3, 4, 6, CAST(N'2019-01-01' AS Date), CAST(120000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[IznosPlate] ([KategorijaID], [PodkategorijaID], [PosaoID], [Datum], [JedinicnaCena]) VALUES (3, 4, 6, CAST(N'2020-01-09' AS Date), CAST(130000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[IznosPlate] ([KategorijaID], [PodkategorijaID], [PosaoID], [Datum], [JedinicnaCena]) VALUES (3, 4, 6, CAST(N'2020-10-11' AS Date), CAST(250000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[IznosPlate] ([KategorijaID], [PodkategorijaID], [PosaoID], [Datum], [JedinicnaCena]) VALUES (3, 4, 6, CAST(N'2020-11-11' AS Date), CAST(270000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[IznosPlate] ([KategorijaID], [PodkategorijaID], [PosaoID], [Datum], [JedinicnaCena]) VALUES (3, 4, 6, CAST(N'2020-12-01' AS Date), CAST(299000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[IznosPlate] ([KategorijaID], [PodkategorijaID], [PosaoID], [Datum], [JedinicnaCena]) VALUES (4, 1, 1, CAST(N'2021-01-01' AS Date), CAST(300000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[IznosPlate] ([KategorijaID], [PodkategorijaID], [PosaoID], [Datum], [JedinicnaCena]) VALUES (10, 10, 43, CAST(N'2021-01-01' AS Date), CAST(45000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[IznosPlate] ([KategorijaID], [PodkategorijaID], [PosaoID], [Datum], [JedinicnaCena]) VALUES (10, 10, 43, CAST(N'2021-01-02' AS Date), CAST(50000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[IznosPlate] ([KategorijaID], [PodkategorijaID], [PosaoID], [Datum], [JedinicnaCena]) VALUES (22, 21, 41, CAST(N'2020-01-19' AS Date), CAST(50000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[IznosPlate] ([KategorijaID], [PodkategorijaID], [PosaoID], [Datum], [JedinicnaCena]) VALUES (22, 21, 41, CAST(N'2020-02-19' AS Date), CAST(65000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[Kategorija] ([ID], [Naziv]) VALUES (1, N'Ugostiteljstvo')
GO
INSERT [dbo].[Kategorija] ([ID], [Naziv]) VALUES (2, N'Administracija')
GO
INSERT [dbo].[Kategorija] ([ID], [Naziv]) VALUES (3, N'itt')
GO
INSERT [dbo].[Kategorija] ([ID], [Naziv]) VALUES (4, N'Obrazovanje')
GO
INSERT [dbo].[Kategorija] ([ID], [Naziv]) VALUES (10, N'Usluzne delatnosti')
GO
INSERT [dbo].[Kategorija] ([ID], [Naziv]) VALUES (22, N'Marketing')
GO
INSERT [dbo].[Opstina] ([DrzavaID], [GradID], [ID], [Naziv]) VALUES (1, 1, 1, N'Novi Beograd')
GO
INSERT [dbo].[Opstina] ([DrzavaID], [GradID], [ID], [Naziv]) VALUES (1, 1, 2, N'Cukarica')
GO
INSERT [dbo].[Opstina] ([DrzavaID], [GradID], [ID], [Naziv]) VALUES (1, 2, 1, N'Medijana')
GO
INSERT [dbo].[Opstina] ([DrzavaID], [GradID], [ID], [Naziv]) VALUES (1, 2, 2, N'Palilula')
GO
INSERT [dbo].[Opstina] ([DrzavaID], [GradID], [ID], [Naziv]) VALUES (1, 3, 1, N'NS')
GO
INSERT [dbo].[Opstina] ([DrzavaID], [GradID], [ID], [Naziv]) VALUES (1, 3, 2, N'Petrovaradin')
GO
INSERT [dbo].[Opstina] ([DrzavaID], [GradID], [ID], [Naziv]) VALUES (2, 1, 1, N'Stari Grad')
GO
INSERT [dbo].[Opstina] ([DrzavaID], [GradID], [ID], [Naziv]) VALUES (2, 1, 2, N'Novo Sarajevo')
GO
INSERT [dbo].[Opstina] ([DrzavaID], [GradID], [ID], [Naziv]) VALUES (2, 2, 1, N'Stari Grad')
GO
INSERT [dbo].[Opstina] ([DrzavaID], [GradID], [ID], [Naziv]) VALUES (2, 2, 2, N'BL')
GO
INSERT [dbo].[Opstina] ([DrzavaID], [GradID], [ID], [Naziv]) VALUES (2, 3, 1, N'Mostar')
GO
INSERT [dbo].[Opstina] ([DrzavaID], [GradID], [ID], [Naziv]) VALUES (2, 3, 2, N'Mostar')
GO
INSERT [dbo].[Opstina] ([DrzavaID], [GradID], [ID], [Naziv]) VALUES (3, 1, 1, N'Stari Grad')
GO
INSERT [dbo].[Opstina] ([DrzavaID], [GradID], [ID], [Naziv]) VALUES (3, 1, 2, N'Golubovci')
GO
INSERT [dbo].[Opstina] ([DrzavaID], [GradID], [ID], [Naziv]) VALUES (3, 2, 1, N'Kotor')
GO
INSERT [dbo].[Opstina] ([DrzavaID], [GradID], [ID], [Naziv]) VALUES (3, 2, 2, N'Kotor')
GO
INSERT [dbo].[Opstina] ([DrzavaID], [GradID], [ID], [Naziv]) VALUES (3, 3, 1, N'Niksic')
GO
INSERT [dbo].[Opstina] ([DrzavaID], [GradID], [ID], [Naziv]) VALUES (3, 3, 2, N'Niksic')
GO
INSERT [dbo].[PDV] ([UplataID], [ID], [IznosUProcentima]) VALUES (1, 1, CAST(5.00 AS Decimal(5, 2)))
GO
INSERT [dbo].[PDV] ([UplataID], [ID], [IznosUProcentima]) VALUES (1, 2, CAST(7.00 AS Decimal(5, 2)))
GO
INSERT [dbo].[PDV] ([UplataID], [ID], [IznosUProcentima]) VALUES (1, 3, CAST(100.00 AS Decimal(5, 2)))
GO
INSERT [dbo].[PDV] ([UplataID], [ID], [IznosUProcentima]) VALUES (1, 4, CAST(0.00 AS Decimal(5, 2)))
GO
INSERT [dbo].[Podkategorija] ([KategorijaID], [ID], [Naziv], [NazivKategorije]) VALUES (1, 1, N'Kuhinja', N'Ugostiteljstvo')
GO
INSERT [dbo].[Podkategorija] ([KategorijaID], [ID], [Naziv], [NazivKategorije]) VALUES (1, 2, N'odrzavanje', N'Ugostiteljstvo')
GO
INSERT [dbo].[Podkategorija] ([KategorijaID], [ID], [Naziv], [NazivKategorije]) VALUES (1, 3, N'posluga', N'Ugostiteljstvo')
GO
INSERT [dbo].[Podkategorija] ([KategorijaID], [ID], [Naziv], [NazivKategorije]) VALUES (2, 2, N'Kanc', N'Administracija')
GO
INSERT [dbo].[Podkategorija] ([KategorijaID], [ID], [Naziv], [NazivKategorije]) VALUES (3, 4, N'Back End', N'itt')
GO
INSERT [dbo].[Podkategorija] ([KategorijaID], [ID], [Naziv], [NazivKategorije]) VALUES (3, 6, N'front end', N'itt')
GO
INSERT [dbo].[Podkategorija] ([KategorijaID], [ID], [Naziv], [NazivKategorije]) VALUES (3, 7, N'php', N'itt')
GO
INSERT [dbo].[Podkategorija] ([KategorijaID], [ID], [Naziv], [NazivKategorije]) VALUES (4, 1, N'Prosvetni radnik', N'Obrazovanje')
GO
INSERT [dbo].[Podkategorija] ([KategorijaID], [ID], [Naziv], [NazivKategorije]) VALUES (10, 10, N'Usluzivanje', N'Usluzne delatnosti')
GO
INSERT [dbo].[Podkategorija] ([KategorijaID], [ID], [Naziv], [NazivKategorije]) VALUES (22, 21, N'ATL ', N'Marketing')
GO
INSERT [dbo].[Posao] ([KategorijaID], [PodkategorijaID], [ID], [Naziv], [OpisPosla], [PoslodavacID], [NazivPoslodavca], [Plata]) VALUES (1, 1, 1, N'Kuvar', N'Kuva', 3, N'Metropola', CAST(150000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[Posao] ([KategorijaID], [PodkategorijaID], [ID], [Naziv], [OpisPosla], [PoslodavacID], [NazivPoslodavca], [Plata]) VALUES (1, 1, 2, N'kuvar2', N'kuva', 2, N'hyatt ragency', CAST(39000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[Posao] ([KategorijaID], [PodkategorijaID], [ID], [Naziv], [OpisPosla], [PoslodavacID], [NazivPoslodavca], [Plata]) VALUES (1, 1, 4, N'Sanker', N'Sprema pica', 4, N'Gelato', CAST(29000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[Posao] ([KategorijaID], [PodkategorijaID], [ID], [Naziv], [OpisPosla], [PoslodavacID], [NazivPoslodavca], [Plata]) VALUES (1, 1, 5, N'Kuvar3', N'Sprema hranu', 5, N'HelgasPub', CAST(37500.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[Posao] ([KategorijaID], [PodkategorijaID], [ID], [Naziv], [OpisPosla], [PoslodavacID], [NazivPoslodavca], [Plata]) VALUES (1, 1, 7, N'kuvar', N'kuva hranu', 2, N'hyatt ragency', CAST(90000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[Posao] ([KategorijaID], [PodkategorijaID], [ID], [Naziv], [OpisPosla], [PoslodavacID], [NazivPoslodavca], [Plata]) VALUES (3, 4, 6, N'php', N'php defvv', 1, N'Holiday Inn', CAST(299000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[Posao] ([KategorijaID], [PodkategorijaID], [ID], [Naziv], [OpisPosla], [PoslodavacID], [NazivPoslodavca], [Plata]) VALUES (3, 4, 8, N'java', N'java', 1, N'Holiday Inn', NULL)
GO
INSERT [dbo].[Posao] ([KategorijaID], [PodkategorijaID], [ID], [Naziv], [OpisPosla], [PoslodavacID], [NazivPoslodavca], [Plata]) VALUES (4, 1, 1, N'Profesor Baza', N'Predaje baze podataka', 7, N'Levi9', CAST(300000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[Posao] ([KategorijaID], [PodkategorijaID], [ID], [Naziv], [OpisPosla], [PoslodavacID], [NazivPoslodavca], [Plata]) VALUES (10, 10, 9, N'usluga', N'usluzivanje', 4, N'Gelato', NULL)
GO
INSERT [dbo].[Posao] ([KategorijaID], [PodkategorijaID], [ID], [Naziv], [OpisPosla], [PoslodavacID], [NazivPoslodavca], [Plata]) VALUES (10, 10, 43, N'Prodavac', N'Prodaja robe', 43, N'Zara', CAST(50000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[Posao] ([KategorijaID], [PodkategorijaID], [ID], [Naziv], [OpisPosla], [PoslodavacID], [NazivPoslodavca], [Plata]) VALUES (22, 21, 41, N'Marketing Manager', N'Marketingiranje', 331, N'Lexa Company', CAST(65000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[Poslodavac] ([ID], [Naziv], [Telefon], [PIB], [TekuciRacun], [DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (1, N'Holiday Inn', N'0628094214', N'53423421344', N'098234095345', 1, 1, 1, 2, N'1                                                 ')
GO
INSERT [dbo].[Poslodavac] ([ID], [Naziv], [Telefon], [PIB], [TekuciRacun], [DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (2, N'hyatt ragency', N'0637984212', N'094182904124', N'809218442142', 1, 1, 1, 1, N'1                                                 ')
GO
INSERT [dbo].[Poslodavac] ([ID], [Naziv], [Telefon], [PIB], [TekuciRacun], [DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (3, N'Metropola', N'0694798124', N'43534234432', N'546456546456', 1, 1, 1, 1, N'2                                                 ')
GO
INSERT [dbo].[Poslodavac] ([ID], [Naziv], [Telefon], [PIB], [TekuciRacun], [DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (4, N'Gelato', N'0617894324', N'31234533455', N'6456435345345', 1, 1, 1, 1, N'1                                                 ')
GO
INSERT [dbo].[Poslodavac] ([ID], [Naziv], [Telefon], [PIB], [TekuciRacun], [DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (5, N'HelgasPub', N'06447984321', N'125534654665', N'094812412444', 1, 1, 1, 1, N'2                                                 ')
GO
INSERT [dbo].[Poslodavac] ([ID], [Naziv], [Telefon], [PIB], [TekuciRacun], [DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (6, N'IT Beograd', N'0678390124', N'8490128409124', N'40918284021', 1, 1, 1, 1, N'1                                                 ')
GO
INSERT [dbo].[Poslodavac] ([ID], [Naziv], [Telefon], [PIB], [TekuciRacun], [DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (7, N'Levi9', N'06390842981', N'4019284908', N'09128409214', 1, 1, 2, 2, N'2                                                 ')
GO
INSERT [dbo].[Poslodavac] ([ID], [Naziv], [Telefon], [PIB], [TekuciRacun], [DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (43, N'Zara', N'06738912789', N'41982749817', N'49817294872174', 1, 1, 2, 2, N'1                                                 ')
GO
INSERT [dbo].[Poslodavac] ([ID], [Naziv], [Telefon], [PIB], [TekuciRacun], [DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (331, N'Lexa Company', N'123 321 33', N'1120195', N'2234 8213 5125 0213', 1, 1, 2, 2, N'2                                                 ')
GO
INSERT [dbo].[PristupniFormular] ([StudentID], [ID], [DatumPopunjavanja], [ZadrugaID]) VALUES (8, 8, CAST(N'2019-12-31' AS Date), 1)
GO
INSERT [dbo].[PristupniFormular] ([StudentID], [ID], [DatumPopunjavanja], [ZadrugaID]) VALUES (1, 1, CAST(N'2020-01-08' AS Date), 1)
GO
INSERT [dbo].[PristupniFormular] ([StudentID], [ID], [DatumPopunjavanja], [ZadrugaID]) VALUES (1, 1, CAST(N'2020-01-09' AS Date), 1)
GO
INSERT [dbo].[PristupniFormular] ([StudentID], [ID], [DatumPopunjavanja], [ZadrugaID]) VALUES (2, 2, CAST(N'2020-02-25' AS Date), 1)
GO
INSERT [dbo].[PristupniFormular] ([StudentID], [ID], [DatumPopunjavanja], [ZadrugaID]) VALUES (44, 331, CAST(N'2020-02-19' AS Date), 1)
GO
INSERT [dbo].[PristupniFormular] ([StudentID], [ID], [DatumPopunjavanja], [ZadrugaID]) VALUES (3, 3, CAST(N'2020-04-03' AS Date), 1)
GO
INSERT [dbo].[PristupniFormular] ([StudentID], [ID], [DatumPopunjavanja], [ZadrugaID]) VALUES (4, 4, CAST(N'2020-04-15' AS Date), 1)
GO
INSERT [dbo].[PristupniFormular] ([StudentID], [ID], [DatumPopunjavanja], [ZadrugaID]) VALUES (5, 5, CAST(N'2020-05-01' AS Date), 1)
GO
INSERT [dbo].[PristupniFormular] ([StudentID], [ID], [DatumPopunjavanja], [ZadrugaID]) VALUES (6, 6, CAST(N'2020-07-07' AS Date), 1)
GO
INSERT [dbo].[PristupniFormular] ([StudentID], [ID], [DatumPopunjavanja], [ZadrugaID]) VALUES (8, 8, CAST(N'2020-12-30' AS Date), 1)
GO
INSERT [dbo].[PristupniFormular] ([StudentID], [ID], [DatumPopunjavanja], [ZadrugaID]) VALUES (43, 43, CAST(N'2021-01-20' AS Date), 1)
GO
INSERT [dbo].[StavkaFakture] ([ZadrugaID], [FakturaID], [ID], [RedniBroj], [OpisStavke], [IznosStavke]) VALUES (1, 1, 1, 1, N'Porezzz', CAST(6000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[StavkaFakture] ([ZadrugaID], [FakturaID], [ID], [RedniBroj], [OpisStavke], [IznosStavke]) VALUES (1, 1, 2, 2, N'Doprinosi', CAST(9000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[StavkaFakture] ([ZadrugaID], [FakturaID], [ID], [RedniBroj], [OpisStavke], [IznosStavke]) VALUES (1, 1, 3, 3, N'Prevoz', CAST(15000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[StavkaFakture] ([ZadrugaID], [FakturaID], [ID], [RedniBroj], [OpisStavke], [IznosStavke]) VALUES (1, 2, 1, 1, N'Porez', CAST(15000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[StavkaFakture] ([ZadrugaID], [FakturaID], [ID], [RedniBroj], [OpisStavke], [IznosStavke]) VALUES (1, 3, 1, 1, N'Porez', CAST(25000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[StavkaFakture] ([ZadrugaID], [FakturaID], [ID], [RedniBroj], [OpisStavke], [IznosStavke]) VALUES (1, 4, 1, 1, N'Porez', CAST(41000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[StavkaFakture] ([ZadrugaID], [FakturaID], [ID], [RedniBroj], [OpisStavke], [IznosStavke]) VALUES (1, 5, 1, 1, N'Porez', CAST(13000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[StavkaFakture] ([ZadrugaID], [FakturaID], [ID], [RedniBroj], [OpisStavke], [IznosStavke]) VALUES (1, 6, 1, 1, N'Porez', CAST(59200.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[StavkaFakture] ([ZadrugaID], [FakturaID], [ID], [RedniBroj], [OpisStavke], [IznosStavke]) VALUES (1, 7, 1, 1, N'Plata', CAST(300000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[StavkaFakture] ([ZadrugaID], [FakturaID], [ID], [RedniBroj], [OpisStavke], [IznosStavke]) VALUES (1, 7, 2, 2, N'Doprinosi', CAST(34000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[StavkaFakture] ([ZadrugaID], [FakturaID], [ID], [RedniBroj], [OpisStavke], [IznosStavke]) VALUES (1, 43, 1, 1, N'Prevoz', CAST(51000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[StavkaFakture] ([ZadrugaID], [FakturaID], [ID], [RedniBroj], [OpisStavke], [IznosStavke]) VALUES (1, 43, 2, 2, N'Doprinosi', CAST(17000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[StavkaFakture] ([ZadrugaID], [FakturaID], [ID], [RedniBroj], [OpisStavke], [IznosStavke]) VALUES (1, 221, 1, 1, N'Manager Markerting', CAST(75000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[StavkaFakture] ([ZadrugaID], [FakturaID], [ID], [RedniBroj], [OpisStavke], [IznosStavke]) VALUES (1, 221, 2, 2, N'Prekovremeni rad', CAST(35000.00 AS Numeric(18, 2)))
GO
INSERT [dbo].[Student] ([ID], [Ime], [Prezime], [Telefon], [BOP], [TekuciRacun]) VALUES (0, N'Ivan', N'Vasic', N'064213892', N'1238123123', N'312312321')
GO
INSERT [dbo].[Student] ([ID], [Ime], [Prezime], [Telefon], [BOP], [TekuciRacun]) VALUES (1, N'Andjela', N'Gajic', N'065123456', N'902184901284', N'1294081209481')
GO
INSERT [dbo].[Student] ([ID], [Ime], [Prezime], [Telefon], [BOP], [TekuciRacun]) VALUES (2, N'Marko', N'Gajic', N'0667873213', N'5464564566', N'65676123234')
GO
INSERT [dbo].[Student] ([ID], [Ime], [Prezime], [Telefon], [BOP], [TekuciRacun]) VALUES (3, N'Stefan', N'Ilic', N'0631480923', N'8677456234', N'11145345434')
GO
INSERT [dbo].[Student] ([ID], [Ime], [Prezime], [Telefon], [BOP], [TekuciRacun]) VALUES (4, N'nina', N'joksic', N'063202842', N'83902183932', N'1382093213')
GO
INSERT [dbo].[Student] ([ID], [Ime], [Prezime], [Telefon], [BOP], [TekuciRacun]) VALUES (5, N'Jovana', N'Ilic', N'067098238', N'10294812489', N'4091284234')
GO
INSERT [dbo].[Student] ([ID], [Ime], [Prezime], [Telefon], [BOP], [TekuciRacun]) VALUES (6, N'Kosana', N'Gajic', N'0698872903', N'8901284091284', N'1098490128449')
GO
INSERT [dbo].[Student] ([ID], [Ime], [Prezime], [Telefon], [BOP], [TekuciRacun]) VALUES (7, N'Alen', N'Hamza', N'06128371283', N'381092830912', N'390128390128')
GO
INSERT [dbo].[Student] ([ID], [Ime], [Prezime], [Telefon], [BOP], [TekuciRacun]) VALUES (8, N'Ivan', N'Pavlovic', N'067213908', N'091284908908', N'12094809148')
GO
INSERT [dbo].[Student] ([ID], [Ime], [Prezime], [Telefon], [BOP], [TekuciRacun]) VALUES (43, N'Jovana', N'Covic', N'069231238', N'41902849012', N'4091824098')
GO
INSERT [dbo].[Student] ([ID], [Ime], [Prezime], [Telefon], [BOP], [TekuciRacun]) VALUES (44, N'Alexa', N'Milosevic', N'+1 564 526 2523 ', N'1506994710022', N'066 958 942 210')
GO
INSERT [dbo].[StudentOstalo] ([ID], [Email], [DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (0, N'ivan@gmail.com', 1, 1, 1, 1, N'1                                                 ')
GO
INSERT [dbo].[StudentOstalo] ([ID], [Email], [DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (1, N'andjela@gmail.com', 1, 1, 1, 2, N'1                                                 ')
GO
INSERT [dbo].[StudentOstalo] ([ID], [Email], [DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (2, N'markogajic@gmail.com', 1, 1, 1, 2, N'1                                                 ')
GO
INSERT [dbo].[StudentOstalo] ([ID], [Email], [DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (3, N'stefan@gmail.com', 2, 2, 2, 2, N'2                                                 ')
GO
INSERT [dbo].[StudentOstalo] ([ID], [Email], [DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (4, N'nina@gmail.com', 1, 1, 1, 1, N'2                                                 ')
GO
INSERT [dbo].[StudentOstalo] ([ID], [Email], [DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (5, N'jovana@gmail.com', 1, 1, 1, 1, N'1                                                 ')
GO
INSERT [dbo].[StudentOstalo] ([ID], [Email], [DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (6, N'kosana@sportv.com', 1, 1, 1, 2, N'1                                                 ')
GO
INSERT [dbo].[StudentOstalo] ([ID], [Email], [DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (7, N'alen@gmail.com', 1, 1, 1, 1, N'2                                                 ')
GO
INSERT [dbo].[StudentOstalo] ([ID], [Email], [DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (8, N'ivan@gmail.com', 2, 2, 1, 1, N'1                                                 ')
GO
INSERT [dbo].[StudentOstalo] ([ID], [Email], [DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (43, N'jovana@gmail.com', 3, 3, 2, 2, N'2                                                 ')
GO
INSERT [dbo].[StudentOstalo] ([ID], [Email], [DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (44, N'lexa.crew@gmail.com', 1, 1, 1, 2, N'2                                                 ')
GO
INSERT [dbo].[TrojniUgovor] ([ID], [ZadrugaID], [StudentID], [PoslodavacID], [KategorijaID], [PodkategorijaID], [RadnoMestoID], [PlataIznos], [DatumOD], [DatumDO], [Info]) VALUES (1, 1, 1, 1, 3, 4, 6, N'299000.00', CAST(N'2020-01-02' AS Date), CAST(N'2022-01-02' AS Date), N'Andjela,Gajic,BOX,Holiday Inn,php')
GO
INSERT [dbo].[TrojniUgovor] ([ID], [ZadrugaID], [StudentID], [PoslodavacID], [KategorijaID], [PodkategorijaID], [RadnoMestoID], [PlataIznos], [DatumOD], [DatumDO], [Info]) VALUES (2, 1, 6, 4, 10, 10, 9, N'Nije uneta plata za izabrani posao', CAST(N'2020-01-01' AS Date), CAST(N'2022-01-01' AS Date), N'Kosana,Gajic,BOX,Gelato,usluga')
GO
INSERT [dbo].[TrojniUgovor] ([ID], [ZadrugaID], [StudentID], [PoslodavacID], [KategorijaID], [PodkategorijaID], [RadnoMestoID], [PlataIznos], [DatumOD], [DatumDO], [Info]) VALUES (3, 1, 6, 4, 1, 1, 4, N'29000.00', CAST(N'2020-01-01' AS Date), CAST(N'2022-01-01' AS Date), N'Kosana,Gajic,BOX,Gelato,Sanker')
GO
INSERT [dbo].[TrojniUgovor] ([ID], [ZadrugaID], [StudentID], [PoslodavacID], [KategorijaID], [PodkategorijaID], [RadnoMestoID], [PlataIznos], [DatumOD], [DatumDO], [Info]) VALUES (4, 1, 5, 3, 1, 1, 1, N'150000.00', CAST(N'2020-01-01' AS Date), CAST(N'2022-01-01' AS Date), N'Jovana,Ilic,BOX,Metropol,Kuvar')
GO
INSERT [dbo].[TrojniUgovor] ([ID], [ZadrugaID], [StudentID], [PoslodavacID], [KategorijaID], [PodkategorijaID], [RadnoMestoID], [PlataIznos], [DatumOD], [DatumDO], [Info]) VALUES (5, 1, 7, 4, 1, 1, 4, N'29000.00', CAST(N'2020-01-01' AS Date), CAST(N'2022-01-01' AS Date), N'Alen,Hamza,BOX,Gelato,Sanker')
GO
INSERT [dbo].[TrojniUgovor] ([ID], [ZadrugaID], [StudentID], [PoslodavacID], [KategorijaID], [PodkategorijaID], [RadnoMestoID], [PlataIznos], [DatumOD], [DatumDO], [Info]) VALUES (6, 1, 8, 7, 4, 1, 1, N'300000.00', CAST(N'2021-01-01' AS Date), CAST(N'2023-01-01' AS Date), N'Ivan,Pavlovic,BOX,Levi9,Profesor Baza')
GO
INSERT [dbo].[TrojniUgovor] ([ID], [ZadrugaID], [StudentID], [PoslodavacID], [KategorijaID], [PodkategorijaID], [RadnoMestoID], [PlataIznos], [DatumOD], [DatumDO], [Info]) VALUES (41, 1, 44, 331, 22, 21, 41, N'65000.00', CAST(N'2020-02-21' AS Date), CAST(N'2020-05-21' AS Date), N'Alexa,Milosevic,BOX,Lexa Company,Marketing Manager')
GO
INSERT [dbo].[TrojniUgovor] ([ID], [ZadrugaID], [StudentID], [PoslodavacID], [KategorijaID], [PodkategorijaID], [RadnoMestoID], [PlataIznos], [DatumOD], [DatumDO], [Info]) VALUES (43, 1, 43, 43, 10, 10, 43, N'50000.00', CAST(N'2021-01-20' AS Date), CAST(N'2021-07-20' AS Date), N'Jovana,Covic,BOX,Zara,Prodavac')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (1, 1, 1, 1, N'Nehruova')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (1, 1, 1, 2, N'Gandijeva')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (1, 1, 2, 1, N'Cukarica ulica 1')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (1, 1, 2, 2, N'Cukarica ulica 2')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (1, 2, 1, 1, N'Medijana ulica 1 ')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (1, 2, 1, 2, N'medijana ulica 2')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (1, 2, 2, 1, N'paliluca ulica 1')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (1, 2, 2, 2, N'palilulca ulica 2')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (1, 3, 1, 1, N'ns ulica 1')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (1, 3, 1, 2, N'ns ulica 2')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (1, 3, 2, 1, N'petrovaradin ulica 1')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (1, 3, 2, 2, N'petrovaradin ulica 2')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (2, 1, 1, 1, N'stari grad ulica1')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (2, 1, 1, 2, N'stari grad ulica 2')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (2, 1, 2, 1, N'Novo Sarajevo ulica1')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (2, 1, 2, 2, N'Novo Sarajevo ulica 2')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (2, 2, 1, 1, N'Stari Grad ulica1')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (2, 2, 1, 2, N'Stari Grad ulica 2')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (2, 2, 2, 1, N'bl ulica 1')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (2, 2, 2, 2, N'bl ulica 2')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (2, 3, 1, 1, N'mostar ulica 1')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (2, 3, 1, 2, N'mostar ulica 2')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (2, 3, 2, 1, N'mostar2 ulica 1')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (2, 3, 2, 2, N'mostar2 ulica 2')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (3, 1, 1, 1, N'stari grad ulica1')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (3, 1, 1, 2, N'stari grad ulica2')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (3, 1, 2, 1, N'Golubovci ulica 1')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (3, 1, 2, 2, N'Golubovci ulica 2')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (3, 2, 1, 1, N'kotor ulica 1 ')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (3, 2, 1, 2, N'kotor ulica 2')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (3, 2, 2, 1, N'kotor2 ulica 1')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (3, 2, 2, 2, N'kotor2 ulica 2')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (3, 3, 1, 1, N'niksic ulica 1')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (3, 3, 1, 2, N'niksic ulica 2')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (3, 3, 2, 1, N'niksic2 ulica 1')
GO
INSERT [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID], [Naziv]) VALUES (3, 3, 2, 2, N'niksic2 ulica 2')
GO
INSERT [dbo].[Zadruga] ([ID], [Naziv], [Telefon], [PIB], [TekuciRacun], [DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID]) VALUES (1, N'BOX', N'06898234', N'80942184214', N'809412804412', 1, 1, 1, 1, N'1                                                 ')
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [Index_NazivPosla]    Script Date: 1/28/2021 1:22:12 PM ******/
CREATE NONCLUSTERED INDEX [Index_NazivPosla] ON [dbo].[Posao]
(
	[Naziv] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [Index_PoslodavacID]    Script Date: 1/28/2021 1:22:12 PM ******/
CREATE NONCLUSTERED INDEX [Index_PoslodavacID] ON [dbo].[Posao]
(
	[PoslodavacID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [UQ__TrojniUg__3214EC26765AD3DA]    Script Date: 1/28/2021 1:22:12 PM ******/
ALTER TABLE [dbo].[TrojniUgovor] ADD UNIQUE NONCLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Broj]  WITH CHECK ADD  CONSTRAINT [FK_Broj] FOREIGN KEY([DrzavaID], [GradID], [OpstinaID], [UlicaID])
REFERENCES [dbo].[Ulica] ([DrzavaID], [GradID], [OpstinaID], [ID])
GO
ALTER TABLE [dbo].[Broj] CHECK CONSTRAINT [FK_Broj]
GO
ALTER TABLE [dbo].[Faktura]  WITH CHECK ADD  CONSTRAINT [FK_Faktura] FOREIGN KEY([ZadrugaID])
REFERENCES [dbo].[Zadruga] ([ID])
GO
ALTER TABLE [dbo].[Faktura] CHECK CONSTRAINT [FK_Faktura]
GO
ALTER TABLE [dbo].[Faktura]  WITH CHECK ADD  CONSTRAINT [FK_Faktura2] FOREIGN KEY([PoslodavacID])
REFERENCES [dbo].[Poslodavac] ([ID])
GO
ALTER TABLE [dbo].[Faktura] CHECK CONSTRAINT [FK_Faktura2]
GO
ALTER TABLE [dbo].[Grad]  WITH CHECK ADD  CONSTRAINT [FK_Grad] FOREIGN KEY([DrzavaID])
REFERENCES [dbo].[Drzava] ([ID])
GO
ALTER TABLE [dbo].[Grad] CHECK CONSTRAINT [FK_Grad]
GO
ALTER TABLE [dbo].[IznosPlate]  WITH CHECK ADD  CONSTRAINT [FK_IznosPlate] FOREIGN KEY([KategorijaID], [PodkategorijaID], [PosaoID])
REFERENCES [dbo].[Posao] ([KategorijaID], [PodkategorijaID], [ID])
GO
ALTER TABLE [dbo].[IznosPlate] CHECK CONSTRAINT [FK_IznosPlate]
GO
ALTER TABLE [dbo].[Opstina]  WITH CHECK ADD  CONSTRAINT [FK_Opstina] FOREIGN KEY([DrzavaID], [GradID])
REFERENCES [dbo].[Grad] ([DrzavaID], [ID])
GO
ALTER TABLE [dbo].[Opstina] CHECK CONSTRAINT [FK_Opstina]
GO
ALTER TABLE [dbo].[Podkategorija]  WITH CHECK ADD  CONSTRAINT [FK_Podkategorija] FOREIGN KEY([KategorijaID])
REFERENCES [dbo].[Kategorija] ([ID])
GO
ALTER TABLE [dbo].[Podkategorija] CHECK CONSTRAINT [FK_Podkategorija]
GO
ALTER TABLE [dbo].[Posao]  WITH CHECK ADD FOREIGN KEY([PoslodavacID])
REFERENCES [dbo].[Poslodavac] ([ID])
GO
ALTER TABLE [dbo].[Poslodavac]  WITH CHECK ADD  CONSTRAINT [FK_Poslodavac] FOREIGN KEY([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID])
REFERENCES [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID])
GO
ALTER TABLE [dbo].[Poslodavac] CHECK CONSTRAINT [FK_Poslodavac]
GO
ALTER TABLE [dbo].[PristupniFormular]  WITH CHECK ADD  CONSTRAINT [FK_PristupniFormular1] FOREIGN KEY([StudentID])
REFERENCES [dbo].[Student] ([ID])
GO
ALTER TABLE [dbo].[PristupniFormular] CHECK CONSTRAINT [FK_PristupniFormular1]
GO
ALTER TABLE [dbo].[PristupniFormular]  WITH CHECK ADD  CONSTRAINT [FK_PristupniFormular2] FOREIGN KEY([ZadrugaID])
REFERENCES [dbo].[Zadruga] ([ID])
GO
ALTER TABLE [dbo].[PristupniFormular] CHECK CONSTRAINT [FK_PristupniFormular2]
GO
ALTER TABLE [dbo].[StavkaFakture]  WITH CHECK ADD  CONSTRAINT [FK_StavkaFakture] FOREIGN KEY([ZadrugaID], [FakturaID])
REFERENCES [dbo].[Faktura] ([ZadrugaID], [ID])
GO
ALTER TABLE [dbo].[StavkaFakture] CHECK CONSTRAINT [FK_StavkaFakture]
GO
ALTER TABLE [dbo].[StudentOstalo]  WITH CHECK ADD  CONSTRAINT [FK_StudentOstalo] FOREIGN KEY([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID])
REFERENCES [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID])
GO
ALTER TABLE [dbo].[StudentOstalo] CHECK CONSTRAINT [FK_StudentOstalo]
GO
ALTER TABLE [dbo].[TrojniUgovor]  WITH CHECK ADD  CONSTRAINT [FK_TU_Poslodavac] FOREIGN KEY([PoslodavacID])
REFERENCES [dbo].[Poslodavac] ([ID])
GO
ALTER TABLE [dbo].[TrojniUgovor] CHECK CONSTRAINT [FK_TU_Poslodavac]
GO
ALTER TABLE [dbo].[TrojniUgovor]  WITH CHECK ADD  CONSTRAINT [FK_TU_RadnoMesto] FOREIGN KEY([KategorijaID], [PodkategorijaID], [RadnoMestoID])
REFERENCES [dbo].[Posao] ([KategorijaID], [PodkategorijaID], [ID])
GO
ALTER TABLE [dbo].[TrojniUgovor] CHECK CONSTRAINT [FK_TU_RadnoMesto]
GO
ALTER TABLE [dbo].[TrojniUgovor]  WITH CHECK ADD  CONSTRAINT [FK_TU_Student] FOREIGN KEY([StudentID])
REFERENCES [dbo].[Student] ([ID])
GO
ALTER TABLE [dbo].[TrojniUgovor] CHECK CONSTRAINT [FK_TU_Student]
GO
ALTER TABLE [dbo].[TrojniUgovor]  WITH CHECK ADD  CONSTRAINT [FK_TU_Zadruga] FOREIGN KEY([ZadrugaID])
REFERENCES [dbo].[Zadruga] ([ID])
GO
ALTER TABLE [dbo].[TrojniUgovor] CHECK CONSTRAINT [FK_TU_Zadruga]
GO
ALTER TABLE [dbo].[Ulica]  WITH CHECK ADD  CONSTRAINT [FK_Ulica] FOREIGN KEY([DrzavaID], [GradID], [OpstinaID])
REFERENCES [dbo].[Opstina] ([DrzavaID], [GradID], [ID])
GO
ALTER TABLE [dbo].[Ulica] CHECK CONSTRAINT [FK_Ulica]
GO
ALTER TABLE [dbo].[Zadruga]  WITH CHECK ADD  CONSTRAINT [FK_Zadruga] FOREIGN KEY([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID])
REFERENCES [dbo].[Broj] ([DrzavaID], [GradID], [OpstinaID], [UlicaID], [BrojID])
GO
ALTER TABLE [dbo].[Zadruga] CHECK CONSTRAINT [FK_Zadruga]
GO
/****** Object:  StoredProcedure [dbo].[IznosFakture]    Script Date: 1/28/2021 1:22:12 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[IznosFakture]
	@IDFaktura int
	AS
	BEGIN
	declare @ukupno numeric(18,2)
	select @ukupno=SUM(IznosStavke) FROM  StavkaFakture
	WHERE FakturaID=@IDFaktura ;
	DISABLE TRIGGER ZabranaIzmeneIznosaFakture ON Faktura;
	UPDATE Faktura set IznosFakture=@ukupno WHERE ID=@IDFaktura;
	ENABLE TRIGGER ZabranaIzmeneIznosaFakture ON Faktura;
	END
GO
/****** Object:  StoredProcedure [dbo].[PlataProc]    Script Date: 1/28/2021 1:22:12 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[PlataProc] 
	@IDPosao int , @Idkategorija int, @idpodkategorija int
	AS 
	BEGIN
	DECLARE @plata numeric(18,2);
	SELECT @plata=JedinicnaCena FROM IznosPlate
	WHERE PosaoID=@IDPosao AND 
			Datum=(SELECT MAX(Datum) FROM IznosPlate WHERE PosaoID=@IDPosao AND KategorijaId=@Idkategorija AND PodkategorijaID=@idpodkategorija and
	Datum<=CURRENT_TIMESTAMP);
	DISABLE TRIGGER ZabranaUnosaPlate ON Posao;
	UPDATE Posao SET Plata=@plata WHERE ID=@IDPosao and KategorijaId=@idkategorija and PodkategorijaID=@idpodkategorija;
	ENABLE TRIGGER ZabranaUnosaPlate ON Posao;
	END
GO
USE [master]
GO
ALTER DATABASE [BOX] SET  READ_WRITE 
GO
