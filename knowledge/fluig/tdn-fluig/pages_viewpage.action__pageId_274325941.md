---
content_hash: 375740220353230f9042917eb4c932e4ad92204a9e9931e0923337d4155448e3
fetched_at: '2026-06-28T21:35:25.110032+00:00'
page_id: '274325941'
product: fluig
source: tdn-fluig
title: Instalação Windows - Modo Caractere
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274325941
version: 28
---

4.\*ndice

# Objetivo

---

Informar como é realizada a instalação de módulos específicos da plataforma no Windows como o do Fluig, Servidor de indexação (Solr) e RealTime (nodejs), em modo caractere.

# Pré-requisitos

---

Antes de iniciar uma instalação, certifique-se de que os procedimentos e requisitos abaixo foram preenchidos:

* Leia atentamente o .

* Verifique se as configurações e especificações do servidor estão de acordo com os requisitos estipulados no [Dimensionamento](http://tdn.totvs.com/display/fluig/Dimensionamento) e na [Matriz de Portabilidade](http://tdn.totvs.com/display/fluig/Matriz+de+Portabilidade).

* Confirme se a base de dados foi criada em um banco de dados homologado, conforme as orientações descritas em [Configuração de banco de dados MySQL](http://tdn.totvs.com/pages/viewpage.action?pageId=257623464), [SQL Server](http://tdn.totvs.com/pages/viewpage.action?pageId=257623499) ou [Oracle](http://tdn.totvs.com/pages/viewpage.action?pageId=257623480).

* É obrigatório que a instalação do(s) módulo(s) seja realizada utilizando o usuário **administrador** ou um usuário que tenha permissões de instalação e alteração de serviços.

# Pacote de instalação

---

**01.** Para fazer *download* do pacote de instalação, acesse a [Central do cliente](http://suporte.totvs.com), conforme descrito na documentação .

**02.** Descompacte o instalador da plataforma no diretório desejado.

**03. Pronto!** Agora você já pode executar os comandos para instalação da plataforma.

# Passo a passo para a instalação da plataforma

---

Movimente-se nas abas abaixo e acompanhe o passo a passo de instalação:

Atenção!

Por questões de segurança, orientamos não expor sua plataforma diretamente à internet. Para isso, será necessário [criar uma rede DMZ](http://tdn.totvs.com/x/MZIbCQ) juntamente com o [protocolo HTTPS](http://tdn.totvs.com/x/vdMgFQ).

0.5falsesamples1fade1Passo 1Nota:

Se você já possui um arquivo de configuração (install.conf) previamente configurado, pode seguir diretamente para o passo 2.

Se a instalação for realizada de forma completa, ou seja, com todos os módulos no mesmo servidor de aplicação, não será necessário executar os procedimentos  e .

* Abra o **Prompt de comandos** no diretório onde o pacote de instalação foi descompactado e execute o comando:

bash

* A execução do comando irá gerar o arquivo de configurações **install.conf** conforme imagem abaixo:

**Figura 1 - Arquivo install.conf gerado**

* Edite o arquivo **install.conf** alterando as variáveis para atender as configurações desejadas para a instalação do produto.

Importante!

Quando informar o diretório onde a plataforma será instalada, no parâmetro INSTALL\_PATH, deve-se usar duas contrabarras (\\) como separador de pastas.

Se o **Servidor de indexação** não for instalado neste momento juntamente com o Fluig, o parâmetro **install.solr** deve ser igual a **false**. Ao optar por instalar, além de alterar o valor do parâmetro **install.solr** para **true,** deve-se informar também o **diretório** de instalação do **JDK** como valor no parâmetro ****solr.jdk****, na condição de estar instalado. Caso o valor do parâmetro permanecer em branco, o **JDK** será instalado automaticamente.

Se o **nodejs** não for instalado neste momento juntamente com o Fuig, o parâmetro **install.node** deve ser igual **false**.

2Passo 2

* Se o arquivo de configuração (install.conf) já existe e está em um diretório diferente, passe como parâmetro o caminho absoluto do arquivo de configuração:

bash\install.conf]]>

* **Pronto!** Ao finalizar a instalação no Console, os **serviços do Fluig** estarão pronto para serem iniciados.

solr

# Passo a passo para instalar somente o Servidor de indexação

---

Siga os passos abaixo para a instalação:

0.5falsesamples2fade1Passo 1Nota:

Se você já possui um arquivo de configuração (install.conf) previamente configurado, pode seguir diretamente para o passo 2.

* Abra o **Prompt de comandos** no diretório onde o pacote de instalação foi descompactado e execute o comando:

bash

* A execução do comando irá gerar o arquivo de configurações **install.conf**.

* Edite o arquivo **install.conf** alterando as variáveis para atender as configurações desejadas para a instalação do produto.

Importante!

Quando informar o diretório onde o **Solr** será instalado, no parâmetro INSTALL\_PATH, deve-se usar duas contrabarras (\\) como separador de pastas.

Para que o **Servidor de indexação** seja instalado neste momento, o parâmetro **install.solr** deve ter o valor **true**. Também é necessário alterar o valor do parâmetro **solr.remote** se a instalação será feita para/em ambiente remoto e **solr.cloud** se a instalação será feita para/em ambiente *cloud*.

Se já houver uma instalação do **JDK**, o seu caminho/diretório deve ser informado como valor no parâmetro **solr.jdk**. Se o valor do parâmetro permanecer em branco o JDK será instalado automaticamente.

2Passo 2

* Se o arquivo de configuração (install.conf) já existe e está em um diretório diferente, passe como parâmetro o **caminho absoluto** do arquivo de configuração executando o comando abaixo:

bash\install.conf]]>

