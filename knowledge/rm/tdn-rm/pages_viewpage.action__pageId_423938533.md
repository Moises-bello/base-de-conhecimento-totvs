---
content_hash: 0a3f8ecb29e9bfdcd9fef936ed89ec861c09267fc225eebdec4b41c23ee92859
fetched_at: '2026-06-29T00:09:27.527591+00:00'
page_id: '423938533'
product: rm
source: tdn-rm
title: Cadastro da Ordem de Serviço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938533
version: 7
---

**Pasta Identificação**

A pasta identificação é composta por um cabeçalho onde será possível informar o cliente para o qual está fazendo abertura da ordem de serviço, o local estoque, data de emissão e a data de saída do objeto da RM Officina.   
Serão exibidos no cabeçalho o identificador do movimento, o Status da ordem, tipo dos itens (peças e serviços) e o tipo do movimento.   
O campo data de autorização será preenchido na mudança de status da ordem para "Em andamento" e data de término na conclusão da ordem.   
Nesta pasta ficará visível as tabelas de "Classificação", "Centro de Custo", "Departamento" e "Faturamento" para o tipo de movimento.   
As mesmas são configuradas no tipo de movimento de geração de ordem de serviço no TOTVS Gestão de Estoques, Compras e Faturamento, nas respectivas etapas. "Etapa 7 - Movimento - Tabelas - Classificação , "Etapa 9 | Movimento | Tabelas | Globais | Etapa 10 - Movimento - Tabelas -Opcionais.  
Os campos destas tabelas poderão ser configurados como obrigatórios e/ou default.

**Pasta Manutenção**

Na pasta identificação informe o objeto de manutenção para o qual está abrindo a ordem de serviço e ultimo indicador de uso do objeto será exibido na pasta indicadores de uso. A pasta planos realizados permite incluir e visualizar os Planos de Manutenção que vão fazer parte da Ordem de Serviço. Para que um plano fique disponível para ser incluído na Ordem de Serviço o mesmo tem que ser previamente inicializado para o objeto de manutenção. Para inicializar o plano é necessário acessar Cadastros | Objeto de Manutenção | Anexo | Inicialização de Planos de Manutenção.   
 No momento de incluir um Plano, o aplicativo emitirá uma mensagem perguntando se o usuário deseja incluir na Ordem de Serviço o(s) Item(ns) correspondente(s) do Plano de Manutenção selecionado.   
 No momento de excluir um Plano, o aplicativo também emitirá uma mensagem perguntando se o usuário deseja excluir o(s) item(ns) correspondente(s) ao plano, que já foram incluídos na Ordem de Serviço no momento de incluir o plano.  
 ***Observação*:** Ao excluir o plano pela tela de visão, os itens não serão excluídos. Se o usuário desejar excluir os itens junto com o plano, é necessário fazer a exclusão através da tela de edição do plano clicando no botão editar e acessando a tela de edição do plano. Ao excluir o plano o sistema exibirá uma mensagem perguntando se o usuário deseja excluir os itens, clicando em sim os itens serão excluídos da Ordem de Serviço.  
 A aba planos realizados só será habilitada após salvar a OS, antes disso não será possível visualiza-la na pasta manutenção.  
 A data de geração do plano realizado nao poderá ser maior que data de término da OS.  
 Ao clicar no lookup para selecionar os planos de manutenção só serão exibidos os planos inicializados.  
 Ao marcar o parâmetro "**Permite visualizar apenas planos inicializados do Objeto na OS**" que se encontra no menu *Opções | Parâmetros | Sistemas*, aba Ordem de serviço, só serão exibidos os planos inicializados do objeto de manutenção.

**Verificar Local de Instalação**

Ao clicar no botão verificar local de instalação o sistema traz os dados do cliente e do local onde o objeto esta instalado.

**Selecionar Cliente** Ao clicar no botão selecionar cliente o sistema exibirá uma tela para que o usuário possa escolher um cliente. Ao selecionar um cliente se o mesmo for proprietário de algum objeto de manutenção este objeto será listado na grid para que o usuário possa selecioná-lo e inseri-lo na OS, também são exibidos os objetos que se encontram instalados neste cliente.

**Indicador de Uso** Ao clicar no botão Indicador de Uso o sistema exibe a mesma tela de histórico de indicador que é exibida ao acessar o caminho Cadastro | Objeto de Manutenção | Anexo | Histórico de Indicador de Uso. Nesta tela é possível lançar um ou mais indicadores de uso para o objeto de manutenção selecionado.

Para saber mais sobre indicadores de uso clique aqui.

**Acessórios**

**Resumo Técnico**

**Contratos deste cliente:**Ao clicar no botão Contratos deste Cliente o sistema exibe a tela "Visão de Contratos", nesta tela é possível visualizar os dados do contrato e também escolher se o mesmo será ou não utilizado para a ordem de serviço.

***Observação:*** Este botão somente ficará habilitado se o objeto de manutenção inserido na OS tiver um contrato cadastrado.

**Pasta Identificação**

**1º Identificador**: Neste campo é possível selecionar o código identificador do objeto de manutenção que será usado para gerar a OS.

**Placa**: Este campo é usado para informar a placa do objeto de manutenção quando o mesmo for do tipo veículo, caminhão etc.

