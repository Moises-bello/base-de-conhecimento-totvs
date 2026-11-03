---
article_id: 32109854540695
category: Escrita Fiscal - Configurador de Tributos
content_hash: dd4064348de59d31fe0399a964b67f3139a807df5fe38589638fccc1e216ec3c
fetched_at: '2026-06-28T22:39:17.742486+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 - Como calcular
  o Diferencial de alíquotas base dupla no Configurador de Tributos?
type: support-article
updated_at: '2025-11-03T18:36:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32109854540695-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-o-Diferencial-de-al%C3%ADquotas-base-dupla-no-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32109870537367) Tempo aproximado para leitura: 00:10**min** **Dúvida**Como calcular o Diferencial de alíquotas base dupla no Fisa170?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

MV\_estado = SP

Fornecedor = MG

Cadastro de Produtos  
NCM = 94033000  
origem = 0

TES  
CFOP = 1556  
Mat consumo = sim

Valor do Produto = 1000,00  
Base de calculo do ICMS = 1000,00 \*12% = 120,00  
Base de calculo do diferencial de alíquotas = 1000,00-120,00 = 880,00  
880,00/0,82 = 1073,17  
1073,17\*18% = 193,17-120,00= 73,17

Configurações no Fisa170

ID tributo = ICMS / CMP

Cadastro de Regra de NCM = 94033000  
ICMS = MG para SP - origem = 0 - Aliquota = 12%  
CMP = MG para SP - origem = 0 - Aliquota = 18%

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32109870538519)

**Perfis**

Perfil de Produto

SB1

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32109870541975)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32109854423447)

Perfil de Operação

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32109854424727)

Perfil de Participantes

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32109870547479)

Perfil de Origem x destino

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32109870549655)

**Regras de Base de Calculo**  
ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32109854432151)

CMP

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32109854433047)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32109854434071)

Regra de Alíquota

aliquota 18%

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32109870560407)

Aliquota ncm 9403.30.00

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32109870563223)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32109854442007)

Regra de Escrituração

ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32109854442391)

Regra de Calculo Documentos Fiscais

ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32109870567575)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32109854445207)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32109854446487)

CMP

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32109870583575)

Perfis os mesmos

Após salvar o perfil, alterar o detalhamento de cálculo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32109870591895)

Documento de entrada

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32109854456471)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32109870609559)

O valor será gravado no campo F3\_icmscom

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32109854474391)
