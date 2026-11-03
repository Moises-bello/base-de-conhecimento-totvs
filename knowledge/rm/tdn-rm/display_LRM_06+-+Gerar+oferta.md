---
content_hash: 98fd513c76f374c9fbde81ef504dfbf84e0bb45bab5ffa88d257aa93d2046b48
fetched_at: '2026-06-29T00:11:28.460933+00:00'
page_id: '731215232'
product: rm
source: tdn-rm
title: 06 - Gerar oferta
type: documentation
url: https://tdn.totvs.com/display/LRM/06+-+Gerar+oferta
version: 19
---

## Visão geral

Este passo é responsável por gerar a oferta e acompanhar a geração de cada curso. Esta geração da oferta consiste em basicamente criar a parametrização por curso, turma e turma/disciplina do período letivo planejado. O processo de fato irá gerar a oferta oficial.

**OBS**. Ao tentar processar novamente um idhabilitacaofilial que já tenha oferta gerada, será emitido validação.

## Funcionamento dos filtros

Os filtros **curso**, **habilitação**, **matriz**e **turno**funcionam da mesma forma que no passo [executar demanda](https://tdn.totvs.com/display/LRM/01+-+Executar+demanda), para mais informações acesse: [funcionamento dos filtros](https://tdn.totvs.com/display/LRM/01+-+Executar+demanda#id-01Executardemanda-Funcionamentodosfiltros).

## Grid dos cursos

Pós seleção dos filtros, basta clicar no botão **adicionar**. Ele irá popular a grid de acordo com o filtro selecionado. Toda vez que se clica no botão adicionar os cursos são adicionados da grid sempre no topo dela, porém, jamais irá repetir o mesmo curso, habilitação, matriz e turno.

A grid é composta pelas colunas de curso, habilitação, matriz e turno, colunas de identificação, e pelas colunas status, data de início, data de término e usuário, colunas responsáveis pela processamento da geração da oferta daquele curso.

Por fim temos três botões pós a grid, **limpar**, **atualizar** e **processar**. O botão **limpar**, tem finalidade de limpar toda a grid. O **atualizar** efetua uma atualização nos dados que estão presente na grid, ou seja, faz uma chamada ao servidor com os dados que estão na grid e traz atualizações dos dados caso exista. Vale frisar que esta grid não se atualiza automaticamente a cada processamento, é necessário clicar no botão **atualizar** ou se clicar no botão **adicionar** para adicionar outro curso, será feito a adição do novo curso e a grid será atualizada. Por último o botão **processar** tem função de processar a geração da oferta de um ou mais cursos, somente é possível processar algo se tiver marcado alguma linha na grid, mais informações do botão processar está descrito logo abaixo.

## Processar Geração da Oferta

Disparada ao clicar no botão **processar** irá criar um job para cada curso marcado na grid. Se o curso selecionado estiver com o status de **geração oferta aguardando processamento** ou**geração oferta em processamento** não será feita o processamento deste curso. Para os demais status será feito o processamento, entretanto vale ressaltar que cursos com status **demanda não processada**, **demanda aguardando processamento**, **demanda em processamento** eles não irão aparecer na grid para seleção. O job tem o objetivo de gerar as seguintes entidades **parametrização por curso (1)**, **turma (2)**, **turma/disciplina (3)**, **horário (4)**,**professor (5)** e **professor do horário (6)**, sendo que as entidades 1, 2 e 3 são criadas a partir dos passos  e , já as entidades 4, 5 e 6 são criadas a partir do passo .

Outro ponto importante é que para os status **geração oferta processada** e **geração oferta processada com erro** é permitido o processamento, entretanto nada será sobreposto, ou seja, se já tiver sido criado uma das entidades mencionadas anteriormente o processo irá pular ela, não alterando em nada o que já existe. Caso a turma/disciplina não exista, mas a turma sim, o processo irá adicionar esta turma/disciplina na turma em questão, além disso, não será gravado nenhum histórico de processamento anteriores.

Importante ressaltar que se a demanda não tiver turma criada conforme exemplo abaixo, nem a turma e nem a turma/disciplina será gerada a oferta.

**Observação!**

Ao realizar a geração inicial da oferta, e no Totvs Educacional já estiver com essas turmas criadas, a verificação é realizada através do código da turma. Ao finalizar a geração o sistema não atualiza ou regera as informações (como turma, turma/disciplina, horário e professor) destas turmas.

É exibido no log as informações que a turma já existe e não será atualizada.

**Geração de oferta de Turma disciplina Gerencial e gerenciada**

Ao gerar oferta para um curso que tenha turma gerencial e gerenciada é criada a parametrização por curso, turmas e turmas/disciplinas da respectiva matriz aplicada. É feita a associação das turmas/disciplinas gerenciais e gerenciadas caso as turmas/disciplinas gerencial e gerenciada tenham o mesmo tipo de turma e mesma data de início e fim. Caso contrário, a associação gerencial/gerenciada não será feita e o sistema registrará no log de execução do job a causa da não associação.

Caso a turma gerenciada pertença a outra matriz aplicada ou a uma turma livre, o sistema irá executar a criação da parametrização por curso (no caso de turma de matriz aplicada), criação de turma e turma/disciplina da matriz aplicada ou da turma livre à qual a turma gerenciada pertence, mas somente a turma e turma/disciplina referente à essa turma/disciplina gerenciada. 

Ao gerar oferta para turma disciplina que contém [subturma](https://tdn.totvs.com/display/LRM/Adicionar+Subturmas) cadastrada, as mesmas são replicadas para o sistema.

Ao gerar oferta para turmas/disciplinas que possuem [subturma](https://tdn.totvs.com/display/LRM/Adicionar+Subturmas), com horários e professores , a subturma é cadastrada no sistema com seus horários e professores alocados. 

Inclusão dos campos complementares na turma disciplina, conforme as informações definidas no Planejamento de Oferta.

O Sistema sincroniza os campos complementares entre o TOTVS Educacional e o Planejamento de Ofertas (PGE) disponíveis para o nível de ensino.

Apenas campos complementares ativos vinculados às turmas/disciplinas do nível de ensino em questão estão disponíveis.

Aviso

Caso o seguinte aviso seja exibido no log da geração de oferta, o cadastro do respectivo campo complementar apontado no log deve ser editado e salvo no TOTVS Educacional para que o campo complementar fique disponível para uso da turma do Planejamento de Ofertas.

Observação: É possível realizar a geração de oferta para turmas/disciplinas e subturmas que possuam alocação de [horários modulares](https://tdn.totvs.com/pages/viewpage.action?pageId=731215136#id-04Alocarhor%C3%A1rio/professor-Gera%C3%A7%C3%A3odaofertadohor%C3%A1riomodular) em seus respectivos cadastros.

Para garantir que os processos de geração e regeração de ofertas realizados pelo Planejamento de Ofertas não removam nem alterem turmas e turmas/disciplina criadas manualmente diretamente no TOTVS Educacional, foi disponibilizado o parâmetro **“Preservar registros criados (oferta) diretamente no TOTVS Educacional”**, localizado em **Secretaria | Geral 7/7 | Gestão de Oferta**.

Quando o parâmetro estiver habilitado, o sistema:

* Mantém todas as turmas criadas manualmente no TOTVS Educacional;
* Mantém todas as turmas/disciplina criadas manualmente;
* Não altera registros manuais;
* Não exclui registros manuais;
* Atualiza apenas os registros gerados pelo Planejamento de Ofertas.

Quando existir uma turma/disciplina criada manualmente no TOTVS Educacional e o processo do Planejamento de Ofertas tentar realizar uma associação gerencial/gerenciada com esse registro, o sistema deverá preservar a integridade da informação manual.

Neste caso, durante a geração de ofertas, o sistema:

* Não realiza a associação gerencial/gerenciada com a turma/disciplina criada manualmente;
* Registra a ocorrência no log do processo;

Com o parâmetro habilitado, o processo de geração de ofertas passa a atualizar apenas os registros criados pelo Planejamento de Ofertas, preservando a integridade das informações cadastradas manualmente no TOTVS Educacional. Disponível a partir das versões: 12.1.2510.237;12.1.2602.151.
