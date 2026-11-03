---
article_id: 1500007999422
category: Portal do Candidato
content_hash: af508c86e89447188656ca2c07b312c60f10f0491ef26ead8d6dc42b7e504b3e
fetched_at: '2026-06-28T22:42:57.878773+00:00'
product: protheus
section_id: 360005048093
source: central-protheus
title: RH - Linha Protheus - PORTAL CANDIDATO - Erro ao enviar e-mail "Operation failed"
type: support-article
updated_at: '2021-04-26T19:38:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007999422-RH-Linha-Protheus-PORTAL-CANDIDATO-Erro-ao-enviar-e-mail-Operation-failed
---

**Dúvida**Ao enviar e-mail no Portal do Candidato é apresentado erro "Operation failed".  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Portal do Candidato – Todas as versões  
  
**Solução**Este erro ocorre quando o domínio especificado no parâmetro **MV\_RHSERV** está incorreto e o parâmetro **MV\_RHAUTEN** está .T. (true) solicitando autenticação do e-mail.   
  
No módulo Configurador (SIGACFG), acesse o menu Ambiente > Cadastro > Parâmetros, filtre o parâmetro **MV\_RHSERV** e configure de acordo com o servidor de e-mail.  
  
Neste exemplo estou utilizando o servidor Gmail.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011870641/mceclip0.png)  
  
**Saiba Mais**[Artigos Portal do Candidato](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048093-RH-Portal-do-Candidato)
