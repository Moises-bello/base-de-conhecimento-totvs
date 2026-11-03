---
content_hash: 5703b35bc1a234d955c6ef475165729a9d1f0d2eefdb887e2356395c4ed1489f
fetched_at: '2026-06-29T00:10:08.717179+00:00'
page_id: '452719565'
product: rm
source: tdn-rm
title: Pasta Identificação - Requisição de Desligamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719565
version: 3
---

**Pasta Identificação - Requisição de Desligamento**

Na pasta Identificação os seguintes dados devem ser informados:

**Número -** Gerado automaticamente e com valor único.

**Status -** Será apresentado logo após a abertura da requisição como  "Pendente". Este campo será alterado a medida que a requisição for avançando no fluxo de aprovações assumindo os valores parametrizados para cada etapa.

Para verificar a parametrização acesse: Configurações | Tipos de Requisições. Os status que poderão ser definidos pelo fluxo de aprovação são "Em Andamento", "Aprovado" e "Reprovado". Os status "Suspenso" e "Cancelado" serão definidos conforme a utilização do processo "Suspender requisição " e "Cancelar Requisição" respectivamente.

O status "Concluído" será determinado quando todas as vagas aprovadas na requisição forem utilizadas, seja nos processos relacionados a efetivação da admissão de candidatos ou nas alterações dos dados funcionais de funcionário(s). Quando a requisição adquirir o status "Aprovado" significa que a mesma ficará disponível para utilização no Totvs Gestão de Pessoas, nos processos relacionados à Seleção de Pessoal e Admissão, conforme utilização do parâmetro relacionado à requisição.

**Os status das requisições são representados pelas cores:**

Aprovada – cor verde

Cancelada – cor preta

Concluída – cor roxa

Em Andamento – cor amarela

Pendente – cor laranja

Reprovada – cor vermelha

Suspensa – cor azul

**Nome do Aprovador atual -** Este campo não é editável e apresentará o nome do aprovador atual da requisição, ou seja, o responsável atual pela requisição, conforme definição do fluxo de aprovações.

**Conclusão -** Irá apresentar a data que a requisição foi concluída, ou seja, a data de efetivação da demissão do funcionário ou a data de demissão do ex-funcionário vinculado.

**Requisitante -** Somente podem ser selecionados chefes da coligada na qual o usuário do Totvs Gestão de Pessoas esteja logado. Esta informação poderá ser modificada enquanto a requisição estiver pendente ou se nenhum parecer tiver sido cadastrado. Caso a requisição seja aberta pelo "Totvs RM Portal" este campo exibirá o nome do usuário logado não podendo ser modificado.

**Listar apenas Ex-Funcionários -** Esta opção deverá ser marcada caso queira registrar a demissão de um ex-funcionário. Ao selecionar um ex-funcionário, os campos "Previsão", "Dias de aviso", "Tipo de demissão" e "Motivo da demissão" serão preenchidos com os respectivos dados da rescisão do funcionário, não podendo ser alterados. Essa requisição será gerada com o status "Concluída".

**Dica:**

Ao selecionar o flag "Listar somente ex-Funcionários" serão exibidos os ex-funcionários desligados à partir da competência atual.

**Funcionário -** Para vinculação na requisição de desligamento serão exibidos os funcionários subordinados ao requisitante e ex-funcionários que já foram subordinados ao requisitante. Se o funcionário selecionado for membro da CIPA, a requisição poderá ser criada, porém a sua conclusão mediante a demissão do funcionário só ocorrerá após o término do período de estabilidade conforme rege a NR 5. Ao selecionar um ex-funcionário, será permitida a criação automática de requisição de substituição com status "Pendente" sem a necessidade de aprovação prévia da requisição pai.

Ao vincular um funcionário PNE à requisição de desligamento o gestor do RH será notificado por e-mail sobre esta demissão, o objetivo deste e-mail é ressaltar a necessidade do cumprimento das cotas legais relacionadas ao número mínimo de funcionários portadores de necessidades especiais que devem ser admitidos em uma empresa. Este campo poderá ser alterado enquanto a requisição estiver pendente e desde que nenhum parecer tenha sido cadastrado.

**Previsão -** Por definição, ser for selecionado um funcionário, será exibida a data atual podendo ser alterada para outra data prevista para a demissão solicitada; caso tenha sido selecionado um ex-funcionário, será exibida a data da efetivação da demissão.

**Dias de aviso -** Por definição, ser for selecionado um funcionário, o valor para dias de aviso será 30 (trinta) podendo ser alterado para outro valor maior ou igual a 0(zero). Ccaso tenha sido selecionado um ex-funcionário, será exibida o número de dias de aviso concedido.

**Tipo de demissão -** Se a pessoa selecionada for um ex-funcionário será exibido, neste campo, o tipo de demissão realizada, caso seja um funcionário deve-se definir qual será o tipo de demissão. Para verificar os tipos de demissões disponíveis acesse: Serviços Globais | Administração | Tabela Dinâmica | Tipo de demissão.

**Motivo da demissão -** Se a pessoa selecionada for um ex-funcionário será exibido, neste campo, o motivo da demissão realizada, caso seja um funcionário deve-se definir qual será este motivo para a demissão. Para verificar os motivos de demissões disponíveis acesse: Serviços Globais | Administração | Tabela Dinâmica | Motivo de demissão.

**Justificativa -** Ao solicitar uma demissão deverá ser informada uma justificativa para tal solicitação. Este campo poderá ser alterado enquanto a requisição estiver pendente e se nenhum parecer tiver sido cadastrado.

**Gerar Substituição -** Esta opção deverá ser marcada se for necessário manter o número de vagas existentes para a respectiva lotação do funcionário que está sendo demitido; caso esta opção não seja selecionada e se houver parametrização para o controle de lotação, o sistema reduzirá o número de vagas disponíveis ao concluir a requisição, este procedimento será o mesmo caso a pessoa vinculada à requisição seja um ex-funcionário. A requisição de substituição será baseada nos dados da requisição de desligamento que lhe der origem (requisição pai) sendo criada quando esta requisição for aprovada, e terá, inicialmente, o status "Em andamento".

Para funcionário PNE a requisição de substituição, caso seja criada, no momento da sua utilização validará se a pessoa beneficiada também é PNE.

**Observações**

Enquanto a requisição estiver com status "Pendente" os dados desta pasta poderão ser alterados, caso o status seja "Em andamento" as alterações somente poderão ser feitas através da inclusão de pareceres.

Ao editar uma requisição que esteja com status "Em andamento", o sistema exibe, no lugar dos dados originais da requisição, os dados correspondentes ao último parecer registrado de modo a posicionar o aprovador atual sobre as mudanças mais recentes. Somente se não existir nenhum parecer anterior, o sistema exibirá os dados originais da requisição.

Requisições em andamento, suspensas, canceladas, aprovadas, reprovadas ou concluídas não podem ser excluídas. Apenas requisições pendentes poderão ser excluídas!
