---
content_hash: e7c8bef25a9ee52a00c53095f4692528e3a8972247cb128277455b4f6c13895a
fetched_at: '2026-06-29T00:09:29.188833+00:00'
page_id: '423938830'
product: rm
source: tdn-rm
title: Novidades da Versão 11.80 - Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938830
version: 4
---

11.82.28 - Cadastro de Centro de Custo

Adicionado o campo ' Responsável ' no cadastro de Centro de Custo.

11.82.28 - Diagnóstico de Rastreabilidade dos Lançamentos Contábeis

Evolução do módulo de rastreabilidade de lançamentos do produto TOTVS Gestão Contábil para que seja possível rastrear Lançamentos originados do produto TOTVS Gestão Financeira gerados antes do novo modelo de BackOffice.

11.82.28 - Lançamentos Contábeis

Melhorada a forma de exclusão de Lançamento/Partidas pela visão de Lançamentos Contábeis através da criação de um novo botão 'Excluir Lançamento Contábil' que passará a funcionar da seguinte forma: Quando uma partida estiver selecionada e for utilizado o botão X 'Excluir', somente a partida selecionada será excluída, e não mais todo o lançamento contábil. Quando uma partida estiver selecionada e for utilizado o novo botão 'Excluir Lançamento Contábil', o lançamento com todas as suas partidas serão excluídos e não somente a partida selecionada.

11.82.27 - Parâmetros do Sistema

Foram incluídos os parâmetros "Barrar Lançamento com centro de custo inativo" e "Permitir Lançamento com Centro de Custos inativos por módulo", ambos são responsáveis pela permissão ou não da inclusão de um lançamento com o centro de custo inativo. Sendo que o segundo possibilita a seleção de módulos para a permissão e somente fica habilitado se o primeiro também estiver.

11.82.25 - Lançamentos Contábeis

Implementado no sistema TOTVS Gestão Contábil o recurso de Acesso Rápido à tela de Partida do Lançamento Contábil, disponível dentro do menu 'Lançamentos|Manutenção de Lançamentos', ou para quem acessa o sistema pela nova interface que dá acesso a todos os seguimentos (RM.EXE), através do menu 'Escrituração Contábil|Lançamentos|Acesso Rápido'.

11.82.25 - Diagnóstico de Rastreabilidade dos Lançamentos Contábeis

Implementada a ferramenta "Diagnóstico de Rastreabilidade dos Lançamentos Contábeis" que tem como objetivo diagnosticar e validar o vínculo das operações financeiras X contábeis e também identificar duplicidade dos lançamentos contábeis com relação à sua origem.

11.82.25 - Preferências de Usuários

* Implementado o campo 'Documento' em Fixação de Campos para inclusão de novas partidas.
* Criada nova preferência de usuário: "Ao salvar a Partida salvar automaticamente o Lançamento Contábil".

11.82.25 - Parâmetros do Sistema

Incluído novo parâmetro do sistema 'Definir ordem de gravação das partidas' responsável por parametrizar a ordem em que as partidas serão gravadas no banco, tanto para lançamentos que forem incluídos diretamente no TOTVS Gestão Contábil como para lançamentos originados em módulos externos ao da contabilidade.

11.82.25 - Filtro por Usuário

Disponibilizadas as tabelas CLANCAMENTO e CPARTIDA na utilização de filtros por usuário disponível dentro do cadastro de usuários.

11.82.25 - Plano de Contas Gerencial

Adicionado o processo "Copiar Contas Gerencias entre Coligadas", responsável por fazer a cópia da(s) conta(s) gerencial(is) de uma coligada para outra.

11.81.15 - Agrupamento de Lançamentos

Implementada a opção de Filtro Genérico no processo de agrupamento de lançamentos, possibilitando a criação de filtros para seleção dos lançamentos/partidas para o processo, podendo ser utilizado um leque amplo de opções. No decorrer do agrupamento o sistema passará a mostrar o progresso da sua execução.

