---
article_id: 360044532413
category: RH - Pensão
content_hash: cd82fcb3b03edca50fd62a084debf3cb3504727cd34cb17320d836ecd5eac2fc
fetched_at: '2026-06-28T22:43:35.212074+00:00'
product: protheus
section_id: 360004995674
source: central-protheus
title: RH - Linha Protheus - GPE - Como conferir o cálculo de pensão alimentícia sobre
  o líquido quando há incidência de IRRF no adiantamento
type: support-article
updated_at: '2021-04-26T16:52:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044532413-RH-Linha-Protheus-GPE-Como-conferir-o-c%C3%A1lculo-de-pens%C3%A3o-aliment%C3%ADcia-sobre-o-l%C3%ADquido-quando-h%C3%A1-incid%C3%AAncia-de-IRRF-no-adiantamento
---

**Dúvida**Como conferir o cálculo de pensão alimentícia sobre o líquido quando há incidência de IRRF no adiantamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Versão 12.1.17  
  
**Solução**

O funcionário possui adiantamento no mês e este adiantamento gerou um desconto de IRRF:

**Adiantamento = R$6.940,05**

Na folha de pagamento há o desconto de pensão alimentícia que deve deduzir o IRRF calculado no adiantamento para dedução da base:

A pensão alimentícia está com incidência para IRRF em seu cadastro (RV\_IR = SIM) e com isso o sistema precisa calcular a base do IRRF baseando-se no cálculo da pensão alimentícia.

Para isso o sistema faz o recalculo da pensão até que a diferença entre o valor descontado seja menor do que $0,01 centavo.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060508973/mceclip0.png)

De acordo com a tabela acima o sistema utiliza a seguinte fórmula:

**1º Cálculo:**

Verba com SIM para IRRF - Valor do INSS = BASE PENSÃO ALIMENTÍCIA

27791,51 - 642,33 = 27149,18

27149,18 \* 25% (PERCENTUAL DEFINIDO NO CADASTRO DE BENEFICIÁRIOS) = 6787,30 → PENSÃO

Cálculo do IRRF da folha:

(Verba com SIM para IRRF - Valor do INSS - Valor da Pensão - Valor do Adiantamento) \* Alíquota - Parcela a Deduzir = IR DA FOLHA

(27791,51 - 642,33 - 6787,30 - 6940,05) \* 27,5% - 869,36 = 2821,64

**2º Cálculo:**

Verba com SIM para IRRF - Valor do INSS - IR do 1º Cálculo = BASE PENSÃO ALIMENTÍCIA

27791,51 - 642,33 - 2821,64 = 24327,54

24327,54 \* 25% (PERCENTUAL DEFINIDO NO CADASTRO DE BENEFICIÁRIOS) = 6081,88→ PENSÃO

Cálculo do IRRF da folha:

(Verba com SIM para IRRF - Valor do INSS - Valor da Pensão - Valor do Adiantamento) \* Alíquota - Parcela a Deduzir = IR DA FOLHA

(27791,51 - 642,33 - 6081,88 - 6940,05) \* 27,5% - 869,36 = 3015,63

**3º Cálculo:**

Verba com SIM para IRRF - Valor do INSS - IR do 2º Cálculo = BASE PENSÃO ALIMENTÍCIA

27791,51 - 642,33 - 3015,63 = 24133,55

24133,55 \* 25% (PERCENTUAL DEFINIDO NO CADASTRO DE BENEFICIÁRIOS) = 6033,39 → PENSÃO

Cálculo do IRRF da folha:

(Verba com SIM para IRRF - Valor do INSS - Valor da Pensão - Valor do Adiantamento) \* Alíquota - Parcela a Deduzir = IR DA FOLHA

(27791,51 - 642,33 - 6033,39 - 6940,05) \* 27,5% - 869,36 = 3028,97

**4º Cálculo:**

Verba com SIM para IRRF - Valor do INSS - IR do 3º Cálculo = BASE PENSÃO ALIMENTÍCIA

27791,51 - 642,33 - 3028,97 = 24120,21

24120,21 \* 25% (PERCENTUAL DEFINIDO NO CADASTRO DE BENEFICIÁRIOS) = 6030,05 → PENSÃO

Cálculo do IRRF da folha:

(Verba com SIM para IRRF - Valor do INSS - Valor da Pensão - Valor do Adiantamento) \* Alíquota - Parcela a Deduzir = IR DA FOLHA

(27791,51 - 642,33 - 6030,05 - 6940,05) \* 27,5% - 869,36 = 3029,89

**5º Cálculo:**

Verba com SIM para IRRF - Valor do INSS - IR do 4º Cálculo = BASE PENSÃO ALIMENTÍCIA

27791,51 - 642,33 - 3029,89 = 24119,29

24119,29 \* 25% (PERCENTUAL DEFINIDO NO CADASTRO DE BENEFICIÁRIOS) = **6029,82** **→ PENSÃO DESCONTADA EM FOLHA**

Cálculo do IRRF da folha:

(Verba com SIM para IRRF - Valor do INSS - Valor da Pensão - Valor do Adiantamento) \* Alíquota - Parcela a Deduzir = IR DA FOLHA

(27791,51 - 642,33 - 6029,82 - 6940,05) \* 27,5% - 869,36 = **3029,95 → IR DESCONTADO EM FOLHA**
