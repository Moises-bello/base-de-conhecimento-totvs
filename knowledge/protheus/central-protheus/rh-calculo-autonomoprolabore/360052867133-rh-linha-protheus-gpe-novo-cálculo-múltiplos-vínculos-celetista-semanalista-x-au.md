---
article_id: 360052867133
category: RH - Calculo Autonomo/Prolabore
content_hash: 231ae42ccb32e7ea69247a435d96edb6b4de2381df4c967f7e6f75d1cd301276
fetched_at: '2026-06-28T22:43:15.209165+00:00'
product: protheus
section_id: 360011983113
source: central-protheus
title: RH - Linha Protheus - GPE - Novo cálculo múltiplos vínculos -  Celetista semanalista
  x Autônomo mensalista
type: support-article
updated_at: '2025-04-15T17:49:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052867133-RH-Linha-Protheus-GPE-Novo-c%C3%A1lculo-m%C3%BAltiplos-v%C3%ADnculos-Celetista-semanalista-x-Aut%C3%B4nomo-mensalista
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26240269907863) Tempo aproximado para leitura: **00:05:00 min**  
**Ocorrência**Novo cálculo do múltiplos vínculos MULTIV e exemplo de cálculo Celetista semanalista x Autônomo mensalista  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.25  
  
**Causa**Visando atender a [nota orientativa 2019.20 do e-Social](https://portal.esocial.gov.br/manuais/nota-orientativa-20-2019-multiplos-vinculos.pdf), a rotina de múltiplos vínculos internos sofrerá algumas alterações para que fique compatível com o que o governo espera receber em se tratando de múltiplos vínculos de empresas diferentes.   
  
**Solução**Celetista semanalista x Autônomo mensalista

Cálculo primeira semana:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26240269911575)

Conferência do cálculo

*INSS = 179,62*

Base primeira semana Primeiro vinculo

* R$1863,31 + R$286,66 => R$2149,97

1º Faixa = R$1045,00 \* 7,5% = R$78,37

2º Faixa = R$2089,60 – R$1045,00 = R$1044,60 \* 9% = R$94,01

3º Faixa = R$2149,97 – R$2089,60 = R$60,37 \* 12% = R$7,24

Soma das faixas = R$78,37 + R$94,01 + R$7,24 = R$179,62

Cálculo segunda semana:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26240260648087)

Conferência do cálculo

*INSS = 281,30*

Base primeira semana Primeiro vinculo + Base da segunda semana Primeiro vinculo

* R$2149,97 + R$2149,97 = R$4299,94

1º Faixa = R$1045,00 \* 7,5% = R$78,37

2º Faixa = R$2089,60 – R$1045,00 = R$1044,60 \* 9% = R$94,01

3º Faixa = R$3134,40 – R$2089,60 => R$1044,80 \* 12% = R$125,37

4º Faixa = R$4299,94 – R$3134,40 =  R$1165,54 \* 14%= R$163,17

Soma das faixas = R$78,37 + R$94,01 + R$125,37 + R$163,17 = R$460,92

Soma das faixas – INSS já descontado

* R$460,92 – R$179,62 = R$281,30

Cálculo segundo vinculo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26240269919255)

Conferência do cálculo

*INSS = 242,00*

Base \* % INSS AUT

* 2200,00 \* 0,11 = 242,00

Executando a rotina Múltiplos Vínculos novamente

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26240260654743)

A primeira semana permanece inalterada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26240269930775)

Cálculo da segunda semana primeiro vinculo e também permanece inalterado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26240260664215)

Calculo do segundo vinculo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26240260665495)

Conferência do cálculo

Base primeira semana + Base segunda semana + Base segundo vinculo

* R$2149,97 + R$2149,97 + R$2200,00 = R$6499,64 (R6101,06 teto)

Base \* % INSS AUT – INSS descontado primeira semana – INSS descontado segunda semana

* R$6101,06 \* 11%  – R$179,62 – R$281,30 = R$210,19

IRRF = 0,00

Não houve dedução de IR pois é mesmo é por competência e a data de pagamento no autônomo mensalista e dia 05.

#### **Rotina GPEM930**

Desenvolvimento de nova rotina (GPEM930) onde será possível consultar todos os funcionários que possuam mais de um vínculo e efetuar o cálculo deles isoladamente do restante dos funcionários. O cálculo através das demais rotinas continua funcionando normalmente, o diferencial desta tela é que será possível calcular todos os vínculos de uma só vez. 

**Principais Campos e Parâmetros  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26240269939735)**

**Identificadores** de Cálculo necessários:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26240260668951)  
  
**Saiba Mais**  
[Manual de Cálculo Multiplos Vinculos](https://tdn.totvs.com/pages/releaseview.action?pageId=552575179#ids-id3)

[RH - Calculo Autonomo/Prolabore](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983113-RH-Calculo-Autonomo-Prolabore)
