---
content_hash: 976afa7801015cf075a08396321e817bd6c7993d1f10723d23d2a248fb84d811
fetched_at: '2026-06-29T00:08:17.111243+00:00'
page_id: '253985038'
product: rm
source: tdn-rm
title: TVFSXF_DT_Contratado_Solicitante
type: documentation
url: https://tdn.totvs.com/display/LRM/TVFSXF_DT_Contratado_Solicitante
version: 3
---

# Ajuste na tag de Contrato Solicitante

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Faturamento para Convênios |
| **Requisito:** | É necessário que o sistema envie o prestador solicitante nos dados de Contratado Solicitante, caso ele possua credenciamento com o convênio. |
| **Implementação**: | Criada parametrização nas Condições Contratuais com o Convênio que indique a informação que será enviada na tag "*contratadoSolicitante*" no faturamento ANS.  Parâmetro: **Enviar médico Solicitante Credenciado DIRETAMENTE nos dados do "contratadoSolicitante"**. |
