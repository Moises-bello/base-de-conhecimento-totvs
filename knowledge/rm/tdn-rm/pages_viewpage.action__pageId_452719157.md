---
content_hash: 84976f4766e2054217a2a1bb42ebe5b399e17bb9c5e6f4cd3d1380165a74bbf2
fetched_at: '2026-06-29T00:10:03.799788+00:00'
page_id: '452719157'
product: rm
source: tdn-rm
title: Layout Para Importação do Histórico do Rateio de Tomador de Serviço (Versão
  12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719157
version: 6
---

**Importante:**

* Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.
* **Campos obrigatórios estão destacados em negrito.**

DELIMITADOR DE CAMPOS: ";"   
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
A tabela abaixo é premissa para a importação de Ficha Financeira;  
- PFUNC

-FCFO

**Atenção!** Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:  
-  0 (zero) ou 1(um) em campos do tipo **Booleano**;

-  Números (00) em campos do tipo **Inteiro**;

-  Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo **Real**;

-  (ddmmyyyy) em campos do tipo **Data**;

-  (GRR20071514) em campos do tipo **String**;

-  Começam /@ e terminam com @/ em campos do tipo **MEMO**.  
Para o caso de importação de históricos a data da mudança deve sempre ser informada. Caso este campo não seja informado, o registro em questão não será importado.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **DESCRIÇÃO** | **TIPO** | **Tamanho** | **Posição** | **Campo** |
| **Chapa do funcionário** | **String** | **16** | **1** | **PFHSTRATEIOTOMADOR****.** **CHAPA** |
| **Mês Inicial** | **Inteiro** | **2** | **2** | **PFHSTRATEIOTOMADOR****.** **DATAINICIO** |
| **Ano Inicial** | **Inteiro** | **4** | **3** | **PFHSTRATEIOTOMADOR****.** **DATAINICIO** |
| **Código da Coligada do Tomador de Serviço** | **Inteiro** | **4** | **4** | **PFHSTRATEIOTOMADOR****.** **CODCOLTOMADOR** |
| **Código do Tomador de Serviço** | **String** | **25** | **5** | **PFHSTRATEIOTOMADOR****.****CODTOMADOR** |
| **Tipo do Tomador** **'1' = Cessão de mão de obra e**  **'2' = Construção civil** | **Inteiro** | **1** | **6** | **PFHSTRATEIOTOMADOR****.** **TPTOMADOR** |
| **ID do Tomador** | **Inteiro** | **6** | **7** | **PFHSTRATEIOTOMADOR****.** **ID** |
| Mês Final | Inteiro | 2 | 8 | PFHSTRATEIOTOMADOR. DATAFIM |
| Ano Final | Inteiro | 4 | 9 | PFHSTRATEIOTOMADOR. DATAFIM |
| CEI do Tomador\* | String | 20 | 10 | PFHSTRATEIOTOMADOR. CEI |
| **Valor do Rateio** | **Inteiro** | **2** | **11** | **PFHSTRATEIOTOMADOR.** **VALOR** |

\*CEI do Tomador deverá ser cadastrado com máscara.

**Observação:**  
Para atender ao leiaute do eSocial, ao realizar a importação de rateio de tomadores, caso não exista o tomador na seção será disparado um gatilho de inclusão no cadastro de Lotação Tributária.
