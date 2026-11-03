---
content_hash: 7b5dc5218b030715274c4ae2679948770a6f6a5b397124c928103b30b4f3697a
fetched_at: '2026-06-29T00:05:53.884381+00:00'
page_id: '1071995018'
product: rm
source: tdn-rm
title: DT - Calcular as férias em dobro quando for referente  ao abono pecuniário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1071995018
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Cálculo das férias |
| País: | Brasil |
| Ticket: | [#26685928](https://totvssuporte.zendesk.com/agent/tickets/26685928) |
| Issue: | [DRHCALCRM-11880](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-11880) |

## **02.****VERSÕES**

**A partir das Versões:**

* 12.1.2506.319
* 12.1.2510.245
* 12.1.2602.160
* 12.1.2606  e Superiores

## **03.****SITUAÇÃO/REQUISITO**

Conforme informado ao nosso setor Jurídico, o sistema não permite o lançamento do pagamento de férias em dobro quando o funcionário possui abono.

Veja retorno do questionamento realizado ao Jurídico:

*"Adicionalmente, a legislação permite, por meio do artigo 143, a conversão de até um terço das férias em abono pecuniário, ou seja, a possibilidade de o empregado “vender” parte dos dias de descanso, sem que isso altere a natureza ou os prazos do direito às férias.*

*No caso apresentado, o período aquisitivo compreendido de 27/03/2024 a 26/03/2025, encerrando-se, portanto, nessa última data. A partir daí, inicia-se o período concessivo, com prazo final em 26/03/2026 para que as férias sejam integralmente concedidas. O fato de o colaborador ter optado pela conversão de 10 dias em abono pecuniário não interfere nesse prazo, tampouco prorroga a data limite para concessão das férias. Trata-se apenas de uma forma de fruição parcial do direito, sem qualquer impacto sobre a contagem legal.*

*Dessa forma, caso as férias sejam concedidas após 26/03/2026, ainda que parcialmente, os dias que ultrapassarem esse limite devem ser pagos em dobro, independentemente da existência de abono pecuniário. Por fim, vale ressaltar que, nos casos de empregados regidos por contrato de trabalho, as férias devem ser iniciadas e concluídas dentro do período concessivo, ou seja, antes do término dos 12 meses subsequentes ao período aquisitivo, salvo nas exceções legais previstas.*

*Assim, o entendimento de que o sistema não deveria alterar o marco de início da dobra em função do lançamento do abono está correto, uma vez que tal lógica não encontra respaldo na legislação trabalhista vigente."*

## **04.****SOLUÇÃO**

Para viabilizar o cálculo das férias em dobro sobre a projeção do abono pecuniário, foi realizada uma implementação que observa as definições do parâmetro “**Abono de Férias (importante para Diferença de Férias e Abono em Dobro)**”. Esta configuração está disponível em Parametrizador | Férias | Cálculo 2/2, permitindo ao usuário determinar se o abono pecuniário será considerado Antes, Durante ou Após o período de gozo das férias. Com base nessa seleção, o sistema processará o valor do abono em dobro de acordo com as regras estabelecidas para cada opção.

## **05. ASSUNTOS RELACIONADOS**

* [Cálculo 2/2 - Férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=570048621)
