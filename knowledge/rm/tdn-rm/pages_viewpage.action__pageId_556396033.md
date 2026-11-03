---
content_hash: edbc6158275a5b44a781121a9949796d132bf280238f8185faa839f273b06b53
fetched_at: '2026-06-29T00:10:46.980053+00:00'
page_id: '556396033'
product: rm
source: tdn-rm
title: Portal TOTVS Obras e Projetos.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=556396033
version: 23
---

---

No mundo dos negócios, onde as empresas precisam ter controle sobre suas operações e, ao mesmo tempo, agilidade para atender aos diversos processos que acontecem simultaneamente foi criado o Portal TOTVS Obras e Projetos.

Neste Portal Web o usuário tem a possibilidade de selecionar a Coligada e o Projeto conforme modelo abaixo, respeitando as parametrizações e permissões do RM para o usuário.

No topo da tela principal do portal é exibido o projeto atual que o usuário está logado.

E ao lado direito ainda no topo da página na logo da Totvs é possível realizar a troca de contexto selecionando outro projeto para visualização.

PaginageralInstalação e Configuração.Instalação

* Na instalação da biblioteca do RM deve-se atentar a porta informada para o host para que seja utilizado nas configurações posteriores.

* É obrigatório que esteja instalado o URL Rewrite como componente do IIS. Esse componente permite que a URL do site seja reescrita durante a navegação.

* É importante verificar também em Tipos de MIME se o tipo de mime ".json" está inserido.

Observação: O cadastro do Tipo de MIME é necessário para que o IIS consiga ler os arquivos ".json" do Portal. A verificação é necessária pois caso o MIME não estiver cadastrado o portal pode apresentar erros na leitura dos arquivos.

Configuração Web.config e Host

O PortalTopWeb e o Cockpit pode ser hospedado no IIS  ou no RM.Host, sendo que ao optar por hospedar eles no RM.Host não é necessário a utilização do instalador ... e do IIS.

É de extrema importância que a configuração do **RM.Host ou RM.Host.Service** **(C:/TOTVS/CorporeRM/RM.Net)**estejam corretamente preenchidos pois eles carregarão a informação da base de dados para o Portal.

* **RM.Host ou RM.Host.Service**(Não use os dois ao mesmo tempo e com a mesma porta para que não há conflito de comunicação)
  + Antes de qualquer alteração, o Host deve estar desativado.
  + Os valores para "DefaultDb", "Port" e "ApiPort" deve estar informados corretamente:
    - "DefaultDB": é o nome do alias que será utilizado por default ao acessar o Portal RM. **(Extremamente importante para acesso no Portal TOTVS Obras e projetos)**;
    - "Port": é a porta do host;
    - "ApiPort": é a porta onde será realizada a comunicação da API. **(Extremamente importante para acesso no Portal Obras do TOTVS Obras e projetos, caso não exista essa tag no host o sistema utiliza o valor 8051 como default)**.

Lembrando que, as portas informadas para o host na chave **Port** e a porta informada na chave **ApiPort** deve estar **permitidas** no **Firewall**para que a comunicação funcione corretamente.

* **Web.config**
  + Os valores para "Port", "Host" e "ServiceAlias" deve estar informados corretamente.:
    - "Port": o valor da porta informada é o valor da porta do Host, seja ele RM.Host ou RM.Host.Service;
    - "Host":  é o nome da máquina;
    - "ServiceAlias": é o nome do alias que será utilizado.

Caso não há essas configurações inseridas no arquivo inseri-las para que o sistema funcione corretamente.

Configurando ISS

O PortalTopWeb e o Cockpit pode ser hospedado no IIS  ou no RM.Host, sendo que ao optar por hospedar eles no RM.Host não é necessário a utilização do instalador ... e do IIS.

Ao finalizar a instalação da Biblioteca do RM Portal, será criado um site no IIS com o nome FrameHTML. O site é criado e toda a comunicação do IIS acontece na pasta **C:\TOTVS\CorporeRM\FrameHTML**

