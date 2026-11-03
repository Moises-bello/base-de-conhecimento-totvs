---
article_id: 40742035428631
category: TAF - eSocial - Eventos Periódicos
content_hash: 7ae8dbd15b5171eb2741ef5202ba8e0891c9a13b7f9ef51467b9c8a341a1ac48
fetched_at: '2026-06-28T22:45:19.061195+00:00'
product: protheus
section_id: 1500001536901
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - Eventos Periódicos - S-1200/S-2299 Erro
  de schema: Element ''{http://www.esocial.gov.br/schema/evt/evtRemun/v_S_01_03_00}codRubr'
type: support-article
updated_at: '2026-05-26T18:44:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40742035428631-RH-Linha-Protheus-TAF-eSocial-Eventos-Peri%C3%B3dicos-S-1200-S-2299-Erro-de-schema-Element-http-www-esocial-gov-br-schema-evt-evtRemun-v-S-01-03-00-codRubr
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40742035395863) Tempo aproximado para leitura: **01:30:10 min**  
  
**Ocorrência:**

**Erro de schema ao transmitir S-1200 ou S-2299:**

Erro de schema: Element '{http://www.esocial.gov.br/schema/evt/evtRemun/v\_S\_01\_03\_00}codRubr': [facet 'minLength'] The value has a length of '0'; this underruns the allowed minimum length of '1'.  
Element '{http://www.esocial.gov.br/schema/evt/evtRemun/v\_S\_01\_03\_00}codRubr': [facet 'pattern'] The value '' is not accepted by the pattern '.[^\s].'.

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Eventos periódicos - Todas as versões  
  
**Solução**

O erro de schema acontece pois ao transmitir o evento que leva informações de folha de pagamento está faltando o preenchimento de alguma rubrica.

1. Para validar, clique nos 3 pontos do lado do evento rejeitado e depois em Editar Registro

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40742035397271)

2.  Acesse a aba do demonstrativos de valores e selecione o demonstrativo correto

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40742019272215)

Depois selecione a aba 'Informações relativas a remuneração do trabalhador no período de apuração'

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40742019273879)

Procure o valor que tem a informação de rubrica em branco, conforme exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40742035403927)

3. Após localizar o valor que está sem a rubrica, e acrescente a rubrica manualmente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40742035405591)

4. Depois só confirmar e transmitir novamente o evento

Obs: Outra solução seria integrar o S-1200/2299 do ERP de origem para o TAF para sobrepor esse que ficou sem a informação da rubrica.

**Saiba Mais**

Para saber mais consulte os links abaixo:

[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)

[Centralizadora TAF](https://tdn.totvs.com/display/public/TAF/Centralizadora+TAF)

[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)

[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)

*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e pesquise por "**Eventos**"*

Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
