---
content_hash: f6c9f43b0b58a004609866f018942f5022bf9d2a0f9f751636f38972c3f9623e
fetched_at: '2026-06-29T00:10:15.903775+00:00'
page_id: '465383538'
product: rm
source: tdn-rm
title: Movimentação de Estoque RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=465383538
version: 30
---

Tempo aproximado para leitura:**20 min**

## **ÍNDICE**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Processos**
4. **Tela de Movimentação de Estoque**
   1. ****Principais Campos e Parâmetros****
5. **Tela de Itens da Movimentação de estoque**
   1. ****Outras Ações / Ações relacionadas****
   2. ****Principais Campos e Parâmetros****
6. **Transcrição de prescrição**
7. **Libera requisição sem imprimir**
8. **Permissão de acesso à Movimentação de Estoque**
9. **Permite processar item sem confirmar**
10. **Permite devolução por unidade de controle**

MovimentacaoDeEstoqueVisaoGeralVisão Geral

## **01. VISÃO GERAL**

As farmácias, principalmente as hospitalares, dependem de uma logística bastante complexa quanto ao abastecimento e distribuição de medicamentos, uma vez que cabe a elas prestar serviços destinados a saúde, é necessário que tenham em estoque todos os medicamentos prescritos para o bom andamento da instituição de saúde.

**Movimentação de Estoque**

Os processos de Movimentação de Estoque são basicamente dois: os de entrada e os de saída de um produto, material e ou medicamento (MatMed), porém, podemos ter vários tipos de movimentos de Entrada e Saída. Em ambos os casos quando as requisições são processadas, duas ações poderão ser realizadas pelo sistema conforme cada situação:

1. Aumento/diminuição física dos Itens da Movimentação listados.
2. Lançamento automático na conta do paciente dos Itens Listados.

Ao finalizar qualquer tipo de movimentação, os usuários autorizados deverão processar a requisição, que efetivamente irá realizar a movimentação solicitada, ora aumentando ora diminuindo no estoque as quantidade de MatMeds informados. Conheça os principais pontos desse processo:

Cabeçalho da Requisição

São informados os dados básicos do paciente, tais como: Nome, Leito, Acomodação, Local de Uso, Centro de Custo e Quantidade Total de Medicamentos solicitados.

Para movimentações que não são associadas a um atendimento, ou seja, não possui paciente o valor do item é o custo médio e não é consultada a tabela de preço.

**Itens da Movimentação**

Compreendem os dados de todos os itens de MatMed que farão parte da movimentação. Os campos item (código e descrição), quantidade, unidade de faturamento do item, fabricante do item, validade e lote se for o caso, deverão ser informados.

Os Tipos de Movimentação de Entrada de um MatMed no TOTVS Gestão Hospitalar são:

* + **Devolução/Paciente:**são registradas as devoluções de MatMeds que não foram utilizados/aplicados/ministrados no paciente.

Independente do motivo pelo o qual o paciente não utilize mais o MatMed que foi dispensado para ele, deverá ser devolvido ao seu local/almoxarifado de origem.

Há um aumento no estoque do almoxarifado e o item é devolvido da conta do paciente quando a requisição for processada.

Nos Parâmetros de Estoque, caso esteja marcado o campo "Obriga informar número da requisição na devolução de Mat/Med", o campo "Req.Associada" presente na Movimentação de Estoque , será obrigatório preencher.

* + **Devolução de Centro de Custos:**são registradas as devoluções de MatMeds do Centro de Custos da Instituição, que são previamente cadastrados. Caso algum MatMed não for utilizado por algum Centro de Custo, ele poderá ser devolvido ao seu local/almoxarifado de origem.

Os Tipos de Movimentação de Saída de um MatMed no TOTVS Gestão Hospitalar são:

