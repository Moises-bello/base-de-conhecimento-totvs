---
article_id: 360052073634
category: RH - Calculo Autonomo/Prolabore
content_hash: c7d711b983449280f1f4bbf8315d9e6983cf334c7c784476e9a3d8b26f1c410c
fetched_at: '2026-06-28T22:43:15.202646+00:00'
product: protheus
section_id: 360011983113
source: central-protheus
title: RH - Linha Protheus - GPE - Novo cálculo múltiplos vínculos -  Celetista Mensalista
  x Autônomo Mensalista
type: support-article
updated_at: '2025-04-15T18:02:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052073634-RH-Linha-Protheus-GPE-Novo-c%C3%A1lculo-m%C3%BAltiplos-v%C3%ADnculos-Celetista-Mensalista-x-Aut%C3%B4nomo-Mensalista
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22248388378263) Tempo aproximado para leitura: 00:03:00 min**

**Ocorrência**Novo cálculo do múltiplos vínculos MULTIV, exemplo de cálculo Celetista Mensalista x Autônomo Mensalista.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.25  
  
**Causa**Visando atender a [nota orientativa 2019.20 do e-Social](https://portal.esocial.gov.br/manuais/nota-orientativa-20-2019-multiplos-vinculos.pdf), a rotina de múltiplos vínculos internos sofrerá algumas alterações para que fique compatível com o que o governo espera receber em se tratando de múltiplos vínculos de empresas diferentes.   
   
**Solução**

Celetista Mensalista x Autônomo Mensalista

Cálculo folha funcionário celetista

![image2020-6-13_23-55-49.png](https://tdn.totvs.com/download/attachments/552575153/image2020-6-13_23-55-49.png?version=1&modificationDate=1592104122397&api=v2)

Conferência do cálculo

*INSS = 221,62*

Base INSS = 2500,00

1º Faixa = 1045,00 \* 0,075 => 78,37

2º Faixa = 2089,60 – 1045,00 => 1044,60 \* 0,09 => 94,01

3º Faixa = 2500,00 – 2089,60 => 410,40 \* 0,12 => 49,24

Soma das faixas => 78,37 + 94,01 + 49,24 = 221,62

*IRRF = 28,07*

Base – INSS \* % IRRF – Dedução => 2500,00 – 221,62 \* 0,075 – 142,80 = 28,07

Cálculo Funcionário Autônomo (Segundo vinculo):

![](https://tdn.totvs.com/download/attachments/552575153/image2020-6-13_23-57-20.png?version=1&modificationDate=1592104122363&api=v2)

Conferência do cálculo

*INSS = 385,00*

Base \* % INSS AUT => 3500,00 \* 0,11 => 385,00

*IRRF = 112,45*

Base – INSS \* % IRRF – Dedução => 3500,00 – 385,00 \* 0,15 – 354,80 = 112,45

Executando a rotina Múltiplos Vínculos

![](https://tdn.totvs.com/download/attachments/552575153/image2020-6-13_23-58-46.png?version=1&modificationDate=1592104122327&api=v2)

No primeiro vinculo não houve alterações no cálculo:

![](https://tdn.totvs.com/download/attachments/552575153/image2020-6-13_23-59-40.png?version=1&modificationDate=1592104122287&api=v2)

No segundo vinculo, foram ajustados os valores das verbas:

![](https://tdn.totvs.com/download/attachments/552575153/image2020-6-14_0-0-30.png?version=1&modificationDate=1592104122250&api=v2)

Conferência do cálculo

Base primeiro vinculo + Base segundo vinculo \* % INSS AUT – INSS primeiro vinculo =>

2500,00 + 3500,00 \* 0,11 – 221,62 => 438,38

*IRRF = 112,45*

Base primeiro vinculo + Base segundo vinculo \* % IRRF – Dedução – IR já descontado =>

2278,38 + 3061,62 \* 0,275 – 869,36 -  28,07 =  571,07

#### **Rotina GPEM930**

Desenvolvimento de nova rotina (GPEM930) onde será possível consultar todos os funcionários que possuam mais de um vínculo e efetuar o cálculo deles isoladamente do restante dos funcionários. O cálculo através das demais rotinas continua funcionando normalmente, o diferencial desta tela é que será possível calcular todos os vínculos de uma só vez. 

**Principais Campos e Parâmetros  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22247800574871)**

**Identificadores** de Cálculo necessários:

|  |  |  |  |
| --- | --- | --- | --- |
| **Id** | **Descrição** | **Tipo Cod** | **Tipo** |
| 0236 | Base IR Férias Outos Períodos | Base Provento | Valor |
| 0237 | IR Férias Outros Períodos | Base Provento | Valor |
| 0288 | Salário Contribuição INSS Outras Empresas | Base Provento | Valor |
| 0289 | Desconto INSS Outras Empresas | Base Provento | Valor |
| 0396 | Base INSS Férias Outros Períodos | Base Provento | Valor |
| 0397 | INSS Férias Outros Períodos | Base Provento | Valor |
| 0992 | Base IR Outras Empresas | Base Provento | Valor |
| 0993 | IR Outras Empresas | Base Provento | Valor |
| 1847 | Base INSS Autônomo Outras Empresas | Base Provento | Valor |
| 1951 | Deduções modelo completo IR Folha no período anterior | Base Provento | Valor |

**Saiba Mais**

[RH - Linha Protheus - GPE - INSS Múltiplos Vínculos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023123011-RH-Linha-Protheus-GPE-INSS-M%C3%BAltiplos-V%C3%ADnculos)

[RH - Linha Protheus - GPE - Validação Base INSS outras Empresas quando existe Múltiplo Vínculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051258974-RH-Linha-Protheus-GPE-Valida%C3%A7%C3%A3o-Base-INSS-outras-Empresas-quando-existe-M%C3%BAltiplo-V%C3%ADnculo)

[RH - Linha Protheus - GPE - Novo cálculo múltiplos vínculos de empresas diferentes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058056993-RH-Linha-Protheus-GPE-Novo-c%C3%A1lculo-m%C3%BAltiplos-v%C3%ADnculos-de-empresas-diferentes)

[RH - Linha Protheus - GPE - Novo cálculo múltiplos vínculos - Celetista semanalista x Autônomo Semanalista](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052866553-RH-Linha-Protheus-GPE-Novo-c%C3%A1lculo-m%C3%BAltiplos-v%C3%ADnculos-Celetista-semanalista-x-Aut%C3%B4nomo-Semanalista)

[RH - Linha Protheus - GPE - Novo cálculo múltiplos vínculos - Celetista semanalista x Autônomo mensalista](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052867133-RH-Linha-Protheus-GPE-Novo-c%C3%A1lculo-m%C3%BAltiplos-v%C3%ADnculos-Celetista-semanalista-x-Aut%C3%B4nomo-mensalista)

[RH - Linha Protheus - GPE - Novo cálculo múltiplos vínculos - Pró-labore x Autônomo semanalista](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052867673-RH-Linha-Protheus-GPE-Novo-c%C3%A1lculo-m%C3%BAltiplos-v%C3%ADnculos-Pr%C3%B3-labore-x-Aut%C3%B4nomo-semanalista)

[RH - Linha Protheus - GPE - Novo cálculo múltiplos vínculos - Autônomo Semanalista x Celetista Mensalista](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052074934-RH-Linha-Protheus-GPE-Novo-c%C3%A1lculo-m%C3%BAltiplos-v%C3%ADnculos-Aut%C3%B4nomo-Semanalista-x-Celetista-Mensalista)
