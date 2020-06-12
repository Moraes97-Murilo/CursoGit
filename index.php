<?php
//script teste do curso de PHP JEDAI
	$azul = '<div style="width:1500px;height:14px;background:blue;">TESTE</div>';
	//função para selecionar um número de caracteres dentro de uma string
	$texto = 'I grew up in a town there are famous as a place from movie scenes the noise is aways loud there are sirens all around and the streets are mean';

	echo substr($texto,1,15);

echo $azul;
	//função para atribuir um índice para cada item dentro de uma string e transformar em um ARRAY, utilizando como separador o ESPAÇO ou outra coisa que vier no explode

	$nome = 'Murilo Alves Moraes';
	$nomeS = explode(' ', $nome);

	print_r($nomeS);

echo $azul;

	//é possível fazer o oposto com implode
	$arr = [5,8,9,7,5];
	$arrI = implode('', $arr);

	echo $arrI;

echo $azul;

	//aprendendo a usar trip_tags para tirar todos os códigos html
	echo strip_tags($azul);

echo $azul;
	//Mostrar código nem o navegador interpretar com htmlentities
	echo htmlentities($azul);
?>