* + **Requisição/Paciente:**são registradas as saídas de MatMeds direto para o paciente. Há uma diminuição no estoque de almoxarifado e o item é lançado na conta do paciente.
  + **Prescrição Médica:**são registradas as saídas de MatMeds direto para o paciente. Há uma diminuição no estoque do almoxarifado e o item é lançado na conta do paciente. A diferença deste Tipo de Movimento para a requisição, é que este é realizado pelo Médico e contém detalhes para a administração do medicamento, tais como: Aplicação (endovenosa, oral, etc.), Dose, Frequência (de 4 em 4 horas, de 8 em 8 horas, 1 vez ao dia, etc.), Dilução (se o medicamento será diluído em alguma solução), a partir de qual horário (horário padrão, agora, ou a partir da hora x, etc.), e a quantidade solicitada, que é calculada em função dos parâmetros acima. Esta prescrição é feita pelo médico utilizando o PEP, ou poderá ser transcrita pela equipe da farmácia e/ou enfermagem utilizando o processo de movimentação de estoque.
  + **Transferência entre Almoxarifados:** tipo de movimentação que há transferência de itens de MatMed de um local de estoque para outro. Nestes casos a responsabilidade de quem irá dar a saída do MatMed será  o almoxarifado de destino, que fará um dos Tipo de Movimentação citados acima.
  + **Folha de Sala:**são registrados o consumo de MatMed de uma cirurgia. Geralmente, após o término da cirurgia, os itens que não foram utilizados são retirados da requisição. Após processamento da requisição, os itens são "baixados" do estoque e lançados automaticamente na conta do paciente.
  + **Requisição para Centro de Custos:**são registradas as saídas de MatMeds para os Centros de Custos da Empresa, que são previamente cadastrados. Servirá para a apuração dos custos de cada setor, posteriormente.

## **01.1 TABELAS UTILIZADAS**

* SZMOVIESTOQUE
* SZMOVIESTOQUEITEM
ExemploExemplo de Utilização

**02. EXEMPLO DE UTILIZAÇÃO**

**Incluindo Movimentação de Estoque**

1. No TOTVS Gestão Hospitalar acesse Farmácia/Movimentação de Estoque.

1. Selecione uma das opções de filtro ou crie um novo filtro clicando em Novo.
2. Clique em OK.
3. Clique em incluir.
4. Na guia Identificação selecione o Tipo de Movimento.
5. Preencha os campos do formulário de acordo com o Tipo de Movimento selecionado.
6. Clique em Salvar.
7. Abra o anexo de Itens da Movimentação de Estoque.
8. Clique em incluir.
9. Será exibido a tela para cadastro do Itens da Movimentação.
   1. Caso o Parâmetro de Estação "Habilita a utilização na estação de trabalho" do Código de Barras estiver marcado, será exibido o formulário de inserção por código de barras.  
        
      Obs¹.: Caso o parâmetro "Assumir 1 como quantidade padrão na Movimentação de Estoque" esteja habilitado, então será inserido por padrão a quantidade 1, caso queira outra quantidade basta informar no campo Quantidade da tela de leitura do código de barras.  
      Obs².: O campo Quantidade não permite valor 0 ou valor negativo.
   2. Senão, será exibido o formulário padrão de cadastro.
10. Preencha os campos do cadastro (Campos obrigatórios e/ou campos habilitados).
    1. Código de barras.
       1. Inserir um código de barras válido (nos padrões EAN16, EAN128 e Datamatrix) e previamente já registrado no cadastro de produto.
       2. Alterar o campo QUANTIDADE para o valor desejado. Este campo fará o arredondamento automático de um valor decimal caso habilitado a opção de "Arredondamento de quantidade fracionada na movimentação do estoque" em Cadastros/Produto/Informações Produto.
    2. Formulário.
       1. Selecione o produto.
          1. Seleção via código.
             1. Preencha o campo Código do Produto.
             2. Pressione a tecla TAB.
             3. As informações do Produto serão preenchidas automaticamente no formulário.
          2. Seleção via formulário de busca.
             1. Pressione o botão de busca () ao lado do campo de Código do Produto.
             2. Será exibido o formulário de busca de produtos.
             3. Preencha os critério de busca da maneira desejada.  
                Obs.: Caso nenhum critério de busca for preenchido, a busca retornará todos os produtos.
             4. Pressione o botão de busca ().
             5. Selecione o produto desejado na tabela.
             6. Clique em OK.
             7. As informações do Produto serão preenchidas automaticamente no formulário.
       2. Preencha os demais campos do formulário.
          1. Caso o parâmetro "Busca automática (lote/validade) pelo método PEPS na requisição de MAT/MED." estiver marcado, após a seleção do produto, o sistema irá retornar o lote ativo automaticamente.
          2. Caso deseje preencher o Lote do produto.
             1. Pressione o botão de busca () ao lado do campo de Lote.
             2. Será exibido uma tela que apresentará todos lotes configurados para aquele produto.
             3. Selecione o Lote desejado na tabela.
             4. Clique em OK.
             5. As informações do Lote serão preenchidas automaticamente no formulário.
