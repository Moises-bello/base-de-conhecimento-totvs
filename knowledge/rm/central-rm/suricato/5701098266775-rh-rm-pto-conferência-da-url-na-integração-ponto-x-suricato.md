---
article_id: 5701098266775
category: Suricato
content_hash: 42df5c930b5b9edfa35610c9413d34abcd714a5cabbafdc6f4b2f89146a1b559
fetched_at: '2026-06-28T22:46:26.394977+00:00'
product: rm
section_id: 28312167464215
source: central-rm
title: RH - RM - PTO - Conferência da URL na Integração Ponto x Suricato
type: support-article
updated_at: '2025-09-05T19:46:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5701098266775-RH-RM-PTO-Confer%C3%AAncia-da-URL-na-Integra%C3%A7%C3%A3o-Ponto-x-Suricato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19409202454423) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como realizar a conferência da URL para integração do RM Automação de Ponto com o Suricato?   
  
**Ambiente**  
RH - RH (Linha RM) - TOTVS Automação de Ponto - A partir da 12.1.  
  
**Solução**

Para realizar a conferência, siga os passos abaixo:

1. Abra o IIS (Gerenciador de Serviços de Informação da internet) e selecione o site TSA. Clique no botão **Procurar \*80(http)**:   
     
   ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5700506712215)  
     
   Deverá ser aberta uma página, igual à imagem abaixo:   
     
   ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5700503272087)  
     
   Caso abra, clique na URL e após **localhost/TSA/**, complemente o link com **/tsservice.asmx,** como no exemplo abaixo:  
     
   **http://localhost/TSA/tsservice.asmx**Verifique se abrirá a página abaixo:  
    **![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5700677256599)**
2. Em seguida, acesse no módulo de Integração o menu **Ferramentas | Parâmetros** e selecione o processo **50.01 - Configurações Gerais ByYouESB**:  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/13810414445463)  
     
   Confira se no campo **URL do WebService RM** o endereço informado é o mesmo do navegador:   
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/13810540411671)  
     
   *Observação: Como será aberto localhost, altere para o IP ou nome do servidor*  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/13807327497495)
3. Por fim, confira também no arquivo **Web.config** do webservice RM **(caminho padrão C:\TSA)** se os links dos serviços do Suricato estão corretos :

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5700902421143)

**Saiba mais**

[RH - RM - PTO - Instalação e configuração do Webservice RM para integração com o Suricato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27720600761367)

[RH - RM - PTO - Configuração do RM para integrar com o sistema Suricato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27719956683927)