* **Pronto!** Ao finalizar a instalação no Prompt de Comandos, o serviço do **Servidor de indexação** estará pronto para ser iniciado.

Dica!

Se desejar configurar **alta disponibilidade (*Cluster*)**, continue a instalação conforme os procedimentos descritos na documentação .

node

# Passo a passo para instalar somente o RealTime

---

Para realizar a instalação, siga os passos abaixo:

0.5falsesamples3fade1Passo 1Nota:

Se você já possui um arquivo de configuração (install.conf) previamente configurado, pode seguir diretamente para o passo 2.

* Abra o **Prompt de comandos** no diretório onde o pacote de instalação foi descompactado e execute o comando:

bash

* A execução do comando irá gerar o arquivo de configurações **install.conf**.

* Edite o arquivo **install.conf** alterando as variáveis para atender as configurações desejadas para a instalação do produto.

Importante!

Quando informar o diretório onde o **nodejs** será instalado, no parâmetro INSTALL\_PATH, deve-se usar duas contrabarras (\\) como separador de pastas.

Para o **nodejs** ser instalado neste momento, o parâmetro **install.node** deve ter o valor **true**.

2Passo 2

* Se o arquivo de configuração (install.conf) já existe e está em um diretório diferente, passe como parâmetro o caminho absoluto do arquivo de configuração executando o comando abaixo:

bash\install.conf]]>

* **Pronto!** Ao finalizar a instalação no Prompt de Comandos, o serviço do **RealTime** estará pronto para ser iniciado.

# Atualização dos módulos

---

As instruções para realizar o atualização dos serviços do Fluig estão informados abaixo:

0.5falsesamples4fadetrue1Fluig

* Abra o **Prompt de comandos** no diretório onde o pacote de instalação foi descompactado e execute o comando abaixo. Se o Fluig foi instalado de forma completa ou seja, com todos os módulos, não será necessário atualizar os módulos Servidor de indexação e RealTime separadamente, sendo preciso apenas executar este comando:

bash]]>2Servidor de Indexação

* Abra o **Prompt de comandos** no diretório onde o pacote de instalação foi descompactado e execute o comando:

bash]]>

3RealTime

* Abra o **Prompt de comandos** no diretório onde o pacote de instalação foi descompactado e execute o comando:

bash]]>

# Exceção Firewall

---

Caso o servidor onde a plataforma foi instalada possua *firewall* ativo é necessário adicionar exceções para as seguintes portas utilizadas pela plataforma:

* Porta do Servidor de Aplicação;
* Porta do Servidor para RealTime;
* Porta do Servidor de Chat.

# Primeiro acesso

---

Para informações sobre os próximos passos, que envolvem o primeiro acesso à plataforma, acesse a documentação .
