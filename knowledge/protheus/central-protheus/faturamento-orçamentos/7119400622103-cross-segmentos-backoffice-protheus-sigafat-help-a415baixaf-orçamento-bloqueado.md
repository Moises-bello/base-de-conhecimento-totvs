---
article_id: 7119400622103
category: Faturamento - Orçamentos
content_hash: e7cb5c174232f3c6e388d8c067bdbda791343bebec3d94e10e71ce131da6a741
fetched_at: '2026-06-28T22:38:24.967381+00:00'
product: protheus
section_id: 1500001539281
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Help A415BAIXAF Orçamento
  Bloqueado
type: support-article
updated_at: '2026-02-09T19:25:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7119400622103-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Help-A415BAIXAF-Or%C3%A7amento-Bloqueado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38279078678295) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Ao efetivar um orçamento, o sistema gera o help: A415BAIXAF

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7118990173079)  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**  
O Help somente ocorre quando se tenta efetivar um orçamento que esteja bloqueado:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7119054600343)

O orçamento é bloqueado quando possui uma **regra de negócios** e ao efetuar o orçamento, o mesmo atende aos requisitos da regra, como por exemplo, um determinado produto só pode dar desconto de até 5% e no orçamento foi dado 6%, nesta situação o orçamento é bloqueado, não podendo ser efetivado.

Neste caso, deverá adequar o orçamento a regra de negócios ou desabilitar o uso da regra em questão.

**Observação:** O orçamento não possui desbloqueio de regras como ocorre com o pedido de vendas

Para saber qual Regra de Negócio (FATA100) esta bloqueando o Orçamento, basta habilitar o parâmetro MV\_VEBLQRG (.T.) e o sistema disponibilizará no menu "Outras Ações" a opção "Blq. Regra", ao selecionar esta opção, o sistema apresenta o código da Regra de Negócio (FATA100) que gerou o bloqueio, assim como o Motivo do bloqueio e o item bloqueado:

![](https://tdn.totvs.com/download/attachments/271182137/image2020-9-3_18-23-16.png?version=1&modificationDate=1599168196617&api=v2)

Saiba mais:

* [Orçamento de Venda (MATA415) Bloqueado por Regra](https://tdn.totvs.com/x/OekpE)
* [Cross Segmentos - Backoffice Protheus - SIGAFAT - CJ\_STATUS - Orçamento de Vendas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025815874-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-CJ-STATUS-Or%C3%A7amento-de-Vendas)
