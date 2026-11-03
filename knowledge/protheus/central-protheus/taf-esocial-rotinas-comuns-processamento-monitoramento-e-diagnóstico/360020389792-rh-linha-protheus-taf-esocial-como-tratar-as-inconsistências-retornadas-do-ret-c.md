---
article_id: 360020389792
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: 035d8264bc85ec7b798381ad19cae390f6fedd1f437c00862615bf46cf15ce1c
fetched_at: '2026-06-28T22:45:21.133766+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Como tratar as inconsistências retornadas
  do RET, como Código do erro 721 e Código do erro 125
type: support-article
updated_at: '2026-06-26T12:12:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020389792-RH-Linha-Protheus-TAF-eSocial-Como-tratar-as-inconsist%C3%AAncias-retornadas-do-RET-como-C%C3%B3digo-do-erro-721-e-C%C3%B3digo-do-erro-125
---

**Dúvida**

Como tratar as inconsistências retornadas do RET, como **Código do erro 721 e** **Código do erro 125**?  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Rotinas Comuns - Versão 12.1.2310.

**Solução**O e-Social identificou que o Período dos Eventos Periódicos onde o evento está sendo inserido, possui o evento S-1299 de fechamento, ou S-1295 de fechamento em contingência (código de erro 125). Por consequência, não permite o registro de nenhum evento dentro deste período fechado (código de erro 721).

**Código do erro 721:** "Não foi possível registrar o evento atual pois existe(m) cadastro(s) com data de ocorrência posterior para esse trabalhador que se tornarão inconsistentes em caso de recepção deste...."

**Código do erro 125:** "O movimento deste período já se encontra fechado. Para enviar admissão de novos trabalhadores é necessário reabrir o movimento."Foi transmitido para o e-Social determinado evento, de inclusão ou alteração, e retorna inconsistente, informando o **código de erro 721** e **125:**

*![RET_cod_erro_721_125.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360016572552)*

Para **solucionar** os erros gerados, siga o passo a passo:

**1.** Reabra o Período dos Eventos Periódicos que encontra-se fechado, através do evento S-1298 - Reabertura dos Eventos Periódicos;

Esse evento é gerado somente pelo TAF, acesse o menu principal **Atualizações > Eventos eSocial > Periódicos > Reabertura Periódicos:**

![RET_cod_erro_721_125_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016625911)

**2.** Após transmissão consistente da Reabertura dos Eventos Periódicos (S-1298), transmita o evento anteriormente rejeitado;   
  
**3.** Após as alterações necessárias, o período deverá ser fechado novamente com o evento S-1299 - Fechamento dos Eventos Periódicos ou 1295 - Fechamento em Contingência.
