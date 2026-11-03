---
content_hash: f9435025ff2ca90030c3a3d806f2eaf1e5a3c0922c16d952dc488729b6e074d6
fetched_at: '2026-06-29T00:06:16.135139+00:00'
page_id: '211063305'
product: rm
source: tdn-rm
title: TTOCZP_DT_1aParcela13o_Considerando_Salario_Mes_Anterior
type: documentation
url: https://tdn.totvs.com/display/LRM/TTOCZP_DT_1aParcela13o_Considerando_Salario_Mes_Anterior
version: 1
---

# PARÂMETRO PARA CONSIDERAR SALÁRIO ATUAL NA 1a.PARCELA DE 13o.

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Décimo Terceiro* |
| **Situação/Requisito:** | *Quando o parâmetro “Utiliza salário atual p/ 1ª. Parcela” está desmarcado, no Parametrizador, pasta 13º Salário, o cálculo do evento de CC 9, 1a.Parcela de 13o., deve considerar o salário vigente no mês anterior.*  *No módulo específico de 13o., o lançamento da 1a. parcela está considerando o valor correto.*  *Entretanto, no recálculo do envelope, o evento de CC 9 está sendo recalculado considerando o salário atual do funcionário.* |
| **Solução/Implementação:** | *Ajuste no código de cálculo 9, 1a. Parcela de 13o. Salário, para sempre verificar o parâmetro “Utiliza salário atual p/ 1ª. Parcela”, no Parametrizador, pasta 13º Salário. Independente de o processamento estar sendo feito no módulo específico ou através do recálculo da folha.*  *Caso o parâmetro esteja desmarcado, o cálculo do evento de CC 9 sempre deve considerar o salário vigente no mês anterior.* |
| **Chamados   relacionados:** | *TTOCZP* |
| **Versões/Release:** | *11.82.42* |
