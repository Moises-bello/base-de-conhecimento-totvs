---
article_id: 360039488794
category: Comércio Exterior - Easy Export Control - Embarque
content_hash: cc47883a17058b546a590fc3a144c8210f5c08810044ca677c31c9980b8db611
fetched_at: '2026-06-28T22:36:39.196159+00:00'
product: protheus
section_id: 1500001549322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Já existe mensagem
  recebida com UUID enviado
type: support-article
updated_at: '2022-06-09T20:46:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039488794-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-J%C3%A1-existe-mensagem-recebida-com-UUID-enviado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:02:00 min  
  
Dúvida**Como corrigir a mensagem: Já existe mensagem recebida com UUID enviado. Para os processos de integração entre Protheus e Logix.

![](https://atendimento.totvs.com/attachments/token/ULwoAGKlHFXAwaffWXzse1mIQ/?name=image002.png)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – A partir da versão 12.1.17  
  
**Solução**Para solução do incidente verifique o parâmetro **MV\_EAIURL2** - Parâmetro que indica ao **EAI Protheus** para qual endereço de *Webservices* a mensagem será disparada. Este parâmetro é utilizado quando o **adapter** está cadastrado com o **Canal Envio** (XX4\_CHANEL) =EAI;  Este parâmetro precisa estar configurado para o *Webservice* do Logix, caso esteja configurado para o *Webservice* do Protheus será apresentada a mensagem de inconsistência.  
  
**Saiba mais**  
[A camada do EAI](https://tdn.totvs.com/display/framework/A+camada+do+EAI#AcamadadoEAI-_Toc403759539)
