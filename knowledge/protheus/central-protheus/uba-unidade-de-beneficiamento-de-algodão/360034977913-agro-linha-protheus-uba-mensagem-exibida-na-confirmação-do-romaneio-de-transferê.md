---
article_id: 360034977913
category: UBA - Unidade de Beneficiamento de Algodão
content_hash: ec6708b29ab13ba8c464e43320243b8de47d9a79799985c312373dc2dc4efa3f
fetched_at: '2026-06-28T22:45:35.625274+00:00'
product: protheus
section_id: 360005717853
source: central-protheus
title: Agro - Linha Protheus - UBA - Mensagem exibida na confirmação do romaneio de
  transferência
type: support-article
updated_at: '2025-06-20T17:39:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034977913-Agro-Linha-Protheus-UBA-Mensagem-exibida-na-confirma%C3%A7%C3%A3o-do-romaneio-de-transfer%C3%AAncia
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21973210468375)**Tempo aproximado para leitura: **00:00:25 min**  
 **Ocorrência**Na rotina **AGRA500 - Romaneio Unificado** ao confirmar um registro é exibida a mensagem: **Entidade inválida para o tipo de operação do romaneio**.  
  
 **Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - UBA - Unidade de Beneficiamento de Algodão - Versão 12  
  
 **Causa**Essa mensagem é exibida porque o Sistema não permite que sejam efetuadas transferências, tanto do tipo **A - Entrada**, quanto do tipo **B - Saída**, para a mesma filial.  
  
 **Solução**  
Para que a mensagem não seja exibida é necessário alterar a entidade informada no registro de romaneio, a fim de que seja uma entidade diferente da filial logada.
