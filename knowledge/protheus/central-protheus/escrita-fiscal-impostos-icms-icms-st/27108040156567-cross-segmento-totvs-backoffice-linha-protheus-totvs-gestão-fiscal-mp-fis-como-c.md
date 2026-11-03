---
article_id: 27108040156567
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: 4242648896711cf6144b2f074eb12817db5fae7d4a44cbce610fd1001645699d
fetched_at: '2026-06-28T22:39:20.341460+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal -
  MP FIS Como configurar o calculo do ICMS ST Importação origem do EIC
type: support-article
updated_at: '2024-10-16T14:02:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27108040156567-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Gest%C3%A3o-Fiscal-MP-FIS-Como-configurar-o-calculo-do-ICMS-ST-Importa%C3%A7%C3%A3o-origem-do-EIC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27108040138007) Tempo aproximado para leitura: 03:00**min** **Dúvida** Como configurar o calculo do ICMS ST Importação origem do EIC

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Para obter o cálculo de ICMS – ST considerando as movimentações geradas pelo Módulo SIGAEIC, quando o campo Agrega Valor (F4\_AGREG) possuir preenchimento = B, observe a configuração do parâmetro a seguir:

**MV\_TIPOB** = Informe os Estados que deverão realizar o cálculo do ICMS-ST, quando for utilizado o tipo B do TES.

* Descrição do Tipo B: O valor da mercadoria não contém o valor do ICMS, portanto, os valores do ICMS e da mercadoria serão agregados ao total do documento. Este agregador de valor não calcula nenhum imposto, portanto mantém o que for informado pelo usuário ou transmitido por outro sistema.

TES

Calcula icms = não

L fiscal icms = de acordo com a sua necessidade

Agrega valor = B

Sit trib icms = 10

Calcula ipi = não

L fiscal ipi = de acordo com a sua necessidade
