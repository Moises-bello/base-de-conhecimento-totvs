---
content_hash: 20d9a5ea552e327249e16644105d76a8491179c5cfcc3d6bce6fe7353bb3f5db
fetched_at: '2026-06-29T00:11:03.629767+00:00'
page_id: '624621846'
product: rm
source: tdn-rm
title: Cadastros Básicos - App Minha Obra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=624621846
version: 35
---

Configuração

Confira o Acelerador de Implantação do APP Minha Obra para facilitar seus cadastros e a configuração das funcionalidades. [Saiba mais](https://tdn.totvs.com/x/q6nyIw)

ConfiguraçãoConfiguraçãoParâmetros Gerais

* Opção de Menu: Projetos \ Construção e Projetos \ Projetos \ Parâmetros \ Construção e Projetos \ Gerais;
* O parâmetro “**Utiliza mais de um projeto por coletor móvel**” define se um coletor móvel pode estar associado a mais de um projeto. O parâmetro será desabilitado, caso algum coletor móvel possua mais de um projeto associado;
* O parâmetro “**Utiliza mais de um coletor móvel por usuário**” define se um usuário pode estar associado a mais de um coletor móvel. O parâmetro será desabilitado, caso algum usuário possua mais de um coletor móvel associado;
* O parâmetro “**Permite enviar imagens para o coletor (Coligada e Usuários)**" define se ao sincronizar as imagens do cadastro da coligada e da pessoa no qual o usuário está associado, serão enviados para o coletor;
* O parâmetro **“Integrado com SIGA-MNT”** define se a integração está ativa no sistema;
  + - A manutenção de ativos, controlada pelo PROTHEUS, requer que seja sincronizado o cadastro de bens para o RM;
    - A comunicação/integração é realizada utilizando o EAI do RM (TOTVSMessage) através de troca de mensagens no padrão de mensagem única. O EAI do RM disponibiliza WebService e métodos para envio, recebimento, processamento das mensagens inclusive pontos de customizações;
    - Este cadastro no RM, uma vez integrado, significa que a origem de seus registros serão os registros do PROTHEUS então os mesmos não poderão ser manipulados no RM. É necessário rever as permissões de acesso, pois os cadastros que são feitos no BackOffice PROTHEUS devem ficar desabilitados no BackOffice RM;
    - A máscara utilizada para o código do patrimônio no cadastro de patrimônio deve ser com dois níveis. Sendo um para identificar a família do PROTHEUS que corresponde a um Título no patrimônio do RM, e outro nível para identificar o item dentro da família/título. Exemplo: ###. ####;
    - São tratados nesta integração além da manutenção do cadastro do bem, a transferência de filial e de centro de custos. Não é permitido a exclusão de um bem, quando houver esta necessidade, deverá ser inativado;
    - Para o campo “Capacidade de produção” e “Unidade da Capacidade da Produção” foi criada uma tabela de especialização da tabela de patrimônio no TOP. Esta tabela terá a manutenção exclusiva pelo processo de integração.

      * Código: 1005;
      * Descrição: TOTVS Construção Obras e Projetos x Manutenção de Ativos;
      * Mensagem/Versão: EQUIPMENT / 1.002.
* O parâmetro **“Valida Filial do equipamento”** é utilizado para validar se o equipamento está relacionado à filial do projeto no cadastro de bens, durante a vinculação dos equipamentos aos insumos do projeto;
* O parâmetro “**Permite registrar fotos em apontamentos no coletor**" define se será permitido o registro de fotos no apontamento de avanço físico do coletor e consequentemente o envio para o TOTVS Construção Obras e Projetos durante o sincronismo. São permitidas 6 fotos para cada apontamento .
* O parâmetro de**"Informações adicionais do Funcionário/Terceiro no coletor"**é uma forma de customizar a informação do funcionário exibida no coletor no APP Minha Obra. O usuário poderá visualizar no coletor as seguintes informações extras: Apelido, Função, Situação, CPF, Matrícula (Chapa);

* O parâmetro **“Enviar e-mail de log de erros”** define se haverá o envio de e-mail com um texto padrão para o usuário ou um grupo de usuários do sistema (este grupo deve ser criado pelo próprio cliente, conforme modelo de envio de e-mail para um grupo assim como é feito no Outlook), e que receberá informações do log de erros das importações/exportações realizadas pelos coletores móveis, através dos webservices disponibilizados no projeto Mobilidade. O endereço para envio do e-mail de log de erros poderá ser parametrizado por projeto ou um endereço geral. O log de erros de sincronização de cadastros será enviado para o endereço parametrizado nos parâmetros gerais. O log de erro dos processos (Avanço Físico, Mão de obra, Equipamentos e Ciclo de Transporte) será enviado para o e-mail parametrizado para o projeto. Caso não esteja parametrizado nenhum endereço para o projeto será enviado para o e-mail informado nos parâmetros gerais;
Utilizando Folha Tarefa

* Parâmetro para Habilitar a Utilização da Folha Tarefa:

* Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Básico \ Mobilidade \ Folhas Tarefa;

* Uma Folha Tarefa, representada principalmente por suas tarefas, pode ser considerada como um planejamento em curto prazo. Através desta Folha será possível ter o conhecimento das tarefas a serem realizadas em um dado intervalo de tempo bem como distribuir estes “planejamentos” entre as equipes/usuários das diversas frentes de obra, receber/gerir os apontamentos para diversas funções que as tarefas podem representar;
* Permite a alocação de equipes para a execução. Após o término da alocação, a mesma fica disponibilizada para ser sincronizado pelo coletor e posterior registro e envio dos apontamentos referente as frentes de execução;
* O objetivo desta funcionalidade é maior agilidade no direcionamento de tarefas nas frentes de obra e acompanhamento dos projetos através do envio/recebimento de informações sobre o andamento das tarefas (e atualização no TOP) com o uso de coletores móveis (a princípio smartphones). Para isso **a folha tarefa a ser disponibilizada para o coletor deve ser a folha tarefa do tipo Coletor Móvel;**
* Permite o sincronismo de informações para o coletor móvel e o gerenciamento dos apontamentos realizados e sincronizados;
* Depende do cadastro do projeto;
* Uma Folha Tarefa poderá se encontrar em uma das seguintes situações:
  + **Em Processamento**: Folha Tarefa criada, porém ainda não disponibilizada para os dispositivos de coleta de dados;
  + **Disponível para Coletor (Gerada)**: Folha Tarefa cadastrada e disponível para o coletor;
  + **Pronta para Impressão**: Folha Tarefa disponível para impressão e coleta através do leitor de código de barras;
  + **Encerrada**: Folha Tarefa encerrada. O PERT já foi atualizado. Esta situação significa que todos os dados dos coletores já foram recebidos para todas as tarefas, validados e atualizados no PERT;
  + **Cancelada**: Folha Tarefa cancelada. Não permite qualquer outra operação. Os dados das tarefas (por exemplo, oriundos de coletores) desta Folha não poderão gerar atualização no PERT e não poderão ser importadas informações dos coletores;
  + **Associada ao coletor**: Folha Tarefa foi enviada ao coletor móvel;
  + **Apontada**: Folha Tarefa possui apontamentos em seus itens após a mesma ter sido fechada no coletor.
* A data fim da Folha é calculada conforme a periodicidade informada e o valor do parâmetro “Quebra por períodos do Cronograma”, exceto quando a periodicidade é definida como **Personalizada**;
* Primeiramente determina-se o valor da data fim de acordo com a periodicidade:
  + **Semanal**: Se Soma seis dias a data inicial;
  + **Quinzenal**: Se Soma quatorze dias a data inicial;
  + **Mensal**: Se Soma trinta dias a data inicial;
  + **Personalizada**: Permite a alteração manual das datas início e fim.
* Posteriormente, caso o parâmetro “Quebra por períodos do Cronograma” esteja selecionado, será verificado se existe algum fim de período no cronograma entre as datas inicial e final informadas na Folha. Caso exista, o valor encontrado será utilizado como data fim da folha e será exibida uma mensagem contendo informações sobre a quebra. Posteriormente, o usuário poderá cadastrar um novo item a fim de complementar o período. Caso contrário, será exibida uma mensagem de erro, informando que não foi possível encontrar um intervalo de cronograma. Esse parâmetro somente estará habilitado se a periodicidade padrão for diferente de Personalizada.

* **Parâmetro da folha tarefa habilitado**
  + Ao habilitar o Parâmetro 'Utiliza Folha Tarefa', a Folha Tarefa será exibida no Menu de Mobilidade e em todos os locais no app Minha Obra.
  + Ao realizar o sincronismo com o app Minha Obra, todas as Folhas Tarefas associadas ao coletor, serão enviadas para o mesmo e ficarão disponíveis para apontamento.
  + Na associação de projeto ao coletor o usuário pode informar um filtro de tarefas adicionais, que são as tarefas que serão sincronizadas para o App caso o projeto não use Folha Tarefa.

* + **Coletores Associados à Folha Tarefa**
    - Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Básico \ Mobilidade \ Folhas Tarefa \ Anexos \ Coletores Associados a Folha Tarefa;
    - Neste anexo o usuário deverá associar os coletores que a folha tarefa poderá ser sincronizada.
    - Não será possível incluir novos coletores caso a folha tarefa esteja com status de cancelada ou Encerrada.
    - Não será possível excluir coletores que já possuem status de ‘associado ao coletor’.
    - **Processo de Associar Coletor à Folha Tarefa**
      * Permite a associação de coletores à folha tarefa selecionada:
        + Para sua execução é necessário que o status da folha seja "Em Processamento", "Gerada" ou "Associada ao Coletor";
        + São exibidos apenas os coletores que tem o projeto corrente associado;
        + São exibidos apenas os coletores que tem usuários associados;
  + **Itens da Folha Tarefa**
    - Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Básico \ Mobilidade \ Folhas Tarefa \ Anexos \ Itens da Folha Tarefa;
    - As tarefas de uma Folha Tarefa são as atividades que foram planejadas para serem executadas nas frentes de obra em dado intervalo de tempo. É do progresso destas tarefas que deve ser obtido os apontamentos através do uso de coletores móveis pelos responsáveis por tais funções;
    - A inserção das tarefas da Folha Tarefa se baseará, única e exclusivamente, na planilha de atividades do TOP. Este anexo contém as tarefas da planilha de atividades e ainda possui campos adicionais;
    - Para seleção das tarefas para a Folha Tarefa o sistema disponibiliza algumas formas de fazê-lo:
      * Cadastro padrão inserindo uma tarefa por vez;
      * Processo que permitirá selecionar várias tarefas ao mesmo tempo e inseri-las;
      * “Drag-and-Drop”, o usuário deverá abrir a planilha de atividades e o anexo de itens da Folha tarefa lado a lado, arrastando e soltando as tarefas para o anexo de itens.
    - Em qualquer situação de apresentação das tarefas da planilha de atividades, para seleção/inserção como tarefa da Folha, as tarefas da planilha de atividades são filtradas de acordo com as datas de início e fim da Folha previamente cadastrada;
    - Este filtro deve ser aplicado nos campos início e fim programado das tarefas da planilha de atividades e serão exibidas (da Planilha de Atividades, Seleção múltipla, cadastro padrão) somente as tarefas que façam interseção com o período informado.
* A partir do APP Minha Obra é possível criar/alterar medições de itens de contrato através dos apontamentos de Avanço Físico dos itens da Folha Tarefa, sendo via coletor ou apontamento manual. Para que essa incidência ocorra, é necessário vincular o contrato desejado ao item associado à folha tarefa, porém é necessário considerar algumas premissas:

  + A tarefa deve ser definida antes do contrato;
  + As datas início e fim do contrato devem fazer interseção com as datas início e fim da folha tarefa;
  + A tarefa selecionada deve estar associada ao contrato;
  + Ao salvar a associação do contrato ao item, caso o parâmetro de medição acima de 100% estiver diferente de SEMPRE PERMITIR, será verificado se a quantidade planejada do item da folha é maior que a quantidade do saldo do item no contrato, o que não deve ser permitido.

  No processo de Validar Apontamento de Avanço Físico o parâmetro de medição acima de 100% também é verificado e se estiver diferente de SEMPRE PERMITIR, e a quantidade apontada do item da folha for maior que a quantidade do saldo do item no contrato, um alerta será exibido, não permitindo a execução.

  No processo de Atualizar PERT o parâmetro de medição acima de 100% também é verificado e se estiver diferente de SEMPRE PERMITIR, e a quantidade apontada do item da folha for maior que a quantidade do saldo do item no contrato, um alerta será exibido, não permitindo a execução. Caso as validações estejam aprovadas, a quantidade apontada do item será incorporada à medição do item no contrato, no respectivo período que corresponde à DATA DE APONTAMENTO do item da folha. Se o período do contrato estiver liberado, a medição não será inserida e o erro deverá ser exposto.

  Na tela de medição de itens, nos períodos do contrato, é possível consultar os apontamentos que influenciaram na medição do item corrente, basta selecionar o item no grid e clicar no botão .
* **Programado X Alocado**
* Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Básico \ Mobilidade \ Folha Tarefa \ Anexos \ Programado X Alocado;
* Esta visão exibe informações relacionadas com as quantidades programadas e quantidades alocadas de cada Tarefa. Exibe somente insumos do tipo mão de obra, necessários para a execução da tarefa;
* Na medida em que as Equipes forem alocadas na tarefa, será atualizado o campo de quantidade de horas alocadas por insumo. Estes dados ficarão disponíveis somente para consulta, para que o usuário tenha uma noção do quanto já foi alocado na tarefa e quanto ainda precisa ser alocado, ou mesmo se houve super alocação de horas na tarefa.

* + **Recalcular planejamento das tarefas**
    - Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Básico \ Mobilidade \ Folhas Tarefa \ Processos \ Recalcular planejamento das tarefas;
    - Recalcular as quantidades planejadas utilizando o mesmo cálculo quando a tarefa é associada à folha.
  + **Disponibilizar Folha para Envio**
    - Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Básico \ Mobilidade \ Folhas Tarefa \ Processos \ Disponibilizar Folha para Envio;
    - Disponibiliza a folha tarefa do tipo de apontamento “coletor” para envio.
  + **Copiar Folha Tarefa**
    - Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Básico \ Mobilidade \ Folhas Tarefa \ Processos \ Copiar Folha Tarefa;
    - Permite realizar a cópia de uma Folha Tarefa selecionada;
    - Somente folhas com o status de Cancelada ou Encerrada podem ser copiadas;
      * Cancelada: Serão copiados apenas os itens associados a folha tarefa origem respeitando as validações de associação de itens a folha;
      * Encerrada: Serão copiados os itens associados a folha tarefa origem respeitando as validações e regras de associação de itens a folha e também as alocações de equipe respeitando as validações e regras de alocação de Equipe.
    - Os Campos Periodicidade e Tipo de Apontamento exibem os valores definidos na folha origem da cópia;
    - Os Campos Data Início e Descrição estão disponíveis para a criação da nova folha tarefa;
    - Copiar Alocação de Equipe: esta flag estará visível somente quando a folha estiver com status Encerrada.
  + **Cancelar Folha Tarefa**
    - Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Básico \ Mobilidade \ Folhas Tarefa \ Processos \ Cancelar Folha Tarefa;
    - Permite realizar o cancelamento da Folha Tarefa selecionada.
  + **Relatório Folha Tarefa**
    - O relatório**TOPREL0030 - Folha Tarefa por equipe (Mobilidade).TotvsReport** pode ser encontrado no book de relatórios e sua geração disponibiliza os códigos de barras para serem utilizados no APP Minha Obra. A geração do relatório é através do menu Projetos \ Construção e Projetos \ Relatórios \ Mobilidade \ Folha tarefa.

* Campos da Folha Tarefa impressa:
  + Número da Folha Tarefa;
  + Nome da Folha Tarefa;
  + Data de Criação;
  + Data da Carga no Coletor;
  + Data de Início da Execução;
  + Coletor;
  + Código da Tarefa;
  + Nome da Tarefa;
  + Centro de Custo;
  + Quantidade no Período;
  + Quantidade Total;
  + Saldo a Executar;
  + Unidade de serviço;
  + Executado 100% (Checkbox);
  + Código de barras;
  + Responsável pela Execução.
* O código de barras contém informações suficientes para que em sua leitura o sistema consiga identificar de qual projeto/obra/tarefa está se referindo o valor do apontamento e seja capaz de gravá-lo.

* + **Interface de Coleta Via Código de Barras**
    - Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Básico \ Mobilidade \ Folhas Tarefa \ Anexos \ Interface de Coleta Via Código de Barras;
    - O menu de acesso à Interface de Coleta via Leitura de Código de Barras somente está disponível para Folhas Tarefa com o status “Pronta para Impressão”, ou seja, ao selecionar na visão, uma folha com o status diferente do citado, o menu ficará desabilitado. Além disso, o processo só pode ser acessado caso a folha tenha o tipo de apontamento manual;
    - O anexo de Tarefas da Folha Tarefa já possui uma série de informações sobre as tarefas e será disponibilizada uma área com controles e tratamentos específicos para se efetuar a leitura dos códigos de barra e atualização do sistema a partir dos dados informados nesta área;
    - Nela contém um indicador de 100%, um campo para o código de barras e botões com percentuais de completude (0%, 25%, 50%, 75%);
    - Esta interface será apresentada de acordo com perfil do usuário que indica os usuários que irão realizar a leitura do código de barras, direto no sistema, terão de ter permissão para fazê-lo;
    - O usuário marca o indicador de 100% e realizará a leitura do código de barras. Em seguida, o sistema irá interpretar este código de barras identificado a qual tarefa se refere e atualizará o campo de apontamento com o 100%;
    - Pode ocorrer da tarefa não estar com 100% de completude, então o usuário pode desmarcar o indicador de 100%, efetuar a leitura do código de barras e selecionar o percentual de completude (0%, 25%, 50%, 75%). Ao efetuar esta seleção o sistema irá interpretar este código de barras identificando a qual tarefa se refere e atualizará o campo de apontamento de acordo com o percentual selecionado. As informações serão gravadas em uma tela de validação, não atualizando diretamente o PERT.

Sem Utilizar Folha Tarefa

As tarefas que irão estar visíveis para o apontamento do coletor seguem o seguinte padrão:

* Na associação de projeto ao coletor o usuário pode informar um filtro para o sincronismo das tarefas
* O Filtro criado segue o mesmo padrão de filtros do RM.
* Os campos passíveis a serem utilizados neste filtro são correspondentes as tabelas que se relacionam com as Tarefas, como.: Cronograma Previsto, Local de Serviço, Unidade de Serviço.

* Após definir o Projeto e o Filtro, é possível testar o mesmo e visualizar as tarefas que serão sincronizadas para o respectivo coletor, basta clicar no botão abaixo do Filtro que a tela de "Tarefas do filtro avançado a serem sincronizadas" será aberta com suas respectivas tarefas. Se nenhuma tarefa for exibida é porque nenhuma delas se encaixa nas condições definidas no filtro.
* Caso não haja filtro definido o sistema disponibiliza para o sincronismo uma seleção padrão com as Tarefas que tem o cronograma planejado definido em períodos que correspondam ao intervalo da data corrente menos 15 dias e mais 15 dias;
* Caso o **projeto** esteja parametrizado **utilizando PERT** poderão ser associadas **somente as tarefas** que possuírem **percentual concluído inferior a 100%**.
* Caso o **projeto** esteja parametrizado **sem utilização do****PERT**, poderão ser associadas **somente tarefas** que possuírem percentual do **cronograma realizado inferior a 100%**;
* Se o projeto utiliza travamento de períodos do cronograma planejado, apenas os passíveis de utilização serão considerados.

Coletores Móveis

A utilização de coletores móveis se dará através do número de licenças adquiridas, ou seja, cada licença será correspondente a um coletor. Caso exista o número de coletores correspondente ao número máximo de licenças adquiridas ativas, não será permitido a ativação de novos coletores.   

Importante

* **Uma mesma licença de coletor pode ser utilizada para os aplicativos Minha Obra e Minhas Inspeções, porém será necessário realizar dois cadastros, um para cada aplicativo com o seu respectivo ID do App.**

Para o cadastro de coletores, obrigatoriamente o usuário deverá informar o nome, o modelo e informar se o coletor está ativo para utilização ou não. Estes campos devem ser preenchidos de acordo com o detalhamento abaixo:

* **ID do App:** número único de identificação do coletor/aplicativo;
* **Ativo:** a representação do coletor ativo será feita quando o campo "Ativo" estiver selecionado. Para desativá-lo será necessário retirar a seleção do campo;
* **Nome:** a descrição do coletor para diferenciar os coletores cadastrados;
* **Modelo:** será preenchido de acordo com as características de modelo do equipamento;
* **Aplicativo:** define qual aplicativo irá utilizar o coletor cadastrado.

Para as funções abaixo, pode-se utilizar as respectivas teclas de atalho:

* Inclusão: Ctrl + Ins
* Exclusão: Ctrl +Del
* Edição: Ctrl + Enter

O **ID do App** pode ser visualizado na tela inicial do App Minha Obra ou ao selecionar o tipo de configuração manual. Caso seja selecionada a configuração manual o ID do APP será exibido no topo da configuração.

* **Ativar Coletores Móveis:**

Para ativar coletores móveis para uso do sistema, o usuário deverá selecionar o coletor na visão de cadastro de coletores e acessar o Menu Processos | Ativar Coletores Móveis .

Para verificar o status atual do(s) coletor (es), o sistema exibirá uma visão de uma tabela com o status (Ativo ou Inativo), permitindo ao usuário selecionar apenas coletores desativados.

Caso o processo de ativação seja executado e o usuário tenha selecionado coletores com status inativos, o sistema irá mantê-los ativos e irá alterar apenas o status dos que estavam inativos, alterando para o status Ativo.

**Observação:**

1. Caso o usuário selecione vários coletores para ativação ou para desativação e entre estes possua coletores que já estavam ativos na ativação ou inativos na desativação, o sistema executará o processo para os demais, sem interromper o processo. Apenas irá ignorar os coletores que já estiverem no status desejado.
2. O Coletor Móvel será cadastrado de forma global e poderá estar vinculado com tantos projetos quantos forem necessários.  
   A utilização de coletores móveis se dará através do número de licenças adquiridas, ou seja, cada licença será correspondente a um coletor. Caso exista o número de coletores correspondente ao número máximo de licenças adquiridas ativas, não será permitido a ativação de novos coletores.

**Validações:**

1. Verifica se a última desativação do coletor é maior que 5 dias, pois somente é possível ativar o coletor se for a primeira ativação ou se a sua desativação é maior que o número de dias citado;
2. Verifica se existem licenças para utilização de coletores;
3. Verifica se existe algum coletor com o controle de CRC inválido;
4. Verifica se o número de coletores ativos atingiu o número de licenças adquiridas.

* **Desativar Coletores Móveis:**

Para desativar coletores móveis, o usuário deverá selecionar o(s) coletor(es) na visão de cadastro de coletores (Cadastros | Mobilidade | Coletores Móveis) e acessar o menu Processos | Desativar Coletores Móveis.

Nesse processo existe a opção de "Migrar vínculos do(s) coletor(es) selecionado(s)", que possibilita que todas as informações relacionadas ao(s) coletor(es) de origem selecionado(s) sejam associadas ao coletor de destino. Ao executar o processo as relações de Projetos, Usuários de Coletores, Itens de Folhas Tarefas e Apontamentos serão associadas ao novo coletor. o coletor de destino será ativado automaticamente.

Se a opção de "Migrar vínculos do(s) coletor(es) selecionado(s) não estiver sido selecionada a seguinte mensagem será exibida antes da execução do processo:

Quando o coletor for desativado, todos os vínculos serão excluídos.

**Validações:**

1. Verifica se existe algum coletor com o controle de CRC inválido;
2. Verifica se o coletor selecionado está ativo;
3. Verifica se o usuário possui acesso aos projetos associados ao coletor que será desativado.

**Observação:**

1. Caso o usuário selecione vários coletores para ativação ou para desativação e entre estes possua coletores que já estavam ativos na ativação ou inativos na desativação, o sistema executará o processo para os demais, sem interromper o processo. Apenas irá ignorar os coletores que já estiverem no status desejado.
2. O Coletor Móvel será cadastrado de forma global e poderá estar vinculado com tantos projetos quantos forem necessários.  
   A utilização de coletores móveis se dará através do número de licenças adquiridas, ou seja, cada licença será correspondente a um coletor. Caso exista o número de coletores correspondente ao número máximo de licenças adquiridas ativas, não será permitido a ativação de novos coletores.
Associação de Projeto ao Coletor

Através desta funcionalidade, o usuário poderá associar quantos projetos forem necessários à um coletor, sendo feita essa associação através do Menu Cadastros | Mobilidade | Coletores Móveis | Anexos | Associação de Projeto(s) a Coletor, que realizará o vínculo do projeto ao Coletor Móvel.

* **Parâmetro da folha tarefa habilitado**
  + Ao habilitar o Parâmetro 'Utiliza Folha Tarefa', a Folha Tarefa será exibida no Menu de Mobilidade e em todos os locais no app Minha Obra.
  + Ao realizar o sincronismo com o app Minha Obra, todas as Folhas Tarefas associadas ao coletor, serão enviadas para o mesmo e ficarão disponíveis para apontamento.
  + Na associação de projeto ao coletor o usuário pode informar um filtro de tarefas adicionais, além da Folha Tarefa para apontamento de Equipamentos e apontamento avulso de Mão de Obra.
* **Parâmetro da folha tarefa desabilitado**
  + Ao desabilitar o Parâmetro 'Utiliza Folha Tarefa', a Folha Tarefa não será exibida no Menu de Mobilidade e em todos os locais no app Minha Obra.
  + Ao realizar o sincronismo com o app Minha Obra, será criada uma folha tarefa interna do sistema para retornar as tarefas.
  + Na associação de projeto ao coletor o usuário pode informar um filtro para o sincronismo das tarefas

Para associar Projeto(s) a Coletor, o coletor deverá está ativo;  
Para associar mais de um Projeto a Coletor, é necessário parametrizar a opção "Utiliza mais de um projeto por coletor móvel", através do Menu Opções | Parâmetros |TOTVS Obras e Projetos | Gerais | aba Mobilidade.

Usuários de Coletores Móveis

Através desta funcionalidade, serão cadastrados os usuários que poderão utilizar os coletores móveis para realizar apurações e apontamentos das tarefas.

Informe os dados:

**Nome:** Nome completo do usuário do ERP.   
**Usuário**: Código do usuário do ERP  (identificador único).  
**Ativo**: Este campo indica o status do usuário, e por default, virá marcado como ativo. Caso o usuário queira cadastrar o usuário como inativo, ele deve desmarcar esta opção.  
**Permissões:** Através desses campos serão informada as permissões que o usuário terá ao coletor e, consequentemente, às Folhas Tarefa:

1. Apontamento de Avanço Físico: Com esta permissão marcada, o usuário terá acesso a efetuar "Apontamento de Avanço Físico";
2. Apontamento de Mão de Obra: Com esta permissão marcada, o usuário terá acesso a efetuar "Apontamento de Mão de Obra";
3. Apontamento de Equipamentos: Com esta permissão marcada no cadastro, o usuário terá acesso a efetuar  "Apontamento de Controle de Equipamentos";
4. Apontamento de Ciclo de Transporte: Com esta permissão marcada no cadastro, o usuário terá acesso a efetuar "Apontamento de Ciclo de Transporte";
5. Pedido: Com esta permissão marcada no cadastro, o usuário terá acesso ao portal de Pedidos através do app Minha Obra;
6. Pedido Extra: Com esta permissão marcada no cadastro, o usuário terá acesso ao portal de Pedidos Extras através do app Minha Obra;
7. Movimentações de Produtos: Com esta permissão marcada no cadastro, o usuário terá acesso à solicitação de materiais ao almoxarifado através do módulo de Suprimento/Faturamento.

**Importante:**

* O usuário cadastrado nesta tela, obrigatoriamente, não possuirá nenhum vínculo com o cadastro de pessoas que é integrado à Folha de Pagamento.   
  Este usuário será cadastrado como usuário do TOTVS Construção Obras e Projetos e deverá ser associado a um perfil, que possua permissão para realizar apontamentos e o sincronismo dos dados dos coletores móveis;
* Para que um mesmo usuário esteja em mais de uma Coligada, é necessário fazer o cadastro do mesmo em ambas as Coligadas, assim com a associação de coletores à estes usuários;
* Para que o coletor utilize as funcionalidades Pedido e Pedido extra é necessário definir a permissão de o Portal TOTVS Obras e Projetos deve estar configurado.
* No APP Minha Obra existem as opções de acesso ao Portal do TOTVS Obras e Projetos para as funcionalidades de Pedido e Pedido Extra. Para a utilização desses itens de menu, é necessário definir a permissão de acesso no cadastro de usuários de coletores. Após essa definição, basta realizar o sincronismo com o coletor que as opções estarão disponíveis tanto no menu principal quanto no menu lateral do APP Minha Obra.
Associação de Coletores a Usuários

Na visão de cadastro de usuários de coletores, o usuário poderá fazer o vínculo e visualizar quais coletores estão associados ao usuário,através do Menu Cadastros | Mobilidade | Usuários de Coletores Móveis | Anexos | Associação de Coletor a Usuário(s).

Por definição, cada usuário de coletor móvel ativo somente poderá estar associado a 1 (um) único coletor móvel.

Esta validação será executada no momento da vinculação do coletor.

Caso o usuário opte por permitir a vinculação de mais de 1 (um) coletor por usuário, o mesmo deverá alterar o parâmetro "Utiliza mais de um coletor móvel por usuário" disponível em Opções | Parâmetros | TOTVS Obras e Projetos | Gerais | aba Mobilidade.

Caso o parâmetro não esteja habilitado, o sistema não permitirá associar mais de um coletor a este usuário.

**Atenção:**  
Somente os coletores ativos poderão ser vinculados ao usuário. Serão exibidos apenas coletores ativos, não sendo possível associação de coletores desativados.

Associação de Equipamentos a Usuários

**Equipamentos Associados a Usuários**

* Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Básico \ Mobilidade \ Usuários de Coletores Móveis\ Anexos \ Equipamentos Associados ao Usuário;
* No cadastro de usuário de coletores móveis pode ser realizado a associação de equipamentos que serão utilizados pelo usuário, este como Operador de Equipamentos, no coletor;
* Os equipamentos que estarão disponíveis para a associação ao usuário são os que foram associados aos projetos (Projetos \ Construção e Projetos \ Controle \ Básico \ Mobilidade \ Equipamentos \ Equipamentos Associados ao Projeto) que estão relacionados ao coletor no qual o usuário utilizará;
* Somente será possível associar equipamentos, se existirem coletores associados ao usuário;
* Ao realizar o sincronismo no coletor, essas informações serão enviadas. Ao solicitar a inclusão de entrada de apontamento de equipamento, a tela de equipamentos associados será exibida para que o equipamento seja selecionado. Detalhes sobre essa função estão exemplificadas no módulo de equipamentos neste documento;
* **Validações:**
  + Inclusão e Alteração:
    - Valida se existe coletor associado ao usuário, pois os equipamentos são originários dos projetos associados ao coletor;
    - Valida se o usuário do coletor é Operador de Equipamentos.

**Processo de Associar Equipamentos ao Usuário**

* Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Mobilidade \ Usuários de Coletores Móveis\ Processos \ Associar Equipamentos ao Usuário;
* Através deste processo, é possível realizar a associação de vários equipamentos de uma só vez;
* São exibidos apenas os equipamentos que não estão associados ao usuário;
* As validações são as mesmas da inclusão unitária.
Sincronismo

**Entenda o Sincronismo (Envio e recebimento do coletor)**

* Para que o sincronismo possa ser realizado, é necessário que o WebService que receberá e enviará informações esteja ativo;
* É necessário dispor de um coletor móvel ou utilizar um emulador;
* Com a aplicação Minha Obra no coletor aberta, realizar o sincronismo com o usuário e senha de acesso a base de dados do TOP, ou seja, usuário definido para utilização do coletor;

As configurações de sincronismo podem ser realizadas manualmente ou através da leitura do QR Code que guarda as configurações:

* **Configuração Automática:**

 

Selecionando a opção automática deverá apontar o leitor para o QR Code gerado no sistema para configuração automática:

* **Geração do QR Code:**

Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Mobilidade \ Usuários de Coletores Móveis\ Processos \QR Code para Configuração Automática do Sincronismo do App Minha Obra:

* **Configuração Manual:**

Basta digitar a URL:

Mapas de Apontamentos

* Durante o registro do apontamento no coletor, informações de localização (coordenadas GPS) serão coletadas e enviadas no sincronismo para o banco de dados do sistema.
* Com isso, será possível visualizar as posições dos apontamentos no sistema.
* Para habilitar a visualização de mapas é necessário configurar a chave de acesso ao Google Maps:

+ Menu: Ambiente -> Parâmetros -> Parâmetros Gerais -> Aba Google -> Chave de identificação para Google Maps
+ Como configurar a chave de acesso: [http://tdn.totvs.com/pages/viewpage.action?pageId=42043762](https://tdn.totvs.com/pages/viewpage.action?pageId=42043762)

* + Observação: É necessário configurar apenas a chave de acesso, não existe a necessidade de configurar o portal com IIS (Internet Information Services).  
      
      
    - Observação:
    * O aplicativo Minha Obra deverá coletar as coordenadas GPS em intervalos de 1 minuto.
    * A precisão das coordenadas GPS será de 50 metros e deverá funcionar em ambientes abertos.
