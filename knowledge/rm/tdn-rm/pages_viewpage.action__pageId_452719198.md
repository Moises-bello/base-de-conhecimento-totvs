---
content_hash: b833a5310dbf7c1a42f54c31eb864e5750e383351fc4453d1acd856b6769a4e2
fetched_at: '2026-06-29T00:10:04.107424+00:00'
page_id: '452719198'
product: rm
source: tdn-rm
title: Layout Para Importação de Histórico de Horário (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719198
version: 2
---

**Importante:**  
 Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
 **Campos obrigatórios estão destacados em negrito.**  
 DELIMITADOR DE CAMPOS: ";"  
 Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
 Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
 As tabelas abaixo são premissas para a importação, caso as mesmas estejam vinculadas a tabela de Histórico de Horários da base de origem:  
 - PFUNC  
 - AHORARIO  
 - AMOTMUDHOR  
    
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
| **DESCRIÇÃO** | **TIPO** | **TAMANHO** | **Posição** | **CAMPO** |
| **Chapa** | **String** | **16** | **1** | **PFHSTHOR.CHAPA** |
| **Data da Mudança de Horário (ddmmaaaa hh:mm:ss)** | **Data** | **17** | **2** | **PFHSTHOR.DTMUDANCA** |
| **Código do Horário** | **Inteiro** | **10** | **3** | **PFHSTHOR.CODHORARIO** |
| **Letra associada ao índice** | **Inteiro** | **2** | **4** | **PFHSTHOR.INDINICIOHOR** |
| Data de Alteração do Histórico | Data | 8 | 5 | PFHSTHOR.DATAALTERACAO |
| Motivo da alteração | String | 2 | 6 | PFHSTHOR.MOTIVO |
| **Comportamento do horário anterior** | **Inteiro** | **4** | **7** | **PFHSTHOR.COMPORTAMENTOHORARIOANTERIOR** |
| **Comportamento do horário atual** | **Inteiro** | **4** | **8** | **PFHSTHOR.COMPORTAMENTOHORARIOATUAL** |
