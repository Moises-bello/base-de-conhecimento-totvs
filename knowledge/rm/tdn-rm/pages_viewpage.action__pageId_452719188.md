---
content_hash: f6b034bcbfbca1365959c9ad4f07127d90de3a9be588ee3bb2c38f44bb6e9fb9
fetched_at: '2026-06-29T00:10:04.038384+00:00'
page_id: '452719188'
product: rm
source: tdn-rm
title: Layout Para Importação de Histórico de Dados Bancários (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719188
version: 2
---

**Importante:**  
 Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
 **Campos obrigatórios estão destacados em negrito.**  
 DELIMITADOR DE CAMPOS: ";"  
 Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
 Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
 As tabelas abaixo são premissas para a importação, caso as mesmas estejam vinculadas a tabela de Histórico de Dados Bancários da base de origem:  
 - PFUNC  
 - GBANCO  
 - GAGENCIA  
    
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
| **Chapa** | **String** | **16** | **1** | **PFHSTCPGTO.CHAPA** |
| **Banco de Pagamento** | **String** | **3** | **2** | **PFHSTCPGTO.CODBANCOPGTO** |
| **Agência de Pagamento** | **String** | **6** | **3** | **PFHSTCPGTO.CODAGENCIAPGTO** |
| **Conta de Pagamento** | **String** | **15** | **4** | **PFHSTCPGTO.CONTAPGTO** |
| Operação Bancária | String | 5 | 5 | PFHSTCPGTO.OPBANCARIA |
| **Data da Mudança (ddmmaaaa hhmmss)** | **Data** | **17** | **6** | **PFHSTCPGTO.DTMUDANCA** |
| Tipo de conta bancária | String | 1 | 7 | PFHSTCPGTO.TPCONTABANCARIA |
| **Tipo da Conta     (S = Principal,      N = Alternativa)** | **String** | **1** | **8** | **PFHSTCPGTO.PRINCIPAL** |
