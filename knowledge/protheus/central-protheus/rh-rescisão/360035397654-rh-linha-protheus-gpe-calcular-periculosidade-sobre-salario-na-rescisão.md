---
article_id: 360035397654
category: RH - Rescisão
content_hash: 1072298dfd71cf6765cca25944d8dae5edbab91b0fe024fa4d291850c4a41785
fetched_at: '2026-06-28T22:43:51.112325+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Calcular Periculosidade sobre salario na rescisão
type: support-article
updated_at: '2025-06-13T11:54:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035397654-RH-Linha-Protheus-GPE-Calcular-Periculosidade-sobre-salario-na-rescis%C3%A3o
---

**Dúvida**Ao efetuar calculo de rescisão sistema considera salario mais verbas para calcular a periculosidade de acordo com o cadastro do sindicato. Como considerar apenas salario para base da periculosidade sem alterar o cadastro do sindicato?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046043314/mceclip0.png)

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17

**Solução**

Ajustar o mnemônico P\_RESADISB para .T.

Quando o conteúdo do mnemônico está com valor Verdadeiro (**.T.**), o sistema irá utilizar somente o Salario Base para o cálculo dos Adicionais para as verbas indenizatórias.

Abaixo um link do tdn contendo detalhes sobre o mnemônico

<https://tdn.totvs.com/pages/viewpage.action?pageId=337347883>
