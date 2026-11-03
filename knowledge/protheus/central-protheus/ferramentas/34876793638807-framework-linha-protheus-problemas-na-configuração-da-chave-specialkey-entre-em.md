---
article_id: 34876793638807
category: Ferramentas
content_hash: 30e7b9025acc177d97dafda121c7ffe928b1a9df58c658ab7a45e546dacb2271
fetched_at: '2026-06-28T22:42:17.971646+00:00'
product: protheus
section_id: 360000075448
source: central-protheus
title: Framework - Linha Protheus - Problemas na configuração da chave SpecialKey,
  entre em contato com o Administrador! on MYSPECIALKEY
type: support-article
updated_at: '2025-09-11T20:18:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34876793638807-Framework-Linha-Protheus-Problemas-na-configura%C3%A7%C3%A3o-da-chave-SpecialKey-entre-em-contato-com-o-Administrador-on-MYSPECIALKEY
---

**Dúvida**

Mensagem apresentada no acesso ao Protheus: Problemas na configuração da chave SpecialKey, entre em contato com o Administrador! on MYSPECIALKEY

**Ambiente**  
Protheus - Appserver - A partir da versão 12

**Solução**

Dentro dos Appserver.ini's, avalie a chave Specialkey, se está com o mesmo nome dentro dos ambientes que apontam para o mesmo banco de dados e Protheus\_data.

Segue documentação completa: [SpecialKey](https://tdn.totvs.com/display/framework/SpecialKey)
