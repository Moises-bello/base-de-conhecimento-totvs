---
content_hash: 7ce16e005bcdaa726245fdbf54d595fb43021ca89a20451b34b920d3deaae9b4
fetched_at: '2026-06-29T00:11:21.194209+00:00'
page_id: '689066030'
product: rm
source: tdn-rm
title: Painel de dispensação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=689066030
version: 58
---

PainelDispensacaoVisão geral

## **01. VISÃO GERAL**

Ao acessar o menu Painel de dispensação a seguinte tela é apresentada:

Sempre serão apresentados os dados referente ao dia corrente, respeitando-se o turno - caso esteja selecionado.

O usuário poderá alterar o dia pelo filtro de "data" disponível. Além deste estão disponíveis dois filtros para o usuário selecionar: "Local de estoque" e "Escolha o Turno". Para seleção de um local de turno é necessário que um local de estoque esteja definido.

Os dados para o filtro "Escolha o Turno", devem ser cadastrados em "Cadastros > Cadastros de Estoque > Faixas de período do painel de farmácia". Como evidenciado abaixo:

As faixas de período são cadastradas em função do local de estoque.

No grid do painel podemos observar a coluna de Nível de Urgência.

Para cadastrar os níveis de urgência devemos acessar  "Cadastros > Cadastros de Estoque > Níveis de urgência do painel de farmácia".

Os níveis de urgência são cadastrados em função do local de estoque.

Os níveis de urgência ditarão a ordem para a entrega dos itens no painel de dispensação.

Caso o usuário sinta necessidade há um temporizador para que a tela seja atualizada a cada intervalo escolhido.

## **02. Permissões**

Na tela de perfil do usuário existe a possibilidade de o usuário definir quais as permissões que cada perfil possui, vide imagem abaixo.

Separar item somente por código de barra

A partir do patch 12.1.2402.237 foi criado uma nova opção de acesso, para "Desabilitar Busca de Item Manual".

Caso esteja marcado, no Painel de Dispensação somente será permitido separar item pelo código de barra, ou seja, não será permitido pesquisar um produto manualmente e nem escolher um lote.

O botão "Adicionar" continuará permitindo a busca de itens a serem adicionados, independente do parâmetro estar marcado.

**Configuração de Visualização**

Versões Disponíveis

Disponível nas versões 12.1.2306 ou superiores.

O painel de dispensação pode ser configurado por dois modos de exibição.

O primeiro deles é por horário: Na tela de visão do painel será exibido um registro para cada horário de aprazamento da mesma requisição.

A segunda exibição é por turnos: Nela será exibida apenas um registro, que contemplará os aprazamentos compreendidos no turno selecionado, por requisição.

Para definir como deve ser exibido a visão do painel de dispensação os seguintes parâmetros devem ser definidos:

1 - Acessar a tela de perfil de serviços globais: Segurança > Acesso > Perfil

2 - Selecionar o perfil que deseja configurar, clicar em anexos e a opção Parâmetros RM Saúde.

3 - Na tela Parâmetros RM Saúde, acessar a aba Geral 2. A configuração está na secção da Farmácia, conforme imagem abaixo:

Após a configuração de exibição por turno o usuário poderá realizar uma segunda configuração, nela o usuário poderá definir se na tela de dispensação do painel será exibido os itens agrupados por horário ou agrupados por item/turno.

Para realizar essa configuração o usuário deve acessar Menu > Cadastro > Uso Geral > Unidade de Atendimento.

Na tela de unidade de atendimento acessar a aba Farmácia, nela terá a configuração de exibição dos itens na tela de dispensação, vide imagem abaixo.

## **03. Processo Imprime Requisição**

Este processo permite a impressão do relatório da requisição que independentemente da visão do painel da farmácia (por turno ou horário), a requisição completa sempre será impressa. É possível selecionar e solicitar a impressão de múltiplos relatórios simultaneamente.

Um relatório padrão, **SAUREL0158 - Requisição Farmacêutica**, é disponibilizado através do TOTVS Compartilhamento.

Atendimento da requisição

## **02. ATENDIMENTO DA REQUISIÇÃO**

Para acessar o atendimento da requisição basta escolher um registro e clicar no botão de edição, todos os itens do horário selecionado serão exibidos no seguinte formulário:

O formulário possui um cabeçalho onde serão exibidas de forma reduzida as informações sobre o paciente e seu atendimento. Campo de busca para que seja carregada outra requisição sem precisar fechar o formulário. Um campo de login, para que seja realizada a troca do usuário responsável pelo atendimento da requisição sem a necessidade de fazer login no padrão RM.

