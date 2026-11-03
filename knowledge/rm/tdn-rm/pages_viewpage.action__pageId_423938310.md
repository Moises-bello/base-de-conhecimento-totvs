---
content_hash: 991489c0e4e7a31e9867591526fcda4ebd18b338483d5c18a403ed809d388a1b
fetched_at: '2026-06-29T00:09:26.520646+00:00'
page_id: '423938310'
product: rm
source: tdn-rm
title: Novidades da Versão 11.50.0 - Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938310
version: 4
---

**11.52.57 –** **Integração de Lotes**

Foi criado no processo de integração de lote, a opção *"Excluir Lote(s) após o mesmo ser integrado"*. Esta opção deve ser marcada caso deseje excluir o lote após a integração. Se esta opção não for marcada, o lote não será excluído. É importante lembrar que os Lotes que possuírem parametrização fixa em módulos externos ao da contabilidade, como no TOTVS Gestão Financeira, Gestão Patrimonial etc., em nenhuma hipótese serão excluídos pelo sistema após a sua integração.  
   
**11.52.55 -** **Diagnóstico de Rastreabilidade dos Lançamentos Contábeis**

Implementada a ferramenta "Diagnóstico de Rastreabilidade dos Lançamentos Contábeis" que tem como objetivo diagnosticar e validar o vínculo das operações financeiras X contábeis e também identificar duplicidade dos lançamentos contábeis com relação à sua origem.  
   
**11.52.50 -** **Plano de Contas Gerencial**

Adicionado o processo "Copiar Contas Gerencias entre Coligadas", responsável por fazer a cópia da(s) conta(s) gerencial(is) de uma coligada para outra.

**11.52.50 -** **Preferências de Usuários**

Implementado o campo 'Documento' em Fixação de Campos para inclusão de novas partidas.   
   
**11.52.50 - Parâmetros do sistema**

Incluído novo parâmetro do sistema 'Definir ordem de gravação das partidas' responsável por parametrizar a ordem em que as partidas serão gravadas no banco, tanto para lançamentos que forem incluídos diretamente no TOTVS Gestão Contábil como para lançamentos originados em módulos externos ao da contabilidade**.**  
   
**11.51.45 -** **Alteração Global do Período para Manutenção dos Lançamentos Contábeis**

Criada neste processo a opção "Ativar Filtro por Coligada". Esta opção irá habilitar mais uma etapa no processo, aonde o usuário poderá definir para quais coligadas deseja que as configurações sejam aplicadas simultaneamente.  
   
**11.51.45 - Parâmetros do Sistema**

* Criado o parâmetro 'Aplica Contra Partida Automaticamente na Inclusão de Lançamentos '. Se este parâmetro for ativado, o sistema passará a preencher automaticamente a Contra Partida nos lançamentos contábeis incluídos diretamente no TOTVS Gestão Contábil ou originados em módulo externo ao da contabilidade, desde que os lançamentos possuam a contabilização da seguinte forma: Uma partida somente com o Débito e outra somente com o Crédito: a Contra Partida da partida a crédito será preenchida com a conta lançada a débito, e vice-versa. Uma partida somente com o Débito para várias partidas a Crédito: a Contra Partida das partidas a crédito serão preenchidas com a conta lançada a débito. Uma partida somente com o Crédito para várias partidas a Débito: a Contra Partida das partidas a débito serão preenchidas com a conta lançada a crédito. Atenção: Caso se altere um lançamento e o salve esta regra não será aplicada novamente e a alteração do campo Contra Partida, se necessária, deverá ser feita de forma manual.
* Criado o parâmetro 'Não salvar lançamentos com diferenças entre Débitos X Créditos '. Se este parâmetro for ativado, o sistema não permitirá que um lançamento seja salvo enquanto houver, no lançamento, diferença entre o total de débitos e créditos.

**11.51.45 -** **Agrupamento de lançamentos**

Implementada a opção de Filtro Genérico no processo de agrupamento de lançamentos, possibilitando a criação de filtros para seleção dos lançamentos/partidas para o processo, podendo ser utilizado um leque amplo de opções. No decorrer do agrupamento o sistema passará a mostrar o progresso da sua execução.  
   
**11.51.45 -** **Importação de Dados**

A rotina de importação de dados por texto, foi migrada para Plataforma .NET. Para realizar a importação de dados no TOTVS Gestão Contábil, será utilizada a ferramenta "RM Conector", que facilita a execução destas operações de forma dinâmica, utilizando a própria regra dos cadastros da contabilidade.  
   
**11.51.40 -** **Tarefas**

Disponibilizado no recurso de Tarefa a opção do tipo 2 'Exclusão de Lançamentos de Estorno e Estornados do Lote Zero'. Este tipo de tarefa exclui apenas os Lançamentos Contábeis de Estorno e Estornados. Para utilizar este serviço os módulos que geram as contabilização devem disponibilizar o processo de solicitação de Tarefa para o tipo 2.  
   
**11.50.25 - Parâmetros do Sistema**

