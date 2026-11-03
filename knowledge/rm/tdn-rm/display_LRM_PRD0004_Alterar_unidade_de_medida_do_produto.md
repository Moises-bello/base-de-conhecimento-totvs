---
content_hash: 2e7bb2871b8c04c5f50bd5ccf0e64e95d2119f3223e7c0b879d36bebb587f304
fetched_at: '2026-06-29T00:08:37.065750+00:00'
page_id: '284867872'
product: rm
source: tdn-rm
title: PRD0004_Alterar_unidade_de_medida_do_produto
type: documentation
url: https://tdn.totvs.com/display/LRM/PRD0004_Alterar_unidade_de_medida_do_produto
version: 1
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Versões:** | 11.52 e Superiores |
| **Ocorrência:** | Alteração de Unidade do Produto |
| **Ambiente:** | Cadastro de Produto |
| **Passo a passo:** | Problema Ao tentar alterar a unidade do produto o sistema apresenta a seguinte mensagem:   Causa  1. Existe saldo físico para o produto; 2. Existem pedidos pendentes para o produto; 3. Existem movimentações que afetam saldo para o produto posterior a data de fechamento de estoque. Isto para o caso de troca de unidades que tenha o “Cod. Unidade Base” diferentes.  Solução     1. Regerar Saldos e Custos do produto, marcando a opção “Forçar Regeração Total” (se data de fechamento de estoque não for por saldo). Consultar saldos e custos para o produto e zerar o saldo para a filial/ local que estiveram com saldo maior que zero. 2. Consultar quais são as movimentações pendentes do produto para em seguida faturar/receber ou excluir estes movimentos. 3. Não deixar nenhuma movimentação que afete estoque deste produto posterior a data de fechamento de estoque, ou seja, a data de fechamento de estoque deve ser maior que a última movimentação de estoque do produto.         * **Informações Adicionais**      Uma vez alterado a data de fechamento de estoque NÃO É RECOMENDADO voltar à mesma, pois o saldo dos produtos que tiveram sua unidade de controle altera podem apresentar divergências por não possuírem a mesma unidade base em suas movimentações. |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
