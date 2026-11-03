---
article_id: 22006607105943
category: Encargos
content_hash: e985c32af4a0b316539497a32813aaa7504d9f9b783944b799549269fee4ecea
fetched_at: '2026-06-28T22:46:52.281850+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP -  Como gerar Lançamento Financeiro na Folha para unificar INSS
  e IRRF na DCTFWeb
type: support-article
updated_at: '2024-09-16T18:04:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22006607105943-RH-RM-FOP-Como-gerar-Lan%C3%A7amento-Financeiro-na-Folha-para-unificar-INSS-e-IRRF-na-DCTFWeb
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22006607077911) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**

# [DCTFWeb - Como chegar no valor da DARF a recolher? Será possível unificar as DARF de INSS e IRRF?](https://tdn.totvs.com/pages/viewpage.action?pageId=808478015)

**Ambiente**

* 12.1.2302.192
* 12.1.2306.135
* 12.1.2310.001

**Solução**

A folha de pagamento gera os valores tributados na folha de pagamento conforme enviado ao eSocial através dos eventos S-1200 e S-1210, de acordo com a parametrização realizada nos tipos de lançamentos financeiros: "**2****5-DCTFWeb Folha**" e "**26-Total Guia INSS DCTFWeb 13º Salário**".

Para obter mais detalhes, consulte o TDN  [DT - Lançamento Financeiro: "25-Total Guia INSS DCTFWeb" e "26-Total Guia INSS DCTFWeb 13º Salário"](https://tdn.totvs.com/pages/viewpage.action?pageId=727915586) e [Parametrização dos Lançamentos Financeiros](https://tdn.totvs.com.br/display/LRM/Cadastros+Financeiros)

É importante gerar o relatório de conferência antes de realizar a geração do lançamento financeiro, garantindo a compatibilidade entre os valores da folha de pagamento e aqueles gerados pelo eSocial.

Veja detalhes no TDN: [Middleware - Relatório de Conferência de INSS](https://tdn.totvs.com/pages/viewpage.action?pageId=536721262) e [Relatório de Conferência INSS Patronal#1](https://tdn.totvs.com/pages/viewpage.action?pageId=714242305#Relat%C3%B3riodeConfer%C3%AAnciaINSSPatronal-1)

**ATENÇÃO:**Os montantes de retenção previstos na Lei 9.711 serão encaminhados por meio da REINF. Nesse contexto, caso a empresa pretenda deduzir tais valores na folha de pagamento, será necessário acessar tanto a DCTFWeb quanto o setor financeiro para efetuar essa configuração.

**OBSERVAÇÃO:**Qualquer dúvida referente a esse processo deverá acionar o atendimento de Folha de Pagamento.

Segue o link com mais informações:

[DCTFWeb - Como chegar no valor da DARF a recolher? Será possível unificar as DARF de INSS e IRRF?](https://tdn.totvs.com/pages/releaseview.action?pageId=808478015)
