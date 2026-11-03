---
article_id: 17564654562583
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: d23402a81500804f64613c65b5af89498dd073760aa1d76aed5b1fcfd008cd45
fetched_at: '2026-06-28T22:39:09.449431+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 - Como configurar
  o parâmetro MV_A010FAC para adicionar campos corretamente e seu limite?
type: support-article
updated_at: '2025-03-27T13:31:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17564654562583-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-Como-configurar-o-par%C3%A2metro-MV-A010FAC-para-adicionar-campos-corretamente-e-seu-limite
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17564662956183) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Qual o limite máximo de campos para o Facilitador de Produtos, dentro do parâmetro MV\_A010FAC, e como configurar?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**O parametro MV\_A010FAC, tem a seguinte finalidade:

"Este parâmetro tem como objetivo informar campos da tabela SB1 (Descrição genérica de produtos) que não são considerados no padrão."

Exemplo de como configurar:

Defina os campos separados por barras /, e insira a barra no final do ultimo campo.

Exemplo abaixo: **B1\_EMIN/B1\_ESTSEG/B1\_PE/**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17564285138967)

Dessa forma você poderia utiliza-los no facilitador:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30965480381463)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17564423005463)

**Qual é o tamanho maximo de campos permitidos?**

Atualmente o tamanho é de acordo o que existe dentro da sua SX6, na avaliada agora, o campo possuem 142 caracteres, e esses não podem ser alterados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17564544816663)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
