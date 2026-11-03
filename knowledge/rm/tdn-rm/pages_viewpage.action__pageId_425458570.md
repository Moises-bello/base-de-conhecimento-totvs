---
content_hash: 3c74f559af7266ce0b4c7a22b1e4d48de99dc0d5b0e1cbbec16b2387a2ac426a
fetched_at: '2026-06-29T00:09:30.938443+00:00'
page_id: '425458570'
product: rm
source: tdn-rm
title: Status no Período Letivo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458570
version: 43
---

# Descrição

Nesta tela você pode ativar ou desativar vários tipos de status para a situação de matrícula no Período Letivo.

# Aba Geral

#### Disciplinas com esta situação de matrícula assumem a nova situação de matrícula do Período Letivo

Na mudança de status do aluno no período letivo, o sistema verifica se as disciplinas em que o aluno está matriculado têm o mesmo status antigo do aluno no período letivo. Caso tenha, estas disciplinas assumem o novo status, conforme parametrização.

Ex: Status no Período Letivo e nas Disciplinas é Matriculado. Status Matriculado está com esse parâmetro "Disciplinas com esta situação de matrícula assumem a nova situação de matrícula do Período Letivo" habilitado.  
Se aluno mudar para Status Trancado no período Letivo, todas as disciplinas que estiverem com Status igual ao do Período Letivo anterior (que era Matriculado) passará para o Status atual que é Trancado.

Todas as disciplinas do aluno no período letivo que atenderem à regra, terão seus status alterados, independente se são da mesma turma do período letivo ou não.

Necessário que a situação de matrícula da disciplina esteja marcado o item **disciplina** na aba disciplina.

Este parâmetro tem prioridade sobre o lookup "**Altera situação de matrícula das disciplinas em curso e/ou conta como aluno matriculado para:" (Ensino Superior)** e sobre o lookup **"Altera situação de matrícula das disciplinas para:" (Ensino Básico)**

#### Altera o Tipo do aluno para

Você poderá alterar o tipo do aluno atual para outros tipos cadastros.  
Ex.: tipo Candidato para o tipo Aluno

#### Ação usuário do aluno

A situação de matrícula do aluno pode cancelar/ativar/não alterar o usuário do aluno no RM. Um aluno somente terá seu usuário cancelado, caso esta opção estiver marcada, se ele não possuir nenhuma matrícula ativa em algum período letivo. Ou seja, se o mesmo possuir uma matrícula no período letivo 2017/2 ativa, e o mesmo tiver sua situação de matrícula no período letivo 2018/1 alterada para uma que cancela o usuário, o mesmo não será cancelado, pois a matrícula em 2017/2 está ativa.

#### Bloqueia alteração para este status por falta de doc. obrigatórios

Quando estiver ativo um aluno que assumir essa situação terá a verificação se os documentos obrigatórios forem entregues.

#### Desativa usuário da biblioteca ou do Pergamum

Quando este parâmetro está habilitado e um aluno assumir esta situação de matrícula, se o TOTVS Educacional estiver integrado com o TOTVS Gestão Bibliotecária ou Pergamum, será cancelado o usuário no sistema  bibliotecário de acordo com integração habilitada.

#### Altera situação de matrícula das disciplinas em curso

Este parâmetro tem por objetivo informar que ao se alterar a situação de matrícula do período letivo, as disciplinas com situação de matrícula (com parâmetro marcado **é uma disciplina curso**) também terão seus status alterados para o status informado no respectivo campo..

A partir das versões 12.1.34.229, 12.1.2205.172, 12.1.2209.114 e 12.1.2302, este parâmetro terá o seu nome alterado para "**Altera situação de matrícula das disciplinas em curso e/ou conta como aluno matriculado para:"**. Com isso, disciplinas com situação de matrícula (com um dos parâmetros marcados **é uma disciplina em curso**e/ou **conta como aluno matriculado na turma e turma/disciplina**) também terão seus status alterados.

No Ensino Básico esse parâmetro se chama "**Altera situação de matrícula das disciplinas para:**", e tem por objetivo informar que ao se alterar a situação de matrícula do período letivo, as disciplinas do aluno no período letivo também terão seus status alterados para o status informado no respectivo campo.

Para o Ensino Básico, somente **as disciplinas cuja turma é a mesma turma do período letivo** e que atenderam à regra, é que terão seus status alterados.

#### Bloqueia alteração de situação de matrícula

Esse parâmetro bloqueia a alteração da situação de matrícula do aluno no período letivo. O sistema possui uma permissão especial localizada nos Parâmetros Educacionais no perfil do usuário. Essa permissão especial permite que o usuário associado a esse perfil altere a situação de matrícula do aluno.

#### Preenche data de encerramento de matrícula para efeitos do Educacenso

Quando este parâmetro está habilitado na situação de matrícula, ao executar o processo de alterar a situação de matrícula o campo data de encerramento da matrícula para efeitos do Censo será preenchido com a data atual da execução do processo.

#### Exige contrato financeiro

Quando este parâmetro estiver habilitado, ao executar o processo de matrícula ou o processo de mudança de turno (Ensino Básico - ver detalhes em ), um novo contrato do tipo Plano será criado para o aluno. Entretanto, se estiver executando um processo que altera a situação de matrícula no período letivo para um que tenha a situação com este parâmetro marcado, o sistema verifica se já existe um contrato do tipo "Plano" no período letivo referente a matriz aplicada, caso não exista o sistema então cria um novo, porém se existir não será criado nenhum contrato novo.

