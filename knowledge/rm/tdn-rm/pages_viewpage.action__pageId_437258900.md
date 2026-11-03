---
content_hash: 9a837317b03ff0fd0623722a67e681fb55019927cd77bcbb72153a929a4a0f9f
fetched_at: '2026-06-29T00:09:51.664434+00:00'
page_id: '437258900'
product: rm
source: tdn-rm
title: DEDUANALYTICS-674 DT Parametrização de Alunos Egresso do Ensino Básico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=437258900
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | TOTVS Educacional. |
| **Módulo:** | Educacional. |
| **Função:** | Parâmetro Alunos Ativos e Alunos Egressos do Ensino Básico. |
| **Situação/Requisito:** | O parametrizador não permite que um status configurado para aluno ativo seja configurado para aluno egresso do ensino básico. Essa situação é possível pois o status sozinho não define se o aluno formou, para isso, deve ser verificado se a série está configurada como última série do ensino básico da instituição de ensino. |
| **Solução/Implementação:** | Retirado a trava do parametrizador que não permitia a configuração do mesmo status para alunos ativos e alunos egresso do ensino básico. Foi alterado também a consulta de extração da fato de alunos do ensino básico para classificar o aluno como ativo ou egresso de acordo com o status e a série. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |
| **Documento de Referência:** | N/A. |
| **Pacote:** | N/A |
