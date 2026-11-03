---
content_hash: 4ed5450cef859463204ffdc33b696b4713522839e1a2a624803df081e77e6aed
fetched_at: '2026-06-29T00:10:04.761816+00:00'
page_id: '452719246'
product: rm
source: tdn-rm
title: Layout Para Importação de Valores Fixos (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719246
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
| **Código do Valor Fixo** | **String** | **4** | **1** | **PVALFIX.CODIGO** |
| **Início da Vigência** | **Data** | **8** | **2** | **PVALFIX.INICIOVIGENCIA** |
| **Nome do Valor Fixo** | **String** | **45** | **3** | **PVALFIX.NOME** |
| **Valor do Valor Fixo** | **Real** | **11** | **4** | **PVALFIX.VALOR** |
| **Final da Vigência** | **Data** | **8** | **5** | **PVALFIX.FINALVIGENCIA** |
| Finalidade | Inteiro | 2 | 6 | PVALFIX**.**FINALIDADE |
| **Atualiza vigência (0 ou 1)** | **Inteiro** | **1** | **7** | **PVALFIX.ATUALIZAVIGENCIA** |
