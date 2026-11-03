---
content_hash: 69cdef944f01eb9ac40d9dfcf4c12dadc5c57f6f819a3c7e98d6201497b327d4
fetched_at: '2026-06-29T00:09:07.799685+00:00'
page_id: '385849661'
product: rm
source: tdn-rm
title: 3421024 FISCAL01-5792 DT Encerramento Contribuição Previdenciária Outras Atividades
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=385849661
version: 1
---

**Apurar Imposto Contribuição Previdenciária**

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Apurar Imposto Contribuição Previdenciária |
| **Situação/Requisito:** | Ao realizar a transmissão do evento R-2060 para o governo o mesmo retornou como rejeitado com a seguinte mensagem:  <regOcorrs>  <tpOcorr>1</tpOcorr>  <localErroAviso> - Campo: codAtivEcon - XPATH: /Reinf/evtCPRB/infoCPRB/ideEstab/tipoCod/codAtivEcon</localErroAviso>  <codResp>MS1106</codResp>  <dscResp>O código da atividade econômica informado deve ser um código válido da tabela 9</dscResp>  </regOcorrs> |
| **Solução/Implementação:** | No encerramento do período de apuração do tributo contribuição previdenciária e quando é gerado o registro de  Outras Receitas com a diferença do faturamento no código de atividade será informado o código conforme regra abaixo:  Preenchimento do Código da Atividade:  Se Alíquota igual a 1% Então "99990010" Senão Se Alíquota igual a 1.5% Então "99990015"  Senão Se Alíquota igual a 2.5% Então "99990025"  Senão Se Alíquota igual a 3% Então "99990030"  Senão Se Alíquota igual a 4.5% Então "99990045"  Senão "99999999". |
| **Requisito:** | FIS000407 |
