---
content_hash: 9e8c238955fbeaf462f0296083ed5bf01c97c7bcd98c1e40c04d5f2322424567
fetched_at: '2026-06-29T00:06:06.052161+00:00'
page_id: '201727915'
product: rm
source: tdn-rm
title: TTCHLV_DT_Geracao_Rescisao_Coletiva
type: documentation
url: https://tdn.totvs.com/display/LRM/TTCHLV_DT_Geracao_Rescisao_Coletiva
version: 3
---

# RESCISÃO COLETIVA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *TOTVS Folha de Pagamento* |
| **Função:** | *Geração da rescisão coletiva* |
| **Situação/Requisito:** | *Ao gerar a rescisão coletiva é apresentado mensagem de advertência, pois mesmo sem aviso prévio misto era enviado o valor de menor data do sistema, causando erro na consulta do banco de dados.* |
| **Solução/Implementação:** | *Foi realizado a validação no campo de data de aviso prévio para não enviar a menor data do sistema.* |
| **Versões/Release:** | *11.83.55* |
