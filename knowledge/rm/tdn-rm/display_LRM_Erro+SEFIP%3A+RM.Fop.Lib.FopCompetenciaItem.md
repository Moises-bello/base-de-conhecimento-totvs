---
content_hash: 2d0c8ef8f0ddea3819e0a018609576e260d4d6a5e0c1e065607136dc0992074c
fetched_at: '2026-06-29T00:05:56.006277+00:00'
page_id: '149881215'
product: rm
source: tdn-rm
title: 'Erro SEFIP: RM.Fop.Lib.FopCompetenciaItem'
type: documentation
url: https://tdn.totvs.com/display/LRM/Erro+SEFIP%3A+RM.Fop.Lib.FopCompetenciaItem
version: 1
---

| Produto | **RM** |
| --- | --- |
| **Sintoma** | **Ao gerar SEFIP retroativo não aparece nenhuma coliga para selecionar e o sistema apresenta a seguinte mensagem:**  ****“Não foram encontradas coligadas para a competência RM.Fop.Lib.FopCompetenciaItem verifique os parâmetros de recolhimento. ”**** |
| Solução | **O erro ocorre porque as movimentações não estão na ficha financeira do funcionário. Para corrigi-lo realize o procedimento abaixo:**    **Acessar o menu Rotinas | Restauração da ficha Financeira Complementar restaurar a ficha com a data que deseja gerar o arquivo SEFIP, exemplo:**  **Competência inicial 01/2010**  **Competência final 12/2011**    **Gere a SEFIP novamente.**   **OBS: Ao liberar a competência as informações retornarão automaticamente para a Ficha Financeira Complementar.** |
