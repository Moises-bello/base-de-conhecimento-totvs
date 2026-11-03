---
content_hash: 7186f8331ffc2738df57c3af6a41bb7c8e65f32a158d715b057e699c5994cbc2
fetched_at: '2026-06-29T00:09:09.082157+00:00'
page_id: '392495378'
product: rm
source: tdn-rm
title: 3550820 FINANCEIRO01-8602 DT Travamento (LOCK) durante registro online
type: documentation
url: https://tdn.totvs.com/display/LRM/3550820+FINANCEIRO01-8602+DT+Travamento+%28LOCK%29+durante+registro+online
version: 1
---

# Lock nas tabelas ao realizar o registro online através do portal do educacional

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Registro Online |
| **Situação/Requisito:** | Ao realizar a impressão do boleto do aluno pelo portal o sistema não concluía a impressão por conta de erros durante o registro online e causava LOCK na tabela de boletos. |
| **Solução/Implementação:** | Modificado o serviço de registro online para salvar o Json/Xml em outro momento do processamento do registro online para não causar LOCK nas tabelas relacionadas. |
| **Tickets relacionados:** | 3550820 |
