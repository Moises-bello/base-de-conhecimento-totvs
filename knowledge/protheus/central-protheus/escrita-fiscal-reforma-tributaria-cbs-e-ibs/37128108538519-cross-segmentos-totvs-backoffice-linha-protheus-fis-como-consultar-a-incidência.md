---
article_id: 37128108538519
category: Escrita Fiscal - Reforma Tributaria - CBS e IBS
content_hash: e200e685c086a0a7158396bbef1b95c109b4c06db2362880421b63caab443359
fetched_at: '2026-06-28T22:39:15.803279+00:00'
product: protheus
section_id: 33305945453079
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como consultar a
  incidência de tributos IBS e CBS por Documento Fiscal no Protheus
type: support-article
updated_at: '2025-12-19T17:06:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37128108538519-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-consultar-a-incid%C3%AAncia-de-tributos-IBS-e-CBS-por-Documento-Fiscal-no-Protheus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37128098594583) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**  
Como gerar relatório com os valores de IBS e CBS?  
  
**Ambiente**  
  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - A partir da versão 12.1.2310  
  
**Solução**  
No Protheus, é possível consultar a incidência dos tributos IBS e CBS por Documento Fiscal por meio do **Configurador de Tributos** e também através de um relatório disponível no **SmartView**.

**Configurador de Tributos**

1. Acesse o **Configurador de Tributos**.
2. Navegue até a pasta **Regras Fiscais**.
3. Em seguida, acesse: Relatórios > Tributos Genéricos por Documento Fiscal:

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37128108531095)
4. No relatório, preencha as seguintes informações:

   - Data de Inicial?  
   - Data Final?  
   - Seleciona Filiais?  
   - Tributo?

   Segue exemplo:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37128098597527)
5. O sistema exibirá a **incidência do tributo em cada nota fiscal**, permitindo a conferência das regras aplicadas.

**OBS:** Para gerar informações no relatório Tributos Genéricos por Documento Fiscal deve ser gerado F2D e CJ3 referente ao tributo. 

**SmartView**

Também é possível realizar a conferência utilizando o relatório do SmartView:

* **Nome do relatório:** Listagem de Conferência de Tributos

Esse relatório permite analisar e validar os tributos calculados nos documentos fiscais de forma consolidada.

[Listagem de Conferência de Tributos](https://tdn.totvs.com/pages/viewpage.action?pageId=821585275)

Documentações relacionada:

* [CFGTRIB - Configurador de Tributos](https://tdn.totvs.com/display/PROT/CFGTRIB+-+Configurador+de+Tributos)
* [Smartview - Fiscal - P12 - Consultas](https://tdn.totvs.com/display/PROT/Smartview+-+Fiscal+-+P12+-+Consultas)
