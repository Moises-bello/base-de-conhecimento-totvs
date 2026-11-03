---
content_hash: bdbd943064f05d926f2a817ff83681da2ffc621f90961f134ccdac90abcc5fa8
fetched_at: '2026-06-29T00:09:47.082867+00:00'
page_id: '435104913'
product: rm
source: tdn-rm
title: Seguro - Processo - Desfazer Endosso
type: documentation
url: https://tdn.totvs.com/display/LRM/Seguro+-+Processo+-+Desfazer+Endosso
version: 2
---

Processo responsável por desfazer endossos de seguro cadastrados no sistema.

Este processo pode ser executado em endossos com a situação Em Preparação ou Efetivado. Após a execução, as parcelas do endosso e reembolso são canceladas e excluídas.  
O cancelamento do endosso será realizado somente se não houver nenhuma parcela baixada.  
O endosso é excluído do sistema após a execução do processo.  
O seguro endossado terá o seu status alterado de Endossado para Efetivado. As parcelas de despesa e reembolso são geradas novamente. A integração das novas parcelas geradas pelo processo, deverá ser realizada manualmente pelo usuário.
