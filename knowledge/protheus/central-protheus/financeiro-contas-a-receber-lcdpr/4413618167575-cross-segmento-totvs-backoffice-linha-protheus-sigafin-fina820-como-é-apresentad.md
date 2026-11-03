---
article_id: 4413618167575
category: Financeiro - Contas a Receber - LCDPR
content_hash: 6d96e4a0a66147cf3de08bbdf476bebc533227fdcbdce3728c4fc6a396ea2558
fetched_at: '2026-06-28T22:38:15.843023+00:00'
product: protheus
section_id: 1500001539361
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) – SIGAFIN - FINA820 - Como
  é apresentado o FUNRURAL no LCDPR
type: support-article
updated_at: '2022-03-24T19:21:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413618167575-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-FINA820-Como-%C3%A9-apresentado-o-FUNRURAL-no-LCDPR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) **Tempo aproximado para leitura: 00:00:02 min****Dúvida**Como é apresentado o FUNRURAL no LCDPR?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Financeiro – A partir da versão 12  
  
**Solução**

De acordo com a documentação do perguntas e respostas do link <https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/declaracoes-e-demonstrativos/lcdpr-livro-caixa-digital-do-produtor-rural/perguntas-e-respostas-livro-caixa-digital-do-produtor-rural-lcdpr.pdf>

Pergunta 36

Uma vez que o produtor rural escriturará a receita de venda da produção pelo valor bruto

da nota fiscal, como deverá escriturar o valor retido pelo adquirente e qual código deve ser

preenchido no campo **COD\_CONTA** do **registro Q100**?

As retenções realizadas pelo adquirente de produção do produtor rural devem ser registradas como

despesa no **registro Q100** utilizando o código “999 – Numerário em trânsito” no campo

**Livro Caixa Digital Produtor Rural** (**LCDPR**)

Perguntas e Respostas

**COD\_CONTA**, o CPF ou CNPJ do adquirente no campo **ID\_PARTIC** e apontado o número da nota fiscal

de origem do valor retido no campo **HIST** do registro.

A mesma regra deve ser aplicada em casos de abatimentos de vendas que ocorrem posteriormente

à operação (descontos condicionais concedidos).

Pergunta 37

Quando o produtor realiza uma compra com pagamento antecipado e emissão de nota

fiscal de entrega futura com posterior emissão de notas fiscais de simples remessa pelo vendedor

por ocasião da entrega das mercadorias, qual código deverá ser utilizado no campo **COD\_CONTA**

do **registro Q100** na data do recebimento dos produtos/mercadorias e qual a nota fiscal a ser

escriturada?

Quando o produtor rural realiza uma compra com pagamento antecipado, deve utilizar o código da

conta corrente em que foi realizado o débito do pagamento e o número da nota fiscal de simples

remessa no campo **NUM\_DOC** do **registro Q100**, informando o número e data da nota fiscal de

entrega futura no **campo HIST** do mesmo registro.

**Exemplo:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413618151703/mceclip0.png)**

A linha Q100 da NF deve conter o valor bruto.

A linha Q100 do imposto abatendo o valor total da NF e sendo de numerário 999.

A linha Q200 deve sempre conter o valor real recebido. No caso do exemplo acima R$1.000,00 – R$100,00 = R$900,00.
