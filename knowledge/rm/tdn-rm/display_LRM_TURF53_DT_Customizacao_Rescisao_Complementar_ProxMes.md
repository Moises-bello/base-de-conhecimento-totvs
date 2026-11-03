---
content_hash: 4fe9960db02b18974dd4de8519edd51f97ed2ca3734befcad2f96b4624a4ef7c
fetched_at: '2026-06-29T00:08:05.559186+00:00'
page_id: '235597844'
product: rm
source: tdn-rm
title: TURF53_DT_Customizacao_Rescisao_Complementar_ProxMes
type: documentation
url: https://tdn.totvs.com/display/LRM/TURF53_DT_Customizacao_Rescisao_Complementar_ProxMes
version: 2
---

# CUSTOMIZAÇÃO PARA RESCISÃO COMPLEMENTAR DO PRÓXIMO MÊS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão Complementar* |
| **Situação/Requisito:** | *Conforme necessidade de lançar eventos da rescisão complementar na próxima competência através de customização, foram criadas duas propriedades na classe ParametrosExecucaoBase.*  *Uma flag para controlar se o processo da rescisão complementar deve ou não ser considerado para o próximo mês e uma propriedade inteira para o valor do período.*  *Será utilizado o entry point já existente na classe CalculoServer (CustomCalculoPre) onde é enviado o clone do objeto parametrosExecucao para a customização.* |
| **Solução/Implementação:** | *Foram criadas as duas propriedades abaixo:*  *ParametrosExecucao.CustomRescComplementarProximoMes -> Booleano. Se true irá alterar o ambiente do processo para a competência seguinte, se false, seguirá o fluxo padrão, considerando o ambiente da competência atual.*  *ParametrosExecucao.CustomRescComplementarPeriodoProxMes -> Int. Será verificado somente se o parâmetro anterior for true. Neste caso, será considerado como o período local da competência seguinte.* |
| **Chamados   relacionados:** | *TURF53, TUUAOJ* |
| **Versões/Release:** | *12.1.11* |
