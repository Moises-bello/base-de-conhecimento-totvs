---
content_hash: b71614e37f4f395818b8047bf93ce6f2d89645fe61557bf66b5f6ce5e35157d7
fetched_at: '2026-06-29T00:09:13.665025+00:00'
page_id: '421385082'
product: rm
source: tdn-rm
title: Associar Faturamento Direto - Dedução de Produto Faturado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385082
version: 19
---

---

# **Objetivo:**

Este processo permite realizar faturamento direto na liberação do período, onde TOTVS Construção Obras e Projetos deverá integrar com o BackOffice (podendo ser TOTVS Gestão de Estoque, Compras ou Faturamento e Protheus)

# **Passos:**

# ****Dedução de Produto Faturado Integrado com o BackOffice** TOTVS Gestão de Estoque, Compras ou Faturamento:**

1) A TOTVS Construção Obras e Projetos | Parâmetros do Projeto | Suprimento e Faturamento | Geral | Integrado com Suprimento e Faturamento.

2) Parametrizar o tipo de movimento no TOTVS Gestão de Estoque, Compras e Faturamento no menu Opções | Parâmetros | Etapa | Projetos| deve se marcar "usa dedução de contrato", escolhendo a opção "obrigatório por item de movimento" ou " Opcional por item de movimento" na opção "Integração Projeto | Informa Projeto/Tarefa.

O parâmetro **Usa Dedução de Contrato,** pode utilizar os seguintes valores que são retornados a partir dos campos no movimento/item de movimento e/ou resultado de alguma fórmula utilizada no mesmo.

* **Valor Liquido:**Composição do Valor Líquido do item:

**Movimento parametrizado para editar "Preço Total do Item":** Acessar os Parâmetros do tipo de movimento, etapa Item-Preços:

**No Item de Movimento:**

**- Se a flag "Preço Total Editado" estiver desmarcada:**  
Valor Líquido = Valor Bruto do Item;  
  
**- Se a flag "Preço Total Editado" estiver marcada:**  
Valor Líquido = Valor Total do Item;  
  
**Movimento NÃO parametrizado para editar "Preço Total do Item":**  
Valor Líquido = Quantidade x Preço Unitário.

* **Valor Bruto Item: Para visualizar esse campo, basta editar o item do movimento integrado.**

* **Valor Opcional 1 Item(Fórmula): Item - Valores Financeiros 1/2, parâmetro Valor Opcional 1**

* **Valor Opcional 2 Item(Fórmula): Item - Valores Financeiros 1/2, parâmetro Valor Opcional 2**

* **Valor Rateio Centro de Custo / Departamento Item: Etapa Rateio C Custo - Departamento**

* **Valor Financeiro: Movimento afetar estoque financeiro.**

Tipo de Movimento - Entrada(1.1.XX ou 1.2.XX): Fórmula de valor financeiro definido nos parâmetros do tipo de movimento na Etapa Estoque/Estoque 2/3.  
  
**Exceção:**  
- Tipo de Movimento parametrizado para buscar custo no movimento relacionado(usado na cópia por referência): Custo do item relacionado multiplicado pela quantidade;

Após definidas as parametrizações no TOTVS Gestão de Estoque, Compras ou Faturamento, realiza-se o vínculo entre produto e dedução, esse vínculo é feito de duas formas:

1) A primeira forma é informando no movimento o código do projeto, tarefa e contrato que o item será vinculado. (O projeto, tarefa e contrato já devem estar incluído no TOTVS Construção Obras e Projetos).

2) No TOTVS Construção Obras e Projetos no menu Controle | Contratos | acesse o contrato vinculado ao projeto.

