---
content_hash: 6d050ad9ed086ddb14b67e9e5d548c368fa537638c4a7f05310c7ca13c817d80
fetched_at: '2026-06-28T21:35:27.941515+00:00'
page_id: '6066542'
product: fluig
source: tdn-fluig
title: Diagramas
type: documentation
url: https://tdn.totvs.com/display/fluig/Diagramas
version: 18
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**. 

# Índice

true.\*ndicenone

## Criação

Os diagramas identificam o fluxo de informações bem como os componentes utilizados para que o TOTVS ESB processe as mensagens. Para criar um novo diagrama tem-se abaixo os procedimentos.

* Acessar o menu principal **File**, item **New** e subitem **ESB Diagram**.
* Aparecerá uma janela com os seguintes campos que deverão ser preenchidos:

| Campo | Descrição |
| --- | --- |
| Enter or select the parent folder | Deve-se selecionar o projeto e o diretório de armazenamento do diagrama. |
| File name | Nome do arquivo de diagrama com a extensão .esb que deverá ser único em todo o projeto. |

* Após preencher as informações clicar no botão **Next**.
* Aparecerá uma janela com um campo para inserir comentários referentes ao diagrama, se desejado.
* Clicar no botão **Finish**.

O TOTVS ESB Editor abrirá o diagrama criado no painel central contendo uma área de construção de diagramas e à direita uma lista de componentes disponíveis para desenhar o fluxo de informações para o TOTVS ESB. Os componentes disponíveis são discriminados no item  da documentação. Para construir o diagrama deve-se seguir a sequência abaixo.

1. Clique no componente desejado no painel direito e clique dentro do diagrama para inserir o componente desejado.
2. Preencha as propriedades de cada um dos componentes, utilizando o painel **Properties** que é visualizar no painel inferior ao selecionar o componente no diagrama.
3. Faça a conexão entre os componentes utilizando as setas situadas no componente ao selecionar o mesmo no painel central. As setas possuem duas classificações:

* **Seta para o componente:** indica que a mensagem trafegada será destinada ao componente
* **Seta do o componente:** indica que a mensagem trafegada será oriunda do componente

Após configurar o diagrama conforme desejado, pode-se salvar através do menu principal **File** e item **Save**.

## Publicação (*deploy*)

Para que o TOTVS ESB reconheça o novo diagrama construído, é necessário a sua publicação (*deploy*) no servidor TOTVS ESB. Para realizar esse procedimento segue abaixo as etapas.

1 - Na listagem de projetos (painel esquerdo), clicar com o botão direito sobre o arquivo de diagrama.

2 - Selecionar a opção **Deploy to ESB Server....** Aparecerá uma janela com os seguintes campos a serem preenchidos:

| Campo | Descrição |
| --- | --- |
| Server | Servidor TOTVS ESB cadastrado na . |
| Diagram | Tipo de publicação do diagrama podendo ser:  **Add the diagram in the Server:** Adiciona o diagrama selecionado aos já existentes no servidor TOTVS ESB  **Replace the diagram in the Server:** Substitui todos os diagramas existentes do servidor TOTVS ESB pelo diagrama selecionado |

3 - Clicar em **Finish** para iniciar os procedimentos de publicação.

4 - Será mostrado uma mensagem identificando o sucesso da operação.
