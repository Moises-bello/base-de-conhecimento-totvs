---
article_id: 14522036989591
category: Encargos
content_hash: a4aa32225e50cdcb688d51ddbcc05a4392ac795cbda4aa1ad7ec39912494b346
fetched_at: '2026-06-28T22:46:52.332127+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Geração do encargo TIPO 5 - Provisão de FGTS de férias
type: support-article
updated_at: '2024-10-11T19:13:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14522036989591-RH-RM-FOP-Gera%C3%A7%C3%A3o-do-encargo-TIPO-5-Provis%C3%A3o-de-FGTS-de-f%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min****Dúvida**Como gerar o encargo TIPO 5 - Provisão de FGTS de férias ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Solução**Para geração do encargo TIPO 5 - Provisão de FGTS de férias, o sistema irá considerar para o calculo a provisão do mês atual - provisão do mês anterior multiplicado ao valor que estiver informado no cadastro do encargo dividido por 100:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14834653227031)

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/14521729543447)**

**Importante:** O parâmetro **Arredonda FGTS conforme SEFIP** nos parâmetros de cálculo do RM Labore, interfere nos cálculos de arredondamento dos encargos de FGTS. O parâmetro **Arredonda FGTS conforme SEFIP** marcado têm prioridade sobre o parâmetro **Aplicar arredondamento sobre o valor total do encargo**, também marcado, durante a contabilização. Os tipos de encargos afetados são:  
2 - Base: incidência de FGTS  
5 - Provisão de FGTS de férias  
8 - Provisão de FGTS de 13o. salário  
M - Base: incidência de FGTS de 13o. salário

Para geração do encargo | geração de encargos é necessário verificar o código ativo associado ao encargo pois na hora de gerar será necessário selecionar o mesmo código ativo associado no cadastro:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14521911162647)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14521913068695)

Log da geração:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14521932740631)

**Saiba mais**[Encargos - Folha de Pagamento](https://tdn.totvs.com/display/public/LRM/Encargos+-+Folha+de+Pagamento)  
[RH - RM - FOP - Encargos: Criação de códigos ativos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021841391-RH-RM-FOP-Encargos-Cria%C3%A7%C3%A3o-de-c%C3%B3digos-ativos)
