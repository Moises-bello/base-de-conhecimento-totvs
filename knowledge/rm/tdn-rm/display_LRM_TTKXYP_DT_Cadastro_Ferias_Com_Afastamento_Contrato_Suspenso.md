---
content_hash: bd4c13c5b56e292e9f51e7e50b9b5f95252612c73ff25d034e8e67fa50b2ba9a
fetched_at: '2026-06-29T00:06:16.772875+00:00'
page_id: '212899552'
product: rm
source: tdn-rm
title: TTKXYP_DT_Cadastro_Ferias_Com_Afastamento_Contrato_Suspenso
type: documentation
url: https://tdn.totvs.com/display/LRM/TTKXYP_DT_Cadastro_Ferias_Com_Afastamento_Contrato_Suspenso
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
| **Chamados   relacionados:** | *TTKXYP* |
| **Versões/Release:** | *11.82.42* |
