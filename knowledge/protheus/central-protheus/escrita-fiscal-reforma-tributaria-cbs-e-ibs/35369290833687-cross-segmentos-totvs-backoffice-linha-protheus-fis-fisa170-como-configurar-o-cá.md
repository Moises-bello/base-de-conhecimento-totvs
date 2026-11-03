---
article_id: 35369290833687
category: Escrita Fiscal - Reforma Tributaria - CBS e IBS
content_hash: 36318c474ea5ae84547bc4d921764f3ea79d2eac71a045f8f42968b8c3e8d5c4
fetched_at: '2026-06-28T22:39:15.821996+00:00'
product: protheus
section_id: 33305945453079
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - FISA170 - Como configurar
  o cálculo do IBSMUN no Configurador de Tributos?
type: support-article
updated_at: '2025-11-21T15:05:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35369290833687-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-configurar-o-c%C3%A1lculo-do-IBSMUN-no-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35369290740759) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**  
Como configurar o cálculo do IBSMUN (IBS Municipal) no Configurador de Tributos?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - FIS - a partir da release 12.1.2310  
  
**Solução**  
**A configuração apresentada abaixo é um exemplo, que poderá servir como base para a criação do cenário específico da sua empresa.**

**Recomenda-se validar junto à sua equipe Fiscal ou Contábil a memória de cálculo que deverá ser aplicada às suas operações.**

## Tributos

IBSMUN - IBS MUNICIPAL

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36495739048471)

## Perfil de Produto

Criar um Perfil de produto e incluir TODOS no campo Cód. Produto.

Todos os produtos serão considerados nesse perfil.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36495707479191)

## Perfil de Operação

Utilizar o Perfil de Operação 000051 - TODOS OS CFOPS  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36495739052055)![](https://centraldeatendimento.totvs.com/hc/article_attachments/36495739053463)

## Perfil de Participante

Criar um Perfil de Participante e incluir TODOS os Fornecedores e Cliente.

No campo Participante digite a palavra TODOS e no campo Loja ZZ ou quantidade caracteres que possua em seu ambiente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36495707482263)

## Perfil de Origem/Destino

Utilizar o Perfil 000002 - Todas as UFS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36495739057047)![](https://centraldeatendimento.totvs.com/hc/article_attachments/36495739059223)

Regra de Base de Cálculo

Na Regra de Base de Cálculo utilizar a opção 11 - Fórmula Manual.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36495739060631)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36495739061271)

## Regra de Alíquota

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36495739064087)

## Configuração para a Regra de Escrituração:

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como importar a tabela cClassTrib-IBS/CBS no Configurador de Tributos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34662420522391-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-importar-a-tabela-cClassTrib-IBS-CBS-no-Configurador-de-Tributos)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36495707492375)

OBS: O cClassTrib a ser utilizado deve ser analisado e informado pelo Fiscal responsável da empresa, pois possui diversas variações. Segue o link com maiores informações:

[Classificação Tributária](https://dfe-portal.svrs.rs.gov.br/Cff/ClassificacaoTributaria)

## Regra de Cálculo - Documentos Fiscais

Regra de cálculo - IBSMUN

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36495739067287)![](https://centraldeatendimento.totvs.com/hc/article_attachments/36495707495831)![](https://centraldeatendimento.totvs.com/hc/article_attachments/36495739070231)

**7)** Inclusão da Nota pelo Faturamento – Pedido de Venda no valor de R$ 1.000,00:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36495739072407)

**8)** Inclusão da Nota pelo Compras – Documento de Entrada no valor de R$ 1.000,00:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36495739073943)

**Documentações relacionadas:**

[Escrita Fiscal - Reforma Tributaria - CBS e IBS](https://centraldeatendimento.totvs.com/hc/pt-br/sections/33305945453079-Escrita-Fiscal-Reforma-Tributaria-CBS-e-IBS)

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Reforma Tributária](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27223416466967-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Reforma-Tribut%C3%A1ria)

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Atualização para Reforma Tributária e Adequação para a Reforma Tributária](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34792278750999-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Atualiza%C3%A7%C3%A3o-para-Reforma-Tribut%C3%A1ria-e-Adequa%C3%A7%C3%A3o-para-a-Reforma-Tribut%C3%A1ria)

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como configurar o cálculo do CBS/IBS no Configurador de Tributos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33325130340887-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-c%C3%A1lculo-do-CBS-IBS-no-Configurador-de-Tributos)
