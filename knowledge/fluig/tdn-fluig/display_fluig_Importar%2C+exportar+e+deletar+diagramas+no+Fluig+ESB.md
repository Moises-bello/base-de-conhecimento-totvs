---
content_hash: 0db58e8765a4c48b272ea3ed86a9a4ff8965a6a5d6af34c350e725f553594fdf
fetched_at: '2026-06-28T21:35:22.648906+00:00'
page_id: '238036968'
product: fluig
source: tdn-fluig
title: Importar, exportar e deletar diagramas no Fluig ESB
type: documentation
url: https://tdn.totvs.com/display/fluig/Importar%2C+exportar+e+deletar+diagramas+no+Fluig+ESB
version: 14
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**. 

# Índice

4true.\*ndicenone

# Objetivo

---

A partir da versão 12 do Fluig ESB há um novo conceito de importação, exportação e exclusão de diagramas. O objetivo desse manual é demonstrar como exportar, importar e deletar os diagramas da versão 12 através do TDS (TOTVS Developer Studio) utilizando o plugin Fluig ESB.

O processo de exportação e importação de diagramas é muito utilizado quando é necessário compartilhar integrações sem precisar acessar um Fluig ESB Server. É necessário que o usuário tenha  juntamente com o plugin Fluig ESB.

# Exportação de diagramas

---

11Passo 1

* Para exportar diagramas do Fluig ESB utilizando o TDS, deve-se acionar o menu **File → Export...** e selecionar a opção **General → Archieve File** e clique sobre o botão **Next**.

2Passo 2

* Selecione o projeto que deseja exportar e informe o local desejado para criar o arquivo de exportação. Por padrão, o projeto será exportado no formato ZIP, mas também é possível salvar o projeto no formato TAR. Clique em *Finish* para concluir o processo de exportação.  
  Agora seu projeto exportado em formato ZIP ou TAR pode ser compartilhado entre equipes de trabalho sem necessitar acessar um Fluig ESB Server.

# Importação de diagramas

---

samples1Passo 1

* Para importar diagramas exportados do Fluig ESB utilizando o TDS, deve-se  
  Para saber o caminho correto do diretório *workspace* que o TDS está utilizando, acesse o menu **File → Switch Workspace → Other...**

2Passo 2

* Descompacte o conteúdo do arquivo ZIP exportado no passo anterior dentro do diretório *workspace* do TDS.  
  Utilizando o TDS, acione o menu **File → Import...** e selecionar a opção **General → Existing Projets into Workspace** e clique sobre o botão **Next**.

3Passo 3

* Clique sobre o botão **Browse** e selecione o diretório que foi descompactado no passo anterior conforme imagem abaixo. Deixe o projeto selecionado na opção **Projects** e clique em no botão **Finish** para concluir o processo de importação.

4Passo 4

* Após concluir a importação é possível **visualizar**, **alterar** e fazer **deploy** para um Fluig ESB server disponível na rede.

# Deletar diagramas do ESB Server

---

Para remover um diagrama importado para o servidor do Fluig ESB siga os passos abaixo:

0.5falseremoveDiagfadetrue1Passo 1

1. Acesse a aba ESB Servers;
2. Clique sobre Servers;
3. Dê um duplo clique sobre o servidor cadastrado;
4. Clique sobre a aba **Diagrams** no Painel Central, conforme imagem abaixo:

2Passo 2

1. Clique sobre a tag do diagrama que deseja deletar;
2. Acione o botão Delete;
3. Clique em **OK** para confirmar a exclusão;
4. Salve o procedimento clicando sobre o ícone Save.

5. **Pronto!**
