---
content_hash: 53cdb118b453c2f25581cf719b27a5024be325f1668483da68b9c51afd592c4d
fetched_at: '2026-06-29T00:10:37.871314+00:00'
page_id: '543064647'
product: rm
source: tdn-rm
title: Layout Para Importação de Autônomos Externos (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=543064647
version: 6
---

**Importante:**  
Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
**Campos obrigatórios estão destacados em negrito.**  
DELIMITADOR DE CAMPOS: ";"   
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".

**Observação:** O código do autônomo é  sequencial, o mesmo será gerado de acordo com a ordem da importação. 

Atenção

**Caso marque o parâmetro "Considerar código do Autônomo", sistema respeitará o código informado no arquivo e caso o mesmo já exista na base as informações serão substituídas.**

    
   
 **Atenção!** Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:  
-  0 (zero) ou 1(um) em campos do tipo **Booleano**;

-  Números (00) em campos do tipo **Inteiro**;

-  Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo **Real**;

-  (ddmmyyyy) em campos do tipo **Data**;

-  (GRR20071514) em campos do tipo **String**;

-  Começam /@ e terminam com @/ em campos do tipo **MEMO**.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Descrição** | **Tipo** | **Tamanho** | **Posição** | **Campo** |
| **Código Autônomo** | **Inteiro** | **6** | **1** | **PPAGTOAUTONOMOEXT.CODIGO** |
| **Código Filial Autônomo** | **Inteiro** | **2** | **2** | **PPAGTOAUTONOMOEXT.CODFILIAL** |
| CNPJ do Tomador | String | 20 | 3 | PPAGTOAUTONOMOEXT.CNPJTOMADOR |
| CEI do Tomador | String | 20 | 4 | PPAGTOAUTONOMOEXT.CEITOMADOR |
| Tipo do Tomador  '1' = Cessão de mão de obra e  '2' = Construção civil | Inteiro | 1 | 5 | PPAGTOAUTONOMOEXT.TPTOMADOR |
| **Nome Autônomo** | **String** | **100** | **6** | **PPAGTOAUTONOMOEXT.NOMEAUTONOMO** |
| **Data Nascimento** | **Data** | **8** | **7** | **PPAGTOAUTONOMOEXT.DTNASCIMENTO** |
| **CPF** | **String** | **11** | **8** | **PPAGTOAUTONOMOEXT.CPF** |
| **NIT** | **String** | **11** | **9** | **PPAGTOAUTONOMOEXT.NROINSCRICAO** |
| **CBO Autônomo** | **String** | **10** | **10** | **PPAGTOAUTONOMOEXT.CBOAUTONOMO** |
| **Categoria Autônomo** | **Inteiro** | **2** | **11** | **PPAGTOAUTONOMOEXT.CATAUTONOMO** |
| **Código Ocorrência SEFIP** | **Inteiro** | **2** | **12** | **PPAGTOAUTONOMOEXT.CODOCORSEFIP** |
| **Data Emissão** | **Data** | **8** | **13** | **PPAGTOAUTONOMOEXT.DATAEMISSAO** |
| **Data Vencimento** | **Data** | **8** | **14** | **PPAGTOAUTONOMOEXT.DATAVENCIMENTO** |
| **Data Inicio Atividade** | **Data** | **8** | **15** | **PPAGTOAUTONOMOEXT.DATAINIATIVIDADE** |
| Natureza Atividade | Inteiro | 2 | 16 | PPAGTOAUTONOMOEXT.NATUREZAATIV |
| Quantidade Dependentes Salário Família | Inteiro | 6 | 17 | PPAGTOAUTONOMOEXT.QTDDEPSF |
| Quantidade Dependentes IRRF | Inteiro | 6 | 18 | PPAGTOAUTONOMOEXT.QTDDEPIRRF |
| **Valor Bruto** | **Real** | **15** | **19** | **PPAGTOAUTONOMOEXT.VALORBRUTO** |
| **Valor INSS** | **Real** | **15** | **20** | **PPAGTOAUTONOMOEXT.VALORINSS** |
| Valor IRRF | Real | 15 | 21 | PPAGTOAUTONOMOEXT.VALORIRRF |
| **Data Pagamento** | **Data** | **8** | **22** | **PPAGTOAUTONOMOEXT.DATAPAGAMENTO** |
| Valor SEST | Real | 15 | 23 | PPAGTOAUTONOMOEXT.VALORSEST |
| Valor SENAT | Real | 15 | 24 | PPAGTOAUTONOMOEXT.VALORSENAT |
| ~~CNPJ Remuneração Outro Emprego~~ | ~~String~~ | ~~18~~ | ~~25~~ | ~~PPAGTOAUTONOMOEXT.CNPJREMUNOUTREMPR~~ |
| ~~Categoria eSocial Outro Emprego~~ | ~~Inteiro~~ | ~~3~~ | ~~26~~ | ~~PPAGTOAUTONOMOEXT.CODCATEG~~ |
| Indicativo de Múltiplos Vínculos | Inteiro | 1 | 25 | PPAGTOAUTONOMOEXT.INDMV |
| ~~Valor INSS Outro Emprego~~ | ~~Real~~ | ~~15~~ | ~~28~~ | ~~PPAGTOAUTONOMOEXT.VALORINSSOUTROEMPREGO~~ |
| Valor ISS | Real | 15 | 26 | PPAGTOAUTONOMOEXT.VALORISS |
| Categoria eSocial Autônomo | Inteiro | 3 | 27 | PPAGTOAUTONOMOEXT.CATEGORIAESOCIAL |
| Valor Remuneração Frete | Real | 15 | 28 | PPAGTOAUTONOMOEXT.VALORREMUNERACAOFRETE |
| Valor Remuneração Frete Incidência IRRF | Real | 15 | 29 | PPAGTOAUTONOMOEXT.VALORREMUNFRETEINCIDEIRRF |
| Valor Remuneração Frete Incidência INSS | Real | 15 | 30 | PPAGTOAUTONOMOEXT.VALORREMUNFRETEINCIDEINSS |
