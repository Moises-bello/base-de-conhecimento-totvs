---
content_hash: b0a16c2421e793f975576385cf02f12c5e8c078d331f82f86e26160970cf9a24
fetched_at: '2026-06-29T00:11:49.683785+00:00'
page_id: '837420172'
product: rm
source: tdn-rm
title: DT - S-1200 - Tratativa na geração do XML para diferença de férias retroativa
  e férias partidas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=837420172
version: 6
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | S-1200 - Tratativa na geração do XML para diferença de férias retroativa e férias partidas |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado): | [DRHROTRM-9623](https://jiraproducao.totvs.com.br/browse/DRHROTRM-9623 "View this issue") |

## **02.** **VERSÕES**

Lembrando que, será a partir dos patches:

* 12.1.2310.189
* 12.1.2402.125 e superiores

## **03.** **SITUAÇÃO/REQUISITO**

Em uma circunstância específica: quando o funcionário tem dois períodos de gozo de férias, abrangendo meses diferentes, com dissídio em parte de ambos os períodos e diferença sem dissídio em outra parte do gozo.

**EXEMPLO:**

* + O funcionário possui duas férias partidas, sendo:
  + Primeiro gozo: 26/12/2023 a 04/01/2024 = 10 dias
  + Segundo gozo: 25/01/2024 a 08/02/2024 = 15 dias
  + **Competência atual:** 02/2024
  + **Diferença Dissídio Retroativa**: 01/01/2024

**Em 02/2024**

Ao calcular a diferença retroativa o sistema irá lançar:

**Primeiro Gozo**

Diferença Férias Pagas no Mês Anterior (**[CC86](https://tdn.totvs.com/pages/viewpage.action?pageId=452718395)**) =  4 dias (01/01 a 04/01/2024)

DISSÍDIO = SIM

**Segundo Gozo**

Diferença Férias Pagas no Mês (cc45) =  7 dias (25/01 a 31/01/2024)

DISSÍDIO = SIM

Diferença Férias Pagas no Mês Anterior (**[CC86](https://tdn.totvs.com/pages/viewpage.action?pageId=452718395)**) = 8 dias (01/02 a 08/02/2024) 

DISSÍDIO = NÃO

Neste caso o cálculo lança o **[CC86](https://tdn.totvs.com/pages/viewpage.action?pageId=452718395)** com o valor de 12 dias e como DISSÍDIO = NÃO, e lança o [CC116](https://tdn.totvs.com/pages/viewpage.action?pageId=452718644) com 11 dias, que estorna dos 19 dias totais  
A base de INSS tem que ficar com os 8 dias referente ao mês de fevereiro, que é a competência atual.

Neste cenário, o cálculo está lançando o  **[CC86](https://tdn.totvs.com/pages/viewpage.action?pageId=452718395)** com o valor de 12 dias (8 + 4), com DISSÍDIO = NÃO, e o [CC116](https://tdn.totvs.com/pages/viewpage.action?pageId=452718644) com 11 dias (7 + 4), estornando dos 19 dias totais. A base de INSS precisa refletir apenas os 8 dias referentes ao mês de fevereiro, que é a competência atual.

## **04.** **SOLUÇÃO**

Realizamos a tratativa na geração do XML para corrigir a duplicação de valores nos eventos de diferença de férias. Agora, quando os códigos de cálculos 45, 86, 79 e 87 estiverem presentes na PFFINANC, consultamos a tabela PFVERBASDISFER para verificar se existem eventos duplicados com valores de dissídio diferentes.

Para cada código de cálculo:

* Para o cc45, verificamos o código [41 - Férias no Mês](https://tdn.totvs.com/pages/viewpage.action?pageId=452718570)
* Para o cc86, verificamos o código [44 - Férias Pagas no Mês Anterior](https://tdn.totvs.com/pages/viewpage.action?pageId=452718568)
* Para o cc79, verificamos o código [76 - 1/3 Férias no Mês](https://tdn.totvs.com/pages/viewpage.action?pageId=452719012)
* Para o cc87, verificamos o código [78 - 1/3 férias pagas mês anterior](https://tdn.totvs.com/pages/viewpage.action?pageId=452719011)

Caso exista mais de uma linha do mesmo evento na tabela PFVERBASDISFER, consideramos o valor do evento com DISSIDIO=SIM e abatemos esse valor do evento de diferença na PFFINANC que será enviado para o eSocial. Também ajustamos o campo de referência no XML.
