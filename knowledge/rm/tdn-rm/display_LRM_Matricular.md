---
content_hash: 365e2707f1edd9d40df787bce7f393262cd7f3ef8b9f7e5b61d34b7b9381d5c6
fetched_at: '2026-06-29T00:09:33.403051+00:00'
page_id: '425459013'
product: rm
source: tdn-rm
title: Matricular
type: documentation
url: https://tdn.totvs.com/display/LRM/Matricular
version: 33
---

No processo de matricular o aluno através do processo seletivo é necessário que o usuário tenha executado o pré-requisito para listar os alunos para matrícula. Para listar os alunos, o usuário terá que informar o Processo Seletivo e a Área Ofertada. Após esta seleção, o sistema irá listar a relação dos candidatos que foram aprovados no processo seletivo.

No processo de matrícula, o Totvs Educacional irá aproveitar os documentos entregues no Processo Seletivo, ou seja, documentos marcados como entregue. Ao realizar a matrícula no Totvs Educacional, o sistema irá atualizar a quantidade entregue e a data de entrega será mesma data em que foi realizada a matrícula do candidato através da matrícula no Processo Seletivo RM.

Para maiores informações sobre como configurar os documentos que serão exibidos para o candidato enviar acesse: <https://tdn.totvs.com/x/EREMKg>

Podemos selecionar o plano de pagamento no processo. O plano que será exibido deverá possuir a data final maior que a data em que a matricula está sendo realizada.

Plano de pagamento associado ao prospect

A partir da versão **12.1.2209,** o sistema disponibiliza uma funcionalidade que permitirá que a instituição de ensino realize negociações de plano de pagamento com o prospect (futuro aluno) a fim de viabilizar a matrícula deles.

Essa negociação permitirá associar planos de pagamento criados previamente a uma pessoa, seja um prospect, candidato ou aluno, para atender campanhas e negociações na captação de alunos.

Caso o candidato possua um plano de pagamento associado ao seu CÓDIGO ou CPF (ou passaporte, no caso de estrangeiro), ao finalizar o processo de matrícula, será associado ao contrato o plano que está associados ao prospect ou candidato. Se possuir mais de um plano de pagamento associado ao seu CÓDIGO ou CPF (ou passaporte, no caso de estrangeiro), o sistema irá relacionar ao contrato o plano de pagamento que foi selecionado na tela.

Para mais informações referentes à prospecções, clique [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=702373785).

Bolsas associadas ao prospect

A partir da versão **12.1.2209,** o sistema disponibiliza uma funcionalidade que permitirá que a instituição de ensino realize negociações de bolsas com o prospect (futuro aluno) a fim de viabilizar a matrícula deles.

Essa negociação permitirá associar bolsas criadas previamente a um prospect (candidato do processo seletivo, aluno do educacional ou pessoa com vínculo através de CPF ou Número do passaporte), para atender campanhas e negociações na captação de potenciais alunos.

Caso o candidato possua uma bolsa associada ao seu CÓDIGO ou CPF (ou passaporte, no caso de estrangeiro), ao finalizar o processo de matrícula, será vinculada ao contrato a bolsa que está associada ao prospect (candidato), se a bolsa estiver vinculada ao período letivo da matrícula ou for válida para todo o curso.

Para mais informações referentes à prospecções, clique [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=702373785).

Seleção do plano de pagamento

Caso o sistema esteja parametrizado para considerar a data de contabilização conforme a data da competência contábil do Contrato/Plano de pagamento, ao selecionar o plano de pagamento e ele não possuir o período de contabilização preenchido o sistema irá exibir a mensagem abaixo:

Vale ressaltar que essa informação não é mandatória para a finalização da etapa de matrícula, caso ainda assim ela continue sem ser preenchida, se o usuário tentar avançar o processo o sistema irá exibir a mensagem a seguir, e dará opção de prosseguir sem preencher essa informação no momento da matrícula:

Na regra de matrícula existem várias validações que podem gerar avisos ou erros dependendo das opções configuradas no perfil do usuário. No último passo do processo o usuário tem como interferir nestas questões, ou seja, se este tem no seu perfil a possibilidade de matricular um aluno inadimplente é possível neste passo permitir ou não este ação. Sempre que o usuário possuir pelo menos uma opção marcada no perfil do usuário para os itens "Matrícula / Rematrícula" e/ou "Biblioteca" uma nova aba será disponibilizada. Esta nova aba conterá todas as opões destes itens, no entanto apenas as opções que no perfil estiverem marcadas estarão habilitadas e permitirão modificação. Desta forma se neste perfil a opção "Matricular alunos inadimplentes" estiver marcada será possível alterar o seu valor antes da execução do processo acima mencionado.

