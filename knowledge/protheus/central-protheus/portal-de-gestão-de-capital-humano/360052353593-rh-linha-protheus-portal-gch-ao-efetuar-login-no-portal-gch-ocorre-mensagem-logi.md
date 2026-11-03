---
article_id: 360052353593
category: Portal de Gestão de Capital Humano
content_hash: a82c6f8256fb9055db6c6d9631483c4c4dc9672cf61b819d53ed40fae4d6f911
fetched_at: '2026-06-28T22:42:58.893266+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: 'RH - Linha Protheus - PORTAL GCH - Ao efetuar login no Portal GCH ocorre mensagem
  "Login Inválido: Perfil do usuário não localizado"'
type: support-article
updated_at: '2023-08-28T14:36:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052353593-RH-Linha-Protheus-PORTAL-GCH-Ao-efetuar-login-no-Portal-GCH-ocorre-mensagem-Login-Inv%C3%A1lido-Perfil-do-usu%C3%A1rio-n%C3%A3o-localizado
---

**Dúvida**Ao efetuar login no Portal GCH ocorre mensagem "Login Inválido: Perfil do usuário não localizado".  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082756973/mceclip0.png)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Portal Gestão do Capital Humano – Todas as versões  
  
**Solução**No módulo SIGAAPD, na rotina *Atualizações > Participantes > cadastro*, na aba "Outros" verifique se o campo **"Usuário Portal"** está preenchido.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082757213/mceclip1.png)  
  
No módulo Configurador, na rotina *Base de Dados > Dicionário > Base de Dados* deve verificar se as tabelas (AI3, AI6, AI7, AI8 e AI9) estão com mesmo compartilhamento.  
Após os ajustes, efetue login no Portal GCH novamente.  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o Portal GCH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)
