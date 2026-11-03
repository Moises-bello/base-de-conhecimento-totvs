---
article_id: 360027700172
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 714eceb794f48625fe8d3a7ca05d1fb6a888b6bde227362ce4d943a2ede49dac
fetched_at: '2026-06-28T22:39:58.548983+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Transmissão
  de NFSE (TXT/XML)
type: support-article
updated_at: '2025-06-10T18:23:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027700172-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Transmiss%C3%A3o-de-NFSE-TXT-XML
---

**Dúvida**Como realizar transmissão para municípios que utilizam a modalidade .TXT e .XML?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução****1.** Gere um Pedido de Vendas e prepare o Documento de Saída;  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068937673/mceclip3.png)  
  
**2.** Entre na rotina FISA022 e acesse o Wizard.cfg, lá será possível definir se o arquivo TXT/XML será salvo em Diretório Local (pasta desejada) ou na pasta padrão FTP do TSS.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068937633/mceclip2.png)  
  
**3.** Feito a configuração completa do Wizard.cfg, realize a a transmissão do RPS. Caso tenha escolhido salvar em diretório local, selecione a pasta desejada;  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068938153/mceclip4.png)  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068939373/mceclip6.png)  
  
**4.** Monitorando o RPS, será apresentado a mensagem para realizar a importação do arquivo validado pela prefeitura;  
  
![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068955973/mceclip10.png)  
  
**5.** Após gerar o arquivo na pasta escolhida, realize o UPLOAD do arquivo no Portal da Prefeitura, onde o mesmo será validado;  
  
**6.** Feito isso, realize o download do arquivo de retorno validado da Prefeitura;  
  
**7.** Salve o arquivo de retorno em alguma pasta;  
  
**8.** Dentro da rotina FISA022, acesse o menu **Outras Ações -> Imp. Retorno**, selecionando o arquivo salvo;  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068955913/mceclip9.png)  
  
**9.** Após ter realizado a importação do arquivo corretamente, monitore o RPS em questão.  
  
![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068959553/mceclip12.png)  
  
**Obs**.: *Vale lembrar que a **Transmissão via TXT/XML é feita por somente algumas prefeituras.** Para a grande maioria o processo é feito via Web Services, onde o retorno da prefeitura é de recebido de forma automática pela rotina.*Poderá verificar a relação através do link abaixo: [-](http://tdn.totvs.com/pages/releaseview.action?pageId=4814340)[Municípios Homologados](http://tdn.totvs.com/pages/releaseview.action?pageId=4814340)