Há uma opção de sobrescrever as informações de deficiência e/ou endereço do aluno dentro do processo. O intuito destes parâmetros é permitir ao usuário a possibilidade de sobrescrever ou não os dados de deficiência e/ou endereço, sendo que se o novo candidato não existir no cadastro de pessoas, os dados de endereço e deficiências serão automaticamente copiados para a nova pessoa, a função sobrescrever somente terá ação para candidatos cuja pessoa já existe no cadastro de pessoas.

RA Global

Se o TOTVS Educacional estiver parametrizado (Parâmetros >> Secretária >> Geral 1/6) para utilizar RA Global, e a opção “Candidato que já são alunos" estiver definida para aproveitar o RA existente, será verificando se o aluno já está cadastrado em outras coligadas e caso o aluno já exista em outra coligada o RA do aluno será preservado/reaproveitado.

Se a coligada da matricula do processo seletivo for diferente da coligada que o aluno já possui outra matricula, e o responsável financeiro já definido no aluno não for global, será gerado um novo cadastro para o responsável financeiro na coligada em que a matricula está sendo efetivada.

É importante ressaltar que se o responsável financeiro for global a coligada em que a matricula está sendo efetivada deve estar com o TOTVS Gestão Financeiro parametrizado para permitir cadastros de cliente como global.

Balanceamento de Turma

É possível aplicar o balanceamento de turma marcando a opção "**Realizar enturmação aplicando o balanceamento de turmas**", para maiores informações [clique aqui](https://tdn.totvs.com/display/LRM/Balanceamento+de+Turma)

Webservice

## **Webservice**

Quando o processo é executado pelo RM.exe, na etapa de seleção dos candidatos, somente serão exibidos candidatos que estejam com o "Status de opção" como "Em chamada", ou seja, passaram por todo o fluxo de inscrição e classificação (manual ou por nota) para chegar a etapa de matrícula. No caso da execução do processo ser executado por Webservice (SOAP ou Rest), as regras são as mesmas, ou seja, só serão matriculados os candidatos que estiverem corretamente posicionado nesta situação do fluxo de matrícula, ou seja, estejam com o "Status de opção" como "Em chamada".   
Candidatos com "Status de opção" diferente de "Em chamada" não serão matriculados e serão reportados ao final do processo como erro indicando que não estavam aptos para matrícula.

Esta validação está disponível à partir das versões: 12.12502.272, 12.1.2506.233 e 12.1.2510.161.

## ****Ensino Básico****

Durante o processo, o aluno pode se matricular em um ou mais [itinerários formativos](https://tdn.totvs.com/pages/viewpage.action?pageId=547240322). Para que seja possível visualizar quais itinerários estão disponíveis é necessário realizar a configuração no Totvs Processo Seletivo. No Processo Seletivo, acesse a [Área de Interesse Ofertada](https://tdn.totvs.com/pages/viewpage.action?pageId=425458924) e informe quais os itinerários serão ofertados de acordo com a matriz aplicada informada. Após, selecione durante a [Inscrição do Candidato](https://tdn.totvs.com/pages/viewpage.action?pageId=425458937) em quais itinerários o aluno está apto a se inscrever.

No decorrer da matricula, a seleção da turma do itinerário formativo só ficará disponível mediante a seleção da turma no período letivo (no passo anterior). Caso não seja informada a turma para o itinerário, o aluno não será matriculado nas suas disciplinas, apenas no itinerário formativo. No passo de seleção de turma para os itinerários, serão exibidos todos os itinerários que os candidatos fizeram inscrição, ou seja, uma interseção com todos os candidatos selecionados, mas na execução do processo, cada candidato que irá se tornar um aluno, o mesmo será matriculado em seu itinerário formativo correspondente à sua inscrição.

**Funcionalidade disponível a partir da versão 12.1.27.**

Importante

É possível através dos parâmetros de "Sobrescrever informações do aluno", marcando o grupo de dados que serão sobrescritos, são eles, deficiências, endereço e dados pessoais. **Observação: Apenas os dados referentes ao aluno serão sujeitos a sobrescrita em caso de aproveitamento de pessoa, os dados dos responsáveis não serão alterados.**

**Importante**: A opção de Dados pessoas está disponível a partir da versão 12.1.2306 (Junho/2023).

Importante

Ao utilizar a opção de geração de contrato o candidato ou seu responsável financeiro serão utilizados para geração do cliente/fornecedor, porém, antes é feito uma busca para validar a existência de um cliente/fornecedor com os mesmos dados, sendo assim o sistema irá filtrar somente cliente/fornecedores que estejam ativos no TOTVS Gestão Financeira.

Á partir da versão 12.1.24.255, 12.1.25.195, 12.1.26.139, o sistema irá validar também as datas dos períodos de matrículas das turma/disciplinas (caso estejam preenchidas) da turma em que o candidato está sendo matriculado, se pelo menos uma das turma/disciplinas estiver fora do período válido de matrícula, o processo irá ser cancelado e o candidato não será matriculado.
