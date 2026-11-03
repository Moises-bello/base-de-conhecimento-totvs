---
content_hash: ba21d7fce84b5e587076beb1bf3d1d735bc1cc98df375e4b99fcc7b6db4141b7
fetched_at: '2026-06-29T00:06:27.499978+00:00'
page_id: '232823566'
product: rm
source: tdn-rm
title: TUHZMO_DT_Finaliza_Ferias_Gerenciador_Movimento_Rateio_CCusto
type: documentation
url: https://tdn.totvs.com/display/LRM/TUHZMO_DT_Finaliza_Ferias_Gerenciador_Movimento_Rateio_CCusto
version: 2
---

# FINALIZA FÉRIAS COM GERENCIADOR DE MOVIMENTO NÃO PODE EXECUTAR O RATEIO POR CENTRO DE CUSTO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Finaliza Férias* |
| **Situação/Requisito:** | *No processo para Finalizar Férias, quando é utilizado o Gerenciador de Movimento, está executando o rateio por centro de custo de forma incorreta.*  *Neste processo, o rateio só deve ser executado no lançamento do Gerenciador de Movimento para o envelope do funcionário.* |
| **Solução/Implementação:** | *Ajuste no módulo de Finalizar Férias para que, quando estiver sendo utilizado Gerenciador de Movimento, não executar o rateio por centro de custo.*  *Neste caso, o campo Centro de Custo do Gerenciador deverá ficar em branco.* |
| **Chamados   relacionados:** | *TUHZMO, TUJOAE* |
| **Versões/Release:** | *11.82.43, 12.1.10* |
