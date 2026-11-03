---
article_id: 26984777531031
category: RH - Folha de Pagamento
content_hash: bc90bae2697d2961217c9e11e6c8e06f471680c3ad3ac0ab2a21168e645670b9
fetched_at: '2026-06-28T22:44:12.235926+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular Contribuição Assistencial para comissionado
  puro
type: support-article
updated_at: '2025-11-07T19:54:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26984777531031-RH-Linha-Protheus-GPE-Como-calcular-Contribui%C3%A7%C3%A3o-Assistencial-para-comissionado-puro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26984775583767) Tempo aproximado para leitura: **02:00:00min**

**Dúvida**Como calcular Contribuição Assistencial para comissionado puro?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões

**Solução**

Para calcular Contribuição Assistencial para o funcionário categoria Comissionado, deve-se utilizar os cadastros conforme abaixo:

**1º** A verba de Comissão, DSR de comissão e Garantia de comissão, devem ter o campo **Incorpora**  
**salario igual** a **SIM** para ajustar as verbas acesse **Atualizações > Definições de Cálculos > Verbas (GPEA040)**;

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26984775589783)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26984775590807)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26984775594391)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26984777491223)**

**2º** No cadastro do Sindicato em **Atualizações > Cadastros > Sindicatos (GPEA340)** o campo **Tipo de Salario** deve estar igual a **Composto**;  
O campo Tipo Referencia pode estar como Percentual, ou Valor

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26985361466391)

**3º** No cadastro do Funcionário em **Atualizações > Funcionários > Funcionários (GPEA010)** o campo **Contribuição Assistencial** deve estar igual a **SIM**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26985361470231)

**4º** Calcule a folha em **Miscelânea > Cálculos > Por Roteiro (GPEM020)**;

**5º** Visualize o cálculo pela rotina lançamentos por funcionários em **Atualizações > Lançamentos > Por Funcionários (GPEA580)**;

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26984775610135)**

**Saiba mais:**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
