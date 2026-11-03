---
content_hash: 8442e523e2e80bbcbb38d2431f5f338a9afc323849008d5ce89018b42f95308e
fetched_at: '2026-06-29T00:10:05.436917+00:00'
page_id: '452719292'
product: rm
source: tdn-rm
title: Layout Para Importação de Períodos de Gozo (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719292
version: 5
---

**Importante:**  
Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
**Campos obrigatórios estão destacados em negrito.**  
DELIMITADOR DE CAMPOS: ";"  
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
A tabela abaixo é premissa para a importação, caso a mesma esteja vinculada a tabela de Períodos de Gozo da base de origem:  
- PFUFERIAS  
   
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
| **Chapa** | **String** | **16** | **1** | **PFUFERIASPER.CHAPA** |
| **Data final do período aquisitivo** | **Data** | **8** | **2** | **PFUFERIASPER.FIMPERAQUIS** |
| **Data de pagamento das férias** | **Data** | **8** | **3** | **PFUFERIASPER.DATAPAGTO** |
| **Data de início das férias** | **Data** | **8** | **4** | **PFUFERIASPER.DATAINICIO** |
| **Data de fim das férias** | **Data** | **8** | **5** | **PFUFERIASPER.DATAFIM** |
| **Data de aviso das férias** | **Data** | **8** | **6** | **PFUFERIASPER.DATAAVISO** |
| Número de dias de abono pecuniário | Real | 9 | 7 | PFUFERIASPER.NRODIASABONO |
| Ind. de pagto. da 1ª parcela 13ºsalário | Booleano | 2 | 8 | PFUFERIASPER.PAGA1APARC13O |
| Licença remunerada férias colet. 1ºmês | Real | 9 | 9 | PFUFERIASPER.NDIASLICREM1 |
| Licença remunerada férias colet. 2ºmês | Real | 9 | 10 | PFUFERIASPER.NDIASLICREM2 |
| Indicativo de per.ref.à férias coletivas | Booleano | 2 | 11 | PFUFERIASPER.FERIASCOLETIVAS |
| Dias de férias perdidos devido a faltas | Inteiro | 2 | 12 | PFUFERIASPER.FERIASPERDIDAS |
| Obs. a ser impressa no recibo de férias | String | 80 | 13 | PFUFERIASPER.OBSERVACAO |
| Situação das férias | String | 1 | 14 | PFUFERIASPER.SITUACAOFERIAS |
| Data Inicio Desconto Empréstimo Férias | Data | 8 | 15 | PFUFERIASPER.DATAINICIODESCEMPR |
| Nro Vezes Desconto Empréstimo Férias | Inteiro | 4 | 16 | PFUFERIASPER.NROVEZESDESCEMPR |
| Faltas | Real | 9 | 17 | PFUFERIASPER.FALTAS |
| Nro.dias antecipados do próx.periodo | Real | 9 | 18 | PFUFERIASPER.NRODIASANTECIPADOS |
| Fim per.aquis.referente aos dias antec. | Data | 8 | 19 | PFUFERIASPER.FIMPERAQUISANTEC |
| Data pagto.referente aos dias antec. | Data | 8 | 20 | PFUFERIASPER.DATAPAGTOANTEC |
| Indica se este periodo foi antecipado | Booleano | 2 | 21 | PFUFERIASPER.PERIODOANTECIPADO |
| NRODIASFERIADO | Real | 9 | 22 | PFUFERIASPER.NRODIASFERIADO |
| Número de dias de férias corridos | Real | 9 | 23 | PFUFERIASPER.NRODIASFERIASCORRIDOS |
| Número de dias de abono corridos | Real | 9 | 24 | PFUFERIASPER.NRODIASABONOCORRIDOS |
| Abono antes ou depois das férias | Inteiro | 2 | 25 | PFUFERIASPER.POSICAOABONO |
| Indicativo de per.ref.à férias compulsórias | Booleano | 2 | 26 | PFUFERIASPER.FERIASCOMPULSORIA |