* O IIS realiza interações com a pasta do site e ele deve ter permissão total de acesso a pasta. É necessário inserir nas propriedades da pasta o controle total para o IIS: **NOMEDAMAQUINA\IIS\_IUSRS**.

* Uma das melhores formas de se testar a comunicação do IIS com a pasta é abrir o site logo após essas configurações é abrir o site pelo Procurar Site:

* Se o site for aberto sem nenhum erro é porque a comunicação entre a pasta e o IIS está corretamente configurada. Caso encontre algum erro nesse passo vá até a aba desse documento com nome **Erros e Soluções**.

Site aberto:

* Com o site aberto navegue entre as pastas **RM/Login/Login.aspx** ou simplismente insira na URL do navegador dessa forma **<http://localhost:8080/RM/Login/Login.aspx.>**Ressaltando que, no caso a minha porta de comunicação do IIS é **:8080** conforme exibido no IIS na etapa Procurar site. Caso a porta cadastrada no IIS seja diferente deve ser informada a porta  correta para realizar esse segundo teste de validação. Se a página de login aparecer com sucesso sem exibir nenhum erro é porque a comunicação do IIS com a pasta está correta.

Página de Login:

Configuração Monitor de Obras\ Cockpit

* A última configuração que deve ser feita para o correto funcionamento do Portal TOTVS Obras e Projetos é informar o valor correto desejado no arquivo **config.json (C:\totvs\CorporeRM\FrameHTML\Web\App\Prj\PortalTopWeb\config\config.json).**
* O arquivo não possui muitas informações mas deve se manter atento ao preenchimento para que ele funcione corretamente.
  + Após a instalação o arquivo estará preenchido conforme abaixo:

