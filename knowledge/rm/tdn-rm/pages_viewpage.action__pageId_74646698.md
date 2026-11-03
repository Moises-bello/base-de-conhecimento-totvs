---
content_hash: e176a805254632f11ba4271fb2e627eb932893e25748db0fc81ff8fb3509de47
fetched_at: '2026-06-29T00:11:32.300557+00:00'
page_id: '74646698'
product: rm
source: tdn-rm
title: Demonstração do processo de Industrialização (Retorno em 1 NF) - Remetente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=74646698
version: 1
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão de Estoque Compras e Faturamento                       **Versão:** 11.52 e posteriores |
| **Processo** | **:** | Estoque DE/COM Terceiros |
| **Subprocesso** | **:** | Demonstração do processo de Industrialização (Retorno em 1 NF) - Remetente |
| **Data da publicação** | **:** | 13/09/2013 |

### **Demonstração do processo:**

Estoque do produto antes do processo:

Saldo Atual: 10,00

Saldo Disponível: 10,00

Saldo Financeiro: 1.000,00

#### **--> Inclusão do movimento de Remessa Para Industrialização:**

Informar o local de estoque que o produto vai sair e o fornecedor que está sendo enviado o produto para ser industrializado.

Informar o Produto e a Quantidade do produto que será enviado para a Industrialização.

Após o Movimento de Remessa para Industrialização incluído, a verificação do produto na consulta de saldos e custos.

Saldo Atual do produto: 10,00

Saldo Disponível: 0,00

#### **--> Inclusão do movimento de Industrialização Realizada por Terceiros:**

Filtrar o movimento de Remessa Para Industrialização.

Marcar o Item que foi industrializado.

O Movimento de Retorno Simbólico da Mercadoria irá ser aberto.

No Movimento de Retorno Simbólico da Mercadoria incluir o serviço de Industrialização e o preço do serviço.

Informar a quantidade do produto que foi industrializado.

Ao salvar esse movimento de retorno simbólico da mercadoria, o sistema irá gerar automaticamente o movimento de entrada do produto acabado:

O movimento será aberto sem nenhum item, dessa forma o usuário deve informar qual foi produto acabado.

 

Após o movimento de Retorno da Mercadoria Simbólica (Parcial) e Entrada do Produto Acabado o Saldo do produto vai ficar da seguinte forma:

Saldo Atual: 3,00 (Produtos que não foram industrializados)

Saldo Disponível: 0,00 (Porque ainda não foi feito o movimento de retorno do produto não industrializado).

#### --> Inclusão do movimento de Retorno do Produto não Industrializado.

Selecionar o movimento de Remessa Para Industrialização e executar o processo.

O Movimento de Retorno da Mercadoria não Industrializada irá ser gerado com a quantidade do produto que ainda não foi devolvida.

Após a Inclusão do Movimento vamos verificar o Saldo do Produto.

Saldo Atual: 3,00

Saldo Disponível: 3,00

E a consulta do Saldo do Produto Acabado:

Saldo Atual: 2,00

Saldo Disponível: 2,00
