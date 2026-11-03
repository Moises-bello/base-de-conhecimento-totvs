---
article_id: 4403611489815
category: Meu RH - Atestado
content_hash: c459016681858cf0f50c2c41b420886939fc15d26a6c70e08472a99ae1e75699
fetched_at: '2026-06-28T22:47:33.171254+00:00'
product: rm
section_id: 1500000861722
source: central-rm
title: RH - RM - Meu RH -  Bloquear visualização no sistema de pre-atestados inseridos
  via Meu RH
type: support-article
updated_at: '2025-01-21T18:48:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403611489815-RH-RM-Meu-RH-Bloquear-visualiza%C3%A7%C3%A3o-no-sistema-de-pre-atestados-inseridos-via-Meu-RH
---

**Dúvida**Como bloquear visualização no sistema de pre-atestados inseridos via Meu Rh  
  
**Ambiente**RM - A partir do release 12.1.32  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Acesse o Modulo Serviços Globais, aba segurança, opção perfis, localize e edite o perfil associado aos funcionários.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28679980512407)  
  
2. Va ate a aba Acesso a Campos  localize a tabela VPREATESTADO e em permissões desmarque os parâmetros destacados abaixo:  
![vpreatestado.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403625703703)  
  
Após realizar a parametrização reinicie o sistema e não serão mais apresentados os pre-atestados inseridos no Meu RH para todos os usuários associados a este perfil.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28679980514839)
