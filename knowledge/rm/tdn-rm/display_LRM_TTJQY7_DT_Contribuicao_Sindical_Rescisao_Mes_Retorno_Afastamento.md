---
content_hash: bafe7ccc5941b8678cf3bc2da27a50eff33b3bc5caefab7e554f64b1286a2d94
fetched_at: '2026-06-29T00:06:14.957915+00:00'
page_id: '210050672'
product: rm
source: tdn-rm
title: TTJQY7_DT_Contribuicao_Sindical_Rescisao_Mes_Retorno_Afastamento
type: documentation
url: https://tdn.totvs.com/display/LRM/TTJQY7_DT_Contribuicao_Sindical_Rescisao_Mes_Retorno_Afastamento
version: 2
---

# DESCONTO DA CONTRIBUIÇÃO SINDICAL EM RESCISÃO NO MÊS DE RETORNO DO AFASTAMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Contribuição Sindical* |
| **Situação/Requisito:** | *Funcionário com início de afastamento anterior a competência de março, onde a contribuição sindical não foi descontada.*  *Ao retornar o funcionário para ativo e calcular sua rescisão no mesmo mês do retorno, não era permitido lançar o desconto da contribuição sindical.* |
| **Solução/Implementação:** | *Nas situações de afastamentos anteriores à março, a contribuição sindical só pode ser descontada no mês posterior ao retorno do afastamento.*  *Somente no caso de rescisão no mesmo mês do retorno, haverá um tratamento de exceção para permitir o desconto.* |
| **Chamados   relacionados:** | *TTJQY7* |
| **Versões/Release:** | *11.82.42* |
