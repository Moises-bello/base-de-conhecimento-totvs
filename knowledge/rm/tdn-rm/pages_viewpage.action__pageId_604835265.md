---
content_hash: 812d8b0a205944e68b6e20481402967473f4be5562f4defe7c6055b310512327
fetched_at: '2026-06-29T00:10:58.258579+00:00'
page_id: '604835265'
product: rm
source: tdn-rm
title: Processo OPME com utilização do CME
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=604835265
version: 8
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Cadastro de Materiais**
3. **Movimentação de Estoque**
4. **CME**
   1. **Entrada de Materiais**
   2. **Conferência**
   3. **Limpeza**
5. **Preparo**
6. **Esterilização**
7. **Arsenal**

PainelVisão Geral

## **01. VISÃO GERAL**

* Este guia tem como objetivo orientar o usuário a configurar e utilizar o controle de materiais de OPME com reutilização, passando pelo processo de esterilização pelo CME.

* Este guia tem como premissa o entendimento do documento “**MIT043 - R03PT - Especificação de Parametrização - CME**”.
Cadastro de Materiais

## **03. CADASTRO DE MATERIAIS**

* Para iniciar o processo devera acessar o cadastro de materiais do sistema, para configurar/incluir o material desejado. Devemos ir em: Cadastros > Estoque > Produto.

* Selecionar o o material desejado ou o grupo de material de OPME.

* Ao localizar o material, acessar a opção Anexos > Informações – TOTV- Saúde.

* Ao acessar a tela, localizar o campo CME e indicar o Tipo de Material Esterilizável como Material Reutilizável.

* Quando é informado que o material é esterilizável, é necessário indicar quantas vezes este item poderá ser utilizado, pois o sistema passa a controlar a quantidade de utilização e pós atingir o numero de vezes aqui indicado, o sistema não permitira mais a dispensação do item.

* Acessar o menu Anexos > Código de Barras para o CME.

* Nesta tela deverá ser inserido um código de barras para cada item “físico” existente no estoque, pois o controle de utilização do item é feito pelo código de barras, então não é possível controlar vários itens com o mesmo código de barras.

* Cliquei no ícone incluir.

* Gere um código de barras

* Incluir o código de barras na tela.

Movimentação de Estoque

## **04. MOVIMENTAÇÃO DE ESTOQUE**

* Fazer uma movimentação do estoque para este item. Devemos ir em Farmácia > Controle de Estoque > Movimentação de Estoque

* Incluir o tipo de movimento.

* Incluir o tipo de movimento "Requisição para Paciente"

* Selecionarei o paciente que recebera o material.

* Incluiremos o material desejado indo em Requisição > Selecionando o Paciente e dando duplo click.

* Após isso, adicione os itens desejados informando o código de barras ou buscando manualmente

* Após lançados os itens, clicar no ícone “Processar”.

* Finalizando dará a confirmação de sucesso.

* Após o processo de dispensação do material para utilização pelo paciente, vamos começar a fazer o processo de retorno do material para o local de estoque de controle do material OPME, ou seja, o processo de esterilização pelo do CME.
CMEExpurgoEntrada de Materiais

* Acessar o menu conforme imagem abaixo. Devemos ir em Apoio > Expurgo > Entrada de Materiais.

* Selecionar a unidade do CME que será processado o material.
* Indicar qual a origem da pesquisa do material, que deverá ser a mesma da saída da folha de sala.

* S

* Nesta tela ao informar o código de barra que foi dispensado na requisição de dispensação para o paciente, o sistema já identifica o material e carregara os dados na tela, tal como nome do material, a quantidade dispensada, nome do paciente...etc.

* Para executar o processamento, o usuário precisa ter permissão de gerar o tipo de movimento configurado nos parâmetros tratados no documento “MIT043 - R03PT - Especificação de Parametrização - CME”, caso contrário o sistema emitira a mensagem de alerta abaixo.

* Caso não tenha nenhum problema, será apresentanda a mensagem de confirmação da entrada.

* Neste processo o sistema indica que o material foi utilizado pela “N” vez. Ou seja, caso este processo de recebimento de material no Expurgo não for executado, o contador de utilização não sera atualizado.

**OBSERVAÇÃO:**

* Como o material teve a indicação de utilização como duas utilização.

* Ao tentar inseri-lo em uma nova requisição para um novo paciente, o sistem emite a mensagem de alerta de utilização do item, e não permite mais a utilziação.

* Após o recebimento do item, o próximo processo é fazer a conferencia do item.
Conferência 

* Acesse o menu abaixo.

* Indique a unidade do CME que esta trabalhando.

* Será exibida a tela para informar os itens que está fazendo a conferencia, aqui deverá selecionar o item que está em mãos e clica no ícone avançar.

* Ao concluir o processamento será exibida a tela de sucesso.

* A próxima etapa será a limpeza do item
Limpeza

* , acessar o menu abaixo.

* Indicar a unidade de CME que está trabalhando.

Será exibida a tela para as indicações se a limpeza será,

* Manual nada mais será habilitada na tela.
* Automatizada o sistema habilitará os ícones para selecionar os produtos de limpeza e o equipamento utilizado.
* Manual com solução Enzimática, o sistema habilitara para a inclusão de produto de limpeza.
* Manual e Automatizada com solução enzimática, o sistema habilitara o ícone para inclusão de produtos de limpeza e equipamento de limpeza.

* Após configurar o tipo de limpeza do material, será exibida a tela para a seleção dos materiais disponíveis para a limpeza. Marcar os materiais que será processados e clicar no ícone avançar.

* Caso o processo seja concluído com sucesso, será exibida a tela de confirmação.

* Caso consulte o saldo do material, poderá observar que o item selecionar consta no local de estoque configura como local de estoque de limpeza.

Preparo

* O próximo processo é fazer o preparo do material. Acessar o menu abaixo.

* O Preparo do item para a esterilização, selecione a unidade de Esterilização.

* Será exibida a tela para indicar o tipo de operação, sendo as opções abaixo.

* No caso de liberação para esterilização interna será solicitado os dados de “Invólucro” que poderá ser selecionado clicando no ícone três pontinhos.

* Selecionar o Invólucro para a esterilização, que poderá ser selecionado clicando no ícone três pontinhos.

* Ao selecionar o tipo e o invólucro, poderá informar um número de lote (controle interno) e o ciclo da máquina que será iniciado a esterilização e clique no ícone avançar.

* Nesta tela será apresentado os materiais disponíveis para a esterilização, devera ser selecionado os materiais que farão parte do ciclo. Clique no ícone avançar.

* Caso ocorra tudo bem com o processamento, o sistema apresentara a mensagem de finalização.

Esterilização

* Para executar a esterilização, acessar o menu abaixo.

* Nesta tela selecionar a unidade de CME que será executada a esterilização.

* Nesta tela será exibido todos os itens já preparados para a esterilização. Deverá ser selecionar os itens que deverão fazer parte do processo de esterilização.

* Nesta tela deverá ser informado os parâmetros do processo de esterilização. Clique no ícone avançar.

* Será exibida a tela a  ser preenchida (opcional) se houve teste de material biologico.
* Clicar no ícone “Avançar”.

* Caso não ocorre nenhum problema, será exibida a mensagem de finalização.

Arsenal

* Processo processo é receber o material no arsenal, acessar o menu abaixo.

* Selecionar a unidade de CME que vai atuar.

* Indicar de onde estará recebendo o material, podendo ser uma das opções abaixo.

* Selecionar os itens que está recebendo. Clicar no ícone avançar.

* Ao finalizar será apresentada a mensagem de conclusão do processo.

* Nesta tela de saldo, é possível identificar em que parte do processo o item está estocado.
