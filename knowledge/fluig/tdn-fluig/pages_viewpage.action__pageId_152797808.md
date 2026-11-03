---
content_hash: 29fa08af5c8e6b52d6a3aeb5053319984b0d0edec9fa64681bfa2ef9faab69c4
fetched_at: '2026-06-28T21:35:18.165860+00:00'
page_id: '152797808'
product: fluig
source: tdn-fluig
title: Instalação Linux - Modo Caractere
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=152797808
version: 48
---

# Índice

4true.\*ndicenone

# Objetivo

---

Informar como é realizada a instalação de módulos específicos da plataforma no Linux como o do Fluig, Servidor de indexação (Solr) e RealTime (nodejs), em modo caractere.

Orientação de segurança

Por motivos de segurança recomendamos que após a instalação do TOTVS Fluig Plataforma em ambientes Linux, seja retirado o usuário como root seguindo o processo na documentação [Configurar ambiente Linux para não utilizar o usuário root](http://tdn.totvs.com/x/v2cWGw).

# Pré-requisitos

---

Antes de iniciar uma instalação, certifique-se de que os procedimentos e requisitos abaixo foram preenchidos:

* Leia atentamente o
* Verifique se as configurações e especificações do servidor estão de acordo com os requisitos estipulados no [Dimensionamento](http://tdn.totvs.com/display/fluig/Dimensionamento) e na [Matriz de Portabilidade](http://tdn.totvs.com/display/fluig/Matriz+de+Portabilidade).
* Confirme se a base de dados foi criada em um banco de dados homologado, conforme as orientações descritas em [Configuração de banco de dados MySQL](http://tdn.totvs.com/pages/viewpage.action?pageId=257623464), [SQL Server](http://tdn.totvs.com/pages/viewpage.action?pageId=257623499) ou [Oracle](http://tdn.totvs.com/pages/viewpage.action?pageId=257623480).
* Conheça as orientações listadas no documento [Configurações sugeridas em ambientes Linux.](http://tdn.totvs.com/pages/viewpage.action?pageId=242389225)
* É obrigatório que a instalação do(s) módulo(s) seja realizada utilizando o usuário **root** ou um usuário que tenha os privilégios de instalação de pacotes e alteração de serviços.
* Ter instalado o pacote unzip para descompactação de arquivos.
* Ao utilizar o Fluig em ambiente Linux, é necessário que a biblioteca **fontconfig** (ou **libfontconfig1**, dependendo da distribuição) esteja instalada.

# Distribuições homologadas

---

As distribuições Linux homologadas para a plataforma TOTVS Fluig podem ser consultadas na [Matriz de Portabilidade](http://tdn.totvs.com/display/fluig/Matriz+de+Portabilidade)

# Pacote de Instalação

---

1. Para fazer download do pacote de instalação acesse o [Portal do Cliente](http://suporte.fluig.com/), conforme descrito na documentação ;
2. Descompacte o instalador da plataforma no diretório desejado;
3. **Pronto!** Agora você já pode executar os comandos para instalação da plataforma.

# Passo a passo para a instalação da plataforma

---

Movimente-se nas abas abaixo e acompanhe o passo a passo de instalação.

Importante!

Por questões de segurança orientamos não expor sua plataforma diretamente à internet. Para isso, será necessário [criar uma rede DMZ](http://tdn.totvs.com/x/MZIbCQ) juntamente com o [protocolo HTTPS](http://tdn.totvs.com/x/vdMgFQ).

0.5falsesamples1fade1Passo 1Observação

Se você já possui um arquivo de configuração (install.conf) previamente configurado, pode seguir diretamente para o passo 2.

Se a instalação for realizada de forma completa, ou seja, com todos os módulos no mesmo servidor de aplicação, não será necessário executar os procedimentos  e .

* Abra o **Console** no diretório onde o pacote de instalação foi descompactado e execute o comando:

bash

* A execução do comando irá gerar o arquivo de configurações **install.conf.**

* Edite o arquivo **install.conf** alterando as variáveis para atender as configurações desejadas para a instalação do produto.

Atenção!

Quando informar o diretório onde a plataforma será instalada, no parâmetro INSTALL\_PATH, deve-se usar uma barra (/) como separador de pastas.

Se o **Servidor de indexação** não for instalado neste momento juntamente com o Fluig, o parâmetro **install.solr** deve ser igual a **false**. Ao optar por instalar, além de alterar o valor do parâmetro **install.solr** para **true,** deve-se informar também o **diretório** de instalação do **JDK** como valor no parâmetro ****solr.jdk****, na condição de estar instalado. Caso o valor do parâmetro permanecer em branco o **JDK** será instalado automaticamente.

Se o **nodejs** não for instalado neste momento juntamente com o fuig, o parâmetro **install.node** deve ser igual **false**.

2Passo 2

* Se o arquivo de configuração (install.conf) já existe e está em um diretório diferente, passe como parâmetro no <diretório> o **caminho absoluto** do arquivo de configuração (install.conf). Isso significa que, em <diretório> deve ser incluído o caminho onde o arquivo de configuração está salvo:

bash\install.conf]]>

* **Pronto!** Ao finalizar a instalação no Console, os **serviços do Fluig** estarão pronto para serem iniciados.

solr

# Passo a passo para instalar somente o Servidor de indexação

---

Siga os passos abaixo para a instalação:

0.5falsesamples2fade1Passo 1Observação

Se você já possui um arquivo de configuração (install.conf) previamente configurado, pode seguir diretamente para o passo 2.

* Abra o **Console** no diretório onde o pacote de instalação foi descompactado e execute o comando:

bash

* A execução do comando irá gerar o arquivo de configurações **install.conf**.

* Edite o arquivo **install.conf** alterando as variáveis para atender as configurações desejadas para a instalação do produto.

Atenção!

Quando informar o diretório onde o **solr** será instalado, no parâmetro INSTALL\_PATH, deve-se usar uma barra (/) como separador de pastas.

Para o **Servidor de indexação** ser instalado neste momento, o parâmetro **install.solr** deve ter o valor **true**. Também é necessário alterar o valor do parâmetro **solr.remote** se a instalação será feita para/em ambiente remoto e **solr.cloud** se a instalação será feita para/em ambiente cloud.

Se já houver uma instalação do **JDK**, o seu caminho/diretório deve ser informado como valor no parâmetro **solr.jdk**. Se o valor do parâmetro permanecer em branco o JDK será instalado automaticamente.

2Passo 2

* Se o arquivo de configuração (install.conf) já existe e está em um diretório diferente, passe como parâmetro no <diretório> o **caminho absoluto** do arquivo de configuração  (install.conf). Isso significa que, em <diretório> deve ser incluído o caminho onde o arquivo de configuração está salvo:

bash\install.conf]]>

* **Pronto!** Ao finalizar a instalação no Console, o serviço do **Servidor de indexação** estará pronto para ser iniciado.

Dica!

Se desejar configurar **alta disponibilidade (*Cluster*)**, continue a instalação conforme os procedimentos descritos na documentação .

node

# Passo a passo para instalar somente o RealTime

---

Para realizar a instalação, siga os passos abaixo:

0.5falsesamples3fade1Passo 1Observação

Se você já possui um arquivo de configuração (install.conf) previamente configurado, pode seguir diretamente para o passo 2.

* Abra o **Console** no diretório onde o pacote de instalação foi descompactado e execute o comando:

bash

* A execução do comando irá gerar o arquivo de configurações **install.conf**.

* Edite o arquivo **install.conf** alterando as variáveis para atender as configurações desejadas para a instalação do produto.

Atenção!

Quando informar o diretório onde o **nodejs** será instalado, no parâmetro INSTALL\_PATH, deve-se usar uma barra (/) como separador de pastas.

Para o **nodejs** ser instalado neste momento, o parâmetro **install.node** deve ter o valor **true**.

2Passo 2

* Se o arquivo de configuração (install.conf) já existe e está em um diretório diferente, passe como parâmetro no <diretório> o **caminho absoluto** do arquivo de configuração  (install.conf). Isso significa que, em <diretório> deve ser incluído o caminho onde o arquivo de configuração está salvo:

bash\install.conf]]>

* **Pronto!** Ao finalizar a instalação no Console, o serviço do **RealTime** estará pronto para ser iniciado.

# Atualização dos Módulos

---

As instruções para realizar o atualização dos serviços do Fluig estão informados abaixo:

0.5falsesamples4fadetrue1Fluig

* Abra o **Console** no diretório onde o pacote de instalação foi descompactado e execute o comando abaixo. Se o Fluig foi instalado de forma completa ou seja, com todos os módulos, não será necessário atualizar os módulos Servidor de indexação e RealTime separadamente, sendo preciso apenas executar este comando:

bash]]>2Servidor de Indexação

* + Abra o **Console** no diretório onde o pacote de instalação foi descompactado e execute o comando:

bash]]>

3RealTime

* + Abra o **Console** no diretório onde o pacote de instalação foi descompactado e execute o comando:

bash]]>

# Exceção Firewall

---

Caso o servidor onde a plataforma foi instalada possua *firewall* ativo é necessário adicionar exceções para as seguintes portas utilizadas pela plataforma:

* Porta do Servidor de Aplicação do Fluig;
* Porta do Servidor para RealTime;
* Porta do Servidor de Chat.

# Inicialização

---

Os procedimentos de inicialização estão disponíveis na página .

Dica!

Para informações sobre acesso e utilização da plataforma, acesse o , acompanhe os primeiros passos e se familiarize com o produto!