11.81.10 - Tarefas

Criado o serviço de exclusão de Lançamentos de Estornos e de Lançamentos Estornados através do recurso de solicitação de Tarefa. A solicitação desta Tarefa deve ser feita diretamente no módulo que originou a contabilização. As Tarefas solicitadas são enviadas para o TOTVS Gestão Contábil onde poderão ser executadas ou canceladas. Se a solicitação da Tarefa for executada, os lançamentos de estornos e os estornados serão excluídos da base. Para utilizar este serviço os módulos externos de onde os lançamentos contábeis são originados devem estar devidamente preparados para utilizá-lo.

11.81.10 - Parâmetros do Sistema

* Criado o parâmetro 'Aplica Contra Partida Automaticamente na Inclusão de Lançamentos '. Se este parâmetro for ativado, o sistema passará a preencher automaticamente a Contra Partida nos lançamentos contábeis incluídos diretamente no TOTVS Gestão Contábil ou originados em módulo externo ao da contabilidade, desde que os lançamentos possuam a contabilização da seguinte forma: Uma partida somente com o Débito e outra somente com o Crédito: a Contra Partida da partida a crédito será preenchida com a conta lançada a débito, e vice-versa. Uma partida somente com o Débito para várias partidas a Crédito: a Contra Partida das partidas a crédito serão preenchidas com a conta lançada a débito. Uma partida somente com o Crédito para várias partidas a Débito: a Contra Partida das partidas a débito serão preenchidas com a conta lançada a crédito. Atenção: Caso se altere um lançamento e o salve esta regra não será aplicada novamente e a alteração do campo Contra Partida, se necessária, deverá ser feita de forma manual.
* Criado o parâmetro 'Não salvar lançamentos com diferenças entre Débitos X Créditos '. Se este parâmetro for ativado, o sistema não permitirá que um lançamento seja salvo enquanto houver, no lançamento, diferença entre o total de débitos e créditos.

11.81.10 - Agrupamento de Lançamentos

Implementado no processo de Agrupamento de Lançamentos o filtro para seleção de Contas Contábeis. Ao selecionar a opção para utilização deste filtro, o sistema habilita dois filtros de contas, um para Débito e outro para Crédito de acordo com a forma de agrupamento escolhido anteriormente. Estes filtros já vêm preenchidos com as contas contábeis utilizadas no débito ou no crédito conforme o filtro, podendo o usuário incluir ou excluir contas.

11.81.10 - Plano de Contas Paralelo

Melhoria no processo de "Validação da Associação do Plano Paralelo para o SPED Contábil" sendo adicionada a opção "Validar Conta Contábil sem movimentação, que possui o campo 'Natureza da Conta para emissão do SPED' preenchido e não possui associação com Plano de Contas Paralelo" permitindo ao sistema listar as Contas Contábeis que não possuem movimentação, possuem o campo 'Natureza da Conta para emissão do SPED' preenchido e não possuem associação com Plano de Contas Paralelo.

11.81.10 - Alteração Global do Período para Manutenção dos Lançamentos Contábeis

Criada neste processo a opção "Ativar Filtro por Coligada". Esta opção irá habilitar mais uma etapa no processo, aonde o usuário poderá definir para quais coligadas deseja que as configurações sejam aplicadas simultaneamente.

11.81.10 - Consistência de Lançamentos

Implementada nova consistência que irá verificar 'Lotes que possuem partidas com referências repetidas'. Evoluído o processo referente à consistência de 'Lançamentos que possuem rateios com valor 0 (zero)'.

11.80.1 - Parâmetros do Sistema

