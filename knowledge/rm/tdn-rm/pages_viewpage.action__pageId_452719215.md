---
content_hash: 5e63b8d5b409173c528c1098a2738d2e00cc99c6bb6cf1e64f2fdd206db1690c
fetched_at: '2026-06-29T00:10:04.547303+00:00'
page_id: '452719215'
product: rm
source: tdn-rm
title: Parâmetros do RM Portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719215
version: 39
---

**Etapa 1 -****Demonstrativo de Pagamento**

Permite ao funcionário visualizar seu demonstrativo de pagamento no Portal, de acordo com os parâmetros definidos.

**De/Para**

O usuário pode visualizar e definir o ano, mês e período que são relativos ao demonstrativo de pagamento do período que deseja consultar. Quando definido um período inicial e final os mesmo são aplicavés as competências finais e iniciais, não sendo filtrado para qualquer competência dentro do Mês/Ano Competência Inicial e Final.

Exemplo:

Mês/Ano competência Inicial: 01/2020; Número do Período Inicial: 1

Mês /Ano Competência Final: 12/2021; Número do Período Final: 99

Funcionário possui demonstrativo no período 105, na competência 11/2021, o mesmo será exibido, pois é competência é menor que foi definida no campo Mês/Ano Competência Final

Funcionário possui demonstrativo no período 105, na competência 12/2021, o mesmo não será exibido, pois a competência é a mesma que foi definida no campo Mês/Ano Competência Final e o período é maior que o número de período final definido.

**Não visualizar o dem. de pagamento nos seguintes períodos ( ; )**

Neste campo é possível informar quais períodos o funcionário não pode visualizar, para todas as competências informadas no parâmetro De/Para.

Exemplo:

Mês/Ano competência Inicial: 01/2020; Número do Período Inicial: 1

Mês/Ano Competência Final: 12/2022; Número do Período Final: 200

Informado no campo o período 105

Funcionário possui demonstrativo no período 105, na competência 11/2021 e na competência 12/2021, neste caso não ficará disponível para ele ambos dos demonstrativos

falseObservação

É possível informar mais de um período para este campo e os mesmos devem ser separados por ; (ponto e vírgula)

**Filtrar os períodos acima apenas na competência atual**

Com este parâmetro marcado, os períodos informados no campo não visulizar o dem. de pagamento nos seguintes períodos será aplicado somente para a competência atual, sendo visulizados os mesmos períodos em competências anteríores.

Exemplo:

Mês/Ano competência Inicial: 01/2020; Número do Período Inicial: 1

Mês/Ano Competência Final: 12/2022; Número do Período Final: 200

Informado no campo Não visualizar o dem. de pagamento nos seguintes períodos o período 105

Parâmetro Filtrar os períodos acima apenas na competência atual marcado

Funcionário possui demonstrativo no período 105, na competência 11/2021 e na competência 12/2021. A base está na competência 12/2021, logo o demonstratvivo da competência  11/2021 ficará disponível para o funcionário. O demonstrativo da competência 12/2021 não ficará disponível devido ao parâmetro marcado.

**Mostrar Salário com data de mudança até:**

Foi criado um parâmetro para definir a data limite das alterações salariais a serem exibidas no RM Portal, o parâmetro é válido para funcionários visualizando suas alterações, chefes continuarão visualizando todo o histórico de seus subordinados. Caso o parâmetro esteja desmarcado, não será estabelecido um limite para a data de exibição dos históricos salariais para os funcionários.

**Não seleciona ano/mês no demonstrativo**

Selecione esta opção para que o usuário possa apenas visualizar o mês de competência referente aos parâmetros informados acima. Caso não seja marcado este parâmetro, todos os envelopes da ficha financeira serão visualizados e o mês de competência e período referente aos parâmetros informados acima inclusive.

**Gera envelope via RM Reports**

Caso marcado, habilitará a seleção do **"Relatório do RM Reports"**.

**Relatório do RM Reports**

Nesse campo o sistema disponibilizará os relatórios importados/criados no RM Reports, ou seja, da plataforma .net.

