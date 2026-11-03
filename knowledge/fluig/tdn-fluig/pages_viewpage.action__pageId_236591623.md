---
content_hash: 0f18f5b56479ad7c7ca607d36d62545194459f781cb85b1789dbc4652c08d814
fetched_at: '2026-06-28T21:35:22.474245+00:00'
page_id: '236591623'
product: fluig
source: tdn-fluig
title: FORM 001 - Por que campo do formulário vem preenchido com nome do usuário logado,
  ao invés da matrícula?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=236591623
version: 13
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** fluig

**Versão:** 1.6.1 e anteriores

# Ocorrência

Criamos um formulário no editor web do fluig que foi configurado para ser inicializado com o usuário logado, conforme a imagem abaixo, mas quando o formulário é aberto, o campo em questão é preenchido com a matrícula do usuário e não o nome.

# Solução

A regra de formulário Usuário Logado retornará apenas matrícula do usuário logado; atualmente o editor de processos web do fluig não possuí uma regra para retornar o nome do usuário logado.

Contudo, o fluig permite que seja desenvolvida uma rotina para preencher o nome do usuário em um campo do formulário. Uma maneira de fazer isto é utilizar o evento de formulário [displayFields](http://tdn.totvs.com/pages/viewpage.action?pageId=75270483#DesenvolvimentodeFormulários-DisplayFields).

Primeiramente execute o método **getValue("WKUser")** para saber o código do usuário logado. Em seguida, consulte o dataset **colleague** passando como parâmetro o código obtido no passo anterior. No retorno do dataset, você deverá pegar apenas o valor do campo **colleagueName**.

Logo abaixo segue um simples exemplo ilustrando os passos descritos acima:

jstrue

O trecho de código acima representa apenas uma das maneiras de obter o resultado desejado, por se tratar de um desenvolvimento sobre a plataforma, você poderá programar da maneira que achar melhor.

Para mais informações, disponibilizamos uma documentação completa para [desenvolvimento de formulários](http://tdn.totvs.com/x/U4l8B)
