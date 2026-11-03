---
content_hash: 07c86ab67759c0a5bd413e51a53b7b2584afedf3e69c69b57a571aca7bc21b47
fetched_at: '2026-07-02T19:24:19.831616+00:00'
page_id: '244436867'
product: protheus
source: tdn-tec
title: Implementação - Possibilidade de gerar um documento PDF protegido por senha
  através da File2Printer.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244436867
version: 3
---

Implementação - Nova funcionalidade no agente de impressão TOTVS Printer onde através da função File2Printer é possível gerar um PDF protegido por senha.

|  |  |
| --- | --- |
| Situação | Não havia modos de gerar um PDF protegido por senha através do comando File2Printer. |
| Ocorrência | Necessidade de proteger com senha um documento PDF gerado através do comando File2Printer. |
| Implementação | Foi criada a nova fila de impressão PDF\_WITH\_PASSWORD (e a fila PDF\_WITHOUT\_FONTS\_WITH\_PASSWORD para compatibilidade) que permite especificar ao agente de impressão TOTVS Printer que o documento PDF a ser gerado deverá ser protegido por senha. Além disso dois novos parâmetros onde são especificadas as senhas foram incluídos na função File2Printer. |
| Informações adicionais | * Referente à ocorrência: TEC-5897 * Disponível a partir da build 7.00.131227A com data de geração superior a 08/08/2014. * Disponível a partir da versão 1.5.3 da TOTVS Printer. * Para mais detalhes consulte a documentação da  no TDN. * **IMPORTANTE: Houve mudança na ordem dos parâmetros da função File2Printer após esta implementação, a saber:**   1. Builds 7.00.131227A com data de geração entre 08/08/2014 e 16/02/2016 respeitam a seguinte ordem: file2Printer(cArquivo, cFila, cRFS, nSize, cUserPwd, cOwnerPwd, lChangeCase)   2. Builds 7.00.131227A com data de geração superior a 17/02/2016 respeitam a seguinte ordem: file2Printer(cArquivo, cFila, cRFS, nSize, lChangeCase, cUserPwd, cOwnerPwd) |