11. Clique em Salvar.
    1. Caso seja inserção via código de barras, pressionar Enter para salvar o produto via código de barras. O formulário de código de barras somente será fechado quando o usuário pressionar a tecla ESC.
    2. No formulário padrão, caso o usuário clique no botão OK, os dados serão salvos e o fomulário fechará.
Processos

# **Processos**

No menu Farmácia | Movimentação de Estoque | Processos existem as seguintes opções, conforme permissão de acesso do Perfil do usuário logado:

## **Excluir requisição**

**Nome da action:**SauExcluiRequisicaoProcAction

Será excluído a movimentação e todos os seus itens de requisição.

Caso os itens da requisição seja originado de um Kit Pré-montado, após a exclusão, o status deste kit deve retornar para “não utilizado” novamente

Por exemplo:

**Validações:**

- Movimentação com status “Processado” não será permitido excluir.

- Não será habilitado para o tipo de movimento Transcrição de Prescrição.

**Atenção:**

Dentro da tela “Requisição” existe o botão “Excluir”. Este somente irá excluir apenas o item selecionado.

TelaDeMovimentaçãoTela de Movimentação

## **03. TELA DE MOVIMENTAÇÃO DE ESTOQUE**

**Principais Campos e Parâmetros**

| Campo | Descrição |
| --- | --- |
| Tipo de Movimento | Tipo de Movimento que será referente à requisição. |
| Requisitado por | Nome do usuário que está criando a requisição. |
| Local de Estoque Origem | Local de Estoque no qual será feito a retirada/devolução de produtos referentes a requisição. |

ItensDaMovimentacaoTela de Itens da Movimentação

## **04. TELA DE ITENS DA MOVIMENTAÇÃO DE ESTOQUE**

**Outras Ações / Ações relacionadas**

| Ação | Descrição |
| --- | --- |
| Suspender itens | Suspende itens da requisição, não é possível suspender itens confirmados ou processados. |
| Substituir item | Substitui o item da requisição, não é possível substituir itens confirmados ou suspensos. |
| Desconfirmar | Cancela a confirmação dos itens selecionados. Estes devem estar com o status diferente de Processado e já Confirmados. |
| Confirmar | Confirma os itens selecionados. Devem ter o status diferente de suspenso |
| Confirmar por leitor de código de barras | Confirmar os itens com o leitor de código de barras, é necessário selecionar pelo menos 1 item e informar o código de barras  Obs.: A tela de código de barras deverá permanecer aberta enquanto houver itens a confirmar |

**Principais Campos e Parâmetros**

| Campo | Descrição |
| --- | --- |
| Código do Produto | Código referente ao produto que fará parte da Movimentação. |
| Quantidade | Quantidade física do produto a ser utilizado na Movimentação. |
| Lote | Lote referente ao produto selecionado. Caso o parâmetro CONTROLADOPORLOTE estiver marcado. |

## **1 - Pesquisar o Produto a ser incluído**

## 1.1 - Por Código de Barra

