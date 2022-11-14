-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 14-11-2022 a las 15:08:44
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `rh`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `puesto`
--

CREATE TABLE `puesto` (
  `idPuesto` int(3) NOT NULL,
  `nomPue` varchar(200) NOT NULL,
  `apellidos` varchar(200) NOT NULL,
  `edad` int(3) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `idCuenta` int(20) NOT NULL,
  `servidoresAntes` varchar(3) NOT NULL,
  `idiomas` varchar(200) NOT NULL,
  `habilidades` varchar(200) NOT NULL,
  `idServidor` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `puesto`
--

INSERT INTO `puesto` (`idPuesto`, `nomPue`, `apellidos`, `edad`, `correo`, `idCuenta`, `servidoresAntes`, `idiomas`, `habilidades`, `idServidor`) VALUES
(1, 'Jocelyn ', 'Flores Reyes', 17, 'floresjocelyn@gmail.com', 123, 'Sí', 'Inglés', 'asdas', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `requisi`
--

CREATE TABLE `requisi` (
  `idRequisicion` int(5) NOT NULL,
  `nomReq` varchar(200) NOT NULL,
  `conducta` varchar(30) NOT NULL,
  `reglas` varchar(30) NOT NULL,
  `autorizar` tinyint(5) NOT NULL,
  `idPuesto` int(5) NOT NULL,
  `idServidor` int(5) NOT NULL,
  `nomAutoriza` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `requisi`
--

INSERT INTO `requisi` (`idRequisicion`, `nomReq`, `conducta`, `reglas`, `autorizar`, `idPuesto`, `idServidor`, `nomAutoriza`) VALUES
(1, 'Domini', 'No', 'No', 1, 1, 1, 'Grisel');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `servidor`
--

CREATE TABLE `servidor` (
  `idServidor` int(5) NOT NULL,
  `nomServ` varchar(200) NOT NULL,
  `DireccionIP` int(20) NOT NULL,
  `MaxPersonas` int(3) NOT NULL,
  `ubicacion` varchar(200) NOT NULL,
  `antiguedad` date NOT NULL,
  `Nointegrantes` int(3) NOT NULL,
  `nomPropietario` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `servidor`
--

INSERT INTO `servidor` (`idServidor`, `nomServ`, `DireccionIP`, `MaxPersonas`, `ubicacion`, `antiguedad`, `Nointegrantes`, `nomPropietario`) VALUES
(1, 'Server Minecraft', 345, 22, 'kdfglss', '1998-11-11', 5, 'Andrew Garfield'),
(2, 'Mineplex', 2349, 22, 'México', '2016-02-07', 7, 'Grisel'),
(3, 'Grand Theft Minecart', 444443, 11, 'Mexico', '2022-02-11', 5, 'Gabriel'),
(4, 'PixelmonCraft', 5345, 56, 'España', '2011-11-18', 22, 'Gabo');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `puesto`
--
ALTER TABLE `puesto`
  ADD PRIMARY KEY (`idPuesto`),
  ADD KEY `idServidor` (`idServidor`);

--
-- Indices de la tabla `requisi`
--
ALTER TABLE `requisi`
  ADD PRIMARY KEY (`idRequisicion`),
  ADD KEY `idPuesto` (`idPuesto`),
  ADD KEY `idServidor` (`idServidor`);

--
-- Indices de la tabla `servidor`
--
ALTER TABLE `servidor`
  ADD PRIMARY KEY (`idServidor`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `puesto`
--
ALTER TABLE `puesto`
  MODIFY `idPuesto` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `requisi`
--
ALTER TABLE `requisi`
  MODIFY `idRequisicion` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `servidor`
--
ALTER TABLE `servidor`
  MODIFY `idServidor` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
