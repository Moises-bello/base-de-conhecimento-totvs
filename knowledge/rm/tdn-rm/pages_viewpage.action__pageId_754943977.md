---
content_hash: b3600a0a603118133c5e8cb441e903481e018cb2209034e8fb8603457d7875c0
fetched_at: '2026-06-29T00:11:33.259109+00:00'
page_id: '754943977'
product: rm
source: tdn-rm
title: Avaliação descritiva.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=754943977
version: 12
---

A avaliação descritiva consiste no procedimento executado apenas pelo portal, de avaliação dos professores para os alunos de suas turmas/disciplinas, onde este é executado manualmente para cada aluno matriculado na turma/disciplina.

O aluno e os responsáveis, terão acesso à visualização da avaliação descritiva realizada pelo professor, através da tela de consulta de notas de avaliação.

Parametrização do Corpore.net

A *url* utilizada para acessar o portal: Corpore.Net, é definida nos parâmetros globais, disponível em:  **Serviços Globais | Ambiente | Parâmetros Globais | 'Aba': Gerais**.

A instituição de ensino, tem opção de sobrescrever o valor deste parâmetro, alterando o arquivo de config do portal do professor, na tag "urlCorpore", disponível em: **... FrameHTML\web\app\Edu\PortalDoProfessor\config.json**

Se a Instituição de Ensino, informar outra URL neste campo, o portal está desconsiderar o valor informado na configuração realizada em Globais.

Execução do processo da associação da avaliação descritiva

A criação da avaliação descritiva para os alunos é feita pelo **TOTVS Educacional em Matrícula e Avaliação | Notas e Faltas | Avaliação Descritiva. Saiba mais em**

Realizar a avaliação descritiva

Para realizar a avaliação descritiva é necessário selecionar o ícone:  para cada aluno correspondente. 

Funcionalidade ainda não migrada

A funcionalidade ainda não migrada para novo portal do Professor, ao ser selecionado o sistema irá abrir uma nova aba no navegador e será redirecionado ao relatório do portal do Professor antigo (Corpore.Net).

Comentários

Os comentários das questões não são visíveis a alunos e responsáveis. Estas informações são para uso interno da instituição.

Opção "Bloquear alterações de notas e faltas" desmarcada

No **Portal do Professor** será necessário estar com a opção "Bloquear alterações de notas e faltas" **desmarcada** (localizada no perfil Educacional | Currículo e Oferta | Situação de matrícula | Status na disciplina).
