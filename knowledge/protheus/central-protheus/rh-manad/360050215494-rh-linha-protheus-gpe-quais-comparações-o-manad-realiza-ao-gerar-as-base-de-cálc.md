---
article_id: 360050215494
category: RH - MANAD
content_hash: fafef765850d3814fe3e1775ca0b6c3a34e6971cb4e088d88cdb0a1d2f9a41bb
fetched_at: '2026-06-28T22:43:33.822562+00:00'
product: protheus
section_id: 360008157193
source: central-protheus
title: RH - Linha Protheus - GPE - Quais comparações o MANAD realiza ao gerar as base
  de cálculo referentes à Previdência social, IRRF e FGTS?
type: support-article
updated_at: '2021-04-06T20:21:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050215494-RH-Linha-Protheus-GPE-Quais-compara%C3%A7%C3%B5es-o-MANAD-realiza-ao-gerar-as-base-de-c%C3%A1lculo-referentes-%C3%A0-Previd%C3%AAncia-social-IRRF-e-FGTS
---

**Dúvida**Quais comparações o MANAD realiza ao gerar as base de cálculo referentes à Previdência social, IRRF e FGTS?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Solução:**O sistema faz comparações das bases de cálculo da época com o cadastro atual de rubricas (verbas).

Após o fechamento da folha , as verbas serão gravadas e armazenadas no acumulado mensal ( tabela SRD) com as informações de incidência calculadas da competência.

Ao gerar o MANAD, o sistema busca os valores de base calculo do acumulado e compara com o cadastro atual de verbas. Veja na imagem abaixo a visualização do acumulado de um determinado mês:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077666013/mceclip0.png)  
  
Verificaremos agora, o cadastro de verba atual:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076519534/mceclip1.png)  
  
No validador SVA do MANAD , será apresentada divergência , se alguma das verbas calculadas estiverem com incidência diferente da época do cálculo.   
  
**Saiba Mais**[Artigos sobre Manad](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360008157193-RH-MANAD)
