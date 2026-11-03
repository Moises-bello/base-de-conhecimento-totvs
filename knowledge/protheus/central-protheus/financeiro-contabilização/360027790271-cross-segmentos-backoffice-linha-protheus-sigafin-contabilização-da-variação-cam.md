---
article_id: 360027790271
category: Financeiro - Contabilização
content_hash: 01f55fff5bd4517b74ecbe31dcc62baf98be5994047f8d57b269d049218afa83
fetched_at: '2026-06-28T22:38:05.210601+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Contabilização da variação
  cambial ou correção monetária no Protheus
type: support-article
updated_at: '2026-06-12T17:15:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027790271-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Contabiliza%C3%A7%C3%A3o-da-varia%C3%A7%C3%A3o-cambial-ou-corre%C3%A7%C3%A3o-monet%C3%A1ria-no-Protheus
---

**Dúvida**  
Como funciona a contabilização de correção monetária ou variação cambial no *Protheus*.  
  
**Ambiente**  
Microsiga Protheus – Financeiro – A partir da versão 11.80  
  
**Solução**  
O sistema trata de forma diferente **Correção Monetária** / **Variação Cambial**. Desta forma o conceito dos dois são diferentes no sistema *Protheus*.

**Variação Cambial**  
A variação cambial é a diferença das moedas comparando a data de compra/venda até a data de pagamento/recebimento, ou seja a variação da moeda do título desde sua inclusão até sua baixa.

**Variação Cambial no sistema Protheus**.  
Contabilizar a variação monetária através da rotina **FINA350**, deve-se utilizar as LP´s.  
**598 Na Variação Monetária - Contas a Receber**  
**599 Na Variação Monetária - Contas a Pagar**

**Exemplo:**  
Utilize este processo quando precisar contabilizar a variação da moeda no período em que o título não for baixado (dia-dia).

**Importante:**  
A rotina **FINA350** não contabiliza registros baixados.  
Ao executar a rotina **FINA350** ocorrerá a contabilização dos registros e a rotina irá ajustar os campos **E1\_DTVARIA** e **E1\_TXMDCOR**, desta forma atualiza o título com a nova taxa, ou seja ao baixa-lo o sistema irá considerar a nova taxa (**E1\_TXMDCOR**).

\*\*Sempre ao executar a rotina **FINA350** esses campos vão ser atualizados, não tendo histórico.

**Saiba Mais:**  
**Variação Cambial:**  
<http://tdn.totvs.com/pages/viewpage.action?pageId=244934660>

[MP - SIGAFIN - FINA350 - Quais os Lp's (Lançamento Padrão) utilizados na Correção Monetário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023379792-MP-SIGAFIN-FINA350-Quais-os-Lp-s-Lan%C3%A7amento-Padr%C3%A3o-utilizados-na-Corre%C3%A7%C3%A3o-Monet%C3%A1rio-?source=search)

**Lançamento Padrão Financeiro**  
https://tdn.totvs.com/pages/releaseview.action?pageId=532386758

**Correção Monetária**  
A correção monetária é a diferença das moedas comparando a data de compra/venda x data de pagamento/recebimento, ou seja o valor "corrigido" e final sobre aquela movimentação (baixa).

**Correção Monetária no Sistema Protheus**  
Para contabilizar a **correção monetária** no momento da baixa, utilize as LP de baixa da rotina **Contas a Pagar ou Contas a Receber** e utilize o campo **SE5->E5\_VLCORRE**.

**Exemplo:**  
Ao precisarmos contabilizar a **correção monetária** no momento da baixa, podemos utilizar o campo/expressão ABS(**SE5->E5\_VLCORRE**).

Lembrando que o escopo de atendimento do *help-desk* não contempla auxilio/manutenção nas expressões **ADVPL**.

**Importante:**  
Tanto na variação quanto na correção, temos a opção de ser uma correção/variação ATIVA ou PASSIVA.

Ativa = Valor positivo  
Passiva = Valor negativo

Como sabemos que na contabilidade não tem valor negativo, devemos utilizar a função ABS.

**Saiba mais Correção Monetária**:  
<http://tdn.totvs.com/pages/releaseview.action?pageId=235585410> - Lp´s por rotina  
<http://tdn.totvs.com/pages/viewpage.action?pageId=23888835> - Função ABS
