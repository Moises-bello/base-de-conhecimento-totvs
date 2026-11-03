---
article_id: 360028448431
category: Comércio Exterior - Easy Import Control - Purchase - Order
content_hash: 2bcd8648141f3c801d64df368a36354915212ae3ab3ceac7b9c076ac924c588d
fetched_at: '2026-06-28T22:39:41.208342+00:00'
product: protheus
section_id: 1500001538481
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Provisório na
  fase pedido
type: support-article
updated_at: '2021-09-09T14:06:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028448431-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Provis%C3%B3rio-na-fase-pedido
---

**Ocorrência**Geração dos títulos provisórios (PR), fase PO.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**Títulos provisórios (PR) fase PO.   
A seguir apresentam-se as regras para a geração dos títulos no módulo Financeiro:

- É necessário que o PO seja vinculado a uma tabela de pré-cálculo. Recomenda-se que seja informada uma tabela na capa do PO, de acordo com a via de transporte utilizada. Caso isso não ocorra, será considerada a tabela com o código de menor numeração referente à Via de transporte do PO. Se não houver nenhuma tabela relacionada à via, será considerada a tabela de menor código dentre todas as cadastradas.   
  
- Para que sejam gerados todos os títulos provisórios das despesas pertinentes ao processo de importação, é necessário relacionar cada despesa a um fornecedor. Isto é tratado no ambiente Financeiro da seguinte forma:   
Despesa FOB - o título será automaticamente relacionado ao fornecedor informado na capa do PO. Despesa Frete - o título será relacionado ao Agente Transportador informado no PO (pasta Transporte), desde que efetuados os procedimentos de indicação de fornecedor abaixo apresentados. Caso contrário, não será gerado o título. Demais despesas - os títulos serão relacionados com o Despachante informado na capa do PO (pasta Cadastrais), desde que efetuados os procedimentos abaixo apresentados. Caso contrário, não serão gerados os títulos.   
  
Indicação de fornecedor: Deve-se cadastrar o despachante tanto no seu devido cadastro como no Cadastro de Fornecedores e vincular estes 2 cadastros, preenchendo o campo "Fornecedor" do Cadastro de Despachantes com o código criado no Cadastro de Fornecedores. Deve-se proceder de forma análoga para o Agente Transportador.   
  
Exemplo:   
O despachante Lopes Despachos Ltda., foi registrado no Cadastro de Fornecedores com o código "55" e no Cadastro de Despachantes com o código "03". Neste caso, deve-se preencher o campo "Fornecedor" do Cadastro de Despachantes com o código "55".

Caso não seja preenchido o código do fornecedor, somente serão gerados os títulos das despesas FOB e Frete (o título do Frete somente será gerado se for informado um fornecedor para o Agente Transportador).   
  
É possível definir alguns dados padrões para registro dos lançamentos financeiros e, para tanto, deve-se utilizar os seguintes parâmetros:   
MV\_FORDESP Deve-se informar o código default de fornecedor a ser gerado para o despachante, caso não seja nenhum informado;   
MV\_LOJDESP Deve-se informar o código default da loja do fornecedor despachante, caso não seja nenhum informado;   
MV\_NATDESP Deve-se informar o código da natureza default.   
  
Critérios para a geração dos títulos:   
  
- Na geração do pedido de compras, geram-se os títulos provisórios correspondentes ao valor da mercadoria, respeitando as datas de vencimento conforme a condição de pagamento especificada a contar da data prevista de embarque.   
- São gerados os títulos provisórios das despesas informadas na tabela de pré-cálculo, com vencimento baseado na maior data de entrega que houver entre os itens.   
- O valor do título provisório da despesa FOB em reais é calculado com base na taxa de conversão do ambiente Financeiro e, caso a moeda desta despesa não seja uma das moedas especificadas nos parâmetros MV\_SIMB2 a MV\_SIMB5 (símbolo da moeda) o título não será gerado. As demais despesas são calculadas com base nas cotações de moedas registradas no ambiente de importação, sendo considerada a data do dia ou a menor mais próxima que possua cotação para a moeda.   
- Caso o PO seja cancelado ou estornado totalmente, os títulos provisórios correspondentes serão excluídos. Em caso de estorno ou cancelamento parcial, os títulos serão recalculados.
