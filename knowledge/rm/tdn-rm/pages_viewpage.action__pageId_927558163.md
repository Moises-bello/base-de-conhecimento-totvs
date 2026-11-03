---
content_hash: 7bde88848a1533e2c1d7ae307154e2df0860f0dccd777fbd0cf6cee9b7627e83
fetched_at: '2026-06-29T00:12:07.996750+00:00'
page_id: '927558163'
product: rm
source: tdn-rm
title: Instalação e Configuração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=927558163
version: 25
---

---

Para instalar o app **Minha Obra**, basta acessá-lo nas lojas oficiais do **Android** . Clique na imagem abaixo para ser redirecionado ao site.

---

---

**Pré Requisitos**

* **Android:**
  + Android 10 ou superior
  + Memória 2 GB
  + Wi-Fi
  + GPS
  + Câmera 5.0 Mpixels
  + Processador 1.5 GHz Quad Core
  + Tela 5.0"
  + Resolução Mínima 480 X 854

    ---

**Após instalar o app, recomendamos o uso do acelerador de implantação para facilitar e agilizar sua configuração e utilização no Minha Obra.**

---

Esta funcionalidade do TOTVS Construção Obras e Projetos está disponível a partir da versão 12.1.32 e possibilita que a configuração do ambiente de Integração com app Minha Obra

seja realizado de forma simples e rápida. [Acelerador de Implantação - App Minha Obra](https://tdn.totvs.com/pages/viewpage.action?pageId=603105707)

---

**Caso não deseje utilizar o acelerador é possível configurar manualmente pelos passos descritos abaixo. Lembrando que pelo acelerador é mais simples é mais agil.**

---

Antes de inciar a sua configuração oficial você pode acessar a utilização de uma versão demontração onde informações fictícias são inseridas no banco de dados do aplicativo.

**1 - Download Aplicativo:**

<https://play.google.com/store/apps/details?id=com.totvs.topmobile>

| 2 - Configuração Automática | 3 - Configuração Manual | 4 - Base Demonstrativa |
| --- | --- | --- |
|  |  |  |

Caso a opção escolhida para configuração seja automática:

É indicado utilizar na configuração QRCode a url de sincronismo apontando para o host.

Porem nada impede que configure uitlizando ISS de forma manual.

Para utilizar o QR Code para configuração automatica informe a url sincronismo (host). Para ISS somente de forma manual.

**Geração do QR Code:**

Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Minha Obra\ Usuários de Coletores Móveis\ Processos \QR Code para Configuração Automática do Sincronismo do App Minha Obra:

**Configuração Manual:**

Basta digitar a URL:

Url sincronismo ISS - API (Opcional quando desejo usar o ISS)

Url sincronismo HOST- API (Indicado)

Após a definição das informações de sincronismo, o mesmo é executado e as informações sincronizadas com o TOTVS Construção Obras e Projetos.

Caso ocorra algum erro no processo de sincronismo, será possível visualizar em qual etapa ocorreu e expandir o mesmo para mais detalhes.

   

É possível realizar a configuração do sincronismo para que seja realizado de forma automática. O Minha Obra possibilita que seja definido o intervalo de tempo em minutos do sincronismo e o tipo de rede que será executado: Wifi, Wifi e Celular (3g).

    

O Minha Obra possibilita a utilização de uma versão de demonstração onde informações fictícias são inseridas no banco de dados do aplicativo. Com essa versão de demonstração não é possível realizar o sincronismo. Para ativá-la, basta limpar o conteúdo do campo WebService da tela de configuração manual e clicar no botão a seguir:

     

---

**Informações gerais sobre o app Minha Obra**

Caso o Teclado numérico padrão do seu aparelho exiba incorretamente a formatação decimal nos apontamentos como a imagem abaixo:

Recomendamos que faça o Download de um novo Teclado para que seja possível realizar apontamentos com casas decimais. Ex.: Teclado Gboard Google (Play Store).

A partir do **Android 12** é necessário atribuir a seguinte permissão para realizar a comunicação do coletor com as impressoras:

| 1) Informações do aplicativo Minha Obra | 2) Dispositivos por perto na Secção Não Permitido | 3) Pressionar a opção Permitir |
| --- | --- | --- |
|  |  |  |

