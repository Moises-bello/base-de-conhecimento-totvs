---
content_hash: 173867004f746f709e517874c9bbb3eadfb666982a5e4c4ce34871dfa31172ff
fetched_at: '2026-06-28T21:35:17.070479+00:00'
page_id: '1022378406'
product: fluig
source: tdn-fluig
title: RequestInfoVO
type: documentation
url: https://tdn.totvs.com/display/fluig/RequestInfoVO
version: 4
---

# Descrição

---

Este é um objeto de entrada do método de validação de login. Foi implementado na atualização **Fluig 2.0.0-260224** e permite criar validações com os dados da requisição como IP, host, porta.

#f2f2f2#f2f2f2

Este objeto é um dos parâmetros de entrada do método .

# Atributos da instância

---

**String ip**

* Endereço IP real do cliente, considerando cabeçalhos de proxy (X-Forwarded-For).
* Este IP só é confiável quando o ambiente utiliza um **[Proxy reverso](https://tdn.totvs.com/x/nwVbDw)** configurado corretamente, com a funcionalidade de encaminhamento do IP original habilitada na requisição.

**String userAgent**

* Valor enviado pelo navegador contendo detalhes sobre sistema operacional, navegador e dispositivo.

**String method**

* O método HTTP utilizado na requisição (GET, POST, PUT, DELETE…).

**String requestURI**

* Parte do caminho solicitado pelo cliente dentro da aplicação.
* Ex: /portal/login/auth.

**String queryString**

* Parâmetros enviados na URL quando o método é GET.
* Ex: user=jose&id=10.

**String host**

* Valor do cabeçalho Host, normalmente o domínio acessado.
* Ex: fluig.minhaempresa.com ou localhost:8080.

**String protocol**

* Protocolo e versão usados na requisição.
* Ex: HTTP/1.1 ou HTTP/2.

**String referer**

* URL da página anterior de onde o usuário veio (caso o navegador envie). Útil para entender fluxo de navegação e identificar redirecionamentos externos.

 

# Exemplos de uso

---

**Impressão dos dados da requisição:**

jstrue

**Saída:**

jstrue
