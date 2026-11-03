---
article_id: 34371268913303
category: Escrita Fiscal - Configurador de Tributos
content_hash: cae7f0172fa360a9f9d051587fcf526a8aaf11c091fd64359eed246be39debf4
fetched_at: '2026-06-28T22:39:17.551728+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Quantas majorações
  posso incluir em outro tributo no Configurador de Tributos?
type: support-article
updated_at: '2025-08-22T16:44:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34371268913303-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Quantas-majora%C3%A7%C3%B5es-posso-incluir-em-outro-tributo-no-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34371254988439) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**  
Quantas majorações posso incluir em outro tributo no Configurador de Tributos?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - a partir da versão 12.1.2310  
  
**Solução**

**Somente é possível adicionar um percentual extra de majoração ao cálculo de determinados tributos.**

**Abaixo detalhamento completo.**

## 1. O que é Majoração?

A majoração de tributos permite adicionar um percentual extra ao cálculo de determinados tributos, como o FECP (Fundo de Combate à Pobreza) sobre o ICMS ou o DIFAL.  
Para garantir o correto funcionamento do sistema e evitar alterações manuais em fórmulas, é fundamental utilizar o campo **Tributo para Majoração (F2B\_TRBMAJ)**.

> **Referência:**  
> [Configurador de Tributos](https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos#CFGTRIBConfiguradordeTributos-RegrasComplementares)

---

## 2. Conceitos - Chave

* **Tributo para Majoração (F2B\_TRBMAJ):** Campo onde se informa qual tributo será utilizado como base para a majoração.
* **Regra de Majoração:** Deve ser cadastrada apenas uma regra de alíquota de majoração para o tributo.
* **Dinamicidade:** A alíquota pode ser atualizada dinamicamente conforme o NCM e o estado.

---

## 3. Como Configurar o Cálculo com Majoração

### 3.1. Identifique os Tributos Envolvidos

* **Tributo principal:** Exemplo: ICMS
* **Tributo majorado:** Exemplo: FECP de Difal (ID TOTVS `000042`)
* **Tributo que referencia a majoração:** Exemplo: DIFAL (ID TOTVS `000037`)

### 3.2. Configure as Regras de Cálculo

#### a) ICMS

* **Tributo:** ICMS (`000021`)
* **Base de cálculo:**  
  `Valor da mercadoria + frete + seguro + despesa - desconto`
* **Alíquota:** Definida pelo estado (exemplo: 12%)
* **Fórmula do valor:**  
  `Base * Alíquota`

#### b) FECP do Difal (Tributo Majorado)

* **Tributo:** FCPCMP (`000042`)
* **Base de cálculo:**  
  `Valor da mercadoria + frete + seguro + despesa - desconto`
* **Alíquota:**
  + Índice de cálculo: `I:MAJORACAO`
  + Atualizada dinamicamente conforme o NCM
* **Fórmula do valor:**  
  `Base * Alíquota`

#### c) DIFAL (Tributo que referencia a majoração)

* **Tributo:** DIFAL (`000037`)
* **Base de cálculo:**  
  `Valor da mercadoria + frete + seguro + despesa - desconto`
* **Alíquota:** Definida pelo estado
* **Configuração especial:**
  + Informe o tributo majorado (FECP) no campo **Tributo para Majoração (F2B\_TRBMAJ)**
* **Fórmula automática:**  
  `Base * (Alíquota + ALQ:FECP)`
* **Fórmula com dedução de ICMS:**  
  `(Base * (Alíquota + ALQ:FECP)) - Valor ICMS`

  > **Nota:**  
  > `ALQ:FECP` corresponde à alíquota do tributo informado no campo de majoração.

---

## 4. Exemplo Prático

| Descrição | Valor |
| --- | --- |
| Valor da mercadoria | R$ 10.000,00 |
| Alíquota interestadual ICMS | 12% |
| Alíquota interna no destino | 18% |
| Alíquota FECP de Difal | 2% |

### Cálculo do ICMS e DIFAL com Majoração

* Base de Cálculo: R$ 10.000,00

* Alíquota Interestadual: 12%

* Alíquota Interna no Destino: 18%

* Valor do ICMS: R$ 1.200,00

* Valor do ICMS Interestadual: R$ 1.800,00

* Valor do FECP Difal: R$ 200,00

* Valor do DIFAL sem majoração: R$ 600,00

* Valor do DIFAL com majoração: R$ 800,00

---

## 5. Recomendações e Boas Práticas

* Sempre utilize o campo **F2B\_TRBMAJ** para informar o tributo a ser majorado.
* Configure a regra de cálculo do FECP com o índice `I:MAJORACAO` para garantir atualização dinâmica da alíquota.
* Certifique-se de que as fórmulas estejam corretas e que cada tributo esteja devidamente referenciado.
* Revise as configurações após alterações de legislação ou regras fiscais.

---

## 6. Observações Finais

* O correto uso do campo de majoração evita inconsistências e retrabalho.
* O sistema reconhecerá automaticamente a base, alíquota e valor do tributo majorado.
* Em caso de dúvidas, consulte a documentação oficial ou o suporte técnico.
