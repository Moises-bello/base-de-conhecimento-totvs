---
content_hash: b89cd3c163660c1b839db8ef38a7222ad64d9533747e49234ab71f0918b5193b
fetched_at: '2026-06-29T00:06:15.817770+00:00'
page_id: '211062163'
product: rm
source: tdn-rm
title: TTMMIY_DT_Periodo_CALCMED_Com_Antecipacao_Ferias
type: documentation
url: https://tdn.totvs.com/display/LRM/TTMMIY_DT_Periodo_CALCMED_Com_Antecipacao_Ferias
version: 2
---

# PERIODO CONSIDERADO NA CALCMED QUANDO AS FÉRIAS SÃO ANTECIPADAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Função CALCMED* |
| **Situação/Requisito:** | *Função de fórmula CALCMED está considerando um periodo incorreto quando as férias são antecipadas em poucos dias antes do final do periodo aquisitivo.*  *Mesmo que o funcionário já tenha adquirido o direito aos 12 avos completos, como o periodo aquisitivo ainda não venceu, deve ser passado como parametro na CALCMED o número 5 referente à férias proporcionais.*  *E neste caso, o periodo de apuração das médias no cálculo do recibo de férias não está sendo considerado corretamente.* |
| **Solução/Implementação:** | *Ajuste na função de fórmula CALCMED para buscar corretamente o periodo de apuração das médias do cálculo de férias, quando o período de gozo é iniciado poucos dias antes do final do periodo aquisitivo.*  *Neste caso, a CALCMED deve considerar como periodo de férias proporcionais todos os meses do periodo aquisitivo corrente.* |
| **Chamados  relacionados:** | *TTMMIY* |
| **Versões/Release:** | *11.82.42* |