As informações da requisição são apresentadas em 2 grids separados por status e apenas itens do horário selecionado na view serão exibidos nesse momento.  
Na grid de itens solicitados serão exibidos os itens pendentes de atendimento e os itens que foram cancelados/suspensos. Os itens serão exibidos de acordo com o aprazamento.

Na grid de itens separados são exibidos os itens separados, confirmados ou processados.

Separar item

## **03. SEPARAR ITEM**

### **03.1 SEPARAR VIA NOME DO PRODUTO**

Caso não tenho o código de barra de um determinado produto o usuário tem a possibilidade de pesquisar o produto pelo seu nome ou código para separar, seguindo os passos abaixo.

1 - O usuário deve clicar na lupa, conforme imagem abaixo:

2 - Após clicar na lupa será exibida a tela abaixo com a possibilidade de o usuário pesquisar o nome/código do produto.

Após o preenchimento do nome/código do produto, automaticamente as demais informações serão preenchidas.

Caso o produto seja controlado por lote o usuário deve selecionar qual o lote do medicamento que está utilizando, para isso deve clicar nos "..." ao lado do campo de lote.

Após clicar, será aberta uma tela com a lista de lotes disponível, o usuário deve selecionar o lote e seguir com a separação do item.

### **03.2 SEPARAR COM CÓDIGO DE BARRA**

O usuário tem a opção de informar o código de barras do produto para realizar a separação, para isso, basta preencher o campo código de barras e informar a quantidade.

Ao preencher o código de barras poderá seguir com "enter" para a separação do item, ou clicar sob o botão "Separar Item". 

Após a separação será exibido da seguinte forma:

### **03.3 SEPARAR VIA GRID**

Para os itens que não são controlados por lote, o usuário tem a opção de confirmar todos via grid.

O usuário deve selecionar o checkbox o produto que deseja confirmar e clicar no botão separar item, vide imagem abaixo:

 

Importante

1
complete
Quando utilizado essa função a quantidade total do item será separada, não sendo possível separar a quantidade parcialmente.

2
complete
Os itens são exibidos agrupados pelo item, e em casos de itens controlados por lote, serão agrupados pelo lote do item.

3
complete
O status Separado é uma ação volátil que existe apenas enquanto o usuário estiver passando os itens entre as grids para posteriormente realizar a confirmação. Se não houver a confirmação nem processamento dos itens e o usuário fechar o formulário, o item retornará para a grid de Itens Solicitados com status Pendente.

4
complete
Quando o perfil do usuário estiver marcado a opção "Desabilitar Busca de Item Manual", o usuário NÃO terá a opção de pesquisar pelo nome do produto e nem selecionar um lote. Somente será possível separar item utilizando um leitor de código de barra.
Adicionar item

## **04. ADICIONAR ITEM**

Nessa função o usuário tem a permissão de incluir materiais que não foram solicitados pelo médico.

1 - Na tela de dispensação clicar no botão Adicionar Item.

2 - Após abrir a tela de busca, o usuário deve selecionar o material que deseja incluir na requisição.

3 - Após selecionar o material, usuário deve clicar no botão Adicionar.

4 - Após clicar no botão, o usuário será redirecionado para a tela de dispensação, o material que foi adicionar ficará no grid de Itens Separados.

O material só será salvo após a confirmação, caso feche a tela o material adicionado será removido.

Caso o usuário utilize a função retirar item, o material que foi adicionado e está com o status de separado será removido da requisição.

Retirar item

## **05. RETIRAR ITEM**

### **05.1 RETIRAR ITENS**

É possível remover itens do grid "Itens separados" que ainda estejam com os status Confirmado e Separado. Os itens com o status Confirmado, serão atualizados em banco de dados retornando o status para Pendente, e depois desse processo, serão movidos para o grid de Itens Solicitados. Os itens com o status separado serão movidos diretamente.

1 - O usuário deve selecionar o item com os status Confirmado ou Separado, conforme imagem abaixo:

2 - Após selecionar deverá clicar em retirar item. Caso o grid de Itens Solicitados possuam um item correspondente, o RM deverá somar a quantidade, do contrário será criado um novo registro.

Confirmar item

## **06. CONFIRMAR ITEM**

Para confirmar o item o usuário deve clicar no botão confirmar, todos os itens que estão com o status Separado serão confirmados.

Ao clicar no botão de confirmar será exibido uma mensagem de confirmação, informando que todos os itens separados serão confirmados.

Clicando em sim será exibido alerta e os itens passarão para o status confirmado.

Processar Item

## **07. PROCESSAR ITEM**

Poderão ser processados os itens que estiverem com o status "Confirmado". Para isso será necessário clicar sobre o botão "Processar" e neste momento todos os itens que foram confirmados serão processados.