* "apiServer": endereço da API para ser acessado no Portal TOTVS Obras e Projetos.
  + Devem ser informados os valores corretamente;
  + A porta da API deve estar preenchida com a **mesma porta** informada na **configuração do Host:  "ApiPort".**Se a tag estiver com valor 8052 a porta deve ser alterada;
  + O endereço localhost limita o acesso no portal somente para quem está na máquina localmente. Para acessos externos o endereço deve ser alterado para o nome completo do computador (Exemplo: <http://bhn050102752.bh01.local:8051>)

* "apiKeyGoogleMaps": chave gerada pelo google maps para que as localizações dos apontamentos provenientes do TOP Mobile sejam visualizadas no Portal TOTVS Obras e Projetos.
Parametrização do Mapa

Acessar a plataforma de mapas do google : <https://cloud.google.com/maps-platform/?hl=pt>

Clicar em Primeiros Passos:

Selecionar o projeto google:

*Caso não há nenhum projeto criado, ao clicar sobre a seta é possível inserir um novo projeto.*

Ao avançar, será exibida a página para configurar o faturamento do Google Maps Plataform:

Informar a Etapa 1 e continuar.

Informar corretamente todos os dados na Etapa 2 e clicar em "INICIAR MINHA AVALIAÇÃO GRATUITA".

Ao avançar na Etapa 2, será exibida a ativação da Plataforma do Google Maps e clicando em "PRÓXIMA" será exibida a chave do Google Maps criada.

Agora adicione a sua Chave da API em **Serviços Globais | Ambiente | Parâmetros | Parâmetros Globais | Google | Google Maps**

Caso seu ambiente possua proxy, preencha as configurações do proxy.

Acessando o Monitor de Obras

A URL de acesso do Portal TOTVS Obras e Projetos é <http://localhost:8080/web/app/Prj/PortalTOPWeb/index.html>. Ressaltando que, nessa URL informada, [http://localhost:8080](http://localhost:8080/) é apenas um exemplo e caso há alteração para o nome completo do computador no arquivo **config.json** essa URL deverá ser alterada. (Exemplo: <http://bhn050102752.bh01.local:8080/web/app/Prj/PortalTOPWeb/index.html)>

* A base que estiver informada no alias cujo o valor está informado no "DefaultDB" será a base acessada no login.
* O usuário para login deve ser o usuário de login no RM.

Erros e Soluções

1. Um dos primeiros erros que podem acontecer no teste da comunicação do IIS é relacionado a configuração "directoryBrowse". Em alguns casos ele está definido como "false" e o Portal necessita que a configuração esteja "true".

1.1. Para realizar o ajuste é necessário entrar no editor de configurações e alterar o "directoryBrowse" para true e aplicá-la

2. Erro **403 - Forbidden: Acess is denied**

2.1. Esse erro na maioria das vezes pode acontecer pois a configuração de Autenticação Anônima do IIS está incorreta. Para alterar deve-se acessar a Autenticação → Selecionar a Autenticação Anônima com um clique → Editar → Informar a Identidade de usuário anônimo: Identidade de pool de aplicativos

3. Erro por ausência do arquivo ou ausência de informação no arquivo A**lias.dat (C:/TOVS/CorporeRM/RM.Net/Alias.dat)**

3.1. Para corrigir esse erro o arquivo deve existir na pasta. Esse erro não é tão comum de acontecer quando se instala a Biblioteca RM e em seguida o Portal, pois na instalação da Biblioteca RM já se informa uma base de dados e automaticamente essa base será preenchida no arquivo **Alias.dat**

Monitor de Obras 

**Monitor de Obras**

Para a funcionalidade do Monitor de Obras foram desenvolvidas telas Web para que o usuário possa ter um acesso mais ágil e prático dos apontamentos.

.Mão de Obra

* **Mão de Obra**

**Localização do Funcionário**

* **Funcionários Ociosos:** Os membros da equipe estão presentes mas com improdutividade.
* **Funcionários Presentes:** Todos os membros da equipe estão trabalhando.
* **Total de Funcionários:** Funcionários Presentes + Funcionários Ociosos
* **Horas apontadas:** Total de horas apontadas em todas as folhas.
* **Horas improdutivas:** Total de horas improdutivas em todas as folhas.
* **Ver detalhes:** abre a página de detalhes do monitor de mão-de-obra.

Equipamentos

* **Equipamentos**:

* **Status Geral**
  + **Equipamentos em Operação:**Todos os Equipamentos que estão operantes.
  + **Equipamentos não Apontados:** Todos os Equipamentos que não tiveram apontamentos até o momento.
  + **Equipamentos Parados:** Todos os Equipamentos que tiveram apontamentos no dia porém não existe apontamento em aberto no momento e não possui Motivo de Improdutividade.
  + **Equipamentos Improdutivos:** Todos os Equipamentos que possuem apontamentos em aberto e que se encontram com motivo de improdutividade.
  + **Total de Equipamentos:** Total de equipamentos associados ao Projeto.
  + **Horas Apontadas:** Total  de horas apontadas.
  + **Horas Trabalhadas:**Total de horas Trabalhadas.
  + **Horas Improdutivas:** Total de horas Improdutivas.

* **Dashboard**
  + Serão exibidos os dados agrupado por Família de Equipamentos
  + **Em Operação:**Total de Equipamentos da família que se encontra com apontamento em aberto e sem Motivo de improdutividade
  + **Não Apontados:** Total de  Equipamentos da família que não tiveram apontamentos até o momento.
  + **Parados:**Total de Equipamentos da família que ja tiveram apontamentos o dia porém no momento não possui nenhum apontamento em aberto e não possui Motivo de improdutividade.
  + **De Terceiros:** Total de Equipamentos da família que são de Terceiros;

* **Improdutividade**

+ **Motivos de improdutividade:**Total de Improdutividades agrupados por prioridades Normal, Alta e Crítica

* **Ver detalhes:**  
  + Ao clicar em ver detalhes será aberto uma nova tela com os detalhes de apontamentos dos equipamentos da família.
  + Para os Equipamentos que não sem apontamentos no dia será exibido a mensagem "Não possui agendamentos"
  + Para os Equipamentos com Motivos de inatividade o mesmo será exibido e abaixo as seguintes informações:
    - Descrição da tarefa
    - Dados de Entrada e Saída do apontamento
    - Usuário
    - Centro de Custo
    - Observações do apontamento

* **No Dashboard teremos duas formas de realizar buscas**
  + **Busca Simples: Esta busca será realizada no campo "Pesquisar por Descrição", e irá retornar as famílias que contiver o termo informado no campo**
  + **Busca Avançada: Esta estão definidos filtros por inatividade, por Prioridade e Apenas Famílias com equipamentos de terceiros**

* **Status/Alertas**
  + A exibição do Status/Alertas da família é realizada conforme descrito abaixo:
  + **Não Iniciado:**Todos os Equipamento da família se encontram sem apontamentos até o momento
  + **Conforme Esperado:** Abaixo de 20% dos Equipamentos parados e/ou Improdutivos;
  + **Atenção:** Percentual de 20% a 39% dos Equipamentos parados e/ou Improdutivos;
  + **Crítico:**Acima de 40% dos Equipamentos parados e/ou Improdutivos ou basta 1 Equipamento com Motivo de Improdutividade crítico;

* **Localização dos Equipamentos**
  + Localização geográfica dos Apontamentos realizados.

Ciclo de transporte

* **Ciclo de Transporte:**

* Nome do ciclo de transporte
* Iniciados: Total de cargas em aberto realizadas no ciclo de transporte
* Concluídos: Total de Ciclos concluídos (Carga e Descarga) realizados no ciclo

* Status  
  + Os apontamentos concluídos (Carga e Descarga) será exibido na cor Verde
  + Os apontamentos que não possuem Descarga será exibido na cor Amarela

* Ver Detalhes
  + Será exibido os detalhes dos apontamentos do ciclo
    - Carga: Data e hora em que foi realizado o apontamento inicial seguido do responsável pelo apontamento
    - Descarga: Data e hora em que foi realizado o apontamento inicial seguido do responsável pelo apontamento

* Observações
  + Observações da Carga/Descarga: Será exibido as observações informadas no momento do apontamento de Carga ou Descarga

* Mapa
  + No mapa serão exibidos as localizações dos apontamentos de Carga e Descarga

Avanço Físico

* **Avanço Físico:**
  + **Últimas tarefas apontadas:** Exibe a lista das 3 últimas tarefas apontadas na obra.
  + **Ver detalhes:** abre a página de detalhes do monitor de avanço físico.

Em detalhes do Apontamento é exibido as Tarefas onde foram realizadas os apontamentos, assim como o Percentual apontado. É exibido também a localização geográfica no mapa de onde foram feitos os apontamentos.

Ao selecionar uma ou mais das Tarefas, no mapa é exibidos somente os apontamentos referentes ao selecionado.

Nos detalhes das Tarefas é exibido:

* Código da Tarefa;
* Descrição da Tarefa;
* Unidade;
* Valor unitário;
* Quantidade;
* Valor total;
* Observações do apontamento;
* Fotos do Apontamento;

* **Últimos acontecimentos:**Mostra os últimos acontecimentos por avanço físico, mão-de-obra e equipamento.
* **Coletores:**
  + Número de coletores ativos na obra.
  + Número de coletores sem apontamento na última hora.
  + Informações dos coletores sem apontamento.

**Observação:**A página do monitor de obras será atualizada automaticamente de 30 em 30 segundos.

Pedido

### Pedido

Para a funcionalidade do Pedido no TOTVS Obras e Projetos foram desenvolvidas telas Web para que o usuário possa ter um acesso mais ágil e prático da funcionalidade.   
Foram desenvolvidas todos os cadastros e visões de anexo para o Pedido da seguinte forma:

* Tela com a listagem dos pedidos salvos na base de dados com opções de Fazer Novo Pedido, Visualizar, Editar e Excluir;

* Ao fazer novo pedido é apresentando uma tela para preenchimento dos campos.

* Ao editar o pedido é apresentado uma tela detalhada contendo:
  + Item de Pedido;

* + Ao expandir um item são apresentados os seguintes detalhamentos:  
    - Contratos;
    - Datas de Necessidade;
    - Datas de Entrega;
    - Preço Orçado;
    - Produtos;
      * Opção de Editar item mostrando detalhes da compra separado por Tarefa, com possibilidade de alterar a Necessidade dos mesmos;

* Ao clicar em Editar itens, é exibido uma tela com os itens do insumo, e ao clicar no itens os campos de edição são carregados

* + - Histograma;
      * 511pxRequisição;
      * Necessária;
      * Pedida;

* + Informações do Pedido;
    - Status;
    - Data Requisição;
    - Tipo de Requisição

* + Configuração;
    - Utiliza Preço Orçado;
    - Tipo de Movimento;
    - Local de Estoque;

Para os processos foram desenvolvidas telas Web todos os processos que envolvem o Pedido, de acordo com :

* Pedido
  + Criação do Pedido;
  + Visualizar Movimento, com a opção de rastreio;
  + Excluir Movimentos;
  + Importar preços cotados;
  + Rateio de Produtos;
  + Excluir Pedido;
  + Envia pedido para Suprimentos/Faturamento gerando apenas 1 (um) movimento.
  + Envia pedido para  Suprimentos/Faturamento gerando 1 (um) mov. por data de entrega

Pedido Extra

### Pedido Extra

O Pedido Extra tem a finalidade de controlar os gastos extras, ou seja, material além do planejado. São controladas todas as movimentações de pedidos, autorização do pedido, quantidade pedida para determinada tarefa e principalmente as pessoas envolvidas no processo.

Para a funcionalidade de cadastro do Pedido Extra no TOTVS Obras e Projetos foram desenvolvidas telas Web para que o usuário possa ter um acesso mais ágil e prático da funcionalidade.

Foram desenvolvidas todos os cadastros e visões de anexo para o Pedido Extra da seguinte forma:

* Tela com a listagem dos pedidos de materiais extras salvos na base de dados com opções para Adicionar, editar, visualizar e excluir ;

Tela com os detalhes do Pedido Extra;

* Item de Pedido Extra;
* Status do Pedido;
* Data Requisição;
* Configurações:
  + Utiliza Preço Orçado;
  + Responsável;
  + Tipo de Movimento;
  + Local de Estoque;

De acordo com o status do pedido haverá um botão para executar os processos:

* **Retornar para criação:** Quando o pedido está no status "Em aprovação" e deseja-se realizar alterações no pedido.
* **Enviar para Aprovação:** Quando o pedido está no status "Em criação" e pronto para ser analisado e aprovado.
* **Finalizar Aprovação:** Quando o pedido está no status "Em aprovação" e houve alguma alteração individual em algum item, ou seja foi aprovado parcialmente.
* **Aprovar Pedido Extra:** Quando o pedido está no status "Em aprovação" e deseja aprovar o pedido por completo, sem nenhuma ressalva.
* **Reprovar Pedido Extra:** Quando o pedido está no status "Em aprovação" e deseja reprovar o pedido por completo.

Não será possível selecionar múltiplos registros para execução dos processos, seguindo o padrão de uso Web, devendo executar item a item. Foram migados todos os processos que envolvem o Pedido:

* Pedido
  + Retornar para criação
  + Enviar Pedido Extra para Aprovação
  + Finalizar Aprovação de Pedido Extra
  + Aprovar Pedidos Extra
  + Reprovar Pedidos Extra
  + Gerar 1 Movimento
  + Gerar Movimento por Data de Entrega
  + Excluir Movimento
* Anexo Item do Pedido

* + Aprovar item
  + Reprovar Item
  + Aprovar Item Parcialmente
  + Colocar Itens em Análise

* Movimento
  + Rastreamento de movimento foi mantido o comportamento similar ao da interface WinForms, onde o usuário somente executa o processo e recebe como retorno a mensagem com o status de processamento.

* Ao Adicionar um novo Item de Pedido Extra, existe o campo "Manter preenchimento do último item adicionado".
  + Caso esteja marcado, ao Adicionar Novo Item, a tela deve vir preenchida com os dados do último item adicionado, exceto a Quantidade que deve vir em branco.
  + Se o campo não estiver marcado, o comportamento se mantém o atual.

Saiba mais em.: [Geração de Pedido](http://tdn.totvs.com/display/LRM/Pedido+de+Material) e [Geração de Pedido Extra](http://tdn.totvs.com/pages/viewpage.action?pageId=421385494&moved=true).

Cockpit de Tarefas / Insumos

O Cockpit é uma ferramenta de busca de informações detalhadas da tarefa e dos insumos permitindo dessa forma um acompanhamento visual do que foi planejado, realizado e apropriado no projeto selecionado.

É uma ferramenta de busca simples onde se informa a opção desejada (Tarefa/ Insumo) e o sistema atualiza as informações visualmente na tela.

No topo da tela basta selecionar o que procura. E depois de informar o código ou descrição é exibido o resultado.

.Tarefa

**Nome da tarefa:** Nome da tarefa pesquisada (caso a opção selecionada for insumo será exibido o nome do mesmo).

Código da tarefa / Código do insumo

***Status*:** Esse quadro informa em percentual o quanto a tarefa já está finalizada.

***Custo:*** No quadro custo é exibido uma barra percentual enfocando o valor que foi planejado para a tarefa e o valor que já foi apropriado para a mesma durante a execução do projeto.

**Planejado:** Valor orçado para a tarefa no seu planejamento (API busca quantidade valor )

**Apropriado:** Valor que já foi executado da tarefa

**Saldo:** Exibe quanto ainda tenho de saldo para realização da tarefa.

***Pedido***

No pedido o Cockpit reflete o resultado do que já foi pedido proporcionalmente ao que já foi de fato entregue.

**Pedido:** Total que foi pedido e apropriado na tarefa

**Entregue:** Total do que realmente foi entregue da tarefa.

O total entregue é calculado com base nos tipos de movimento de entrega/devolução informados por projeto, e será exibido de acordo com a parametrização do projeto selecionado no contexto do portal. Os movimentos gerados através de movimentos de devolução, são subtraídos do total dos movimentos de entrega.  
   
Para definir os tipo de movimento de entrega/devolução, acesse os parâmetros do projeto, em Integração>Suprimentos/Faturamento>Movimentações Backoffice:

**Valor Pago RM:**Considera os movimentos que foram gerados no backoffice pelo TCOP , ou seja , que sejam de origem do Totvs Obras e Projetos. Busca apenas valor pago referente a pedido , pedido extra , contrato de fornecimento de material e pedido de faturamento direto.

Em caso de notas fiscais de faturamento direto (que tem contrato e projeto/tarefa informado) e entraram diretamente pelo nucleus, sem pedido de faturamento direto do Totvs Obras e Projetos , serão consideradas no valor pago.

**Valor Pago Protheus :** Considera os valores nas baixas dos títulos financeiros onde existem rateio de tarefa/projeto originados pelo pedido, extra e contratos . Lançamentos feitos manualmente não vão ser considerados pois não partem de origem Totvs Obras e projetos é considerado apenas como apropriação e não como valor pago. 

Para auxiliar na conferência dos números exibidos no cockpit foi disponibilizada, no módulo de projetos, a tela de Movimentações do Backoffice.

Seu acesso é feito através do menu Executar:

Insumo

Outra opção que pode ser selecionada no top da pagina é Insumo:

Na lupa de pesquisa é possível filtrar qual insumo deseja ver o detalhamento no cockpit.

Ao informar o código do insumo ou descrição o cockpit carrega as informações do mesmo na tela

**Planejado:** Valor orçado para a tarefa no seu planejamento (API busca quantidade valor )

**Apropriado:** Valor que já foi executado do insumo

**Saldo:** Exibe quanto ainda tenho de saldo para realizaçãodo insumo

***Pedido***

No pedido o Cockpit reflete o resultado do que já foi pedido proporcionalmente ao que já foi de fato entregue.

**Pedido:** Total que foi pedido e apropriado no insumo

**Entregue:** Total do que realmente foi entregue  do insumo

Saldo da quantidade e valor do insumo
