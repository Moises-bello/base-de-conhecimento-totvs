---
article_id: 360058709693
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 07cb3d68033456d5ba7df53244bde4b7c56167974d80dbc1fa02bb3cdca5190b
fetched_at: '2026-06-28T22:42:40.972840+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Cálculo das necessidades de Produção/Compras
type: support-article
updated_at: '2026-06-23T13:01:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058709693-Manufatura-Linha-Protheus-SIGAPCP-C%C3%A1lculo-das-necessidades-de-Produ%C3%A7%C3%A3o-Compras
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:04:20 min**  
**Dúvida**Como é o cálculo das necessidades de **Produção/Compras**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**A decisão de produzir ou comprar os produtos empenhados se dá com base na estrutura, considerando:

* **Produzir**  
  Quando a empresa produz os componentes, produtos com estrutura, necessários para a execução da **OP principal**, e não existem componentes suficientes em estoque ou previsão de produção, o Sistema gera automaticamente **OPs intermediárias** de acordo com a quantidade necessária verificada, para que ao final do processo todos os componentes necessários para a fabricação do produto principal estejam disponíveis.  
  Observe os parâmetros **MV\_GERAOPI**e **MV\_QUEBROP** que definem algumas regras para geração automática de **OPs** filhas.
  + **MV\_GERAOPI**Para que as **OPs filhas** sejam geradas automaticamente a partir da inclusão de uma **OP principal** preencha este parâmetro com **.T.**, caso contrário preencha-o com **.F.**. Por padrão, o Sistema gera as **OPs filhas** automaticamente.
  + **MV\_QUEBROP**   
    Indica se deve quebrar as **OPs** por quantidade de acordo com o **lote econômico** e **lote mínimo** informados no **MATA010**, ou gerar uma única **OP** com a quantidade total, para a abertura automática das **OPs filhas**. Preencha com **S** para quebrar ou **N** para não quebrar.
* **Comprar**   
  A empresa não é fabricante do componente, não existe estrutura associada, utilizado para a execução da **OP** e não possui a quantidade necessária em estoque ou previsão de recebimento. Assim, para que a **OP** possa ser executada, é gerada uma solicitação de compra de acordo com a quantidade necessária para a execução da **OP**  
  Observe os parâmetros **MV\_GERASC** e **MV\_QUEBRSC** que definem algumas regras de geração automática de **Solicitações de Compras**.
  + **MV\_GERASC**   
    Para que as **Solicitações de Compras** sejam geradas automaticamente a partir da inclusão de uma **OP principal** preencha este parâmetro com **.T.**, caso contrário preencha-o com **.F.** Por padrão, o Sistema gera as **Solicitações de Compras** automaticamente.
  + **MV\_QUEBRSC**Indica se deve ou não quebrar as **SCs** por quantidade, de acordo com o **lote econômico** e **quantidade por embalagem** informado no **MATA010** ou gerar uma única solicitação de compra.

**Exemplos:**  
Se os parâmetros **MV\_QUEBROP** e **MV\_QUEBRSC** estiverem preenchidos com **S**, o Sistema gera as solicitações de compra e as ordens de produção da seguinte forma:  
**N - Necessidade**  
**LE - Lote Econômico**  
**LM - Lote Mínimo ou Quantidade por Embalagem**  
**TOL - Tolerância**  
**ME - Múltiplo de LE**  
**MM - Múltiplo de LM**  
  
**Exemplo 1**:  
Considere:  
**LE = 500**; **LM = 100**; **TOL = 0**; **MV\_USAQTEM =N**.

|  |  |  |  |
| --- | --- | --- | --- |
| **Necessidade** | **Regra** | **A Comprar/Produzir** | **SCs/OPs Geradas** |
| 500 | N<=LE | LE | 500 |
| 520 | N<=(LE+LM) | LE+LM | 500, 100 |
| 600 | N<=(LE+LM) | LE+LM | 500, 100 |
| 620 | N>(LE+LM) | LE+MM | 500, 200 |
| 880 | N>(LE+LM) | LE+MM | 500, 400 |
| 980 | N>=(LE+LM) | ME | 500, 500 |
| 1020 | N>(LE+LM) | ME+LM | 500, 500, 100 |

**Exemplo 2**:  
Considere:  
Os mesmos dados, assumindo o parâmetro **MV\_USAQTEM = S**

|  |  |  |  |
| --- | --- | --- | --- |
| **Necessidade** | **Regra** | **A Comprar/Produzir** | **SCs/OPs Geradas** |
| <=100 | N<=LM | LM | 100 |
| >100 E <=500 | LM<N<=LE | LE | 500 |
| 520 | N<=(LE+LM) | LE+LM | 500,100 |
| 600 | N<=(LE+LM) | LE+LM | 500,100 |
| 620 | N>(LE+LM) | ME+MM | 500,200 |
| 880 | N>(LE+LM) | ME+MM | 500,400 |
| 980 | N>(LE+LM) | ME+MM | 500,500 |
| 1020 | N>(LE+LM) | ME+MM | 500,500,100 |

**Exemplo 3:**  
Se o valor de **LM** for igual à **zero**, o Sistema completa a quantidade a ser gerada com o saldo restante.  
Considere:   
Os mesmos dados, assumindo **LM = 0**

|  |  |  |  |
| --- | --- | --- | --- |
| **Necessidade** | **Regra** | **A Comprar/Produzir** | **SCs/OPs Geradas** |
| <=500 | N<=LE | LE | 500 |
| 520 | N<=(LE+LM) | LE+LM | 500, 20 |
| 600 | N<=(LE+LM) | LE+LM | 500, 100 |
| 620 | N<=(LE+LM) | LE+LM | 500, 120 |
| 880 | N>(LE+LM) | ME+MM | 500, 380 |
| 980 | N>(LE+LM) | ME+MM | 500, 480 |
| 1020 | N>(LE+LM) | ME+MM | 500, 500, 20 |

**Importante**  
O parâmetro **MV\_USAQTEM** indica se o Sistema deve considerar a **quantidade por embalagem** ou o **lote mínimo** antes do **lote econômico**. O Sistema realizará este controle se o conteúdo for **S**, caso seja **N**, o lote econômico será considerado primeiro.  
  
**Glossário**  
**OP** - Ordem de Produção;  
**SC** - Solicitação de Compra;  
**MATA010** - Cadastro de produto;  
**MV\_GERAOPI** -  Gera **OP** do produto intermediário a Partir de **OP** do produto principal;  
**MV\_USAQTEM** - Indica se na explosão de necessidade de material deve ser utilizada a quantidade por embalagem/lote mínimo como quantidade valida antes de tentar o lote econômico; **MV\_QUEBROP** - Define se as **OPs** serão quebradas de acordo com o lote econômico ou se será gerada apenas uma ordem de produto com quantidade total;**MV\_QUEBRSC** - Indica se deve quebrar as solicitações de compra em lotes econômicos, ou gerar uma única solicitação;  
**MV\_GERASC** - Gera solicitação de compra a partir da inclusão da ordem de produção.
