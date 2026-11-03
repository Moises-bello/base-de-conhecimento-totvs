---
content_hash: 2cab7ff9f68de7e68975aa27ae255e6d5e1f06b4c8d17fd472ecc407a8c9a285
fetched_at: '2026-06-29T00:10:03.735585+00:00'
page_id: '452719150'
product: rm
source: tdn-rm
title: Layout Para Importação de Anotação de Funcionário (12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719150
version: 2
---

**Importante:**  
 Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
 **Campos obrigatórios estão destacados em negrito.**  
 DELIMITADOR DE CAMPOS: ";"  
 Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
 Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
 **Observação:** O Código da pessoa solicitante da anotação poderá não ser o mesmo na coligada destino, caso isso ocorra, deverá ser feito de/para.  
 A tabela abaixo é premissa para a importação de Anotações de Funcionário;  
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
| **Descrição** | **Tipo** | **Tamanho** | **Posição** | **Campo** |
| Chapa | String | 5 | 1 | PFUNC.CHAPA |
| **Cód. Anotação** | **Inteiro** | **2** | **2** | **PANOTAC.NROANOTACAO** |
| **Tipo da Anotação** | **Inteiro** | **2** | **6** | **PANOTAC.TIPO** |
| **Data da Anotação** | **Data** | **8** | **4** | **PANOTAC.DTANOTACAO** |
| Data da Resolução | Data | 8 | 5 | PANOTAC.DTRESOLUCAO |
| Texto | Memo | 16 | 3 | PANOTAC.TEXTO |
| Código da pessoa solicitante da anotação | Inteiro | 4 | 7 | PANOTAC.CODPESSOAAUT |
