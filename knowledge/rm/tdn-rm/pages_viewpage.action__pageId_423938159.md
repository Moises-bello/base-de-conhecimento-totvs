---
content_hash: cdf40a2fee759bcf4982eb87a1e0222b96bad17ad2aabbbfb6910b47039885e2
fetched_at: '2026-06-29T00:09:25.468717+00:00'
page_id: '423938159'
product: rm
source: tdn-rm
title: Recebimento/Faturamento de Movimentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938159
version: 17
---

O recebimento ou faturamento de movimentos é um dos recursos mais importantes do sistema.   
É através dele que transformamos as ordens de compras em recebimento de materiais, que transformamos pedidos de vendas em movimentos de baixa, que realizamos transferência entre filiais dentre outros.  
Utilize esta opção quando o seu movimento de origem for atingir um novo estágio, como deixar de ser um pedido de vendas e passar a ser uma nota de saída.  
Exemplo: Movimento de pedido de venda 2.1.01 foi incluído com sucesso e agora passará a ser uma nota fiscal de venda 2.2.01.  
O processo a ser utilizado neste caso é chamado de Faturamento.  
Se fosse uma entrada, para uma ordem de compras do tipo 1.1.03 se tornar um recebimento de materiais do tipo 1.2.01, o processo chamado seria Recebimento.   
Nos dois casos o comportamento é o mesmo.  
É possível faturar/receber um ou mais movimentos ao mesmo tempo. E selecionando mais de um movimento, temos a opção de:

**Receber:**O sistema realiza o recebimento/faturamento de todos os movimentos de maneira separada.

**Agrupar todos:** O sistema agrupa todos os movimentos , porém ele verifica o parâmetro geral  "*Permite faturar agrupado para diferentes Clientes/Fornecedores*" e se ele estiver desmarcado, o sistema permite agrupar apenas para Clientes/Fornecedores iguais. Se o parâmetro estiver marcado, o sistema agrupa todas as movimentações, porém mantém o cliente/fornecedor da nota de menor número.

**Agrupar por cliente/fornecedor:**O sistema permite o faturamento de N movimentos, porém as movimentações serão agrupadas por cliente/fornecedor.  
Para dar prosseguimento, devemos saber qual é o tipo de faturamento informado nos parâmetros do tipo de movimento de pedido na etapa "Compra/Vendas – Características". São eles:

* **Com seleção do tipo de movimento:**O sistema apresenta todos os tipos de movimentos  que podem ser faturados do mesmo grupo (entrada ou saída). Após a seleção do movimento e execução do processo, o sistema abre a tela do novo movimento ainda não gravado na base para edição de seus dados.

* **Sem seleção do tipo de movimento:**  O sistema não apresenta nenhum movimento para seleção, e gera apenas para o tipo de movimento gerado deafult parametrizado no pedido. Após a execução do processo, o sistema abre a tela do novo movimento ainda não gravado na base para edição de seus dados.

* **Automático:** O sistema gera a movimentação automaticamente para o movimento gerado deafult parametrizado no pedido. E no final do processo apresenta um log com o número de movimentos gerados e/ou alguma mensagem de erro.

* **Com seleção específica do tipo de movimento**  O sistema permite selecionar apenas os movimentos parametrizados como "Selecionados" na etapa "Compra/Venda – Características" no tipo de movimento de pedido. E após a seleção do movimento e execução do processo, o sistema abre a tela do novo movimento ainda não gravado na base para edição de seus dados.

* ·**Automático com seleção específica do tipo de movimento**  O sistema permite selecionar apenas os movimentos parametrizados como "Selecionados" na etapa "Compra/Venda – Características" no tipo de movimento de pedido, e a movimentação é gerada automaticamente após a seleção do movimento.  No final do processo, é apresentado um log com o número de movimentos gerados e/ou alguma mensagem de erro. Assim como a opção do tipo de faturamento na etapa "Compra/Venda – Características" do movimento de origem existem alguns parâmetros que influenciam no processo de faturamento. São eles:

* **Exibição após o faturamento:**

1
incomplete
Voltar para o tipo de movimento de origem

2
incomplete
Permanecer no tipo de movimento gerado

3
incomplete
Exibir diálogo do movimento gerado

4
incomplete
Exibir diálogo do movimento gerado e retornar para o movimento de origem

* **Baixar pedido de venda/compra após geração do movimento:**
  + **Importante:** Quando estiver configurado para "**Baixar para movimento default**" ou "**Baixar para grupo de movimento default**" e o movimento de destino selecionando não atender a essa regra o efeito será semelhante ao "**Não Baixar**", neste caso, sem que exista baixa, processos como estorno não são usuais.

