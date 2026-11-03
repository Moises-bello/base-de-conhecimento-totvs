---
content_hash: 94a1e9ba3eefa06913356f8797f5d3fb5195fb095d4951a5f4914bab2d0d2cf6
fetched_at: '2026-06-29T00:05:59.023615+00:00'
page_id: '189307132'
product: rm
source: tdn-rm
title: PlanRMWorkbook - SaveAs
type: documentation
url: https://tdn.totvs.com/display/LRM/PlanRMWorkbook+-+SaveAs
version: 2
---

SaveAs(string filename)

## Descrição

---

Salva a planilha associada ao objeto em um arquivo.  

## Parâmetros

---

**password** - Senha utilizada para proteger a planilha.

## Exemplo

---

Protegendo uma planilhatruec#1SaveAs(string filename, bool overwrite)

## Descrição

---

Habilita a proteção da planilha com uma senha e com o código do usuário. Se a planilha for aberta pelo usuário informado no parâmetro, a senha não será solicitada.  

## Parâmetros

---

**codUsuario** - Código do usuário.

**password** - Senha utilizada para proteger a planilha.

## Exemplo

---

Protegendo uma planilhatruec#1SaveAs(string filename, bool overwrite, PlanRMFileFormat format)

## Descrição

---

Habilita a proteção da planilha com uma senha e com o código do usuário. Se a planilha for aberta pelo usuário informado no parâmetro, a senha não será solicitada. Se a senha interna for utilizada, a senha informada pelo usuário não será a mesma que protegerá o conteúdo da planilha.  

## Parâmetros

---

**codUsuario** - Código do usuário.

**password** - Senha utilizada para proteger a planilha.

**useInternalPassword** - Define que a senha interna será utilizada para proteger a planilha.

## Exemplo

---

Protegendo uma planilhatruec#1Para maiores informações:

****[@FRAMEWORK](http://fluig.totvs.com/portal/p/10097/subject/rframework)****

**Canais de Atendimento**

**Chamado:** Através do Portal TOTVS - [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2-2-3-9-5 (Framework) ou 2-2-3-9-4 (BI)
