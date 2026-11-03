---
article_id: 360028652851
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: b87670c9f22915f5ea477ec8100d2caccbf588afef7369a6ed5dc43f813650a7
fetched_at: '2026-06-28T22:42:05.204794+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Geração dos registros F200, F205 e F210
type: support-article
updated_at: '2023-01-04T17:35:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028652851-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Gera%C3%A7%C3%A3o-dos-registros-F200-F205-e-F210
---

**Dúvida**Como gerar os Registros **F200**, **F205** e **F210** do **EFD Contribuições**?  
   
 **Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
Os Registros **F200**, **F205** e **F210** do arquivo do **EFD Contribuições**, são gerados somente utilizando o Ponto de Entrada**SPDPCIMOB**.

Ponto de entrada **SPDPCIMOB**:  
<http://tdn.totvs.com/pages/releaseview.action?pageId=6077220>  
  
**Registro tipo F200 – Operações da atividade Imobiliária - Unidade Imobiliária vendida:**Gere esse Registro através do ponto de entrada **SPDPCIMOB.** O último campo de retorno do PE deve ser o tipo de Regime a qual pertence o registro, (0) **Cumulativo**, (1) **Não Cumulativo**, esta informação é necessária para geração do **Bloco M**.  
  
**Registro tipo F205 – Operações da atividade Imobiliária - Custo Incorrido da atividade Imobiliária:**Gere esse Registro através do ponto de entrada **SPDPCIMOB**.  
  
**Registro tipo F210 – Operações da atividade Imobiliária - Custo orçado da unidade imobiliária vendida:**Este registro é gerado através do ponto de entrada **SPDPCIMOB.**Considerações para o Tratamento do **Lucro Presumido** – **Regime de Caixa**: Para os Contribuintes enquadrados como **Lucro Presumido**, optantes pela apuração da contribuição de **PIS** e da **COFINS** pelo **Regime de Caixa**, serão gerados os registros **F500**, **F509**, **F510**, **F519**, **F525** e **1900**.