Caso no menu “Ambiente/Parâmetros/Gestão Hospitalar/Parâmetros por Estação de Trabalho” esteja marcado o parâmetro "Habilita a utilização de código de barra na estação de trabalho", será exibido o formulário de inserção por código de barras.

Quantidade Padrão

Caso o parâmetro "Assumir 1 como quantidade padrão na Movimentação de Estoque" esteja habilitado, então será inserido por padrão a quantidade 1, caso queira outra quantidade basta informar no campo Quantidade da tela de leitura do código de barras.  
O campo Quantidade não permite valor 0 ou valor negativo.

## **1.2 - Pesquisar pelo Código do Produto**

O campo “Código do Produto” pode ser preenchido das seguintes maneiras:

**- Seleção via Código:** preencha o campo código do produto, pressione a tecla TAB. As informações do Produto serão preenchidas automaticamente no formulário.

**- Seleção via formulário de busca:** Pressione o botão de busca  ao lado do campo de Código do Produto. Será exibido o formulário de busca de produtos.

Preencha os critérios de busca da maneira desejada.  
Caso nenhum critério de busca for preenchido, a busca retornará todos os produtos.

Pressione o botão de busca

Selecione o produto desejado na tabela.

Clique em OK.

As informações do Produto serão preenchidas automaticamente no formulário.

Exibir Saldo

Nos “Itens da Movimentação de Estoque”, para permitir exibir a coluna “Saldo” ao pesquisar pelo código do produto , é necessário que esteja DESMARCADO o parâmetro “Não exibir saldo na pesquisa de produto” no Perfil do Usuário , no item **Farmácia/Controle de Estoque.**

## **2 - Pesquisar Lote**

### **2.1 -** Caso o parâmetro "Busca automática (lote/validade) pelo método PEPS na requisição de MAT/MED." estiver marcado, após a seleção do produto, o sistema irá retornar o lote ativo automaticamente.

### 2.2 - Caso deseje preencher o Lote do produto.

### Pressione o botão de busca ao lado do campo de Lote.

### Será exibido uma tela que apresentará todos lotes configurados para aquele produto.

Selecione o Lote desejado na tabela

Clique em OK.

As informações do Lote serão preenchidas automaticamente no formulário.

## **5 - Botão SALVAR**

* Clique em Salvar.
  + Caso seja inserção via código de barras, pressionar Enter para salvar o produto via código de barras. O formulário de código de barras somente será fechado quando o usuário pressionar a tecla ESC.
  + No formulário padrão, caso o usuário clique no botão OK, os dados serão salvos e o formulário fechará.

## **4 - Itens/Produtos Compostos**

Ao inserir um item composto será apresentada a seguinte tela, onde deve serão listados os itens contidos no item composto:

1. **Itens para incluir:** Itens que não podem ser confirmados automaticamente, geralmente itens que possuem controle por lote.
2. ****Itens Incluídos:**** Itens que já foram confirmados ao serem incluídos na movimentação de estoque.
   * + **Retirar item(s):** Botão para retirar os itens confirmados a inclusão na movimentação.
     + **Confirmar e adicionar:**Botão para confirmar e adicionar os itens incluídos na listagem no grid 2 **"Itens Incluídos"**.
3. **Itens Controlados por Lote:**
   * + **Quantidade:** A quantidade de itens que devem ser incluídos.
     + **Código de barras:**Código de barras do item
     + **Botão .. :** Selecionar o item por listagem.
     + **Botão Incluir Item(s):**Inclui os itens selecionados no grid¹ "**Itens para incluir"**.

Ao clicar **"Confirmar e adicionar"**  os itens contidos no grid 2 **"Itens Incluídos"**serão adicionados a movimentação.

### **Comportamento de Itens Compostos em Movimentos de Estoque**

Ao utilizar **itens compostos** nos seguintes **tipos de movimento de estoque**:

* Requisição para Centro de Custo
* Transferência
* Devolução para Centro de Custo
* Requisição CME
* Devolução CME

é importante observar que **não será realizada a conversão de unidade de medida** para os itens que compõem o produto composto.

#### **Detalhamento**

