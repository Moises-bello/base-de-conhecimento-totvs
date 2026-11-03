---
content_hash: 1203464446c00e7803d52cb7aa5ffb98e4a208ece7e8a25fac4f11c0911c153a
fetched_at: '2026-06-28T21:35:22.235904+00:00'
page_id: '235326776'
product: fluig
source: tdn-fluig
title: DES - Como saber com quem o conteúdo será compartilhado no evento beforeSocialShare?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235326776
version: 4
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

# Ocorrência

Para concluir nossos desenvolvimentos sobre a plataforma, necessitamos saber com quem o conteúdo será compartilhado no evento beforeSocialShare

# Solução

No evento beforeSocialShare, são disponibilizados os parâmetros companyId e share. O share permite acesso ao SocialShareEventVO e nele é possível obter os objetos SocialEventVO e SociableEventVO.

O método share.getSocialPlace() permitirá retornar o objeto que recebe o compartilhamento (SocialEventVO).

Este objeto possuí diversos métodos, como por exemplo getAlias() que retorna o código social do usuário que receberá o compartilhamento. O método getName() que retornará o nome do usuário e o método getType(), que permitirá saber se o compartilhamento é com uma comunidade ou usuário.

Segue um exemplo:

js
