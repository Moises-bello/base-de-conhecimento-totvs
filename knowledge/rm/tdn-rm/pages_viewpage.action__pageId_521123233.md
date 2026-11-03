---
content_hash: a9f5583c8c05fdd4903d7d7b985a79cb520f1310565faac4effb5d1391605e99
fetched_at: '2026-06-29T00:10:31.228132+00:00'
page_id: '521123233'
product: rm
source: tdn-rm
title: Layout Para Importação de Histórico de Tipo de Recebimento (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=521123233
version: 4
---

**Importante:**  
Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
**Campos obrigatórios estão destacados em negrito.**  
DELIMITADOR DE CAMPOS: ";"  
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
A tabela abaixo é premissa para a importação de Histórico de Ocorrências SEFIP  
- PFUNC  
   
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
| **Chapa** | **String** | **16** | **1** | **PFHSTCODRECEBIMENTO.CHAPA** |
| **Data da Mudança** | **Data** | **8** | **2** | **PFHSTCODRECEBIMENTO.DTMUDANCA** |
| **Código do Tipo de Recebimento** | **Inteiro** | **1** | **3** | **PFHSTCODRECEBIMENTO.CODRECEBIMENTO** |
