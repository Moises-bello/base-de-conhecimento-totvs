---
content_hash: da8698e152c7ba0e7da32e9780cd97533344a785fb26626a21437067404b7231
fetched_at: '2026-07-02T19:24:18.828256+00:00'
page_id: '221549743'
product: protheus
source: tdn-tec
title: Componente TPaintPanel não move os shapes com códigos iguais no método SetPosition
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=221549743
version: 1
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

|  |  |
| --- | --- |
| Situação | Componente TPaintPanel não move os shapes com códigos iguais no método SetPosition |
| Ocorrência | Adicionar shapes com o mesmo código, ao utilizar o método SetPosition, apenas um dos shapes era movido.  Exemplo:  oPanel:AddShape("id=1;type=3;left=15;top=15;width=50;height=20;gradient=1,0,0,0,0,0.0,#EF8F8F;pen-width=1;pen-color=#FF00FF;can-move=1;can-mark=0;is-blinker=1;")  oPanel:AddShape("id=1;type=7;pen-width=1;font=arial,14,0,0,1;left=15;top=45;width=50;height=20;text=Texto 1;gradient=0,0,0,0,0,0,#000000;can-move=1;")  oPanel:AddShape("id=1;type=7;pen-width=1;font=arial,14,0,0,1;left=15;top=65;width=50;height=20;text=Texto 2;gradient=0,0,0,0,0,0,#000000;can-move=1;")    oPanel:SetPosition(1,50,50) |
| Correção | Corrigido o posicionamento de todos os shapes com o mesmo código quando utlizado o SetPosition |
| Informações adicionais | * Referente ao chamado: não há chamado associado. * Referente à ocorrência: [SCHTML-292](http://jira.totvs.com/browse/SCHTML-292 "View this issue in JIRA") * Disponível a partir da build 7.00.131227A - 2.2.23 |
