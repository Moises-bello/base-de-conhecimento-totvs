---
content_hash: f6d271d360d8c2060238551d2823dbd04eb0f742c9b6c747ff8816ac4c7b4b52
fetched_at: '2026-06-29T00:10:08.934288+00:00'
page_id: '452719609'
product: rm
source: tdn-rm
title: Layout Para Importação de Rateios Fixos (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719609
version: 2
---

**Importante:**  
 Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
 **Campos obrigatórios estão destacados em negrito.**  
 DELIMITADOR DE CAMPOS: ";"   
 Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
 Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
 A tabela abaixo é premissa para a importação de Ficha Financeira;  
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
| **Chapa do Funcionário** | **String** | **16** | **1** | **PFRATEIOFIXO.CODIGO** |
| **Código do Centro de Custo** | **String** | **25** | **2** | **PFRATEIOFIXO.NOME** |
| **Percentual do Rateio (Formato 999,99)** | **Real** | **6** | **3** | **PFRATEIOFIXO.DESCRICAO** |