* Acessar os anexos do contrato | períodos do contrato.
* Selecionar o período e executar o processo "Liberar Período".
* Na tela de Liberar Período na aba de detalhamento da Retenção /Dedução /Adiantamento existe um botão "Adicionar Produtos Faturados a Dedução".
* Ao clicar neste botão será apresentado os itens adicionados ao contrato.
* Ao selecionar os produtos exibidos os mesmos serão adicionados para deduzir na tela de liberação de período do contrato.
* Selecionar o produto a ser adicionado e clicar em ok. (Só serão exibidos produtos (itens de movimento) que possuírem saldo a deduzir maior que zero.
* Após a liberação do período o valor do produto incluído no campo de "Deduções" irá afetar o valor da medição conforme percentual ou valor informado.

No contrato será habilitado o anexo "Produtos Faturados no Contrato" informando a origem do produto no Backoffice o saldo disponível a deduzir.

**Importante:**

* **Os dados apresentados neste anexo servirão apenas para consulta.**  
  **Este anexo ficará visível no contrato, apenas se existir integração com o Suprimento e Faturamento. (Parâmetros do Projeto |Integrações | Suprimento e Faturamento).**
* **Se o vínculo do contrato com o movimento for realizado manualmente na Nota Fiscal no Backoffice, somente contratos com as finalidades de Prestação de Serviço, Contrato de Insumo e Marco Contratual estarão disponíveis.**

* Os produtos apresentados na tela do botão "Produtos Faturados a Dedução" somente serão exibidos se o tipo de movimento (Nota Fiscal 1.2 ou 2.2) estiver parametrizado para "Dedução de Contrato" e não permitir faturamento.
* O contrato é informado na aba Integrações| Projetos | Dedução de contrato do item de movimento.
* O tipo de movimento (Pedido de Compra) também pode ser configurado com "Dedução de contrato", e após o recebimento, o tipo de movimento gerado (Nota Fiscal 1.2 ou 2.2) terá o contrato automaticamente preenchido no campo "Dedução de contrato".

* No TOTVS Construção Obras e Projetos, ao abrir a tela de liberação de período |Detalhamento da retenção / Retenção / Adiantamento e clicar no botão " Adicionar Produtos Faturados a Dedução " serão apresentados os produtos faturados para dedução de contrato.
* O produto deve conter preço pois caso contrário não aparecerá na tela de liberação na opção de dedução.
* No processo de backup de projeto, os dados referentes ao produto e seus valores deduzidos não serão copiados. Isto porque cada produto (item de movimento) do Suprimento e Faturamento será vinculado a um contrato pertencente a um projeto no TOTVS Construção Obras e Projetos. Ao realizar o processo de restauração de backup do projeto este poderá ser feito em outra coligada.

 

# **Dedução de Produto Faturado Integrado com o RM**

1. Para efetuar o faturamento direto com o RM  é necessário informar o código do projeto, tarefa e contrato que o item será vinculado na aba itens relacionados. (O projeto, tarefa e contrato já devem estar incluído no TOTVS Construção Obras e Projetos).
2. No TOTVS Construção Obras e Projetos no menu Controle | Contratos | acesse o contrato
3. Acessar os anexos do contrato | Períodos do contrato.
4. Selecionar o período e execute o processo “Associar Faturamento Direto” ou na tela de Liberação de Período, na aba Detalhamento da Retenção, Dedução e Adiantamento selecione o ícone Produtos Faturados.

5. Nesta tela o sistema exibirá todos os produtos faturados no Backoffice conforme a quantidade de saldo disponível da tarefa. (Caso a tarefa não tenha saldo disponível o sistema não permitirá a dedução.)

Obs.: A possibilidade de manipulação dos dados, dessa tela, depende do parâmetro de projeto Contratos/Liberação/Controle de dedução do faturamento direto, onde a edição só será permitida se o mesmo NÃO estiver definido com a opção "Sem vínculo com movimento (somente valor)", pois com essa opção selecionada, as deduções de faturamento direto devem ser incluída sem vínculo com movimento definindo diretamente no grid o valor desejado. Com a opção "Vínculo por movimento (saldo contrato)" selecionada, a tela permite o preenchimento manual do Valor da Dedução, podendo ainda definir um percentual de aplicação em relação ao saldo da linha selecionada. Com a opção "Vínculo por movimento (saldo tarefa)" selecionada, o sistema passa a preencher automaticamente a coluna Valor Dedução com base no saldo disponível da tarefa, considerando o que já foi medido.

Exemplo:

Foi criado um pedido de material com dois itens

Pedido x

Tarefa 001.01.01 = 500,00

Tarefa 001.01.02 = 100,00

Total do Pedido = 600,00

No Backoffice ocorreu o faturamento desse pedido em sua totalidade .

No RM no Contrato 001 foi realizada uma medição conforme os dados abaixo:

CNT001 → Medição  → Tarefa 001.01.02 = 300,00

                                      Tarefa 001.01.03 = 200,00

                                      Total Medição 500,00

No período 001 do CNT001 ao realizar dedução de produto faturado o sistema permite deduzir apenas 100,00.

# **Dedução de Produto Faturado Integrado com o BackOffice Protheus**

**Este novo modelo de dedução de produto faturado está disponível apenas para integração com BackOffice Protheus EAI 1.0**

Quando integrado com o BackOffice Protheus é necessário configurar o serviço Rest. para realizar a Dedução de Produto Faturado.

Quando o parâmetro "CONSWSAPROPIACAOPROTHEUS" estiver habilitado o faturamento direto rest passará a estar habilitado também utilizando o mesmo parâmetro.  
Para configurar o BackOffice Protheus para utilizar o serviço Rest. acesse: Configurando do serviço Rest. BackOffice Protheus  
   
Para efetuar o faturamento direto ao salvar a nota fiscal no Protheus é informando o código do projeto, tarefa e contrato que o item será vinculado. (O projeto, tarefa e contrato já devem estar incluído no TOTVS Construção Obras e Projetos).

No TOTVS Construção Obras e Projetos no menu Controle | Contratos | acesse o contrato

* Acessar os anexos do contrato | períodos do contrato.
* Selecionar o período e executar o processo "Associar Faturamento Direto".
* Esse processo se dividira em três etapas:
* A primeira consiste em selecionar os produtos para associar aos períodos. Na tela é exibido o saldo total disponível e um campo onde é possível informar o percentual a deduzir.
* A segunda etapa consiste em informar o valor ou o percentual para distribuição por período. Na tela é exibido o total calculado da dedução e um campo para informar que será deduzido.
* A terceira e última etapa do processo é a distribuição por tarefas. O sistema busca através do serviço REST as informações das tarefas, mas nesse momento do processo é possível redefinir se necessário.
* Na tela de Liberar Período na aba de detalhamento da Retenção /Dedução /Adiantamento existe um botão "Adicionar Produtos Faturados a Dedução" ;que chama a mesma tela do processo "Associar Faturamento Direto".
* Na aba de detalhamento de Retenção / Dedução /Adiantamento será apresentado os itens adicionados ao contrato.
* (Só serão exibidos produtos (itens de movimento) que possuírem saldo a deduzir maior que zero. (Condição do Protheus)
* Após a liberação do período o valor do produto incluído no campo de "Deduções" irá afetar o valor da medição conforme percentual ou valor informado.
* No contrato será habilitado o anexo "Produtos Faturados no Contrato" informando a origem do produto e o saldo disponível a deduzir. Os dados apresentados neste anexo servirão apenas para consulta.
* Este anexo ficará visível no contrato, apenas se existir integração com o Suprimento e Faturamento. (Parâmetros do Projeto |Integrações | Suprimento e Faturamento).

 

Recursos Adicionais

---

[DT\_Dedução de Produto Faturado](http://tdn.totvs.com/pages/viewpage.action?pageId=379293680)
