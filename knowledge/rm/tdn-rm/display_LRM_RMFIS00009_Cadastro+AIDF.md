---
content_hash: f6940b24648de9fa005b41dea4943adca3d55895dbe445f6329f20bd4a8362e1
fetched_at: '2026-06-29T00:08:43.737276+00:00'
page_id: '305929616'
product: rm
source: tdn-rm
title: RMFIS00009_Cadastro AIDF
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00009_Cadastro+AIDF
version: 5
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | Totvs Gestão Fiscal |
| **Versões:** | 12.x |
| **Ocorrência:** | Cadastro AIDF |
| **Ambiente:** |  |
| **Passo a passo:** | Para cadastrar o Número da AIDF (Autorização para impressão dos Documentos Fiscais) vá no Totvs Gestão Fiscal em Cadastro | Mais ...| AIDF.        **Aba Identificação**      **Número da Autorização**    Este número se refere à autorização adquirida pela Empresa para emitir Documentos de Tipos diferentes.    **Observação:** Ao excluir uma AIDF, o sistema verificará se existem Lançamentos, Dispositivos Extraviados ou Movimentos no RM Nucleus (se RM Liber for integrado ao RM Nucleus) associado a esta AIDF. Caso exista, o registro não poderá ser excluído.      **Itens AIDF**        Em Anexos | Itens AIDF será possível cadastrar Itens AIDF. Para um mesmo número de AIDF será possível cadastrar diferentes Itens. Sendo que cada item refere-se a uma faixa de notas para determinada Série e Espécie de Documento.  O sistema não permitirá a alteração da faixa de Documentos Inicial e Final de AIDF quando o numero da AIDF já está associado a um Lançamento Fiscal e seus documentos estão listados na pasta Dispositiva de Segurança.  O campo Série terá 4 posições.  Caso o Lançamento Fiscal possua o campo Série preenchido com o valor "----" deverá ser informado no campo Série ltem AIDF o valor "----".    **Atenção:** Não será permitido cadastrar dois itens de uma AIDF com a mesma Série e Espécie. Não será possível vincular uma AIDF ao Lançamento Fiscal cujo Item com a mesma Série e Espécie do lançamento foi cancelado em data anterior ou igual a Data do Lançamento Fiscal. |
| **Observações:** |  |
