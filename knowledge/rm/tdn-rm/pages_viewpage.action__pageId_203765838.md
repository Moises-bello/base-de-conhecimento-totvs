---
content_hash: 6236859fc2a7a9a6438a615cb4bf64139902937315e775bf7d1bcc4a384592d1
fetched_at: '2026-06-29T00:06:10.642295+00:00'
page_id: '203765838'
product: rm
source: tdn-rm
title: TTICGX _DT_Regerar_Lançamento_Valor_Liquido_Zerado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=203765838
version: 1
---

# Mudança de turma

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão**Educacional* |
| **Função:** | *Gerar lançamento.* |
| **Situação/Requisito:** | *Ao regerar lançamento contendo 10% de desconto mais 90% de bolsa, o sistema calcula o valor do líquido negativo e emite mensagem “Lançamento não atualizado. Valor líquido menor que 0”. Somente ocorria com valor de parcela igual à um número impar.* |
| **Solução/Implementação:** | *Alterado o processo de geração de lançamento para permitir regerar lançamento quando o valor total de descontos seja maior que o valor da parcela, nesta situação o valor do liquido deverá ficar zero. Caso esteja configurado nos parâmetros do Educacional para baixar automático, o lançamento com valor liquido igual a zero deverá ser regerado com status Baixado.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *12.1.8* |
