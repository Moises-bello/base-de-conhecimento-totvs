---
content_hash: 2dde97ca95106057e16e6d467abedc5f5371b7b9d49823bc148303d4d2dd2d16
fetched_at: '2026-06-29T00:06:02.850091+00:00'
page_id: '198949441'
product: rm
source: tdn-rm
title: TSWQUL_DT_Cadastro_De_Medias_Nos_Sindicatos
type: documentation
url: https://tdn.totvs.com/display/LRM/TSWQUL_DT_Cadastro_De_Medias_Nos_Sindicatos
version: 1
---

# CADASTRO DE SINDICATOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cadastro de Médias nos Sindicatos* |
| **Situação/Requisito:** | *Ao tentar editar as médias de alguns sindicatos, o sistema bloqueava as telas pois os respectivos registros não exisitiam mais no banco de dados.* |
| **Solução/Implementação:** | *Foi aidicionada a chamada à uma função que trata os casos em que os registros de médias não existem mais, inserindo um registro em branco para permitir a edição pelo usuário* |
| **Chamados relacionados:** | *TSWQUL* |
| **Versões/Release:** | *11.82.41* |
