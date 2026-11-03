---
article_id: 360053279274
category: Portal de Gestão de Capital Humano
content_hash: 8c15f4222d952875a52ab8f239a5f4659e4202b70f0f20e6558cb5fcd495ac72
fetched_at: '2026-06-28T22:42:58.899225+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: 'RH - Linha Protheus - PORTAL GCH - Ao logar no portal  ocorre o erro AUTHENTICATION:
  USER NOT AUTHORIZED'
type: support-article
updated_at: '2024-11-05T12:08:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053279274-RH-Linha-Protheus-PORTAL-GCH-Ao-logar-no-portal-ocorre-o-erro-AUTHENTICATION-USER-NOT-AUTHORIZED
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27566863956887) Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida**Ao Logar no portal ocorre o erro AUTHENTICATION: USER NOT AUTHORIZED.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Portal Gestão Capital Humano - Todas as versões  
  
**Solução** A partir da *LIB Label* 20201019, a ser liberada em Outubro de 2020, o comportamento padrão de autenticação de *WebServices* *SOAP* e *REST* será alterado.  
  
Para os *Webservices* e *REST* precisamos atualizar a forma de autenticação. A partir desta versão, caso a chave *Security* não seja informada no arquivo appserver.ini, os serviços serão iniciados exigindo autenticação de usuário.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4421499607447)  
  
Caso seja necessário trabalhar sem autenticação, a chave deverá ser configurada com o valor 0 (Exemplo: **Security=0**).  
  
A inclusão da Tag **SECURITY=0** deve ser feita em todos os Jobs dos ***WebServices*** e ***URL's*** de Portais conforme exemplo abaixo:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4421518074135)  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4421518120855)  
Segue a documentação sobre a mudança no link abaixo:  
[Alteração de Comportamento - Autenticação SOAP e REST](https://tdn.totvs.com/pages/releaseview.action?pageId=539697514)  
  
IMPORTANTE   
**SECURITY=0** conforme sugestões acima são aplicadas da versão 2310 pra baixo.   
Para versão 2410 em diante é obrigatório o uso do **SECURITY=1.**Deve ser configurado conforme acima mas com **SECURITY=1.**Para versão 2410 em diante é obrigatório aplicar a documentação abaixo:  
[Configuração portais GCH com autenticação **SECURITY=1**](https://tdn.totvs.com/pages/releaseview.action?pageId=563435668)  
  
**Saiba Mais  
[Central de artigos Portal Gestão Capital Humano](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)**
