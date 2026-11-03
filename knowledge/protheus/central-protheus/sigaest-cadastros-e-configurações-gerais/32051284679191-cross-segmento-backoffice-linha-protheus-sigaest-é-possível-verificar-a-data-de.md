---
article_id: 32051284679191
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 19141a946976fb1d4d8b9835fb02afaa07cf0063bc8952366a816897b3793b96
fetched_at: '2026-06-28T22:39:08.208808+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - É possível verificar
  a data de criação de um código de produto na tabela SB1?
type: support-article
updated_at: '2025-05-12T19:56:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32051284679191-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-%C3%89-poss%C3%ADvel-verificar-a-data-de-cria%C3%A7%C3%A3o-de-um-c%C3%B3digo-de-produto-na-tabela-SB1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32051284673431) Tempo aproximado para leitura: 00**:**01:00 min **Dúvida**

Existe algum relatório ou campo na tabela SB1 que informe a data de criação do código de produto?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Atualmente, a tabela SB1 não possui um campo nativo que registre a data de criação do código de produto. No entanto, é possível obter essa informação por meio da funcionalidade **Audit Trail**, desde que esteja previamente habilitada no ambiente.

Ao ativar o Audit Trail, o sistema passa a registrar o evento de inclusão, incluindo a data de criação do registro. Vale ressaltar que os dados anteriores à habilitação do Audit Trail **não serão retroativamente registrados**, ou seja, não será possível identificar a data de criação de produtos que já existiam antes da ativação da funcionalidade.

Para mais informações sobre como configurar o Audit Trail, consulte a documentação oficial da TOTVS no link abaixo:

[https://tdn.totvs.com/display/public/framework/Configurar+Embedded+Audit+Trail](Audit%20Trail)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
