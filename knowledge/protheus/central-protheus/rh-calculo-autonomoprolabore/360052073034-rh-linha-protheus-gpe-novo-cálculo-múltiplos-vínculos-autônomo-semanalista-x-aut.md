---
article_id: 360052073034
category: RH - Calculo Autonomo/Prolabore
content_hash: 591d4994b6d2e1cdfaad32e2a550adea2b52e4b29deea3796a71122fbef8da0a
fetched_at: '2026-06-28T22:43:15.220738+00:00'
product: protheus
section_id: 360011983113
source: central-protheus
title: RH - Linha Protheus - GPE - Novo cálculo múltiplos vínculos - Autônomo semanalista
  x Autônomo mensalista
type: support-article
updated_at: '2025-04-15T17:55:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052073034-RH-Linha-Protheus-GPE-Novo-c%C3%A1lculo-m%C3%BAltiplos-v%C3%ADnculos-Aut%C3%B4nomo-semanalista-x-Aut%C3%B4nomo-mensalista
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22249428912919) Tempo aproximado para leitura: 00:03:00 min****Ocorrência**Novo cálculo do múltiplos vínculos MULTIV, exemplo de cálculo Autônomo semanalista x Autônomo mensalista.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.25  
  
**Causa**Visando atender a nota Orientativa 2019.20 do E-social, a rotina de múltiplos vínculos internos sofrerá algumas alterações para que fique compatível com o que o governo espera receber em se tratando de múltiplos vínculos de empresas diferentes. 

**Solução**Exemplo de cálculo Autônomo semanalista x Autônomo mensalista  
Cadastro período autônomo semanalista:

![image2020-6-13_23-43-57.png](https://tdn.totvs.com/download/attachments/552575153/image2020-6-13_23-43-57.png?version=1&modificationDate=1592104122800&api=v2)

Cálculo da primeira semana:

![image2020-6-13_23-44-39.png](https://tdn.totvs.com/download/attachments/552575153/image2020-6-13_23-44-39.png?version=1&modificationDate=1592104122760&api=v2)

Conferência do cálculo

Base \* % INSS AUT => 1500,00 \* 0,11 => 165,00

Cálculo segunda semana:

**![image2020-6-13_23-45-34.png](https://tdn.totvs.com/download/attachments/552575153/image2020-6-13_23-45-34.png?version=1&modificationDate=1592104122720&api=v2)**

Conferência do cálculo

INSS = Base segunda semana \* % INSS AUT => 1500,00 \* 0,11 => 165,00

IRRF = Base Total primeira semana + Base Total segunda semana – INSS Descontado \* % IRRF – Dedução => 1500,00 + 1500,00 – 165,00 – 165,00 \* 0,075 – 142,80 => 57,45

Cadastro período autônomo mensalista:

Cálculo da folha do segundo vinculo:

![image2020-6-13_23-48-23.png](https://tdn.totvs.com/download/attachments/552575153/image2020-6-13_23-48-23.png?version=1&modificationDate=1592104122640&api=v2)

Conferência do cálculo

INSS = Base segundo vínculo \* % INSS AUT => 3000,00 \* 0,11 => 330,00

IRRF = Base total – INSS \* % IRRF – Dedução => 3000,00 \* 0,075 – 142,80 => 57,45

Execute o cálculo pela rotina Múltiplos Vínculos em **Miscelânea > Cálculos > Múltiplos vínculos (GPEM930)**

![image2020-6-13_23-50-25.png](https://tdn.totvs.com/download/attachments/552575153/image2020-6-13_23-50-25.png?version=1&modificationDate=1592104122603&api=v2)

Log das matriculas que foram executadas:

![image2020-6-13_23-51-9.png](https://tdn.totvs.com/download/attachments/552575153/image2020-6-13_23-51-9.png?version=1&modificationDate=1592104122557&api=v2)

Verificaremos novamente o cálculo do primeiro vinculo, pagamento 01:

![image2020-6-13_23-52-10.png](https://tdn.totvs.com/download/attachments/552575153/image2020-6-13_23-52-10.png?version=1&modificationDate=1592104122520&api=v2)

Verificaremos novamente o cálculo do primeiro vinculo, pagamento 02:

![image2020-6-13_23-52-52.png](https://tdn.totvs.com/download/attachments/552575153/image2020-6-13_23-52-52.png?version=1&modificationDate=1592104122483&api=v2)

Conferência do cálculo

Base \* % INSS AUT => 1500,00 \* 0,11 => 165,00

*IRRF = 57,45*

Base – INSS \* % IRRF – Dedução => 1500,00 + 1500,00 – 330,00 \* 0,075 – 142,80 = 57,45

Verificaremos o cálculo do segundo vinculo:

![image2020-6-13_23-53-58.png](https://tdn.totvs.com/download/attachments/552575153/image2020-6-13_23-53-58.png?version=1&modificationDate=1592104122437&api=v2)

Conferência do cálculo

Verba 913 => Bases duas semanas vinculo 1 => 1500,00 + 1500,00 = 3000,00

Verba 840 => Soma do INSS descontado nas duas semanas do vínculo 1 => 165,00 + 165,00 = 330,00

Verba 417 => Soma de todas as bases dos dois vínculos \* % INSS AUT – INSS já descontado => 1500,00 + 1500,00 + 3000,00 \* 0,11 – 330,00 => 330,00

*IRRF = 57,45*

Base – INSS \* % IRRF – Dedução => 3000,00 – 330,00 \* 0,075 – 142,80 = 57,45

#### **Rotina GPEM930**

Desenvolvimento de nova rotina (GPEM930) onde será possível consultar todos os funcionários que possuam mais de um vínculo e efetuar o cálculo deles isoladamente do restante dos funcionários. O cálculo através das demais rotinas continua funcionando normalmente, o diferencial desta tela é que será possível calcular todos os vínculos de uma só vez. 

**Principais Campos e Parâmetros  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084772933)**

**Identificadores** de Cálculo necessários:

|  |  |  |  |
| --- | --- | --- | --- |
| Id | Descrição | Tipo Cod | Tipo |
| 0236 | Base IR Férias Outos Períodos | Base Provento | Valor |
| 0237 | IR Férias Outros Períodos | Base Provento | Valor |
| 0288 | Salário Contribuição INSS Outras Empresas | Base Provento | Valor |
| 0289 | Desconto INSS Outras Empresas | Base Provento | Valor |
| 0290 | Base INSS 13º Outras Empresas | Base Provento | Valor |
| 0291 | INSS 13º Outras Empresas | Base Provento | Valor |
| 0396 | Base INSS Férias Outros Períodos | Base Provento | Valor |
| 0397 | INSS Férias Outros Períodos | Base Provento | Valor |
| 0992 | Base IR Outras Empresas | Base Provento | Valor |
| 0993 | IR Outras Empresas | Base Provento | Valor |
| 0994 | Base IR Outras Empresas 13º Salário | Base Provento | Valor |
| 0995 | IR Outras Empresas 13º Salário | Base Provento | Valor |
| 1847 | Base INSS Autônomo Outras Empresas | Base Provento | Valor |
| 1951 | Deduções modelo completo IR Folha no período anterior | Base Provento | Valor |

 

**Saiba Mais**  
[Manual do Cálculo de Multiplos Vinculos](https://tdn.totvs.com/pages/releaseview.action?pageId=552575179#ids-id1)  
**[RH - Calculo Autonomo/Prolabore](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983113-RH-Calculo-Autonomo-Prolabore)**  
**[Como configurar o cálculo de múltiplos vínculos na versão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027693112?source=search)**
