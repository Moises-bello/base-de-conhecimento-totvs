---
content_hash: f96d67ac0749290255b6e16aba2c4a319d1323598922ae1a5c371daf92704625
fetched_at: '2026-06-29T00:08:11.489289+00:00'
page_id: '243010550'
product: rm
source: tdn-rm
title: TVCXFX_DT_CALCMEDDATA_Periodo_Vencido_Ferias_Prop
type: documentation
url: https://tdn.totvs.com/display/LRM/TVCXFX_DT_CALCMEDDATA_Periodo_Vencido_Ferias_Prop
version: 2
---

# CALCMEDDATA RETORNA ERRO NA RESCISÃO QUANDO CONSIDERA PERIODO VENCIDO E O CÁLCULO É DE FÉRIAS PROPORCIONAIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Fórmula* |
| **Situação/Requisito:** | *Na função de fórmula CALCMEDDATA utilizada na rescisão, quando considera periodo de férias vencidas em um cálculo de férias proporcionais, ocorre erro caso o funcionário não possua férias vencidas.* |
| **Solução/Implementação:** | *Ajuste no cálculo da função de fórmula CALCMEDDATA para tratar o caso de solicitar o periodo vencido para um cálculo de férias proporcionais.* |
| **Chamados   relacionados:** | *TVCXFX, TVDVX6* |
| **Versões/Release:** | *11.82.45, 12.1.12* |
