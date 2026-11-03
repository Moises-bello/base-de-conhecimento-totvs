---
content_hash: 614a0204104437dc9522d570c82813e5287b2c141a496f62feb40d02df1bb085
fetched_at: '2026-06-28T21:35:22.607900+00:00'
page_id: '238029049'
product: fluig
source: tdn-fluig
title: Instalação e Atualização do Fluig ESB
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=238029049
version: 23
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**. 

# Índice

true.\*ndicenone

# Objetivo

---

Este guia tem como objetivo descrever de forma objetiva, passo a passo, todos os procedimentos necessários para a instalação do produto Fluig ESB, bem como configurar o produto nas plataformas suportadas.

# Pré-requisitos

---

Antes da instalação consulte as documentações de  dimensionamento e [configuração de banco de dados](http://tdn.totvs.com/pages/viewpage.action?pageId=120784259) para garantir que o ambiente onde o Fluig ESB será instalado está homologado.

# Instalando o Fluig ESB

---

0.5falsesamplesfade1Passo 1

Ao descompactar o arquivo que contém a instalação do Fluig ESB, terá a visão da imagem abaixo. Neste diretório encontram-se:

* Um diretório chamado **jre.** (Java Runtime Environment utilizado para executar a instalação).

* O arquivo de instalação, chamado ESB-Installer.exe.

Para iniciar a instalação basta executar o arquivo de extensão EXE (**ESB-Installer.exe**).

2Passo 2

Esta tela oferece a opção de escolher um idioma para o guia de instalação. As opções de idiomas são:

* Português
* Inglês

Para continuar, clique em OK.

3Passo 3

Nesta tela, você pode escolher um diretório para fazer a instalação do ESB. Sendo assim, após clicar no botão próximo, abrirá a caixa de diálogo abaixo:

Clique em OK para continuar a instalação.

4Passo 4

Nesta tela é exibido o progresso da instalação dos pacotes do Fluig ESB no diretório selecionado no passo anterior. Para continuar com a instalação, é necessário aguardar o processo de instalação terminar. Veja a próxima página.

5Passo 5

E então a tela de conclusão do processo de instalação dos pacotes do Fluig ESB é exibida. Para continuar com a instalação, clique em Próximo.

6Passo 6

Nesta tela é exibido o progresso da instalação do JRE (*Java Runtime Environment*) do Fluig ESB no diretório selecionado em etapa anterior. Para continuar com a instalação, é necessário aguardar o processo de instalação terminar. Veja a próxima página.

7Passo 7

E então a tela de conclusão do processo de instalação do JRE do Fluig ESB é exibida. Para continuar com a instalação, clique em Próximo.

8Passo 8

E então a tela de conclusão do processo de instalação do JRE do Fluig ESB é exibida. Para continuar com a instalação, clique em Próximo.

9Passo 9

Nesta tela é exibida a opção de instalação do Serviço do Fluig ESB como Serviço do Windows. Desta forma é possível que cada instalação do Fluig ESB tenha seus respectivos Serviços no Windows, para ambientes de produção e testes, por exemplo.

Para optar por instalar o serviço do ESB como Serviço do Windows, selecione as opções referentes apresentadas na tela. É possível renomear o serviço informando seu novo nome no campo **Nome** que será habilitado ao lado. Para continuar com a instalação, clique em Próximo.

10Passo 10

Nesta tela é exibido o processo de instalação do Serviço do Fluig ESB. Para continuar com a instalação, clique em Próximo.

11Passo 11

Neste ponto são exibidas mensagens de conclusão da instalação do ESB. Para finalizar a instalação clique em Pronto.

Dica

Para saber como inicializar o Fluig ESB após a instalação, acesse .

Importante

Detalhes de como configurar o licenciamento no Fluig ESB estão descritos abaixo no item [Instalando e configurando o TOTVS License Server](http://tdn.totvs.com/pages/viewpage.action?pageId=238029049#Instala%C3%A7%C3%A3oeAtualiza%C3%A7%C3%A3odofluigESB-InstalandoeconfigurandooTOTVSLicenseServer).

# Atualizando o Fluig ESB

---

Importante

1. O processo de atualização está homologado somente para instalações a partir da .

 2. É recomendado que seja realizado um *backup* do diretório atual de instalação do Fluig ESB antes de executar o processo de atualização, caso seja necessário retornar à versão anterior.

sample1Passo 1

Ao descompactar o arquivo que contém a instalação do Fluig ESB, terá a visão da imagem ao lado. Onde encontra-se no mesmo diretório:

* Um diretório chamado jre. (Java Runtime Environment utilizado para executar a instalação)

* O arquivo de instalação, chamado ESB-Installer.exe

Para iniciar a atualização basta executar o arquivo de extensão EXE (**ESB-Installer.exe.**).

2Passo 2

Executando o arquivo.exe de instalação/atualização

Esta tela oferece a opção de escolher um idioma para o guia de instalação. As opções de idiomas são:

* Português

* Inglês

Para continuar, clique em OK.

3Passo 3

Nesta tela, você deve informar o diretório de uma versão anterior do ESB para fazer a atualização de versão. Sendo assim, após clicar no botão próximo, abrirá a caixa de diálogo abaixo:

Clique em **SIM** para continuar a atualização.

4Passo 4

Nesta tela é exibido o progresso da atualização dos pacotes do Fluig ESB no diretório selecionado no passo anterior. Para continuar com a atualização, é necessário aguardar este processo terminar.

5Passo 5

A tela de conclusão do processo de atualização dos pacotes do Fluig ESB é exibida. Para continuar com a atualização, clique em Próximo.

6Passo 6

Nesta tela é exibido o progresso da atualização do JRE (*Java Runtime Environment*) do Fluig ESB no diretório informado em etapa anterior. Para continuar com a atualização, é necessário aguardar este processo terminar.

7Passo 7

A tela de conclusão do processo de atualização do JRE do Fluig ESB é exibida. Para continuar com a atualização, clique em Próximo.

8Passo 8

Neste ponto são exibidas mensagens de conclusão da atualização do ESB. Para finalizar a atualização clique em Pronto.

Dica

Para saber como inicializar o Fluig ESB após a instalação, acesse .

# Instalando e configurando o TOTVS License Server

---

O Fluig ESB utiliza o TOTVS License Server para fazer o controle de licenças do produto. Tanto a solicitação de envio do *Hardlock* quanto a solicitação de geração de licença do License Server, devem ser feitas para a equipe de CST por meio do telefone ou via Portal de Cliente:

* **Portal:** <http://suporte.totvs.com/>

* **Telefone:** (11) 4003 0015

* **Opção 4 – Serviços Administrativos e Financeiros (CST)**

Para maiores informações, consulte o [Guia de Relacionamento e Suporte Fluig](https://suporte.totvs.com/portal/p/10098/guia-relacionamento).

samples1Passo 1

Após a instalação e configuração do TOTVS License Server é necessário também configurar o Fluig ESB para que o mesmo faça comunicação com o TOTVS License Server e consuma as licenças que foram contratadas. Para isto, deve-se acessar as configurações do ESB e na opção **License Configuration** devem ser configuradas as informações do licenciamento do produto, da empresa e dos usuários que utilizam o Fluig ESB. Veja mais informações abaixo:

2Passo 2

Veja abaixo as opções disponíveis na aba **License Configuration**:

* **Company Name:** Razão social da empresa usuária do sistema

* **Federal ID:** Número do CNPJ da empresa

**Contact Information**

* **Name:** Nome da pessoa responsável pelo Fluig ESB na empresa

* **E-mail:** E-mail da pessoa responsável

* **Phone #:** Número do telefone da pessoa responsável

3Passo 3

Também na opção License Configuration deve ser configurado o licenciamento do produto. A licença definitiva é a de categoria *Hard Lock*, na qual é necessário informar os dados de conexão do TOTVS License Server (LS), conforme imagem abaixo:

4Passo 4

Veja abaixo os campos disponíveis na categoria de licença **Hard Lock**:

* **License Category - Opção Hard Lock**

* **Hostname:** Nome ou endereço IP do servidor onde está carregado o TOTVS License Server (LS) com o dispositivo Hard Lock conectado

* **LS Port:** Porta utilizada no servidor informado acima para carregar o TOTVS License Server (LS)

* **Client Port:** Porta da máquina onde esta instalado o Fluig ESB que será utilizada para conectar-se com o TOTVS License Server (LS)

* **Test Connection:** Esse botão tem a finalidade de testar a conexão entre a máquina onde está instalado o Fluig ESB com o TOTVS License Server (LS)

5Passo 5

Outra categoria de licença que pode ser configurada é a licença **Start Key**, impressa na nota fiscal de aquisição do produto e que tem duração de 20 dias, conforme imagem abaixo:

6Passo 6

Veja abaixo os campos disponíveis na categoria de licença **Start Key**:

* **License Category - Opção Start Key**

* **Key:** Chave de licença Start Key

* **Test Validation:** Esse botão tem a finalidade de testar se a chave informada é valida e ainda exibir o número de dias de expiração da licença

7Passo 7

Por fim, caso por algum motivo as categorias de licenças descritas acima não estarem disponíveis para configuração é possível informar uma licença de categoria **Emergencial Key**, que possui validade de 48 horas, conforme imagem abaixo:

8Passo 8

Veja abaixo os campos disponíveis na categoria de licença **Emergencial Key**:

* **License Category - Opção Emergencial Key**

* **Key:** Chave de licença Emergencial Key

* **Test Validation:** Esse botão tem a finalidade de testar se a chave informada é valida
