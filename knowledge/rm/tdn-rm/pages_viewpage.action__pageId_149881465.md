---
content_hash: a0784c0575e129ec4b2de8880fc175f28bb6e7ef78df01355a98ed64e025404e
fetched_at: '2026-06-29T00:05:56.296608+00:00'
page_id: '149881465'
product: rm
source: tdn-rm
title: Utilizando a atividade "Executar sequência conforme o estado de registro"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=149881465
version: 6
---

# Executar sequência conforme o estado de registro:

---

Permite que o usuário consiga executar uma sequencia de atividades conforme o estado do registro.

A atividade leva em consideração o Estado (DataRowState) do Registro (DataRow), para escolher qual sequência será executada.

Portanto é importante avaliar quais os gatilhos podem ser usados e como estará o estado do registro no momento do gatilho.

* Ao utilizar o gatilho "Após Salvar o Registro", o dado ainda não estará efetivado no banco de dados. No entanto, o registro não conterá informações de estado (DataRowState), ou seja, não passará pela sequência esperada.
* Ao utilizar o gatilho "Após a Atualização do Registro (Fim)", o dado já estará no banco de dados. No entanto, o registro não conterá informações de estado (DataRowState), ou seja, não passará pela sequência esperada.
* Ao utilizar o gatilho "Antes de Salvar o Registro", a validação é realizada no estado original do registro, antes de ser persistido e perder a referencia de estado (DataRowState), ou seja, passará pela sequência esperada.
  + OBS: No contexto de FV atribuida a Campos Complementares, a mudança de estado (DataRowState) referente ao DataMember informado é realizada em outro momento e não juntamente com a mudança de estado (DataRowState) da tabela principal executada por este gatilho.
    - Pra estes cenários, existe a possibilidade de manipular a sequencia utilizando uma atividade de código fonte (source code) da FV.

# Exemplo de uso:

---

Uso de uma atividade de Sequência de estado, gerando uma expressão para cada estado e mostrando numa atividade de Exceção:

Ao tentar incluir um novo registro, a mensagem customizada é mostrada:

Ao tentar editar um registro já existente, a mensagem customizada é mostrada:
