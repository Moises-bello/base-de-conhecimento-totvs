---
content_hash: 77f12413f641ca7445be7c1a2faaeb99aab2cfedd52fbcbebd7f7c0d15d01365
fetched_at: '2026-06-29T00:06:19.311816+00:00'
page_id: '219696228'
product: rm
source: tdn-rm
title: TTTNKE_DT_Erro_Campo_Nulo_Diferenca_Salarial
type: documentation
url: https://tdn.totvs.com/display/LRM/TTTNKE_DT_Erro_Campo_Nulo_Diferenca_Salarial
version: 1
---

# ERRO DE PARAMETROS NULOS NA DIFERENÇA SALARIAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Diferença Salarial* |
| **Situação/Requisito:** | *Cálculo da Diferença salarial por dissídio apresentando mensagem: Valor não pode ser nulo. Nome do parâmetro: key* |
| **Solução/Implementação:** | *O erro ocorria quando os novos parâmetros da pasta Folha Normal/Dissidio, do Parametrizador, não foram criados.*  *Foi ajustado no processo da Diferença Salarial, para verificar se os novos parâmetros de evento com CC 69 estão nulos.* |
| **Chamados   relacionados:** | *TTTNKE* |
| **Versões/Release:** | *11.82.42* |
