---
content_hash: dcfd9cce1f8b84316f845eb17e06a96567f024a4ab2487e153445a2384d1902c
fetched_at: '2026-06-29T00:06:13.009954+00:00'
page_id: '207357128'
product: rm
source: tdn-rm
title: TTJHPL_DT_Plano_De_Aula
type: documentation
url: https://tdn.totvs.com/display/LRM/TTJHPL_DT_Plano_De_Aula
version: 1
---

# PLANO DE AULA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Função:** | *Plano de Aula* |
| **Situação/Requisito:** | *Depois de atualizado o sistema para a nova versão, está ocorrendo o erro para os conteúdos que já foram digitados maiores que 2000 caracteres, antes da atualização da versão, para quem tentar digitar agora o conteúdo com mais de 2000 caracteres ele está validando e não salva, o que está correto, porém para os que já foram digitados está ocorrendo esse erro.* |
| **Solução/Implementação:** | *Remoção do limite de 2000 no data props dos campos CONTEUDO e CONTEUDOEFETIVO da tabela SPLANOAULA, tal validação não é necessário, pois os campos são TEXT no Sql Server e CLOB e LONG no Oracle.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.41 e 11.82.42* |