* Por motivo de padronização dos aplicativos da linha RM, os 'Parâmetros do Sistema' que ficavam disponíveis dentro do menu Utilitários ficarão agora disponíveis dentro do menu Ambiente.
* Descontinuados os parâmetros do sistema "Barrar lançamentos com Centro de Custo inativo" e "Barrar lançamentos com Departamento inativo", pois na tela de inclusão de lançamentos só é permitida a utilização de Centro de Custo e/ou Departamento que estiverem Ativos.
* Criado o parâmetro do sistema 'Aplicar regras de validação de lançamentos na Integração de Lotes'. Este parâmetro será aplicado na Integração de Lotes e só ficará disponível se o parâmetro 'Usa regra de validação de lançamentos' estiver habilitado. Marcando-se este novo parâmetro, no momento da Integração de Lotes o sistema fará a validação das regras de inclusão de lançamentos presentes nas Fórmulas e Amarrações de Lançamentos ativas e só fará a integração de lotes se os lançamentos estiverem satisfazendo a estas fórmulas e amarrações ativas. Com este parâmetro desmarcado, as fórmulas e amarrações existentes não serão validadas pelo processo de Integração de Lotes.
* Criado o parâmetro do sistema 'Aplicar regra de validação de lançamentos no Agrupamento de Lançamentos'. Este parâmetro será aplicado na execução de Agrupamento de Lançamentos e só ficará disponível se o parâmetro 'Usa regra de validação de lançamentos' estiver habilitado. Marcando-se este novo parâmetro, no momento da execução do Agrupamento de Lançamentos, além das regras inerentes a este processo, o sistema fará também a validação das regras de inclusão de lançamentos presentes nas Fórmulas e Amarrações de Lançamentos ativas e só fará o agrupamento dos lançamentos que estiverem satisfazendo às fórmulas e amarrações existentes. Com este parâmetro desmarcado, as fórmulas e amarrações existentes não serão validadas pelo processo de Agrupamento de Lançamentos. Vale ressaltar que, dependendo do volume de informações da base de dados, executar o processo de Agrupamento de Lançamentos com este novo parâmetro habilitado, pode comprometer a performance do processo!

11.80.1 - Cadastro de Lotes

Disponibilizadas na visão de Lotes, três novas colunas: Total Débitos, Total Créditos e Valor Soma. Para que estas colunas fiquem visíveis na tela de visão de Lotes é necessário que você marque a exibição de tais colunas. Para isto, na tela de visão de Lotes, clique no ícone Configurar Colunas e marque as colunas que desejar que sejam apresentadas na visão de Lotes.

11.80.1 - Acessar lotes de outros módulos

Ao acessar os lançamentos de um lote que teve origem em outro módulo, o sistema não irá solicitará mais a digitação de usuário/senha nas seguintes situações:

1- Se o usuário logado for um usuário supervisor, ou;

2- Se o usuário logado tiver permissão para manutenção (inclusão ou edição ou exclusão) nos lançamentos do lote, ou;

3- Se o usuário logado tiver permissão para acessar lotes de outros módulos. Se o usuário logado não atender a nenhuma destas condições, o sistema irá então solicitar a digitação de usuário/senha com alguma destas características.

11.80.0 - Agrupamento de Lançamentos

Evoluído o processo de Agrupamento de Lançamentos Contábeis para permitir que seja informado filtro por Filial, filtro de Contas Contábeis e também que seja possível informar um Documento/Complemento para as partidas que serão agrupadas dentro do lote contábil, mantendo, entretanto, inalteradas as informações destes campos ao consultar as partidas nos sistemas de origem.

11.80.0 - Parâmetros do Sistema

