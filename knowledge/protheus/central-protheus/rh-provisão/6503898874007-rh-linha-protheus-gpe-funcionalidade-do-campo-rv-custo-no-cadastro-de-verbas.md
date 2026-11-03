---
article_id: 6503898874007
category: RH - Provisão
content_hash: f6f4c34646d387a5db3f05dff51d7ef5ae8042d87c237dde46ddd3076b076a1c
fetched_at: '2026-06-28T22:43:55.905407+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Funcionalidade do campo RV_CUSTO no cadastro de
  verbas
type: support-article
updated_at: '2025-06-18T18:03:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6503898874007-RH-Linha-Protheus-GPE-Funcionalidade-do-campo-RV-CUSTO-no-cadastro-de-verbas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17325460858647) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Funcionalidade do campo RV\_CUSTO no cadastro de verbas  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

No módulo GPE, este campo será utilizado para que de acordo com a configuração escolhida, a verba faça parte ou não da composição de **PROVISÃO SINTÉTICA ou SIMPLIFICADA (Ocorre junto com a folha de pagamento).**

Saiba Mais sobre a provisão Sintética ou Simplificada:   
[MP - GPE - Cálculo de folha apresenta verba de custo de provisão de férias e 13º (ID's 0194, 0195 e 0196 )](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051286113-MP-GPE-C%C3%A1lculo-de-folha-apresenta-verba-de-custo-de-provis%C3%A3o-de-f%C3%A9rias-e-13%C2%BA-ID-s-0194-0195-e-0196-)  
[MP - GPE - Como Devem ser Preenchidos os Campos %Prov.13º, %Prov.Férias e %Prov.Resc. na tabela S037](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034847234-MP-GPE-Como-Devem-ser-Preenchidos-os-Campos-Prov-13%C2%BA-Prov-F%C3%A9rias-e-Prov-Resc-na-tabela-S037)

Temos 2 opções para configuração do campo:  
  
- "S" para as verbas que serão somadas para custo de Provisão Simplificada no Resumo da Folha.

- "N" para não somar para custo da provisão.

**Obs:** Este campo influencia, também, o ambiente Gestão de Projetos (SIGAPMS).

Abaixo um exemplo do comportamento da rotina com o valor da provisão após configuração do campo RV\_CUSTO no cadastro de verbas: 

Tabela S037 com percentual definido de 10%:   
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6505112616855)

Cálculo da folha:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6504990401943)

Valor Base para cálculo da folha: R$ 2000,00

Verba 550 (verba de desconto) - RV\_CUSTO = SIM - R$ 161,82

Verba 817 (verba de base) - RV\_CUSTO = SIM - R$ 160,00

Cálculo: R$ 2000,00 - R$ 161,82 (desconto) + R$ 160,00 (base) = **R$ 1.998,18**

Com o valor definido de percentual 10% (R$ 1998,18 x 10% = R$ 199,82)   
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6505157180695)

**Importante:**

Esses Identificadores de cálculo, funcionam como uma "Provisão Sintética". Eles são usados **quando o cliente não deseja usar a rotina de provisão** (Miscelânea - Provisão - Provisão 13/ Férias), então utilizam apenas um % de provisionamento na tabela S037 (Versão 12 - Atualizações - Definição de Cálculo - Manutenção de Tabela), onde tem 3 campos pra informar os % que serão gerados sobre esta verba, que são os campos: "% Prov. Fer.", "% Prov. 13º" e "% Prov. Resc".

Logo, somente deverão ser utilizados para calcular essas verbas quando não é utilizada mensalmente a rotina de provisão e mesmo assim que fixar um % sobre a folha pra levar estas verbas para contabilidade.  
  
Esse cálculo de provisão não levará em conta informações de tem como  base o Salário, Adicionais, Médias, Baixas de transferência etc. 

**Saber Mais:**

[RH - Linha Protheus - GPE - Campo "Percentual" no cadastro de verbas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052138673-RH-Linha-Protheus-GPE-Campo-Percentual-no-cadastro-de-verbas?source=search)

[RH - Linha Protheus - GPE - Ao cadastrar ou alterar uma verba, aparece uma tela de Grupo de Verbas para seleção](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035659113-RH-Linha-Protheus-GPE-Ao-cadastrar-ou-alterar-uma-verba-aparece-uma-tela-de-Grupo-de-Verbas-para-sele%C3%A7%C3%A3o?source=search)
