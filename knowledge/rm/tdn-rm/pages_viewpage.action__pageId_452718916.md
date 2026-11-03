---
content_hash: c181c7becd4a278a3784f94006a045d2b8ed8a563551c1f2fb24f4b4d2f14a22
fetched_at: '2026-06-29T00:10:02.463925+00:00'
page_id: '452718916'
product: rm
source: tdn-rm
title: Layout Para Importação de Adicionais de Férias (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718916
version: 2
---

**Importante:**  
 Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
 **Campos obrigatórios estão destacados em negrito.**  
 DELIMITADOR DE CAMPOS: ";"  
 Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
 Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
 A tabela abaixo é premissa para a importação de Adicionais de Férias;  
 -PEVENTO  
    
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
| **Chapa** | **String** | **16** | **1** | **PFADICFER.CHAPA** |
| **Código do Evento Recebido** | **String** | **4** | **2** | **PFADICFER.CODEVTRECIBO** |
| **Código do Evento Folha** | **String** | **4** | **3** | **PFADICFER.CODEVTFOLHA** |
| Valor | Real | 9 | 4 | PFADICFER.VALOR |
| Número de vezes | Inteiro | 4 | 5 | PFADICFER.NROVEZES |
| Evento de recibo prox mês | String | 4 | 6 | PFADICFER.EVENTORECPROXMES |
| Evento Folha Próx.Mês | String | 4 | 7 | PFADICFER.EVTFOLHAPROXMES |
| Evento Folha Mês Ant. | String | 4 | 8 | PFADICFER.EVTFOLHAMESANT |
| Provisionar evento? | Inteiro | 2 | 9 | PFADICFER.PROVEVENTO |
