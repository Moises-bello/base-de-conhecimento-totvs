---
content_hash: bcc6c03054a47b994ef00246bf6dce58488035afa9e53a6e242c3e3589b4b4cc
fetched_at: '2026-06-29T00:10:31.255503+00:00'
page_id: '521135108'
product: rm
source: tdn-rm
title: Apura perda e ganho
type: documentation
url: https://tdn.totvs.com/display/LRM/Apura+perda+e+ganho
version: 1
---

Marcando esta opção o sistema irá habilitar os controles de Conta para caso de Perda e Conta para caso de Ganho. Esta contabilização é opcional, podendo ser utilizada para contabilizar uma perda ou o ganho ao realizar a baixa de um bem.

A forma de contabilização será a seguinte:  
Caso haja ganho  
Será debitada (D) a conta da baixa e creditada(C) a conta de ganho informada no campo Conta para caso de Ganho.

Caso haja perda  
Será creditada (C) a conta da baixa e debitada (D) a conta de ganho informada no campo Conta para caso de Ganho.  
  
O valor do lançamento de ganho / perda será calculado da seguinte forma:  
PerdaGanho = VrVenda - (VrOcorrência - VrDepreciação)