Observação: Para que o relatório seja gerado corretamente no Portal, sendo um relatório novo, é importante o seu tipo ser "Envelope de Pagamento Portal", e então usar os campos que foram adicionados automaticamente, assim todos os parâmetros obrigatórios já são carregados.  
Caso for um relatório antigo e o usuário quiser reutilizá-lo, ele deve ser montado com os seguintes parâmetros do tipo Sequência de Caracteres: "CODCOLIGADA", "CHAPA", "ANOCOMP", "MESCOMP" e "NROPERIODO" (A nomenclatura é importante). Esses parâmetros devem ser usados em consultas SQL, com ":" na frente de cada (Como :CHAPA) para retorno dos dados.

Para mais detalhes sobre como criar/personalizar um relatório para o envelope de pagamento do portal, acesse o documento técnico:  [DT Relatório RM Reports Para o Portal](http://tdn.totvs.com/pages/viewpage.action?pageId=273985377)

**Relatório do Smart View**

Nesse campo o sistema disponibilizará os relatórios importados/criados no Smart View.

**Etapa 3 - Férias**

**Desabilitar marcação de Férias**

Com esta opção marcada, a página de "Férias Normais" será exibida com os campos: Inicio, Quant. Dias, Término, Abono, Dias Abono, 1ª Parc 13ª Sal DESABILITADOS para edição. Com a mensagem em vermelho: "Período de férias cadastrado não pode ser alterado pelo usuário. Vide parâmetros." Caso não exista período de férias cadastrado, o sistema habilitas os campos permitindo o cadastramento, ao salvar, os mesmos são desabilitados.

**Chefe/Supervisor pode fazer o cadastro de suas próprias férias**

* [x] Quando marcado/habilitado: A sugestão de férias cadastrada não precisará ser aprovada pelo gestor, ou seja, não passará pelo status 'G - Aguardando Aprovação do Gestor', sendo direcionada diretamente para aprovação do departamento pessoal, o status será 'D- Aguardando Aprovação do DP'.
* [  ] Quando desmarcado/desabilitado: A sugestão de férias cadastrada seguirá o fluxo normal. Deverá passar pela aprovação do gestor  com o status 'G - Aguardando Aprovação do Gestor', após a aprovação do gestor deverá ser aprovada pelo departamento pessoal, com o status  'D- Aguardando Aprovação do DP'.

**Impedir início de férias em feriados, dias de descanso ou até 2 dias antes destes**

Com esse parâmetro marcado o sistema impede que o funcionário insira sugestões de férias no portal em até dois dias que antecedem feriados e dias de descanso do funcionário.  
A verificação dos feriados cadastrados é de acordo com o calendário que está vinculado à seção do funcionário, no calendário deve ser informado os dias que são feriados. A verificação do dia de descanso é realizada de acordo com a jornada que o funcionário está vinculado, na jornada é inserido o dia de descanso.

Para os horário de trabalho noturno, será considerada a data de início da jornada para considerar o intervalo de 2 (dois) dias de descanso.

Observação

Para o correto funcionamento do parâmetro acima é necessário marcar o Parâmetro 'Ativar alterações da Reforma Trabalhista de acordo com a Lei Nº 13.467 de 13 de Julho de 2017', localizado em RH | Folha de pagamento | Configurações | Parametrizador | Folha Normal | Geral

**Não impedir marcação de férias para jornada 12x36**

Com este parâmetro marcado o sistema deverá permitir o a marcação de sugestão de férias, desde que não seja dia de folga ou feriado do respectivo funcionário. O Parâmetro acima só fica habilitado caso o parâmetro **Impedir início de férias em feriados, dias de descanso ou até 2 dias antes destes**esteja marcado. Mais informações neste [link](https://tdn.totvs.com/pages/viewpage.action?pageId=539699626).

**Desconsiderar dia compensado**

Com este parâmetro marcado o portal irá validar o tipo de Jornada cadastrada para o horário do funcionário e caso a mesma seja compensado, não irá impedir a marcação de férias até dois dias antes deste. O Parâmetro só fica habilitado caso o parâmetro **Impedir início de férias em feriados, dias de descanso ou até 2 dias antes destes**esteja marcado. Mais informações neste .

Observação sobre  relatórios:

Funcionamento padrão do relatório **FOPREL00030 – Aviso de Férias**, conforme configuração nativa no RM:

1. Tabela utilizada

* O relatório foi projetado para buscar informações diretamente na tabela **PFUNC (funcionário).**

2. Situação “**Marcadas**”

* Quando as férias estão apenas com a situação Marcadas, os campos **FIMPROGFERIAS1 e DTAVISOFERIAS** , localizado na **PFUNC**, é preenchido utilizando a primeira solicitação de férias registrada.

3. Duas solicitações de férias “**Marcadas**”

* Caso existam duas solicitações de férias simultaneamente com a situação “**Marcadas**”, o sistema mantém o valor da primeira solicitação no campo **FIMPROGFERIAS1 e DTAVISOFERIAS**.  
  Consequentemente, ao emitir o relatório para a segunda solicitação, o relatório continuará apresentando a data referente à primeira marcação, pois ambas ainda estão como “Marcadas”.

4. Como obter a informação correta para a próxima solicitação

* Para que o relatório utilize os dados da segunda solicitação, é necessário:
* Finalizar a primeira férias;
* Gerar novamente o aviso pelo Meu RH;

Assim, a **PFUNC** será atualizada com a nova **FIMPROGFERIAS1 e DTAVISOFERIAS**, permitindo que o relatório reflita a informação da segunda solicitação.

Para gerar o aviso de férias, mesmo em casos de mais de uma férias marcadas, sugerimos a utilização do Relatório do **SmartView**.

Recomendamos a utilização do relatório **FOPTRP0001 – Aviso de Férias** (**SmartView**), pois ele já disponibiliza filtros completos, como **Coligada, Chapa e Data de Pagamento (>= e <=).** Dessa forma, o aviso é gerado corretamente, com base nas informações das tabelas de funcionário e férias.

Além disso, a estrutura do **SmartView** é aprimorada. O relatório foi desenvolvido para utilizar diretamente a tabela de **FÉRIAS** como base, o que garante maior precisão e consistência nos dados apresentados.

 

**Etapa 4 - Férias II**

**Permite Solicitar 1ª parcela do 13° salário**

O pagamento da primeira parcela, prevista no artigo 2º, § 2º da Lei 4.749/65, que dispõe sobre o pagamento da gratificação natalina prevista na Lei 4.090/62, estabelece que o adiantamento possa ser concedido juntamente com o pagamento das férias do empregado, desde que este faça a solicitação (por escrito) ao empregador durante o mês de janeiro (01 a 31) do corrente ano, a solicitação deve ser feita em Janeiro pelo empregado porém não impede que a empresa faça a aprovação fora da competência de janeiro, já que o pagamento de adiantamento de 13° pode ser efetuada de Fevereiro a Novembro do ano corrente.

Com esse parâmetro marcado o sistema irá habilitar os campos para indicar o mês inicial e final que ficarão disponíveis para a solicitação do adiantamento do 13° salário e os campos para indicar o mês inicial e final para realizar o pagamento do adiantamento no portal.

**Observação:**

Quando o mês final for menor que o mês inicial, o sistema irá considerar o mês final sendo do ano subsequente, permitindo a solicitação da 1ª Parcela de 13º Salário.

**Exemplo:**

 Mês inicial para solicitar: 12

 Mês inicial para solicitar: 1

Serão considerados o mês inicial 12/AAAA e mês final 1/AAAA + 1

**Permite cadastrar abono pecuniário**

Com esse parâmetro marcado, sistema permite o cadastro de abono pelo funcionário no portal.

**Abono de férias requerido até 15 dias antes do término do período aquisitivo**

Com esse parâmetro marcado o sistema permite que seja cadastrado abono pecuniário até 15 dias antes do fim do período aquisitivo;

Exemplo: Funcionário com o período aquisitivo que finaliza em 24/08/2017, com esse parâmetro marcado pode-se marcar férias COM abono até o dia 09/08/2017 , caso desejar marcar COM abono mas independente da data fim do período aquisitivo, é necessário desmarca-lo. Se quiser marcar férias SEM abono, é necessário desmarcar os dois parâmetros.

**Limite de Abono é 1/3 do saldo de férias**

Com esse parâmetro marcado o sistema irá limitar o número de dias de abono pecuniário em 1/3 do saldo de dias de férias.

**Permite até 10 dias de abono pecuniário**

Com esse parâmetro marcado o sistema irá limitar em 10 (dez) dias de abono pecuniário nas férias.

**Limite até 10 dias de abono dentro período aquisitivo**

Com esse parâmetro marcado o sistema irá limitar em 10 (dez) dias de abono pecuniário nas férias dentro do mesmo período aquisitivo.

**Permite solicitar empréstimo de férias**

Ao marcar esse parâmetro, será permitido solicitar empréstimo de férias ao realizar a sugestão de férias através do RM Portal.

**Gerar a data de pagamento automaticamente**

Ao marcar esse parâmetro será gerado automaticamente a data de pagamento do empréstimo de férias.

**Impedir sugestão de férias após data limite início do gozo**

Com esse parâmetro marcado, o sistema irá impedir a marcação de férias com a data de início de gozo das férias que ultrapasse o limite de gozo de férias para que não seja paga férias em dobro para o funcionário.

**Observação:**

Este parâmetro foi criado para impedir a sugestão de férias através do RM Portal, **com abono pecuniário**, com a data de início de gozo das férias que ultrapasse o limite de gozo de férias para que não seja paga férias em dobro para o funcionário. Veja exemplos no link:  [Impedir sugestão de férias após data limite início do gozo](https://tdn.totvs.com/pages/viewpage.action?pageId=700509005)

**Etapa 5 - **E-mail de Férias****

Nesta etapa, o usuário poderá definir se será enviado e-mail de férias customizada para o gestor e/ou funcionário nas situações de: Sugestão de férias cadastradas pelo funcionário, aprovação de férias pelo Gestor, aprovação de férias pelo DP e reprovação de férias pelo Gestor/DP.

O parâmetro 'Enviar email na sugestão e aprovação de férias' que, anteriormente, era visível na etapa de "Férias", foi movido para esta nova etapa. Para que seja enviado o e-mail é necessário que este parâmetro esteja marcado.

Ao marca-lo serão habilitados alguns campos. Em cada um desses campos deve ser vinculada uma mensagem customizada para que o e-mail seja enviado de acordo com a mensagem e com a ação realizada no fluxo de inclusão e aprovação/rejeição de sugestão de férias. Para verificar do que se trata a mensagem customizada verificar o link abaixo:  
   
Mensagens Customizadas  
   
Campos Habilitados:                                                                                     
   
**Sugestão de Férias para confirmação do cadastro do Funcionário**

Quando o funcionário cadastrar uma nova sugestão de suas férias, será enviado um e-mail para o próprio funcionário confirmando a inclusão da sugestão.

**Cadastro da Sugestão de férias para aprovação do Gestor**

O gestor receberá um e-mail informando sobre a sugestão de férias do funcionário e solicitando sua aprovação.

**Impedir início de férias em feriados, dias de descanso ou até 2 dias antes destes.**

Com o parâmetro marcado, o funcionário não poderá cadastrar uma sugestão de férias com data início antecedendo em até 2 dias a feriados e dias de descanso remunerado.

**Aprovação de Férias Gestor**

O funcionário receberá um e-mail informando que suas férias foram aprovadas pelo Gestor.

**Aprovação de Férias DP**

O funcionário receberá um e-mail informando que suas férias foram aprovadas pelo DP.

**Reprovação de Férias**

O funcionário receberá um e-mail informando que suas férias foram reprovadas.

OBS: Para que estas opções funcionem corretamente, é necessário que o sistema esteja configurado para envio de e-mail.

**Etapa 6 - Supervisores**

**Estende código de equipes para os supervisores relacionados a este grupo de acesso**

Marcando esta opção, o supervisor poderá acessar todos os subordinados que pertencerem a sua equipe independente da seção.

Atenção:  
Ressaltamos que é imprescindível associar os subordinados através do campo "Cód. Equipe", em Cadastros | Funcionários | Identificação, campo RM Portal.

Observação 1:  
O supervisor desta equipe ainda estará vinculado seção. Para que um funcionário de outra seção se torne supervisor da equipe a que ele pertence será necessário que o mesmo se torne supervisor na sua seção de origem.  
Observação 2:  
O supervisor visualizará apenas os subordinados constantes dentro da mesma coligada no qual está localizado.  
Observação 3:  
Independente da parametrização, os subordinados locados ou não na mesma seção sempre serão validados através do "Cód. Equipe", em Cadastro | Funcionários | Identificação, campo RM Portal.

Observação 4:  
Quando o funcionário estiver vinculado a uma equipe, ao realizar a sugestão de férias, o sistema irá enviar o e-mail de sugestão de férias para o chefe/supervisor da equipe que o funcionário  estiver vinculado.

**Listagem de Subordinados no Portal NÃO traz por default todos os detalhes do subordinado na listagem (carregamento mais rápido)**

Com este parâmetro marcado na visão de subordinados não será apresentado todos os dados do funcionário, isso fará com que o carregamento seja mais rápido.

**Considerar o chefe da seção como subordinado direto mesmo não estando alocado naquela seção**

Com este parâmetro marcado a visualização de subordinados no portal levará os chefes da seção como subordinados diretos, apenas se estiverem alocados nas mesmas.

Para habilitar/desabilitar o parâmetro acesse:  RM | RH | Folha de Pagamento | Configurações | Parâmetros | Parametrizador | 06 - Folha de Pagamento | 06.05 - RM Portal | Seleção do Grupo de Acesso | Parâmetro | Etapa 6 - RM Portal: Supervisores | Opção “Considerar o Chefe da Seção como subordinado direto mesmo não estando alocado naquela seção”

**Definição de Subordinado Direto:** Subordinados diretos são os funcionários que na hierarquia da tela de “Cadastro de Chefe/Supervisor“ respondem diretamente à um determinado chefe. Ou seja, que pertencem à própria seção da qual o chefe é responsável ou se pertencem à seções filhas que não possuem chefes cadastrados e ativos.

**Exemplificação do parâmetro "Considerar o chefe da seção como subordinado direto mesmo não estando alocado naquela seção" marcado:**

O chefe**“Funcionário A”** visualiza o “**Funcionário B”** como subordinado direto, pois este é chefe da seção 01.01, apesar de estar alocado na seção 02.01 e essa seção é filha da 01 da qual o Funcionário A é chefe. O “**Funcionário A**” visualiza o “**Funcionário C**” como subordinado indireto, pois este é chefe e está alocado na seção 01.01.01.

Visualização de tela "Cadastro de Chefe/Supervisor":

Visualização do "Funcionário A" no RM Portal:

**Exemplificação do parâmetro "Considerar o chefe da seção como subordinado direto mesmo não estando alocado naquela seção" desmarcado:**

O chefe**“Funcionário A”** NÃO visualiza o “**Funcionário B”** como subordinado direto, pois este está alocado na seção 02.01, apesar de ser chefe da 01.01. O “**Funcionário A**” visualiza o “**Funcionário****C**” como subordinado indireto, pois este está alocado na seção 01.01.01 e é subordinado do “**FUNCIONÁRIO B**”.

Visualização de tela "Cadastro de Chefe/Supervisor":

Visualização do "Funcionário A" no RM Portal:

**Considerar o chefe alocado na seção como subordinado direto**

Com este parâmetro marcado se um funcionário for chefe da mesma seção que ele está alocado, aparecerá para o chefe acima dele, como subordinado direto.

Exemplo:

Chapa 00001 – Chefe da seção 01.01

Chapa 00002 – Chefe da seção 01.01.02 e alocado na mesma seção (01.01.02)

Se a chapa 00001 acessar a Gestão de Férias, e o parâmetro estiver marcado, a chapa 00002 aparecerá para ele aprovar, porém nenhum outro funcionário alocado na seção 01.01.02 aparecerá.

Ao marcar o parâmetro “Considerar o chefe da seção como subordinado direto mesmo não estando alocado naquela seção”, este parâmetro será marcado automaticamente e ficará desabilitado.

**Considerar subordinados de todas as coligadas na tela de Subordinados e na de Gestão de Férias do Portal RH**

Marcando esta opção, a consulta de subordinados da tela de Subordinados e de Gestão de Férias considerará subordinados de todas as coligadas e não apenas da coligada do contexto.

**Ocultar Autônomos e Diretores na Gestão de Férias**

Ao marcar este parâmetro não serão apresentados os funcionários do tipo de funcionário 'A - Autônomo' e 'D - Diretor' na tela de Gestão de Férias.

**Exibir Subordinados Demitidos com Rescisão não Calculada.**

Ao marcar este parâmetro serão apresentados também os funcionários com rescisão cadastrada não calculada.

**Etapa 8 - Informe de Rendimentos**

Gera Informe via RM Reports: Caso marcado, habilitará o campo "Relatório do RM Reports", onde o usuário poderá selecionar um relatório para que seja gerado o Informe de Rendimentos

(Portal)
