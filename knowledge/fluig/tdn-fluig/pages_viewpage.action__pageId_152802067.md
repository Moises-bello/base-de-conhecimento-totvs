---
content_hash: 59123031b11a65358231ede3988faee0448ccc096ccdec916698617af9b7ba08
fetched_at: '2026-06-28T21:35:18.216075+00:00'
page_id: '152802067'
product: fluig
source: tdn-fluig
title: Edição de conteúdo com Windows
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=152802067
version: 59
---

true.\*ndicenone

  

# Introdução

---

A edição de conteúdo permite que o usuário faça a alteração do conteúdo de um documento publicado no TOTVS Fluig Plataforma sem precisar fazer o *download* e posteriormente uma nova publicação ou atualização manual.

Diferente da [edição colaborativa com o Google Drive](http://tdn.totvs.com/x/ukQYDQ), **os usuários precisam ter o Microsoft® Office instalado e configurado em seus computadores**.

# Requisitos para edição de conteúdo

---

requisitos

A máquina de quem irá editar o documento precisa ter o sistema operacional Windows 7 ou superior. Os navegadores e as versões do Office compatíveis podem ser consultados na .

# Extensões suportadas

---

As extensões suportadas para edição de conteúdo com o Windows são:

DOC, DOCX, XLS, XLSX, PPT, PPTX, MPP e ODT.

# Suporte ao HTTP no Microsoft® Office

---

A edição de conteúdo com Windows é realizada por meio do protocolo [WebDav](http://tdn.totvs.com/x/QJoKDg). Porém, nem todas as versões do Microsoft® Office suportam o protocolo WebDAV. Neste caso, para verificação e correto funcionamento, é necessário ter suporte ao HTTP no Microsoft® Office.

Para testar se existe esta configuração no Office, basta abrir um documento direto por um link web, por exemplo: [http://calibre-ebook.com/downloads/demos/demo.docx](http://calibre-ebook.com/downloads/demos/demo.docx "http://calibre-ebook.com/downloads/demos/demo.docx"). No Office 2013 essa ação é realizada acionando **Abrir** >**Outros Locais da Web**, conforme imagem:

Para a edição de conteúdo de documentos com a extensão .doc ou .docx, por exemplo, a plataforma utiliza o protocolo MS-WORD. Esse protocolo é instalado na máquina do usuário durante a instalação do pacote MS Office. Para saber se ele está instalado, o usuário que deseja editar deve acessar em sua máquina a tela de Programas Padrão do Windows, e verificar se o protocolo MS-WORD existe e está associado ao Word. Se esse protocolo não existe, o usuário deve restaurar o seu MS Office ou instalar uma versão mais nova (de acordo com [os requisitos](http://tdn.totvs.com/x/E5MbCQ)).

# Editar conteúdo no TOTVS Fluig Plataforma

---

falseeditar conteúdoPasso 1

* Para editar o conteúdo na plataforma o usuário precisa ter permissão de modificação ou permissão total sobre o documento.

Passo 2

* Na navegação, clique sobre o menu do documento e acione **Editar conteúdo**.

Passo 3

* Para continuar é necessário fazer o checkout do documento. Acione **Sim** para continuar.

Passo 4

* O navegador então tenta abrir o documento com o aplicativo associado ao protocolo **MS-WORD** ou **MS-EXCEL** instalados e configurados no computador;
* Marque a opção **Abrir sempre esse tipo de link no app associado** e acione o botão **Abrir Url: Word Protocol**.
Passo 5

* Agora o MS Office exibirá uma janela de confirmação. Para continuar acione **Sim**.

Passo 6

* Acione o botão **Habilitar Edição** para que o MS Office permita a edição do conteúdo.

Passo 6

* Após editar o conteúdo, acione o botão de **Salvar** e o documento na plataforma será atualizado também.

Passo 7

* Volte para a navegação de documentos e acesse a pasta **Meus Documentos** > **Check-out**.
* Acione o botão de check-in e finalize a publicação. Para saber mais, acesse a documentação sobre [check-in](http://tdn.totvs.com/x/7sgGDg).

## Inconsistências relacionadas com produtos do Office

---

É possível que uma estação de trabalho possua diferentes produtos do Office de versões diferentes, como por exemplo Lync 2013 e MS Office 2010. Com isso, ao utilizar o Webdav na plataforma, o documento não é aberto e na barra de endereços do browser terá o seguinte conteúdo: **ms-excel:ofv|u|http://fluigURL:8080/portal** (caso o documento seja uma planilha do Excel).

Para solucionar essa inconsistência, devem ser seguidos os seguintes passos:

1. Abra a instalação do produto Office 2013, nesse exemplo será utilizado o Lync 2013.
2. Escolha a opção "Adicionar ou remover recursos".
3. Expanda Ferramentas Office.
4. Selecione Suporte para Microsoft Sharepoint Foundation e clique em "Não disponível" (observar figura abaixo).
5. Confirme e, após isso, repare a instalação do Microsoft Office 2010 ou 2007.
