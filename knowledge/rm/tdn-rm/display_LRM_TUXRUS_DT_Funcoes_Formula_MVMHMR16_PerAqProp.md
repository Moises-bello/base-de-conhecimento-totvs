---
content_hash: 631b942f73a78e60004fa6bb7b844e5ff005c28b411abf0b6a3ec0103df132cd
fetched_at: '2026-06-29T00:08:09.029508+00:00'
page_id: '239020321'
product: rm
source: tdn-rm
title: TUXRUS_DT_Funcoes_Formula_MVMHMR16_PerAqProp
type: documentation
url: https://tdn.totvs.com/display/LRM/TUXRUS_DT_Funcoes_Formula_MVMHMR16_PerAqProp
version: 1
---

# FUNÇÕES MV, MH E MR COM OPÇÃO 16 VERIFICAR PERIODO AQUISITIVO PROPORCIONAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Fórmula* |
| **Situação/Requisito:** | *Quando são utilizadas as funções de fórmula MV, MH ou MR no cálculo de rescisão, passando como parâmetro a opção 16, periodo aquisitivo, não está tratando se a referência é o periodo proporcional ou o periodo vencido.* |
| **Solução/Implementação:** | *Ajuste nas funções de fórmula MV, MH ou MR, quando chamadas do cálculo de rescisão, passando como parâmetro a opção 16, para verificar se a execução é no evento de CC 25, Férias Proporcionais, e assim considerar o periodo aquisitivo proporcional.* |
| **Chamados   relacionados:** | *TUXRUS* |
| **Versões/Release:** | *12.1.12* |
