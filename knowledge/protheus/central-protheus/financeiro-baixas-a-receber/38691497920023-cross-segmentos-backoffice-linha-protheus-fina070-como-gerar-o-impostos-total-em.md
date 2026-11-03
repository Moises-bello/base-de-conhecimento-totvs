---
article_id: 38691497920023
category: Financeiro - Baixas a Receber
content_hash: bb2e60b4de1a2d13c0a6a7f68867c762648cfe6f37006f25dd85a32888f2456e
fetched_at: '2026-06-28T22:37:43.842435+00:00'
product: protheus
section_id: 33820269506967
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - FINA070 - Como gerar o impostos
  total em uma baixa parcial.
type: support-article
updated_at: '2026-02-27T18:08:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38691497920023-Cross-Segmentos-Backoffice-Linha-Protheus-FINA070-Como-gerar-o-impostos-total-em-uma-baixa-parcial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38691506330775) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como posso realizar a baixa total dos impostos em uma baixa parcial?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões]  
  
**Solução**

**Observação:** Esse procedimento aplica-se aos **impostos na baixa**.

Caso a regra esteja sendo utilizada na **emissão do documento**, ao realizar a configuração o sistema passará a gerar os impostos conforme definido nos parâmetros.

Assim, se o movimento possuir parcelas, os impostos poderão ser gerados **em seu valor total**, em vez de serem distribuídos (rateados) por parcela, conforme a configuração realizada.

Para realizar a baixa, seja rateando ou não os impostos, é necessário configurar corretamente esses dois parâmetros;

* **MV\_RTIPESP**
* **MV\_RTIPFIN**

### **Regras dos Parâmetros MV\_RTIPFIN e MV\_RTIPESP**

#### Quando **MV\_RTIPFIN = .T.**

* Se **MV\_RTIPESP = 000000** ou **111111**  
  → Os impostos serão **rateados em todas as parcelas**.
* Se **MV\_RTIPESP = 222222**  
  → Os impostos serão **atribuídos integralmente na primeira parcela**.

#### Quando **MV\_RTIPFIN = .F.**

* Se **MV\_RTIPESP = 000000** ou **222222**  
  → Os impostos serão **atribuídos na primeira parcela**.
* Se **MV\_RTIPESP = 111111**  
  → Os impostos serão **rateados em todas as parcelas**.

## Situação apresentada

O cliente possui **PCC e IR**, porém deseja que **somente o IR** seja considerado na **primeira parcela**.  
Atualmente, o parâmetro está configurado como:

* **MV\_RTIPFIN = .T.**

### O que fazer?

Manter:

* **MV\_RTIPFIN = .T.**

E ajustar o parâmetro **MV\_RTIPESP** conforme a posição do imposto.

## Estrutura do MV\_RTIPESP

O parâmetro segue a seguinte ordem:

```
MV_RTIPESP = 0    0    0    0    0    0  
              ISS  IRRF INSS CSLL COFINS PIS
```

Cada posição corresponde a um imposto específico.

### Para considerar apenas o IRRF como exemplo na baixa parcial:

Como o **IRRF é a segunda posição**, o parâmetro deverá ser configurado da seguinte forma:

```
MV_RTIPESP = 020000
```

Dessa forma, somente o **IRRF** será tratado de forma diferenciada.

**SAIBA MAIS:**

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Ratear os impostos nas notas fiscais de saída - Retenções](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021640451-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Ratear-os-impostos-nas-notas-fiscais-de-sa%C3%ADda-Reten%C3%A7%C3%B5es)

[DT Rateio da Retenção de impostos PCC (Pis, Cofins, CSLL) conforme parâmetros MV\_RTIPFIN e MV\_RTIPESP](https://tdn.totvs.com/pages/releaseview.action?pageId=828862368)
