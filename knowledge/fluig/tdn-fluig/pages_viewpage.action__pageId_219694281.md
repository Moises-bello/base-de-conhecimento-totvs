---
content_hash: 574ab5b0abd181fbff2d34422d5afb829b87d8858dcfc98adba112777e6bf3dd
fetched_at: '2026-06-28T21:35:19.674444+00:00'
page_id: '219694281'
product: fluig
source: tdn-fluig
title: Widget Adicionar ao calendário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=219694281
version: 48
---

# Índice

true.\*ndicenone

# Objetivo do componente

---

O *widget* Adicionar ao calendário permite a criação de eventos que, posteriormente, os interessados podem adicionar como um compromisso em seu calendário do Outlook, do Google, da Apple ou Yahoo.

# Instalação do componente Adicionar ao calendário

---

* Para que esse *widget* seja exibido na lista de *widgets* disponíveis para páginas, primeiramente é necessário fazer o *download* do código-fonte do componente (**Add-to-calendar**) no [diretório público do fluig](https://git.fluig.com/projects/SAMPLES/repos/add-to-calendar/browse) no Git.
* Após acessar o repositório da *widget*, siga as instruções do [README.md](https://git.fluig.com/projects/SAMPLES/repos/add-to-calendar/browse/README.md) para compilar e dar *deploy* no componente.

# Adicionando o widget em uma página

---

O passo a passo abaixo demonstra como incluir o *widget* Adicionar ao calendário em uma página da plataforma.

0.5falsesamplesfadetrue1Passo 1

* Acesse a página em que deseja adicionar o *widget* de calendário, acione o menu de configuração no canto superior direito e selecione a opção **Editar página.**

2Passo 2

* Selecione algum ****slot**** da página em edição e acione **Adicionar uma nova widget****.**

3Passo 3

* No painel de seleção de *widgets*, navegue até a opção **Adicionar ao calendário**, localizada em **Personalizado → Fluig Store → Adicionar ao Calendário**, e acione **Adicionar**.

4Passo 4

* Após a inclusão do *widget* no *slot**,*** preencha os dados do evento e acione **Salvar**. Os campos **Nome do evento**, **Início** e **Término** são obrigatórios.

5Passo 5

* Após salvar as alterações no *widget*, acesse o menu de configuração no canto superior direito e selecione a opção **Publicar página**.

6Passo 6

* Após a publicação da página, será possível visualizar o *widget* e se desejado ,escolher um dos tipos de calendário para incluir o evento.

# Alterações para o widget Adicionar ao calendário

---

Para ter acesso ao código fonte do componente e efetuar alterações no *widget* padrão conforme as necessidades da sua empresa, siga os passos descritos abaixo**.**

Atenção

Caso deseje utilizar o componente padrão e não tenha interesse em personalizá-lo, o procedimento abaixo não é necessário.

0.5falsesamplesfadetrue1Passo 1

* Acesse o [repositório de exemplos do fluig](http://git.fluig.com/projects/SAMPLES), e selecione a opção **sample-fluigaddtocalendar**.

2Passo 2

* No repositório do **sample-fluigaddtocalendar**, selecione a opção **Download** no menu lateral esquerdo e efetue o *download* na pasta de sua preferência.

3Passo 3

* Efetuado o download do **sample-fluigaddtocalendar,** acesse o fluig Studio, acione a opção **File → Import,** no menu superior esquerdo.

4Passo 4

* Selecione a opção **General → Existing Projects into Workspace**.

5Passo 5  

* Selecione a opção **Select archive file** acione a opção **Browse...** e em seguida navegue até o local onde está localizado o arquivo: **sample-fluigaddtocalendar-master.zip** baixado no Passo 2, em seguida acione o botão **Abrir**.

6Passo 6  

* Para finalizar a importação acione o botão **Finish**.

7Passo 7  

* Após a finalização da importação do Projeto para o **fluig Studio** navegue até a raiz do Widget, **fluigStudio > wcm > widget > AddThisEvent** e selecione a raiz com o botão direito e acione a opção **Export**.

8Passo 8

* + Selecione a opção **Fluig > Exportar para o servidor Fluig**.

9Passo 9

* + Selecione o Servidor desejado e acione a opção **Finish**, após a finalização o widget estará disponível para ser adicionados nas páginas do WCM.
  + \* Caso não tenha um servidor cadastrado no seu **fluig Studio,** siga esse tutorial: [Cadastrando servidor fluig no Studio](http://tdn.totvs.com/display/fluig/Cadastrando+servidor+fluig+no+Studio).
