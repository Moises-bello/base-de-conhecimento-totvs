---
article_id: 15661638818583
category: eSocial - Eventos Totalizadores
content_hash: 552967e472103ea5711edcb71c6c72bdca4fcd2d91283730f49bbb08f2ae37c5
fetched_at: '2026-06-28T22:47:07.019310+00:00'
product: rm
section_id: 1500000834481
source: central-rm
title: RH - RM - FOP - eSocial - Como identificar o valor gerado do consolidado do
  Rendimento não tributável ou isento do IRRF - 7900 no governo?
type: support-article
updated_at: '2024-06-05T11:58:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15661638818583-RH-RM-FOP-eSocial-Como-identificar-o-valor-gerado-do-consolidado-do-Rendimento-n%C3%A3o-tribut%C3%A1vel-ou-isento-do-IRRF-7900-no-governo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15661622790679) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como identificar o valor gerado do consolidado do Rendimento não tributável ou isento do IRRF - 7900 no governo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**O Rendimento não tributável ou isento do IRRF **7900 - Verba transitada pela folha de pagamento de natureza diversa de rendimento ou retenção/isenção/dedução de IR (exemplo: desconto de convênio farmácia, desconto de consignações, etc,** é obtido pelo o governo através do cadastro de rubricas que possuem incidência de IRRF 09.

Para solucionar essa dúvida, realize os seguintes passos:  
1. Identifique no governo todas as rubricas que compõem o XML de remuneração que foi encaminhado. No governo acesse Empregador - Tabelas - Rubricas;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15661602994839)

2. Após identificar todas as rubricas que possuem incidência 09, será necessário realizar o calculo abaixo.  
2.1. Some todas as rubricas de proventos (**Venc.**);

2.2. Some todas as rubricas de base (**Inf.**);

2.3. Some todas as rubricas de desconto (**Desc.**);

2.4. O valor será obtido através do cálculo: Venc. + Inf. - Desc. = Consolidado 7900.

3. Caso seja necessário alterar a incidência de alguma rubrica, encaminhe um S-1010 de alteração para o governo com as devidas correções.

**Importante**

* Caso seja necessário corrigir a incidência da rubrica no governo, ao criar o novo gatilho S-1010 no RM verifique se é necessário ajustar o início de validade da verba, caso sim, basta alterar o campo **Competência** dentro do gatilho para o mês/ano desejado e, após, gerar o XML.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15662148669719)

* No mapeamento da TOTVS consta a parametrização do evento para que o XML S-1010 seja gerado com a *tag*codIncIRRF = 09

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15662241109783)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/15662251161495)

**Saiba mais**  
Para maiores informações, acesse:

[Mapeamento Evento S-1010](https://tdn.totvs.com/display/public/LRM/Evento+S-1010)
