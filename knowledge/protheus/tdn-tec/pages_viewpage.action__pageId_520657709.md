---
content_hash: 61e96cb21cfda1ed5e174c8a9673d869f6a478e3b4c1c189108310c53b637b9a
fetched_at: '2026-07-02T19:24:26.071280+00:00'
page_id: '520657709'
product: protheus
source: tdn-tec
title: DBAccess - Seção [Environment], chave Codepage
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520657709
version: 1
---

Codepage

Permite configurar o *Codepage* a ser utilizado na conexão entre o  true com o SGBD.

---

## Valores válidos

| SGBD | Codepage |
| --- | --- |
| Oracle | WE8MSWIN1252 |
| PostgreSQL | WIN1252 |

---

## Observações

* A chave é específica para os SGBDs **Oracle** e **PostgreSQL**, não influenciando os demais SGBDs.
* Especificar a chave na seção [ORACLE] ou [POSTGRES] tem efeito sobre o valor default de todos os ambientes configurados para estes SGBDs.
* Caso seja especificada dentro de uma seção de uma conexão específica - [ORACLE/ambiente], por exemplo - esta configuração será considerada sobre o default, para todas as conexões com esse ambiente.

---

## Exemplo

textfalse
