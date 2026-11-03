---
content_hash: 7fb9c1c857e327f88b3f494011f7c6e0bce2e41062e6305eb10f775fc5054696
fetched_at: '2026-06-29T00:10:50.847938+00:00'
page_id: '563445162'
product: rm
source: tdn-rm
title: Gráfico em Relatórios no RM Reports.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=563445162
version: 3
---

### **CONTEÚDO**

1. ### **Visão Geral**
2. **Exemplo de utilização**

**01. VISÃO GERAL**

 Documentação criada para elaborar um exemplo de como criar filtros no 

**02. EXEMPLO DE UTILIZAÇÃO**

### **Dados de relatório de grupo:**

  Faça o seguinte para agrupar dados em um relatório:

* Abra um aplicativo de relatório existente ou crie um novo
* Vincule o relatório à tabela "Produtos" do banco de dados.
* Solte o campo "Nome do produto" da lista de campos a banda de detalhes do relatório.

* No painel "**Group and****Sort**", clique em "**Add a Group"** e selecione os critérios do grupo (por exemplo, o campo "CategoryID").

* Ative a caixa de seleção "**Mostrar rodapé"** para adicionar um rodapé de grupo ao relatório.

* Solte o campo "**CategoryID**" no cabeçalho do grupo para exibir os títulos dos grupos no relatório.

### **Criando o Gráfico:**

* Solte o controle XRChart (Gráfico) disponível no toolbox (Caixa de Ferramentas) no Group Footer (Rodapé do grupo).

* Automaticamente o Chart Designer (Designer Gráfico) é aberto, quando arrastado o gráfico. Caso não abra, clique na marca inteligente do gráfico e selecione o comando "**Executar Designer".**

* No Chart Designer, clique no botão de adição para adicionar uma nova série

         

* Selecione a série criada e mude para a guia **Dados** .

  Nesta guia, solte o campo "**ProductName**" na área **Argument (Argumento)** e o campo "**UnitPrice (Preço unitário)**" na área **Value (valor)**

* Alterne para a guia **Propriedades** e clique no botão de reticências da propriedade **DataFilters (Filtro de Dados).**

* No **Editor de coleta de filtro de dados** , clique em **Adicionar** para criar um novo filtro.

  Defina as propriedades **ColumnName (Nome da coluna)** e **ValueBinding** **(Vinculação de Valor)** do filtro para o campo "CategoryID" que é usado como critério de grupo no relatório.

false

Somente a configuração **ValueBinding** **(Vinculação de Valor)**é considerada quando as propriedades **Value (valor)** e **ValueBinding **(Vinculação de Valor)**** são especificadas para um filtro de dados.
