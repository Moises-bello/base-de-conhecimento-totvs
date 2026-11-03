---
article_id: 360053916993
category: TAF - REINF
content_hash: 7954abf5ee6aa9f98d62c4c0913a318704f57987b07823a09830f4bd297c73a5
fetched_at: '2026-06-28T22:41:33.410328+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: CROSS Segmentos - Backoffice Linha Protheus - TAF - REINF - Como configurar
  o Reinf no Ambiente de Homologação ou Produção no TAF.
type: support-article
updated_at: '2023-03-30T16:47:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053916993-CROSS-Segmentos-Backoffice-Linha-Protheus-TAF-REINF-Como-configurar-o-Reinf-no-Ambiente-de-Homologa%C3%A7%C3%A3o-ou-Produ%C3%A7%C3%A3o-no-TAF
---

**Dúvida**

Como configurar o **REINF** no ambiente de **Homologação** ou **Produção** no TAF?

**Ambiente**Protheus 11.80 ou superior.  
   
**Solução**Para configurar o **REINF** no ambiente de **Homologação** ou **Produção****,** realize os seguintes passos;  
  
 1. Execute o "smartclient.exe" selecionando o programa inicial **SIGACFG**;

![](http://tdn.totvs.com/download/attachments/334334200/image2017-12-9_13-1-47.png?version=1&modificationDate=1516996331000&api=v2)

![](http://tdn.totvs.com/download/attachments/334334200/image2017-12-9_13-2-53.png?version=1&modificationDate=1516996331000&api=v2)  
 2. Clique em **Ambiente** > **Cadastro** > **Parâmetros;**

![](http://tdn.totvs.com/download/attachments/334334200/image2017-12-9_13-3-26.png?version=1&modificationDate=1516996331000&api=v2)  
 3. Clique em **Pesquisar;**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088048714/mceclip1.png)

4. Pesquise pelo parâmetro **MV\_TAFAMBR** e edite;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089178213/mceclip0.png)

5. Ajustar o parâmetro **MV\_TAFAMBR** com os seguintes conteúdos nos campos “**Cont.Por**” e salve:

1- **Produção** - (Ambiente de **Produção**);

2- **Pré-produção** - dados reais - (Ambiente de **Homologação**);

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089178313/mceclip2.png)

6. Acesse o TAF - Totvs Automação Fiscal, clique em **Configs.TAF** > **Wizard Configs. TSS**:

![](http://tdn.totvs.com/download/attachments/334334200/image2018-2-23_12-14-58.png?version=1&modificationDate=1519398899000&api=v2)

7. Informe a **URL** e o tipo de **Ambiente** nos campos abaixo:

1- **Produção** - (Ambiente de **Produção**);

2- **Pré-produção** - dados reais - (Ambiente de **Homologação**);

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088048994/mceclip3.png)
