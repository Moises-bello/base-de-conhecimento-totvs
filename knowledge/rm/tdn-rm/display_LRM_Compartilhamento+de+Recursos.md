---
content_hash: e9bc93e8f0bffe170b2fad45eadc58f63e65420afe64a871eb1e23e84df5f5c3
fetched_at: '2026-06-29T00:11:32.931279+00:00'
page_id: '751245782'
product: rm
source: tdn-rm
title: Compartilhamento de Recursos
type: documentation
url: https://tdn.totvs.com/display/LRM/Compartilhamento+de+Recursos
version: 5
---

# Introdução:

---

 Durante o fluxo de uso de um recurso Smart View, vem a ser necessário o gerenciamento dos níveis de permissões dos usuários que acessarão os recursos. Nesta documentação você encontrará uma explicação detalhada sobre como gerenciar o acesso ao seus recursos.

# Níveis de Acesso

---

O Smart View trabalha por meio de dois níveis de acesso aos seus recursos e cada grupo de usuários:

* **Leitor:** Pode apenas ler e exportar o recurso
* **Editor:** Possui plenos acessos de uso ao recurso

# As Categorias

---

Já no RM, o acesso à um recurso se dá por meio de uma categoria atrelada à ele. E esta categoria por vez irá conter todos os perfis que deverão possuir acesso àquele recurso. Deste modo, é possível, com apenas uma categoria, possibilitar que diferentes grupos de usuários tenham diferentes níveis de acesso no Smart View:

Sempre que houver uma alteração no recurso mapeado no RM referente à categoria deste, a sincronização dos perfis atrelados à categoria serão atualizadas automaticamente no Smart View, mantendo o ERP e o Smart View no mesmo nível de compartilhamento!

Não é recomendado, em hipótese alguma, realizar o compartilhamento de um recurso diretamente pelo Smart View e a tentativa de realizar essa ação ocasionará em problemas nas permissões do recurso dentro do RM.

# Compartilhando um recurso

---

Conforme dito anteriormente, para compartilhar um recurso, é necessário criar e atrelar uma categoria ao mapeamento do recurso no RM, conforme descrito abaixo e na página:

TOTVS Compartilhamento

O gerenciamento de acesso de um recurso que foi importado por meio do **TOTVS Compartilhamento** segue a mesma estrutura de qualquer recurso (Demonstrado logo abaixo) porém, por ser um recurso padrão TOTVS, *este sempre será compartilhado apenas com a permissão de leitor tanto no RM quanto no Smart View.*

Lembre-se que o acesso à um recurso Smart View é diferente do acesso ao Objeto de Negócio que está sendo utilizado no recurso. Compartilhar um recurso com um grupo de usuários que não possui acesso ao Objeto de Negócio daquele recurso ocasionará na não execução daquele recurso por estes usuários.

Todo recurso que não possuir uma categoria atrelada só estará disponível para o usuário que o mapeou/criou

Índicefalsefalse

**Produto:** Framework

false

**Versão:** 12.1.2302

false

**Processo:** Integração com o

falsefalseStatus

YellowEM DESENVOLVIMENTO

falseAutores
