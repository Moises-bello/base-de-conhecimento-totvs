---
content_hash: 50ab408fe03f63806803214e266372722959eaee8a09fcfda8e53a80b6413ae0
fetched_at: '2026-06-29T00:11:44.309227+00:00'
page_id: '814524957'
product: rm
source: tdn-rm
title: Ficha medica flexível
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=814524957
version: 18
---

Disponível a partir da versão 12.1.2402

Essa aba permitirá o preenchimento do formulário da . Para que fique visível no portal é necessário dar permissão no perfil do aluno em globais:

 **Educacional | Educacional(Portal) | Acadêmico | Ficha médica**

Dada a permissão para o aluno, a aba já ficará disponível para o preenchimento dos dados da ficha médica.

Caso o portal do aluno não consiga estabelecer comunicação com o Portal Gestão Educacional, será mostrada a tela abaixo:

É importante ressaltar que a **ficha médica flexível**disponibilizada no portal do aluno é a mesma ficha médica que é disponibilizada no **Portal Gestão Educacional (PGE)**, portanto neste caso, há integração entre os dois portais de forma transparente, sendo necessário que ambos portais estejam instalados dentro da pasta **FRAMEHTML**. 

Internamente o portal do aluno reconhece o **Portal Gestão Educacional (PGE)**da seguinte forma: [http://{dominio}/PortalGestaoEducacional](http://localhost/FRAMEHTML).

Caso seja necessário customizar a parte em destaque de vermelho na URL a seguir  [http://{dominio}**/PortalGestaoEducaciona**](http://localhost/FRAMEHTML)l, será necessário adicionar no arquivo **totvs-app.global.config.js**da pasta FrameHTML/Web/js  a TAG "**CONST\_GLOBAL\_URL\_PGE** " com o novo caminho.

Exemplo:

**CONST\_GLOBAL\_URL\_PGE = "/portais/portalgestaoeducacional"**

Caso o portal do aluno e o portal gestão educacional não estejam hospedados no mesmo domínio a aba de ficha médica não estará disponível.
