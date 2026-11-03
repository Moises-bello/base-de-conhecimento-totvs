---
content_hash: 62a47e5e542267563da12735dde75a555b1b5924fc468edd611b0bf54f3a0557
fetched_at: '2026-06-29T00:09:29.318235+00:00'
page_id: '423939451'
product: rm
source: tdn-rm
title: Ocorrência do Erro de Request Validation
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423939451
version: 2
---

# Índice:

---

.\*ndice:

# Objetivo

---

Explicação para uma possível ocorrência do erro de Request Validation.

# Descrição do Ocorrido

---

Ao salvar algumas informações em formato HTML não codificado no Portal RM, pode acontecer do registro não ser salvo e ser apresentada a seguinte mensagem de erro: “Um valor possivelmente perigoso Request.Form foi detectado no cliente (ctl....”.

# Motivo da Ocorrência

---

Esse erro ocorre, porque o portal ou a página do portal está configurada para realizar a validação de conteúdo, visando uma maior segurança de dados e evitando de scripts maliciosos sejam salvos.

# Solução

---

Uma forma de desabilitar essa validação é através do web.config. Basta alterar o valor de validateRequest para FALSE.

    <pages validateRequest="false" controlRenderingCompatibilityVersion="3.5" clientIDMode="AutoID" enableEventValidation="true"/>

Dessa forma os registros poderão ser salvos.

Para maiores informações e outras opções de validação consulta e link abaixo:

<https://docs.microsoft.com/en-us/aspnet/whitepapers/request-validation>

falsefalse

**Produto:** Framework

false

**Versão:** 11.80.XX e 12.01.XX

false

**Processo:** Ocorrência do Erro de Request Validation

falsefalse

**Status:** Finalizado

false

**Data:** 18/10/2018

false

**Autores:**

Guilherme Caram Meireles

Stella Gleyse Macedo Vilaca
