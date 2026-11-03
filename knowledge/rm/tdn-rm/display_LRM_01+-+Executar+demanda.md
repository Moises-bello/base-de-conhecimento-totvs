---
content_hash: f7544f4d87a63664c90c59ff7f1dc27f1fded079b40a9eb43035a6aa8efc17df
fetched_at: '2026-06-29T00:11:28.421808+00:00'
page_id: '731214843'
product: rm
source: tdn-rm
title: 01 - Executar demanda
type: documentation
url: https://tdn.totvs.com/display/LRM/01+-+Executar+demanda
version: 31
---

## Visão geral

Este passo é responsável por executar e acompanhar demandas de cada curso.

## Funcionamento dos filtros

Os filtros disponíveis para seleção são: curso, habilitação, matriz e turno. Os cursos retornados pelo filtro incluirão todos os cursos que possuem  relacionada ao período letivo anterior, informado no  vinculado ao  selecionado no topo da página.

Estes filtros funcionam da seguinte forma, se no curso estiver selecionado a opção **todos** os demais campos (habilitação, matriz e turno) ficam desabilitados, caso se selecione um curso, o campo de habilitação fica disponível para seleção.

Se no campo habilitação estiver selecionado a opção **todas** os demais campos (matriz e turno) ficam desabilitados, caso se selecione uma habilitação, o campo de matriz ficará disponível. O mesmo acontece com o campo de matriz, se estiver selecionada a opção **todas**o campo de turno ficará desabilitado, caso se selecione uma matriz, o campo de turno ficará disponível.

## Tabela dos cursos

Pós seleção dos filtros, basta clicar no botão **adicionar**. Ele irá popular a tabela de acordo com o filtro selecionado. Toda vez que se clica no botão adicionar os cursos são adicionados da grid sempre no topo dela, porém, jamais irá repetir o mesmo curso, habilitação, matriz e turno.

A tabela é composta pelas colunas de curso, habilitação, matriz e turno, colunas de identificação, status, data de início, data de término e usuário responsável pela execução da demanda daquele curso, por fim uma coluna , composta  pelos menus "Parametrização por Curso" e "Visualizar" .

### Parametrização por curso

