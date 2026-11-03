---
article_id: 360035071694
category: GPE - eSocial - Periódicos
content_hash: 60557812ea51bdaae393b2493011e182da226e1bbef3a95142560b02eadc75cb
fetched_at: '2026-06-28T22:45:09.973036+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema não cria as TAGs de remuneração outras
  empresas no S-1200 ao lançar os ids 0289 e 0288 nos valores fixos
type: support-article
updated_at: '2025-07-28T16:52:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035071694-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-cria-as-TAGs-de-remunera%C3%A7%C3%A3o-outras-empresas-no-S-1200-ao-lan%C3%A7ar-os-ids-0289-e-0288-nos-valores-fixos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27476411059479)Tempo aproximado para leitura: **00:02:00min  
  
Dúvida**Como gerar as TAGs de remuneração outras empresas no S-1200 ao lançar os ids 0289 e 0288 nos valores fixos?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para que o sistema gere a *tag* de remuneração outras empresas no S-1200 nos próximos meses deve-se informar a **data início**, campo Dt. Ini. Pgto (**RG1\_DINIPG)**, e a **data fim**, campo Dt. Fim. Pagto (**RG1\_DFIMPG**).  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27476417669911)

Ao salvar o registro no lançamentos fixos, serão criados todos os registros nas tabelas **RAW** e **RAZ**, do período inicial informado no campo Dt. Ini Pagto até o período final informado no campo Dt. Fim. Pagto, com isso, na integração do S-1200, sistema pegará essas informações e criará as TAGs da remuneração outras empresas indicando que o funcionário é múltiplos vínculos na rotina **GPEA924** (visualização dados de múltiplos vínculos) com o indicativo de múltiplo vinculo na *tag* **IndMV** e os dados do outros empregadores, conforme imagem de exemplo abaixo. E essa mesma informação será gerada no **S-1200** do trabalhador.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31672449400599)  
  
Caso necessite visualizar ou fazer manutenção na rotina **GPEA924** (visualização dados de múltiplos vínculos) acesse o artigo: **[S-1200 - Para que serve e como realizar ajustes na rotina GPEA924 para Múltiplos Vínculos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029145033)**

**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)  
  
Para conhecimento dos eventos futuros, acessa a nossa página *[TOTVS Informa](https://informa.totvs.com/)* selecione em categorias a área e pesquise por "Eventos".
