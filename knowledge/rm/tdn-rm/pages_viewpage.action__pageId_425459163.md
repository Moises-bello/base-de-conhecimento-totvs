---
content_hash: 579c43a45a7ce1b5bd2887493445754f86cedd0da3983f04ff8d8bab9769ece2
fetched_at: '2026-06-29T00:09:34.469830+00:00'
page_id: '425459163'
product: rm
source: tdn-rm
title: Assistente de concessão de bolsa futura
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459163
version: 10
---

---

As bolsas futuras a serem concedidas devem ser cadastradas uma a uma para os alunos. O assistente de concessão de bolsa futura é um facilitador para o usuário, uma vez que disponibiliza uma série de filtros, otimizando assim a seleção de alunos torando-a mais prática e rápida.

O sistema possibilita que o usuário faça o filtro de alunos utilizando:

* Seleção por RA
* Seleção de alunos por filtro: Curso, Habilitação, Matriz Curricular e Turno
* Seleção de aluno por consulta SQL

Após adicionar os alunos conforme o filtro utilizado e selecioná-los avance para a próxima etapa do processo clicando no botão *Avançar*.

Nesta nova etapa do processo, na aba *Bolsas*, é necessário que o usuário informe qual [bolsa](http://tdn.totvs.com/display/LRM/Bolsas+-+Educacional) será utilizada, a sua ordem, a validade inicial e final, a indicação do desconto e a confirmação se a bolsa será vinculada a todos os serviços e se a concessão ficará ativa, mas lembre-se que se você optar por desmarcar a opção de concessão ativa, a bolsa não será associada automaticamente na inclusão de um novo . Se desejar conceder a bolsa somente a alguns serviços, por exemplo somente para o serviço Mensalidade, desmarque a opção para todos os serviços e na aba *Serviços*, indique o serviço desejado e confirme ou indique o desconto para este serviço. Na aba *Matriz aplicada* é sempre necessário informar qual [m](http://tdn.totvs.com/display/LRM/Matriz+Aplicada)[atriz aplicada](http://tdn.totvs.com/display/LRM/Matriz+Aplicada) a bolsa será vinculada, pois sem esta informação não é possível o cadastro automático da bolsa no contrato do aluno.

É possível também definir a "Ordem de Aplicação do Desconto por Antecipação" no campo  durante o assistente para concessão de bolsa futura. Esse campo tem o objetivo de informar se o valor do desconto por antecipação será calculado antes ou depois do cálculo do valor da bolsa inserida no contrato via concessão de bolsas futuras. Saiba mais acessando o documento técnico na guia "Ordem de Aplicação do desconto por Antecipação" na seção '[Concessão de Bolsas Futuras](http://tdn.totvs.com/pages/releaseview.action?pageId=325847718)'.

Após preencher todas as informações necessárias como bolsa, validade e matriz aplicada, acione o botão *Incluir* e se desejar conceder para mais alguma bolsa, informe em seguida os novos dados e no final acione novamente o botão *Incluir*.

Após conferir os dados de todas as bolsas indicadas para serem concedidas, clique no botão *Avançar* para finalizar o processo. No final será apresentado um **LOG** com as informações das concessões incluídas.

A partir da versão 12.1.32

A tela *Detalhes da Bolsa* ganhou uma nova estruturação com o objetivo de melhorar a experiência do usuário. A interface carrega melhorias na estruturação de cada bolsa adicionada onde agora é possível identificar de forma simples quais matrizes aplicadas e serviços farão parte da bolsa futura que será concedida. Além de permitir uma melhor interação através da inclusão e remoção de Bolsas, Matrizes Aplicadas e Serviços.

**Obs.:**Caso inclua uma bolsa com a opção de todos os serviços habilitada e deseje desabilitar essa opção, será necessário a remoção da bolsa e a inclusão da mesma com a opção de todos os serviços desmarcada.

Um novo comportamento foi adicionado na tela de concessão de bolsas futuras e no assistente de concessão de bolsas futuras. Caso a opção de todos os serviços NÃO esteja marcada, o usuário será impossibilitado de alterar o tipo de desconto e o percentual da bolsa será nulo. Desta forma, será evidente que o percentual considerado na concessão da bolsa será o valor atribuído no serviço e não o da bolsa.

Quando o sistema for utilizar configurações de serviço, para mudar as configurações do desconto, é necessário marcar o flag "**Permite alterar valor**", no cadastro de bolsa.

No caso acima, o tipo e o valor do desconto serão disponibilizados para edição no anexo de **Serviços de concessão de bolsas futuras**.

**Observações**

* Na inclusão de concessão da bolsa futura, quando o aluno possuir matrícula em mais de uma matriz curricular que esteja ativa ou quando a matriz curricular possuir mais de um turno associado, o usuário deverá selecionar a matriz desejada para a inclusão da bolsa futura.

* No assistente de concessão de bolsas futuras, quando o contexto do sistema estiver parametrizado como Ensino Superior, na guia de matriz aplicada serão listadas somente as matrizes aplicadas nas quais o aluno está matriculado. Já quando o contexto do sistema estiver configurado como Ensino Básico, serão listadas tanto as matrizes referentes aos cursos em que o aluno está matriculado, quanto todas as matrizes que possuam os campos “Próximo Curso”, “Próxima Série” e “Próxima Matriz Curricular” preenchidos na Matriz Curricular.

Os campos “Próximo Curso”, “Próxima Série” e “Próxima Matriz Curricular” estão disponíveis para preenchimento apenas nas matrizes curriculares do Ensino Básico.

* As bolsas futuras somente serão incluídas nos contratos dos alunos se no cadastro das referidas concessões houver a indicação da matriz aplicada à qual poderão ser vinculadas, assim como as referidas bolsas devem estar devidamente associadas ao período letivo dos alunos.

 Informações Complementares

---

Bolsa
