---
content_hash: 2f624380455f3204ed49daba2876cba675da33ae566bb43637cad563d98c74d0
fetched_at: '2026-06-29T00:11:38.979965+00:00'
page_id: '786545704'
product: rm
source: tdn-rm
title: Layout Para Importação de Valores dedutíveis por dependentes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=786545704
version: 4
---

## 

**Importante:**  
Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
**Campos obrigatórios estão destacados em negrito.**  
DELIMITADOR DE CAMPOS: ";"  
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
 A tabela abaixo é premissa para a importação, caso a mesma esteja vinculada a tabela de Valores dedutíveis por dependentes da base de origem:  
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
| **Chapa do Funcionário** | **String** | **16** | **1** | **PFDEPIRRFDED.CHAPA** |
| **Número do Dependente** | **Inteiro** | **4** | **2** | **PFDEPIRRFDED.NRODEPEND** |
| **Ano da Competência** | **Inteiro** | **4** | **3** | **PFDEPIRRFDED.ANOCOMP** |
| **Mês da Competência** | **Inteiro** | **4** | **4** | **PFDEPIRRFDED.MESCOMP** |
| **Número do Período** | **Inteiro** | **4** | **5** | **PFDEPIRRFDED.NROPERIODO** |
| **Ano Caixa** | **Inteiro** | **4** | **6** | **PFDEPIRRFDED.ANOCAIXA** |
| **Mês Caixa** | **Inteiro** | **4** | **7** | **PFDEPIRRFDED.MESCAIXA** |
| **Tipo de movimento da pensão** | **Inteiro** | **4** | **8** | **PFDEPIRRFDED.TIPOMOV** |
| **Valor** | **Real** | **15** | **9** | **PFDEPIRRFDED.VALOR** |
| Data de vencimento de férias | Data | 8 | 10 | PFDEPIRRFDED.DTVENCFERIAS |
| Data de pagamento das Férias | Data | 8 | 11 | PFDEPIRRFDED.DATAPAGTOFER |
