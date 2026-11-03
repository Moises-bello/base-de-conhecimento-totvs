---
article_id: 13321239085719
category: Originação de Grãos (OG)
content_hash: 7aa862c28494aae76c4c79679e5860a7c06dce2eb9d5933698e0e7508d09afea
fetched_at: '2026-06-28T22:45:41.087205+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - OG262S1 PE Alterar Tarifa - Visão Geral
type: support-article
updated_at: '2025-06-18T11:53:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13321239085719-Agro-Linha-Protheus-AGR-OG262S1-PE-Alterar-Tarifa-Vis%C3%A3o-Geral
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15634706027799) Tempo aproximado para leitura: **00:00:50 min** **Dúvida**  
Em Visão Geral. Como realizar uma rotina de calculo de Serviço Armazenagem (OGA262)?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**

O ponto de entrada OG262S1() esta disponível na rotina de calculo de Serviço Armazenagem (OGA262). Este ponto de entrada permite intervir no valor a ser calculado no serviço.

|  |  |
| --- | --- |
| **Localização:** | OG262S1() |
| **Programa Fonte:** | OGA262 - Cálculo Serviço |
| **Função:** | Intervir no valor a ser calculado no serviço.  Exemplo Uso: Adicionar taxa administrativa no valor já calculado. |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | OG262S1 | Numérico | Não envia parâmetros.  Deverá retornar um valor numérico que será o novo valor da tarifa. | não | |
