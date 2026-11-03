---
article_id: 33661274329367
category: Escrita Fiscal - Reforma Tributaria - CBS e IBS
content_hash: 9aa5d578de341c71c3b67763e3b74f490c7ae8c06c3bc89f53019d32a18bfc08
fetched_at: '2026-06-28T22:39:15.790371+00:00'
product: protheus
section_id: 33305945453079
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como configurar o
  calculo do IBS e CBS?
type: support-article
updated_at: '2025-11-14T22:10:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33661274329367-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-calculo-do-IBS-e-CBS
---

**Dúvida**

**Como configurar o calculo do IBS e CBS?**  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Atualmente, temos **dois cenários possíveis** para a configuração das Operações Fiscais no ERP Protheus:

obs: a orientação da TOTVS é que siga o cenário 100% no Configurador de Tributos.

---

### **🔹 1. Cenário 100% no Configurador de Tributos**

Todos os impostos (inclusive ICMS, IPI, PIS, COFINS, IBS e CBS) são calculados por meio do **Configurador de Tributos**.

![📄](https://fonts.gstatic.com/s/e/notoemoji/16.0/1f4c4/72.png) Acesse o passo a passo completo:  
![🔗](https://fonts.gstatic.com/s/e/notoemoji/16.0/1f517/72.png) [Como configurar o cálculo do CBS/IBS no Configurador de Tributos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33325130340887-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-c%C3%A1lculo-do-CBS-IBS-no-Configurador-de-Tributos)

---

### **🔹 2. Cenário Híbrido (Legado + Configurador de Tributos)**

Neste modelo, os impostos atuais (ICMS, IPI, PIS, COFINS etc.) continuam sendo calculados pelos **cadastros legados**, e **apenas o IBS e CBS** são calculados via **Configurador de Tributos**.

![📄](https://fonts.gstatic.com/s/e/notoemoji/16.0/1f4c4/72.png) Acesse o passo a passo completo:  
![🔗](https://fonts.gstatic.com/s/e/notoemoji/16.0/1f517/72.png) [Como realizar carga automática dos Tributos CBS e IBS no Configurador de Tributos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33147484988823-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-realizar-carga-autom%C3%A1tica-dos-Tributos-CBS-e-IBS-no-Configurador-de-Tributos)

---

**Atualização Tabela cClassTrib - IBS/CBS.**

Com a Reforma Tributária, torna-se necessário informar no Configurador de Tributos, os códigos da Classificação Tributária tanto para o **IBS (Imposto sobre Bens e Serviços)** como para a **CBS (Contribuição sobre Bens e Serviços)**. Para isso foi criada uma rotina de cadastro, onde é possível informar todos os dados referentes a cada Código de Classificação Tributária. Como facilitador, dentro desse cadastro foi disponibilizada a opção de importação da tabela oficial, disponibilizada pela Sefaz, o que agiliza o processo além de evitar erros de digitação.

Abaixo Expedição Continua para atualização:

**obs: o arquivo SDFBRA deve ser incluído na pasta systemload e aplicar o compatibilizador UPDDISTR.**

<https://tdn.totvs.com/pages/releaseview.action?pageId=525823851>

# [CFGTRIB - Adequação do Configurador de Tributos aos Códigos de Classificação Tributária do IBS, CBS e IS](https://tdn.totvs.com/pages/viewpage.action?pageId=962623217)

---

### **📄 Atualização das Notas Técnicas – XML**

Para garantir que o XML da NF-e contenha corretamente as novas **tags do IBS e CBS**, acesse:

![🔗](https://fonts.gstatic.com/s/e/notoemoji/16.0/1f517/72.png) [Nota Técnica 2025.002 v.1.10 – Atualização XML NF-e](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33208366723607-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tribut%C3%A1ria-Nota-T%C3%A9cnica-2025-002-v-1-10)
