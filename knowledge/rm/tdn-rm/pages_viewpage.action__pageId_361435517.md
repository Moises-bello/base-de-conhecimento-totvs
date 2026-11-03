---
content_hash: 64ed5255261af60cf11bc28c028292bf6355360e6967888679c622d46738f74f
fetched_at: '2026-06-29T00:08:58.747520+00:00'
page_id: '361435517'
product: rm
source: tdn-rm
title: Como verificar quais foram atualizações aplicados no ambiente do TAF?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=361435517
version: 3
---

O TAF disponibiliza um menu especifico para que o usuário acompanhe o resumo de todas as atualizações do ambiente. Para ter acesso ao resumo, acesse o menu de Diagnóstico conforme a imagem abaixo:

|  |
| --- |
|  |

### **Objetivo da Funcionalidade**

Determinar se o ambiente e o sistema estão devidamente configurados e atualizados para um correto funcionamento do TAF.

 

---

### **Informações da Release corrente no ambiente TAF**

Informa a versão da release do dicionário de dados do TAF e a versão do repositório de fontes do TAF

**Dicionário**

O Dicionário de Dados contém as estruturas das tabelas, campos e demais objetos que serão criados no banco de dados.

Para realizar a atualização do dicionário, é necessário ter o arquivo Diferencial (sdfbra.txt) contido no pacote de atualização e executar a ferramenta padrão de compatibilização da TOTVS, UPDDISTR.

Muito Importante!

Antes de atualizar o dicionário de dados com o Diferencial recém baixado, fazer um backup do sistema e banco de dados, já que o modelo de dados será alterado. 

Marca TAF

Importante ressaltar que a Marca TAF visualizada no diagnóstico não necessariamente será a mesma Marca do ambiente Protheus em que o TAF está sendo utilizado. A Marca TAF representa o cenário do dicionário de dados somente em relação ao TAF.

Por exemplo: Nos casos onde o ambiente Protheus possui dicionário de dados com a marca **12.1.007** e a Marca TAF apresentada no Diagnóstico é **12.1.014**, significa que ainda que o ambiente Protheus seja **12.1.007** o TAF contém todas as atualizações até a release **12.1.014**.

Esta Marca não impede o acesso ao sistema, porém é importante que a Marca TAF RPO ( repositório de objetos ) e a Marca TAF Dic. ( dicionário de dados ) estejam sempre na mesma release.

**RPO**

O repositório de dados é utilizado para armazenar todas as funcionalidades desenvolvidas para o TAF, sendo assim é atualizado sempre que ocorrem melhorias ou implementações no produto.

Para realizar a atualização do repositório de dados, localize o arquivo com extensão “. PTM” contido no pacote de atualização e aplique no ambiente do produto TAF, utilizando o TDS (Totvs Developer Studio).

Muito Importante!

Antes de atualizar o repositório de dados, fazer um backup do RPO atual.

Marca TAF

Importante ressaltar que a Marca TAF visualizada no diagnóstico não necessariamente será a mesma Marca do ambiente Protheus em que o TAF está sendo utilizado. A Marca TAF representa o cenário do dicionário de dados somente em relação ao TAF.

Por exemplo: Nos casos onde o ambiente Protheus possui dicionário de dados com a marca **12.1.007** e a Marca TAF apresentada no Diagnóstico é **12.1.014**, significa que ainda que o ambiente Protheus seja **12.1.007** o TAF contém todas as atualizações até a release **12.1.014**.

Esta Marca não impede o acesso ao sistema, porém é importante que a Marca TAF RPO ( repositório de objetos ) e a Marca TAF Dic. ( dicionário de dados ) estejam sempre na mesma release.

---

### **Informações da última atualização realizada no ambiente do TAF**

Informa os dados da última atualização do ambiente, sendo eles:

* Release do ambiente;
* Data do release;
* Informa que o ambiente possui todas as correções liberadas no TAF até a data informada;

Caso o ambiente esteja desatualizado são descritos os passos para atualização.

---

### **Informações do Web Service (Integração do ERP com o TAF)**

Caso o Web Service de integração do ERP com o TAF esteja configurado corretamente serão listados:

* Endereço do WS (Com link para consulta do serviço);
* Status do Serviço (Parado ou Em Execução);

