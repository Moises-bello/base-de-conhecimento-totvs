---
content_hash: 05fccd27f2e67f1af8bc8ba36a952d31f0432d8f87c8f7672a8b9bad902174ba
fetched_at: '2026-06-29T00:10:08.485811+00:00'
page_id: '452719523'
product: rm
source: tdn-rm
title: Layout Para Importação de Lançamentos Vinculados (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719523
version: 2
---

**Importante:**  
 Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
 **Campos obrigatórios estão destacados em negrito.**  
 DELIMITADOR DE CAMPOS: ";"   
 Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
 Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
 A tabela abaixo é premissa para a importação de Incidência de Lançamentos Vinculados:  
 - PEVENTO  
  **Atenção!** Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:  
 -  0 (zero) ou 1 (um) em campos do tipo **Booleano**;  
 -  Números (00) em campos do tipo **Inteiro**;  
 -  Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo **Real**;

* (ddmmyyyy), em campos do tipo **Data**;
* (GRR20071514), em campos do tipo **String**;
* Começam /@ e terminam com @/ em campos do tipo **MEMO**.  
   Para o caso de importação de históricos a data da mudança deve sempre ser informada. Caso este campo não seja informado, o registro em questão não será importado.

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  | **DESCRIÇÃO** | **TIPO** | **TAMANHO** | **Posição** | **CAMPO** |
  | **Código do Evento** | **String** | **4** | **1** | **PEVTRELACEVT.CODEVENTO** |
  | **Código do Evento Relacionado** | **String** | **4** | **2** | **PEVTRELACEVT.CODEVENTORELAC** |
