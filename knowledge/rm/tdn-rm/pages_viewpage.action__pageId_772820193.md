---
content_hash: 4c1b7eda84ec3d9ca5d7ddc54cdb26dcf3553b6de9158d1cbbd5021ad33bc0a7
fetched_at: '2026-06-29T00:11:36.496686+00:00'
page_id: '772820193'
product: rm
source: tdn-rm
title: Validação Serviço Tools - SFA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=772820193
version: 3
---

* **Este documento visa realizar a ativação do serviço Tools do SFA após a ocorrência de uma atualização,**
* ***Quando depararem com alguma solicitação deste tipo basta seguir os passos abaixo:***

***Passo a Passo:***

* Acesse o servidor LINUX e execute o comando **sudo su**
* Necessitamos alterar 3 diretórios que possuem a tag de ***driver*** para virar ***driver\_class***

  diretórios:

  /ws/tools

  /ws/sincronizasao

  /home/cloud-user

Para acessar os diretórios acima execute o comando cd / exemplo deste primeiro passo no print abaixo:  
Em seguida execute ll para listar o conteúdo do diretório que está acessando:

Exemplo:

Depois para editar execute o comando **vim hibernate.properties** em cada diretório:

***Comandos para alteração:***

editar: i Habilita o cursor para realizar a digitação e alteração.

sair sem salvar: esc :q! sai do diretório sem salvar

sair e salvar: esc :wq! sai do diretório e salva (Recomendado)

Exemplo imagem:

**Finalizada a alteração nos três diretórios o tools volta a ficar habilitado.**
