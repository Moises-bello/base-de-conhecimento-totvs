---
content_hash: 5cb61aa17535a6f6fb67995e4351e330cb29e1d3117371616a3d455d9142835c
fetched_at: '2026-06-29T00:10:03.818549+00:00'
page_id: '452719159'
product: rm
source: tdn-rm
title: Layout Para Importação de Valores Associados - Funcionários (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719159
version: 2
---

**Importante:**  
 Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
 **Campos obrigatórios estão destacados em negrito.**  
 DELIMITADOR DE CAMPOS: ";"   
 Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
 Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
 A tabela abaixo é premissa para a importação, caso a mesma esteja vinculada a tabela de Valores Associados da base de origem:  
 - PFUNC  
 - PCODVALFUNC  
    
  **Atenção!** Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:  
 -  0 (zero) ou 1(um) em campos do tipo **Booleano**;  
 -  Números (00) em campos do tipo **Inteiro**;  
 -  Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo **Real**;  
 - (ddmmyyyy) em campos do tipo **Data**;  
 - (GRR20071514) em campos do tipo **String**;  
 - Começam /@ e terminam com @/ em campos do tipo **MEMO**.  
 Para o caso de importação de históricos a data da mudança deve sempre ser informada. Caso este campo não seja informado, o registro em questão não será importado.  
  

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Descrição** | **Tipo** | **Tamanho** | **Posição** | **Campo** |
| **Chapa** | **String** | **16** | **1** | **PFUNCVAL.CHAPA** |
| **Código do Valor** | **String** | **25** | **2** | **PFUNCVAL.CODVALOR** |
| Descrição do Valor | String | 50 | 3 | PCODVALFUNC.DESCRICAO |
| **Data do Valor (Formato ddmmyyyy)** | **Data** | **8** | **4** | **PFUNCVAL.DTVALOR** |
| Valor (Formato 999999999999,99) | Real | 9 | 5 | PFUNCVAL.VALOR |
| Observação | String | 50 | 6 | PFUNCVAL.OBSERVACAO |
