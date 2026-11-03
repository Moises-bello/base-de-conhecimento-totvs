---
article_id: 37535552749463
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 32a6939131148964e7f476f5f1184821a53972897d5009d12ab4b30bdce2c76b
fetched_at: '2026-06-28T22:39:09.796226+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento – Backoffice (Linha Protheus) – Pontos de lançamento de estoque
  na rotina de PCO
type: support-article
updated_at: '2026-01-08T18:28:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37535552749463-Cross-Segmento-Backoffice-Linha-Protheus-Pontos-de-lan%C3%A7amento-de-estoque-na-rotina-de-PCO
---

A integração entre os módulos Estoque/Custos e Planejamento e Controle Orçamentário (PCO) no TOTVS Protheus gera lançamentos automáticos no PCO para cada movimentação no Estoque/Custos, configurados via parâmetro MV\_PCOINTE e pontos de lançamento no PCO. O artigo detalha o procedimento para configurar esses lançamentos conforme tipos de movimentação, como Solicitação ao Armazém, Movimentos Internos e Acerto de Inventário.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37535547789847) Tempo aproximado para leitura: 01**:**00:00 **min**  
  
**Dúvida**  
Quais são os pontos de lançamento de estoque na integração com o módulo de de PCO (Planejamento e controle Orçamentário) ?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Quando a integração entre os módulos **Estoque/Custos** e **Planejamento e Controle Orçamentário (PCO)** está ativa, cada movimentação registrada no Estoque/Custos gera automaticamente um lançamento correspondente no PCO.

Essa integração funciona por meio do parâmetro **MV\_PCOINTE** e dos lançamentos orçamentários configurados na rotina **Pontos de Lançamento** do módulo de PCO.

## **Procedimento**

Para configurar os lançamentos orçamentários que serão integrados ao Estoque/Custos:

### **1. Acesse a rotina Pontos de Lançamentos**

* Acessar o módulo 57 -> Planejamento e Controle Orçamentário.
* Depois acessar Atualizações -> Lançamento -> Ponto de lançamento (PCOA040)
* Clique em **Lançamentos**.

### **2. Configure os processos conforme cada tipo de movimentação**

#### 

#### **Solicitação ao Armazém – MATA105**

* **Processo 000150, sequência 01** – Inclusão de SA (SCP)
* **Processo 000150, sequência 02** – Exclusão de SA (SCP)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37535552698903)![](https://centraldeatendimento.totvs.com/hc/article_attachments/37535552702615)

#### 

#### **Movimentos Internos – MATA241**

* **Processo 000151, sequência 01** – Inclusão de documento (SD3)
* **Processo 000151, sequência 02** – Estorno de documento (SD3)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37535552705687)![](https://centraldeatendimento.totvs.com/hc/article_attachments/37535547797271)

#### 

#### **Acerto de Inventário – MATA340**

* **Processo 000153, sequência 01** – Inclusão de documento (SB7)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37535547802007)![](https://centraldeatendimento.totvs.com/hc/article_attachments/37535552712855)

### 

### **3. Revise as configurações e confirme o cadastro**

## 

## **Observação**

É possível consultar o resultado do processamento dos movimentos diretamente na rotina **Lançamentos**, permitindo verificar os registros que foram integrados ao PCO.

**Saiba mais:**

[**Integração com Estoque/Custos (PCOA030 - SIGAPCO)**](https://tdn.totvs.com/pages/releaseview.action?pageId=1031534817)

[**Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Quais os Códigos dos Lançamentos Padronizados do Estoque?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020801392-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Quais-os-C%C3%B3digos-dos-Lan%C3%A7amentos-Padronizados-do-Estoque)

[**Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
