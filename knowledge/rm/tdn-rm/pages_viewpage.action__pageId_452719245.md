---
content_hash: b683e554b38a630c65c7e4752113d2c131c7c560fd60f170cb1efefae1442e4e
fetched_at: '2026-06-29T00:10:04.755990+00:00'
page_id: '452719245'
product: rm
source: tdn-rm
title: Layout Para Importação de Valores de Seção (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719245
version: 2
---

**Importante:**  
 Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
 **Campos obrigatórios estão destacados em negrito.**  
 DELIMITADOR DE CAMPOS: ";"  
 Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
 Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
 As tabelas abaixo são premissas para a importação, caso as mesmas estejam vinculadas a tabela de Valores de Seção da base de origem:  
 - PSECAO  
 - PCODVALSEC  
    
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
| **Código da Seção** | **String** | **35** | **1** | **PSECVAL.CODSECAO** |
| **Código do Valor** | **String** | **2** | **2** | **PSECVAL.CODVALOR** |
| **Valor da Seção** | **Real** | **15** | **3** | **PSECVAL.VALOR** |
| **Data do valor** | **Data** | **8** | **4** | **PSECVAL.DTVALOR** |
| Observação | Memo | 50 | 5 | PSECVAL.OBSERVACAO |
