---
article_id: 35065194117911
category: Escrita Fiscal - Reforma Tributaria - CBS e IBS
content_hash: 67e71aef7221bfdfd5425c8508883b99aec633c1d2e6fe2eb4d7ece996c6c320
fetched_at: '2026-06-28T22:39:15.837734+00:00'
product: protheus
section_id: 33305945453079
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – Campos que armazenam
  as informações dos impostos IBS e CBS.
type: support-article
updated_at: '2025-09-19T17:46:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35065194117911-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Campos-que-armazenam-as-informa%C3%A7%C3%B5es-dos-impostos-IBS-e-CBS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35065202656279) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**  
Quais campos e tabelas irão armazenar as informações dos impostos IBS (Imposto sobre Bens e Serviços) e CBS (Contribuição para o Sistema de Saúde) gerados pelo Configurador de Tributos?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Fis - A partir da versão 12.1.2310  
  
**Solução**  
Este documento visa descrever os campos e tabelas onde são armazenadas as informações dos impostos IBS (Imposto sobre Bens e Serviços) e CBS (Contribuição para o Sistema de Saúde) gerados pelo Configurador de Tributos no sistema Protheus.

Atualmente, as informações relacionadas aos impostos **IBS** e **CBS** são armazenadas nas seguintes tabelas e campos:

#### **Tabela CJ3 - Escrituração por Item**

* **Descrição**: A tabela CJ3 é responsável por armazenar os dados relacionados à escrituração de impostos por item, ou seja, os valores de impostos calculados para cada item de nota fiscal ou lançamento contábil.
* **Campos Relevantes**:

  + **Código Tributo** **(CJ3\_TRIB)**: Código do tributo associado ao item.
  + **CST (CJ3\_CST):** CST do IBS e CBS informado na Regra de Escrituração.
  + **CCT (CJ3\_CCT):** CCT do IBS e CBS informado na Regra de Escrituração.
  + **Valor IBS (CJ3\_VALTRIB)**: Valor calculado do imposto IBS.
  + **Valor CBS** **(CJ3\_VALTRIB)**: Valor calculado do imposto CBS.

#### **Tabela F2D - Tributos Genéricos Calculados**

* **Descrição**: A tabela F2D armazena os tributos calculados de forma genérica, sendo utilizados em diversos processos fiscais dentro do sistema. Nessa tabela são guardados dados dos tributos gerados pelo Configurador de Tributos.
* **Campos Relevantes**:

  + **Código Tributo (F2D\_TRIB)**: Código do tributo calculado.
  + **Base de calculo (F2D\_BASE)**: Base de calculo do Tributo.
  + **Alíquota (F2D\_ALIQ)**: Alíquota do tributo
  + **Valor IBS (F2D\_VALOR)**: Valor do IBS gerado pelo sistema.
  + **Valor CBS** **(F2D\_VALOR)**: Valor do CBS gerado pelo sistema.

A estrutura das tabelas CJ3 e F2D garante que as informações fiscais relacionadas ao IBS e CBS sejam corretamente armazenadas e acessíveis para futuros processos de escrituração e apuração de tributos.

**Documentações relacionadas:**

* [Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Reforma Tributária](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27223416466967-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Reforma-Tribut%C3%A1ria)
* [CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Atualização para Reforma Tributária e Adequação para a Reforma Tributária](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34792278750999-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Atualiza%C3%A7%C3%A3o-para-Reforma-Tribut%C3%A1ria-e-Adequa%C3%A7%C3%A3o-para-a-Reforma-Tribut%C3%A1ria)
* [CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como configurar o cálculo do CBS/IBS no Configurador de Tributos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33325130340887-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-c%C3%A1lculo-do-CBS-IBS-no-Configurador-de-Tributos)
