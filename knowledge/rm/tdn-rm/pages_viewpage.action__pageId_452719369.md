---
content_hash: e524fd173a05a471564e7eb9c42b11fa77771f760f2d107255889045a54da1bd
fetched_at: '2026-06-29T00:10:07.157985+00:00'
page_id: '452719369'
product: rm
source: tdn-rm
title: Layout Para Importação de Histórico de Assistência à Saúde (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719369
version: 2
---

**Importante:**  
 Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
 **Campos obrigatórios estão destacados em negrito.**  
 DELIMITADOR DE CAMPOS: ";"  
 Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
 Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
 As tabelas abaixo são premissas para a importação, caso as mesmas estejam vinculadas a tabela de Histórico de Assistência à Saúde da base de origem:  
 - PFUNC  
 - PFDEPEND  
 - PEVENTO  
    
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
| **Chapa** | **String** | **16** | **1** | **PFHSTASSMED.CHAPA** |
| **Ano Competência** | **Inteiro** | **4** | **2** | **PFHSTASSMED.ANOCOMP** |
| **Mês Competência** | **Inteiro** | **2** | **3** | **PFHSTASSMED.MESCOMP** |
| **Período** | **Inteiro** | **2** | **4** | **PFHSTASSMED.NROPERIODO** |
| **Número do dependente** | **Inteiro** | **2** | **5** | **PFHSTASSMED.NRODEPEND** |
| **Código do evento** | **String** | **4** | **6** | **PFHSTASSMED.CODEVENTO** |
| **Tipo do valor** | **Inteiro** | **2** | **7** | **PFHSTASSMED.TIPOVALOR** |
| **Data do desconto** | **Data** | **8** | **8** | **PFHSTASSMED.DTPAGTO** |
| Ano de referência do desconto | Inteiro | 4 | 9 | PFHSTASSMED.ANOREF |
| Mês de referência do desconto | Inteiro | 2 | 10 | PFHSTASSMED.MESREF |
| Período de referência do desconto | Inteiro | 2 | 11 | PFHSTASSMED.PERIODOREF |
| Valor efetivo | Real | 15 | 12 | PFHSTASSMED.VALOR |
| Valor original | Real | 15 | 13 | PFHSTASSMED.VALORORIGINAL |
| Indicativo alteração manual/importação | Booleano | 2 | 14 | PFHSTASSMED.FOIALTERADO |
| Código do evento de férias | String | 4 | 15 | PFHSTASSMED.CODEVENTOFERIAS |
