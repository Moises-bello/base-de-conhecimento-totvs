---
article_id: 27540576188695
category: TAF - GIA
content_hash: 19c9edfa3a24d4e346c10f43d3f13a1a12b235b7b5204cb519d37ea5162c777f
fetched_at: '2026-06-28T22:41:32.383262+00:00'
product: protheus
section_id: 1500001547982
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - GIA - Campo Imposto Inconsistente
  inconsistente.
type: support-article
updated_at: '2024-11-04T15:01:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27540576188695-Cross-Segmentos-Backoffice-Protheus-TAF-GIA-Campo-Imposto-Inconsistente-inconsistente
---

**Ocorrência**

Arquivo da **GIA/ SP**, gerado pelo **TAF** apresenta erro ao ser importado no validador **"Campo imposto inconsistente, posições \*\*\*\*\*"**.

![4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27540576147607)

**Ambiente**Cross segmento - TOTVS BackOffice (Linha Protheus) - TOTVS Automação Fiscal - Todas as versões.

**Causa**

O incidente é causado devido á escrituração divergente, fazendo com que a composição dos valores do **CR14** seja diferente dos valores do **CR10**.

**Solução**

Exemplo abaixo do cenário e como realizar correção

1° Faça o cálculo dos valores do **CR10** e **CR14**, para identificar a diferença dos valores, seguindo o **Manual de Orientação da GIA**.

*Print*:

![1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27540581760791)

  Valores do **CR10**, conforme exemplo do arquivo gerado do *print* acima.

|  |  |
| --- | --- |
| Valor contábil | R$   210.230,53 |
| Base de calculo | R$  210.230,53 |
| IMPOSTO | R$     24.576,45 |

 Valores do **CR14**, conforme exemplo do arquivo gerado do *print* acima.

|  |  |
| --- | --- |
| BASE | R$   200.523,78 |
| IMPOSTO | R$     23.411,63 |

 No arquivo acima foi identificada diferença de:

|  |  |
| --- | --- |
| Diferença | R$        1.164,82 |

Localize a diferença nos valores e identifique quais os documentos estão gerando a diferença, faça a consulta da *query* abaixo no seu **Banco**, para identificar todos documentos considerados para o **CFOP** apresentado no **CR10**.

*Query* etapa 2 do KCS abaixo:

[Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Nova GIA - Arquivo em Branco ou com Valores Incorretos.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048358774-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Nova-GIA-Arquivo-em-Branco-ou-com-Valores-Incorretos)

Apresentado o resultado da *query* salve em "**Excel**", com o arquivo deve ser filtrada a linha correspondente a **UF de destino**.

![2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27540576152471)

Confirme se a **UF** apresentada está correta conforme o **CFOP** utilizado, realize um De x Para com a tabela **C09** validando se a **CFOP** é correspondente a **UF** (Estadual ou Interestadual), neste arquivo foi gerado **CFOP 6352** Para Notas Fiscais de **SP**.

![3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27540576156567)

A diferença foi gerada por ter Notas interestadual **CFOP 6352**, com **UF de SP**, com isso não foi considerado no arquivo esses documentos, tendo em vista que **SP** não representa **CFOP** iniciado por **"6"** **(interestadual)**.

**Analise adicional:**

Identificada a Relação (*print* excel) de Notas Fiscais divergente, faça o cálculo validando se os valores das notas corresponde a diferença estre o **CR14** - Valor do Imposto e **CR10** - Imposto, corrija os documentos divergente na rotina **Doc. de entrada** (**TAFA062E**) ou **Doc. de saída** (**TAFA062S**) e extraia o arquivo novamente para correção.

Abaixo outra possibilidade de erro na integração aonde será gerado arquivo com diferença no valor entre **CR10 e CR14.**

Ao executar o **Extrator ou integrar via TSI**, foi gerado erro na integração do documento (***layout* T013**) o erro deve ser identificado, corrigido e refeita integração.

[Cross Segmentos - Backoffice Protheus - TAF - REINF - Como consultar o gerenciador de integração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043361753-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-consultar-o-gerenciador-de-integra%C3%A7%C3%A3o)
