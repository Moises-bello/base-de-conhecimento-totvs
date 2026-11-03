---
content_hash: 5f95ad1664c173d56ef2e560e511dc42adf15d6ceade5e3972deedb3cde24f9d
fetched_at: '2026-06-29T00:10:04.094767+00:00'
page_id: '452719196'
product: rm
source: tdn-rm
title: Layout Para Importação de Períodos Aquisitivos (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719196
version: 3
---

**Importante:**  
Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
**Campos obrigatórios estão destacados em negrito.**  
DELIMITADOR DE CAMPOS: ";"  
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
**É premissa para a importação, caso Funcionário tenha mais de um período aquisitivo que a primeira linha seja a do período aquisitivo em aberto.**  
   
 **Atenção!** Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:  
-  0 (zero) ou 1(um) em campos do tipo **Booleano**;  
-  Números (00) em campos do tipo**Inteiro**;  
-  Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo **Real**;  
- (ddmmyyyy) em campos do tipo **Data**;  
- (GRR20071514) em campos do tipo **String**;  
- Começam /@ e terminam com @/ em campos do tipo **MEMO**.  
Para o caso de importação de históricos a data da mudança deve sempre ser informada. Caso este campo não seja informado, o registro em questão não será importado.

**Observação**

Ao fazer a importação deve existir um período em situação de aberto no cadastro de período aquisitivo ou no arquivo usado na importação.

O sistema faz algumas validações de cadastro na importação, como:

* Período aquisitivo aberto
* Se período fechado é menor que o período aberto

As validações retornam mensagem de erro e impedem que o registro seja importado. 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Descrição** | **Tipo** | **Tamanho** | **Posição** | **Campo** |
| **Chapa** | **String** | **16** | **1** | PFUNC.CHAPA |
| **Data final do período aquisitivo** | **Data** | **8** | **2** | **PFUFERIAS.FIMPERAQUIS** |
| **Data inicial do período aquisitivo** | **Data** | **8** | **3** | **PFUFERIAS.INICIOPERAQUIS** |
| Saldo do período de férias | Real | 9 | 4 | PFUFERIAS.SALDO |
| **Indicativo de período aquisitivo aberto** | **Booleano** | **2** | **5** | **PFUFERIAS.PERIODOABERTO** |
| Indicativo de período aquisitivo perdido | Booleano | 2 | 6 | PFUFERIAS.PERIODOPERDIDO |
| Motivo da perda do período aquisitivo | String | 2 | 7 | PFUFERIAS.MOTIVOPERDA |
| Faltas ocorridas no período aquisitivo | Real | 9 | 8 | PFUFERIAS.FALTAS |
| Bônus | Real | 9 | 9 | PFUFERIAS.BONUS |
