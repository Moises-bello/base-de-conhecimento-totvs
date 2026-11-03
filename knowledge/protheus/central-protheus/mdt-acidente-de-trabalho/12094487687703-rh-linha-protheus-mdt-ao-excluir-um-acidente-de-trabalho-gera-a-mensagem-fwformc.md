---
article_id: 12094487687703
category: MDT - Acidente de Trabalho
content_hash: da071d29d069c018888559caddb9b939839a0f238db8701678a3e3302568940d
fetched_at: '2026-06-28T22:44:23.951496+00:00'
product: protheus
section_id: 360012070513
source: central-protheus
title: RH - Linha Protheus - MDT - Ao excluir um acidente de trabalho gera a mensagem
  FWFORMCANCEL Violação de Integridade. Foi encontrada referência de Acidente (TNC_ACIDEN)
  na tabela TO6 - Questionário do Acidente. Formulário TNCMASTER Linha :1
type: support-article
updated_at: '2025-10-02T19:02:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12094487687703-RH-Linha-Protheus-MDT-Ao-excluir-um-acidente-de-trabalho-gera-a-mensagem-FWFORMCANCEL-Viola%C3%A7%C3%A3o-de-Integridade-Foi-encontrada-refer%C3%AAncia-de-Acidente-TNC-ACIDEN-na-tabela-TO6-Question%C3%A1rio-do-Acidente-Formul%C3%A1rio-TNCMASTER-Linha-1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372874002455) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Ao excluir um acidente de trabalho gera a mensagem "*Help*: FWFORMCANCEL Violação de Integridade. Foi encontrada referência de Acidente (TNC\_ACIDEN) na tabela TO6 - Questionário do Acidente. Formulário TNCMASTER Linha :1", o que avaliar?  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12094447496983)  
  
**Ambiente**TOTVS RH -  (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**

O sistema sempre valida a integridade do registro. Se houver vínculo com outra rotina, não será possível excluir o registro sem antes remover esse vínculo.

Portanto, oriento que seja verificado se o acidente possui vínculo com algum questionário de acidente. Caso exista, remova o vínculo e tente processar novamente a exclusão do acidente.

Acesse: **Atualizações - Acidente de Trabalho - Questionário de Acidente** rotina **MDTA690.**Posicione no acidente que deseja excluir e clique em Questionário, avalie se existe algum vinculo. Retire o vinculo realizando a exclusão do Questionário.  
  
Acesse: **Atualizações - Acidente de Trabalho - Acidente** rotina **MDTA640***.*Posicione no acidente que deseja excluir processe a exclusão.

**Saiba Mais**[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
