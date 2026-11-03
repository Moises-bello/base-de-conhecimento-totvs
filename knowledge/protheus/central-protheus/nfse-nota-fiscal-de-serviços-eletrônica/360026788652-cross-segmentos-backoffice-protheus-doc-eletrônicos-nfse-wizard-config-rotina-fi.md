---
article_id: 360026788652
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: a840d4128674a68516289f491197b98546ca0285cd9d872018c8e9920d74f416
fetched_at: '2026-06-28T22:39:58.636355+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Wizard. Config
  rotina FISA022
type: support-article
updated_at: '2023-11-08T14:35:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026788652-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Wizard-Config-rotina-FISA022
---

**Dúvida**Informações do wizard.config da rotina FISA022.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**

**Tela 1 - Boas Vindas**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026539291)  
  
**Tela 2 - Url do TSS**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026548112)  
  
**Tela 3 - Certificado Digital**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026548172)  
  
**Tela 4 - Configurações do ambiente**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026539571)

Essa última tela pode possuir diferentes campos, de acordo com o município da filial.  
Por exemplo, os campos 'Nome de usuario' e 'Senha' serão habilitados para poucos municípios.  
  
**Ambiente:** Produção ou Homologação.  
**Versão:** [Coluna Versão Homologada](http://tdn.totvs.com/pages/releaseview.action?pageId=4814340)**Codigo SIAFI:** Conteúdo é carregado automaticamente pela rotina, com o código do município de acordo com o SIAFI.  
**CNPJ do certificado digital:** Obrigatório o preenchimento se o CNPJ do certificado for diferente do CNPJ da filial emitente.  
**Nome de usuario:** Seguir orientação da prefeitura.  
**Senha:**Seguir orientação da prefeitura.

**Tela 5 - Modelo**

Define qual tipo de envio será executado para a Empresa/Filial. Se o envio de notas será feito no padrão antigo na qual a nota é enviada para **prefeitura/Provedor** ou no novo padrão **SERPRO / nfs-e Nacional**. 

* Deve ser Selecionado 2- NFS-e Nacional **SOMENTE**para empresas que foram barradas pela Prefeitura e obrigatoriamente devem utilizar o ambiente da nfs-e nacional.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18914193768983)
