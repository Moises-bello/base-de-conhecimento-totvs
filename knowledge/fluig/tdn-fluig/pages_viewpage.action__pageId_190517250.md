---
content_hash: 0093fea3f483cf3155490c43737c1d561c9e8735267183ac50359c34803cc0a2
fetched_at: '2026-06-28T21:35:19.100740+00:00'
page_id: '190517250'
product: fluig
source: tdn-fluig
title: DES - Utilização de mask em campo de formulário com pai e filho
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=190517250
version: 7
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

# Ocorrência

A propriedade 'mask' não funciona para campos pai e filho nos formulários.

# Causa

Isto acontece porque a forma que são tratados estes campos é um pouco diferente, eles são adicionados conforme necessidade no formulário, não são fixos como os outros. Como a execução dos campos filhos ocorre antes que estes campos apareçam no formulário, não são atribuídas as máscaras.

# Solução

Para funcionar deve-se criar uma função, uma sugestão é utilizar as funções JQuery para pegar os campos de uma coluna inteira da tabela do pai e filho e atribuir a máscara que precisar nos campos.  
Outra forma de solucionar o problema é adicionar as propriedades 'mask' no campo pai e filho normalmente e recarregar o evento 'mask', para atribuir nos campos filhos, conforme exemplo abaixo:

js
]]>

# Observações

É necessário ter conhecimento de Javascript básico ou JQuery para fazer este procedimento.   
Para mais detalhes sobre o 'mask' e desenvolvimento de pai e filho, favor consultar a documentação de .
