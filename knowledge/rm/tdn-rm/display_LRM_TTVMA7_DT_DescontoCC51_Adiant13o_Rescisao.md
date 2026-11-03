---
content_hash: a86519191b2ef8900e73eb61bcae657a8b470f4a621770d54df1bab7be82802b
fetched_at: '2026-06-29T00:06:23.559123+00:00'
page_id: '224106448'
product: rm
source: tdn-rm
title: TTVMA7_DT_DescontoCC51_Adiant13o_Rescisao
type: documentation
url: https://tdn.totvs.com/display/LRM/TTVMA7_DT_DescontoCC51_Adiant13o_Rescisao
version: 2
---

# DESCONTO DO ADIANTAMENTO DA 2a. PARCELA DE 13o PAGO NO ENVELOPE DE RESCISÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão* |
| **Situação/Requisito:** | *Quando é calculada uma rescisão em dezembro, com a 2a.Parcela de 13o. já processada com data de pagamento posterior à rescisão, existe a opção do usuário transferir os eventos do envelope da 2a.parcela para o envelope de rescisão.*  *Nesta situação ficam no mesmo envelope os eventos de CC 102 (2a.Parcela) e CC 48 (13o.Rescisão), e não é descontado o valor do adiantamento de 2a.parcela no CC 51.* |
| **Solução/Implementação:** | *Ajuste no cálculo de rescisão, para efetuar o desconto do adiantamento de 2a. parcela de 13o. salário no evento de CC 51, mesmo quando o valor pago está no envelope corrente.* |
| **Chamados   relacionados:** | *TTVMA7, TUBSGN* |
| **Versões/Release:** | *11.82.43, 12.1.10* |
