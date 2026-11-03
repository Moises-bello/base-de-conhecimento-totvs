---
article_id: 20196128914839
category: Materiais - Compras (SIGACOM)
content_hash: d949cfecd2a5dabce100e1c559eb4b084cd37b3ddc86108a04dbebe8987ff127
fetched_at: '2026-06-28T22:41:18.899826+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Protheus - SIGACOM - Help AJUDA:CCOBRIGATORIO
  A conta XXX exige o preenchimento do Centro de Custo na Inclusão do Documento de
  entrada.
type: support-article
updated_at: '2023-12-29T16:04:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20196128914839-Cross-Segmentos-TOTVS-Backoffice-Protheus-SIGACOM-Help-AJUDA-CCOBRIGATORIO-A-conta-XXX-exige-o-preenchimento-do-Centro-de-Custo-na-Inclus%C3%A3o-do-Documento-de-entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20196128898071) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Por quê o sistema gera o help abaixo?

AJUDA:CCOBRIGATORIO  
A conta XXX exige o preenchimento do Centro de Custo.

Tabela SF1 27/12/2023 21:00:00  
Tipo da Nota - F1\_TIPO := N  
Form. Prop. - F1\_FORMUL := N  
Numero da NF - F1\_DOC := 123456  
Serie - F1\_SERIE := 001

\*O XXX representa o código da conta contábil em questão.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - a partir da 12.1.33  
  
**Causa**O help acima é gerado quando, no cadastro da conta contábil, o campo CT1\_OBRG = 1 - Sim, essa conta contábil for utilizada e não utilizar um centro de custo. Quando este campo está como "Sim", significa que sempre que esta conta contábil for utilizada deveremos obrigatoriamente preencher um centro de custo no rateio.

![](https://totvssuporte.zendesk.com/attachments/token/BdT3eHCo0yMsS7c7epo0K2p3n/?name=image.png)

Dessa forma, se utilizarmos a conta contábil com esse campo como Sim e não preenchermos o centro de custo no rateio o sistema gera o help.

**Solução**

Caso deseje manter essa obrigatoriedade, deverá digitar um centro de custo sempre que utilizar essa conta contábil. Caso deseje tirar essa obrigatoriedade, basta colocar o campo CT1\_OBRG = 2 - Não.

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
