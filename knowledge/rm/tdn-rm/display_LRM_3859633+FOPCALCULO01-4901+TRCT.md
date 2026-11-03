---
content_hash: 33e3b1289ad336ff526ec0d531c10bbecccc10efee8f9845bae9580520314f45
fetched_at: '2026-06-29T00:09:13.442929+00:00'
page_id: '420546834'
product: rm
source: tdn-rm
title: 3859633 FOPCALCULO01-4901 TRCT
type: documentation
url: https://tdn.totvs.com/display/LRM/3859633+FOPCALCULO01-4901+TRCT
version: 1
---

# TRCT

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | TRCT |
| **Situação/Requisito:** | Funcionário está em contrato de experiência, porém foi demitido por justa causa, ao emitir o TRCT. No campo 22, o sistema está gerando ” Rescisão antecipada, pelo empregador, do contrato de trabalho por prazo determinado”, onde deveria gerar “Despedida por justa causa, pelo empregador”.  No campo 27 está gerando RA2, onde deveria gerar JC2. |
| **Solução/Implementação:** | Ajuste (SQL) no TRCT dos campos 22 e 27, para emitir o TRCT de acordo com a causa e código de afastamento do funcionário demitido por justa causa (JC2). |
| **Tickets relacionados:** | 3859633 |
