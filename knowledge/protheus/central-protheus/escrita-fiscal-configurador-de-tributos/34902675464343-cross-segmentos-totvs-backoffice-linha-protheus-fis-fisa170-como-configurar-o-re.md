---
article_id: 34902675464343
category: Escrita Fiscal - Configurador de Tributos
content_hash: b68da592e60de94104117c93bbdc42cf3a17feb01766df8e136715213ae548fd
fetched_at: '2026-06-28T22:39:17.762074+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 - Como configurar
  o Reflexo para Diferencial de alíquotas no RJ?
type: support-article
updated_at: '2025-09-12T21:09:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34902675464343-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-configurar-o-Reflexo-para-Diferencial-de-al%C3%ADquotas-no-RJ
---

**Dúvida**  
Como configurar o Reflexo para Diferencial de alíquotas no RJ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

MV\_estado = RJ

Fornecedor = SP

Valor da mercadoria = 250,00

base de calculo do icms = 250,00\*12% = 30,00

base de claculo do diferencial de aliquotas = 282,05\*22% = 32,05

Base de calculo do fecp = 282,05\*2% = 5,64

RJ700000002 - Diferencial de aliquotas sobre material de consumo = 26,41

RJ700000006- Fecp sobre diferencial de aliquotas = 5,64

Regra de Ajuste de Lançamento

Cadastro da mensagem para gerar o C195/C197

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34902631480983)

Regra de Ajuste de lançamento do FECP sobre o diferencial de aliquotas

RJ700000006- Fecp sobre diferencial de aliquotas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34902631482519)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34902631486103)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34902631486871)

Regra de Ajuste de lançamento sobre o Diferencial de aliquotas sem o FECP

Criar uma regra sem a majoração do FECP

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34902675445655)

Sem regra de escrituração

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34902675446039)

RJ700000002 - Diferencial de aliquotas sobre material de consumo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34902631489175)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34902631490071)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34902631490839)

Lançamento da nota fiscal de entradas / aba - lançamento da apuração

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34902631491479)

Apuração do ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34902631492247)