5
incomplete
**Baixa sempre:** O sistema altera o status do movimento de origem para recebido/faturado sempre que o processo de recebimento/faturamento é realizado.

6
incomplete
**Baixa para movimento deafult:** O sistema altera o status do movimento de origem para recebido/faturado apenas se for faturado para o movimento parametrizado como "Movimento Gerado (Deafult)".

7
incomplete
**Baixa para grupo de movimento deafult:** O sistema altera o status do movimento de origem para recebido/faturado apenas se o faturamento for para tipos de movimento do mesmo grupo que o deafult parametrizado. Exemplo*:*Movimento 1.1.01 está parametrizado desta forma (baixa para grupo de movimento deafult), e seu tipo de movimento gerado deafult é o 1.1.03. O sistema irá alterar o status do movimento 1.1.01 para recebido/faturado  apenas se o recebimento for realizado para tipo de movimentos do grupo 1.1xx.

* **Não baixa:**O sistema não altera o status do movimento de pedido após seu recebimento/faturamento.

* **Efeito do pedido:**Este parâmetro é de extrema importância durante o faturamento, pois é nele que definimos se o faturamento parcial será realizado ou não.

* **Faturar Parcialmente - Quantidade:**Será apresentada uma mensagem com as opções: SIM, NÃO e AUTOMÁTICO, onde o usuário deverá optar por uma delas. Optando por SIM, será apresentada a tela para edição do movimento origem que está sendo faturado (esta opção só estará disponível para movimentos que não tenham sido originados de agrupamento). Optando por NÃO, o movimento origem será baixado (concluído) independente de estar sendo faturado parcialmente. Já a opção AUTOMÁTICO, o movimento origem será faturado parcialmente automaticamente.

* **Não Faturar Parcialmente:**O movimento origem será baixado (concluído) independente de estar sendo faturado parcialmente.

* **Faturar Parcialmente Automático - Quantidade:**O movimento de origem será faturado parcialmente automaticamente, fechando a tela de edição do movimento origem

* **Faturar Parcialmente por Valor - Movimento:**O movimento de origem será faturado parcialmente se o valor recebido do movimento for inferior ao valor definido em [Faturamento | Recebimento Parcial por Valor - Valor Utilizado Movimento](https://tdn.totvs.com/pages/viewpage.action?pageId=423938835)

* .**Faturar Parcialmente por Valor - Item:**O movimento de origem será faturado parcialmente se o valor recebido do item do movimento for inferior ao valor definido em [Faturamento/Recebimento Parcial por Valor - Valor Utilizado Item Movimento](https://tdn.totvs.com/pages/viewpage.action?pageId=423938835).

* **Lançamentos Pedido Faturado Parcialmente**

8
incomplete
**Gerar:**O sistema gera o lançamento financeiro  no faturamento parcial. E também confere o que estiver definido no parâmetro  "Lançamentos no faturamento após geração" informado na etapa "Compra/Venda – Outros dados".

9
incomplete
 **Não gerar:**O sistema não gera o lançamento financeiro no faturamento parcial e confere o que estiver definido no parâmetro "Lançamentos no faturamento após geração" informado na etapa "Compra/Venda – Outros dados".

***Atenção!***Durante o faturamento o sistema valida várias consistências definidas entre o movimento de origem e o movimento de destino. Como campos obrigatórios, rateios, valores financeiros,  fórmula de consistência, aprovação, efeitos no estoque e etc. Sempre que houver alguma informação incorreta durante o faturamento, o sistema irá apresentar uma mensagem de erro e não permitirá a realização do mesmo até que a correção seja feita.  
As validações são variadas, e vai depender da parametrização dos tipos de movimento.

* [Como Fazer - Gráfico - Quantidade de Emissão de Notas Fiscais Diárias Durante o Mês Anterior](http://tdn-homolog.totvs.com/pages/releaseview.action?pageId=4813439)
* [Como Fazer - Gráfico - Cliente TOP 5 Durante Determinado Período](http://tdn.totvs.com/pages/viewpage.action?pageId=4813613)
* [Como Fazer - Sentença SQL - Informações do Item de Movimento](http://tdn.totvs.com/pages/viewpage.action?pageId=4813484)

Quando utilizado , sua aplicação se restringe às visualizações de tabelas.

O objetivo é limitar os registros que um usuário pode consultar, garantindo que quando o usuário acessar uma tabela, ela já estará filtrada.

O processo de faturamento não é interrompidos ou barrados por essa configuração.
