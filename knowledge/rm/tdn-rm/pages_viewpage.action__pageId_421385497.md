---
content_hash: 02c8a46942925669c47b693b158f20b513e36c024e677df5466274be2275dbac
fetched_at: '2026-06-29T00:09:16.265437+00:00'
page_id: '421385497'
product: rm
source: tdn-rm
title: Integração > Suprimentos/Faturamento > Geral
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385497
version: 13
---

**Integrado com o Suprimentos/Faturamento:**  
Caso esta opção esteja habilitada, a integração com o Suprimento/Faturamento estará ativa. Para projetos globais essa integração é somente para ativar o menu Utilitários | Conversões | Importar Insumos do Suprimento/Faturamento e Exportar Insumos para o Suprimento/Faturamento, portanto os demais campos não ficam visíveis.  
   
   
**Utiliza Rateio de Centro de Custo**: Informe se os movimentos gerados terão o centro de custo do Totvs Obras e Projetos. Primeiro será verificado se existe centro de custo para tarefa, depois para etapa, obra e, por último, no projeto.

Obs: Se habilitado informar na parametrização do backoffice que utiliza tipo de rateio como valor.  
**Utiliza Rateio de Departamento**: Informe se os movimentos gerados terão o departamento do Totvs Obras e Projetos. Primeiro será verificado se existe departamento para tarefa, depois para etapa, obra e, por último, no projeto.  
Para a Liberação dos Adiantamentos, o Conector necessita gerar um movimento no Suprimentos/Faturamento, e para isso os seguintes parâmetros devem ser informados:  
**Arredondar quantidade na conversão de unidades**:  
Informe se os movimentos gerados terão as quantidades arredondadas na conversão das unidades do Totvs Obras e Projetos para a unidade de compra do Suprimento/Faturamento.  
**Exemplo:**  
Suponhamos que temos um insumo X no Totvs Obras e Projetos com unidade KG (Quilograma) e relacionado a este insumo um produto Y do BackOffice Suprimento/Faturamento com unidade de compra SC20 (saco de 20Kg) com 0 casas decimais. Uma requisição de materiais gerou a seguinte necessidade do insumo X: 210 Quilogramas. Ao enviar a requisição para o BackOffice Suprimento/Faturamento o sistema deve arredondar de 10,5(210 / 20) para 11 (caso o parâmetro esteja marcado) esta necessidade de material, ou seja, será criado um movimento no BackOffice Suprimento/Faturamento com um item de 11 sacos de 20 kg.  
Caso o insumo X tenha 2 casas decimais na sua unidade e sua necessidade seja de 210,555, ao enviar a requisição para o BackOffice Suprimento/Faturamento o sistema deve arredondar a necessidade de 10,52775 para 10,53, mais se for definido na unidade do insumo X 3 casas decimais, o sistema deve arredondar para 10,528.  
**Atenção:** Ao enviar a requisição de materiais para o BackOffice Suprimento/Faturamento, o sistema sempre converte a unidade do insumo para a unidade de compra do BackOffice.  
   
Possíveis situações de conversão:  
   
