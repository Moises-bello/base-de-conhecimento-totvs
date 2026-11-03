---
content_hash: cf4c3a42f2b80af9d7aa0b6e65761456ae4c2df5865f2d87832d1b64cf39b156
fetched_at: '2026-06-29T00:10:03.297550+00:00'
page_id: '452719094'
product: rm
source: tdn-rm
title: Considera percentual para exibir no saldo do banco de horas
type: documentation
url: https://tdn.totvs.com/display/LRM/Considera+percentual+para+exibir+no+saldo+do+banco+de+horas
version: 3
---

**Considera percentual para exibir no saldo do banco de horas**

Este parâmetro tem por objetivo considerar o percentual de incidência das horas extras ao apurar o saldo de banco de horas. Caso marcado, será considerado o percentual de incidência da hora extra. Pré-Requisito:

Os eventos de extras devem ter o parâmetro "Considera percentual de incidência" marcado.

**O percentual será demonstrado nas funcionalidades abaixo -** Movimento | Banco de Horas por Dia: Créditos, Débitos e Saldos Movimento | Histórico do Saldo do Banco de Horas: Extra Anterior e Extra Atual Relatório do Espelho do Funcionário: Saldo do Período RM Portal | Saldo do Banco de Horas do Funcionário: Saldo Atual RM Portal | Espelho do Funcionário: Saldo Anterior e  Saldo Atual

**Exemplo:**

Extra Faixa 1: 02:00 Evento: Hora Extra 50% Percentual: 1.5

Extra Faixa 2: 02:00 Evento: Hora Extra 100% Percentual: 2.0

Parametro marcado : Extra Atual: 07:00 (Considerando percentual)

Parametro desmarcado : Extra Atual: 04:00 (Desconsiderando percentual)
