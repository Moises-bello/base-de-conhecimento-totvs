---
content_hash: 4a07804d44f01b8834693a92a112958ccc0c4849a5eb285f2b60924d1eabc88e
fetched_at: '2026-06-29T00:10:31.232878+00:00'
page_id: '521123358'
product: rm
source: tdn-rm
title: Layout Para Importação de Histórico de Tipo de Funcionário (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=521123358
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
| **Chapa** | **String** | **16** | **1** | **PFHSTCODTIPOFUNCIONARIO.CHAPA** |
| **Data da Mudança** | **Data** | **8** | **2** | **PFHSTCODTIPOFUNCIONARIO.DTMUDANCA** |
| **Código do Tipo de Funcionário** | **Inteiro** | **1** | **3** | **PFHSTCODTIPOFUNCIONARIO.CODTIPO** |
