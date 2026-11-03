---
content_hash: e934e8ab313bd32de6e500ec104457748633beb8080c6ed1b48df44f750473b9
fetched_at: '2026-06-29T00:11:39.052261+00:00'
page_id: '787855155'
product: rm
source: tdn-rm
title: Utilizando o Repositório
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=787855155
version: 18
---

## Visão geral

A  funcionalidade de armazenamento de arquivos **(FileRepo)** foi idealizado para atender à necessidade de armazenamento de arquivos de forma rápida e simples no sistema.

Com ele, será possível armazenar e acessar arquivos de forma rápida e segura, sem a necessidade de um conhecimento técnico aprofundado.  
A solução oferece uma interface amigável e funcionalidades que permitem gerenciar arquivos de maneira eficiente.

Preparado para vincular arquivos ou documentos em um determinado registro de uma visão.  
Este recurso esta disponível a partir da **versão 12.1.2310**

Antes de continuar a leitura deste texto é necessário seguir os seguintes procedimentos:

1) Utilizando o conector para Google drive

[Como criar credenciais Utilizando Oauth](https://tdn.totvs.com.br/display/LRM/Como+criar+credenciais+Utilizando+Oauth)

    Ou One Drive for Business (A partir da versão 12.1.2506)

2)

repoBackup

Qualquer tipo de arquivo pode ser vinculado a um registro, (Word, Powerpoint, Imagem, PDF, Texto, ZIP), não importa o conteúdo ou tipo de extensão.  
Os arquivos são armazenados em um serviço de repositório de terceiros, como por exemplo o serviço do Google Drive ou One Drive for Business

ATENÇÃO

O RM não armazena os arquivos, apenas realiza a transferência utilizando as Apis fornecidas pelo serviço do terceiro.  
Dessa forma o RM não é responsável pelo armazenamento, manutenção ou backup dos arquivos.

O RM não realiza controle de versão.  
Ao excluir um arquivo ele não poderá mais ser recuperado!

## Segurança e Permissão de acesso

É necessário liberar o acesso a funcionalidade pelo Cadastro de Perfil, habilitando a permissão para o Repositório de arquivos.

## 

Além disso o recurso deve ser implementado para cada Visão que for necessária sua utilização, ou seja, este recurso não é disponibilizado de forma automática.  
Quando a visão tiver o recurso habilitado será apresentado o ícone referente Repositório de Arquivos.

Aviso

A tela de usuários não contém a funcionalidade de Repositório de arquivos, esse print é apenas para exemplificação da funcionalidade.

Clicando neste ícone será apresentada a tela de anexos à direita da visão, onde será possível utilizar o recurso de Repositório de Arquivos.  
Os arquivos estarão vinculados ao registro selecionado na visão.

## Incluindo um arquivo (Upload)

Clicado no botão de incluir, no anexo do repositório de arquivos, será apresentada a tela de identificação.  
Selecione o conector que deverá ser utilizado como repositório.  
Informe o arquivo e sua descrição.  
Selecionando [OK] ou [Salvar], o arquivo será enviado ao repositório e vinculado ao registro selecionado na visão.

Após finalizado o processo de Upload do arquivo, ele estará disponível para ser consultado, ou para realizar o Download.

É permitido incluir mais de uma cópia do mesmo arquivo, usando o mesmo nome. O arquivo será diferenciado pelo identificador e não pelo conteúdo ou nome.  
Este recurso não realiza controle de versão.

## Consultando um arquivo (Download)

Ao selecionar um registro na visão, os arquivos vinculados a este registro serão apresentados no anexo à direita, que é o Repositório de Arquivos.  
Um duplo clique no arquivo vai apresentar a opção de Baixar o Arquivo (Download) e salvar em uma pasta local.

## Editando um arquivo

Não é possível alterar ou editar/atualizar o conteúdo de um arquivo. Apenas a Descrição pode ser alterada.

Caso seja necessário atualizar um documento, o registro antigo deve ser excluído e então o novo deve ser adicionado.

## Excluindo um arquivo

Ao excluir o registro o arquivo também será removido do repositório.
