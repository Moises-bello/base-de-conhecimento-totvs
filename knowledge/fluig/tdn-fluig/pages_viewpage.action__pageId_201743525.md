---
content_hash: e81cb19bcac6c4349278b5688497c79f08e1a4ccc5ef7910ee80dfb79abb3033
fetched_at: '2026-06-28T21:35:19.347714+00:00'
page_id: '201743525'
product: fluig
source: tdn-fluig
title: BPM 009 - Como comparar variáveis de tipos "string" e "number" em eventos com
  maior e menor?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201743525
version: 7
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

**Versão:**Todas as versões

# Ocorrência

Constantemente há a necessidade de realizar a comparação entre variáveis, ou com valores fixos, principalmente nas condições de atividades automáticas.

# Causa

O JavaScript só reconhece como *number*valores com um único ponto de até 21 casas decimais, ou seja, valores de *string* com milhares como 1.000.02 não serão considerados *number*e falharão em todas as comparações com uma variável de tal tipo.

# Solução

Modificar a variável de comparação para se adequar ao formato necessário.

Abaixo, seguem exemplos de validações que podem ser utilizadas como condições para atividades automáticas:

js1Comparar um campos do formulário com um valor fixotrue= j;]]>js1Comparar dois campos do formuláriotrue= j;]]>
