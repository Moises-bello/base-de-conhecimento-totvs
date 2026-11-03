---
content_hash: 5d0cf3bd63e4902b0c4208ab608e226488a10f80d79669f248ad0ae841cdf6b1
fetched_at: '2026-06-28T21:35:19.837397+00:00'
page_id: '223929070'
product: fluig
source: tdn-fluig
title: MOB - Por que formulários que acessam datasets no mobile estão trazendo valores
  nulos?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223929070
version: 14
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**Fluig Mobile

# Ocorrência

O campo de um formulário que acessa um dataset traz apenas valores nulos, mas via web funciona normalmente.

# Causa

Se o seu formulário possui uma estrutura de arquivos semelhante a essa:   
- SEU\_FORMULÁRIO.html;   
- SEU\_FORMULARIO\_ecmmobile.html;   
  
Abra o segundo arquivo e verifique se o código HTML do campo que está apresentando problemas é semelhante ao código abaixo:

xmlSEU\_FORMULARIO\_ecmmobile.html

LABEL DO CAMPO

null
null

null
null
]]>

# Solução

Converta o formulário para a nova versão - que utiliza o novo [Style Guide](https://style.fluig.com/) - onde apenas um código serve tanto para o navegador web quanto para o app mobile. Siga os passos abaixo:

1) Tenha certeza de que você está utilizando a versão mais recente do Fluig Studio (que seja compatível com seu Fluig server);

2) Crie um novo formulário;

3) Copie todos os arquivos do seu formulário anterior para o novo, com exceção do(s) arquivos .html. Veremos esse(s) a seguir;

4) Sobre o arquivo SEU\_FORMULARIO.html:

* Abra o fonte de seu formulário antigo e copie o conteúdo da tag:

xml

]]>

* Abra o fonte de seu novo formulário e cole o conteúdo copiado dentro da tag:

xml

]]>Importante

Não copie a tag "<form>", apenas o conteúdo dela

5) Sobre o arquivo SEU\_FORMULARIO\_ecmmobile.html:

* Ignore-o e não o copie para a nova estrutura;

6) Ao exportar novamente o formulário para o Fluig, não o faça como novo formulário. Escolha o nome do antigo, como se fosse gerar apenas uma nova versão dele

# Observações

Provavelmente será necessário remodelar a parte visual do formulário. Facilitadores podem ser encontrados em [https://style.fluig.com](https://style.fluig.com/)