Se o serviço não estiver configurado ou houver alguma divergência nas informações será apresentado uma mensagem informando os passos para correção.

---

### **Informações do TSS**

Apresenta as informações do TSS caso este serviço esteja configurado, sendo elas:

* URL TSS (URL e link para consulta do serviço);
* Status TSS (Conectado ou Não Conectado);
* Validade do Certificado (Caso o certificado não seja encontrado é necessário utilizar o Wizard de comunicação do TAF com o TSS para envio do certificado digital);
* Versão do TSS (Informa release e versão do TSS);

---

### **Link para o portal do cliente - Atualização do TAF**

Apresenta link direto para a página de atualização do TAF.

Atenção

É preciso estar logado no portal do cliente da TOTVS no navegador para que o link seja aberto corretamente.

---

### **Procedimentos para atualização do TAF**

Lista como deve ser feita a atualização do TAF no portal do cliente.

* Dicionário: Selecione a opção "Dicionário de Dados";
* Repositório: Selecione a opção "Atualizações Periódicas";
* Help: Selecione a opção "Help de Campos";
* Menu: Selecione a opção "Menus";

---

### **Resultado da análise do ambiente**

* **Versão do layout do e-Social na base do TAF**

Informa a versão do layout do e-Social. Este serviço de ser verificado manualmente

* **Tabelas Auto-Contidas**

Arquivo que contém as tabelas auxiliares previamente alimentadas.

As tabelas auto-contidas são preenchidas automaticamente pelo sistema, como por exemplo o cadastro de Países, Estados e Municípios.

