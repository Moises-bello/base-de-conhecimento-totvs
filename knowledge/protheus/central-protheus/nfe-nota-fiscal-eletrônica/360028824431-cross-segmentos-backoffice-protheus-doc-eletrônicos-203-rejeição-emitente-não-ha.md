---
article_id: 360028824431
category: NFe - Nota Fiscal Eletrônica
content_hash: c24c118ee1e0d215f9947d834a06277e4cb7a9fa6ea9ad812e51a0fd83b7603f
fetched_at: '2026-06-28T22:40:03.753484+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 203 Rejeição :
  Emitente não habilitado para emissão de NF-e'
type: support-article
updated_at: '2025-06-12T18:20:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028824431-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-203-Rejei%C3%A7%C3%A3o-Emitente-n%C3%A3o-habilitado-para-emiss%C3%A3o-de-NF-e
---

**Dúvida**Como resolver a rejeição 203 : Emitente não habilitado para emissão de NF-e ?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

A rejeição ocorre, pois o emitente da **NF-e não está habilitado para realizar emissão** deste modelo de documento **fiscal (55).**

* Abaixo segue os motivos pelo qual pode **ocorrer a rejeição:**

1. Normalmente, empresas recém criadas e que **ainda estão em processo de cadastramento** na Sefaz;
2. Empresas que já são emissoras, porém estão com algum **tipo de pendência na Sefaz ou Receita Federal;**
3. Este incidente é mais comum na Sefaz PR, mas pode ocorrer em qualquer UF. Caso se trate da Sefaz PR, verifique com nosso jurídico, **"CST - Serviços Jurídicos"** se seu acesso esta habilitado.
4. Por **instabilidade na Sefaz.**

Nessa situação, **o ideal é que primeiro consulte sua Inscrição Estadual ou CNPJ no  Cadastro Centralizado de Contribuintes (CCC)**. Ao fazer essa consulta, é possível verificar a situação cadastral da sua empresa e se encontra-se habilitada.

* **Cadastro Centralizado de Contribuinte (CCC) consultar o link abaixo:**

[Clique aqui](https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc)

* **Saiba mais:**

Em todos os casos, é importante **entrar em contato com a Sefaz** para verificar sua situação cadastral na Sefaz e o motivo da rejeição.   
  
Normalizado o problema, basta reenviar sua NF-e.

Para verificar se no XML o **CNPJ e o IE da empresa,** estão corretos:

1. Acessar a  **rotina de transmissão SPEDNFE;**

![nfesefaz.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17384496612247)

2. Clique em **Outras ações -> Monitor -> faixa ->** Digite o número e série da nota;

**![monitor_faixa.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17384529249943)**

3. Clique no **botão Schema; Copie e Cole o conteúdo completo do XML.**

![546_rejeicao.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17384529256471)

4. Verifique se a ***TAG CNPJ e IE.***

* **Validação da Sefaz:**

![](http://www.oobj.com.br/bc/assets/Articles/99/Rej203.PNG)

Fonte: [Manual de Orientação ao Contribuinte(v. 6.00)](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=URCYvjVMIzI=)