**Cod. Tipo Objeto**: Campo usado para informar o tipo do objeto de manutenção. Objeto de manutenção é cadastrado em Cadastro | Objeto de Manutenção.

**Reforma**: Este campo é usado para objetos de manutenção do tipo pneu, ao marcar o check list reforma é habilitado o botão "Reforma de Pneu" na tela da OS.

**Cod. Modelo**: Neste campo é exibido o modelo do objeto de manutenção.

**Cod. Sub-Modelo**: Neste campo é exibido o sub-modelo do objeto de manutenção.

**Status**: Neste campo é exibido o status da ordem de serviço. Os status são:

* **Aguardando Análise**: Status inicial que o movimento assume automaticamente ao ser criado. Quando a Ordem de Serviço está neste status, é permitido executar os processos de mudança de status "Cancela OS" e "Termina Análise".
* **Não-Iniciado**: Indica que o orçamento do objeto está pronto para ser apresentado ao cliente, esperando somente sua autorização para ser iniciado. Quando a Ordem de Serviço está neste status, é permitido executar os processos de mudança de status "Cancela OS", "Termina Execução da OS" e "Marca para Faturamento".
* **Em andamento**: O movimento apresenta este status quando a manutenção do objeto já estiver iniciada (após o cliente autorizar o serviço). Quando a Ordem de Serviço está neste status, é permitido executar os processos de mudança de status "Cancela OS" e "Termina Execução da OS".

Caso a Ordem de Serviço tenha sido gerada pelo TOTVS Gestão de Relacionamento com Cliente, nesse status é possível executar somente a opção "Próxima Etapa", ao escolher essa opção, o atendimento vinculado a Ordem de Serviço é avançado para a próxima etapa no TOTVS Gestão de Relacionamento com Cliente.

**Terminado**: Indica o término da manutenção.Neste momento o objeto se encontra disponível para ser retirado da empresa. Não é possível inserir peça ou serviço (se for necessário, o status voltará para em Aguardando Análise, se o estoque não tiver sido baixado no TOTVS Gestão de Estoque, Compras e Faturamento). Quando a Ordem de Serviço está neste status, é permitido executar os processos de mudança de status "Cancela OS", "Marcar para Faturamento" e "Reiniciar OS".

**A Faturar**: Após o cliente aprovar a manutenção realizada, o movimento deverá assumir este status. Quando a Ordem de Serviço está neste status, é permitido executar os processos de mudança de status "Cancela OS" e "Voltar para Terminado".

**Faturado**: Após o faturamento (TOTVS Gestão de Estoque, Compras e Faturamento), o movimento assumirá este status na janela de visão de movimentos do RM Officina. Quando a Ordem de Serviço está neste status não é permitida alteração de status.

**Cancelado**: A Ordem de serviço assumi esse status após ser realizado o processo de cancelamento. Quando a Ordem de Serviço está neste status não é permitida alteração de status.

**Atenção:** Ao alterar o status da ordem de serviço de "Não iniciado" para "Em Andamento" o sistema fará as seguintes consistências:

Se a OS não tiver mão de obra alocada o usuário terá que alocar neste memento, exceto para OS de terceiros.

Se o objeto contido na OS se encontrar transferido para outra coligada o sistema não colocará a OS em andamento.

Se o objeto contido na OS se encontrar sucateado o sistema não colocará a OS em andamento.

Se o objeto tiver OS em andamento o sistema emitirá uma mensagem informando o usuário que existe OS aberta para este objeto e se o usuário quer mesmo assim iniciar o serviço desta OS.

Se a OS for de terceiros ao iniciar a execução dos serviços será gerado um movimento de remessa. O movimento que é gerado pode ser informado no menu Opções | Parâmetros | Sistema, aba movimento, campo Movimento de Terceirização.

**Func. Responsável:** Nome do funcionário responsável pela manutenção do objeto desde o seu período de chegada à oficina até, por exemplo, o retorno do objeto à empresa para possíveis reclamações na execução dos serviços. Ele é responsável por todas as etapas da manutenção: alocação de mão-de-obra, informar a data prevista de entrega do objeto etc.   
 Marcando o check list "Listar todos os func desta coligada", é possível incluir na Ordem de Serviço o nome de um funcionário cadastrado em outra coligada.

**Data de Programação**: Data em que a Ordem de Serviço programada deverá ser executada, (ou já foi executada). A Data de Programação é utilizada para os casos em que se queira controlar a abertura antecipada de ordens de serviço. Caso o campo não apresente alguma data, então a Ordem de Serviço não foi programada.  

**Pasta Indicadores de Uso**

Nesta pasta é exibido o indicador de uso que está lançado para o objeto de manutenção com data igual ou menor a data de criação da OS. Se o usuário quiser alterar o indicador com outra data basta acessar com o botão direito do mouse a funcionalidade "Alterar indicadores de uso". Para saber mais sobre esta funcionalidade clique aqui.   
    
 **Pasta Itens**

Na tela de cadastro de item, existe o botão "Expandir Itens Compostos". Se o tipo de movimento de geração de ordem de serviço estiver parametrizado para trabalhar com produto composto, ao clicar no botão "Expandir Itens Compostos" todos os itens serão exibidos na grid do cadastro de itens. Um produto é considerado composto quando o mesmo possui vários itens que compõe um único produto.
