---
content_hash: 26d3cdf0cacdfb4a0b8471e00216cb8c003f5cb4c6a20ab6c88fc6e5589cd20c
fetched_at: '2026-06-29T00:10:08.115800+00:00'
page_id: '452719513'
product: rm
source: tdn-rm
title: Layout Para Importação de Rubricas (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719513
version: 2
---

**Importante:**  
 Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
 **Campos obrigatórios estão destacados em negrito.**  
 DELIMITADOR DE CAMPOS: ";"   
 Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
 Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
    
  **Atenção!** Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:  
 -  0 (zero) ou 1(um) em campos do tipo **Booleano**;

-  Números (00) em campos do tipo **Inteiro**;

-  Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo **Real**;

-  (ddmmyyyy) em campos do tipo **Data**;

-  (GRR20071514) em campos do tipo **String**;

-  Começam /@ e terminam com @/ em campos do tipo **MEMO**.  
 Para o caso de importação de históricos a data da mudança deve sempre ser informada. Caso este campo não seja informado, o registro em questão não será importado.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Descrição** | **Tipo** | **Tamanho** | **Posição** | **Campo** |
| **Código do cliente** | **String** | **3** | **1** | **PRUBRICA.CODCLIENTE** |
| Código interno | String | 3 | 2 | PRUBRICA.CODINTERNO |
| Descrição | String | 68 | 3 | PRUBRICA.DESCRIÇÃO |
| Pode alterar (0 - Não/ 1 - Sim) | Inteiro | 5 | 4 | PRUBRICA.PODEALTERAR |
