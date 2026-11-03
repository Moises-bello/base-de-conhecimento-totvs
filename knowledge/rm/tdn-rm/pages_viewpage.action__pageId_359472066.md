---
content_hash: 8eefe4816cb47bf17689cc24c1eb5b1948400b2cdb551c0c1921b5cd5dd273d2
fetched_at: '2026-06-29T00:08:58.111585+00:00'
page_id: '359472066'
product: rm
source: tdn-rm
title: 2711889 FISCAL01-4492 DT envio de NF-e informações de PIS e COFINS CST 01
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=359472066
version: 2
---

# Envio de NF-e informações de PIS e COFINS CST 01

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Totvs Gestão Fiscal |
| **Função:** | Envio de NF-e |
| **Situação/Requisito:** | Ao enviar uma NF-e onde o calculo do tributo é menor que 2 casas decimais após a virgula, ou seja representam valor menor que zero é apresentado a seguinte mensagem de inconsistência:  Não foi possível enviar a nota.  Enviar NF-e: Erro no envio da NF-e.  TSS - Erro na validação desta nota.  Motivo:Campo: PISAliq': O seguinte campo do Layout era esperado e não foi preenchido: vPIS . Campo: COFINSAliq': O seguinte campo do Layout era esperado e não foi preenchido: vCOFINS .  Mensagem Original:  Element '  {<http://www.portalfiscal.inf.br/nfe>}  PISAliq': Missing child element(s). Expected is (  {<http://www.portalfiscal.inf.br/nfe>}  vPIS ). Element '  {<http://www.portalfiscal.inf.br/nfe>}  COFINSAliq': Missing child element(s). Expected is (  {<http://www.portalfiscal.inf.br/nfe>}  vCOFINS ).  Identificador do Movimento: 6941, Chave de Acesso: 31180408444204000123550928977897891999830599 |
| **Solução/Implementação:** | Alteração no preenchimento das tags vPIS e vCofins para os CSTs 01 e 02 para que as mesmas sejam geradas mesmo que com o seu preenchimento zerado. |
