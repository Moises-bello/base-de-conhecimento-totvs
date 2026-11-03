---
content_hash: ef8d9a7ad46b92ac09b715790da99e75f40625f182193a072c4fc251f7fd5482
fetched_at: '2026-06-29T00:10:19.321851+00:00'
page_id: '4813329'
product: rm
source: tdn-rm
title: Movimento fora das datas parametrizadas de movimentação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813329
version: 6
---

BLOCK

Movimento fora das datas parametrizadas de movimentação

FAQ: **Movimento fora das datas parametrizadas de movimentação**

|  |  |
| --- | --- |
| Produto: | RM |
| Ambiente: | Unspecified |
| Versão: | 12 |

Avaliação

**Produto:** Totvs Gestão de Estoque, Compras e Faturamento **Versão: 12  
**Processo do Sistema**: Compras  
**SubProcesso**: Movimentação**

**Sintoma**

Ao tentar incluir/alterar um movimento é apresentada a seguinte mensagem:  
*“Movimento fora das datas parametrizadas de movimentação!”*

**Causas**

A data do movimento não esta compatível com o período parametrizado para movimentação.

Solução

1. Acessar **Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento** **| Parâmetros Gerais | Definições Gerais | Definições Gerais 2/3** e verificar qual o período de movimentação definido no campos Início e Fim.
2. Nos parâmetros do tipo de movimento e na etapa **Movimento – Datas** e verificar a data default do campo **“Data do Movimento Default”,** caso não esteja informada, defina uma data para ser considerada no período de movimentação. Lembrando que a data escolhida também deverá estar habilitada para ser utilizada no tipo de movimento, onde sua edição deverá ser diferente de “Não Edita”.   
     
   Exemplo: A data default do movimento é a Data Extra1. No qual a Data Extra1 também deverá ser habilitada e sua edição deverá ser “Edita”, Edita Obrigatoriamente“ ou Mostra”, conforme conveniência do cliente.
3. Após verificado as parametrização confirmar se durante a inclusão/alteração do movimento a data definida como default do movimento esta dentro do período de movimentação definido. No caso do exemplo acima a data extra1.

**Informações Adicionais**

As possíveis datas que podem ser utilizadas como default de data do movimento são:

* Data de Emissão
* Data Entrada/Saída
* Data Extra1
* Data Extra2
* Data do Sistema
* Data de Processamento
