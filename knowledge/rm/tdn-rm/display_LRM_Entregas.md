---
content_hash: 0f49ddb58e41debe7a1fa1533a1898e9fc442ce360a7ec11e9749a82e626d74b
fetched_at: '2026-06-29T00:08:37.561035+00:00'
page_id: '284880156'
product: rm
source: tdn-rm
title: Entregas
type: documentation
url: https://tdn.totvs.com/display/LRM/Entregas
version: 9
---

A aba notas por etapa tem por objetivo realizar a entrega dos trabalhos / avaliações para uma determinada disciplina. Além disso, poderá alterar ,excluir e baixar o arquivo portado.

## **01. PERFIL DE ACESSO**

Habilitar o acesso ao menu: Entrega de Trabalhos e avaliações no perfil do aluno

## **02. ENTREGA DE AVALIAÇÕES E TRABALHOS DISPONÍVEIS**

O professor deverá configurar a entrega do trabalho / Avaliação no portal

**03. ENVIAR ARQUIVO**

Clicando na opção de **Outras ações | Enviar Arquivo**

Parametrização de armazenamento

Para acessar a funcionalidade, será necessário realizar informar as extensões permitidas e o tamanho máximo do arquivo em: **Configurações | Parâmetros | RM Portal |RM Portal | Geral | Portal - Geral 3/15**

Tamanho de arquivo configurado no IIS

A configuração do iis determina o tamanho máximo de arquivo aceito e prevalece sobre a configuração do rm, deve avaliar o tamanho máximo de conteúdo permitido, para configurar esse parâmetro no iis deve seguir os seguintes passos:

* Abrir o Gerenciador do IIS.
* Selecione o site que você deseja configurar.
* Certifique-se de estar na Visualização de Recursos pelo botão na parte inferior do gerenciador.
* Selecione Filtragem de Solicitações e abra-a clicando duas vezes no ícone. O painel Filtragem de Solicitações é exibido.
* No painel Ações no lado direito da tela, clique no link Editar configurações de recursos.... A janela Editar configurações de filtragem de solicitação é exibida.
* Na seção Limites de solicitação, insira o tamanho máximo de conteúdo permitido apropriado (Bytes) e clique no botão OK.
* Reinicie o IIS.
Extensões de arquivos permitidas

Caso o campo "Extensões de arquivos permitidas" esteja vazio, o sistema irá permitir **todas** as extensões possíveis.

## **04. ATUALIZAR , EXCLUIR E BAIXAR ARQUIVO**

Após a inclusão o arquivo, o portal irá habilitar outras opções como: Atualizar o arquivo, Excluir o Arquivo, Baixar o Arquivo

Data e hora limite da entrega do trabalho

O aluno só conseguirá alterar o arquivo até a data e hora limite da entrega do trabalho no portal definida pelo professor.

## **04. VISUALIZAR/****BAIXAR ARQUIVO** **NO PORTAL DO PROFESSOR**

**A partir da versão 12.1.2502, as mudanças estarão disponíveis no Portal do Professor.**

Na tela de Diário de Classe | Digitação de Notas de Avaliação, para as avaliações que possuem a possibilidade de incluir arquivos será possível visualizar e realizar o download dos arquivos entregues. Ao clicar no ícone para ver entrega, será possível realizar o download do arquivo e/ou marcar como visualizado. Arquivos suportados: pdf, txt, jpeg, jpe, png, jpg, doc, docx, xls, xlsx, .zip, .ppt, .pptx

Status dos ícones:

     Olho aberto - Arquivo disponível, mas não marcado como visualizado

     Olho cortado - Entrega marcada como visualizada pelo professor

     Exclamação - Entrega pendente

Os arquivos suportados no preview do modal são: pdf, txt, jpeg, jpe, png, jpg

Quando não for possível visualizar o arquivo no preview será apresentado o aviso "Visualização indisponível para este tipo de arquivo. Faça o download para acessá-lo".
