---
article_id: 8978026790167
category: Evento S-2210
content_hash: 991911f921776aef1a5cd641637550ef2998704c062709b2c9318f1804f77ab6
fetched_at: '2026-06-28T22:45:24.395863+00:00'
product: protheus
section_id: 8260521640983
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2210 - Ao gerar o evento S-2210 aparece
  a mensagem "Órgão de Classe em Branco", o que conferir
type: support-article
updated_at: '2024-07-31T11:50:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8978026790167-RH-Linha-Protheus-MDT-eSocial-S-2210-Ao-gerar-o-evento-S-2210-aparece-a-mensagem-%C3%93rg%C3%A3o-de-Classe-em-Branco-o-que-conferir
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25281692656919) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ao gerar o evento S-2210 aparece a mensagem "Órgão de Classe em Branco", o que conferir?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**O órgão de classe deve *(***TMK\_ENTCLA ou TNP\_ENTCLA**) ser preenchido. Caso as informações do atendimento médico sejam enviadas pelo atestado, o campo a ser preenchido para envio do órgão de classe é o **TNY\_EMITEN** e caso as informações do atendimento médico sejam enviadas pelo diagnóstico o campo a ser preenchido para envio do órgão de classe é o **TMT\_CODUSU**.  
  
Órgão de Classe deve ser igual a **1- CRM, 2- CRO ou 3- RMS**.  
  
O órgão de classe deve (TMK\_ENTCLA ou TNP\_ENTCLA*)* deve ser igual a **CRM, CRO** ou **RMS.**   
  
Para ajuste, acesse o menu Atualizações > Atendimento Médico > Atestado Médico e preencha o campo "**Emit. Atest.**":  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25281692673047)  
  
ou  
  
Menu Atualizações > Atendimento Médico > Diagnóstico Médico, preencha o campo **Médico**:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25281739341591)  
  
Caso o conteúdo do campo TMK\_ENTCLA ou TNP\_ENTCLA conter a palavra **CRM**, o sistema envia automaticamente o código **1**.  
Caso o conteúdo do campo TMK\_ENTCLA ou TNP\_ENTCLA conter a palavra **CRO**, o sistema envia automaticamente o código **2**.  
E caso o conteúdo do campo TMK\_ENTCLA ou TNP\_ENTCLA conter a palavra **RMS** o sistema envia automaticamente o código **3**.  
  
Quer saber mais sobre a regra de busca das informações do atendimento médico do acidente através? Consulte o *link* abaixo.  
[Envio das Informações do Atendimento Médico no Evento S-2210 do eSocial](https://tdn.totvs.com/pages/releaseview.action?pageId=628970344)  
  
**Saiba Mais**  
[Artigos sobre Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos sobre eventos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
