---
content_hash: 74e1c4aee365e7566f5f358efa26db32be9467f6ca25ba5323810108fd1b7af4
fetched_at: '2026-06-29T00:10:02.451217+00:00'
page_id: '452718912'
product: rm
source: tdn-rm
title: Layout Para Importação de Valores de Sindicato (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718912
version: 2
---

**Importante:**  
  Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.

**Campos obrigatórios estão destacados em negrito.**  
 DELIMITADOR DE CAMPOS: ";"   
 Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
 Entre ponto virgula ( **;;** ) "Correspondendo um campo NULL".  
 As tabelas abaixo são premissas para a importação, caso as mesmas estejam vinculadas a tabela de Valores de Sindicato da base de origem:  
 - PSINDIC  
 - PCODVALSIND  
    
  **Atenção!** Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:  
 -  0 (zero) ou 1 (um) em campos do tipo **Booleano**;  
 -  Números (00) em campos do tipo **Inteiro**;  
 -  Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo **Real**;

-  (ddmmyyyy), em campos do tipo **Data**;

-  (GRR20071514), em campos do tipo **String**;

-  Começam /@ e terminam com @/ em campos do tipo **MEMO**.  
 Para o caso de importação de históricos a data da mudança deve sempre ser informada. Caso este campo não seja informado, o registro em questão não será importado.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **DESCRIÇÃO** | **TIPO** | **TAMANHO** | **Posição** | **CAMPO** |
| **Código Sindicato** | **Inteiro** | **10** | **3** | **PSINDVAL.CODSINDICATO** |
| **Código do Valor** | **String** | **2** | **1** | **PSINDVAL.CODVALOR** |
| Valor | Data | 15 | 2 | PSINDVAL.VALOR |
| **Data do Valor** | **Data** | **8** | **4** | **PSINDVAL.DTVALOR** |
| Observação | Memo | 50 | 5 | PSINDVAL.OBSERVACAO |
