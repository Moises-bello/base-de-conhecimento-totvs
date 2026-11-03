---
content_hash: 3f4207a18c09cf2fc7e8a35a7f8b5b3cd20ce7698b64d5f29042f4fca8af0ccb
fetched_at: '2026-06-29T00:11:53.720512+00:00'
page_id: '850707319'
product: rm
source: tdn-rm
title: DT - Múltiplos Vínculos - Exclusão de dados na Tabela PFPRECISARECALCULOMV
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=850707319
version: 14
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Múltiplos Vínculos - Exclusão de dados na Tabela PFPRECISARECALCULOMV |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-6947](https://jiraproducao.totvs.com.br/browse/DRHROTRM-6947) |

## **02.** **RELEASES**

* 12.1.2402.171
* 12.1.2406.103 e superiores

## **03.****SITUAÇÃO/REQUISITO**

Atualmente, no produto, ao liberar a competência, é apresentada uma mensagem de aviso sobre a pendência de recálculo nos múltiplos vínculos, e a tabela PFPRECISARECALCULOMV é alimentada. Devido a essa tratativa, caso um dos vínculos esteja em uma coligada que já tenha liberado a competência, o sistema impossibilita a geração do XML. O produto bloqueia a geração devido ao registro na tabela PFPRECISARECALCULOMV.

## **04.****SOLUÇÃO**

É inviável modificarmos o tratamento de erros na geração do XML do evento devido às implicações no eSocial, especialmente em casos de pendências de recálculo de múltiplos vínculos, pois isso poderia causar problemas no eSocial. Diante disso, disponibilizamos no produto a possibilidade de excluir o registro na tabela PFPRECISARECALCULOMV.

Lembramos que avisos de alerta serão emitidos, e as consequências dessa exclusão serão de responsabilidade do usuário analisar se haverá consequências no eSocial.

**IMPLEMENTAÇÃO**

1) No menu Configurações | Parametrizador | eSocial | Configurações 4/7 foi disponibilizado o parâmetro "**Permite excluir Múltiplos Vínculos que Necessitam de Recálculo**". Ao marcar esse parâmetro será apresentada a seguinte mensagem de alerta: 

      

2) No menu Folha Mensal l Consulta l Múltiplos Vínculos que Necessitam de Recálculo foi criado o ícone que possibilita a exclusão do registro. 

Ao clicar em "Excluir" será apresentada novamente a mensagem de alerta:
