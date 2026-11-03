---
content_hash: e06aa1a37bb12d9e760eba89427b8264e9e43760c98de85ccf273c261db0f271
fetched_at: '2026-06-29T00:11:54.031047+00:00'
page_id: '852917479'
product: rm
source: tdn-rm
title: 2.6.1 - Soap
type: documentation
url: https://tdn.totvs.com/display/LRM/2.6.1+-+Soap
version: 123
---

## O que é?

A atividade de SOAP no TOTVS Automação de Testes é uma ferramenta que permite testar e automatizar chamadas a WebServices SOAP, facilitando a integração e validação de processos.

WebServices são usados para disponibilizar serviços interativos na WEB, podendo ser acessados por outras aplicações. O SOAP (Simple Object Access Protocol) está se tornando padrão para a troca de mensagens entre aplicações e Web Services, já que é uma tecnologia construída com base em XML e HTTP. Como o RM possui seus web services podemos utilizar o TOTVS Automação de Testes para testá-los.

## Para que serve?

Serve para automatizar o teste e a execução de WebServices SOAP, incluindo registros, processos e outros serviços oferecidos pelo sistema RM.

## Links Úteis

1. Documentação e Download **Soap Ui**: <https://www.soapui.org/docs/>
2. O que são **WebServices**: <https://pt.wikipedia.org/wiki/Web_service>

## Exemplo de Uso

Como cadastrarComo cadastrar1. Navegação para o cadastro.

1. Navegue no menu do TOTVS Automação de Testes e clique em: **Atividades →** **Serviços** → **Soap**.
2. Na tabela que será mostrada, clique no botão verde em destaque para criar **Atividade de Soap.**

2. Link para Definir cabeçalho (Nome e nível de acesso)

[Clique aqui para obter as informações do cabeçalho](https://tdn.totvs.com/pages/viewpage.action?pageId=859591806)

3. Preenchimento dos CamposVersão

Especifica a versão da atividade em questão. O objetivo de versionar uma atividade é para quando necessitamos ter mais de uma atividade em versões diferentes. Isso irá nos auxiliar a ter um histórico de atualizações e assegurar que as mudanças feitas sejam rastreáveis e reversíveis, se necessário.

Se for necessário utilizar mais de uma versão do RM no seu ambiente, é recomendado que a versão da atividade seja compatível com o sistema RM em uso. Caso contrário, pode-se optar por uma versão padrão de sua preferência.

*Exemplo utilizando a versão do RM*

*Exemplo utilizando a versão padrão*

Descrição de Atividade 

Fornece uma descrição detalhada da atividade, explicando seu propósito e operações, facilitando a compreensão e manutenção futura.

Condição de Erro 

Se ocorrer um erro durante a execução de alguma das requisições, o TOTVS Automação de Testes deve tomar medidas específicas para lidar com esse erro. As ações variam conforme o tipo e a gravidade do erro.

**Logar o Erro**: Caso ocorra um erro em alguma das requisições SOAP, o TOTVS Automação de Testes deverá registrar todas as informações relevantes sobre o erro no log de execuções.

* + - **Exemplo:** Se uma requisição SOAP falhar com um erro 500, o TOTVS Automação de Testes deverá registrar essas informações nos logs para análise posterior. A execução do processo não será finalizada

**Gerar Erro de Execução:** Caso ocorra um erro em alguma das requisições SOAP, o TOTVS Automação de Testes deverá lançar uma exceção que interrompa a execução do processo atual.

* + - **Exemplo:** Se uma requisição SOAP falhar com um erro 500, o TOTVS Automação de Testes deverá registrar essas informações nos logs para análise posterior e a execução do processo será finalizada.

**Gerar Alerta e Continuar:** Caso ocorra um erro alguma das requisições SOAP, o TOTVS Automação de Testes deverá registrar um alerta e continuar a execução das operações subsequentes. Isso permite que outros processos continuem sendo executados.

* + - **Exemplo:** Se uma requisição SOAP falhar com um erro 500, o TOTVS Automação de Testes deverá registrar um alerta sobre a execução da atividade e continuar processando outras operações relacionadas sem interrupção.

Operações

Neste cadastro, é possível realizar as seguintes operações:

Recuperar Operações

Permite que o TOTVS Automação de Testes recupere e liste todas as operações disponíveis no serviço web configurado. Esta funcionalidade é essencial para identificar e selecionar as operações específicas que podem ser executadas pelo serviço web.

**Atenção:** O Agent e o Host do RM devem estar devidamente sendo executados no servidor em questão.

**Saiba mais:** [Agent](https://tdn.totvs.com/display/LRM/10+-+TestFlow+Agent) e [Servidor](https://tdn.totvs.com/display/LRM/5.+Servidores).

**Funcionamento:**

* **Inicialização:** Deve-se informar o servidor e a URI correspondente. O TOTVS Automação de Testes enviará uma requisição ao serviço web para listar todas as operações disponíveis.
* **Listagem:** As operações recuperadas são exibidas em uma interface onde os usuários podem visualizar e selecionar as operações desejadas.

Alteração em Massa

Permite a atualização ou modificação de múltiplos campos de múltiplas requisições em uma única operação. Este recurso é utilizado para aplicar mudanças consistentes em vários elementos ao mesmo tempo, economizando tempo e reduzindo o risco de erros manuais.

**Funcionamento:**

* **Configuração:** O usuário define os parâmetros e os registros que serão alterados em massa. É possível realizar a alteração dos seguintes campos:
  + Uri da Coleção;
  + Soap Endpoint;
  + Timeout XML;
  + Usuário;
  + Senha;
  + Domínio;

Executar Todas

Permite executar todas as requisições definidas em uma sequência ou lote. Esta funcionalidade é útil para automatizar a execução de múltiplas operações de forma ordenada e eficiente. Para isso, escolha o servidor em que deve ser executado às requisições.

**Atenção:** O Agent e o Host do RM devem estar devidamente sendo executados no servidor em questão.

**Saiba mais:** [Agent](https://tdn.totvs.com/display/LRM/10+-+TestFlow+Agent) e [Servidor](https://tdn.totvs.com/display/LRM/5.+Servidores).

**Funcionamento:**

* **Definição:** O usuário configura uma série de requisições que devem ser executadas em sequência.
* **Execução:** O TOTVS Automação de Testes processa cada requisição na ordem definida, garantindo que todas as operações sejam executadas conforme especificado.
* **Log:** Será logado o resultado de cada requisição executada, assim como o seu status code.
  + Verde: A requisição foi executada com sucesso.
  + Vermelho: Houve um erro para processar a requisição.

Requisições Info

**URI (WSDL):** É o endereço onde está localizado o arquivo WSDL que descreve o WebService. Este arquivo define os métodos disponíveis, os tipos de dados, e as operações que podem ser executadas pelo WebService**.**

**SOAP Endpoint:** O SOAP Endpoint é o endereço onde o serviço SOAP está disponível para receber as requisições. Este é o URL que os clientes utilizam para enviar as mensagens SOAP ao servidor

**Timeout (Segundos**) O Timeout define o tempo máximo (em segundos) que o TOTVS Automação de Testes deve esperar por uma resposta do WebService antes de considerar a requisição como falhada. Este campo é importante para garantir que a aplicação não fique indefinidamente esperando por uma resposta.

**Descrição**: Campo que permite adicionar uma descrição detalhada sobre a requisição SOAP. Pode incluir informações sobre o propósito da requisição, detalhes dos parâmetros e qualquer outra informação relevante

**Status de Retorno HTTP Esperados:** Lista dos códigos de status HTTP que são esperados como resposta válida do WebService em questão. Isso ajuda a identificar se a requisição foi bem-sucedida ou se encontrou algum tipo de erro.

Mensagem

A **Mensagem** é a estrutura principal de uma requisição SOAP, onde são definidos os dados a serem enviados e recebidos pelo serviço web.

Nesta aba são compostos pelos seguintes campos:

**SOAP Action:** É um cabeçalho HTTP específico usado em requisições SOAP para indicar a operação ou método específico que deve ser executado pelo serviço web. Ele é essencial para o roteamento correto e processamento da solicitação pelo servidor. Sendo assim ele informa ao servidor SOAP qual operação deve ser executada, sendo útil em serviços web que expõem múltiplas operações.

Exemplo de Soap Action:

**Envelope:** O envelope SOAP é o elemento raiz que define o início e o fim da mensagem SOAP.

Exemplo de Envelope:

Autenticação

A seção **Autenticação** é crucial para garantir a segurança das requisições SOAP. Nesta seção, são especificadas as credenciais necessárias (Login, senha e domínio) para acessar o serviço web.

Exemplo:

Ações

É o processo de enviar uma mensagem SOAP a um serviço web para solicitar a execução de uma operação específica. Este processo envolve a criação e configuração de uma mensagem SOAP, incluindo a definição do envelope SOAP e a especificação do cabeçalho SOAP Action.

a. Sendo assim clique no botão em destaque para **Executar a Requisição** e coloque o servidor de uso.

**Atenção:** O Agent e o Host do RM devem estar devidamente sendo executados no servidor em questão.

**Saiba mais:** [Agent](https://tdn.totvs.com/display/LRM/10+-+TestFlow+Agent) e [Servidor](https://tdn.totvs.com/display/LRM/5.+Servidores).

b. E para remover a requisição clique no botão em destaque **Deletar requisição.**

Variáveis de ambiente

As Variáveis de Ambiente são utilizadas para configurar e personalizar o comportamento da Atividade. Elas permitem definir valores específicos ou dinâmicos que podem ser usados durante a execução dos testes, assegurando que o teste execute conforme o ambiente em que o mesmo é executado. As Variáveis de Ambiente são cadastradas no cadastro de Ambiente onde informamos os valores fixos ou de forma dinãmica no cadastro de Script SQL.

Consulte quais campos permitem o uso das Variáveis de Ambiente nessa Atividade:

[Soap - Variáveis de ambiente](https://tdn.totvs.com/pages/viewpage.action?pageId=842285169)

Saiba mais sobre [Ambientes](https://tdn.totvs.com/display/LRM/4+-+Ambientes).

Exemplo prático1. Criação de chamadas SOAP para cadastros no RM.

## Cadastro: Unidade de medida.

Coleta de informações 

1. Após estar devidamente configurados conforme os requisitos deste tipo de Atividade carregue o Host do RM como Administrador.
2. Acesse a URL do webservice do Host (<http://localhost:8051/wspageindex/>).
   1. Se a página abaixo for exibida suas configurações estão corretas.
3. Vamos usar como exemplo o processo de inclusão de uma Unidade de Medida. O primeiro passo é analisar o cadastro que queremos fazer pelo WebService para coletar algumas informações relevantes:

1. 1. Quais dados serão inseridos.
   2. Qual é o DataServer do cadastro.
      1. Para descobrir qual é o DataServer do cadastro, vá até a aba de edição ou cadastro de um registro, clique em qualquer campo da tabela fornecida e pressione a combinação de teclas: **`CTRL + ALT + F9`****.**
Utilização do SoapUI

## Resgate do XML:

1. De posse do DataServer e das informações do cadastro, vamos identificar o método do WebService que utilizaremos para incluir um registro. Para isso, precisamos de um XML.
2. Baixe em seu computador um aplicativo que se chama SoapUI ([Baixe aqui](https://www.soapui.org/downloads/thank-you-for-downloading-soapui/)). Nela podemos inserir a URL do WebService do host para saber qual método utilizar para incluir nosso registro

Após instalar, abra o aplicativo e no menu File escolha New Soap Project.

4. Escolha um nome como, por exemplo **Cadastros do RM,** e na Inicial WSDL cole a seguinte URL: <http://localhost:8051/wsDataServer/MEX?wsdl>.

Lembre-se que neste momento o host deve estar em execução na máquina (localhost).

5. Após confirmar se tudo correr bem serão apresentados na tela os métodos existentes no WebService dos DataServers do RM .

6. Como não conhecemos o XML para inclusão de registros, vamos buscar um que já existe na tabela para que sejam retornados seus dados e seu XML. Desta forma podemos somente substituir os dados do registro que carregamos pelos dados que queremos incluir. Para carregar registros pelo WebService utilizamos o método **ReadRecord.**

1. 1. Clicando com o botão direito sobre o método escolhemos a opção New Request, dê um nome para ela e clique no botão OK.
   2. No XML apresentado, preencha a tag `DataServerName` com o nome obtido no item 3.b, exatamente como exibido na tela, em **camel case**.
   3. Para buscar a Primary Key do registro, entre no seguinte link: <https://apitotvslegado.z15.web.core.windows.net/> e procure pelo Data Server resgatado anteriormente. Se o DataServer não estiver disponível, verifique a PK pelo banco de dados ou utilize o método GetSchema neste DataServer e conseguirá verificar nas informações retornadas a PK da tabela.
   4. Logo em seguida, clique em **EstUndData.**Pode-se verificar que logo no cabeçalho da página contém as informações da Primary Key desse cadastro, no caso será **CODUND.**
   5. Na tag `PrimaryKey`, insira apenas o Código da Unidade para o cadastro de Unidades de Medida. Vamos utilizar "M" (Metros).
   6. Para a Tag Contexto, podemos resgatar essa informação na aba Sistema do RM, localizada no canto inferior esquerdo da tela.  
        
        
        
      Defina o contexto com CODCOLIGADA=1

7. Preencha a autenticação com o usuário utilizado para acessar o RM. Para isso, siga os passos abaixo:

1. 1. Vá em Auth → Add New Authorization → Basic.
   2. Marque a opção Authenticate pre-emptively.
   3. Feche a tela de autenticação.
   4. Clique no botão Play.

1. 1. Será apresentado o XML com o registro desejado. Guarde esse XML que iremos precisar dele para a inclusão do registro.

      ## Inclusão do Novo Registro:
   2. Para a inclusão no SoapUi escolha o método SaveRecord, clique com o botão esquerdo e escolha New Request. Dê um nome para a requisição e clique em OK.
   3. Na tela apresentada, preencha a tag **`DataServerName`** com o mesmo dataserver utilizado no Read Record.
   4. Na tag `XML`, informe o conteúdo retornado do Read Record, copiando da expressão `<![CDATA[` até `]]>`.
   5. Em seguida, altere os dados antigos para os novos. Insira os dados do registro que você quer criar, substituindo os dados do registro que foi lido no Read Record.
   6. Para a Tag Contexto, sera da mesma forma utilizada no Read Record.  
      Defina o contexto com CODCOLIGADA=1.

8. Preencha a autenticação e teste a requisição se desejar. Assim, a solicitação pode ser transferida para a Atividade de Soap no TOTVS Automação de Testes. Se a inclusão for bem-sucedida, o ID do registro será retornado.

Configuração no TOTVS Automação de Testes

1. Informe o servidor no qual o Agent do TOTVS Automação de Testes está sendo executado. ([Clique aqui](https://tdn.totvs.com/display/LRM/10+-+TestFlow+Agent)para mais informações sobre o Agent). Informe a URL do WebService: <http://localhost:8051/wsDataServer/MEX?wsdl>.
2. Clique em RECUPERAR para que os métodos do WebService sejam apresentados.
3. Clique em **`RM_IwsDataServer`** para expandir os métodos.
4. Selecione o método **`SaveRecord`** e clique no sinal de "".

1. No lado direito da tela, expanda a requisição criada.
2. Dos campos já preenchidos, o único que precisa ser editado é o `Soap Endpoint`.
3. Altere a URL, substituindo o nome da máquina que aparece por `LOCALHOST`. Dessa forma, sua requisição será executada em qualquer máquina, e não apenas na especificada.
4. Informe a descrição da sua requisição, o que é útil caso sejam criadas várias requisições na mesma atividade.
5. Escolha o código de retorno adequado. Para operações de inserção, geralmente o código retornado é 201 (Created), mas isso pode variar dependendo de quem codificou a chamada. No SoapUI, você pode verificar o código correto ao executar a chamada. No caso da unidade de medida, o retorno de sucesso é 200 (OK).  
   1. Na aba **MENSAGEM** cole o envelope de requisição que foi criado no SoapUI. Copie todo o XML e cole na área de edição.
   2. Na aba **AUTENTICAÇÃO**, insira o usuário e a senha utilizados para executar a chamada. Utilize as mesmas credenciais que você usa para acessar o RM. O campo de domínio não é obrigatório.
   3. Na aba **AÇÕES**, você pode testar sua requisição ou deletar se for necessário.
   4. Salve sua Atividade e ela está pronta para para ser executada ou inserida em um Projeto, Agendamento ou Coleção.
2. Criação de chamadas SOAP para processos do RM.

## Processo: Ajuste a Valor Presente

Coleta de Informações

1. 1. Acesse o RM e execute o processo desejado manualmente. Vamos escolher um processo simples para sermos mais didáticos:  Ajuste a Valor Presente
      1. **Observação:** Se o processo que você escolheu automatizar for necessário alguma intervenção manual para preenchimento de dados fora do passo a passo (Wizard) não será possível automatizar pelo método **RM\_IwsProcess.**
   2. Acesse a guia Gestão Financeira e na aba Contas a Pagar/Receber, escolha a opção Ajuste a Valor Presente e informe o dados solicitados e clique no botão executar e aguarde o processo ser executado.
2. Após finalizar o processo com sucesso, acesse a aba **Ambiente** e, em seguida, o item **Gerenciamento de Jobs**. Crie um filtro para exibir apenas os jobs processados hoje, facilitando a localização do registro desejado..
3. Edit o registro desejado e na guia Processo anote o valor do campo Classe do Processo, que neste caso é **FinAVPData.**
4. No botão Anexos, abra o item de menu **XML de Parâmetros de Job**, copie o XML que vai ser apresentado e reserve.
Utilização do SoapUI

1. No SoapUI no menu Project crie um New SOAP Project
   1. Insira um nome: Processos RM
   2. Informa a Initial WSDL <http://localhost:8051/wsProcess/MEX?wsdl>
   3. No projeto criado navegue até **RM\_IwsProcess → ExecuteWithXmlParams**. Clique com o botão direito sobre e escolha New Request. Dê um nome a ela e clique em OK
   4. Será mostrado um envelope. Na tag**ProcessServerName** informe a classe de processo copiada no item 5.d **FinAVPData.**
   5. Na tag strXmlParams informe a seguinte string: <![CDATA[\*\*\*\*]]>
   6. Substitua os asteriscos da string acima pelo XML que salvou no item 5.d
   7. Preencha a autorização, navegando no menu. Para isso, vá em Auth →  Add New Authorization → Basic, insira suas credenciais e clique na opção "Authenticate pre-emptively". Por fim, execute a chama para testar.

h. Na janela a direita deve ser retornado o valor 1 se houve sucesso.

7. Após conseguir êxito na chamada você já tem tudo que necessita para criar sua atividade.

Configuração no TOTVS Automação de Testes

1. 1. Acesse o TOTVS Automação de Testes em **Atvidades → Serviços → Soap** e clique no sinal de   para incluir um novo registro.
   2. Preencha um nome que descreva sua Atividade e preencha o grupo e as permissões de acesso.
   3. Informe a versão desejada e uma descrição detalhada pela qual qualquer um que editar a Atividade consiga entender seu propósito. Informe também qual será o comportamento no caso de ocorrer erro de execução.

8. Clique no botão RECUPERAR OPERAÇÕES, informe o servidor no qual o Agent do TOTVS Automação de Testes está sendo executado. Informe a URL do WebService o Host do RM. <http://localhost:8051/wsProcess/MEX?wsdl>.

Clique em RECUPERAR OPERAÇÔES para que os métodos do WebService sejam apresentados.9. Clique em **RM\_IwsProcess** para expandir os métodos.

1. 1. Escolha o método **ExecuteWithXmlParams** e clique no sinal de  e uma requisição será criada do lado direito da tela. Após isso, expanda-a.

1. 1. Dos campos que já são apresentados preenchidos o único a ser editado é o Soap Endpoint.
   2. Altere a URL, substituindo o nome de máquina que aparecer por LOCALHOST. Desta forma sua requisição irá executar em qualquer máquina e não somente na que foi apresentada.
   3. Informe a descrição de sua requisição. Isto é útil caso sejam criadas mais de uma requisição na mesma Atividade.
   4. Escolha o código de retorno. Para operações de inserção geralmente o código retornado é 201 (Created), porém isto depende muito de quem codificou a chamada. Pelo SoapUi dá para saber. qual é ao executar a chamada. No caso do nosso exemplo é 200.
   5. Na aba **MENSAGEM** cole o envelope de requisição que foi criado no SoapUI. Copie todo o XML e cole na área de edição.
   6. Na aba **AUTENTICAÇÃO**, informe o usuário e senha para execução da chamada. É o mesmo usuário que você utiliza para acessar o RM. O campo domínio não é obrigatório.
   7. Na aba **AÇÕES**, você pode testar sua requisição ou deletar se for necessário.

---

# Saiba mais

As mensagens SOAP são baseadas em XML e possuem uma estrutura rígida que inclui um envelope, cabeçalhos opcionais e um corpo. Esta estrutura permite uma comunicação padronizada e extensível.

Pelo TOTVS Automação de Testes, é possível testar sua requisição SOAP antes de ser incluída em um projeto de teste.

É possível definir variáveis de ambiente para execução das atividades SOAP.

# FAQ

**P: O que é preciso para configurar meu ambiente para testar WebServices?**

R: O Agent deve estar em execução como administrador, o Host do RM deve estar em execução e seu arquivo de configuração deve conter às keys necessárias para o seu uso.

**P: Qual é o papel do SoapUI neste processo?**

R: O SoapUI é utilizado para criar e testar requisições SOAP, ajudando a identificar métodos e a estruturar o XML necessário para incluir registros no sistema RM.

**P: A minha atividade apresentou o seguinte erro: Erro na chamada do método ExecuteWithXmlParams. The remote server returned an error: (401) Unauthorized. O que fazer?**

**R:** Usuário utilizado para login inválido ou vencido. 

**P: A minha atividade apresentou o seguinte erro: There is an error in XML document (0, 0). O que fazer?**

**R:** A chamada webservice aponta para uma máquina específica. Para isso, edite o campo *Soap Endpoint* e aponte a chamada para LOCALHOST.
