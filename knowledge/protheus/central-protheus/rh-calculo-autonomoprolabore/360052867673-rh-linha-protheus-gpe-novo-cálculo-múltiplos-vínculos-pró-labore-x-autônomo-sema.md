---
article_id: 360052867673
category: RH - Calculo Autonomo/Prolabore
content_hash: 8d954b80bcc651aa5c929cb47ebd1cd642486671225287beda59bc9bcd1fbb36
fetched_at: '2026-06-28T22:43:15.245149+00:00'
product: protheus
section_id: 360011983113
source: central-protheus
title: RH - Linha Protheus - GPE - Novo cálculo múltiplos vínculos - Pró-labore x
  Autônomo semanalista
type: support-article
updated_at: '2025-04-15T17:54:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052867673-RH-Linha-Protheus-GPE-Novo-c%C3%A1lculo-m%C3%BAltiplos-v%C3%ADnculos-Pr%C3%B3-labore-x-Aut%C3%B4nomo-semanalista
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26240861047063) Tempo aproximado para leitura: **00:04:00 min**  
**Ocorrência**Novo cálculo do múltiplos vínculos MULTIV, exemplo de cálculo Pró-labore x Autônomo semanalista  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.25  
  
**Causa**Visando atender a nota orientativa 2019.20 do E-social, a rotina de múltiplos vínculos internos sofrerá algumas alterações para que fique compatível com o que o governo espera receber em se tratando de múltiplos vínculos de empresas diferentes.   
  
**Solução**Pró-labore x Autônomo semanalista

Cadastro pró-labore:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26240861048215)

Cadastro autônomo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26240855137687)

Tela da rotina nova do multv (GPEM930):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26240861051543)

Cálculo vinculo 1 AUTÔNOMO SEMANALISTA semana 1:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26240855140631)

Recebimento: R$15.186,89

INSS (Teto): R$671,11

Base do IRRF: R$15186,89 - R$671,11 = R$14515,78

R$14515,78 \* 27,5% = R$3991,84

R$3991,84 - R$869,36 (PARCELA A DEDUZIR) = **R$3122,47 (DESCONTO DO IRRF) Primeiro Vinculo Nº pagamento 1**

Vinculo 2 pró-labore:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26240855142295)

Recebimento: R$15.236,38

Base IRRF outras empresas: R$14515,78

IRRF outras empresas: R$3.122,47

R$15236,38 + R$14515,78 = R$29.752,16

R$29752,16 \* 27,5% = R$8181,84

R$8181,84 - R$869,36 (parcela a deduzir) = R$7312,48

R$7312,48 - R$3122,47 (IRRF outras empresas) = **R$4190,01 (DESCONTO DO IRRF) Segundo Vinculo**

Primeiro Vinculo Semana Nº de pagamento 02:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26240861057943)

Recebimento: R$15186,89

BASE IRRF OUTRAS EMPRESAS: R$15.236,38

IRRF OUTRAS EMPRESAS: R$4.190,01

Soma dos recebimentos do autônomo semanalista: R$15.186,89 + R$15.186,89 = R$30.373,78

R$30.373,78 - R$671,11 = 29.702,67 (BASE DO IRRF)

R$29.702,67 + R$15.236,38 (BASE IRRF OUTRAS EMPRESAS) = R$44.939,05

R$44.939,05 \* 27,5% = R$12.358,24

R$12.358,24 - R$869,36 (PARCELA A DEDUZIR) = R$11.488,88

R$11488,88 - R$3122,47 (IRRF PRIMEIRO VINCULO SEMANA 1) - R$4190,01 (IRRF SEGUNDO VINCULO) = **R$4176,39 (DESCONTO DO IRRF) Segundo Vinculo 2 Numero de pagamento 02**

**I****Rotina GPEM930**

Desenvolvimento de nova rotina (GPEM930) onde será possível consultar todos os funcionários que possuam mais de um vínculo e efetuar o cálculo deles isoladamente do restante dos funcionários. O cálculo através das demais rotinas continua funcionando normalmente, o diferencial desta tela é que será possível calcular todos os vínculos de uma só vez. 

**Principais Campos e Parâmetros  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26240861058839)**

**Identificadores** de Cálculo necessários:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26240861060631)  
  
**Saiba Mais**  
[Manual de Cálculos Multiplos Vinculos](https://tdn.totvs.com/pages/releaseview.action?pageId=552575179#ids-id3)

[RH - Calculo Autonomo/Prolabore](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983113-RH-Calculo-Autonomo-Prolabore)
