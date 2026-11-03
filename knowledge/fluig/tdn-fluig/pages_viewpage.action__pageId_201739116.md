---
content_hash: 377aa2bf16c0580588da07f0a76c767cb9c4ed5f7f3f157a316451e9e9908364
fetched_at: '2026-06-28T21:35:19.338736+00:00'
page_id: '201739116'
product: fluig
source: tdn-fluig
title: Identity | Provisionar usuário para o Active Directory
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201739116
version: 31
---

.\*ndice

---

O Identity permite que usuários criados dentro do serviço sejam provisionados em um domínio Active Directory vinculado ao contexto.

Usuários provisionados terão informações como nome, sobrenome, e-mail e grupos sincronizadas entre o Identity e o Active Directory, além de poderem utilizar a senha do AD para acessar o Identity.

Este recurso não se aplica aos usuários que foram importados do Active Directory para o Identity, pois estas contas já estão sincronizadas.

# Pré-requisitos

* [SmartSync](https://tdn.totvs.com/x/VIs0DQ) instalado, configurado e em execução.

* [Active Directory configurado](http://tdn.totvs.com/pages/viewpage.action?pageId=201739046) no contexto da empresa no Identity.

* Usuários que tenham sido cadastrados diretamente no Identity, sem ter sido importados do Active Directory.

# Provisionamento

O passo a passo para realizar o provisionamento de um usuário do Identity para o Active Directory pode ser consultado na documentação .