A unidade do insumo pode ser igual a unidade de compra. O sistema não modifica a quantidade; A unidade do insumo pode ser incompatível com a unidade de compra do BackOffice Suprimento/Faturamento. O sistema informa que a unidade é incompatível e não gera o movimento para o BackOffice. A unidade do insumo pode ser uma e a do produto outra (Kg para solicitação de compras, por exemplo, onde uma é unidade base da outra). O sistema converte de acordo com a unidade base e o fator de conversão; A unidade do insumo pode ser uma e a do produto outra, sendo que ambos têm a mesma unidade de conversão (T para mg, onde a unidade base de ambos é Kg).  
**Exemplo:**  
Suponhamos que temos um insumo X no Totvs Obras e Projetos com unidade SC25 (saco de 25Kg) e relacionado a este insumo um produto Y do BackOffice Suprimento/Faturamento com unidade de compra SC50 (saco de 50Kg). Uma requisição de materiais gerou a seguinte necessidade do insumo X: 1000 Sacos de 25 kg. Ao enviar a requisição para o BackOffice Suprimento/Faturamento o sistema deve converter (caso o parâmetro esteja marcado) esta necessidade de material para a unidade de compra do produto no BackOffice Suprimento/Faturamento, ou seja, será criado um movimento com um item de 500 sacos de 50 kg.Caso o preço orçado esteja sendo enviado para o backoffice, o preço do insumo será convertido para a unidade de compra.  
**Observação:** O BackOffice Suprimento/Faturamento não permite que um produto seja cadastrado sem unidade de compra. O CorporeRM não permite que seja cadastrada uma unidade sem fator de conversão para a unidade base.  
**Enviar descrição completa do insumo para requisição de materiais**   
Se este parâmetro estiver marcado, todo o conteúdo da descrição completa do insumo será enviado para o campo observação do item do pedido na Geração de pedidos no BackOffice Suprimento/Faturamento.  
**Considerar contratos na requisição de materiais**   
**Condição de Pagamento:** Informe a condição de pagamento que será considerada se não houver condição de pagamento definida no cadastro do insumo e nem no cadastro do grupo de custo. Essa condição de pagamento será considerada no cronograma desembolso do projeto.

**Acordo Corporativo**

**Usa acordo Corporativo**

São 4 opções para indicar se o projeto **Não utiliza**  nos seus pedidos, utiliza **Apenas Pedido**, **Apenas Pedido Extra** ou em **Ambos os Pedidos.** Caso utilize em algum dos pedidos ou em ambos, deverá definir o Tipo de Movimento no respectivo campo do parâmetro :

**Prioridade de uso no Pedido**

Para o caso de já existir um contrato do mesmo fornecedor de um Acordo, este parâmetro define qual a prioridade no uso, se será no **Acordo Corporativo** ou no **Contrato de Material.**

**Ordem de seleção do Acordo Corporativo**

Havendo mais de um Acordo com o mesmo item, esse parâmetro irá identificar a ordem de seleção do Acordo: por **Prioridade**, **Preço** e **Prazo** (Todos campos informados no anexo do Item do Acordo, para cada Produto/Serviço associado).

**Cliente para Faturamento**

Com o objetivo de ampliar a flexibilidade na gestão de faturamento de projetos, foi criada a funcionalidade **Cliente para Faturamento**.

Essa novidade permite que um mesmo projeto possa ser vinculado a um ou mais clientes específicos para fins de faturamento, independentemente do cliente principal do projeto.

Essa abordagem atende cenários onde o faturamento precisa ser direcionado para diferentes entidades, como filiais, parceiros ou responsáveis financeiros distintos, garantindo maior controle e aderência aos processos comerciais e financeiros.

A funcionalidade foi desenvolvida de forma parametrizável, permitindo que cada projeto defina se irá ou não utilizar esse recurso, sem impactar os projetos que não necessitam dessa configuração.

**Importante**: Esse parâmetro não será exibido para clientes que utilizam BackOffice Protheus conforme a imagem abaixo.

* Quando definido como Não Utiliza: → não há alteração no comportamento atual do sistema.
* Quando definido como Utiliza: → será habilitado o anexo Clientes para Faturamento no cadastro do projeto.
* O anexo será disponibilizado no Cadastro do Projeto, com as seguintes características:

  + Nome do anexo: Clientes para Faturamento
  + Visível apenas quando o parâmetro estiver como Utiliza
  + Não será exibido para clientes com BackOffice Protheus

Veja também na documenação anexo do projeto :   
  
**Cliente para Faturamento**  
Quando este parâmetro estiver habilitado para utiliza, o sistema permitirá informar um Cliente para Faturamento nos contratos e no processo de integração com Suprimento/Faturamento. Somente clientes cadastrados no anexo “Clientes para Faturamento” do projeto poderão ser selecionados, garantindo que as notas fiscais sejam direcionadas corretamente ao cliente responsável pelo pagamento.
