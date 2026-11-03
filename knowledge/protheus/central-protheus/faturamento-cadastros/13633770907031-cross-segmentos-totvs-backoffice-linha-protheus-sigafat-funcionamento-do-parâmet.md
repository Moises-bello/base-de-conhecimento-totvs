---
article_id: 13633770907031
category: Faturamento - Cadastros
content_hash: 6ca411781ad97ba9bd7bdbc6b56ba64256de7e7c4620b98b254068758900367d
fetched_at: '2026-06-28T22:38:36.866287+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Funcionamento
  do parâmetro MV_1DUP
type: support-article
updated_at: '2024-09-25T20:47:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13633770907031-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Funcionamento-do-par%C3%A2metro-MV-1DUP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26628419868567) Tempo aproximado para leitura: **00:01:30 min**

**Dúvida**Qual o conceito e como utilizar o parâmetro MV\_1DUP?

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

O parâmetro MV\_1DUP determina se a contagem do campo E1\_PARCELA vai ser:

* Por letra ou número
* Limite das parcelas (segue a quantidade de carácteres do parâmetro)

Exemplo 1: MV\_1DUP = A ou 1

* Quantidade: 1 Caractere
* Limite se MV\_1DUP = A: A até Z (26 parcelas)
* Limite se MV\_1DUP = 1: 1 até 9 (9 parcelas)

Exemplo 2: MV\_1DUP = AA e 01

* Quantidade: 2 Caracteres
* Limite se MV\_1DUP = AA: AA até ZZ (100+ parcelas)
* Limite se MV\_1DUP = 01: 01 até 99 (99 parcelas)

Exemplo 3:

Gerando em um faturamento dois títulos/duplicatas com o parâmetro MV\_1DUP por letra ou por número

![fra1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/13633771453463)

![fra2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/13633771452823)

**Mais informações:**

[FIN0079\_Utilização do parâmetro MV\_1DUP](https://tdn.totvs.com/pages/releaseview.action?pageId=286197157)

**Saiba Mais**

Compreenda as regras e características gerais das Condições de Pagamento disponíveis no Protheus: **[FAT0089 - Condições de Pagamento](https://tdn.totvs.com/x/PdpSDg)**
