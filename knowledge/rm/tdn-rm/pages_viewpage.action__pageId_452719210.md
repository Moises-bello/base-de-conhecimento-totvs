---
content_hash: 8fb937f9ba51b45aacb024c5a6b0fafd9723d8057129b9a17cdda5fb9626e6df
fetched_at: '2026-06-29T00:10:04.503077+00:00'
page_id: '452719210'
product: rm
source: tdn-rm
title: Layout Para Importação de Histórico de Contribuição Sindical (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719210
version: 3
---

**Importante:**  
Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
**Campos obrigatórios estão destacados em negrito.**  
DELIMITADOR DE CAMPOS: ";"  
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
As tabelas abaixo são premissas para a importação, caso as mesmas estejam vinculadas a tabela de Histórico de Contribuição Sindical da base de origem:  
- PFUNC  
- PSINDIC  
   
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
| **DESCRIÇÃO** | **TIPO** | **TAMANHO** | **Posição** | **CAMPO** |
| **Chapa do funcionário** | **String** | **16** | **1** | **PFHSTCSD.CHAPA** |
| **Data de contribuição** | **Data** | **8** | **2** | **PFHSTCSD.DTCONTRIBUICAO** |
| **Código do sindicato** | **String** | **10** | **3** | **PFHSTCSD.CODSINDICATO** |
| **Valor da contribuição** | **Real** | **15** | **4** | **PFHSTCSD.VALOR** |
| **Verifica se a contribuição é uma diferença de contribuição** | **Inteiro** | **2** | **5** | **PFHSTCSD.DIFCONTRIBSINDC** |
