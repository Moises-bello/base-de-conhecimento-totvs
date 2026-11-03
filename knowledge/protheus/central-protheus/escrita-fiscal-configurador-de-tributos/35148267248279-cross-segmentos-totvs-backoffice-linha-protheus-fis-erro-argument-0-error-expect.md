---
article_id: 35148267248279
category: Escrita Fiscal - Configurador de Tributos
content_hash: 4ccc9e9dd39991f3ceb472a2b39c3833c570f58920f2c35969ab32caafe794fe
fetched_at: '2026-06-28T22:39:17.653028+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Erro argument #0
  error, expected A->U,  function asize on TOTVS.PROTHEUS.BACKOFFICE.FISCAL ao gerar
  nota com impostos calculados pelo Configurador de Tributos'
type: support-article
updated_at: '2025-09-23T19:24:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35148267248279-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Erro-argument-0-error-expected-A-U-function-asize-on-TOTVS-PROTHEUS-BACKOFFICE-FISCAL-ao-gerar-nota-com-impostos-calculados-pelo-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35148270188695) Tempo aproximado para leitura: **00:10 min**  
  
**Ocorrência**  
Ao gerar uma nota fiscal em que os impostos são calculados pelo **Configurador de Tributos**, está sendo registrado o seguinte error.log:  
  
*argument #0 error, expected A->U,  function asize on TOTVS.PROTHEUS.BACKOFFICE.FISCAL.ADDITIONALDATA.TCADDITIONALDATA:GETADDITIONALDATAIDSFROMMATXFIS(BACKOFFICE.FISCAL.TAXCONFIGURATOR.ADDITIONALDATA.CLASS.TLPP)*  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - A partir da versão 12.1.2310  
  
**Causa**  
Esse erro ocorre devido a uma inconsistência interna relacionada ao cálculo tributário com o uso do Configurador de Tributos nas versões impactadas do Protheus.  
  
**Solução**  
Para corrigir essa situação, é necessário aplicar os pacotes de atualização disponibilizados conforme a versão do seu ambiente Protheus.

Segue abaixo a relação das versões e seus respectivos links de atualização:

| Versão Protheus | Link para atualização |
| --- | --- |
| 12.1.2210 | [Download](https://r.totvs.io/p/1214137) |
| 12.1.2310 | [Download](https://r.totvs.io/p/1214138) |
| 12.1.2410 | [Download](https://r.totvs.io/p/1214136) |
| 12.1.2510 | [Download](https://r.totvs.io/p/1214139) |

⚠️ **Importante**: Após aplicar o pacote, certifique-se de compilar os fontes atualizados, aplicar dicionários e reiniciar os serviços do Protheus.
