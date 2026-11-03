---
content_hash: f600e0fb790e78c8a58ae93a32f00fc296bd2f1e47fea1d0409e7f60a808f561
fetched_at: '2026-06-29T00:10:06.947193+00:00'
page_id: '452719352'
product: rm
source: tdn-rm
title: Layout Para Importação de Recibo de Férias (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719352
version: 3
---

**Importante:**  
Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
**Campos obrigatórios estão destacados em negrito.**  
DELIMITADOR DE CAMPOS: ";"  
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
 A tabela abaixo é premissa para a importação, caso a mesma esteja vinculada a tabela de Recibo de Férias da base de origem:  
-PFUFERIASPER  
   
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
| **Chapa do Funcionário** | **String** | **16** | **1** | **PFUFERIASRECIBO.CHAPA** |
| Data final do período aquisitivo | Data | 8 | 2 | PFUFERIASRECIBO.FIMPERAQUIS |
| Data de pagamento das férias | Data | 8 | 3 | PFUFERIASRECIBO.DATAPAGTO |
| Desconto de Inss ref. ao primeiro mês | Real | 9 | 4 | PFUFERIASRECIBO.INSS1 |
| Desconto de Inss ref. ao segundo mês | Real | 9 | 5 | PFUFERIASRECIBO.INSS2 |
| Desconto de Irrf | Real | 9 | 6 | PFUFERIASRECIBO.IRRF |
| Base de Inss referente ao primeiro mês | Real | 9 | 7 | PFUFERIASRECIBO.BASEINSS1 |
| Base de Inss referente ao segundo mês | Real | 9 | 8 | PFUFERIASRECIBO.BASEINSS2 |
| Base de Irrf | Real | 9 | 9 | PFUFERIASRECIBO.BASEIRRF |
| Valor Líquido do Recibo de Férias | Real | 9 | 10 | PFUFERIASRECIBO.LIQUIDO |
| Observação referente ao Recibo de Férias | String | 80 | 11 | PFUFERIASRECIBO.OBSERVACAO |
| GUID da execução do processo de cálculo | String | 40 | 12 | PFUFERIASRECIBO.EXECID |
| Pensão | Real | 9 | 13 | PFUFERIASRECIBO.PENSAO |
| Base da Pensão | Real | 9 | 14 | PFUFERIASRECIBO.BASEPENSAO |
| Valores forçados manualmente | Inteiro | 2 | 15 | PFUFERIASRECIBO.VALORESFORCADOS |
| Média do período aquisitivo atual | Real | 9 | 16 | PFUFERIASRECIBO.MEDIAPERAQATUAL |
| Média do próximo período aquisitivo | Real | 9 | 17 | PFUFERIASRECIBO.MEDIAPROXPERAQ |
| Salário do func. no momento do cálculo | Real | 9 | 18 | PFUFERIASRECIBO.SALARIO |
| Número de dependentes de IRRF | Inteiro | 2 | 19 | PFUFERIASRECIBO.NRODEPENDIRRF |
| Número dependentes de Salário Família | Inteiro | 2 | 20 | PFUFERIASRECIBO.NRODEPENDSALFAMILIA |
| IRRF Simplificado | Inteiro | 2 | 21 | PFUFERIASRECIBO.IRRFSIMPLIFICADO |
| IRRF Simplificado Caixa | Inteiro | 2 | 22 | PFUFERIASRECIBO.IRRFSIMPLIFICADOCAIXA |
