---
article_id: 34792278750999
category: Escrita Fiscal - Reforma Tributaria - CBS e IBS
content_hash: 40482320b03662fae3ce97f26a1f92f926d7b3035072f45243b4b1c59bbd5d70
fetched_at: '2026-06-28T22:39:15.758645+00:00'
product: protheus
section_id: 33305945453079
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Atualização para
  Reforma Tributária e Adequação para a Reforma Tributária
type: support-article
updated_at: '2026-03-16T20:24:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34792278750999-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Atualiza%C3%A7%C3%A3o-para-Reforma-Tribut%C3%A1ria-e-Adequa%C3%A7%C3%A3o-para-a-Reforma-Tribut%C3%A1ria
---

**Dúvida**  
O que devo atualizar em meu ambiente para atender a Reforma Tributária?  
  
**Ambiente**   
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Solução**

**Nesta documentação contempla a Atualização Configurador de Tributos, Atualização XML, Configuração IBS e CBS, Atualização da Reforma Tributária.**

### Atualização do **Configurador de Tributos**

Com a **Reforma Tributária**, torna-se necessário parametrizar no **Configurador de Tributos (CFGTRIB)** os códigos da **Classificação Tributária** referentes ao **IBS (Imposto sobre Bens e Serviços)** e à **CBS (Contribuição sobre Bens e Serviços)**.

Para isso, foi criada uma **rotina de cadastro**, permitindo informar todos os dados de cada Código de Classificação Tributária. Como facilitador, a rotina disponibiliza a opção de **importação da tabela oficial da Sefaz**, agilizando o processo e evitando erros de digitação.

### 🚀 Procedimento de Atualização (Expedição Contínua)

> **Obs.:** O arquivo **SDFBRA** deve ser incluído na pasta **systemload** e aplicado via compatibilizador **UPDDISTR**.

🔗 [Expedição Contínua – Atualização CFGTRIB](https://tdn.totvs.com/pages/releaseview.action?pageId=525823851)  
🔗 [**CFGTRIB – Adequação do Configurador de Tributos** aos Códigos de Classificação Tributária do **IBS, CBS e IS**](https://tdn.totvs.com/pages/releaseview.action?pageId=962623217)

### ⚙️ Configuração do **Cálculo de IBS e CBS**

* Cenário 100% no Configurador de Tributos – recomendado: todos os impostos (ICMS, IPI, PIS, COFINS, IBS e CBS) calculados pelo Configurador.
* Cenário Híbrido (legado + Configurador) – apenas IBS e CBS calculados pelo Configurador; disponível após atualização via expedição contínua.
* Rotina **FISA170** é utilizada para implementar os novos cálculos de IBS e CBS.

🔗 [Como configurar o cálculo do IBS e CBS – FIS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33325130340887-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-c%C3%A1lculo-do-CBS-IBS-no-Configurador-de-Tributos)  
[🔗 Como realizar carga automática dos Tributos CBS e IBS no Configurador de Tributos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33147484988823-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-realizar-carga-autom%C3%A1tica-dos-Tributos-CBS-e-IBS-no-Configurador-de-Tributos)  
🔗 [Seção Escrita Fiscal – Reforma Tributária – CBS e IBS](https://centraldeatendimento.totvs.com/hc/pt-br/sections/33305945453079-Escrita-Fiscal-Reforma-Tributaria-CBS-e-IBS)

### 📄 Atualização das **Notas Técnicas – XML**

Para garantir que o **XML da NF-e** contenha corretamente as novas tags do IBS e CBS, consulte:

🔗 [Nota Técnica 2025.002 v.1.10 – Atualização XML NF-e](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33208366723607-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tribut%C3%A1ria-Nota-T%C3%A9cnica-2025-002-v-1-10-e-v1-20?utm_source=chatgpt.com)
