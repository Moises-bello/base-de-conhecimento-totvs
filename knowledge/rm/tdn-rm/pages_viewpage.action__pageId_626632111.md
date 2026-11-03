---
content_hash: eede9b1ef6f561d67a21c8850df1f38a94f66ee4c770ad7e984a232d89164a39
fetched_at: '2026-06-29T00:11:04.324953+00:00'
page_id: '626632111'
product: rm
source: tdn-rm
title: Layout para Múltiplos Vínculos do Autônomo Externo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=626632111
version: 4
---

**Importante:**  
Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
**Campos obrigatórios estão destacados em negrito.**  
DELIMITADOR DE CAMPOS: ";"   
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".

**Observação:** Código Pagamento dos Autônomos Externos deverá ser associado ao campo codigo da tabela pai (PPAGTOAUTONOMOEXT.CODIGO)****.****  
   
 **Atenção!** Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:  
-  0 (zero) ou 1(um) em campos do tipo **Booleano**;

-  Números (00) em campos do tipo **Inteiro**;

-  Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo **Real**;

-  (ddmmyyyy) em campos do tipo **Data**;

-  (GRR20071514) em campos do tipo **String**;

-  Começam /@ e terminam com @/ em campos do tipo **MEMO**.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Descrição** | **Tipo** | **Tamanho** | **Posição** | **Campo** |
| **Código Pagamento dos Autonomos Externos** | **Inteiro** | **6** | **1** | **PPAGTOAUTONOMOEXTMV.CODIGOPAGTO** |
| CNPJ  Remuneração Outro Emprego | String | 18 | 2 | PPAGTOAUTONOMOEXTMV.CNPJREMUNOUTREMPR |
| **Categoria  eSocial Outro Emprego** | **Inteiro** | **3** | **3** | **PPAGTOAUTONOMOEXTMV.CATEGORIAESOCIAL** |
| Valor INSS outro Emprego | Real | 15 | 4 | PPAGTOAUTONOMOEXTMV.VALORINSS |
