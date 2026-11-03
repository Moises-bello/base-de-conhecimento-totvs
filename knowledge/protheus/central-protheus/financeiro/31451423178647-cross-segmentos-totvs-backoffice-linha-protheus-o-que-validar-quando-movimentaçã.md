---
article_id: 31451423178647
category: Financeiro
content_hash: 5b982f00286b4fd0c9180d8148bad724598b2674a750d53e722b26100f0d52d5
fetched_at: '2026-06-28T22:38:01.017208+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - TOTVS BackOffice (Linha Protheus) - O que validar quando
  movimentação de título não é integrado com o contábil
type: support-article
updated_at: '2025-04-16T11:20:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31451423178647-Cross-Segmentos-TOTVS-BackOffice-Linha-Protheus-O-que-validar-quando-movimenta%C3%A7%C3%A3o-de-t%C3%ADtulo-n%C3%A3o-%C3%A9-integrado-com-o-cont%C3%A1bil
---

**Dúvida**O que validar quando movimentações de títulos não são integradas com o contábil?  
  
**Ambiente**Cross Segmento – TOTVS Backoffice (Linha Protheus) – Financeiro – Todas as releases  
  
**Solução** **Cenários gerais:**

De modo geral, primeiramente deve ser validado o **LP** (Lançamento Padrão) especifico da contabilização.

Conforme documentação **TDN** abaixo, cada processo possui seu **LP** especifico, portanto, deverá identificá-lo e confirmar se existe seu cadastro.

[Documentação Lançamento padrão por rotina do financeiro](https://tdn.totvs.com/pages/releaseview.action?pageId=235585410)

Tendo o cadastro, será necessário identificar se a regra imposta no **LP** esta conforme o esperado para a contabilização (**Campo CT5\_VLR01**),  sabendo que, se o retorno for **nulo** ou **Zero,** o registro não é contabilizado. Neste caso, validar possível Sintaxe ADVPL contida para regra.

***OBS:** indicamos o uso do conteúdo padrão **SE5->E5\_VALOR** ou **SE2->E2\_VALOR** ou variável **VALOR** para os primeiros testes e a partir disso, aprimorar sintaxe **ADVPL**.*

**Outros Cenários:**

Caso a contabilização seja de inclusões de títulos provenientes as inclusões automáticas de outros módulos, deve ser observado se a contabilização aconteceu ou não na origem.

**Exemplo:**

Na inclusão de um **documento de entrada**, é geralmente contabilizada a inclusão da nota e criado o registro do título no **contas a paga**r, considerando este cenário, o registro no **contas a pagar**será criado com o campo **E2\_LA = S**e mesmo tendo o **LP 510, não será contabilizado,**pois já foi contabilizado no processo de origem.
