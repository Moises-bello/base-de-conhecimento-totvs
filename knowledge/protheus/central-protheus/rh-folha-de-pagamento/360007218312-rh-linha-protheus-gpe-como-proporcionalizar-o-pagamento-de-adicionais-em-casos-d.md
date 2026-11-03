---
article_id: 360007218312
category: RH - Folha de Pagamento
content_hash: f944bf06c15c6988566ec8eb92f3138f96d8de6cc23b40c7b3871ea5cce214ae
fetched_at: '2026-06-28T22:44:14.696322+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como proporcionalizar o pagamento de adicionais
  em casos de afastamento
type: support-article
updated_at: '2026-04-14T13:12:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007218312-RH-Linha-Protheus-GPE-Como-proporcionalizar-o-pagamento-de-adicionais-em-casos-de-afastamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31586773994391) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**  
Como proporcionalizar o pagamento de adicionais, quando o funcionário tem afastamento?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
  
**1.** Acesse **Atualizações > Definições de Cálculo > Tipos de Ausência** (**GPEA430**), Localize a Ausência do funcionário e clique em **Alterar**;  
**2.** Altere o conteúdo do campo "**Calc. Pr. Adic**" (RCM\_PROADI) de acordo com a orientação abaixo.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084760093)

Informe '**2=Não**' para que o cálculo proporcione o valor dos adicionais conforme os afastamentos ou '**1=Sim**' para que não proporcione.  
  
**Exemplo**  
Funcionário afastado de 01/07/2017 à 03/07/2017.  
  
Ao preencher o campo **RCM\_PROADIC** com **2=Não** , para que o cálculo dos adicionais sejam pagos os dias trabalhados mais os dias de afastamento, nesse caso 31 dias.

Ao preencher o campo **RCM\_PROADIC** com **1=Sim**, serão pago apenas sobre os dias trabalhados, nesse caso 28 dias

**Atenção**  
Válido para todos os tipos de ausências exceto a do tipo **4=Controle de Dias de Direito**.  
  
**3.** Confirme a alteração;  
**4.** Inclua a ausência para o Funcionário, através do menu **Atualizações > Lançamentos > Ausência** **(GPEA240)**;  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084766413)  
  
**Importante**  
Referente ao **Depósito do FGTS**, caso seja calculado pelos dias pagos ou calculo integral, informe no campo **Depos. FGTS** conforme imagem abaixo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048575313)

**Saiba Mais**  
[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019172351-MP-GPE-Pagamento-de-adicionais-nos-primeiros-15-dias-de-afastamento?source=search)
