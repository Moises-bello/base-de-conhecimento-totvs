---
article_id: 10462831128343
category: RH - Rescisão
content_hash: 8882a48cc4bf8fda8a9d24fcac35ec22c373db24e1271699a03bb04d9e06e1aa
fetched_at: '2026-06-28T22:43:48.383172+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE -  Funcionalidade do mnemônico P_BASE30HE
type: support-article
updated_at: '2022-11-24T12:23:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10462831128343-RH-Linha-Protheus-GPE-Funcionalidade-do-mnem%C3%B4nico-P-BASE30HE
---

**Dúvida**Qual a funcionalidade do **mnemônico P\_BASE30HE?**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da Versão 12..1.33  
  
**Solução**

Criação do mnemônico **P\_BASE30HE** para permitir que horas extras na rescisão sejam calculadas com base em 30 dias em período que possui 31 dias, 30 dias para cálculo e o mnemônico **P\_DIASRES** estiver configurado com **1**.

Dessa forma, caso o mnemônico **P\_BASE30HE**esteja ativo, isto é, configurado com **.T.**, verbas de horas e dias incluídas na rescisão serão calculadas com base em 30 dias.

O mnemônico P\_BASE30HE permite duas configurações:

* .F. = Falso. Efetua o cálculo da hora extra na rescisão de acordo com os dias de cálculo do mês.;
* .T. = Verdadeira. Efetua o cálculo da hora extra na rescisão com base em 30 dias.

Segue exemplo para esclarecer a diferença:  
  
Período 10/2022, possui 31 dias, está configurado com **30** dias para cálculo.

O mnemônico P\_DIASRES está ativo, isto é, está configurado com **1**.

Funcionário com salário mensal de R$ 1.200,00, com 220 horas mensais no cadastro, ou 7,3333 horas/dia.

Cálculo de 10 horas extras a 100%:

| Configuração | Valor calculado | Explicação |
| --- | --- | --- |
| P\_BASE30HE configurado com .F. | R$ 105,57 | R$ 1.200,00**÷**(7,3333 X**31**) X 2 X 10 = R$ 105,57 |
| P\_BASE30HE configurado com .T. | R$ 109,09 | R$ 1.200,00**÷**(7,3333 X**30**) X 2 X 10 = R$ 109,09. |

**Saiba mais**Para adquirir maior conhecimento acesse o *link* abaixo

[RH - Linha Protheus - GPE - Como calcular rescisão de acordo com os dias do mês ou sempre por 30 (divisão salário) (P\_DIASRES)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025315674-RH-Linha-Protheus-GPE-Como-calcular-rescis%C3%A3o-de-acordo-com-os-dias-do-m%C3%AAs-ou-sempre-por-30-divis%C3%A3o-sal%C3%A1rio-P-DIASRES-?source=search)

<https://tdn.totvs.com/pages/releaseview.action?pageId=721721855>

<https://tdn.totvs.com/pages/releaseview.action?pageId=721023886>
