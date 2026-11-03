---
content_hash: e41542bc36e73b6c0475bedcd123391a8b198abdf53a1f7e842bda91b0fce83a
fetched_at: '2026-06-29T00:09:28.666130+00:00'
page_id: '423938742'
product: rm
source: tdn-rm
title: Novidades da Versão 11.40.0 - Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938742
version: 7
---

**11.40.75 – Parâmetros do Sistema**  
Incluido novo parâmetro do sistema 'Definir ordem de gravação das partidas' responsável por parametrizar a ordem em que as partidas serão gravadas no banco, tanto para lançamentos que forem incluídos diretamente no TOTVS Gestão Contábil como para lançamentos originados em módulos externos ao da contabilidade.

**11.40.70 -**

Disponibilizadas as tabelas CLANCAMENTO e CPARTIDA na utilização de filtros por usuário disponível dentro do cadastro de usuários.

**11.40.70 –** **Plano de Contas Gerencial**

Adicionado o processo "Copiar Contas Gerencias entre Coligadas", responsável por fazer a cópia da(s) conta(s) gerencial(is) de uma coligada para outra.

**11.40.70 –** **Plano de Contas Paralelo**

Melhoria no processo de "Validação da Associação do Plano Paralelo para o SPED Contábil" sendo adicionada a opção "Validar Conta Contábil sem movimentação, que possui o campo 'Natureza da Conta para emissão do SPED' preenchido e não possui associação com Plano de Contas Paralelo" permitindo ao sistema listar as Contas Contábeis que não possuem movimentação, possuem o campo 'Natureza da Conta para emissão do SPED' preenchido e não possuem associação com Plano de Contas Paralelo.

**11.40.45 -** **Cadastro de Lotes**

Disponibilizadas na visão de Lotes, três novas colunas: 'Total Débitos', 'Total Créditos' e 'Valor Soma'. Para que estas colunas fiquem visíveis na tela de visão de Lotes é necessário que você marque a exibição de tais colunas. Para isto, na tela de visão de Lotes, clique no ícone Configurar Colunas e marque as colunas que desejar que sejam apresentadas na visão de Lotes.

**11.40.45 - Parâmetros do Sistema**

Criado o parâmetro do sistema '*Aplicar regras de validação de lançamentos na Integração de Lotes'*. Este parâmetro será aplicado na Integração de Lotes e só ficará disponível se o parâmetro 'Usa regra de validação de lançamentos' estiver habilitado. Marcando-se este novo parâmetro, no momento da Integração de Lotes o sistema fará a validação das regras de inclusão de lançamentos presentes nas Fórmulas e Amarrações de Lançamentos ativas e só fará a integração de lotes se os lançamentos estiverem satisfazendo a estas fórmulas e amarrações ativas. Com este parâmetro desmarcado, as fórmulas e amarrações existentes não serão validadas pelo processo de Integração de Lotes.

**11.40.45**  **Acessar lotes de outros módulos**

Ao acessar os lançamentos de um lote que teve origem em outro módulo, o sistema não irá solicitará mais a digitação de usuário/senha nas seguintes situações: 1 Se o usuário logado for um usuário supervisor, ou 2- Se o usuário logado tiver permissão para manutenção (inclusão ou edição ou exclusão) nos lançamentos do lote, ou 3- Se o usuário logado tiver permissão para acessar lotes de outros módulos. Se o usuário logado não atender a nenhuma destas condições, o sistema irá então solicitar a digitação de usuário/senha com alguma destas características.

**11.40.40 - Parâmetros do Sistema**

Criado o parâmetro do sistema '*Aplicar regra de validação de lançamentos no Agrupamento de Lançamentos'*. Este parâmetro será aplicado na execução de Agrupamento de Lançamentos e só ficará disponível se o parâmetro 'Usa regra de validação de lançamentos' estiver habilitado. Marcando-se este novo parâmetro, no momento da execução do Agrupamento de Lançamentos, além das regras inerentes a este processo, o sistema fará também a validação das regras de inclusão de lançamentos presentes nas Fórmulas e Amarrações de Lançamentos ativas e só fará o agrupamento dos lançamentos que estiverem satisfazendo às fórmulas e amarrações existentes. Com este parâmetro desmarcado, as fórmulas e amarrações existentes não serão validadas pelo processo de Agrupamento de Lançamentos. Vale ressaltar que, dependendo do volume de informações da base de dados, executar o processo de Agrupamento de Lançamentos com este novo parâmetro habilitado, pode comprometer a performance do processo!

**11.40.40 -** **Agrupamento de Lançamentos**

Evoluído o processo de Agrupamento de Lançamentos Contábeis para permitir que seja informado filtro por Filial, filtro de Contas Contábeis e também que seja possível informar um Documento/Complemento para as partidas que serão agrupadas dentro do lote contábil, mantendo, entretanto, inalteradas as informações destes campos ao consultar as partidas nos sistemas de origem.

**11.40.40 - Associação Dinâmica do Centro de Custo/Conta Gerencial ao Plano Paralelo**

Implementado processo responsável por fazer automaticamente a associação dos centros de custos (ou contas gerenciais conforme utilização indicada nos Parâmetros do Sistema/Rotinas Legais) utilizados nos lançamentos contábeis às respectivas contas contábeis movimentadas e que estejam associadas ao Plano Referencial da Receita - Plano Paralelo.

**11.40.40 - Visualização das Associações das Contas Contábeis com Planos Paralelos**

Funcionalidade implementada, responsável por identificar e mostrar individualmente todas as associações existentes da conta contábil selecionada ao(s) Plano(s) Paralelo(s)/Conta(s) Paralela(s).

