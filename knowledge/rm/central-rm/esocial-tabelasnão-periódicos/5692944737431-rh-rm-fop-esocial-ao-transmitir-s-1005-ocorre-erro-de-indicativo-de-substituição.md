---
article_id: 5692944737431
category: eSocial - Tabelas/Não Periódicos
content_hash: 0feddca6921c92e719acae9f64d048f70bdc89e294fdb076c3c42fcf209de54d
fetched_at: '2026-06-28T22:47:10.260484+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RH - RM - FOP - eSocial - Ao transmitir S-1005 ocorre  erro de Indicativo de
  substituição da contribuição patronal deve ser preenchido
type: support-article
updated_at: '2025-07-02T17:24:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5692944737431-RH-RM-FOP-eSocial-Ao-transmitir-S-1005-ocorre-erro-de-Indicativo-de-substitui%C3%A7%C3%A3o-da-contribui%C3%A7%C3%A3o-patronal-deve-ser-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24456131812887) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao transmitir o evento S-1005 ocorre o Erro **O evento ID: xxxxxx foi rejeitado pelo RET. Erro código 8: Grupo #39;Indicativo de substituicao da contribuicao Patronal#39; deve ser preenchido. Localização: /eSocial/evtTabEstab/infoEstab/inclusao/dadosEstab.**

![llllll.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/5700440378007)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - 12.1.29.284, 12.1.31.199, 12.1.32.136 e superiores   
  
**Causa**Esse incidente ocorre, pois no leiaute 1.0 é obrigatório o preenchimento da *tag* **indSubstPatrObra**, caso o S-1000 tenha sido enviado com a *tag* indConstr igual à 1 e a *tag* **indDesFolha** igual à 1, e evento S-1005 esteja com a *tag* **ideEstab/tpInsc** esteja preenchida como 4.

Leiaute S-1.0

![eu.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/5700954549143)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5680487627415)

**Solução**Para solucionar essa ocorrência, realize as seguintes validações:  
1. Acesse **eSocial | Informações do Empregador** e verifique se o campo **Indicativo de Desoneração da Folha** e **Indicativo de construtora** estão preenchidos corretamente;

![2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/5701317419287)

2. Verifique em **Administração de Pessoal | Cliente e Fornecedor | Anexo | eSocial** se a opção **Obra Própria** está selecionada;

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5692914004247)

3. Acesse **Administração de Pessoal | Cliente e Fornecedor | CEI do Cliente/ Fornecedor**, faça a edição do CNO desejado após acesse **Anexo | eSocial** e preencha o campo **Indicativo de Substituição da Contribuição Patronal de Obra de Construção Civil**;

![cei.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5701759574295)

4. Após gere novamente o XML do S-1005 e envie ao eSocial.  
  
**Saiba mais**Para mais informações acesse:

 • [Como desonerar uma empresa no eSocial?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028307112)  
 • [Desoneração de CNO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028548251-RM-eSocial-Desonera%C3%A7%C3%A3o-de-CNO)
