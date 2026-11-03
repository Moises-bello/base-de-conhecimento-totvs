---
content_hash: 2dfdfea824634afd2e83f1117f67d9c691e33fc1107de3bfae645d3d77e9a341
fetched_at: '2026-06-29T00:09:31.785805+00:00'
page_id: '425458721'
product: rm
source: tdn-rm
title: Gerar plano de aula
type: documentation
url: https://tdn.totvs.com/display/LRM/Gerar+plano+de+aula
version: 26
---

Plano de aula é o cronograma de aula da turma/disciplina com conteúdos previstos e realizados, lição de casa, entre outras informações. Para que a geração aconteça com sucesso, a turma/disciplina já deve ter os seus horários cadastrados, pois o plano de aula é gerado para cada aula da turma/disciplina. A geração do plano de aula pode ser feita para todo o período de datas definido na turma/disciplina, no período letivo, ou então para um intervalo de datas específicas.  Para consultar o plano de aula gerado, acesse **Anexos | Plano de aula**, disponível em Turmas/Disciplinas.

Os planos de aula serão gerados conforme a seleção de opções disponíveis na tela do processo.

Definir o período de geração do plano de aula

As datas de início e fim consideradas para a geração do intervalo de plano de aula, seguem o critério conforme a seleção da opção desejada. Ao **menos uma das opções** entre, data de início e data final, deve ser escolhida.

Prioridade na seleção das datas

Caso a opção de datas de início e final da Turma/disciplina ou Período letivo **esteja marcada**, as datas preenchidas nos respectivos cadastros irão **sobrepor** as datas personalizadas informadas pelo usuário.

Data personalizada pelo usuário

Ao selecionar esta opção, o sistema irá gerar os planos de aula dentro do intervalo definido pelo usuário.

Data da turma/disciplina

Ao selecionar esta opção, o sistema irá gerar os planos de aula dentro do intervalo definido no cadastro da turma/disciplina.

Validar a data do plano de aula dentro do intervalo do período letivo

Ao selecionar esta opção, o sistema irá gerar os planos de aula dentro do intervalo defino no cadastro do período letivo.

Data final

O sistema irá considera a "**Data de término**" se **preenchida** ou a "**Previsão de término**" cadastrada.

Regerar plano(s) de aula(s) existente(s)

O processo de Regerar plano(s) de aula(s) existente(s) tem como objetivo, regerar os plano(s) de aula(s) para que a Instituição possa realizar alguma manutenção, e consiste na exclusão dos planos existentes no período, seguido da geração de novos planos de aula. **Saiba mais em .**

Gerar plano(s) de aula(s) com data inicial menor que o plano(s) de aula(s) existente(s) e reordenar o número da aula.

O processo de '**Gerar plano(s) de aula(s) com data inicial menor que o plano(s) de aula(s) existente(s) e reordenar o número da aula**' tem como objetivo, gerar os plano(s) de aula(s) para um período menos que os plano(s) de aula(s) existente(s) e em seguida reordenar o número da aula para que fique na ordem correta.

***Exemplo:***

A instituição gerou os planos de aula nos meses de março, abril, maio, entre outros, mas esqueceu de gerar os planos referentes ao mês de fevereiro.

Nesse caso, o sistema irá gerar automaticamente os planos de aula para fevereiro e reordenar a numeração das aulas conforme a nova sequência cronológica

Não verificar data de validade do período letivo

As datas para a geração devem estar sempre dentro da validade do período letivo, mas se for necessário gerar um plano de aula fora desta validade, basta **marcar a opção** "Não verificar data de validade do período letivo".

Utilizar a carga horária da disciplina

Podemos utilizar a carga horária da disciplina como horas através do parâmetro: **Configurações | Parâmetros | Secretaria | Geral 2/7 | Considerar a carga horária da disciplina como horas**

Caso utilize o parâmetro anterior junto com "**Não ultrapassar carga horária da disciplina**" do processo, o sistema validará a duração da aula em minutos com a carga horária da disciplina em horas.

Validar a data do plano de aula em feriados ou eventos acadêmicos específicos

Para que **não sejam gerados** planos de aulas para datas ocorridas em **feriados** ou **eventos acadêmicos específicos**, no momento da geração marque o tipo de feriado e/ou de eventos acadêmicos específicos para os quais não desejam gerar plano de aula nas respectivas datas.

Feriados

Na geração do plano de aula, o calendário é procurado primeiro no cadastro de parametrização por curso, caso **não encontre o campo preenchido**, será considerado o calendário no cadastro do período letivo.

Eventos acadêmicos específicos