Alguns parâmetros para a execução da demanda que se aplicam a todas as matrizes do período de planejamento estão presentes no cadastro do [período letivo de planejamento](https://tdn.totvs.com/pages/viewpage.action?pageId=710554269).

Na etapa de execução da demanda, o menu de ação "Parametrização por curso" disponível para cada item do grid, permite definir esses (e outros) parâmetros para a execução da demanda de forma específica para a respectiva matriz aplicada.

Ao entrar nessa tela pela primeira vez, ela será carregada com os parâmetros gerais cadastrados no cadastro de [período letivo de planejamento](https://tdn.totvs.com/pages/viewpage.action?pageId=710554269). Ao preencher os dados nessa tela e salvar, os parâmetros a serem utilizados na execução da demanda para a respectiva matriz aplicada, passarão a ser os que foram definidos nessa parametrização por curso.

Detalhes sobre o preenchimento e utilização desses parâmetros estão na documentação do cadastro de [período letivo de planejamento](https://tdn.totvs.com/pages/viewpage.action?pageId=710554269).

Períodos não ofertantes, define quais períodos não serão ofertados no próximo período letivo. Caso o próximo período do aluno seja um período não ofertado o sistema informa o próximo.  
Exemplo: Aluno do 3º período, o próximo é o 4º período, porém a instituição não irá ofertar o 4º período, dessa forma o próximo período do aluno passa a ser o 5º período.

### Visualizar

Possibilita visualizar a , ao clicar neste ícone, será feito o redirecionamento para o passo de , com os filtros preenchidos do curso, habilitação, matriz e turno referente a linha clicada. As colunas data de início, data de término, usuário ficarão preenchidas caso a demanda esteja em processamento, processada ou processada com erro, já a coluna de visualizar demanda, somente ficará disponível se a demanda tiver sido executada com sucesso, ou seja, com status de processado.

Por fim temos três botões pós a grid, **limpar**, **atualizar** e **processar**. O botão **limpar**, tem finalidade de limpar toda a grid. O **atualizar** efetua uma atualização nos dados que estão presente na grid, ou seja, faz uma chamada ao servidor com os dados que estão na grid e traz atualizações dos dados caso exista. Vale frisar que esta grid não se atualiza automaticamente a cada demanda executada, é necessário clicar no botão **atualizar** ou se clicar no botão **adicionar** para adicionar outro curso, será feito a adição do novo curso e a grid será atualizada. Por último o botão **processar** tem função de processar a demanda de um ou mais cursos, somente é possível processar algo se tiver marcado alguma linha na grid, mais informações do botão processar está descrito logo abaixo.

## Processar Demanda

Disparada ao clicar no botão **processar** irá criar um job para cada curso marcado na grid. Se o curso selecionado estiver com o status de **demanda aguardando processamento,** **demanda em processamento**, **geração da oferta aguardando processamento**, **geração da oferta em processamento**, **geração da oferta processada** ou **geração da oferta processada com erro** não será feita o processamento deste curso. Para os demais status será feito o processamento, porém vale ressaltar que um curso já processado com sucesso for processado novamente o mesmo será sobreposto, não será gravado nenhum histórico de processamento anteriores. O mesmo vale para cursos que estão com o status **demanda processado com erro**.

A regra de processamento da demanda funciona da seguinte maneira, o  selecionado, tem vinculado a ele um , e este possui um período letivo anterior. Dado esta informação, o processo irá buscar todos os alunos devidamente matriculados no período letivo anterior do curso selecionado para o processamento. Uma informação obrigatória e que deverá estar devidamente preenchida é o campo período na matrícula do período letivo do aluno, sem este campo preenchido o processamento dará erro e este aluno não será considerado na contagem da demanda. Para cada aluno matriculado será buscado todas as disciplinas obrigatórias concluídas, pendentes e em andamento, e a cada disciplina da grade é verificado se aluno não cursou a disciplina, caso afirmativo, é verificado se o período da disciplina é menor ou igual ao período do aluno, se sim soma 1 de vaga devedora, se não soma 1 de vaga regular. Isso acontece enquanto o período da disciplina da grade for menor ou igual ao período do aluno + 1.

As disciplinas de 1º período podem receber um valor de demanda regular. Para isso, é necessário preencher o campo demanda de alunos do 1º período no cadastro do  ou através do cadastro de parametrização por curso . Com este campo preenchido, ao processar uma matriz curricular que tenha o status "Atual", todas as disciplinas do 1º período dessa matriz curricular receberá este valor na coluna de demanda regular.

Disciplinas **optativas/eletivas** não são consideradas neste processo, apenas disciplinas **obrigatórias**. A regra de **correquisito**também não está sendo levada em consideração.

Foi incluído o campo Validar pré-requisitos no cadastro do [período letivo de planejamento](https://tdn.totvs.com/pages/viewpage.action?pageId=710554269). Com este parâmetro marcado, não será possível gerar demanda para disciplinas que não tenha o pré-requisito cumprido.

Exemplo

Dado o curso de Sistema de Informação, o mesmo possui 8 períodos, sendo cada período com 5 disciplinas. Um aluno está no 3º período, matriculado nas 5 disciplinas do período.

No 1º período o aluno concluiu apenas 4 disciplinas.

No 2º período o aluno concluiu todas as 5 disciplinas.

Ao rodar o processamento da demanda, o calculo para este aluno seria assim, 1 demanda de períodos anteriores (disciplina do 1º período que não foi concluída) e 5 demanda regular (como o aluno está no 3º período com todas as 5 disciplinas matriculadas, deduzimos que ele vai concluir todas). Com isso, na  a disciplina que o aluno não conclui no 1º período terá o valor de 1 na demanda períodos anteriores e 0 na demanda regular, totalizando o valor de 1 na demanda total. Já as disciplinas do 4º período todas terão o valor de 0 na demanda períodos anteriores e 5 na demanda regular, totalizando 5 na demanda total.

Isso irá se repetir para todos os alunos e somando para cada disciplina.

**Por fim, após realizar o processamento de uma demanda, será executada uma rotina que irá atualizar o status dessa etapa na tabela SPLETIVOPLANETAPAS. A etapa em questão é a 2, seus status passará a ser 2 e ATIVA será atualizado de 0 para 1.**
