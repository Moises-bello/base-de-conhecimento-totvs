---
content_hash: e920e23f93ccfd0e433b92424bffe68d0cbb9440db3a3fc4ef7fa80ad0ac8143
fetched_at: '2026-06-29T00:11:36.012021+00:00'
page_id: '770944329'
product: rm
source: tdn-rm
title: Agrupar demanda
type: documentation
url: https://tdn.totvs.com/display/LRM/Agrupar+demanda
version: 8
---

Permite realizar o agrupamento de demandas, flexibilizando a futura geração de turmas/disciplinas de acordo com a necessidade da instituição.

Para realizar o agrupamento de demanda, é necessário selecionar dois ou mais registros da tabela de resultados:

No exemplo acima, a disciplina de 'Algorítmos e Técnicas de Programação I', dos três cursos, está abaixo do esperado para a demanda, logo a instituição pode optar por agrupar as três demandas, criando apenas uma turma no momento da geração da oferta, conforme abaixo:

É necessário selecionar qual será a turma AGRUPADORA, ou seja, qual turma receberá a demanda das outras turmas, e que será utilizada na geração da oferta.

Após selecionar a turma AGRUPADORA, e clicar em agrupar, o resultado será o seguinte:

É possível identificar, na tabela de resultados, através dos ícones e do tooltip (dica ao passar o mouse), a turma AGRUPADORA (que agrega a demanda das demais turmas) e as turmas AGRUPADAS (que cedem a demanda para a turma agrupadora).

Clicando na seta para baixo, ao lado do ícone de status, é possível verificar a rastreabilidade, ou seja, é possível ver na turma AGRUPADORA, quais são suas turmas agrupadas e, nas turmas AGRUPADAS, é possível ver quem é sua turma agrupadora.

Ao realizar o agrupamento, apenas a demanda da turma AGRUPADORA é alterada, para somar as demandas das turmas AGRUPADAS com a sua própria demanda.

Caso uma turma esteja com o ícone de AGRUPADA, não será possível realizar outra operação de agrupamento com a mesma.

É permitido incluir novas turmas AGRUPADAS dentro de uma AGRUPADORA, para isso, selecione na tabela de resultados, a turma identificada como AGRUPADORA, em seguida selecione uma ou mais turmas que não possuam identificação de AGRUPADAS. Nesse caso, será identificado a turma AGRUPADORA e as demais serão automaticamente incluídas como AGRUPADAS.

É importante destacar que apenas a turma **AGRUPADORA** terá oferta gerada; as turmas AGRUPADAS, por outro lado, não terão oferta gerada.
