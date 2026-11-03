---
content_hash: 08bf3148c4734b319711182db5d3a38a3fe19e8328256f1a69af79804fc2f5a2
fetched_at: '2026-06-28T21:35:27.898415+00:00'
page_id: '6066527'
product: fluig
source: tdn-fluig
title: Execução do Fluig ESB
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=6066527
version: 14
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**. 

true.\*ndicenone

O Fluig ESB pode ser executado como um programa ou como um serviço do sistema operacional Windows. O benefícios e os procedimentos serão demonstrados a seguir.

O banco de dados configurado para o Fluig ESB deverá estar inicializado para que o mesmo funcione corretamente.

* Caso o banco de dados configurado para o ESB seja o Derby, certificar-se de que o serviço do Windows ESB Derby NT Service esteja operante.

* Caso o Derby não esteja instalado como serviço do Windows, executar o arquivo Startup\_DB.bat contido na pasta bin do diretório de instalação do ESB.

* Caso seja a **primeira execução** do Fluig ESB, será utilizado o banco de dados Derby para iniciar as  através do ESB Editor.

# Programa

---

Um dos benefícios da execução como programa é a visualização em tempo real do log no console do sistema operacional. Para executar o Fluig ESB como programa é necessário executar o arquivo **Startup\_Esb.bat** que se encontra no diretório ESB\_INSTALL\bin onde ESB\_INSTALL é o diretório de instalação do Fluig ESB.

Ao executar o arquivo mencionado, será iniciado o processador de mensagens Fluig ESB. Pode-se também utilizar atalhos ou item do menu iniciar **ESB Startup** para executar o Fluig ESB como programa, caso a opção de criação de atalhos tenha sido marcada durante a instalação.

# Serviço do Windows

---

Como serviço do Windows, o principal benefício desse recurso é a inicialização automática ao iniciar o sistema operacional. Para executar o Fluig ESB como serviço no sistema operacional Windows é necessário efetuar os passos abaixo.

0.5falseServicosfadetrue1Instalar

Para **instalar** o serviço basta executar o arquivo install-esb-service.bat que se encontra no diretório [Instalação\_ESB]\bin. Ao executar o arquivo mencionado, será criado um serviço denominado **TOTVS |** **ESB Service**.

2Iniciar

Para **inciar** o serviço do Fluig ESB, siga os passos abaixo:

1. Abra o Gerenciador de Serviços do Windows executando o comando 'services.msc' no menu **Iniciar** opção **Executar.**
2. Localize o serviço **TOTVS | ESB Service** e de um clique com o botão direito do mouse selecionando '**Iniciar**' na listagem. O serviço também pode ser iniciado selecionando o serviço **TOTVS | ESB Service** na listagem e clicando no link '**Iniciar**o serviço' situado no painel esquerdo.

3Parar

Para **parar** o serviço do Fluig ESB, siga os passos abaixo:

1. Abra o Gerenciador de Serviços do Windows executando o comando 'services.msc' no menu **Iniciar** opção **Executar.**
2. Localize o serviço **TOTVS | ESB Service** e de um clique com o botão direito do mouse selecionando '**Parar**' na listagem. O serviço também pode ser parado selecionando o serviço **TOTVS | ESB Service** na listagem e clicando no link '**Parar**o serviço' situado no painel esquerdo.

Configurar um usuário de rede que possua os privilégios de acesso (administrador) necessários.
