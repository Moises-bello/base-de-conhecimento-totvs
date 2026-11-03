---
content_hash: e98c10c7acb94902bad64dd5f803a23881bfdf3df8de34cb2fcb42a871b6b0eb
fetched_at: '2026-06-29T00:08:04.001002+00:00'
page_id: '235332951'
product: rm
source: tdn-rm
title: TULFGS_DT_Provisao_Ferias_Prop_Permite_Valor_Negtivo
type: documentation
url: https://tdn.totvs.com/display/LRM/TULFGS_DT_Provisao_Ferias_Prop_Permite_Valor_Negtivo
version: 1
---

# PROVISÃO DE FÉRIAS PROPORCIONAIS NÃO CONSIDERA PARAMETRO PERMITE VALOR NEGATIVO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Provisão de Férias* |
| **Situação/Requisito:** | *Na Geração do Histórico de Provisões, quando somente as férias proporcionais retornam valor negativo, não está considerando os parâmetros "Permite valor negativos" e "Permite avos negativos".*  *Mesmo estando desmarcados, está abatendo o valor negativo das férias proporcionais no valor total da provisão.* |
| **Solução/Implementação:** | *Ajuste na Geração do Histórico de Provisões para verificar os parâmetros "Permite valor negativos" e "Permite avos negativos", mesmo quando somente as férias proporcionais retornarem valor negativo.* |
| **Chamados   relacionados:** | *TULFGS* |
| **Versões/Release:** | *11.82.43, 12.1.11* |
