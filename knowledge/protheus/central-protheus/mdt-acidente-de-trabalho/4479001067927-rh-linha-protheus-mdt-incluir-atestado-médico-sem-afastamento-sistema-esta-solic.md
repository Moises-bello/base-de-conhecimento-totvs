---
article_id: 4479001067927
category: MDT - Acidente de Trabalho
content_hash: 48b00b1e0f90fc673c449875f70fe2f6ac39f6f9685b945ee510e312507b4b3a
fetched_at: '2026-06-28T22:44:23.941845+00:00'
product: protheus
section_id: 360012070513
source: central-protheus
title: RH - Linha Protheus - MDT -  Incluir atestado médico sem afastamento, sistema
  esta solicitando preenchimento da quantidade de dias (dias perdido)
type: support-article
updated_at: '2025-07-31T14:08:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4479001067927-RH-Linha-Protheus-MDT-Incluir-atestado-m%C3%A9dico-sem-afastamento-sistema-esta-solicitando-preenchimento-da-quantidade-de-dias-dias-perdido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20007977466391) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Ao Incluir atestado médico sem afastamento, sistema esta solicitando preenchimento da quantidade de dias (dias perdido).  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4478878590615)  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho -  Todas as versões  
  
**Solução**O campo "Dias perdido" (TNC\_QTAFAS) é **obrigatório** quando o campo o campo "Afastamento" (TNC\_AFASTA) estiver igual a 1.Sim, desta forma deverá preencher os campos "Dt.Atend.Med" (TNC\_DTATEN) e "Hr.Atendim." (TNC\_HRATEN) estão preenchidos.  
  
No menu Atualizações - Acidente Trabalho - Acidentes, localize o registro e verifique os campos citados "Dt.Atend.Med e Hr.Atendim." não precisam ser preenchidos no momento da CAT, já que esses campos também estão presente no cadastro do atestado.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10467899687447)  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4478964805143)  
  
Campo "Dias Perdido" igual 2.Não o sistema não irá permitir o preenchimento do campo Dias Per.  (TNC\_QTAFAS)

Retornará a mensagem "Problema: Esse campo somente deve ser informado quando o campo Afastamento for igual a Sim."  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10467971197335)

Para mais informações de como gerar a CAT, verifique o artigo: [RH - Linha Protheus - MDT - eSocial - S-2210 - Como emitir uma CAT evento S-2210 no eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409360161047)  
  
[Envio das Informações do Atendimento Médico no Evento S-2210 do eSocial](https://tdn.totvs.com/pages/releaseview.action?pageId=628970344)  
  
**Saiba Mais**  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