Sua atualização se dá através da [Wizard de Configuração](http://tdn.totvs.com.br/pages/viewpage.action?pageId=185752114).

* **Totvs Application Server**

A build deve ser igual ou superior a 7.00.131227A.

Para atualizar este recurso, é necessário:

* + Acessar o portal da TOTVS( <http://interno.totvs.com/customercenter>  ) \ Portal do Cliente;
  + Efetuar login e acessar a opção Downloads e Atualizações( <https://suporte.totvs.com/download> );
  + Selecionar a opção "Protheus" e escolher a opção "Todos";
  + Na opção "Categorias", selecionar "Totvs Binário" e escolher conforme estrutura desejada;Muito Importante!

  Ao baixar a versão desejada de AppServer e SmartClient, fazer primeiramente um backup do binário atual, antes de sobrepor os arquivos com os recém baixados do portal.

* **Totvs DbAccess (TAF e WS)**

A build deve ser igual ou superior a 20141119 - compilação de 08/04/2015 ou última disponível no portal.

Para atualizar este recurso, é necessário:

* + Acessar o portal da TOTVS( <http://interno.totvs.com/customercenter>  ) \ Portal do Cliente;
  + Efetuar login e acessar a opção Downloads e Atualizações( <https://suporte.totvs.com/download> );
  + Selecionar a opção "Protheus" e escolher a opção "Todos";
  + Na opção "Categorias", selecionar "Totvs DbAccess" e escolher conforme estrutura desejada;Caso o TAF tenha sido utilizado com uma versão desatualizada do Totvs Dbaccess e o banco de dados utilizado seja **ORACLE** acesse o link abaixo para verificar os procedimentos que devem ser adotados para evitar problemas na utilização do produto:
* <http://tdn.totvs.com.br/pages/viewpage.action?pageId=233736548>
* Muito Importante!

  Ao baixar a versão desejada do DbAccess, fazer primeiramente um backup da aplicação atual, para em seguida efetuar a atualização com o instalador recém baixado do portal.

* **LIB**

Para o correto funcionamento do sistema é necessário efetuar a atualização do repositório de objetos com a última LIB disponibilizada na Central de Downloads.

Para atualizar este recurso, é necessário:

* + Acessar o portal da TOTVS( <http://interno.totvs.com/customercenter>  ) \ Portal do Cliente;

Efetuar login e acessar a opção Downloads e Atualizações( <https://suporte.totvs.com/download> );

* + Selecionar a opção "Protheus" e escolher a versão desejada;
  + Digitar "LIB" na caixa de pesquisa e efetuar a busca;
* Muito Importante!

  Ao baixar a versão desejada da LIB, fazer primeiramente um backup do RPO, para em seguida efetuar a aplicação do pacote recém baixado do portal.

* **TopMemoMega**

Para efetuar a gravação em um campo MEMO ( binário ) com conteúdo superior a 500kb, deve ser habilitado o parâmetro TOPMEMOMEGA no arquivo .ini do appserver.

Maiores detalhes na página [TOPMemoMega](http://tdn.totvs.com/display/tec/TOPMemoMega).

 

* **Auto Recno**

Trata-se de um novo recurso do DBAccess que o TAF vem a utilizar para ter maior performance no processamento das movimentações. Este recurso passa a usar o controle de auto-incremento do campo R\_E\_C\_N\_O\_ pelo próprio SGBD, não mais pelo DBAccess.

Para que este recurso esteja funcionando corretamente, é necessário antes do primeiro acesso ao TAF ou a execução de qualquer processamento, verificar se o DBAccess está atualizado conforme [pré-requisitos](http://tdn.totvs.com/pages/viewpage.action?pageId=196052689) estabelecidos; sem este recurso habilitado, o sistema apresentará erros de execução forçando a descartar a instancia de SGBD criada e para criação de uma nova para ser utilizada com o DBAccess correto.

Para atualizar o DBAccess, é necessário baixar uma versão mais atual na Central de Downloads, e proceder com a atualização.

Maiores detalhes na página [Auto Recno](http://tdn.totvs.com/display/framework/campos+RECNO+auto-incremental).

* **CLOB**

Tipo de campo nativo do banco de dados que está sendo usado para emular um campo memo.

Maiores detalhes na página [CLOB](http://tdn.totvs.com/pages/viewpage.action?pageId=183730211).

* **WebApp (SmartCliente Web)**

Se configurado no server mostra os dados do endereço e porta de comunicação.

---

**Rotinas disponíveis na opção "Outras Ações"**

### **Gerar Extrato (.ZIP)**

Exporta todos os dados apresentados em tela, bem como, todas as informações disponíveis na opção "Outras Ações".

Ao final da execução é gerado um arquivo compactado com os dados abaixo:

Histórico de Atualizações do RPO;

Console.log do ambiente TAF (Se configurado no diretório padrão de instalação);

Console.log do ambiente WS (Se configurado no diretório padrão de instalação);

Informações da tela do diagnóstico;

Informações de tamanho do campo \_FILIAL do dicionário x banco de dados (se existir diferenças nos campos);

Informações de compartilhamento entre tabela pai e filhas do TAF (se existir diferenças nos compartilhamentos);

Inspetor de Objetos com dados de todos os fonte do TAF;

---

### **Abrir Log do TAF**

Abre o arquivo console.log do ambiente do TAF.

Importante

O arquivo será aberto somente se for localizado no diretório padrão da instalação.

---

### **Abrir Log do WS**

Abre o arquivo console.log do ambiente do WS.

Importante

O arquivo será aberto somente se for localizado no diretório padrão da instalação.

---

### **Lista de Fontes**

São carregados todos os fontes do **TAF** do repositório de objetos (RPO). É possível exportar os dados para consulta.

---

### ****Valida Campo Filial****

Compara o tamanho de todos os campos de "\_FILIAL" do dicionário x banco de dados e retorna as informações caso encontre alguma diferença.

---

### ****Relacionamento de Tabelas****

Compara o relacionamento de todas as tabelas pai x filhas do TAF e verifica se ha diferença no compartilhamento de tabelas em todos os níveis (Empresa, Unidade de Negócio e Filial).

Ao encontrar alguma diferença nos compartilhamentos é apresentada uma tela com as divergências e um link informando como realizar a correção, a apresentação se dará na ordem, tabela Pai e na sequencia a(s) tabela(s) Filho(s).

---

### **Lista Tabelas dos Cadastros**

Lista todas as tabelas do TAF e seus respectivos relacionamentos e compartilhamentos, a apresentação se dará na ordem, tabela Pai e na sequencia a(s) tabela(s) Filho(s).

---

### **Histórico de Atualizações**

Carrega as informações de todos os patchs aplicados no ambiente. Ao exportar os dados é detalhado o nome e a data do fonte atualizado.
