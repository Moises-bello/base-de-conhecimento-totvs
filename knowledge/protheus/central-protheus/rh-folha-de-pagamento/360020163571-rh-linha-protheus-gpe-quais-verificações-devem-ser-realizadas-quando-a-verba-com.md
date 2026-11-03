---
article_id: 360020163571
category: RH - Folha de Pagamento
content_hash: 7b5552bd09f72a92bac8a64e2099b6df63a43107a8b00a215f7da65b964c3e62
fetched_at: '2026-06-28T22:44:16.236270+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Quais verificações devem ser realizadas quando
  a verba com ID 0045 for apresentada indevidamente no cálculo
type: support-article
updated_at: '2025-08-13T14:57:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020163571-RH-Linha-Protheus-GPE-Quais-verifica%C3%A7%C3%B5es-devem-ser-realizadas-quando-a-verba-com-ID-0045-for-apresentada-indevidamente-no-c%C3%A1lculo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26247961433623) Tempo aproximado para leitura: 00:01:30 min**

**Dúvida**Quais verificações devem ser realizadas quando a verba com **ID 0045 (Crédito Saldo Insuficiente)** for apresentada indevidamente no cálculo, mesmo quando os valores de proventos sejam maiores do que os descontos?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Verifique na SRV se há amarrações desta verba no campo **RV\_CODMSEG** e no campo **RV\_CODCORR**.

Abra a tabela SRV e realize um filtro para verificar se algum provento está por engano com o campo **PAGAMENTO OBRIGATÓRIO (RV\_OBRIGAT)** igual a **SIM.** Apenas a verba de salário família pode estar com esse campo habilitado. 

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[RH - Linha Protheus - GPE - Como gerar tabela em planilha](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060836073-RH-Linha-Protheus-GPE-Como-gerar-tabela-em-planilha)