Criado o parâmetro do sistema 'Aplicar regra de validação de lançamentos no Agrupamento de Lançamentos'. Este parâmetro será aplicado na execução de Agrupamento de Lançamentos e só ficará disponível se o parâmetro 'Usa regra de validação de lançamentos' estiver habilitado. Marcando-se este novo parâmetro, no momento da execução do Agrupamento de Lançamentos, além das regras inerentes a este processo, o sistema fará também a validação das regras de inclusão de lançamentos presentes nas Fórmulas e Amarrações de Lançamentos ativas e só fará o agrupamento dos lançamentos que estiverem satisfazendo às fórmulas e amarrações existentes. Com este parâmetro desmarcado, as fórmulas e amarrações existentes não serão validadas pelo processo de Agrupamento de Lançamentos. Vale ressaltar que, dependendo do volume de informações da base de dados, executar o processo de Agrupamento de Lançamentos com este novo parâmetro habilitado, pode comprometer a performance do processo!

11.80.0 - Recálculo do Segundo Valor

O Recálculo do Segundo Valor foi migrado para a plataforma .NET. Este processo é responsável por fazer o recálculo do 2º Valor, levando-se em consideração o Valor do Lançamento, a Data e a Cotação cadastrada para a Moeda utilizada no processo.

11.80.0 - Associação Dinâmica do Centro de Custo/Conta Gerencial ao Plano Paralelo

Implementado processo responsável por fazer automaticamente a associação dos centros de custos (ou contas gerenciais conforme utilização indicada nos Parâmetros do Sistema/Rotinas Legais) utilizados nos lançamentos contábeis às respectivas contas contábeis movimentadas e que estejam associadas ao Plano Referencial da Receita - Plano Paralelo.

11.80.0 - Visualização das Associações das Contas Contábeis com Planos Paralelos

Funcionalidade implementada, responsável por identificar e mostrar individualmente todas as associações existentes da conta contábil selecionada ao(s) Plano(s) Paralelo(s)/Conta(s) Paralela(s).

11.80.0 - Classificação Automática da Natureza da Conta Contábil

Processo implementado no sistema com o objetivo de otimizar o preenchimento do campo 'Natureza da conta para emissão do SPED'. Informando-se o grupo de contas e a Natureza da conta para emissão do SPED, o sistema preenche automaticamente o campo 'Natureza da conta para emissão do SPED' de todas as sub-contas pertencentes ao grupo informado com a Natureza também informada na execução do processo.

11.80.0 - LOG de execução do SPED Contábil

No final da geração do SPED Contábil o sistema apresentará um LOG de execução, indicando todas as ações realizadas para a geração do SPED Contábil e o tempo gasto em cada uma.

11.80.0 - Upload/Download de arquivos na geração do SPED Contábil

Implementados os recursos de Upload para Razão Auxiliar e Arquivos Adicionais-J800 e Download do arquivo digital gerado. Estes recursos visam otimizar a utilização da memória do computador evitando travamento na execução do processo, uma vez que o Upload leva parcialmente os arquivos manipulados para o servidor de aplicação liberando a memória e o Download baixa o arquivo do servidor para o local indicado.

11.80.0 - Histórico de Fechamento na geração do SPED Contábil

Foi disponibilizada uma nova opção na geração do SPED Contábil para facilitar a identificação do(s) Histórico(s) de Fechamento(s) utilizado(s) na apuração de resultado do período. Agora é possível indicar o código da estrutura de Transferência de Grupos Contábeis utilizada para a apuração de resultado do período para que o sistema faça a leitura e indique automaticamente o(s) Histórico(s) de Fechamento(s) utilizado(s). Se preferir, ainda é possível indicar manualmente o(s) código(s) do(s) Histórico(s) de Fechamento(s) utilizado(s) e suas respectivas datas, bastando para isto clicar no link correspondente.

11.80.0 - Rastrear origem do lançamento contábil

Este recurso que mostra graficamente a origem do lançamento contábil foi evoluído. À medida que os aplicativos da linha RM forem migrando para o BackOffice eles passarão a enviar informações para que a origem do lançamento possa ser rastreada e visualizada de forma gráfica. Hoje este recurso já está disponível para lançamentos originados do TOTVS Gestão de Estoque, Compras e Faturamento, TOTVS Educacional e TOTVS Gestão Fiscal.
