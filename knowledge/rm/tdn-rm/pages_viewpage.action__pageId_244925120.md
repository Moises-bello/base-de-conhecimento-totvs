---
content_hash: 7a496ecefb1992b3722fb65b817156abfdfff271e0701b849649db778f8e4149
fetched_at: '2026-06-29T00:08:15.829667+00:00'
page_id: '244925120'
product: rm
source: tdn-rm
title: 3. Histórico Padrão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244925120
version: 3
---

|  |  |
| --- | --- |
| Descrição | Histórico Padrão |
| Observações | Afim de atender a contabilização do novo módulo de Aluguel serão criadas novas variáveis que poderão ser utilizadas no cadastro dos Históricos Padrões. |

Opções de mnemônicos:

* Código do imóvel: concatena quando mais de um ou se estiver “aplicando” por “Item do contrato de locação” busca apenas o imóvel do Contexto;
* Descrição do imóvel: concatena quando mais de um ou se estiver “aplicando” por “Centro de Custo” busca apenas o Centro de custo do Contexto
* Número do contrato de locação;
* Código do contrato de locação;
* Data do contrato;
* Data de Início da Locação;
* Vigência Inicial do Ct. Locação;
* Vigência Final do Ct. Locação;
* Nome cliente (concatena mais de um);
* Data de Estorno: corresponde a data original do lançamento contábil gerado. Esta variável será utilizada nos históricos de estono contábil;
* Descrição do Evento Financeiro;

 Novas variáveis podem ser criadas em tempo de projeto, e neste caso deve ser mantido o comportamento quando houver mais de um retorno, como é o caso do imóvel deve ser concatenado os N valores ou retorna o registro do contexto. Os valores das variáveis devem respeitar os dados no tempo, ou seja, buscar o imóvel conforme data de referência da contabilização.
