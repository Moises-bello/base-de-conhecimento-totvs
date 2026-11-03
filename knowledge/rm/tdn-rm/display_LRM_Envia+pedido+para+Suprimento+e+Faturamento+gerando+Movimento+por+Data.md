---
content_hash: 31be7b141270f9fcd01de95f968f74368d5ab19619937cf7cc5248170544f047
fetched_at: '2026-06-29T00:09:14.868755+00:00'
page_id: '421385287'
product: rm
source: tdn-rm
title: Envia pedido para Suprimento e Faturamento gerando Movimento por Data
type: documentation
url: https://tdn.totvs.com/display/LRM/Envia+pedido+para+Suprimento+e+Faturamento+gerando+Movimento+por+Data
version: 3
---

Selecionar o pedido na visão da Requisição de Material, após selecionar a requisição, clique no botão (Gerar movimento por Data) ou Processos | Envio Pedido para Suprimento/Faturamento Gerando Movimento por Data.  
Através desse processo, serão gerados N movimentos de acordo com os períodos planejados, onde para cada período o sistema criará um movimento correspondente no Gestão de Estoque Compras e Faturamento,   
A data de entrega dos itens será a data correspondente ao início de cada período.

**Observação**

* Caso o projeto esteja com a parametrização [Integração TOTVS Aprovação e Atendimentos](https://tdn.totvs.com/x/1tQdGQ) ativa, no momento do Envio do pedido para Suprimentos/Faturamento, gerando apenas um movimento ou gerando movimento por data, o sistema permite que seja gerado o movimento somente se existir um workflow com o status de aprovado. É necessário que o atendimento seja concluído como aprovado para seguir o fluxo normal da Requisição de Material. Caso o atendimento seja concluído como reprovado, identifique quais mudanças devem ser efetuadas. Os itens do pedido de material não poderão ser alterados, assim como o pedido excluído enquanto o workflow não for concluído.
* No momento de enviar o pedido para o Suprimento/Faturamento gerando apenas um movimento ou gerando movimento por data de entrega será possível informar manualmente o fator de conversão para insumos específicos, a fim de chegar o mais próximo possível da quantidade real necessária do insumo na etapa corrente do projeto. Para isso basta acessar Totvs Obras e Projetos | menu Orçamento | Insumos | Cadastros | Pasta Identificação e marcar o Parâmetro 'Fator de Conversão Variável'.
