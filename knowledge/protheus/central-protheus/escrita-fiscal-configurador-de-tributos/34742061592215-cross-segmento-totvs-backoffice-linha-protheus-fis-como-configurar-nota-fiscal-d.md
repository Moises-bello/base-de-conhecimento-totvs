---
article_id: 34742061592215
category: Escrita Fiscal - Configurador de Tributos
content_hash: b620edb015e7d16a35f1e94659f7ae3e801636d3184a8559a4c2e9558c25d5dd
fetched_at: '2026-06-28T22:39:17.220475+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como configurar
  nota fiscal de importação pelo Configurador de Tributos?
type: support-article
updated_at: '2026-01-12T20:37:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34742061592215-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-nota-fiscal-de-importa%C3%A7%C3%A3o-pelo-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34742045885847) Tempo aproximado para leitura: **00:15:00 min**  
  
**Dúvida**  
Como configurar nota fiscal de importação pelo Configurador de Tributos?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - a partir da versão 12.1.2310  
  
**Solução**

NF de importação

MV\_ESTADO = PR

Fornecedor = EX

TES

CFOP = 3102

Gera duplicata = sim

Valor da importação = 10.000,00

II = 16%

IPI = 3,25%

PIS = 2,10%

COF = 9,65%

ICMS = 12%

despesa = 250,00

Id tributos

II

ICMS

IPI

PIS

COF

Regra de NCM

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742061565719)

Majoração das alíquotas do PIS / COFINS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742045886103)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742045886743)

**Perfil de Produtos**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742045886871)

**Perfil de Operação**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742045888023)

**Perfil de Participantes**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742061568407)

Sa2

Tipo = outros

estado = EX

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742061568791)

Perfil de Origem x destino

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742061568919)

Imposto de Importação - II

Regra de base de cálculo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742061569175)

Regra de alíquota

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742045888663)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742045889047)

Regra de escrituração

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742045889431)

Regra de Calculo Documentos Fiscais do II

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742045890967)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742061570455)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742045893527)

Regra de Base de calculo do IPI

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742061571479)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742061571991)

Regra de aliquota

a mesma

Regra de escrituração

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742045896087)

Regra de Calculo Documentos Fiscais - IPI

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742045896471)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742061573015)

Perfis os mesmos

Regra de Base de calculo do PIS/COFINS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742045896855)

Regra de alíquota do PIS / COFINS

I:ALIQ\_NCM

Regra de Escrituração PIS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742045896983)

Regra de Escrituração COFINS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742061573655)

Regra de Calculo Documentos Fiscais - PIS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742045897495)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742045897751)

Perfis os mesmos

Regra de Calculo Documentos Fiscais - COFINS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742045898263)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742061574807)

Perfis os mesmos

Regra de Calculo Documentos Fiscais - PIS Majorado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742061575063)

Alíquota

I:Majoração

Não tem regra de escrituração, pois será majorado no PIS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742061575447)

Perfis os mesmos

Após criar o PIS majorado, precisa alterar a Regra de calculo do PIS para incluir o majoração

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742061576087)

Regra de Calculo Documentos Fiscais COFINS majorado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742061576215)

Regra de alíquota

I:majoração a mesma do PIS majorado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742061576343)

Sem regra de escrituração

Perfis os mesmos

Após criar o COFINS  majorado, precisa alterar a Regra de calculo do COFINS  para incluir o majoração

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742061576727)

Regra de Base de calculo - ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742045902615)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742045902871)

composição da base de calculo do ICMS ( mercadoria - desconto + despesa + frete + seguro  + II + pis + cofins +ipi ) / ( 1 - aliquota de 12% /100 )

Regra de Alíquota = I:ALIQ\_NCM

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742045903383)

Regra de alíquota = 12%

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742045903895)

Regra de escrituração

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742045904023)

Regra de Calculo Documentos Fiscais - ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742045904535)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742045905303)

Perfis os mesmos

TES

Gera duplicata = sim

CFOP = 3102

Campos

Agrega valor = sim

Agrega PIS = não

Agrega COF = não

Documento de entradas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742061582231)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742045905687)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742061583383)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742061584279)

SF3

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34742045907735)
