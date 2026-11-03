---
article_id: 37869982636823
category: TOTVS Linha Protheus
content_hash: 6fbe2e56b3f517fd41a6053698b006f0ddc04f2a416018f825ed946631d51bb0
fetched_at: '2026-06-28T22:36:18.789575+00:00'
product: protheus
section_id: 360001794451
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Linha Protheus - Financeiro - FINA460 -Comportamento
  do parâmetro MV_RTIPFIN na Liquidação a Receber
type: support-article
updated_at: '2026-01-23T11:35:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37869982636823-Cross-Segmentos-Totvs-Backoffice-Linha-Protheus-Financeiro-FINA460-Comportamento-do-par%C3%A2metro-MV-RTIPFIN-na-Liquida%C3%A7%C3%A3o-a-Receber
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37870040986903) Tempo aproximado para leitura: **05:00 min**  
  
**Dúvida**  
Qual é a funcionalidade do parâmetro **MV\_RTIPFIN** na rotina de Liquidação Contas a Receber (FINA460) e qual a diferença prática entre a utilização do conteúdo **.T.** (Verdadeiro) e **.F.** (Falso) no cálculo de impostos?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**  
O parâmetro **MV\_RTIPFIN** define o critério de apuração dos impostos (como IRRF, PIS, COFINS, CSLL) no momento da liquidação de um título a receber. Ele determina se o sistema deve realizar um **rateio proporcional** do imposto já gravado no título original ou se deve realizar um **recálculo** baseando-se nas regras atuais do cadastro de Natureza Financeira.

Abaixo, detalhamos o comportamento de cada configuração utilizando um cenário prático.

Cenário de exemplo:

* **Título Original:** R$ 10.000,00
* **Imposto Original (IRRF 1,5%):** R$ 150,00 (Valor gravado na tabela SE1 na emissão).
* **Ação:** Liquidação (FINA460) do título original gerando **2 parcelas de R$ 5.000,00**.

---

#### 1. Configuração MV\_RTIPFIN = .T. (Rateio Proporcional)

**Conceito:** O sistema realiza o rateio do valor do imposto já existente no título original. O cálculo considera o valor gravado na tabela SE1 e o divide proporcionalmente entre as novas parcelas geradas, garantindo a integridade do valor original retido.

**Comportamento Prático:**

O sistema utiliza os R$ 150,00 originais e aplica a proporção das novas parcelas (50% para cada).

* **Parcela 1 (R$ 5.000,00):** Gera IR de **R$ 75,00**
* **Parcela 2 (R$ 5.000,00):** Gera IR de **R$ 75,00**

**Aplicação:** Indicado para garantir que a soma dos impostos das parcelas liquidadas seja exata ao imposto do título de origem, independentemente de alterações cadastrais posteriores.

---

#### 2. Configuração MV\_RTIPFIN = .F. (Recálculo)

**Conceito:** O sistema ignora o valor de imposto gravado no título original e realiza um novo cálculo. O sistema valida as regras atuais (Cliente/Natureza Financeira) aplicáveis ao valor da nova parcela no momento da liquidação.

**Comportamento Prático:**

O sistema aplica a alíquota do cadastro de Natureza Financeira (ex: 1,5%) sobre o novo valor base.

* **Parcela 1 (R$ 5.000,00) x 1,5%:** Gera IR de **R$ 75,00**
* **Parcela 2 (R$ 5.000,00) x 1,5%:** Gera IR de **R$ 75,00**

**Aplicação:** Indicado quando a liquidação deve respeitar a legislação ou alíquota vigente na data da operação financeira, e não a da emissão original.

---

#### Diferença Crítica (Alteração de Alíquota)

Embora os valores possam coincidir quando não há mudança na regra fiscal, a diferença fundamental ocorre se houver alteração na alíquota entre a data de emissão e a data de liquidação.

**Exemplo:** A alíquota na Natureza Financeira foi alterada de **1,5%** para **0% (Isento)** antes da liquidação.

* **Com MV\_RTIPFIN = .T.:** O sistema **mantém o imposto**. Ele ignora a isenção atual e rateia o valor de R$ 150,00 original. Os novos títulos terão imposto a pagar.
* **Com MV\_RTIPFIN = .F.:** O sistema **zera o imposto**. Ele recalcula com base na regra atual (0%). Os novos títulos não terão imposto retido.

#### Tabela Resumo

| **Característica** | **MV\_RTIPFIN = .T.** | **MV\_RTIPFIN = .F.** |
| --- | --- | --- |
| **Fonte do Cálculo** | Valor gravado no Título Original (SE1) | Cadastro de Natureza/Cliente Atual |
| **Metodologia** | Divisão matemática (Rateio) | Novo cálculo fiscal (Recálculo) |
| **Mudança de Alíquota** | Mantém a carga tributária original | Atualiza conforme a alíquota vigente hoje |

### Saiba mais

* [TDN - Parâmetro MV\_RTIPFIN e Cálculo na Liquidação](https://tdn.totvs.com/pages/releaseview.action?pageId=545236275#FINA460Liquida%C3%A7%C3%A3oareceberP12-04.IMPOSTOS)
