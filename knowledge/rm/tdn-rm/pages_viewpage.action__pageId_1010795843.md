---
content_hash: 5068c976563a5b53318b1062a85c6c1172ece627e2b70520126b41e14d333706
fetched_at: '2026-06-29T00:05:47.333700+00:00'
page_id: '1010795843'
product: rm
source: tdn-rm
title: Painel de Separação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1010795843
version: 11
---

painelSeparacaoDeckVisão Geral

# **01. VISÃO GERAL**

## **01.1.** **Confirmando Itens da Ordem de Manipulação**

A tabela de itens no painel de separação exibe o Princípio Ativo e a Concentração do produto e permite separar dois produtos de apresentações distintas, por exemplo um de frasco de 20ML e outro de 100ML para o mesmo princípio ativo.  
O sistema permite que sejam bipados até atingir a a quantidade exata prescrita ou acima. Após atingir a quantidade prescrita não será mais permitido bipar mais para o mesmo princípio ativo.

### **01.1.1.** **Atualizações do Status do Itens da Ordem de Manipulação**

Os itens que estiverem listadas no painel de separação, poderão refletir três status possíveis:

* Pendente: correspondendo à itens que ainda não começaram a ser separados.
* Parcial: correspondendo à itens que já possuem alguma quantidade separada.
* Confirmado: correspondendo à itens que não necessitam mais de separação.

### **01.1.2.** **Itens confirmados**

Na tabela de Itens confirmados a quantidade dos itens são exibidas na unidade de controle do produto, e será criada uma linha para cada lote do produto separado.

É possível desfazer a separação de um item clicando no ícone de Excluir e confirmando a exclusão.

### **01.1.3.** **Itens não manipulados**

Quando houver a necessidade de dispensar um item diretamente, sem que ele passe pelo fluxo de manipulação, a fim de otimizar o processo e agilizar a entrega de medicamentos que não requerem manipulação é possível selecionar uma linha  e clicar em **Não Manipular**. 

## **01.2.** **Status da Ordem de Manipulação**

As prescrições que estiverem listadas no painel de separação, poderão refletir três status possíveis:

* Pendente: correspondendo à prescrições que foram liberadas e que possuem itens para separação, e que ainda não está "selecionada" por nenhum usuário.
* Em Separação: correspondendo à prescrição selecionada por algum usuário.
* Finalizado: correspondendo à prescrições que não possuem mais itens para separação.

### **01.2.1.** **Atualizações do Status da Ordem de Manipulação**

Todas as ordens de manipulação iniciam com o status **Pendente.**

Ao selecionar uma ordem de manipulação na listagem e clicar em **Editar** o status é alterado para **Em Separação**, se fechar a ordem de manipulação o status continua como **Em Separação**.

Se com a ordem de manipulação clicar em **Finalizar** a ordem será atualizada para o status **Pendente** quando ela ainda conter itens que não foram separados ou marcados como **Manipular** Não. Se todos os itens estiverem com o status Confirmado, ao clicar em **Finalizar** a ordem de manipulação será atualizada para o status **Finalizado**.

Unidades de Medidas

# **02. UNIDADES DE MEDIDAS**

## **02.1.** **Unidade de medidas exibidas**

O painel de separação exibe diferentes unidades de medidas dos produtos.

**Campos contornados com verde**

Na tabela de *Itens* os produtos são exibidos na unidade prescrita, tanto para *Quantidade prescrita*, como para a *Quantidade confirmada*.

**Campos contornados com azul**

Durante a separação, ao utilizar o leitor de código de barras, é utilizado a unidade de controle na *Quantidade*, assim também, na tabela de *Itens confirmados* os produtos são exibidos com Quantidade na unidade de controle.

## **02.2.** **Conversão das unidades de medidas**

Para a conversão entre essas unidades é utilizada a Equivalência de dosagem cadastrada na

Rótulo do Medicamento

# **03. Rótulo do Medicamento**

## **03.1.** **Imprimindo um rótulo**

O painel de separação permite imprimir o rótulo de todos os medicamentos manipulados ou de um medicamento selecionado na lista.

São gerados rótulos somente para os medicamentos cadastrados no protocolo oncológico, então não serão gerados rótulos para diluentes e materiais.

**Exibição do relatório**

O rótulo será exibido numa nova janela que possui as opções de salvar e imprimir o rótulo.

## **03.2.** **Informações do rótulo**

Enquanto o medicamento não for manipulado, algumas informações não serão serão exibidas pois necessitam da manipulação para serem disponibilizadas.

As informações exibidas somente após a manipulação são as seguintes:

* Data do Preparo
* Validade
* Nome e registro do manipulador

## **03.3.** **Configurando o relatório do Rótulo**

O relatório está disponibilizado no TOTVS Compartilhamento e deve ser importado no menu Gestão → Smart View

Após a importação ele deve ser configurado para ser usado no painel de separação em Parâmetros →  Gestão Hospitalar → Estoque 

Dispensando durante a separação

# **04. Dispensando durante a separação**

## **04.1.** **Dispensado via Não Manipular**

Durante a separação é possível dispensar os medicamentos, movimentando estoque e lançando o item na conta no paciente através da opção Não manipular.

**Janela Não Manipular**

Após selecionar um item na lista e clicar em não manipular será aberta uma janela onde terá a opção **Dispensar?** e selecionando ela será possível realizar a leitura do código de barras ou pesquisar o produto, após isso podem ser liberadas as opções de **Número de Lote** e **Baixa Estoque** de acordo com o cadastro do produto.

**Momento da Dispensação**  
A movimentação do produto e o lançamento na conta só irá ocorrer ao **Finalizar** a separação quando todos os itens já estiverem com o status **Finalizado.**
