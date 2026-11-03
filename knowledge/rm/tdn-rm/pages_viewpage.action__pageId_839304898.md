---
content_hash: 4acb55a94f4e4de935e85412770c5c18c87411d4bbccec65777356f50f8dd8a2
fetched_at: '2026-06-29T00:11:50.253431+00:00'
page_id: '839304898'
product: rm
source: tdn-rm
title: DT - Férias Individuais - Validação de dias de gozo de férias e regras de inicio
  de férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=839304898
version: 6
---

## **01. DADOS GERAIS**

| Produto: | TOTVS - Folha de Pagamento |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Validação de dias de gozo de férias e regras de inicio de férias |
| País: | Brasil |
| Epic | [DRHCALCRM-5789](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-5789) |

## **02. SITUAÇÃO/REQUISITO**

Com as alterações provenientes da Reforma Trabalhista de acordo com a Lei nº 13.467 de 13 Julho de 2017, o colaborador poderá flexibilizar as férias em até **3**(**três)**períodos de gozo, sendo que nenhum deles pode ser menor que **5 (cinco)** dias e pelo menos deve existir um período com **14 (quatorze)** dias ou mais de gozo. Além disso, as férias não podem iniciar em dias descanso e/ou feriado ou até dois dias antes deste.

No portal já é feita esta validação não permitindo que o colaborador solicite férias que não atenda esta regra. Porém no RM.exe é retornando mensagens, mas não é feito nenhum bloqueio.

## **03. SOLUÇÃO**

Foi evoluído o cadastro de férias individuas para validar estas regras mediante a parametrização para comportar a  Lei nº 13.467. Estes parâmetros tem comportamentos únicos e para descrever cada comportamento criamos o FAQ e o Documento Referencia mencionado abaixo explicando e exemplificando suas particularidades

## **04.****ASSUNTOS RELACIONADOS**

* [FAQ](https://tdn.totvs.com/pages/viewpage.action?pageId=838692998)
* [Documentação de Referencia](https://tdn.totvs.com/pages/viewpage.action?pageId=736959073&draft=true)
