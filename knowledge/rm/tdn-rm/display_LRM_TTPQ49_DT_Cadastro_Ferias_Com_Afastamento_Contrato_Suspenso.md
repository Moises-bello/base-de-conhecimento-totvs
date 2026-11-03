---
content_hash: ef22f0483fbd0d85188a27c626fbae2a3e5487054111f1bbdd75756bc4c0d02b
fetched_at: '2026-06-29T00:06:16.776615+00:00'
page_id: '212899556'
product: rm
source: tdn-rm
title: TTPQ49_DT_Cadastro_Ferias_Com_Afastamento_Contrato_Suspenso
type: documentation
url: https://tdn.totvs.com/display/LRM/TTPQ49_DT_Cadastro_Ferias_Com_Afastamento_Contrato_Suspenso
version: 1
---

# DIAS A MARCAR NO CADASTRO DE FÉRIAS QUANDO EXISTE PERIODO DE CONTRATO SUSPENSO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cadastro de Férias* |
| **Situação/Requisito:** | *Quando funcionário tem afastamento tipo C - Contrato Suspenso, onde o período aquisitivo é estendido no número de dias de afastamento, no cadastro deste período aquisitivo está demonstrando um número incorreto no campo "Dias de férias a marcar".*  *Nesta mesma situação, o processo de Finalizar Férias, não está abrindo um novo período aquisitivo, quando é zerado o saldo do funcionário.* |
| **Solução/Implementação:** | *Ajuste na contagem do campo "Dias de férias a marcar" no cadastro de período aquisitivo, para considerar a extensão do período no número de dias de afastamento.*  *E ajuste no processo de Finalizar Férias, quando funcionário tem afastamento tipo C - Contrato Suspenso, onde o período aquisitivo é estendido no número de dias de afastamento.* |
| **Chamados   relacionados:** | *TTPQ49* |
| **Versões/Release:** | *12.1.9* |
