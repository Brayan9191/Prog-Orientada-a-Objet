-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3307
-- Tiempo de generación: 11-04-2025 a las 18:38:19
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `app`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `app`
--

CREATE TABLE `app` (
  `id_App` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `atencion_al_cliente`
--

CREATE TABLE `atencion_al_cliente` (
  `id_Atencion_al_cliente` int(10) NOT NULL,
  `Horario` text NOT NULL,
  `Correo` varchar(50) NOT NULL,
  `Lin_Telefonicas` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `camb_y_devol`
--

CREATE TABLE `camb_y_devol` (
  `id_Camb_y_devol` int(10) NOT NULL,
  `Pol_de_retractos` varchar(100) NOT NULL,
  `Pol_garantias` varchar(100) NOT NULL,
  `Pol_de_cambios` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carrito`
--

CREATE TABLE `carrito` (
  `id_Carrito` int(10) NOT NULL,
  `Cant_prod_en_carrito` int(10) NOT NULL,
  `Finalizar_compra` varchar(20) NOT NULL,
  `Volver_al_inicio` varchar(20) NOT NULL,
  `Producto` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `enc_satisfaccion`
--

CREATE TABLE `enc_satisfaccion` (
  `id_Enc_satisfaccion` int(10) NOT NULL,
  `Pregunta` varchar(100) NOT NULL,
  `Enviar` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `favoritos`
--

CREATE TABLE `favoritos` (
  `id_Favoritos` int(10) NOT NULL,
  `Productos` varchar(100) NOT NULL,
  `Filtros` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `filtros`
--

CREATE TABLE `filtros` (
  `id_Filtros` int(10) NOT NULL,
  `Diseño` varchar(100) NOT NULL,
  `Color` varchar(100) NOT NULL,
  `Tipo` varchar(100) NOT NULL,
  `Material` varchar(100) NOT NULL,
  `Gama_precio` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `guia_de_tallas`
--

CREATE TABLE `guia_de_tallas` (
  `id_Guia_de_tallas` int(10) NOT NULL,
  `Enterizo` varchar(100) NOT NULL,
  `Brasier` varchar(100) NOT NULL,
  `Falda` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `informacion`
--

CREATE TABLE `informacion` (
  `id_Informacion` int(10) NOT NULL,
  `Camb_y_devol` text NOT NULL,
  `Pol_de_envios` text NOT NULL,
  `Enc_Satisfaccion` text NOT NULL,
  `Guia_de_Tallas` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `login`
--

CREATE TABLE `login` (
  `id_Login` int(10) NOT NULL,
  `Telefono` int(10) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Contraseña` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `paginas`
--

CREATE TABLE `paginas` (
  `id_Pag` int(10) NOT NULL,
  `ProdPag` varchar(50) NOT NULL,
  `AtCPag` int(11) NOT NULL,
  `InfoPag` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pag_principal`
--

CREATE TABLE `pag_principal` (
  `id_Pag_Principal` int(10) NOT NULL,
  `Ruleta_Imagenes` int(10) NOT NULL,
  `Productos` geometry NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registrarse`
--

CREATE TABLE `registrarse` (
  `id_Regis` int(10) NOT NULL,
  `TelRegis` int(10) NOT NULL,
  `WhatRegis` int(10) NOT NULL,
  `NomRegis` varchar(50) NOT NULL,
  `EmailRegis` varchar(100) NOT NULL,
  `ContRegis` varchar(30) NOT NULL,
  `DirecRegis` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
