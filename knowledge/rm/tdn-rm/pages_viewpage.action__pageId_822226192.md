---
content_hash: 9b8537899ed33fe20197eb4bb153bbf2b139fb5d881a35bbbdbf8cbf8da27fc8
fetched_at: '2026-06-29T00:11:45.960743+00:00'
page_id: '822226192'
product: rm
source: tdn-rm
title: Importação da Movimentação de Convênios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=822226192
version: 4
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela Processo de Importação da Movimentação de Convênios do Funcionário**
   1. **Principais Campos e Parâmetros**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Neste modulo é possível realizar a importação da movimentação do convênio através de SQL ou layout de importação.

A importação das movimentações dos convênios se baseará em arquivos de importações (.txt) ou base de dados externa, sendo que para o último caso, as informações necessárias serão extraídas por meio de consulta SQL.

O processo definirá o caminho a percorrer, arquivo de importação ou consulta SQL, de acordo com a parametrização feita em [Cadastros - Convênios](https://tdn.totvs.com/pages/viewpage.action?pageId=452719510).

Atenção

Caso no cadastro de convênio não tenha sido cadastrada nenhum tipo de forma de importação, o sistema apresentará mensagem de alerta.

## **02. EXEMPLO DE UTILIZAÇÃO**

11Layout de Importação

Para realizar a importação da movimentação dos convênios via Layout de importação, ou seja, retirar as informações necessárias de um arquivo com extensão “.txt” e importa-las para dentro do sistema, será necessário configurar um layout através do menu Folha de Pagamento | Configurações | Importações | Layout de Importação.

Dentro do menu citado acima, devemos criar um novo layout e nos atentar aos seguintes itens:

* Deverá ser preenchido apenas a descrição para o layout que está sendo criado (Item 1), o campo Layout (Item 2) será preenchido automaticamente ao salvar toda a configuração.

* Na aba “Arquivo Importação”, será necessário fazer a configuração de como o sistema deverá fazer a interpretação do arquivo.

1. Para que o sistema pegue a estrutura de como o arquivo se encontra montado, será necessário selecionar um arquivo como exemplo.

Deverá ser informado também se o arquivo possui um caractere para separar as informações.

2.  Deve-se preencher os itens com as informações que o sistema irá levar em consideração para a leitura do arquivo, sendo:

* + - * + - * + **Separador decimal utilizado no arquivo** – Informar qual será o caractere que está sendo usado como separador de números decimais.  
                **Observação:** No caso do decimal 100,50, se encontra sendo usado a vírgula (,) como separador decimal.

* + - * + - * + **Formato de data utilizado no arquivo** – Informar qual a estrutura da data que se encontra preenchida no arquivo.

* + - * + - * + **Separador do arquivo de importação** – Caso o arquivo possua um separador das informações, deverá ser preenchido com o caractere utilizado.  
                Um exemplo do que é dito acima pode ser visto no campo “Visualização (item 3) ” do print, veja que o ponto e vírgula (;), está sendo usado para separar as informações existentes, sendo que o campo será liberado apenas caso use separador no arquivo.

3. Deverá preencher o campo “Tipo de Layout” com a opção “Importação de Movimento de Convênio de Funcionários”, sendo que o campo “Visualização” será preenchido automaticamente de acordo com o arquivo selecionado.

* A forma de exercer a configuração na aba “Layout” irá variar de acordo com a utilização de separador ou não no arquivo.
  + - * + - **Com Separador**

Será necessário apenas fazer a ligação das informações separadas pelo separador com os campos sendo que o campo “Tipo” será sugerido automaticamente.

Após fazer a configuração acima, basta salvar o processo.

* + - * + - **Sem Separador**

Para configurar o layout sem separador, deverá fazer os seguintes passos:

1. De acordo com o print abaixo, no campo em que se encontra de “Amarelo” e consta uma linha do arquivo, deverá ser selecionado com o mouse um trecho do texto referente a uma determinada informação.

2. Clique no botão “Define a seleção do item” e confirme se a posição inicial e o tamanho estão corretos.

3. Informe a qual campo essa seleção pertence e clique no botão “Confirma seleção de item”.

Após fazer a configuração acima, basta salvar o processo.

Ao finalizar a parametrização do layout de importação ou consulta SQL, deverá acessar Administração de Pessoal | Controle de Convênio – Movimento | Importação da Movimentação de Convênios.

A tela de processos que será aberta, deverá ser preenchida tanto o código do convênio que irá ser considerado para a importação como o intervalo de datas para a importação, no qual deverá estar dentro do período cadastrado no tópico “Período dos Convênios”.

Existirá também dois parâmetros possíveis para marcação, sendo:

* + - * + - **Sobrepor Movimentação já importada –** Caso já exista uma movimentação para o fornecedor, com nota fiscal e data de emissão iguais e que não tenha sido feito o lançamento de nenhuma parcela para o envelope, poderá substituir o mesmo marcando este parâmetro.
          - I**mportar para funcionários com rescisão –** Permitirá que seja importado movimentação para funcionários que já possuem rescisão criada.

Poderá optar também pela forma de exibição do log, variando entre um log mais simples ou detalhado, onde o log detalhado irá retornar as informações com melhor estrutura.

2Consulta SQL

As importações via consulta SQL, conforme já foi dito anteriormente, tem o objetivo de fornecer ao usuário a possibilidade de fazer a importação das movimentações de convênios levando em consideração bancos de dados externos.

Para trabalharmos então com essa opção, deverá ser criado uma nova Consulta SQL no sistema, acessando o menu superior Gestão | Visões de Dados.

Ao adicionar um novo registro, será apresentado a tela a seguir.

Conforme selecionado na imagem acima, deverá ser preenchido o campo “Banco de dados externo” com o link de conexão para a base que contém as informações necessárias.

Ao clicar no lookup (Ícone com três pontos finais), será apresentado todas as conexões a banco de dados criados dentro do sistema, caso não exista o acesso ao banco desejado, clique no botão de incluir.

Preenchimentos campos:

* Nome e Descrição - Adicionar um nome e descrição diferenciado para a conexão que será criada.
* String de Conexão - Clique no lookup (Ícone com três pontos finais) e faça:
  1. Selecione o tipo de banco de dados que será acessado.
  2. Na tela que irá abrir, faça:

1. 1. Preenchimento do campo “Server name” com o nome do servidor que se encontra restaurado a base de dados.
   2. Informe também como será a forma de autentificação para o acesso a base.
   3. Os campos dentro do agrupador “Connect to a database” passarão a ficar  habilitados, podendo ser optado por acesso a base de dados já restaurada ou realizar um "Attach" do arquivo da base de dados.
   4. Ao final do processo, teste a conexão e verifique se terá um retorno de sucesso.

**Observação:** Após configurar a conexão ao banco externo, certifique-se que o campo “Banco de dados externo” se encontre preenchido.

A sentença SQL a ser adicionada, deverá conter e retornar os campos na ordem:

1. Código da coligada
2. Código do convênio
3. Código do serviço do convênio
4. Chapa
5. Código do fornecedor
6. Número da nota fiscal
7. Data de emissão
8. Data de lançamento
9. Valor total
10. Número de parcelas;

Ou seja, após toda a configuração passada a cima, teremos algo como isso:

## **03.** **TELA Processo de Importação da Movimentação de Convênios do Funcionário**

****Principais Campos e Parâmetros****

| Campo | Descrição |
| --- | --- |
| Quebra de Seção | Informar a quebra de seção |
| Seleção de funcionários | Selecionar os funcionários para os quais o movimento será importado |
| Convênio | Código do Convênio que tenha cadastro o layout de importação nele |
| Período de importação | Período para importação |
| Sobrepor movimentação já importada | Sobreporá o movimento já existente |
| Importar para funcionários com rescisão | Importará para funcionários com rescisão |
| Forma de exibição do log | O log poderá ser exibido simples ou detalhado |

## **04. TABELAS UTILIZADAS**

* PFMOVCONVENIO