Parâmetros Gerais

Ao optar realizar os cadastros básicos sem o apoio do assistente de implantação é importante:

Permitir enviar imagens ao coletor e permitir registrar fotos em apontamentos no coletor.

Definir se irá utilizar folha tarefa

Veja os detalhes :

Veja também a documentaçao completa : 

Associar coletor a folha tarefa e associar usuarios ao coletor

Veja em:

Incluir itens na folha tarefa

Veja em:

Disponibilizar folha para envio

Veja em :

Copiar Folha Tarefa

Veja em:

Cancelar Folha Tarefa

Relatório

* O relatório**TOPREL0030 - Folha Tarefa por equipe (Mobilidade).TotvsReport** pode ser encontrado no book de relatórios e sua geração disponibiliza os códigos de barras para serem utilizados no APP Minha Obra. A geração do relatório é através do menu Projetos \ Construção e Projetos \ Relatórios \ Mobilidade \ Folha tarefa.

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

* Interface de coleta via código de barras

* Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Básico \ Mobilidade \ Folhas Tarefa \ Anexos \ Interface de Coleta Via Código de Barras;
* O menu de acesso à Interface de Coleta via Leitura de Código de Barras somente está disponível para Folhas Tarefa com o status “Pronta para Impressão”, ou seja, ao selecionar na visão, uma folha com o status diferente do citado, o menu ficará desabilitado. Além disso, o processo só pode ser acessado caso a folha tenha o tipo de apontamento manual;
* O anexo de Tarefas da Folha Tarefa já possui uma série de informações sobre as tarefas e será disponibilizada uma área com controles e tratamentos específicos para se efetuar a leitura dos códigos de barra e atualização do sistema a partir dos dados informados nesta área;
* Nela contém um indicador de 100%, um campo para o código de barras e botões com percentuais de completude (0%, 25%, 50%, 75%);
* Esta interface será apresentada de acordo com perfil do usuário que indica os usuários que irão realizar a leitura do código de barras, direto no sistema, terão de ter permissão para fazê-lo;
* O usuário marca o indicador de 100% e realizará a leitura do código de barras. Em seguida, o sistema irá interpretar este código de barras identificado a qual tarefa se refere e atualizará o campo de apontamento com o 100%;
* Pode ocorrer da tarefa não estar com 100% de completude, então o usuário pode desmarcar o indicador de 100%, efetuar a leitura do código de barras e selecionar o percentual de completude (0%, 25%, 50%, 75%). Ao efetuar esta seleção o sistema irá interpretar este código de barras identificando a qual tarefa se refere e atualizará o campo de apontamento de acordo com o percentual selecionado. As informações serão gravadas em uma tela de validação, não atualizando diretamente o PERT.

**Não Utiliza Folha Tarefa**

As tarefas que irão estar visíveis para o apontamento do coletor seguem o seguinte padrão:

* Na associação de projeto ao coletor o usuário pode informar um filtro para o sincronismo das tarefas
* O Filtro criado segue o mesmo padrão de filtros do RM.
* Os campos passíveis a serem utilizados neste filtro são correspondentes as tabelas que se relacionam com as Tarefas, como.: Cronograma Previsto, Local de Serviço, Unidade de Serviço.

* Após definir o Projeto e o Filtro, é possível testar o mesmo e visualizar as tarefas que serão sincronizadas para o respectivo coletor, basta clicar no botão abaixo do Filtro que a tela de "Tarefas do filtro avançado a serem sincronizadas" será aberta com suas respectivas tarefas. Se nenhuma tarefa for exibida é porque nenhuma delas se encaixa nas condições definidas no filtro.
* Caso não haja filtro definido o sistema disponibiliza para o sincronismo uma seleção padrão com as Tarefas que tem o cronograma planejado definido em períodos que correspondam ao intervalo da data corrente menos 15 dias e mais 15 dias;
* Caso o **projeto** esteja parametrizado **utilizando PERT** poderão ser associadas **somente as tarefas** que possuírem **percentual concluído inferior a 100%**.
* Caso o **projeto** esteja parametrizado **sem utilização do****PERT**, poderão ser associadas **somente tarefas** que possuírem percentual do**cronograma realizado inferior a 100%**;
* Se o projeto utiliza travamento de períodos do cronograma planejado, apenas os passíveis de utilização serão considerados.

**Coletores Móveis**

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

O **ID do App** pode ser visualizado na tela inicial do App Minha Obra ou ao selecionar o tipo de configuração manual. Caso seja selecionada a configuração manual o ID do APP será exibido no topo da configuração.

 

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

**Associação de Projetos aos Coletores**

Através desta funcionalidade, o usuário poderá associar quantos projetos forem necessários à um coletor, sendo feita essa associação através do Menu Cadastros | Mobilidade | Coletores Móveis | Anexos | Associação de Projeto(s) a Coletor, que realizará o vínculo do projeto ao Coletor Móvel.

* **Parâmetro da folha tarefa habilitado**

* Ao habilitar o Parâmetro 'Utiliza Folha Tarefa', a Folha Tarefa será exibida no Menu de Mobilidade e em todos os locais no app Minha Obra.
* Ao realizar o sincronismo com o app Minha Obra, todas as Folhas Tarefas associadas ao coletor, serão enviadas para o mesmo e ficarão disponíveis para apontamento.

* **Parâmetro da folha tarefa desabilitado**

* Ao desabilitar o Parâmetro 'Utiliza Folha Tarefa', a Folha Tarefa não será exibida no Menu de Mobilidade e em todos os locais no app Minha Obra.
* Ao realizar o sincronismo com o app Minha Obra, será criada uma folha tarefa interna do sistema para retornar as tarefas.
* Na associação de projeto ao coletor o usuário pode informar um filtro para o sincronismo das tarefas

Para associar Projeto(s) a Coletor, o coletor deverá está ativo;  
Para associar mais de um Projeto a Coletor, é necessário parametrizar a opção "Utiliza mais de um projeto por coletor móvel", através do Menu Opções | Parâmetros |TOTVS Obras e Projetos | Gerais | aba Mobilidade.

**Usuários de  Coletores Móveis**

Através desta funcionalidade, serão cadastrados os usuários que poderão utilizar os coletores móveis para realizar apurações e apontamentos das tarefas.

Informe os dados:

**Nome:** Nome completo do usuário do ERP.  
**Usuário**: Código do usuário do ERP  (identificador único).  
**Ativo**: Este campo indica o status do usuário, e por default, virá marcado como ativo. Caso o usuário queira cadastrar o usuário como inativo, ele deve desmarcar esta opção.  
**Permissões:** Através desses campos serão informada as permissões que o usuário terá ao coletor e, consequentemente, às Folhas Tarefa:

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
* Para que o coletor utilize as funcionalidades Pedido e Pedido extra é necessário definir a permissão de o Portal da Obra deve estar configurado.
* No APP Minha Obra existem as opções de acesso ao Portal da Obra para as funcionalidades de Pedido e Pedido Extra. Para a utilização desses itens de menu, é necessário definir a permissão de acesso no cadastro de usuários de coletores. Após essa definição, basta realizar o sincronismo com o coletor que as opções estarão disponíveis tanto no menu principal quanto no menu lateral do APP Minha Obra.

**Associação de  Coletores a Usuários**

Na visão de cadastro de usuários de coletores, o usuário poderá fazer o vínculo e visualizar quais coletores estão associados ao usuário,através do Menu Cadastros | Mobilidade | Usuários de Coletores Móveis | Anexos | Associação de Coletor a Usuário(s).

Por definição, cada usuário de coletor móvel ativo somente poderá estar associado a 1 (um) único coletor móvel.

Esta validação será executada no momento da vinculação do coletor.

Caso o usuário opte por permitir a vinculação de mais de 1 (um) coletor por usuário, o mesmo deverá alterar o parâmetro "Utiliza mais de um coletor móvel por usuário" disponível em Opções | Parâmetros | TOTVS Obras e Projetos | Gerais | aba Mobilidade.

Caso o parâmetro não esteja habilitado, o sistema não permitirá associar mais de um coletor a este usuário.

**Atenção:**  
Somente os coletores ativos poderão ser vinculados ao usuário. Serão exibidos apenas coletores ativos, não sendo possível associação de coletores desativados.

**Associação de Equipamentos a Usuários**

* Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Básico \ Mobilidade \ Usuários de Coletores Móveis\ Anexos \ Equipamentos Associados ao Usuário;

* No cadastro de usuário de coletores móveis pode ser realizado a associação de equipamentos que serão utilizados pelo usuário, este como Operador de Equipamentos, no coletor;
* Os equipamentos que estarão disponíveis para a associação ao usuário são os que foram associados aos projetos (Projetos \ Construção e Projetos \ Controle \ Básico \ Mobilidade \ Equipamentos \ Equipamentos Associados ao Projeto) que estão relacionados ao coletor no qual o usuário utilizará;
* Somente será possível associar equipamentos, se existirem coletores associados ao usuário;
* Ao realizar o sincronismo no coletor, essas informações serão enviadas. Ao solicitar a inclusão de entrada de apontamento de equipamento, a tela de equipamentos associados será exibida para que o equipamento seja selecionado. Detalhes sobre essa função estão exemplificadas no módulo de equipamentos neste documento;
* **Validações:**
  + Inclusão e Alteração:
    - Valida se existe coletor associado ao usuário, pois os equipamentos são originários dos projetos associados ao coletor;
    - Valida se o usuário do coletor é Operador de Equipamentos.
* **Processo de Associar Equipamentos ao Usuário**
* Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Mobilidade \ Usuários de Coletores Móveis\ Processos \ Associar Equipamentos ao Usuário;

* Através deste processo, é possível realizar a associação de vários equipamentos de uma só vez;
* São exibidos apenas os equipamentos que não estão associados ao usuário;
* As validações são as mesmas da inclusão unitária.

**Sincronismo**

**Entenda o Sincronismo (Envio e recebimento do coletor)**

* Para que o sincronismo possa ser realizado, é necessário que o WebService que receberá e enviará informações esteja ativo;
* É necessário dispor de um coletor móvel ou utilizar um emulador;
* Com a aplicação Minha Obra no coletor aberta, realizar o sincronismo com o usuário e senha de acesso a base de dados do TOP, ou seja, usuário definido para utilização do coletor;

As configurações de sincronismo podem ser realizadas manualmente ou através da leitura do QR Code que guarda as configurações:

Para utilizar o QR Code para configuração automatica informe a url sincronismo (host). Para ISS somente de forma manual.

**Geração do QR Code:**

Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Minha Obra\ Usuários de Coletores Móveis\ Processos \QR Code para Configuração Automática do Sincronismo do App Minha Obra:

**Configuração Manual:**

Basta digitar a URL:

Url sincronismo ISS - API (Opcional quando desejo usar o ISS)

Url sincronismo HOST- API (Indicado)

Após a definição das informações de sincronismo, o mesmo é executado e as informações sincronizadas com o TOTVS Construção Obras e Projetos.

Caso ocorra algum erro no processo de sincronismo, será possível visualizar em qual etapa ocorreu e expandir o mesmo para mais detalhes.

     

É possível realizar a configuração do sincronismo para que seja realizado de forma automática. O Minha Obra possibilita que seja definido o intervalo de tempo em minutos do sincronismo e o tipo de rede que será executado: Wifi, Wifi e Celular (3g).

      

**Mapa de apontamentos**

* Durante o registro do apontamento no coletor, informações de localização (coordenadas GPS) serão coletadas e enviadas no sincronismo para o banco de dados do sistema.
* Com isso, será possível visualizar as posições dos apontamentos no sistema.
* Para habilitar a visualização de mapas é necessário configurar a chave de acesso ao Google Maps:

+ Menu: Ambiente -> Parâmetros -> Parâmetros Gerais -> Aba Google -> Chave de identificação para Google Maps
+ Como configurar a chave de acesso: [http://tdn.totvs.com/pages/viewpage.action?pageId=42043762](https://tdn.totvs.com/pages/viewpage.action?pageId=42043762)

* + Observação: É necessário configurar apenas a chave de acesso, não existe a necessidade de configurar o portal com IIS (Internet Information Services).  
      
      
    - Observação:
    * O aplicativo Minha Obra deverá coletar as coordenadas GPS em intervalos de 1 minuto.
    * A precisão das coordenadas GPS será de 50 metros e deverá funcionar em ambientes abertos.