#### Validar inadimplência de aluno na matrícula pelo portal

Parâmetro com a finalidade de efetuar ou não a validação de inadimplência do aluno na matrícula no portal.

Porém para que este parâmetro fique disponível é necessário marcar o parâmetro **bloquear alunos** em Configurações | Parâmetros | RM Portal | Geral 4/6 | grupo **débitos financeiros**.

#### Situação de matrícula - Diploma Digital

Este campo tem por objetivo atender as situações de matrícula, de acordo com o layout definido pelo Diploma Digital na versão 1.05.

# Aba Envio de e-mail

A instituição tem a possibilidade de configurar suas situações de matricula para que o aluno, ao receber uma determinada situação, seja avisado por e-mail sobre tal mudança.  
Exemplo suponhamos que um aluno está com status de "Aguardando Vaga". A instituição pode configurar que quanto ele passar para o status de "Matricula definitiva" seja enviado um e-mail para o aluno lhe avisando disto.

Já é disponibilizado um template padrão do corpo do e-mail, onde as tags serão substituídas pelo valor do campo, por exemplo, onde tem **\_NOMEDOALUNO\_** será substituído pelo nome do aluno e assim por diante. As tags disponíveis são:

* \_NOMEDOALUNO\_, nome do aluno
* \_RAALUNO\_, registro acadêmico do aluno
* \_NOMEHABILITACAOFILIAL\_, nome do curso
* \_CODPERLET\_, código do período letivo
* \_SITUACAOANTERIOR\_, situação de matrícula anterior
* \_NOVASITUACAO\_, nova situação de matrícula
* \_DATAALTERACAO\_, data da alteração da situação de matrícula
* \_NOMEDAFILIAL\_, nome da filial

Ainda nesta tela é possível parametrizar um relatório do reports para que o mesmo seja enviado como anexo junto ao e-mail. Caso informe um relatório o mesmo deverá conter como **banda principal** a tabela **SMATRICPL**. Esta banda principal poderá ser colocada de duas maneiras, adicionado como fonte de dados a própria tabela ou uma consulta SQL. Vale reforçar que na consulta sql é necessário informar quatro campos no filtro, são eles CODCOLIGADA, RA, IDPERLET e IDHABILITACAOFILIAL. Além disso, será necessário criar **quatros** parâmetros para que eles sejam utilizados no filtro que são CODCOLIGADA, IDPERLET, IDHABILITACAOFILIAL e RA, onde a **ordem** de criação dos parâmetros é importante ser obedecida para o correto funcionamento.

Segue exemplo de uma consulta SQL simples com os filtros.

Segue exemplo dos parâmetros criados no relatório.

# Aba Itinerário Formativo

#### Sub aba exclusiva para o nível de ensino básico.

#### Alteração de situação de matrícula no período letivo

A situação de matrícula pode ser configurada de forma que ao ser executado ao processo de alteração de situação de matrícula no período letivo, a situação de matrícula do itinerário também seja alterada. Todos os itinerários que estejam com a situação de matrícula equivalente a uma das selecionadas na lista abaixo, assumirão a mesma situação do período letivo.

Caso não seja selecionada nenhuma opção na grid a replicação do status não irá ocorrer.

#### Alteração da situação de matrícula no itinerário formativo

A alteração de situação de matrícula pode ser propagada para as **disciplinas**, bastando apenas configurar também qual situação as disciplinas deverão assumir caso o itinerário seja alterado.

Ao alterar a situação de matrícula do Itinerário Formativo, se a opção abaixo estiver preenchida todas as disciplinas do Itinerário Formativo que estiverem com status igual ao do Itinerário assumirão a situação de matrícula configurada neste local.

Caso não seja informado nenhuma situação de matrícula em **Altera situação de matrícula das disciplinas do Itinerário Formativo para** areplicação do status não irá ocorrer.  

#### Bloqueia alteração de situação matrícula em itinerário formativo na matrícula online

Ao deixar este parâmetro marcado, após o aluno confirmar a matrícula pela confirmação da rematrícula web ou matrícula de itinerário pelo menu exclusivo, a situação de matrícula do itinerário formativo não será alterada.

#### Alterar situação de matrícula apenas das disciplinas de itinerário que contam como aluno matriculado na turma

Criado a partir das versões 12.1.2502.237, 12.1.2506.186, 12.1.2510.119 e 12.1.2602, tem por objetivo escolher se as disciplinas de itinerário formativo terão ou não sua situação de matrícula atualizada caso estejam ou não com o parâmetro **conta como aluno matriculado na turma**marcado.

Se ele estiver marcado, apenas as disciplinas de itinerário formativo que **conta como aluno matriculado na turma** terão a sua situação de matrícula alterada para a nova, as demais disciplinas não terão seu status alterado.

---

**[Novo Ensino Médio](https://tdn.totvs.com/x/C3R9IQ)**

* [Itinerário Formativo](https://tdn.totvs.com/x/gjmeI)
* [Itinerário Formativo da Matriz Curricular](https://tdn.totvs.com/x/ThVxIQ)
* [Turma/Disciplina do Itinerário Formativo](https://tdn.totvs.com/x/jBVxIQ)
* [Parametrização por Curso](https://tdn.totvs.com/x/x-xbGQ)
* [Disponibilidade do Itinerário Formativo](https://tdn.totvs.com/x/VQx9IQ)
* [Matricular Aluno](https://tdn.totvs.com/x/4vtbGQ)
