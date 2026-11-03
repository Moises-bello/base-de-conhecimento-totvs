---
content_hash: ec691f2382145d3c22a12dff697b5114f9c4ee13c9a4ca23bc352132a40481dd
fetched_at: '2026-06-29T00:08:58.734620+00:00'
page_id: '361435516'
product: rm
source: tdn-rm
title: 2374797 EDUCACIONAL01-4371 DT Reserva de Exemplares Bloqueados para Consulta
  Interna
type: documentation
url: https://tdn.totvs.com/display/LRM/2374797+EDUCACIONAL01-4371+DT+Reserva+de+Exemplares+Bloqueados+para+Consulta+Interna
version: 1
---

# RESERVA DE EXEMPLARES BLOQUEADOS PARA CONSULTA INTERNA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Bibliotecária |
| **Função:** | Reservas |
| **Situação/Requisito:** | O sistema está parametrizado para liberar reservas de circulação interna e dos 5 exemplares de uma publicação, apenas 1 está marcado para bloquear, porém, ao tentar fazer uma reserva, aparece a seguinte mensagem: "Impossível realizar reserva, pois todos os exemplares disponíveis desta publicação são para consulta interna". |
| **Solução/Implementação:** | Foi verificado que a publicação possuía apenas 1 exemplar bloqueado para consulta interna e os demais não estavam com essa opção marcada, porém, no banco de dados o campo estava vazio e o sistema estava considerava vazio como sendo consulta interna. Foi feita uma alteração no sistema para considerar os campos vazios como NÃO sendo de consulta interna. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
