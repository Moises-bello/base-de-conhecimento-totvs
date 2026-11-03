---
content_hash: c66e0cf556e648c03952b18b4e623649ad600614513b7d5fb38655e333bf6ab0
fetched_at: '2026-06-29T00:09:54.892198+00:00'
page_id: '445655905'
product: rm
source: tdn-rm
title: 4616297 - DEDUINTEGRACOES-3973 - Alteração de plano de pagamento de contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=445655905
version: 1
---

# ALTERAÇÃO DE PLANO DE PAGAMENTO DE CONTRATO - PROCESSO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Alteração de plano de pagamento de contrato |
| **Situação/Requisito:** | Parcelas do contrato não são atualizadas quando executamos o processo de alteração de plano de pagamento para o mesmo plano de pagamento do contrato. |
| **Solução/Implementação:** | Ajuste para que o processo de alteração de plano de pagamento altere as parcelas de um contrato mesmo que o plano de pagamento selecionado seja o mesmo do contrato em questão. Ajustes no status do processo que sempre mostrava com sucesso mesmo que alguma validação tivesse sido feita. A partir de agora o status será setado da seguinte forma: - Se todos os contratos não tiveram o plano de pagamento alterado, ERRO - Se todos os contratos tiveram o plano de pagamento alterado, SUCESSO - Se alguns contratos não tiveram o plano de pagamento alterado e outros foram processados com sucesso, ADVERTÊNCIA.    **OBSERVAÇÃO**: Somente serão listados os contratos processados caso todos tenham sido processados sem erro, senão, serão listados somente os contratos com erro a fim de não poluir muito o log de processamento. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | Informe o [linkdopacote] |
