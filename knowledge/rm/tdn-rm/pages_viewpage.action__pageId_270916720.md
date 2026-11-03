---
content_hash: d876d443fd348c8ebeaf11515e5a04e479e85b9ad3a9f4bd8066a19f84897c8c
fetched_at: '2026-06-29T00:08:25.516260+00:00'
page_id: '270916720'
product: rm
source: tdn-rm
title: Exportar uma visão para um formato específico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270916720
version: 17
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Exportação com reconhecimento de dados**

## **01. VISÃO GERAL**

Exportação de uma visão do sistema em um determinado formato de documentação.

## **02. EXEMPLO DE UTILIZAÇÃO**

 Em várias visões do sistema é possível exportar suas informações para documento especifico, Os tipos disponíveis para a operação são::

* CSV
* XLS
* PDF
* XLSX
* TXT
* RTF

Nos passos abaixo demostramos como realizar o processo de exportação de dados de uma visão para o Microsoft Excel.

**Exportando dados de uma visão**

Depois de carregada uma visão do sistema. Selecione “Exportar dados da visão” e escolha o formato desejado.

Avance o processo e selecione o destino de exportação.

Atenção!

As opções Google Docs e By-You-ECM **não** estão disponíveis a partir da versão 12.1.26

Defina o local onde o arquivo será salvo e digite o nome que desejar.

Será exibida uma mensagem informando sobre o sucesso da exportação;

Caso clique em "sim" será aberto o documento.

Atenção!

Se alguma coluna da visão contém imagem, ao ser exportada para XLS ou XLSX no lugar da imagem será exportado um identificador para a referida célula. Ressalta-se que o próprio Excel não permite que uma imagem seja atribuída como conteúdo de uma célula.

false

**Versão:** 12.01.XX

## **03. EXPORTAÇÃO COM RECONHECIMENTO DE DADOS**

 A opção "Exportação com reconhecimento de dados" apresenta desempenho e uso de memória aprimorados. Escolha esta opção se precisar processar e analisar dados massivos exportados no MS Excel. Opção disponível apenas para exportação para XLS e XLSX.

Atenção!

Quando exportamos grandes quantidades de dados para XLSX podemos nos deparar com erros relacionados ao limite de 1.048.576 linhas suportadas por este formato, mesmo que o total de linhas selecionadas seja inferior a este limite. Isso ocorre porque algumas linhas são mescladas, por isso são utilizadas mais linhas do que a quantidade selecionada. Para estes casos recomendamos o uso desta nova opção na exportação.

**Exemplo**: Selecionei 900.000 linhas para serem exportadas e quando abro o Excel percebo que foram utilizadas 942.640 linhas porque várias dessas linhas tiveram seu conteúdo mesclado pelo próprio Excel. Na imagem abaixo, marquei de amarelo algumas células mescladas que eu expandi para melhor visualização. E coloquei setas vermelhas mostrando outras linhas que estão mescladas, porém não expandi para mostrar como elas ficam.

Veja imagemVersões:

Disponível a partir da versão 12.1.33.159
