---
content_hash: 79b4ccf50249404e5e32a328b7a321dfbb29c4cb0b306cb80327ef6b91611bd2
fetched_at: '2026-06-29T00:10:07.124759+00:00'
page_id: '452719366'
product: rm
source: tdn-rm
title: Layout Para Importação de Valores Pagos a Pensão dos Dependentes (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719366
version: 3
---

**Importante:**  
Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
**Campos obrigatórios estão destacados em negrito.**  
DELIMITADOR DE CAMPOS: ";"  
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
 A tabela abaixo é premissa para a importação, caso a mesma esteja vinculada a tabela de Valores Pagos de Pensão dos Dependentes da base de origem:  
- PFUNC  
- PFDEPEND  
- PFPERFF  
   
 **Atenção!** Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:  
-  0 (zero) ou 1(um) em campos do tipo **Booleano**;  
-  Números (00) em campos do tipo**Inteiro**;  
-  Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo **Real**;  
- (ddmmyyyy) em campos do tipo **Data**;  
- (GRR20071514) em campos do tipo **String**;  
- Começam /@ e terminam com @/ em campos do tipo **MEMO**.  
Para o caso de importação de históricos a data da mudança deve sempre ser informada. Caso este campo não seja informado, o registro em questão não será importado.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Descrição** | **Tipo** | **Tamanho** | **Posição** | **Campo** |
| **Chapa do Funcionário** | **String** | **16** | **1** | **PFDEPMOV.CHAPA** |
| **Número do Dependente** | **Inteiro** | **4** | **2** | **PFDEPMOV.NRODEPEND** |
| **Ano da Competência** | **Inteiro** | **4** | **3** | **PFDEPMOV.ANOCOMP** |
| **Mês da Competência** | **Inteiro** | **4** | **4** | **PFDEPMOV.MESCOMP** |
| **Mês Caixa** | **Inteiro** | **4** | **5** | **PFDEPMOV.MESCAIXA** |
| **Tipo de movimento da pensão** | **Inteiro** | **4** | **6** | **PFDEPMOV.TIPOMOV** |
| **Valor Efetivo** | **Real** | **15** | **7** | **PFDEPMOV.VALOR** |
| **Valor Original** | **Real** | **15** | **8** | **PFDEPMOV.VALORORIGINAL** |
| Indicativo Alteração Manual/Importação | Booleano | 4 | 9 | PFDEPMOV.FOIALTERADO |
| Número do Período | Inteiro | 4 | 10 | PFDEPMOV.NROPERIODO |
| Data de vencimento de férias | Data | 8 | 11 | PFDEPMOV.DTVENCFERIAS |
| Mês que foi feito o cálculo | Inteiro | 4 | 12 | PFDEPMOV.MESREF |
| Ano que foi feito o cálculo | Inteiro | 4 | 13 | PFDEPMOV.ANOREF |
| Período que foi feito o cálculo | Inteiro | 4 | 14 | PFDEPMOV.PERIODOREF |
| Data de pagamento das Férias | Data | 8 | 15 | PFDEPMOV.DATAPAGTOFER |
| Ano Caixa | Inteiro | 4 | 16 | PFDEPMOV.ANOCAIXA |
