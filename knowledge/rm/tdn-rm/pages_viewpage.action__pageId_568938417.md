---
content_hash: 305a8a0ef7307320d5e2dffaef6bdc9d697e48a8834a59b2080741d16345dd38
fetched_at: '2026-06-29T00:10:51.554092+00:00'
page_id: '568938417'
product: rm
source: tdn-rm
title: Layout de Importação de Vínculos Empregatícios outra Empresa(terceiros)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=568938417
version: 16
---

O layout de importação do "Vínculos empregatícios outra Empresa (Terceiro)" foi desenvolvido para que sejam importadas os vínculos empregaticios de terceiros no anexo do cadastro do funcionário. 

**Importante:**

Campos obrigatórios estão destacados em **negrito**.  
DELIMITADOR DE CAMPOS: ";"  
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".

**CODCOLIGADA, CHAPA, TPINSCRICAO, NRINSCRICAO, MESCOMP, ANOCOMP** são campos chaves. Caso uma ou mais linhas contenha os mesmos valores, só serão inseridos o ultimo e os demais em questão não serão importados.

 **Atenção!**

Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:  
-  0 (zero) ou 1(um) em campos do tipo **Booleano**;  
-  Números (00) em campos do tipo**Inteiro**;  
-  Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo **Real**;  
- (ddmmyyyy) em campos do tipo **Data**;  
- (GRR20071514) em campos do tipo **String**;  
- Começam /@ e terminam com @/ em campos do tipo **MEMO**.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Descrição** | **Tipo** | **Tamanho** | **Posição** | **Campo** |
| **Código da Coligada** | **int** | **2** | **1** | **PFMULTVINCULOSEXTERNO.CODCOLIGADA** |
| **Chapa** | **string** | **16** | **2** | **PFMULTVINCULOSEXTERNO.CHAPA** |
| **Tipo de Inscrição** | **int** | **2** | **3** | **PFMULTVINCULOSEXTERNO.TPINSCRICAO** |
| **Número da Inscrição** | **string** | **20** | **4** | **PFMULTVINCULOSEXTERNO.NRINSCRICAO** |
| **Mês Competência** | **int** | **2** | **5** | **PFMULTVINCULOSEXTERNO.MESCOMP** |
| **Ano Competência** | **int** | **2** | **6** | **PFMULTVINCULOSEXTERNO.ANOCOMP** |
| Valor da remuneração | decimal | 17 | 7 | PFMULTVINCULOSEXTERNO.VLRREMUNERACAO |
| Valor da contribuição previdenciária | decimal | 17 | 8 | PFMULTVINCULOSEXTERNO.VLRCONTRIBUICAO |
| Mês de competência final | int | 2 | 9 | PFMULTVINCULOSEXTERNO.MESCOMPFINAL |
| Ano de competência final | int | 2 | 10 | PFMULTVINCULOSEXTERNO.ANOCOMPFINAL |
| Sempre válido | int | 2 | 11 | PFMULTVINCULOSEXTERNO.SEMPREVALIDO |
| Código categoria | int | 2 | 12 | PFMULTVINCULOSEXTERNO.CODCATEGORIA |
