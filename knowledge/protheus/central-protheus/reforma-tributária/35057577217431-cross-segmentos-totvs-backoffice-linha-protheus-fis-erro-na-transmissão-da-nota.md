---
article_id: 35057577217431
category: Reforma Tributária
content_hash: a6275e8fd1f3d238abbf4c18eecf307d309b0236a9a5ec8a06dc8970497669c4
fetched_at: '2026-06-28T22:39:53.813354+00:00'
product: protheus
section_id: 34900856700439
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – Erro na Transmissão
  da Nota Fiscal com Cálculo do IBS/CBS - Rejeição 029 devido a falta do cClassTrib.
type: support-article
updated_at: '2025-09-19T13:44:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35057577217431-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Erro-na-Transmiss%C3%A3o-da-Nota-Fiscal-com-C%C3%A1lculo-do-IBS-CBS-Rejei%C3%A7%C3%A3o-029-devido-a-falta-do-cClassTrib
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35057587504919) Tempo aproximado para leitura: **00:10 min**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - a partir da 12.1.2310

**Ocorrência**  
Durante a transmissão da nota fiscal que contém cálculo do IBS (Imposto sobre Bens e Serviços) e CBS (Contribuição sobre Bens e Serviços), ocorre a **Rejeição 029**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35057577205911)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35057577206551)  
Após monitorar a nota, clicar no botão Schema e escolher a opção “Não” para mostrar o erro completo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35057587506839)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35057577207959)

**Causa**  
A rejeição ocorre porque o código de Classificação Tributária não está vinculado corretamente na Regra de Escrituração associada às Regras de Cálculo do IBS e CBS.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35057587507735)

**Obs:** Antes de realizar a transmissão da nota, é possível validar se o cClassTrib foi preenchido corretamente na nota analisando a aba de Tributos Genéricos - Por Item no Documento de Saída.

**Solução**  
Para resolver o problema, é necessário ajustar as configurações conforme a documentação oficial disponível:

* Acesse a documentação [CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como importar a tabela cClassTrib-IBS/CBS no Configurador de Tributos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34662420522391-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-importar-a-tabela-cClassTrib-IBS-CBS-no-Configurador-de-Tributos)
* Vincule corretamente o código de Classificação Tributária na Regra de Escrituração associada às Regras de Cálculo do IBS e CBS

Após realizar o ajuste:

* Crie um novo Pedido de Venda
* Efetue a transmissão da nota fiscal a partir deste novo pedido
