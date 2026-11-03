---
article_id: 360028555052
category: RH - Contabilização
content_hash: 763095d3e00519fada946d588d0cd10991b15400a07e35ac7eb710489628d015
fetched_at: '2026-06-28T22:43:45.812048+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Como contabilizar a folha de pagamento por Centro
  de Custo
type: support-article
updated_at: '2025-07-30T20:48:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028555052-RH-Linha-Protheus-GPE-Como-contabilizar-a-folha-de-pagamento-por-Centro-de-Custo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33832494584855)**Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como contabilizar a folha de pagamento por Centro de Custo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**1) Calcule a folha de pagamento (no exemplo abaixo, teremos 3 funcionários cadastrados em 3 centros de custos diferentes):   
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029653412)![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029653652)  
  
2) Configure um **lançamento padrão** para atrelar as verbas que deverão ser integradas ao processo de **contabilização**. Neste exemplo, configuramos um lançamento padrão e amarramos no **campo RV\_LCTOP** do cadastro das seguintes verbas, 112, 417, 419, 708, 748 , 749. **(Atualizações-> Definições de cálculo-> Verbas-> Aba contabilização-> Campo Lcto Padrão).**

**Importante:** Os lançamentos padrões configurados nos *prints* abaixo servem apenas para ilustrar o processo. Realize a **configuração de acordo com a regra de negócio da sua empresa**. Caso não tenha conhecimento na utilização do cadastro de Lançamento Padrão, solicite ao seu agente de relacionamento Totvs a visita de um analista in loco para avaliação.![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029647291)![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029647351)  
![mceclip15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029655592)  
![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029647711)

Mais **informações para configuração de lançamento padrão**, acesse:   
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021101152-MP-GPE-Como-configurar-Lan%C3%A7amento-Padr%C3%A3o-para-Folha-de-Pagamento-do-Protheus-?source=search>

3) No ambiente Gestão de Pessoal , acesse **Miscelânea-> Fechamentos -> Contabilização:**

![mceclip18.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029657832)

![mceclip22.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029685092)

4) Quando configurado no grupo de perguntas **Mostra lançamento = SIM**, os lançamentos de verbas contabilizadas serão apresentados na tela de acordo com a configuração do lançamento padrão por ordem de centro de custos:    
![mceclip21.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029684212)

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Como configurar Lançamento Padrão para Folha de Pagamento do Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021101152-RH-Linha-Protheus-GPE-Como-configurar-Lan%C3%A7amento-Padr%C3%A3o-para-Folha-de-Pagamento-do-Protheus-)
