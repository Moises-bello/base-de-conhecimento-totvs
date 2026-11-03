---
content_hash: 524a86de51e8813be4ac2c669ea8fe5dc937e445e94663cebee12627b58631ee
fetched_at: '2026-06-29T00:10:06.913108+00:00'
page_id: '452719349'
product: rm
source: tdn-rm
title: Importação de Histórico de Provisões
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719349
version: 3
---

layout para importar o Histórico de Provisões

**Importante:**  
Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.

**Campos obrigatórios estão destacados em negrito.**

DELIMITADOR DE CAMPOS: ";"

Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( **;;** ) "Correspondendo um campo NULL".

A tabela abaixo é premissa para a importação de Histórico de Provisões

* PFUNC

**Atenção!** Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:

* 0 (zero) ou 1(um) em campos do tipo **Booleano**;
* Números (00) em campos do tipo**Inteiro**;
* Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo **Real**;
* (ddmmyyyy) em campos do tipo **Data**;
* (GRR20071514) em campos do tipo **String**;
* Começam /@ e terminam com @/ em campos do tipo **MEMO**.

Para o caso de importação de históricos a data da mudança deve sempre ser informada. Caso este campo não seja informado, o registro em questão não será importado.  
 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **DESCRIÇÃO** | **TIPO** | **TAMANHO** | **Posição** | **CAMPO** |
| **Chapa** | **String** | **16** | **1** | **PFHSTPROV.CHAPA** |
| **Ano do Histórico** | **Inteiro** | **4** | **2** | **PFHSTPROV.ANO** |
| **Mes do Histórico** | **Inteiro** | **2** | **3** | **PFHSTPROV.MES** |
| Nro. Avos de Férias Vencidos | Real | 5 | 4 | PFHSTPROV.NROAVOSVENCFERDEC |
| Nro. de Avos de Férias Proporcionais | Real | 5 | 5 | PFHSTPROV.NROAVOSPROPORCDEC |
| Nro de avos de 13o | Real | 5 | 6 | PFHSTPROV.NROAVOS13DEC |
| Data de Venc. de Férias | Data | 8 | 7 | PFHSTPROV.DTVENCFER |
| Valor da Provisão de Férias | Real | 15 | 8 | PFHSTPROV.VALPROVFER |
| Valor da Provisão de 13o. | Real | 15 | 9 | PFHSTPROV.VALPROV13 |
| Valor Provisão com Abatimento de Férias | Real | 15 | 10 | PFHSTPROV.VALPROVCOMABATFER |
| Valor Provisão sem Abatimento de Férias | Real | 15 | 11 | PFHSTPROV.VALPROVSEMABATFER |
| Médias de férias vencidas | Real | 15 | 12 | PFHSTPROV.MEDIASFERVENC |
| Médias de férias proporcionais | Real | 15 | 13 | PFHSTPROV.MEDIASFERPROP |
| Médias de 13º Salário | Real | 15 | 14 | PFHSTPROV.MEDIAS13SAL |
| Editado pelo usuário | Booleano | 1 | 15 | PFHSTPROV.EDITADO |
| Valor provisão de férias proporcionais | Real | 15 | 16 | PFHSTPROV.VALPROVFERPROP |
| Valor da provisão de férias vencidas | Real | 15 | 17 | PFHSTPROV.VALPROVFERVENC |
| Valor baixado provisão de férias no mês | Real | 9 | 18 | PFHSTPROV.VALPROVFERMES |
| ID de Execução da Provisão Férias | String | 40 | 19 | PFHSTPROV.EXECIDFER |
| ID de Execução da Provisão 13º | String | 40 | 20 | PFHSTPROV.EXECID13 |
| Valor da Provisão de Férias em Dobro | Real | 15 | 21 | PFHSTPROV.VALPROVFERDOBRO |