Criado o parâmetro do sistema 'Aplicar regras de validação de lançamentos na Integração de Lotes'. Este parâmetro será aplicado na Integração de Lotes e só ficará disponível se o parâmetro 'Usa regra de validação de lançamentos' estiver habilitado. Marcando-se este novo parâmetro, no momento da Integração de Lotes o sistema fará a validação das regras de inclusão de lançamentos presentes nas Fórmulas e Amarrações de Lançamentos ativas e só fará a integração de lotes se os lançamentos estiverem satisfazendo a estas fórmulas e amarrações ativas. Com este parâmetro desmarcado, as fórmulas e amarrações existentes não serão validadas pelo processo de Integração de Lotes.  
   
**11.50.25 -****Acessar lotes de outros módulos**

Ao acessar os lançamentos de um lote que teve origem em outro módulo, o sistema não irá solicitará mais a digitação de usuário/senha nas seguintes situações:

1 - Se o usuário logado for um usuário supervisor, ou

2 - Se o usuário logado tiver permissão para manutenção (inclusão ou edição ou exclusão) nos lançamentos do lote, ou

3 - Se o usuário logado tiver permissão para acessar lotes de outros módulos.

Se o usuário logado não atender a nenhuma destas condições, o sistema irá então solicitar a digitação de usuário/senha com alguma destas características.  
   
**11.50.25 -** **Consistência de Lançamentos**

Implementada nova consistência que irá verificar 'Lotes que possuem partidas com referências repetidas'. Evoluído o processo referente à consistência de 'Lançamentos que possuem rateios com valor 0 (zero)'.  
   
**11.50.25 -** **Agrupamento de Lançamentos**

Implementado no processo de Agrupamento de Lançamentos o filtro para seleção de Contas Contábeis. Ao selecionar a opção para utilização deste filtro, o sistema habilita dois filtros de contas, um para Débito e outro para Crédito de acordo com a forma de agrupamento escolhido anteriormente. Estes filtros já vêm preenchidos com as contas contábeis utilizadas no débito ou no crédito conforme o filtro, podendo o usuário incluir ou excluir contas.  
   
**11.50.20 -** **Agrupamento de Lançamentos**

Evoluído o processo de Agrupamento de Lançamentos Contábeis para permitir que seja informado filtro por Filial, filtro de Contas Contábeis e também que seja possível informar um Documento/Complemento para as partidas que serão agrupadas dentro do lote contábil, mantendo, entretanto, inalteradas as informações destes campos ao consultar as partidas nos sistemas de origem.  
   
**11.50.20 - Associação Dinâmica do Centro de Custo/Conta Gerencial ao Plano Paralelo**

Implementado processo responsável por fazer automaticamente a associação dos centros de custos (ou contas gerenciais conforme utilização indicada nos Parâmetros do Sistema/Rotinas Legais) utilizados nos lançamentos contábeis às respectivas contas contábeis movimentadas e que estejam associadas ao Plano Referencial da Receita - Plano Paralelo.  
   
**11.50.20 - Visualização das Associações das Contas Contábeis com Planos Paralelos**

Funcionalidade implementada, responsável por identificar e mostrar individualmente todas as associações existentes da conta contábil selecionada ao(s) Plano(s) Paralelo(s)/Conta(s) Paralela(s).  
   
**11.50.20 - Classificação Automática da Natureza da Conta Contábil**

Processo implementado no sistema com o objetivo de otimizar o preenchimento do campo 'Natureza da conta para emissão do SPED'. Informando-se o grupo de contas e a Natureza da conta para emissão do SPED, o sistema preenche automaticamente o campo 'Natureza da conta para emissão do SPED' de todas as sub-contas pertencentes ao grupo informado com a Natureza também informada na execução do processo.  
   
**11.50.20 - LOG de execução do SPED Contábil**

No final da geração do SPED Contábil o sistema apresentará um LOG de execução, indicando todas as ações realizadas para a geração do SPED Contábil e o tempo gasto em cada uma.  
   
**11.50.20 - Upload/Download de arquivos na geração do SPED Contábil**

Implementados os recursos de Upload para Razão Auxiliar e Arquivos Adicionais-J800 e Download do arquivo digital gerado. Estes recursos visam otimizar a utilização da memória do computador evitando travamento na execução do processo, uma vez que o Upload leva parcialmente os arquivos manipulados para o servidor de aplicação liberando a memória e o Download baixa o arquivo do servidor para o local indicado.  
   
**11.50.20 - Histórico de Fechamento na geração do SPED Contábil**

Foi disponibilizada uma nova opção na geração do SPED Contábil para facilitar a identificação do(s) Histórico(s) de Fechamento(s) utilizado(s) na apuração de resultado do período. Agora é possível indicar o código da estrutura de Transferência de Grupos Contábeis utilizada para a apuração de resultado do período para que o sistema faça a leitura e indique automaticamente o(s) Histórico(s) de Fechamento(s) utilizado(s). Se preferir, ainda é possível indicar manualmente o(s) código(s) do(s) Histórico(s) de Fechamento(s) utilizado(s) e suas respectivas datas, bastando para isto clicar no link correspondente.  
   
