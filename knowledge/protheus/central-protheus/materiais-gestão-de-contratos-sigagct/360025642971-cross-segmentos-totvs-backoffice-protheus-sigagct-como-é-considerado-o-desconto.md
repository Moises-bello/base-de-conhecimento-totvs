---
article_id: 360025642971
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: b1e61cb28251fc2990f2e79af4a1003d781aed1d04f1038923faa1872fd3fc77
fetched_at: '2026-06-28T22:37:19.851148+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como é considerado
  o desconto informado na Medição nos Títulos Financeiro gerados no seu encerramento  ?
type: support-article
updated_at: '2026-02-06T20:46:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025642971-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-%C3%A9-considerado-o-desconto-informado-na-Medi%C3%A7%C3%A3o-nos-T%C3%ADtulos-Financeiro-gerados-no-seu-encerramento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37894371282711) Tempo aproximado para leitura: **03:00:00min**  
  
**Dúvida**

Como são considerados os descontos no financeiro em títulos gerados pelo encerramento da medição ?

**Ambiente**

Microsiga Protheus – Gestão de contratos – A partir da versão 12

**Solução**

Abaixo seguem as informações sobre o desconto aplicado na medição, e como ele é considerado no no título financeiro que é gerado no encerramento da medição:

Na versão 12 do sistema, os títulos que são gerados no financeiro através do encerramento da medição, levam o valor dos **descontos** aplicados na medição no **campo de Decréscimo (E2\_DECRESC/E1\_DECRESC) do título** e o desconto será aplicado no título somente quando o pagamento do título for realizado pelo processo de baixas a pagar.

Em resumo, todo o desconto, acréscimo, decréscimo, multas, valores acessórios são aplicados no momento do pagamento (Baixas a pagar) e não no momento da inclusão.

Ao fazer a inclusão do título, o cliente poderá emitir o relatório de Contas a Pagar (FINR150), para visualizar o valor liquido.

Segue abaixo um breve exemplo deste processo:

Medição  
===========================  
Valor da medição: R$ 1.000,00  
Valor de desconto: R$ 150,00

Contas a pagar  
===========================  
Valor Original do título: R$ 1.000,00  
Valor de desconto: R$ 150,00   
Valor liquido do título: R$ 850,00

***Saiba Mais:***  
[Processo de Desconto no GCT](http://tdn.totvs.com/display/public/PROT/GCT0117+-+Processo+de+desconto)

[Como são considerados os descontos no financeiro em títulos gerados pelo encerramento da medição,](http://tdn.totvs.com/pages/releaseview.action?pageId=354464789)

[Como configurar o tipo de desconto na medição?](http://tdn.totvs.com/pages/viewpage.action?pageId=239037294)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
