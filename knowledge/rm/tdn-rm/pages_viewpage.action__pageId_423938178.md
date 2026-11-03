---
content_hash: f035a474b2d577abeb5dab29700998d52ca4058d814fc795dc6d5f722b1be0f3
fetched_at: '2026-06-29T00:09:25.844004+00:00'
page_id: '423938178'
product: rm
source: tdn-rm
title: Estoque Terceiros (Estoque)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938178
version: 8
---

Consideramos para o Controle do Estoque de Terceiros, os estoques de propriedade da empresa que estão **COM Terceiros** (fisicamente localizado nas dependências de terceiros) e os estoques **De Terceiros** em poder da empresa (fisicamente localizado nas dependências da empresa). **Em ambos os controles, teremos a informação do proprietário da mercadoria/produto**.   
O estoque **COM Terceiros** compõe o Saldo Atual da mercadoria/produto, porém não esta disponível para movimentações de saídas enquanto não retornar. Em todas as movimentações que afetam o estoque, o sistema irá considerar como saldo disponível para movimentação, a diferença entre o Saldo Atual e o saldo COM Terceiros.

**Estoque Disponível = Saldo Atual – COM Terceiros**

O sistema **bloqueará** a utilização do Controle de Estoque de Terceiros, se o parâmetro geral de Controle de Estoque (*Opções –Parâmetros – Gestão de Estoque, Compras e Faturamento – Gestão de estoque – Definições de Estoque – Saldo de Estoque 1/3*) estiver permitindo trabalhar com estoque **Negativo** no **Saldo Atual**, proporcionando uma consistência real dos dados.  
A mercadoria/produto que possui estoque COM Terceiros, terá o custo médio único na empresa (conforme critério de cálculo do custo médio adotado pela empresa – por local ou por filial).  
O sistema permitirá que o estoque em poder de terceiros utilize o custo por filial que irá conduzir os dados de custo médio por local de estoque para o custo médio por filial.  
O estoque **DE Terceiros** é tratado separadamente do Saldo Atual, **sendo valorizado exclusivamente a custo médio**, calculado de forma distinta do controle interno da empresa, através de fórmulas de valorização do estoque definidas conforme critério da empresa.  
O saldo do estoque **COM Terceiros** e **DE Terceiros** poderá ser consultado através da opção 'Consulta de Saldos e Custos' (CTRL + T) do sistema.  
Para a gestão desse controle no sistema, utilizam-se as tabelas **TESTOQUETERCEIROS** 'Estoque DE/COM Terceiros' e **TRELSLDTERCEIROS** 'Ficha Física dos Produtos DE/COM Terceiros'.  
Todas as movimentações relacionadas ao controle estoque de terceiros serão gravadas na tabela TMOVRELAC e TITMMOVRELAC, sendo o campo TMOVRELAC.TIPORELAC='T'.

---
