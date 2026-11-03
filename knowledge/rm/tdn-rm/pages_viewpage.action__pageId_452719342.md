---
content_hash: 1c987e8fcee5e7cb410ee6c8b1f1ddb71909c2b7d7cf205e57809f73d19fa3ab
fetched_at: '2026-06-29T00:10:06.830797+00:00'
page_id: '452719342'
product: rm
source: tdn-rm
title: Layout Para Importação de Salários Compostos (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719342
version: 8
---

**Importante:**  
Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
**Campos obrigatórios estão destacados em negrito.**  
DELIMITADOR DE CAMPOS: ";"  
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
As tabelas abaixo são premissas para a importação, caso as mesmas estejam vinculadas a tabela de Salários Compostos da base de origem:  
- PFUNC  
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
| **Descrição** | **Tipo** | **Tamanho** | **Posição** | **Campo** |
| **Chapa do funcionário** | **String** | **16** | **1** | **PFSALCMP.CHAPA** |
| **Número do salário** | **Inteiro** | **2** | **2** | **PFSALCMP.NROSALARIO** |
| **Código do evento** | **String** | **4** | **3** | **PFSALCMP.CODEVENTO** |
| Jornada referente ao salário (HHH:MM) | Inteiro | 6 | 4 | PFSALCMP.JORNADA |
| Valor do salário | Real | 15 | 5 | PFSALCMP.VALOR |
| Indicativo de Valores Forçados | Inteiro | 2 | 6 | PFSALCMP.VALORESFORCADOS |
| Referência do Salário | Inteiro | 2 | 7 | PFSALCMP.REFERENCIA |
| Nível tabela salarial | String | 10 | 8 | PFSALCMP.CODNIVELSAL |
| Faixa tabela salarial | String | 10 | 9 | PFSALCMP.CODFAIXASAL |
| Código da tabela salarial | String | 10 | 10 | PFSALCMP.CODTABELA |
| **Motivo da mudança** | **Inteiro** | **2** | **11** | **PFHSTSAL.MOTIVO** |
| Data da mudança (ddmmaaaa hh:mm:ss) | Data | 17 | 12 | PFHSTSAL.DTMUDANCA |
