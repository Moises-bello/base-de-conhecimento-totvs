---
content_hash: e1a6ecc3dc9d32082c96101c81030989a1de5be708a419ea3a4f06cb64077985
fetched_at: '2026-06-29T00:10:05.312560+00:00'
page_id: '452719283'
product: rm
source: tdn-rm
title: Layout Para Importação de Parâmetros de Cálculo do Sindicato (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719283
version: 5
---

**Importante:**  
Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
**Campos obrigatórios estão destacados em negrito.**  
DELIMITADOR DE CAMPOS: ";"  
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
   
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
| Código do Tipo | Inteiro | 2 | 1 | PSINDMED.CODTIPO |
| **Código do Sindicato** | **String** | **10** | **2** | **PSINDMED.CODSINDICATO** |
| Tipo de Cálculo | Inteiro | 2 | 3 | PSINDMED.TIPOCALCULO |
| Número de meses para média | Inteiro | 2 | 4 | PSINDMED.NROMESESANALISE |
| Número de meses habituais para férias | Inteiro | 2 | 5 | PSINDMED.NROMESESHABITUAL |
| Número de meses média/valor | Inteiro | 2 | 6 | PSINDMED.NROMESESMEDIAVALOR |
| Número de meses média/hora | Inteiro | 2 | 7 | PSINDMED.NROMESESMEDIAHORA |
| Número de maiores valores para média 1 | Inteiro | 2 | 8 | PSINDMED.NROMAIORESVALORES |
| Número de meses média/valor2 | Inteiro | 2 | 9 | PSINDMED.NROMESESMEDIAVALOR2 |
| Número de meses média/hora2 | Inteiro | 2 | 10 | PSINDMED.NROMESESMEDIAHORA2 |
| Número de maiores valores para média 2 | Inteiro | 2 | 11 | PSINDMED.NROMAIORESVALORES2 |
| Número de meses média/valor3 | Inteiro | 2 | 12 | PSINDMED.NROMESESMEDIAVALOR3 |
| Número de meses média/hora3 | Inteiro | 2 | 13 | PSINDMED.NROMESESMEDIAHORA3 |
| Número de maiores valores para média 3 | Inteiro | 2 | 14 | PSINDMED.NROMAIORESVALORES3 |
| Corrige Antes | Inteiro | 2 | 15 | PSINDMED.CORRIGEANTES |
| Despreza Adicional | Inteiro | 2 | 16 | PSINDMED.DESPREZAFORMADIC |
| Corrige Valor | Inteiro | 2 | 17 | PSINDMED.CORRIGIRVALOR |
| Código da tabela de correção | String | 10 | 18 | PSINDMED.CODTABCORRECAO |
| Número de valores a corrigir | Inteiro | 2 | 19 | PSINDMED.NROVALORESACORRIGIR |
| Parâmetros considera maior valor para soma | Inteiro | 2 | 20 | PSINDMED.MAIORVALORPARASOMA |
| Afastamentos Considerados para a média | String | 15 | 21 | PSINDMED.AFASTCONSIDERADOS |
| Dias afast. necessários para descon. mês | Inteiro | 2 | 22 | PSINDMED.DIASAFASTMES |
| Considerar dias afastamento para soma | Inteiro | 2 | 23 | PSINDMED.DIASAFASTPARASOMA |
| Dias Férias considerados p/ descon. mês | Inteiro | 2 | 24 | PSINDMED.DIASFERIASMES |
| Considerar Dias Ferias para soma | Inteiro | 2 | 25 | PSINDMED.DIASFERIASPARASOMA |
| Corrige valor pelo salário | Inteiro | 2 | 26 | PSINDMED.CORRIGIRVLSALARIO |
| Número de meses média/ref | Inteiro | 2 | 27 | PSINDMED.NROMESESMEDIAREF |
| Número de meses média/ref 2 | Inteiro | 2 | 28 | PSINDMED.NROMESESMEDIAREF2 |
| Número de meses média/ref 3 | Inteiro | 2 | 29 | PSINDMED.NROMESESMEDIAREF3 |
| Considera Ano Anterior para Médias(0-Não/1-Sim) | Inteiro | 1 | 30 | PSINDMED.CONSIDANOANTERIORMED |
| Considera mês atual para cálculo da média de 13º | Inteiro | 1 | 31 | PSINDMED.MESATUALMEDIA13O |
| (Atenção: este campo não é obrigatório, e será utilizado apenas por Clientes Piloto da Máquina de Cálculo).  Substitui período de afastamento por meses anteriores | Inteiro | 1 | 33 | PSINDMED.SUBSTITUIPERAFAST |
| Nro meses efetiv trab p/ cálculo média | Booleano | 2 | 32 | PSINDMED.CONSIDNROMESESEFETIVTRAB |
| Substitui periodo de férias por meses anteriores | Booleano | 2 | 34 | PSINDMED.SUBSTITUIPERFERIAS |
| Considera soma total da competência para buscar maiores valores | Booleano | 2 | 35 | PSINDMED.MAIORVALORTOTALPORMES |
| Últimos meses do período aquisitivo (1), a partir da versão 12.1.2402 | Inteiro | 2 | 36 | PSINDMED.NULTMESESPERAQ1 |
| Últimos meses do período aquisitivo (2), a partir da versão 12.1.2402 | Inteiro | 2 | 37 | PSINDMED.NULTMESESPERAQ2 |
| Últimos meses do período aquisitivo (3), a partir da versão 12.1.2402 | Inteiro | 2 | 38 | PSINDMED.NULTMESESPERAQ3 |
