---
content_hash: 5203a2f9356767c3ed69be0be4153f6ea3dc296aa6ff8a3edf6fe6ed4213c46b
fetched_at: '2026-06-29T00:09:00.100148+00:00'
page_id: '364917151'
product: rm
source: tdn-rm
title: 'RM - Incidente: Ao gerar o evento S-1200, as verbas de desconto do Plano de
  Saúde não foram lançadas no XML.'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364917151
version: 11
---

Erros e AçõesIncidente

Incidente - Ao gerar o evento S-1200, as verbas de desconto do Plano de Saúde **não** foram lançadas no XML.

Ação

Ação:

* Verifique se existe um evento de desconto de Assistência Medica cadastrado e parametrizado com a rubrica 9219:

* Verifique se o evento está associado na Operadora de Saúde:

* Lance o desconto no envelope de pagamento do funcionário:

* Gere o XML do evento S-1200:

* Verifique na estrutura do XML se o sistema lançou a verba referente ao desconto de Assistência Medica:

**OBS:** Lembrando que se a empresa utiliza Tomador de Serviço , é necessário realizar a Distribuição Sefip antes de realizar a geração do evento S-1200:

**IMPORTANTE:** Caso o funcionário possua dependentes e deseje discriminar os descontos, é necessário verificar se os valores estão lançados no Histórico de Assistência Medica:
