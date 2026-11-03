---
content_hash: 1d19d19f7d88719cc93dd259cf321196cbd2fbe08f6d4130d014384066d2d792
fetched_at: '2026-06-29T00:06:16.142379+00:00'
page_id: '211063409'
product: rm
source: tdn-rm
title: TTOSLK_DT_1aParcela13o_Considerando_Salario_Mes_Anterior
type: documentation
url: https://tdn.totvs.com/display/LRM/TTOSLK_DT_1aParcela13o_Considerando_Salario_Mes_Anterior
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
| **Chamados   relacionados:** | *TTOSLK* |
| **Versões/Release:** | *12.1.9* |
