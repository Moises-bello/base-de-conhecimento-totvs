---
article_id: 9980688678423
category: RH - Férias
content_hash: 4f116a01ee322b17ef5b5e72d0fd25e050784f1ddf46defa9366bf4c4fec217a
fetched_at: '2026-06-28T22:43:58.324396+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - No cálculo de Férias o valor de IRRF não está considerando
  o arredondamento na 3ª casa decimal
type: support-article
updated_at: '2025-09-12T16:49:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9980688678423-RH-Linha-Protheus-GPE-No-c%C3%A1lculo-de-F%C3%A9rias-o-valor-de-IRRF-n%C3%A3o-est%C3%A1-considerando-o-arredondamento-na-3%C2%AA-casa-decimal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26489051505559) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**  
Por que no cálculo de Férias o valor de IRRF não está considerando o arredondamento na 3ª casa decimal?  
**Exemplo:**  
Base IR: **R$ 3.331,16**  
Desconto IR (7,5%): **R$** **22,137**  
Desconto da verba de IR nas Férias: **R$** **22,13**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32646237779223)

**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - Todas as versões

**Solução**Atualmente, o sistema apenas **trunca os valores** sem aplicar regras específicas de arredondamento.  
**Não há disposições legais** que determinem uma regra sobre truncamento ou arredondamento do IR.  
Como a **Lei Orgânica do INSS** **também não estabelece regras** para ajustes de casas decimais nos cálculos do tributo e o INSS pode ser deduzido do IRRF (dependendo do modelo de cálculo utilizado), a recomendação é que o tratamento sistêmico para o valor seja equivalente para o IR.

**Saiba Mais**[RH - Linha Protheus - GPE - Configuração do parâmetro MV\_DINSSFM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016451652-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-do-par%C3%A2metro-MV-DINSSFM)  
[RH - Linha Protheus - GPE - O que analisar quando o Valor do INSS ou IRRF de Férias estão Incorretos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024709574-RH-Linha-Protheus-GPE-O-que-analisar-quando-o-Valor-do-INSS-ou-IRRF-de-F%C3%A9rias-est%C3%A3o-Incorretos)  
[RH - Linha Protheus - GPE - Sistema não gera valor de dedução de dependente de IR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11283264869271-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-gera-valor-de-dedu%C3%A7%C3%A3o-de-dependente-de-IR)
