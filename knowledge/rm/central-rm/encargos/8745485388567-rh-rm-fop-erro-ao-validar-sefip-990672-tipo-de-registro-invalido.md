---
article_id: 8745485388567
category: Encargos
content_hash: af7d5f84cb7b88e34946b38bde1f4771b161b3033ed2153ca349fb82b49e2980
fetched_at: '2026-06-28T22:46:52.128087+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Erro ao validar SEFIP 990672 - Tipo de Registro Invalido
type: support-article
updated_at: '2025-08-07T14:12:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8745485388567-RH-RM-FOP-Erro-ao-validar-SEFIP-990672-Tipo-de-Registro-Invalido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:25 min****Dúvida**Como realizar a correção do erro 990672 - Tipo de Registro Invalido apresentado na validação da SEFIP?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para realizar a correção do erro apresentado na validação da SEFIP, deve-se validar os dados cadastrais da seção, ou dos dados do funcionário. Este erro pode ocorrer caso o arquivo **SEFIP** gerado esteja com espaços em branco em seu leiaute, causando assim o deslocamento das posições no arquivo. Estes espaços em branco em meio ao arquivo gerado são derivados de algum campo de **cadastro do funcionário** estar incorreto, com espaços em branco à mais.

Valide o leiaute do arquivo SEFIP, e valide a linha informada na mensagem de erro:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8745354585367/mceclip0.png)

Verifique as posições que estiverem com espaço em branco, fora do leiaute padrão, como no exemplo abaixo. Veja em que posição que o espaço incorreto está inserido, e isso demonstrará qual campo está incorreto no cadastro de funcionário

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019533652/mceclip2.png)

Após o ajuste, libere as flags de FGTS e gere um novo arquivo da **SEFIP,** por fim importe no validador.

**Saiba mais**  
[RH - RM - FOP - Liberação de Flags de FGTS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415143205143-RH-RM-FOP-Libera%C3%A7%C3%A3o-de-Flags-de-FGTS)
