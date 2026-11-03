---
article_id: 360028548251
category: eSocial - Cadastros
content_hash: 3df18eac87f9bd9e5030cc1d8fa2d293a98f31cc325e9e34e022d995e2e4eedb
fetched_at: '2026-06-28T22:47:14.489621+00:00'
product: rm
section_id: 1500000834341
source: central-rm
title: RH - RM - FOP - eSocial - Desoneração de CNO
type: support-article
updated_at: '2024-06-04T20:55:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028548251-RH-RM-FOP-eSocial-Desonera%C3%A7%C3%A3o-de-CNO
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21510025639447)Tempo aproximado para leitura: 00:02:30 min**

**Dúvida**Como informar a desoneração do CNO no eSocial?  
  
 **Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões  
  
**Solução**A desoneração do CNO só é possível para pessoas jurídicas com indicativo de construtora. Para validação desta informação, verifique se em **eSocial | Informações do Empregador** o campo **Indicativo de Construtora** está informado como **1 - Empresa Construtora**. No evento S-1000, esta informação é preenchida na tag **indConstr**.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028846131)

Além disso, deve-se validar se trata-se de uma obra própria, ou seja, o CNO foi registrado em nome do próprio cliente/fornecedor ao qual está vinculado. Se tratando de obra própria, verifique em **Administração de Pessoal | Cliente e Fornecedor | Anexos | eSocial** se a opção **Obra Própria** está selecionada. Certifique-se de ter transmitido com sucesso o evento **S-1005** referente ao registro do CNO.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21510025649559)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21510025652375)

Após as validações supracitadas, caso sua empresa esteja apta a encaminhar a desoneração do CNO, realize os passos a seguir:

1. Selecione o menu **Administração de Pessoal | Cliente e Fornecedor | CEI do Cliente/ Fornecedor**, faça a edição do CNO desejado após acesse **Anexos | eSocial** preencha o campo **Indicativo de Substituição da Contribuição Patronal de Obra de Construção Civil** com seu respectivo valor.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21510109332759)

2. No menu **eSocial | Período de Apuração**, crie/edite o período de apuração desejado e preencha os campos relacionados às **Informações Substituição Patronal**. 

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028872832)

3. Após, acesse **eSocial | Gerar XML (Periódicos)** e faça a geração do S-1280 para integração e transmissão ao RET.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029472612)

**Saiba mais**  
Veja links úteis sobre eventos e telas envolvidos neste processo:  
      • [S-1005](http://tdn.totvs.com/display/public/LRM/S-1005)  
      • [S-1280](http://tdn.totvs.com/pages/releaseview.action?pageId=364909345)  
      • [Desoneração da Folha](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028307112)
