---
article_id: 10384360966679
category: Integrações Outros BackOffice
content_hash: 0c37471ba1e30bbd89893f7286030b7bab687eb1d419cafc4b5530fa813b0136
fetched_at: '2026-06-28T22:46:42.115393+00:00'
product: rm
section_id: 4410716084503
source: central-rm
title: RM - FOP  - Erro lançamento financeiro - unable to cast object of type System.DBfNull
  to type System.string
type: support-article
updated_at: '2024-07-16T11:20:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10384360966679-RM-FOP-Erro-lan%C3%A7amento-financeiro-unable-to-cast-object-of-type-System-DBfNull-to-type-System-string
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21486725139991) Tempo aproximado para leitura: **00:01:03 min****Ocorrência**Erro no lançamento financeiro, é apresentado **unable to cast object of type System.DBfNull to type System.string**  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**  
O Erro é apresentado devido o parâmetro **RH\_NATUREZAFINANCIERADEFAULT** presente nos **Parametros Adapter** não esta cadastrado ou esta com o campo " **Valor** " sem preencher.  
  
**Solução**  
Acesse o módulo Integrações:

Se utilizar EAI 1.0 acesse INTEGRAÇÕES > INTEGRAÇÃO > MENSAGEM ÚNICA > INTEGRAÇÃO > selecione a integração e em anexos selecione Parâmetros de Adapter.  
  
Se utilizar o EAI 2.0 será em INTEGRAÇÕES > EAI 2.0 > PARÂMETROS DE ADAPTER  
  
Crie o parâmetro exatamente como o print abaixo:

COLIGADA = 0 (DEVE SER CRIADO GLOBAL, DIFERENTE DE 0 PODE RETONAR ERRO)  
Nome do Parâmetro = **RH\_NATUREZAFINANCEIRADEFAULT**  
TIPO = TEXTO  
Valor = **Informar o código da natureza financeira a ser levado.**  
  
![](https://totvssuporte.zendesk.com/attachments/token/lgJ5XaVI71a0XzFoSOTDKaahw/?name=image.png)

Após criação do parâmetro, execute novamente a integração do lançamento, caso retorne o erro abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24929388214423)

Configura o KCS abaixo:

[RM - FOP - Integração RM Labore x BackOffice Protheus - Natureza Financeira não integrado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4584852852119-RM-FOP-Integra%C3%A7%C3%A3o-RM-Labore-x-BackOffice-Protheus-Natureza-Financeira-n%C3%A3o-integrado)