Nesse contexto, os componentes do item composto serão sempre lançados utilizando a **unidade de controle** e a **quantidade total**, conforme definidos na estrutura do composto. Ou seja, mesmo que algum dos componentes esteja configurado com **unidade de faturamento**, o sistema desconsiderará essa configuração e lançará os itens exclusivamente com base na unidade de controle.

#### **Exemplo Prático**

Se um produto composto contém um item configurado com unidade de faturamento (ex: caixa) e unidade de controle (ex: unidade), e for requisitado por um dos tipos de movimento listados, o sistema lançará diretamente a quantidade correspondente em **unidades**, sem realizar a conversão de "caixa para unidade".

---

Essa é uma limitação esperada nesses tipos de movimento e deve ser considerada durante o processo de requisição ou devolução para garantir o controle correto dos estoques.

TranscricaoDePrescricaoTranscrição de Prescrição

## **05. TRANSCRIÇÃO DE PRESCRIÇÃO**

**05.1 PERMISSÃO**

Para permitir o usuário faça requisições do tipo transcrição de prescrição, o usuário deve realizar a permissão através da tela de perfil, vide imagem abaixo:

LiberaRequisiçãoSemImprimirLibera requisição sem imprimir

## **06. PROCESSO - LIBERA REQUISIÇÃO SEM IMPRIMIR**

**06.1 VISÃO GERAL**

No menu Movimentação de Estoque, o processo “Libera requisição sem imprimir” irá checar a coluna Impressa/Liberada da movimentação de estoque.

Action = SauLiberaMoviEstoqueSemImpressaoAction

- Para ser exibido o processo é necessário ativar o parâmetro *Não utiliza impressão na movimentação de estoque*

**06.2 PARÂMETROS**

Parâmetros do Gestão Hospitalar - Estoque

Caixa de seleção - Não utiliza impressão na movimentação de estoque

Essa opção estará disponível para usuários/perfis que não possuem permissão para Processar a requisição. 

perfilUsuarioPermissão de acesso à Movimentção de Estoque

Em Serviços Globais, no Perfil de Usuário, será configurado as permissões de acesso aos "Processos" e "Tipos de Requisição" da Movimentação de Estoque da Farmácia.

Por exemplo, o usuário somente conseguirá criar uma requisição do tipo “Requisição para Paciente” se o perfil dele possuir a permissão de acesso.

processaSemConfirmarPermite processar item sem confirmar

## **07. PERMITE PROCESSAR ITEM SEM CONFIRMAR**

Esse parâmetro tem o objetivo de agilizar o processo de dispensação na tela de *Movimentação de Estoque*, eliminando a necessidade de confirmação manual de cada item.

O parâmetro impacta somente as movimentações realizadas através do menu *Movimentação de Estoque.*

Quando ativo, ao adicionar itens na movimentação de estoque, eles serão adicionados como confirmado e assim não tendo a necessidade de confirmar eles antes de processar a movimentação de estoque.

O sistema também permite alterar o lote dos itens pendentes confirmados com esse parâmetro ativo.

DevolucaoUnidadeControlePermite devolução por unidade de Controle

## **08. PERMITE DEVOLUÇÃO UTILIZANDO UNIDADE DE CONTROLE**

**Funcionalidade disponível na versão 12.1.2506 e superiores.**

Esse parâmetro permite que a Devolução, via movimentação de estoques, seja feita pela unidade de Controle, possibilitando  assim a devolução de produtos tanto por unidade de controle quanto por unidade de faturamento.

Ambiente>Parâmetros>Gestão Hospitalar>Estoque

**O parâmetro impacta somente as devoluções realizadas através do menu *Movimentação de Estoque.***Ao ativar o parâmetro, os campos para serem utilizados na Devolução para Paciente serão alterados conforme a imagem abaixo:

Será permitido o usuário escolher a Unidade de Controle para a devolução, levando em conta que ao preencher **"Qnt. p/ Devolução"**o valor da quantidade em faturamento será calculada corretamente.

]]>
