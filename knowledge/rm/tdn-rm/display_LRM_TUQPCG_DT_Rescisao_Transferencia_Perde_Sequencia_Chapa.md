---
content_hash: b3e7905647c14acc38f6b2d16628d73d383722e1e5f9c4b3ed1bb92f6a3d69f3
fetched_at: '2026-06-29T00:08:08.442227+00:00'
page_id: '238036284'
product: rm
source: tdn-rm
title: TUQPCG_DT_Rescisao_Transferencia_Perde_Sequencia_Chapa
type: documentation
url: https://tdn.totvs.com/display/LRM/TUQPCG_DT_Rescisao_Transferencia_Perde_Sequencia_Chapa
version: 2
---

# RESCISÃO POR TRANSFERÊNCIA PERDE SEQUENCIA NA GERAÇÃO AUTOMÁTICA DE CHAPA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão por Transferência* |
| **Situação/Requisito:** | *Quando está marcado o parâmetro para "Cadastro automático de chapas seqüenciais", na Rescisão por Transferência do cadastro individual está gerando a nova chapa na tela do processo.*  *Com isto, caso a execução seja cancelada antes do processamento da transferência, está sendo incrementado o valor na tabela GAUTOINC, e assim perdendo a sequencia correta.*  *Ao tentar acessar novamente a tela da rescisão é apresentado o próximo registro.* |
| **Solução/Implementação:** | *Tratar na Rescisão por Transferência do cadastro individual para ter o mesmo comportamento da Rescisão Coletiva, onde a geração da nova chapa ocorre durante o processamento, e assim possibilita um controle através de Transação.*  *Caso a execução seja cancelada, a GAUTOINC permanecerá inalterada.* |
| **Chamados   relacionados:** | *TUQPCG, TUZUGS* |
| **Versões/Release:** | *11.82.44, 12.1.12* |
