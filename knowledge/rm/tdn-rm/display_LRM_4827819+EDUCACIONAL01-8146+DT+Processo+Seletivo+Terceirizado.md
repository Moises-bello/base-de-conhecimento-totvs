---
content_hash: 0b765b48fd7234ea0ac64e66834b64676e5633c4daa99cafb6adbd919cba1c0d
fetched_at: '2026-06-29T00:10:12.359632+00:00'
page_id: '454453125'
product: rm
source: tdn-rm
title: 4827819 EDUCACIONAL01-8146 DT Processo Seletivo Terceirizado
type: documentation
url: https://tdn.totvs.com/display/LRM/4827819+EDUCACIONAL01-8146+DT+Processo+Seletivo+Terceirizado
version: 1
---

# PROCESSO SELETIVO TERCEIRIZADO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Totvs Educacional |
| **Função:** | Processo Seletivo Terceirizado |
| **Situação/Requisito:** | Ao realizar a matricula de um candidato, que já possui registro no educacional em períodos anteriores, via processo seletivo terceirizado ocorre o erro "Referência de objeto não definida para uma instância de um objeto." |
| **Solução/Implementação:** | A rotina de processo seletivo terceirizado foi alterada para verificar se é necessário alterar as tabelas SALUNOMEC, SALUNOCOMPL e VFILIACAO. Dessa forma o sistema não tenta atualizar tabelas que não estão preparadas para isso. O que acabaria gerando erro. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
