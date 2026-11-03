---
content_hash: 0e0df6adae9ad08207bed9983d78fdc395f675a9307bd575c114f9fb7e16fce3
fetched_at: '2026-06-29T00:05:59.011752+00:00'
page_id: '189307114'
product: rm
source: tdn-rm
title: PlanRMWorkbook - Protect
type: documentation
url: https://tdn.totvs.com/display/LRM/PlanRMWorkbook+-+Protect
version: 2
---

Protect(string password)

## Descrição

---

Habilita a proteção da planilha com uma senha.

## Parâmetros

---

**password** - Senha utilizada para proteger a planilha.

## Exemplo

---

Protegendo uma planilhatruec#1Protect(string codUsuario, string password)

## Descrição

---

Habilita a proteção da planilha com uma senha e com o código do usuário. Se a planilha for aberta pelo usuário informado no parâmetro, a senha não será solicitada.  

## Parâmetros

---

**codUsuario** - Código do usuário.

**password** - Senha utilizada para proteger a planilha.

## Exemplo

---

Protegendo uma planilhatruec#1Protect(string codUsuario, string password, bool useInternalPassword)

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

Protegendo uma planilhatruec#1Protect(string codUsuario, string password, bool useInternalPassword, bool protectStructure, bool protectWindows)

## Descrição

---

Habilita a proteção da planilha com uma senha e com o código do usuário. Se a planilha for aberta pelo usuário informado no parâmetro, a senha não será solicitada. Se a senha interna for utilizada, a senha informada pelo usuário não será a mesma que protegerá o conteúdo da planilha.  

## Parâmetros

---

**codUsuario** - Código do usuário.

**password** - Senha utilizada para proteger a planilha.

**useInternalPassword** - Define que a senha interna será utilizada para proteger a planilha.

**protectStructure** -Define que só o conteúdo da planilha será protegido.

**protectWindows** - Define que só a estrutura da planilha será protegida.

## Exemplo

---

Protegendo uma planilhatruec#1Para maiores informações:

****[@FRAMEWORK](http://fluig.totvs.com/portal/p/10097/subject/rframework)****

**Canais de Atendimento**

**Chamado:** Através do Portal TOTVS - [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2-2-3-9-5 (Framework) ou 2-2-3-9-4 (BI)
