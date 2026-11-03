---
article_id: 38777174413463
category: Escrita Fiscal - Configurador de Tributos
content_hash: 43092a42592b0d2564e6d1d0953003146bd6ce965a573f4b2def4da8d564888a
fetched_at: '2026-06-28T22:39:17.563281+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS Como configurar o
  ICMS diferido 100% e gerar cBenef para SP?
type: support-article
updated_at: '2026-05-06T20:36:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38777174413463-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-ICMS-diferido-100-e-gerar-cBenef-para-SP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38777174380311) Tempo aproximado para leitura: 08:00**min**  
  
**Dúvida**  
Como configurar o ICMS diferido 100% e gerar cBenef para SP?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões

**Solução**

Calculo do icms diferido 100% pelo configurador de tributos e geração do cBenef para SP

Exemplo

Valor da mercadoria = 1000,00

Base de calculo do ICMS = 1000,00\*18% = 180,00

MV\_estado = SP

Cliente = SP

Cadastro de Produtos

Origem = 0

TES

CFOP = 5101

Calculo

ID tributos

ICMS

Regra NCM = 39232910

SP para SP - origem = 0 - aliquota 18%

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38777174381079)

Regra de Base de calculo

O:VAL\_mercadoria

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38777174384407)

Regra de aliquota

I:ALIQ\_NCM

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38777174385431)![](https://centraldeatendimento.totvs.com/hc/article_attachments/38777196836119)

Regra de escrituração

Incidencia = outros

Diferimento = 100

CST = 51

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38777174386711)![](https://centraldeatendimento.totvs.com/hc/article_attachments/38777196837143)

Regra de Calculo Documentos Fiscais = 000403

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38777174392215)![](https://centraldeatendimento.totvs.com/hc/article_attachments/38777196840855)![](https://centraldeatendimento.totvs.com/hc/article_attachments/38777174392983)

1a ) Pedido de Vendas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38777196841751)

Livro fiscal

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38777196842391)

Cj3

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38777196850455)

2a) Regra de Ajuste de lançamento

ICMS diferido = SP053600

Mensagem

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38777174397719)

O codigo precisa estar na rotina Fisa156

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38777196852119)

Cadastro Regra de ajuste Lançamento

Tabela 52 - SP053600 - inicio 01/01/2026 - regra tributária = 000403

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38777174402071)![](https://centraldeatendimento.totvs.com/hc/article_attachments/38777196853527)![](https://centraldeatendimento.totvs.com/hc/article_attachments/38777196854807)

Cbenef

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38777174403607)
