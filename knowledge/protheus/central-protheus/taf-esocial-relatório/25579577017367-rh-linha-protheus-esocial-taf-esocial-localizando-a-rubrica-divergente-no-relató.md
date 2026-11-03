---
article_id: 25579577017367
category: TAF - eSocial - Relatório
content_hash: 8f01eac0412494f128348f89a98302e8337bbccf8b4eceaabb859e5b7a6f2df8
fetched_at: '2026-06-28T22:45:19.904053+00:00'
product: protheus
section_id: 1500001536821
source: central-protheus
title: RH (Linha Protheus) - eSocial - TAF eSocial - localizando a rubrica divergente
  no relatório de conferência
type: support-article
updated_at: '2026-06-18T12:12:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25579577017367-RH-Linha-Protheus-eSocial-TAF-eSocial-localizando-a-rubrica-divergente-no-relat%C3%B3rio-de-confer%C3%AAncia
---

**Dúvida**Como localizar a rubrica que está dando divergência no relatório de conferência?  
  
**Ambiente**TOTVS RH  - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Todas as versões  
  
**Solução**  
1.  Localize um dos CPFs divergentes no relatório de conferência seja no INSS - FGTS **(gerando o relatório como somente divergente)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25583143113623)**

Cenário do Valor que está faltando no relatório **como exemplo:**

**Valor a menos.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25579577007255)

2.  Validando a divergência na coluna TAF, gere o XML do **TAF** de um dos CPFs do **(S-1200/S-2299)**

[RH - Linha Protheus - TAF - eSocial - Configuração - Como gerar XML de retorno dos eventos no TAF, e o XML do TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046869313-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-Como-gerar-XML-de-retorno-dos-eventos-no-TAF-e-o-XML-do-TAF)

 3.  Abra o XML e localize o valor que deveria constar no relatório

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25579893526935)

4.  Encontrando o valor e sua Rubrica, valide o detalhamento da rubrica se consta a natureza de rubrica e incidência do relatório

[RH - Linha Protheus - TAF - eSocial - Eventos de tabelas - Como validar o cadastro de um evento de rubrica no TAF (S-1010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25509916713495-RH-Linha-Protheus-TAF-eSocial-Eventos-de-tabelas-Como-validar-o-cadastro-de-um-evento-de-rubrica-no-TAF-S-1010)

5. Caso a divergência for um valor a mais na coluna TAF do que na coluna governo

**Valor a mais.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25580903325335)

Valide no XML do S-1200/S-2299 qual valor que está vindo a mais comparado com o valor governo, verifique a rubrica que está para este valor a mais, e se a mesma está cadastrada com a natureza e incidência para aparecer no relatório.

Exemplo de duas rubricas que tem a natureza e incidência de INSS que a soma dos valores está aparecendo na coluna do TAF

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25590827354007)