**11.50.20 - Parâmetros do Sistema**

* Por motivo de padronização dos aplicativos da linha RM, os 'Parâmetros do Sistema' que ficavam disponíveis dentro do menu Utilitários ficarão agora disponíveis dentro do menu Ambiente.
* Descontinuados os parâmetros do sistema "Barrar lançamentos com Centro de Custo inativo" e "Barrar lançamentos com Departamento inativo", pois na tela de inclusão de lançamentos só é permitida a utilização de Centro de Custo e/ou Departamento que estiverem Ativos.

**11.50.20 -** **Cadastro de Lotes**

Disponibilizadas na visão de Lotes, três novas colunas: 'Total Débitos', 'Total Créditos' e 'Valor Soma'. Para que estas colunas fiquem visíveis na tela de visão de Lotes é necessário que você marque a exibição de tais colunas. Para isto, na tela de visão de Lotes, clique no ícone Configurar Colunas e marque as colunas que desejar que sejam apresentadas na visão de Lotes.  
   
**11.50.20 - Parâmetros do Sistema**

Criado o parâmetro do sistema 'Aplicar regra de validação de lançamentos no Agrupamento de Lançamentos'. Este parâmetro será aplicado na execução de Agrupamento de Lançamentos e só ficará disponível se o parâmetro 'Usa regra de validação de lançamentos' estiver habilitado. Marcando-se este novo parâmetro, no momento da execução do Agrupamento de Lançamentos, além das regras inerentes a este processo, o sistema fará também a validação das regras de inclusão de lançamentos presentes nas Fórmulas e Amarrações de Lançamentos ativas e só fará o agrupamento dos lançamentos que estiverem satisfazendo às fórmulas e amarrações existentes. Com este parâmetro desmarcado, as fórmulas e amarrações existentes não serão validadas pelo processo de Agrupamento de Lançamentos. Vale ressaltar que, dependendo do volume de informações da base de dados, executar o processo de Agrupamento de Lançamentos com este novo parâmetro habilitado, pode comprometer a performance do processo!   
   
**11.50.0 -** **Lançamentos Periódicos**

A rotina de Agendamento de Lançamentos que era executada em modo Server foi descontinuada. Foi criado um conversor para converter, se achar conveniente, as antigas estruturas para dentro do cadastro de Lançamentos Periódicos. Se desejar, os antigos agendamentos de lançamentos também poderão ser convertidos. Este conversor será apresentado somente se existirem Agendamento de Lançamentos antigos e somente usuário Supervisor terá permissão para executá-lo.  
Quem trabalha com o JobServer configurado para executar em modo 3 Camadas pode contar com o recurso global de Agendamento, e agendar a execução do processo de Geração de Lançamentos Periódicos para outro momento, podendo ainda criar recorrências ou repetições para estes agendamentos.

**11.50.0 - Evolução dos cadastros de** **Preferências de Usuário** **e do** **Período para Manutenção de Lançamentos**

* O cadastro de Preferência de Usuários foi migrado para a nova plataforma .NET, ficando muito mais intuitivo.
* O Período para Manutenção de Lançamentos Contábeis também foi migrado e está disponível dentro dos *Anexos* do próprio cadastro de usuários, ficando este *Anexo* disponível somente para usuários Supervisores.
* O processo para Alteração Global do Período para Manutenção que permite definir e/ou alterar o período para manutenção de lançamentos contábeis para um ou vários usuários simultaneamente, também foi migrado, sendo que, independente se o usuário for supervisor ou não supervisor, a permissão de acesso a este processo deve ser definida no *Perfil* associado ao usuário.

**11.50.0 -** **Inativação/Ativação de Contas Contábeis**

Criado processo de Inativação/Ativação de Contas Contábeis que possibilita inativar ou ativar contas contábeis. As contas inativadas não poderão ser utilizadas em novas movimentações contábeis, porém os saldos e os registros das movimentações anteriormente realizadas nestas contas serão mantidos.

**11.50.0 -** **Pré-Validador do SPED Contábil**

Implementado processo responsável por fazer uma pré-validação nos dados que serão gerados para a Escrituração Contábil Digital com o objetivo de apontar possíveis inconsistências para que estas possam ser acertadas antes da geração propriamente dita do SPED Contábil, otimizando assim tempo e procedimentos no envio dos dados para o SPED.

**11.50.0 - Parâmetros do Sistema**

Adicionado no processo de parametrização do sistema Gestão Contábil, informações sobre a última alteração realizada na Data de Fechamento, mostrando o usuário/data responsável pela última modificação.

**11.50.0 -** **Lançamentos contábeis**

Ajustada a tela de visão/edição de lançamentos para que seja exibida a diferença entre Débitos x Créditos da seguinte forma: - Quando houver partidas selecionadas será calculada apenas a diferença entre Débitos x Créditos das partidas selecionadas. - Quando não houver partidas selecionadas será calculada a diferença entre todas as partidas da tela de visão/edição.

**11.50.0 - Outras atualizações:**

Evolução no Relatório de Consistência de Lançamentos
