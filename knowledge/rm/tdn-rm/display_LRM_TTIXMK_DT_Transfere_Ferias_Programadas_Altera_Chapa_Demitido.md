---
content_hash: 3c5581a8e52719861cc006be741d5d944f69bb4b98c4513c52e96cd8c5271125
fetched_at: '2026-06-29T00:06:11.382799+00:00'
page_id: '203768634'
product: rm
source: tdn-rm
title: TTIXMK_DT_Transfere_Ferias_Programadas_Altera_Chapa_Demitido
type: documentation
url: https://tdn.totvs.com/display/LRM/TTIXMK_DT_Transfere_Ferias_Programadas_Altera_Chapa_Demitido
version: 4
---

# TRANSFERÊNCIA DE FÉRIAS PROGRAMADAS QUANDO ALTERA CHAPA DO DEMITIDO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cálculo de Rescisão* |
| **Situação/Requisito:** | *Ao fazer a transferência de um funcionário sem ônus (tipo 5), com o parâmetro desmarcado para transferir férias programadas e alterando a chapa do funcionário demitido, as férias programadas são transferidas, ficando o período de gozo marcado com o funcionário ativo.*  *Caso o usuário não marque o parâmetro para alterar a chapa do funcionário demitido, as férias programadas continua com o funcionário demitido.* |
| **Solução/Implementação:** | *Ajuste no processo de transferência para que, no caso de não transferir férias programadas e alterar a chapa do demitido, o período de gozo marcado fique no funcionário demitido, ou seja, na nova chapa.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTIXMK* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
