---
article_id: 360052074934
category: RH - Calculo Autonomo/Prolabore
content_hash: 668072874d0c2afc065a31bea60eb55beb2b9920c75d24ad9808e9ebf5ef89f7
fetched_at: '2026-06-28T22:43:15.227617+00:00'
product: protheus
section_id: 360011983113
source: central-protheus
title: RH - Linha Protheus - GPE - Novo cálculo múltiplos vínculos - Autônomo Semanalista
  x Celetista Mensalista
type: support-article
updated_at: '2025-04-15T17:46:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052074934-RH-Linha-Protheus-GPE-Novo-c%C3%A1lculo-m%C3%BAltiplos-v%C3%ADnculos-Aut%C3%B4nomo-Semanalista-x-Celetista-Mensalista
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26245638407831) Tempo aproximado para leitura: **00:04:00 min**  
**Ocorrência**Novo cálculo do múltiplos vínculos MULTIV, exemplo de cálculo Autônomo Semanalista x Celetista Mensalista  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.25  
  
**Causa**Visando atender a [nota orientativa 2019.20 do e-Social](https://portal.esocial.gov.br/manuais/nota-orientativa-20-2019-multiplos-vinculos.pdf), a rotina de múltiplos vínculos internos sofrerá algumas alterações para que fique compatível com o que o governo espera receber em se tratando de múltiplos vínculos de empresas diferentes.   
  
**Solução**Exemplo de cálculo Autônomo Semanalista x Celetista Mensalista

Cálculo primeira semana autônomo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26245627541655)

Conferência do cálculo

*INSS = 82,50*

Base \* % INSS AUT => 750,00 \* 0,11 => 82,50

Segunda semana autônomo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26245627556759)

Conferência do cálculo

*INSS = 82,50*

Base \* % INSS AUT => 750,00 \* 0,11 => 82,50

Cálculo segundo vinculo, celetista mensalista:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26245638428823)

Conferência do cálculo

*INSS = 172,42*

Base INSS = 2090,00

1º Faixa = 1045,00 \* 0,075 => 78,37

2º Faixa = 2089,60 – 1045,00 => 1044,60 \* 0,09 => 94,01

3º Faixa = 2090,00 – 2089,60 => 0,40 \* 0,12 => 0,04

Soma das faixas => 78,37 + 94,01 + 0,04 = 172,42

Executando a rotina Múltiplos Vínculos

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26245627562903)

Primeiro vinculo semana 02 sem alterações:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26245638436759)

Cálculo do mensalista celetista:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26245627570583)

Conferência do cálculo

*INSS = 179,92*

Base INSS = Salário primeira semana primeiro vinculo + segundo vinculo

* 750,00 + 2090,00 = 2840,00

1º Faixa = 1045,00 \* 0,075 => 78,37

2º Faixa = 2089,60 – 1045,00 => 1044,60 \* 0,09 => 94,01

3º Faixa = 2840,00 – 2089,60 => 750,40 \* 0,12 => 90,04

Soma das faixas => 78,37 + 94,01 + 90,04 = 262,42

Soma das faixas – INSS já descontado

* 262,42 – 82,50 = 179,92

Cálculo da segunda semana do primeiro vinculo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26245627573271)

Conferência do cálculo

*INSS = 132,48*

Base INSS = Base primeiro vinculo primeira semana + Base segundo vinculo + Base primeiro vinculo segunda semana=> 750,00 + 2090,00 + 750,00 = 3590,00

Base \* % INSS AUT – INSS já descontado primeiro vinculo – INSS descontado segundo vinculo

* 3590,00 \* 0,11 – 82,50 – 179,92 = 132,48

#### **Rotina GPEM930**

Desenvolvimento de nova rotina (GPEM930) onde será possível consultar todos os funcionários que possuam mais de um vínculo e efetuar o cálculo deles isoladamente do restante dos funcionários. O cálculo através das demais rotinas continua funcionando normalmente, o diferencial desta tela é que será possível calcular todos os vínculos de uma só vez. 

**Principais Campos e Parâmetros  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25024863857559)**

**Identificadores** de Cálculo necessários:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25024875149079)  
  
**Saiba Mais**  
[Manual de Cálculos Multiplos Vinculos](https://tdn.totvs.com/pages/releaseview.action?pageId=552575179#ids-id3)

[RH - Calculo Autonomo/Prolabore](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983113-RH-Calculo-Autonomo-Prolabore)
