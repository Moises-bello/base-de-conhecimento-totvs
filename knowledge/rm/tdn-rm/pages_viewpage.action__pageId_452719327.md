---
content_hash: e823b98158d500083ba306870ec10e8ee33157fd5a34db2d65c65ae506622209
fetched_at: '2026-06-29T00:10:06.672525+00:00'
page_id: '452719327'
product: rm
source: tdn-rm
title: Layout Para Importação de Ficha Financeira (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719327
version: 2
---

**Importante:**  
 Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
 **Campos obrigatórios estão destacados em negrito.**  
 DELIMITADOR DE CAMPOS: ";"   
 Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
 Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
 A tabela abaixo é premissa para a importação de Ficha Financeira;  
 - PFUNC  
    
  **Atenção!**Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:  
 -  0 (zero) ou 1 (um) em campos do tipo **Booleano**;

-  Números (00) em campos do tipo **Inteiro**;

-  Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo **Real**;

-  (ddmmyyyy) em campos do tipo **Data**;

-  (GRR20071514 ) em campos do tipo **String**;

-  Começam /@ e terminam com @/ em campos do tipo **MEMO**.  
 Para o caso de importação de históricos a data da mudança deve sempre ser informada. Caso este campo não seja informado, o registro em questão não será importado

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Descrição** | **Tipo** | **Tamanho** | **Posição** | **Campo** |
| **Chapa do Funcionário** | **String** | **16** | **1** | **PFFINANC.CHAPA** |
| **Ano de Competência** | **Inteiro** | **4** | **2** | **PFFINANC.ANOCOMP** |
| **Mês de Competência** | **Inteiro** | **2** | **3** | **PFFINANC.MESCOMP** |
| **Número do Período** | **Inteiro** | **2** | **4** | **PFFINANC.NROPERIODO** |
| Código do Evento | String | 4 | 5 | PFFINANC.CODEVENTO |
| Data de Pagamento | Data | 8 | 6 | PFFINANC.DTPAGTO |
| Hora | String | 6 | 7 | PFFINANC.HORA |
| Referência | Real | 6 | 8 | PFFINANC.REF |
| Valor | Real | 15 | 9 | PFFINANC.VALOR |
| Valor original | Real | 15 | 10 | PFFINANC.VALORORIGINAL |
| Indica o recálculo do evento de férias | Booleano | 2 | 11 | PFFINANC.VERBAFERIAS |
| Origem do Movimento | Inteiro | 2 | 12 | PFFINANC.ORIGEMMOV |
