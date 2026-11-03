---
content_hash: abf9b202cd999a0870f3d2d388c1c5b7b57923245d663d986de56dd6f0f574a6
fetched_at: '2026-06-29T00:06:30.289360+00:00'
page_id: '235318674'
product: rm
source: tdn-rm
title: ER_PCREQ-10738_Apropriacao_de_Lancamento_Financeiro_Avulso
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-10738_Apropriacao_de_Lancamento_Financeiro_Avulso
version: 131
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Apropriação |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto** | R\_C&P\_TOP011 | **IRM** | PCREQ-10737 |
| **Requisito** | PCREQ-10738 | **Subtarefa** | PDR\_CP\_TOP011-166 |
| **Chamado** | Não se aplica | | |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | |  |  | | --- | --- | | **Pré-requisitos para melhor entendimento da especificação** | | | **Entidade** | **Link para o Wikihelp** | | Projetos | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Projetos.aspx> | | Apropriação de Serviços e Insumos | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.ApropriacaoServicosInsumos.aspx> | | | |
| **Integração** | Não se aplica | | |

    

## Objetivo

Este documento tem o objetivo de demonstrar a funcionalidade de apropriação de lançamentos financeiros avulsos.  

*.*

## Definição da Regra de Negócio

Toda a regra de negócio implementada está disponível a partir da versão 12.1.11. Esta implementação torna-se necessária pois foi constatado que lançamentos de títulos avulsos no financeiro não estavam sendo apropriados no Totvs Obras e Projetos.  Para que a apropriação seja realizada é necessário que o título não esteja vinculado a nenhum movimento e que o mesmo possua rateio, informando projeto e tarefa( e ), assim como o parâmetro de uso do rateio no lançamento financeiro ()

Para que o lançamento seja apropriado o usuário precisa informar nos parâmetros de projeto, que possui integração com Financeiro e qual a data de referência a ser considerada pelo Totvs obras e Projetos, quanto apropriação do título financeiro(), caso a data informada no lançamento seja anterior ou superior as datas do cronograma a apropriação será para o primeiro ou ultimo período do cronograma. A apropriação será feita pelo valor original do lançamento e rateio, sendo assim, caso haja um valor inferior ou superior na baixa do lançamento, o mesmo não será considerado na apropriação.

Os valores das apropriações aparecerão no cronograma, assim como é feita a apropriação de movimentos().

## Protótipo de Tela

**Protótipo 01**

**Protótipo 02**

****Protótipo 03****

**Protótipo 04**

****Protótipo 05****

**Existem 3 fluxos que podem ser seguidos para o processo de apropriação via lançamento financeiro avulso, são eles:**

1. Ao gerar um movimento de contrato do TOP é gerado movimento no Núcleos, a partir desse movimento, caso venha emitir a Nota Fiscal no Núcleos desse movimento, o valor da NF é apropriado no Cronograma. Caso esse movimento gere financeiro, é gerado lançamento no módulo Financeiro. Nesse lançamento gerado no financeiro, qualquer movimentação a partir dele, como Emissão de Fatura e Acordo Financeiro **não** são apropriados, uma vez que a NF no Núcleos já o apropriou. (Para NF gerada no Núcleos Apropriar, deve-se estar no tipo de movimento configurado “Gerar Apropriação” em seus parâmetros).
2. Caso envie um movimento do TOP de um contrato que gere diretamente o movimento financeiro sem passar pelo Núcleos, este movimento será apropriado no cronograma diretamente. Caso seja realizada alguma movimentação posterior com esse lançamento como a Inclusão da Fatura ou Acordo Financeiro, o mesmo não será apropriado novamente, uma vez que sua geração do TOP para o Financeiro já gerou essa apropriação.
3. Os lançamentos financeiros incluídos manualmente e que tenham preenchidos as informações de rateio de Projeto e Tarefa, são apropriados diretamente no Cronograma. A partir dessa apropriação, qualquer movimentação do lançamento como Acordo e Nova Fatura, não são mais apropriados, uma vez que essa apropriação foi realizada na inclusão manual do lançamento.

**Importante:** A apropriação é realizada apenas para movimentos “A PAGAR”, sendo assim, movimentos do tipo “A RECEBER” não são considerados como apropriação.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
