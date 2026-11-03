---
content_hash: 3e0090484c381a52c7ed483e59c5ca3e3d009dbb934dfa0333d53469ba38d9e5
fetched_at: '2026-06-29T00:12:15.478896+00:00'
page_id: '979814750'
product: rm
source: tdn-rm
title: Início - Out/2025 (NFCom)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=979814750
version: 9
---

Na **primeira versão**, prevista para **Outubro/2025**, entregaremos os seguintes recursos:

## ✅ Funcionalidades Disponíveis

* **Emissão da NFCom em modalidade normal**
* **Impressão do DANFE-COM**
* **Cancelamento de NFCom (Evento)**
* **NFCom de Substituição**
* **Transmissão via TSS (TOTVS Service SOA)**

# Versões para atualização

A solução está disponível a partir dos patches:

Data:

Biblioteca RM

* 12.1.2502.227
* 12.1.2506.177
* 12.1.2510.110

TSS: [Orientações para Instalação e Atualização do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18590720143639-Cross-Segmentos-TOTVS-Backoffice-Linha-RM-Doc-Eletr%C3%B4nicos-Instala%C3%A7%C3%A3o-e-atualiza%C3%A7%C3%A3o-do-TSS-12-1-2410)

---

## ⚠️ Limitações da Primeira Versão

Alguns grupos e campos do XML da NFCom **não serão gerados** na primeira entrega. Abaixo detalhamos os pontos:

### Grupo `ide` – Identificação da NFCom

* **Tipo de faturamento:** Apenas `0 - Normal` estará disponível.
* Campos **indPrePago** e **indCessaoMeiosRede** não serão gerados.
* Dados de **contingência** não serão implementados nesta versão.  
  🔗 [Detalhes do Grupo ide](https://tdn.totvs.com/pages/viewpage.action?pageId=900452469)

### Grupo `gCofat` – Informações do Cofaturamento

* Não será gerado.  
  🔗 [Detalhes do Grupo gCofat](https://tdn.totvs.com/pages/viewpage.action?pageId=901955758)

### Grupo `gFidelidade` – Programa de Fidelidade do Assinante

* Não será gerado.  
  🔗 [Detalhes do Grupo gFidelidade](https://tdn.totvs.com/pages/viewpage.action?pageId=901956048)

### Grupo `gFat` – Controle da Fatura

* Não serão gerados os campos:

  + **codDebAuto**
  + **codBanco**
  + **codAgencia**

🔗 [Detalhes do Grupo gFidelidade](https://tdn.totvs.com/pages/viewpage.action?pageId=901956138)

### Grupo `gFatCentral` – Faturamento Centralizado

* Não será gerado.  
  🔗 [Detalhes do Grupo gFatCentral](https://tdn.totvs.com/pages/viewpage.action?pageId=901957774)

### Grupo `gRessarc` – Ressarcimento

* Não será gerado.  
  🔗 [Detalhes do Grupo gRessarc](https://tdn.totvs.com/pages/viewpage.action?pageId=901954513)

### Grupo `gProcRef` – Processo Referenciado

* Não será gerado.  
  🔗 [Detalhes do Grupo gProcRef](https://tdn.totvs.com/pages/viewpage.action?pageId=901954486)

### Grupo `FUST` – Dados do FUST

* Não será gerado.  
  🔗 [Detalhes do Grupo FUST](https://tdn.totvs.com/pages/viewpage.action?pageId=901961043)

### Grupo `FUNTTEL` – Dados do FUNTTEL

* Não será gerado.  
  🔗 [Detalhes do Grupo FUNTTEL](https://tdn.totvs.com/pages/viewpage.action?pageId=901961067)

---

## 📌 Observação Final

Todas as demais informações e grupos do XML da NFCom serão **implementados normalmente nesta entrega**.  
As evoluções para os grupos não contemplados nesta primeira versão já estão no nosso backlog e serão priorizadas nas próximas releases