**11.40.40 - Classificação Automática da Natureza da Conta Contábil**

Processo implementado no sistema com o objetivo de otimizar o preenchimento do campo 'Natureza da conta para emissão do SPED'. Informando-se o grupo de contas e a Natureza da conta para emissão do SPED, o sistema preenche automaticamente o campo 'Natureza da conta para emissão do SPED' de todas as sub-contas pertencentes ao grupo informado com a Natureza também informada na execução do processo.

**11.40.40 - LOG de execução do SPED Contábil**

No final da geração do SPED Contábil o sistema apresentará um LOG de execução, indicando todas as ações realizadas para a geração do SPED Contábil e o tempo gasto em cada uma.

**11.40.40 - Upload/Download de arquivos na geração do SPED Contábil**

Implementados os recursos de Upload para Razão Auxiliar e Arquivos Adicionais-J800 e Download do arquivo digital gerado. Estes recursos visam otimizar a utilização da memória do computador evitando travamento na execução do processo, uma vez que o Upload leva parcialmente os arquivos manipulados para o servidor de aplicação liberando a memória e o Download baixa o arquivo do servidor para o local indicado.

**11.40.40 - Histórico de Fechamento na geração do SPED Contábil**

Foi disponibilizada uma nova opção na geração do SPED Contábil para facilitar a identificação do(s) Histórico(s) de Fechamento(s) utilizado(s) na apuração de resultado do período. Agora é possível indicar o código da estrutura de Transferência de Grupos Contábeis utilizada para a apuração de resultado do período para que o sistema faça a leitura e indique automaticamente o(s) Histórico(s) de Fechamento(s) utilizado(s). Se preferir, ainda é possível indicar manualmente o(s) código(s) do(s) Histórico(s) de Fechamento(s) utilizado(s) e suas respectivas datas, bastando para isto clicar no link correspondente.

**11.40.35 –** **Agrupamento de Lançamentos**

Implementado no processo de Agrupamento de Lançamentos o filtro para seleção de Contas Contábeis. Ao selecionar a opção para utilização deste filtro, o sistema habilita dois filtros de contas, um para Débito e outro para Crédito de acordo com a forma de agrupamento escolhido anteriormente. Estes filtros já vêm preenchidos com as contas contábeis utilizadas no débito ou no crédito conforme o filtro, podendo o usuário incluir ou excluir contas.

**11.40.35 – Parâmetros do Sistema**

- Por motivo de padronização dos aplicativos da linha RM, os 'Parâmetros do Sistema' que ficavam disponíveis dentro do menu Utilitários ficarão agora disponíveis dentro do menu Ambiente.

- Descontinuados os parâmetros do sistema "Barrar lançamentos com Centro de Custo inativo" e "Barrar lançamentos com Departamento inativo", pois na tela de inclusão de lançamentos só é permitida a utilização de Centro de Custo e/ou Departamento que estiverem Ativos.

**11.40.5 –** **Consistência de Lançamentos**

Implementada nova consistência que irá verificar 'Lotes que possuem partidas com referências repetidas'. Evoluído o processo referente à consistência de 'Lançamentos que possuem rateios com valor 0 (zero)'.

**11.40.0 -** **Lançamentos Periódicos**

As rotinas de Lançamento Automático e Geração de Lançamentos Automáticos foram migradas para a plataforma .NET e correspondem agora à nova rotina denominada **Lançamentos Periódicos**. Através desta nova rotina é possível criar estruturas e moldes para lançamentos que se repetem periodicamente e uma das novidades é a possibilidade de agendar para outro dia/hora a inclusão dos lançamentos. Ao mandar executar esta rotina, os lançamentos serão incluídos automaticamente na base de dados conforme os moldes definidos na estrutura selecionada, ou então, se desejar, neste mesmo momento indique uma nova data/hora para que os lançamentos sejam incluídos na base de dados.

**11.40.0 -** **Alteração da Distribuição Gerencial**.

A rotina Lançamentos Gerenciais Automáticos foi migrada para a plataforma .Net, e corresponde agora à nova rotina denominada **Alteração da Distribuição Gerencial**. Esta rotina permite alterar a distribuição gerencial existente nos lançamentos contábeis de forma global e automatizada.

**11.40.0 -** **Consistência de Lançamentos**

Implementado neste processo a validação do valor da capa do lote. Se o valor da capa estiver menor que os valores lançados no lote, o sistema poderá fazer a correção caso ao executar o processo de Consistência de Lançamentos a opção 'Ajustar capa do lote automaticamente' esteja marcada.

**11.40.0 -** **Transferência de Grupos Contábeis**

O processo foi evoluído, possibilitando agendar a inclusão dos lançamentos gerados pela transferência. Para isto, na última tela do processo de execução, informe nova data/hora para a inclusão dos lançamentos.

**11.40.0 -** **Lançamentos contábeis**

Ao desmarcar o parâmetro do sistema 'Usa departamento' este campo não fica visível na tela dos lançamentos, embora o seu conteúdo anterior continue gravado no banco. Com este parâmetro desmarcado, em alterações de Filiais dos lançamentos, o sistema não fará mais a consistência entre Filiais/Departamento, possibilitando qualquer alteração.

**11.40.0 - Fórmulas Visuais**

A partir desta versão, o aplicativo TOTVS Gestão Contábil passa a integrar o processo de Lançamentos Contábeis com a ferramenta de Fórmulas Visuais – Recurso Global, que utiliza código e artefatos visuais para a elaboração de customizações, que podem ser criadas até mesmo por usuários finais.
