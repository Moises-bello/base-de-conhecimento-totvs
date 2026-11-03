---
content_hash: 8443c38fd5aeb4b25850aec415a16c4f305fce8f0062e154a1b1d8cfd8196669
fetched_at: '2026-06-29T00:06:11.370957+00:00'
page_id: '203768416'
product: rm
source: tdn-rm
title: TTDX01_DT_Transfere_Ferias_Programadas_Altera_Chapa_Demitido
type: documentation
url: https://tdn.totvs.com/display/LRM/TTDX01_DT_Transfere_Ferias_Programadas_Altera_Chapa_Demitido
version: 1
---

# TRANSFERÊNCIA DE FÉRIAS PROGRAMADAS QUANDO ALTERA CHAPA DO DEMITIDO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cálculo de Rescisão* |
| **Situação/Requisito:** | *Ao fazer a transferência de um funcionário sem ônus (tipo 5), com o parâmetro desmarcado para transferir férias programadas e alterando a chapa do funcionário demitido, as férias programadas são transferidas, ficando o período de gozo marcado com o funcionário ativo.*  *Caso o usuário não marque o parâmetro para alterar a chapa do funcionário demitido, as férias programadas continua com o funcionário demitido.* |
| **Solução/Implementação:** | *Ajuste no processo de transferência para que, no caso de não transferir férias programadas e alterar a chapa do demitido, o período de gozo marcado fique no funcionário demitido, ou seja, na nova chapa.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTDX01* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |
