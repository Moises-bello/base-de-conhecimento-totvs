---
article_id: 360052503314
category: Contabilidade Gerencial - Lançamento Padrão e Ponto de Lançamento
content_hash: 1e2e5512b120f0f48366874b74572625ef9ed0dc02352eeab5296e20e9feee7a
fetched_at: '2026-06-28T22:40:34.078780+00:00'
product: protheus
section_id: 1500001549002
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA080 -  Como Configurar
  lançamento Partida Simples e Partida dobrada
type: support-article
updated_at: '2022-06-17T18:11:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052503314-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA080-Como-Configurar-lan%C3%A7amento-Partida-Simples-e-Partida-dobrada
---

**Dúvida**Como Configurar lançamento Partida Simples e Partida dobrada  
  
**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial - A partir da versão 12

**Solução**

1) Confira a configuração dos**[PARÂMETROS CONTÁBEIS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052504474-MP-SIGACTB-PAR%C3%82METROS-CONT%C3%81BEIS?source=search)**

2) Exemplo configuração Lançamento Padrão

Através da rotina de cadastro de lançamento padrão CTBA080

* o sistema considera o campo Tipo Lcto CT5\_DC

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360086505893/mceclip2.png)

* Exemplo LP **P****artida Dobrada**
* Veja como sistema gera na CT2[um Lançamento de Partida dobrada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053273953-MP-SIGACTB-CTBA102-Como-efetuar-um-Lan%C3%A7amento-de-Partida-dobrada?source=search)
* para partida Dobrada necessário cadastrar somente um lançamento padrão com contas de Debito e Crédito

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085310514/mceclip3.png)

* Informa conta de Debito e Credito

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360086505613/mceclip1.png)

* Exemplo LP partida **Partida Simples**
* Veja como sistema gera na CT2[um Lançamento de Partida Simples](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020712551-MP-SIGACTB-CTBA102-Como-efetuar-um-Lan%C3%A7amento-de-Partida-Simples?source=search) e as configurações necessárias
* para partida Simples necessário cadastrar dois lançamento padrão um para  contas de Debito e  outro para Crédito
* Cadastrar a LP de Debito

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360086506953/mceclip4.png)

* Informa conta de Debito

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085310614/mceclip5.png)

* Cadastrar LP de Credito

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360086507413/mceclip6.png)

* Informa conta de Credito

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085311174/mceclip7.png)

Obs:

* Caso  queira saber a configuração adequada para realizar contabilização, necessário entrar em contato com o modulo origem do lançamento
* Exe.: caso tenha duvida  para configurar o Lp para  realizar contabilização de uma fatura necessário entrar em contato com o Time de faturamento , o modulo irá orientar qual o LP adequado para fazer a contabilização que desejada
* Cabe ao contador verificar se irá realizar a contabilização com partida Simples ou Partida dobrada

**Saiba mais**

**[Dica Configuração Lançamento Padrão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004893562-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA080-Configura%C3%A7%C3%A3o-de-lan%C3%A7amento-padr%C3%A3o)**

[MP - SIGACTB - CTBA102/ CTBA101 Campos da capa do Lote contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019073652-MP-SIGACTB-CTBA102-CTBA101-Campos-da-capa-do-Lote-cont%C3%A1bil?source=search)
