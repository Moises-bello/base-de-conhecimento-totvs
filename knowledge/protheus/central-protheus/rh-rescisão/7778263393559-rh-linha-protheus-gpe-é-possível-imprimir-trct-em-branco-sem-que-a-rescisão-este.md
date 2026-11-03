---
article_id: 7778263393559
category: RH - Rescisão
content_hash: d82421c065556451208af16e94be3ba3bd741a5c9cc825fee52df796cbfa1190
fetched_at: '2026-06-28T22:43:52.154135+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - É possível imprimir TRCT em branco sem que a rescisão
  esteja calculada
type: support-article
updated_at: '2025-05-21T11:24:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7778263393559-RH-Linha-Protheus-GPE-%C3%89-poss%C3%ADvel-imprimir-TRCT-em-branco-sem-que-a-rescis%C3%A3o-esteja-calculada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18075066015511) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**É possível imprimir TRCT em branco sem que a rescisão esteja calculada ao realizar a demissão direto no cadastro de Funcionários?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**Não é possível, para impressão do TRCT deve existir o cálculo da rescisão pela rotina de rescisão, pois mesmo que não tenham valores a serem pagos, será calculado o ID 0318, então será possível imprimir o TRCT zerado.

**Exemplo:**

**Cálculo rescisão zerada somente com o id 0318.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18074800406679)

**Em parâmetros TRCT deixe com Sim em Imp. Disc. Verb Resc.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18074907712791)

**Deste modo o TRCT é gerado zerado.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18075056799383)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18075078247447)

**Saiba mais**Para adquirir maior conhecimento acesse os *links* abaixo:

<http://www.normaslegais.com.br/legislacao/portaria-mte-1057-2012.htm>
