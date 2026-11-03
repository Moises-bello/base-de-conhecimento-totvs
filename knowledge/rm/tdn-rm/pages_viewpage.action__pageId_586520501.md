---
content_hash: ca1ea36ecd4cbbcc17217fa462d268dcc132d902a0b4922df8d6a8555cb4389d
fetched_at: '2026-06-29T00:10:53.799415+00:00'
page_id: '586520501'
product: rm
source: tdn-rm
title: Rematrícula no Ensino superior
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=586520501
version: 27
---

# Descrição

O processo de rematrícula permite que os alunos sejam rematriculados no período letivo seguinte ao que estão cursando.

Esse processo está disponível em ***Matrícula e Avaliação | Matrícula | Rematrícula.***

O processo foi revitalizado e para ganho em performance e possibilidade de utilizar o fracionamento de jobs.

# Vídeos Como Fazer

[PARTE 1 - Oferta de Período Letivo e Parametrização por Curso](https://www.youtube.com/watch?v=9sMcJ_Y41x8&t)

[PARTE 2 - Oferta de Turmas](https://www.youtube.com/watch?v=biePWuKoqKQ&t)

[PARTE 3 - Oferta do Plano de Pagamento](https://www.youtube.com/watch?v=I3OSQ-KiQHU&t)

[PARTE 4 - Execução do Processo 1/2](https://www.youtube.com/watch?v=nmQGaTkrY4A&t)

[PARTE 5 - Execução do Processo 2/2](https://www.youtube.com/watch?v=zVYfRW1kR6A&t)

# Processo

Nesta tela é possível visualizar quem é o próximo período letivo e pré-visualizar os alunos que serão considerados na rematrícula.

Ao clicar na pré-visualização de alunos será exibido a lista de alunos que estarão aptos a rematrícula. Dependendo do filtro efetuado na tela principal da rematrícula, o volume de alunos que o filtro irá retornar poderá ser muito grande, ocasionando uma lentidão ao trazer os alunos.

 A partir desta tela a instituição poderá remover alunos que não queira que faça parte da execução do processo.

 Ao alterar algum filtro, a lista de alunos a serem removidos da matrícula é apagada, e o usuário deverá selecioná-los novamente.

Ao finalizar o processo uma mensagem é exibida para confirmar que os alunos retirados não farão parte da rematrícula, caso confirme, o processo é executado.

***Observação:***Caso o filtro Multi Contexto estiver marcado, não será permitido selecionar os alunos na tela de pré-visualização. 

## Lista de situações de matrícula

Serão listadas na grid de situação de matrícula, todas pertencente ao contexto logado e que estejam habilitadas no período letivo.

| Situação de matrícula habilitada no período letivo |
| --- |
|  |

## Multi Contexto

Foi implementando a possibilidade de utilizar a rematrícula para múltiplos contextos. Ao clicar no botão de seleção dos contextos irá abrir uma tela com os contextos disponíveis para seleção mediante filtro.

Os contextos que serão exibidos, serão os que possuem:

* Permissão no contexto.
* Permissão no item de rematrícula no contexto.
* Relação de cadastro (de-para) entre períodos letivos entre o contexto logado e os outros contextos.

Ao marcar os contextos e clicar no botão **Selecionar contextos** todos os contextos que foram selecionados serão considerados na execução da rematrícula.

Seleção do contexto logado

Lembrando que, para considerar o contexto logado na rematrícula, o mesmo deve ser selecionado nesta tela, ou seja, se não selecionar o contexto logado, o mesmo não será considerado na rematrícula.

A utilização da funcionalidade de multi contexto requer algumas regras:

* Possuir permissão no perfil para utilizar o multi contexto:

* Os contextos que poderão ser utilizados devem possuir a mesma apresentação, ou seja, só serão utilizados contextos do tipo "ensino superior".
* O usuário que está executando a operação deve possuir permissão nos perfis quanto na funcionalidade de rematrícula nos contextos que serão utilizados.
* As relações de cadastro em coligadas e filiais devem existir para os itens "período letivo", "situação" e "turno".

Ao executar o processo todas as relações de cadastro (período letivo, situações de matrícula, e turno) serão validadas se existem para cada contexto. Com isso, o contexto que estiver com as relações de cadastro criadas o mesmo será executado a rematrícula, caso não exista alguma relação de cadastro para o contexto, ele não será considerado na rematrícula.

## Filtros

Foram implementados filtros para a rematrícula, estes filtros são complementares aos dados básicos como período letivo e situações da matrícula, porém não será possível utilizar os três filtros, será permitido somente a utilização de um deles.

### Filtro genérico

Filtra conforme a visão de matrículas de alunos.

### Filtro por Período letivo / Matriz Aplicada

Filtra utilizando o período letivo informando juntamente com a matriz aplicada.

Observações

Não é permitido utilizar este filtro quando a opção de multi contexto for utilizada.

### Filtro por Consulta SQL

Permite a utilização de uma consulta SQL obedecendo as informações mínimas para filtrar os alunos.

**Observação**: é necessário selecionar os campos CODCOLIGADA, RA da tabela SALUNO, IDHABILITACAOFILIAL da tabela SMATRICPL e NOME da tabela PPESSOA. Opcionalmente poderá selecionar o campo CODTURMA da tabela SMATRICPL, entretanto se não informar este campo as opções de dar preferência para a turma anterior e/ou próxima turma não irão funcionar corretamente.

Observações

Não é permitido utilizar este filtro quando a opção multi contexto for utilizada.

## Parâmetros de situação de matrícula pendente

Foram inseridos também três novos parâmetros, estes novos parâmetros possibilitam ao usuário definir uma situação de matrícula pendente no período letivo e nas disciplinas quando o aluno possui pendências financeiras, da biblioteca, de documentos obrigatórios ou ocorrências que bloqueiam a matrícula. Quando marcado algum dos parâmetros, será habilitado os campos para informar as situações de matrícula com pendência para o período letivo e para as disciplinas.

Estes parâmetros só serão habilitados se o usuário possuir a permissão. Segue as regras para para habilita-los:

Observações

Caminho para acesso ao parâmetro geral e parâmetro de perfil **consecutivamente**:

Modulo Educacional → Configurações → Parâmetros → Matrícula → Avançar → Movimento 1/4

Serviços Globais → Segurança → Perfis → Sistema: Educacional → Educacional → Anexos → Parâmetros educacionais → Matricula/Rematrícula/Transferência

**O parâmetro da rematrícula "Aluno em débito de documentos obrigatórios..." é habilitado quando:**

* O parâmetro geral está desabilitado independente da permissão especial no perfil
* e/ou
* O parâmetro geral está habilitado com a permissão especial no perfil habilitado.

Parâmetro geral:

Parâmetro do perfil:

**O parâmetro da rematrícula "Alunos inadimplentes, assumem a situação..." é habilitado quando:**

* O parâmetro geral está desabilitado independente da permissão especial no perfil.
* e/ou
* O parâmetro geral está habilitado com a permissão especial no perfil habilitado.

Parâmetro geral:

Parâmetro do perfil:

**O parâmetro da rematrícula "Alunos com pendências na biblioteca..." é habilitado quando:**

* A permissão especial no perfil estiver habilitada.

Parâmetro do perfil:

**o parâmetro da rematrícula "Alunos com ocorrências que bloqueiam..." é habilitado quando:**

* A permissão especial no perfil está habilitada.

Parâmetro do perfil:

## Recomendações do fracionamento e multi contexto

Por se tratar de uma operação que geralmente é feita para um grande volume de dados, principalmente quando utilizado a função de multi contexto, algumas boas práticas são recomendadas para obter o máximo de desempenho da funcionalidade.

Quando utilizado a opção de multi contexto e um dos contextos selecionados possuir uma quantidade muito superior de alunos que os demais contextos, é altamente recomendável utilizar a rematrícula somente para este contexto, pois os balanceamentos de carga serão mais bem definidos e a operação será otimizada.

Quando a quantidade de alunos a serem rematriculados for semelhante entre os contextos, a opção de multi contexto é muito recomendada e o balanceamento de carga também será bem definido otimizando a execução.

# Campo Período e seu preenchimento automático

Para mais informações [clique aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=1032857467)
