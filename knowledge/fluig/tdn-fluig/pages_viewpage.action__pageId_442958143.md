---
content_hash: d7da099d9eefbdcbc6db41be9b32c5776baa298215f9c93e6fad5780cf1f9ec4
fetched_at: '2026-06-28T21:35:26.922478+00:00'
page_id: '442958143'
product: fluig
source: tdn-fluig
title: BPM 099 - Central de tarefas não apresenta solicitações do gestor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=442958143
version: 3
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

# Ocorrência

Após alterar o gestor da solicitação para o mecanismo **Por campo de formulário**, **Por executor de atividade** ou **Mecanismos customizados** (gerados através do Studio), algumas solicitações não ficam disponíveis para visualização na central de tarefas e na consulta de solicitações.

Confira a solução a seguir para entender melhor.

# Solução

O gestor do fluig é normalmente configurado por processo. Porém, existem situações onde se deseja configurar o gestor por solicitação e a única forma possível era através do mecanismo customizado, o que gerava muita lentidão na consulta, já que era necessário carregar solicitação por solicitação.

A solução se deu com a implementação do cache, que consiste basicamente em criar um cache dessa informação que será utilizada em consultas e na Central de tarefas, o qual será alimentado sempre que a solicitação for salva.

Sempre que editar as propriedades de um processo e alterar o Gestor, o cache atual será limpo e um novo cache de atualização será criado no Agendador de tarefas. Com isso, as atualizações serão aplicadas em blocos de forma que não sobrecarregue o servidor. Assim, em pouquíssimo tempo a central de tarefas e a consulta de solicitações serão atualizadas.

Então, se elas ainda não estão sendo exibidas, é porque o cache deve estar sendo gerado.

Fique por dentro!

Para conhecer mais sobre os mecanismos de atribuição que utilizam o cache, acesse nossa documentação de [Configuração do processo](http://tdn.totvs.com/x/mga5Dw) no nosso manual do usuário.
