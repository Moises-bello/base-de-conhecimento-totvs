---
content_hash: a46c2d6edba70000439e3059847ec6a99f17b142361f2dbfed4782eaa9b449ce
fetched_at: '2026-06-29T00:10:04.120853+00:00'
page_id: '452719199'
product: rm
source: tdn-rm
title: Layout Para Importação Tarifa de Vale Transporte (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719199
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

* (ddmmyyyy) em campos do tipo **Data**;
* (GRR20071514) em campos do tipo **String**;
* Começam /@ e terminam com @/ em campos do tipo **MEMO**.  
   Para o caso de importação de históricos a data da mudança deve sempre ser informada. Caso este campo não seja informado, o registro em questão não será importado.  
    

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  | **Descrição** | **Tipo** | **Tamanho** | **Posição** | **Campo** |
  | **Código da Tarifa** | **String** | **3** | **1** | **PTARIFA.CODIGO** |
  | **Início da Vigência** | **Data** | **8** | **2** | **PTARIFA.INICIOVIGENCIA** |
  | **Final da Vigência** | **Data** | **8** | **3** | **PTARIFA.FINALVIGENCIA** |
  | **Descrição da Tarifa** | **String** | **30** | **4** | **PTARIFA.DESCRICAO** |
  | **Valor da Tarifa** **(Formato 99999,99)** | **Real** | **8** | **5** | **PTARIFA.VALOR** |
  | Atualiza Vigência | Booleano | 1 | 6 | PTARIFA.ATUALIZAVIGENCIA |
