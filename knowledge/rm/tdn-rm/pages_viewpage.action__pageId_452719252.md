---
content_hash: ce9dad51ac340ddcd4470016ef975cfd151a999af41c111c55e8c21483423ebd
fetched_at: '2026-06-29T00:10:04.789425+00:00'
page_id: '452719252'
product: rm
source: tdn-rm
title: Layout Para Importação de Eventos de Sindicatos (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719252
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

-  (ddmmyyyy) em campos do tipo **Data**;

-  (GRR20071514) em campos do tipo **String**;

-  Começam /@ e terminam com @/ em campos do tipo **MEMO**.

Para o caso de importação de históricos a data da mudança deve sempre ser informada. Caso este campo não seja informado, o registro em questão não será importado.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Descrição** | **Tipo** | **Tamanho** | **Posição** | **Campo** |
| **Código do Sindicato** | **String** | **10** | **1** | PSINDEVT.CODSINDICATO |
| **Tipo de Médias** | Inteiro | **2** | **2** | PSINDEVT.TIPOMEDIA |
| **Grupo de Médias** | Inteiro | **2** | **3** | PSINDEVT.GRUPO |
| Código do Evento de Pagto | String | 4 | 4 | PSINDEVT.CODEVENTOPAGTO |
| Código do Evento da diferença | String | 4 | 5 | PSINDEVT.CODEVENTODIF |
| Despreza Adicional | Inteiro | 2 | 6 | PSINDEVT.DESPREZAFORMADIC |
| Código do Evento do Envelope | String | 4 | 7 | PSINDEVT.CODEVENTOENV |
