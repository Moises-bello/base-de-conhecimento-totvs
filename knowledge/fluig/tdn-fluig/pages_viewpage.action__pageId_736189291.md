---
content_hash: 3b08d6704c1bf725485e5febe9a9eae56e44af4401f00cea5f47e12103fde7fc
fetched_at: '2026-06-28T21:35:29.085549+00:00'
page_id: '736189291'
product: fluig
source: tdn-fluig
title: Identity | Controle de segurança de token
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=736189291
version: 8
---

# Falando de controle de segurança de token...

---

O recurso de controle de segurança de token tem o objetivo de evitar a ocorrência de ataques do tipo Falsificação de Requisição Cross Site (CSRF). O TOTVS Identity pode fazer a geração de tokens com o SameSite *Lax* ou *Strict*. O *Lax* faz com que os tokens só possam ser usados por GETs de primeiro nível por outras URLs, enquanto o *Strict* impede qualquer interação de outras URLs com o token.

## Configurar controle de segurança de token

---

**01.**Acione o ícone **Configurações**no canto superior direito e selecione a opção **Segurança**. 

**02**. Acesse o recurso **Controle de Segurança de** **Token.**

**03**. Escolha a opção desejada.

#f2f2f2#f2f2f2

As opções de controle de segurança de token no Identity são: NONE (nenhum), LAX (relaxado) ou STRICT (rigoroso). Por padrão, o controle aplicado é LAX.

Quando a configuração for STRICT, o navegador não enviará o cookie em nenhuma requisição cross-site sob nenhuma hipótese. Quando for LAX, ele apenas não enviará o cookie em requisições inseguras (aquelas que usam o método POST, por exemplo), mas enviará o cookie nas demais requisições cross-site.

IMPORTANTE!

Se você utiliza a widget Analytics do TOTVS Fluig Plataforma, o Controle de Segurança de Token deve ser configurado como NONE.

]]>
