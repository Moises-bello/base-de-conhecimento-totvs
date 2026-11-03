---
content_hash: b4f1c373e247f9ecb76b2c91725ca5110358ced53cb1e879f5f58e385f997dda
fetched_at: '2026-06-29T00:06:15.021571+00:00'
page_id: '210051495'
product: rm
source: tdn-rm
title: TTNMZY_DT_Contribuicao_Sindical_Rescisao_Mes_Retorno_Afastamento
type: documentation
url: https://tdn.totvs.com/display/LRM/TTNMZY_DT_Contribuicao_Sindical_Rescisao_Mes_Retorno_Afastamento
version: 1
---

# DESCONTO DA CONTRIBUIÇÃO SINDICAL EM RESCISÃO NO MÊS DE RETORNO DO AFASTAMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Contribuição Sindical* |
| **Situação/Requisito:** | *Funcionário com início de afastamento anterior a competência de março, onde a contribuição sindical não foi descontada.*  *Ao retornar o funcionário para ativo e calcular sua rescisão no mesmo mês do retorno, não está permitindo lançar o desconto da contribuição sindical.* |
| **Solução/Implementação:** | *Nas situações de afastamentos anteriores à março, a contribuição sindical só pode ser descontada no mês posterior ao retorno do afastamento.*  *Somente no caso de rescisão no mesmo mês do retorno, haverá um tratamento de exceção para permitir o desconto.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTNMZY* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |
