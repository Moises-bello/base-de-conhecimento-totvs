---
content_hash: 05686390c88299a067a6c95cfb45800b68ea91fc2eb29bc66d9c8b8e69317c2e
fetched_at: '2026-06-29T00:11:49.420246+00:00'
page_id: '832650111'
product: rm
source: tdn-rm
title: DT - FGTS Digital - Tratativa quando há base negativa de FGTS e/ou FGTS 13o.
  Salário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=832650111
version: 49
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento - eSocial |
| Função: | FGTS Digital - Tratativa quando há base negativa de FGTS e/ou FGTS 13o. Salário |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-7288](https://jiraproducao.totvs.com.br/browse/DRHROTRM-7288) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2306.240
* 12.1.2310.182
* 12.1.2402.117 e superiores

## **03.****SITUAÇÃO/REQUISITO**

Adaptar  o produto TOTVS Folha de Pagamento para compatibilidade com as normas do FGTS Digital, especialmente para cenários de rescisão com desconto de adiantamento de 13º Salário superior ao valor pago e estorno de FGTS maior que os proventos.

## **04. SOLUÇÃO**

Com a implementação do FGTS Digital, foram realizadas alterações na demonstração das bases de FGTS para os seguintes cenários:

1. Quando o funcionário demitido tem desconto de adiantamento de 13o. Salário superior ao valor pago.
2. Quando o funcionário demitido tem um estorno de FGTS maior que os proventos.

Conforme descrito no Manual de Orientação do Sistema (MOS) no item descrito no MOS no item "9. Projeção do aviso prévio indenizado sobre o 13º salário", relata que: 

**"9.1. No cadastramento de rubrica relativa à projeção do aviso prévio indenizado sobre o 13º salário, deve ser indicada a incidência de FGTS {codIncFGTS} = 21 ou 93, pois essa verba deriva do aviso prévio indenizado e deve acompanhá-lo para fins de apuração da base de cálculo do FGTS. "**

No contexto do programa FGTS Digital, a base "FGTS Aviso Prévio Indenizado" consiste na soma do Aviso Prévio Indenizado com o 13º Salário Indenizado (codIncFGTS = 21). Portanto, o desconto de adiantamento de 13º Salário (codIncFGTS = 12) não pode estornar a base de FGTS do 13º Indenizado, assim como eventos de estorno de FGTS (codIncFGTS = 11), como faltas, não podem estornar a base de FGTS do Aviso Prévio Indenizado.

Para realizar essa tratativa foi necessário a criação de novos campos para que os existentes não sejam afetados e ocorra efeitos colaterais. Sendo os novos campos

* **Base FGTS eSocial**(eventos que incidem FGTS - eventos que estornam FGTS) desconsiderando os códigos de cálculos: 62, 99 e 219;
* **Base FGTS 13o. Sal.** **eSocial**(eventos que incidem FGTS 13 - eventos que estornam FGTS 13) desconsiderando os códigos de cálculos 71, 98 e 220;
* **Base FGTS Indeniz.** **eSocial** considerando somente os códigos de cálculos: 62, 99, 219, 71, 98 e 220.
* **FGTS eSocial**
* **FGTS 13o. Sal. eSocial**
* **FGTS Indeniz.** **eSocial**

**ATENÇÃO: As demais bases de FGTS não sofreram alterações.**

| Código de Cálculo | Descrição Código de Cálculo |
| --- | --- |
| 62 | [Aviso Prévio](https://tdn.totvs.com/pages/viewpage.action?pageId=452719687) |
| 99 | [Dif. Aviso Prévio](https://tdn.totvs.com/pages/viewpage.action?pageId=452718356) |
| 219 | [Aviso Prévio Calculado Pelo Usuário](https://tdn.totvs.com/pages/viewpage.action?pageId=452719689) |
| 71 | [13º Salário indenizado](https://tdn.totvs.com/pages/viewpage.action?pageId=452718484) |
| 98 | [Dif 13º Salário indeniz. Rescisão](https://tdn.totvs.com/pages/viewpage.action?pageId=452718367) |
| 220 | [13º Calculado Pelo Usuário](https://tdn.totvs.com/pages/viewpage.action?pageId=452719649) |

Os processos abaixo foram adequados utilizando os novos campos:

* Folha Analítica: Inclusão dos campos acima
* Relatório Conferência de FGTS - Tratativa o campo "Valor RH" para considerar os novos campos

Aba 1true1Folha AnaliticaFGTS Digital

| FOLHA ANALITICA | REGRA | OBSERVAÇÃO |
| --- | --- | --- |
| Base FGTS eSocial | PEVENTO.INCIDEFGTS - PEVENTO.ESTORNAFGTS | Serão desconsiderados os códigos de códigos: 62, 99, 219 |
| Base FGTS 13º Sal eSocial | PEVENTO.INCIDEFGTS13 - PEVENTO.ESTORNAFGTS13 | Serão desconsiderados os códigos de códigos: 71, 98 e 220 |
| Base FGTS Indeniz. eSocial |  | Serão considerados os códigos de códigos:  62, 99, 219  (Aviso Indenizado) +  Serão considerados os códigos de códigos:  71, 98 e 220 (13o. Salário) |
| FGTS eSocial |  | Retornar o valor do FGTS (8% ou 2%) sobre o campo Base FGTS eSocial |
| FGTS 13º Sal eSocial |  | Retornar o valor do FGTS (8% ou 2%) sobre o campo Base FGTS 13º Sal eSocial |
| FGTS Indeniz. eSocial |  | Retornar o valor do FGTS (8% ou 2%) sobre o campo Base FGTS Indeniz. eSocial |

No exemplo abaixo o funcionário possui faltas e desconto de uma antecipação de 13° salário fazendo com que as bases de folha e 13° salário de FGTS fiquem negativas, note que com as novas bases é levado corretamente, apresentando o total do valor indenizado.

Retorno eSocial

4Relatório de Conferencia FGTSRelatório de Conferencia FGTS

| CAMPO | ANTES | ATUAL |
| --- | --- | --- |
| 13° SALÁRIO | Busca o campo "Base FGTS 13º" da Folha Analítica | Busca o campo "Base FGTS 13º. Sal. eSocial" da Folha Analítica |
| MENSAL | Busca o campo "Base FGTS" da Folha Analítica | Busca o campo "Base FGTS eSocial" da Folha Analítica |
| RESCISÓRIO | Quando for diferente dos tipos demissão 3 ou 4 os seguintes campos da folha Analítica: "Base FGTS 13º" e "Base FGTS"; | Quando for diferente dos tipos demissão 3 ou 4 os seguintes campos da folha Analítica:"Base FGTS 13º. Sal. eSocial" + "Base FGTS Indeniz. eSocial" + "Base FGTS eSocial"; |

No exemplo abaixo o funcionário possui faltas e desconto de uma antecipação de 13° salário fazendo com que as bases de folha e 13° salário de FGTS fiquem negativas,note que no relatorio é considerado corretamente, apresentando o total do valor indenizado.

Retorno eSocial

## **5. DEMAIS INFORMAÇÕES**

[Folha Analítica](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719339)