Mensagem de confirmação:

Neste momento os itens serão movimentados no estoque e lançados na conta do paciente. Após a finalização será exibido alerta de confirmação.

Após a finalização do processamento dos itens no painel de dispensação, um novo pacote é gerado para envio ao menu de "Processos Farmacêuticos". 

anexosAnexos

## **08. Anexos**

No menu Anexos é possível incluir uma Action no Painel de Dispensação, configurando o submenu "Configurar Anexos".

Por exemplo:

### Verifique como **"Configurar Anexos"** da Linha RM, no link  <https://tdn.totvs.com/x/vdKFDg>

No caso do usuário querer visualizar as informações dos itens de Estoque, utilize a SauMovStockItemAction .

Para esta action específica, será permitido apenas a visualização, ou seja, todos os seus Processos e alterações estarão desabilitados.

Baixa Estoque

## **09. Baixa Estoque**

Para o baixa estoque é necessário informar que aquele produto é  baixa estoque sim/ não ou a Definir. Caso as opções sejam SIM/NÃO o procedimento continua da forma que era antes. 

A partir dessa configuração sempre que um item com baixa Estoque a Definir, for solicitado ou inserido, teremos  que  selecionar se esse item é  baixar estoque SIM/Não.

Com o item como baixa estoque a definir, mesmo selecionando pela lupa ou via código de barras, terá que  informar o campo baixa estoque

No grid de itens separados,  é agrupado por Baixa Estoque Sim ou Não . conforme imagem abaixo

Caso eu queira separar os itens solicitados selecionando os mesmos e clicando no botão separar

o sistema ira me perguntar se eu desejo separar os itens que são baixa estoque a definir. Se eu clicar em não... nada acontecera

Mas se eu clicar em sim ele ira aparecer a tela  para que eu informe baixa estoque ; item por item para que eu possa informar se é baixa estoque sim ou não

Tendo o mesmo comportamento se eu não marcar o baixa estoque ele me da uma mensagem

Local de estoque

## **10. Dispensar em locais diferentes do solicitado**

 Recurso disponível nas versões 2506 e superiores

O RM Saúde permite que uma requisição seja dispensada a partir de um local de estoque diferente do que foi originalmente solicitado pelo PEP. Para isso, a permissão **'Permite alterar o local da requisição'** deve ser habilitada para o perfil do usuário na tela de configuração de acessos.

Com a requisição aberta no Painel de Dispensação, o local de estoque pode ser alterado diretamente no lookup **'Local de estoque'**, conforme destacado na imagem abaixo.

Uma vez iniciada a separação de uma requisição, o local de estoque não poderá mais ser alterado, o sistema bloqueia o campo de seleção de local para assegurar que todos os produtos sejam dispensados a partir da mesma origem.   
 A tabela de itens separados indicará o local utilizado.

O RM Saúde está preparado para dispensações parciais, por isso, após processar alguns itens da requisição, o lookup **'Local de estoque'** é desbloqueado. Isso permite que diferentes farmácias colaborem para atender uma mesma requisição em momentos distintos.  
A coluna **'Local de estoque'**, na tabela de **'Itens separados'** exibe onde cada produto foi dispensado. Por padrão, esta coluna só é preenchida para destacar uma exceção, ou seja, quando um item é atendido por um local diferente do solicitado. Se a dispensação ocorrer no local padrão da requisição, o campo permanecerá em branco.

Imprimir etiqueta do pacote

## **11.****IMPRIMIR ETIQUETA DO PACOTE**

Quando uma requisição é processada, a aplicação realiza automaticamente a geração da etiqueta do pacote. Caso isso não ocorra devido a falhas na impressora, ausência de configuração dos parâmetros ou o usuário deseje imprimir novamente, é possível realizar a reimpressão da etiqueta seguindo os passos abaixo:

Acesse o **Painel de Dispensação**:  
*Menu > Farmácia > Gestão da Farmácia > Painel de Dispensação*.

No painel, selecione a requisição desejada para reimpressão da etiqueta. Em seguida, acesse o menu **Processos > Imprimir etiqueta do pacote**.

Somente requisições já processadas devem ser selecionadas para a reimpressão da etiqueta do pacote.

Status Operacional

## **12.** **STATUS OPERACIONAL**

Na lista dos itens separados, há uma coluna "Status Operacional" para indicar a situação da dispensação.

Esta coluna indica com cores diferentes para cada situação, onde ao deixar o mouse sobre a mesma, exibirá uma legenda.

Atualmente este status é baseado no status de autorização da guia, caso exista uma, onde:
