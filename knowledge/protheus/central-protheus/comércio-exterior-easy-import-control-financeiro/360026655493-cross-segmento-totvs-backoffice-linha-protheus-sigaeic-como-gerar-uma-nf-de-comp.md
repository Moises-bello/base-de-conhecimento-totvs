---
article_id: 360026655493
category: Comércio Exterior - Easy Import Control - Financeiro
content_hash: 55ec162fc6c4279f62ed256849b9851a227d48dd44dc4f9d76ae26fd91379254
fetched_at: '2026-06-28T22:39:44.338893+00:00'
product: protheus
section_id: 1500001549642
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Como gerar uma
  NF de Complementar de ICMS para uma Despesa de Acessória
type: support-article
updated_at: '2021-08-24T18:13:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026655493-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Como-gerar-uma-NF-de-Complementar-de-ICMS-para-uma-Despesa-de-Acess%C3%B3ria
---

**Dúvida**Como gerar uma NF de Complementar de ICMS para uma Despesa de Acessória?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
  
**Solução**

Quando a despesa for **complemento de ICMS,** cadastrar da seguinte forma, acesse:

SIGAEIC>Atualizações>Financeiro>Cadastro de Despesas:

- Base de custo = SIM

- Base de imposto = NÃO

- Base de ICMS = SIM

- ICMS na NFT = SIM

- Informar o UF na aba ICMS UF

Existe um parâmetro que define se será calculado ICMS na nota complementar, o mesmo deve estar habilitado: MV\_ICMSNFC.

Para gerar a nota complementar, realizar o seguinte procedimento:

- Acessar a rotina desembaraço -> Manutenção -> Posicionar no processo a ser gerada a nota complementar, clicar em ações relacionadas -> Despesa, informar a despesa base de custo e confirmar.

- Acessar a rotina de Desembaraço -> Recebimento de Importação, posicionar no processo -> Clicar em ações relacionadas -> Complementar.
