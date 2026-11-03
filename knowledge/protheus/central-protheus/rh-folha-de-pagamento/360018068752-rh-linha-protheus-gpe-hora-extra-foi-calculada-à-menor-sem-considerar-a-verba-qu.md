---
article_id: 360018068752
category: RH - Folha de Pagamento
content_hash: 0ef094e1afd37173581bf9790a6e14e0791af1ae8a81fd86a145097c5e7eafb4
fetched_at: '2026-06-28T22:44:14.976494+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Hora Extra foi calculada à menor, sem considerar
  a verba que Incorpora ao salário, quando utilizada a função FGERAVERBA
type: support-article
updated_at: '2025-04-15T14:29:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018068752-RH-Linha-Protheus-GPE-Hora-Extra-foi-calculada-%C3%A0-menor-sem-considerar-a-verba-que-Incorpora-ao-sal%C3%A1rio-quando-utilizada-a-fun%C3%A7%C3%A3o-FGERAVERBA
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26329334670871) Tempo aproximado para leitura: 00:04:00 min**

**Dúvida**

No módulo **SIGAGPE**, o Cálculo da Hora Extra não está considerando o valor do salário + a verba que Incorpora salário, deixando o valor da hora extra à menor.    
Obs. A verba que incorpora  ao salário não possui Identificador de Cálculo e é gerada por meio da função FGERAVERBA.  
 **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Esse incidente ocorre, pois a parametrização está  incorreta na função FGERAVERBA.  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse a rotina  **Atualizações>Definições de Cálculo> Biblioteca de Funções:**

Pesquise por **FGERAVERBA -**Nesse cadastro  é possível notar quais variáveis estão disponíveis nessa fórmula, deve ser avaliado qual ou quais variáveis serão utilizadas, de forma que atenda à necessidade de cálculo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013602131)

2. Acessar a fórmula **FGERAVERBA** e incluir os parâmetros, de acordo com o cálculo desejado.  
Exemplo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013754171)

3. Calcular a folha de pagamento em **Miscelânea> Cálculo por Roteiro, depois visualizar o cálculo.****Detalhamento do Cálculo**

\* Regra para cálculo da Produtividade >>>>  Salário \*4% = R$2.525,47 \* 4% = 101,02

\* Salário Incorporado >>>> 2.626,49  
  
Na folha desse funcionário são  21 dias trabalhados + férias, o cálculo foi realizado da seguinte maneira:

**- Verba 101 Produtividade>>** Salário R$2.525,47 \* 4% /30 \* 21 dias = 70,71

**- H. extra 50%>>** Salário Incorporado R$ 2.626,49/200 horas\*50% \* 10 horas extras = 196,99

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013739572)**

Saiba mais nos links abaixo:

**[Exemplo da função FGERAVERBA()](http://tdn.totvs.com/display/public/PROT/GPE026FORMU_EXEMPLO+FGERAVERBA__P12#)**

<https://tdn.totvs.com/pages/releaseview.action?pageId=396661574>

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
