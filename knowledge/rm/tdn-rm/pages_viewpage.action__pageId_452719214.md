---
content_hash: ef7632068d16e7af2be8a6204113108b4839a29053def3c30d2ebdeca6a8a256
fetched_at: '2026-06-29T00:10:04.532468+00:00'
page_id: '452719214'
product: rm
source: tdn-rm
title: Layout Para Importação de Base AAS (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719214
version: 2
---

**Importante:**  
    
 Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
 **Campos obrigatórios estão destacados em negrito.**  
 DELIMITADOR DE CAMPOS: ";"   
 Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
 Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
 A tabela abaixo é premissa para a importação de Base AAS;  
 - PFUNC  
    
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
| **Chapa** | **String** | **16** | **1** | **PFAAS.CHAPA** |
| **Ano de Competência** | **Inteiro** | **4** | **2** | **PFAAS.ANOCOMP** |
| **Mês de Competência** | **Inteiro** | **2** | **3** | **PFAAS.MESCOMP** |
| **Número do Grupo (Referência a "Código" na tabela de Códigos de Grupos de AAS)** | **Inteiro** | **2** | **4** | **PFAAS.NROGRUPO** |
| Valor (Formato 999999999999,99) | Real | 15 | 5 | PFAAS.BASECONTRIBUICAO |
