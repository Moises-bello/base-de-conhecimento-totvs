---
content_hash: 9534d8e6c3a06cf7b02c9451fa90ece0a5589adf1a01d66b1f6243b874dde04c
fetched_at: '2026-06-28T21:35:23.881327+00:00'
page_id: '267788666'
product: fluig
source: tdn-fluig
title: Configuração de serviços de componentes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267788666
version: 24
---

true.\*ndicenone

  

# Objetivo

---

O objetivo desse guia é apresentar os procedimentos necessários para a configuração dos serviços de componentes, neste caso os softwares do pacote Microsoft® Office, assim como o Word®, PowerPoint® e Excel®, na utilização de forma integrada com o TOTVS Fluig Plataforma.

Este recurso é utilizado em algumas situações como:

Essa configuração deve ser feita no servidor da plataforma. O sistema operacional deve ser Microsoft Windows. Para verificar as versões homologadas, acesse a [Matriz de Portabilidade](http://tdn.totvs.com/x/_ApbB).

# Configuração dos serviços

---

Neste caso algumas configurações devem ser feitas no serviço do Fluig:

falseservicos1Passo 1

* Na tela de Serviços do Windows® é necessário acessar as propriedades do serviço FLUIG, conforme imagem abaixo:

2Passo 2

* É preciso configurar um usuário administrador para execução do serviço. Certifique-se que este usuário tenha **controle total** sobre os diretórios do volume.

3Passo 3

* Na tela de Serviços do Windows® também é necessário que o serviço *Spooler* de Impressão esteja iniciado nas máquinas onde será realizada a impressão:

# Configurar os componentes do pacote Microsoft® Office

---

Também será preciso executar o programa de Serviços de Componente do Windows®. Este programa é responsável pela gestão de componentes de integração COM dentro do Windows®.

falsecomponente1Passo 1

Acesse o Executar (Win + R) ou *prompt* do sistema operacional e digite: **dcomcnfg**.

Neste programa execute os seguintes passos para configurar arquivos Microsoft® Excel, Microsoft® Word e Microsoft® PowerPoint:

* Expanda a opção **Serviços de Componente**
* Expanda a opção **Computadores**
* Expanda a opção **Meu Computador**
* Clique no item **Config DCOM**.

2Passo 2

Na listagem de componentes exibida no painel central, procure pelos componentes:

1. Microsoft Excel Application;
2. Documento do Microsoft Word 97 - 2003;
3. Aplicativo do Microsoft PowerPoint.

Clique sobre o componente em questão com o botão direito do *mouse* e selecione **Propriedades**:

Importante!

Repetir as mesmas permissões de acesso para os três componentes (Word®, Excel® e PowerPoint®).

3Passo 3

Selecione a aba Identidade e escolha a opção **O usuário interativo.**

Em alguns casos esta opção não atende o problema, sendo recomendado portanto selecionar **Este usuário** e definir o mesmo usuário responsável por iniciar o serviço do Fluig.

4Passo 4

Na aba Segurança selecione a opção **Personalizar** para todos os tipos de segurança.

Clique também em **Editar** e adicione o grupo **Todos** em cada uma das permissões:

5Passo 5

Após adicionar o grupo **Todos**, atribuir a opção **Permitir** para todas as permissões possíveis, conforme imagens abaixo:

1. Permissão de Acesso:
   1. Acesso Local e Acesso remoto
2. Permissão de Início e Ativação
   1. Início Local e Início Remoto
   2. Ativação Local e Ativação Remota
3. Alterar Permissão de Configuração
   1. Controle total
   2. Ler

6Passo 6

Na aba Local desmarque todas as opções da tela.

7Passo 7

Após realizar os passos anteriores, efetuar um teste de impressão.

Caso a impressão não funcione corretamente com todas as opções desmarcadas, marque a opção **Executar o aplicativo neste computador** e faça um novo teste.Dica

Caso tenha interesse que o Serviço de Componentes sempre seja exibido no Console, é necessário salvar estas configurações utilizando a opção Salvar e informando um diretório para armazenar o arquivo **console.msc**. Ao executar o Console de Gerenciamento novamente, abra este arquivo.

# Configuração dos componentes 32 bits

---

Importante!

Em algumas máquinas com sistemas operacionais 64 bits, os componentes do Microsoft® Office não são criados no Serviços de Componente para 64 bits, e sim no de 32 bits. Siga os próximos passos para realizar esta configuração.

falsecomponente32bits1Passo 1

* Para visualizar os Serviços de Componente de 32 bits, execute o Console de Gerenciamento para 32 bits:

2Passo 2

* Adicionar o Serviços de Componente ao Console de Gerenciamento, conforme imagens abaixo:

3Passo 3  

1. Selecione na lista de Snap-ins disponíveis, o Serviços de Componente;
2. Adicione o Snap-in selecionado;
3. Clique em OK;
4. Volte para o tópico anterior e efetue os passos para configuração do pacote Microsoft® Office.

# Forçando a configuração do usuário através da GPO (Group Policy).

---

Em caso de instalação do pacote Microsoft® Office através de GPO (*Grupo Policy*) no servidor de aplicação, deve-se observar a necessidade de inclusão do usuário neste procedimento.

Para isto, é preciso seguir os passos abaixo para que o usuário não seja mais removido na instalação.

forceusariodcom1Passo 1

* Após configurar o usuário e senha na DCOM (Serviços de Componentes), conforme imagem abaixo:

2Passo 2

* O Windows® salva o usuário em uma regra nas Diretivas de Segurança Local, que podem ser acessadas conforme imagem abaixo:

3Passo 3

* O Windows® salva o usuário em uma regra nas Diretivas de Segurança Local, que podem ser acessadas conforme imagem abaixo:

4Passo 4

* Após aplicação forçada da GPOs, atualizando as permissões do servidor de aplicação, conforme imagem abaixo.

* Após este processo, pode-se perder o usuário nesta regra, conforme é exibido na imagem abaixo, automaticamente afetando a utilização dos pacotes do Microsoft® Office

Importante!

Para solução deste problema, basta incluir na GPO o usuário responsável por subir os componentes, que no caso foi informado, conforme a imagem do Passo 1 deste tutorial.

# Possíveis problemas

---

falsecomponente32bits1Situação 1

* É importante conferir qual usuário está iniciando o software do pacote Microsoft® Office, neste caso deve ser o mesmo que está configurado para iniciar o serviço do Fluig.

* Para isto, é utilizado o gerenciador de tarefas, na aba de "Processos", conforme imagem abaixo:

Importante!

O processo normalmente deve subir e descer de forma rápida, em torno de 4 segundos, conforme é feito a requisição pelo Fluig.

Em caso do processo ficar preso muito mais tempo que isso pode ocasionar outros problemas no Fluig, como calculo do CRC do documento, gerando o erro "Documento modificado externamente" ao visualizar o mesmo.

2Situação 2

* Observar se não há outros usuários logados no servidor de aplicação que podem estar causando conflitos no momento que o Fluig utilizar os componentes do Microsoft® Office, isto pode ser visto através do gerenciador de tarefas, na aba "Usuários" conforme imagem abaixo:

Importante!

No caso do servidor possuir outros usuários logados e principalmente com algum software do pacote Microsoft® Office aberto, deverá ser finalizado a respectiva sessão.
