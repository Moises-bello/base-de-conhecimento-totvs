---
article_id: 36104242403479
category: SIGAACD - Automação e Coleta de Dados
content_hash: 1d2e04d94eb476361e2553db123caf8f50412ee521b8ba09746ea8276980aa96
fetched_at: '2026-06-28T22:39:11.037472+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Quais critérios para
  gerar conferência na Pré-Nota ou Nota Fiscal
type: support-article
updated_at: '2025-11-04T20:33:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36104242403479-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Quais-crit%C3%A9rios-para-gerar-confer%C3%AAncia-na-Pr%C3%A9-Nota-ou-Nota-Fiscal
---

A conferência física nas rotinas de Pré-Nota ou Documento de Entrada no TOTVS Protheus é controlada pelo parâmetro MV\_CONFFIS. O tipo de conferência é definido pelo parâmetro MV\_TPCONF, com exceções no cadastro do fornecedor via campo A2\_CONFFIS. Para Pré-Nota, MV\_CONFFIS deve estar habilitado e A2\_CONFFIS configurado como 1. Para Documento de Entrada, MV\_CONFFIS habilitado, A2\_CONFFIS como 0, MV\_TPCONF configurado para nota fiscal e TES com F4\_ESTOQUE marcado como SIM.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36104242385815) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**  
Quais critérios para gerar conferência física nas rotinas de Pré-Nota ou  Documento de Entrada?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
Esta rotina controla o material recebido, realizando a leitura do código de barras, conferindo com os dados da Pré-Nota de Entrada ou documento de entrada , verificando inconsistências e/ou realizando a entrada física dos materiais.

Para habilitar a conferência física é necessário configurar o parâmetro [MV\_CONFFIS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/235302467-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Par%C3%A2metros-SX6-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados) (S)

O tipo de conferência é informada no parâmetro **MV\_TPCONF** (Indica se a conferencia física será realizada na Pre-Nota ou na Nota Fiscal de Entrada. O valor default (padrão) desse parâmetro será Pre-Nota).

Porém as exceções são informada no cadastro do Fornecedor  no campo **A2\_CONFFIS** conforme a imagem:

![image.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36104226008983)

Caso a conferência seja na Pré-Nota de entrada, basta habilitar o parâmetro **MV\_CONFFIS**, e o cadastro do fornecedor no campo **A2\_CONFFIS** configurado 1(Pré-Nota).

Caso a conferência seja no Documento de Entrada, é necessário habilitar o parâmetro **MV\_CONFFIS**, o cadastro do fornecedor configurado 0 (Parâmetro) e o parâmetro **MV\_TPCONF**(3 nota fiscal), no cadastro da TES de entrada o campo "Atu. Estoque" (**F4\_ESTOQUE**) deve estar com conteúdo "S-Sim".

**Saiba Mais:**

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)  
[Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Notas de Beneficiamento caindo em processo de Conferência.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35790608732695-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Notas-de-Beneficiamento-caindo-em-processo-de-Confer%C3%AAncia)
