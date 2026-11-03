---
article_id: 1500004623381
category: TAF - eSocial - Cadastros de empresas
content_hash: 9b06f1b8a704e3f6816cbc64907adb227b8a6c2a716a0baf1e49d0e119234136
fetched_at: '2026-06-28T22:45:16.488059+00:00'
product: protheus
section_id: 1500001547962
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Integração - Não são exibidos os códigos
  de filiais para integração ao TAF
type: support-article
updated_at: '2026-06-23T11:34:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004623381-RH-Linha-Protheus-TAF-eSocial-Integra%C3%A7%C3%A3o-N%C3%A3o-s%C3%A3o-exibidos-os-c%C3%B3digos-de-filiais-para-integra%C3%A7%C3%A3o-ao-TAF
---

**Dúvida**Porque não são exibidos no módulo SIGAGPE os códigos da filiais cadastradas no TAF?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial -Todas as versões  
  
**Solução**

1 - Na rotina de carga inicial no **GPE (GPM023)**, não aparece as filiais para seleção de envio:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006311621)

2 - Para que apareça é preciso estar configurado no complemento cadastral do TAF:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006192222)

3 - Clique em Alterar:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006192302)

4 - Verifique se o código da filial está correto, e se não estiver, faça a correção do mesmo e clique em Salvar para o sistema guardar as informações:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006192382)

5 - Clique na aba Outras Filiais e adicione os seus respectivos códigos de filial para que o módulo SIGAGPE encontre as filiais:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006194262)
