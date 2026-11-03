---
content_hash: 0b290c85478c9fa27a7624138e9374b7e268b83d03d8571f763d7f98ec0d512c
fetched_at: '2026-06-29T00:11:16.203952+00:00'
page_id: '665027538'
product: rm
source: tdn-rm
title: Configuração da Tag EnableContentSecurityPolicy
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=665027538
version: 3
---

# Índice:

---

# Objetivo:

---

Tem como objetivo descrever como configurar e aumentar a segurança para prevenção de ataques com injeção de código, XSS.

Ao adicionar um valor a Tag EnableContentSecurityPolicy as requisições passam a acrescentar no cabeçalho de resposta de cada requisição.

# Configuração:

---

Adicionar a Tag nos arquivos "RM.Host.exe.config", "RM.host.Service.exe.config" dos servidores.

**Exemplo:** <add key=“EnableContentSecurityPolicy” value=“default-src 'self'; style-src 'unsafe-inline';” />

Para desativar, basta deixar o conteúdo do valor vazio ou remover a Tag do arquivo.

# Diretivas de segurança CSP:

---

As inúmeras configurações que podem ser adicionadas no valor da Tag, seguem o padrão CSP, <https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP>

Podem ser encontradas aqui, <https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Headers/Content-Security-Policy>

Segue abaixo um pequeno resumo como exemplo:

**default-src:** É a diretiva padrão, que serve de base para todas as outras.

exe: default-src 'self'; Aceita apenas conteúdos da mesma origem da url do site.

**script-src:** Se refere aos scripts(javascript) e como eles poderão ser carregados.

exe: script-src 'unsafe-hashes'; Aceita apenas manipuladores de eventos e bloqueia tag <script> ou elementos com código embutido/inline.

**style-src:** Refere-se aos estilos e como poderão ser carregados.

exe: style-src 'unsafe-inline'; Permite usar o estilo embutido/inline nos elementos. \*(Porém é considerado inseguro)
