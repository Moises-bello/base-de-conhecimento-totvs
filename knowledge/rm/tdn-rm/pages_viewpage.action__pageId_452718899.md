---
content_hash: 42b8edb03f4694fbd442fe4dc748ee98a29a543057bb133a6028818a38d3c28d
fetched_at: '2026-06-29T00:10:02.419711+00:00'
page_id: '452718899'
product: rm
source: tdn-rm
title: Associação PCMSO x PPRA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718899
version: 2
---

**Associação PCMSO x PPRA**

Este cadastro tem como objetivo associar Perfis de Exame a:

* Riscos
* Níveis de Risco
* Avaliação de Risco
* Pessoas

Desta forma é possível gerar os exames que os funcionários necessitam conforme exposição ao risco.

**Observações:**

- Obrigatório escolher um tipo de vínculo.

- Escolhendo "Risco" é obrigatório informar o campo Risco.

- Escolhendo "Nível de Risco" é obrigatório informar os campos Risco e Nível de Risco.

- Escolhendo "Avaliação de Risco" é obrigatório informar os campos Risco e Avaliação de Risco.

- Escolhendo "Pessoas" é obrigatório informar o campo Pessoa.

- Obrigatório preencher o campo "Perfil de Exame".

- O tipo de vínculo só pode ser alterado na inclusão de novos registros.

- Não deve ser permitido vincular um mesmo Perfil de Exame mais de uma vez para um item.

- Quando for incluído um Perfil de Exame que tenha um exame do tipo "Mudança de Função", será emitido um alerta informando ao usuário que na próxima execução da geração de exames pendentes, todos os funcionários expostos àquele perfil terão a pendência gerada.

Para a correta geração de exames a partir da Associação PCMSO x PPRA é necessário seguir as seguintes regras:

* Tem que ter uma avaliação para o item de risco referente ao exame cadastrado em 'Reconhecimento e Avaliação de Risco'.
* Se o perfil de exame é associado ao Risco o mesmo não pode ter preenchido o cód. do nível de risco na avaliação.
* Se o perfil de exame é associado ao Nível de Risco o mesmo tem que ser preenchido no risco na avaliação
