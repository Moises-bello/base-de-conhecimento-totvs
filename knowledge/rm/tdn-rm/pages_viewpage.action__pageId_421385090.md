---
content_hash: 2ad35aec776ae605d41abe4302c3963ec5cebb8fc921c52ce1f906e335893641
fetched_at: '2026-06-29T00:09:13.695735+00:00'
page_id: '421385090'
product: rm
source: tdn-rm
title: Automatização do processo de Cotação de Insumos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385090
version: 2
---

O processo de automatização de Cotação de Insumos, permite automatizar a cotação gerando preços com base nos índices (Ex.: INCC) de cotação informando a moeda indexadora e o intervalo de data ou intervalo de período do cronograma.  
O processo de Cotação de Insumos cria ou atualiza apenas 1 preço, seja aplicando o fator multiplicador, a vigência para o período de cronograma ou inserindo um novo valor para o preço do insumo manualmente.  
Com a automatização utilizando a tabela de cotação do sistema, na terceira tela do Assistente de Cotação de Preços é possível escolher os insumos e clicar no botão "Cotação utilizando índices".  
Feito isso irá aparecer um campo para informar a moeda indexadora, um campo para informar um intervalo de data para o qual se deseja aplicar os índices, um outro com um intervalo de períodos de cronograma (caso deseje utilizar as datas dos períodos) e um campo para escolher quais cronogramas (previsto, medido e realizado) se deseja aplicar a vigência dos preços, além de um botão para confirmar os dados e outro para cancelar a inserção.  
Se for informado um intervalo de datas, o intervalo de períodos será desconsiderado. Caso contrário, ou seja, os campos de intervalo de datas estejam em branco será considerado o intervalo de períodos.

**Atenção!**  
O intervalo de períodos será definido por padrão ao clicar no botão de "Cotação utilizando índices" com o período inicial e final definido nos parâmetros de projeto.  
 Ao clicar no botão de confirmação, para os insumos marcados, o processo irá criar preços com vigência baseado nas cotações da moeda indexadora escolhida dentro do intervalo de datas ou períodos de cronograma.

**Observação:**  
O nome do preço a ser criado será formado da seguinte forma: Cotação {índice} em 15/10/2014. Onde a data no final do preço será a data em que o processo foi executado

   
**Atenção!**  
Para utilizar a automatização utilizando índices de cotação o projeto deverá estar parametrizado através do menu Opções | Parâmetros | TOTVS Obras e Projetos | Projetos | aba Cálculo | subaba BDI, para trabalhar com vigência de preço, para manter preços distintos. Se não estiver utilizando vigência de preços o botão não será exibido.  
Se o parâmetro de projeto, "Utiliza Indexação" em Opções | Parâmetros | TOTVS Obras e Projetos | Projetos | aba Cálculo | subaba Outros, estiver marcado, o preço salvo será o preço cotado e não será aplicado nenhum índice de cotação ao mesmo pelo processo. Para tanto será salvo a moeda/índice escolhida no processo como moeda/índice indexadora no preço e a data de atualização do preço será a data definida no parâmetro de projeto "Data base para Indexação". Para que os novos preços sejam aplicados deverá ser executado o processo de "Calcular Preços" na visão de Insumos.
