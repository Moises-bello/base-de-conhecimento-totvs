---
article_id: 1500004687862
category: Anuais
content_hash: 13ef0b5eb669ca83363ffc8af136a79d59d969ff64dd41daa7bdb8ca581e42cd
fetched_at: '2026-06-28T22:46:51.162654+00:00'
product: rm
section_id: 1500000861142
source: central-rm
title: 'RH - RM - FOP -  RAIS: O arquivo não atende as especificações definidas para
  o ano-base'
type: support-article
updated_at: '2025-03-14T10:04:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004687862-RH-RM-FOP-RAIS-O-arquivo-n%C3%A3o-atende-as-especifica%C3%A7%C3%B5es-definidas-para-o-ano-base
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Ao realizar a importação do arquivo no validador da RAIS, ocorre a seguinte inconsistência: **O arquivo não atende as especificações definidas para o ano-base:****![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006221161/mceclip0.png)****Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Essa situação ocorre devido ao arquivo conter informações que estão em desacordo com o ***layout***para o ano-base.  
  
**Solução**Como o erro é genérico e pode se tratar de qualquer dado incorreto, o usuário deverá acessar o **GDRAIS** na opção **Utilitários - Analisador de Arquivo RAIS** para verificar quais as informações estão em desacordo com o layout do ano-base. Ao validar o arquivo, a inconsistência será apresentada em tela.  
  
Exemplo:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006106302/mceclip1.png)  
  
Nesta tela, o validador apresentará os erros que impedem a transmissão do arquivo gerado. O erro pode estar relacionado a dados preenchidos incorretamente no sistema ou configuração indevida na emissão. Veja nossas documentações sobre [Parametrização](https://tdn.totvs.com/pages/releaseview.action?pageId=223159978) e [Emissão](https://tdn.totvs.com/pages/releaseview.action?pageId=223159688) da RAIS para maiores dúvidas.  
  
**Saiba mais**[RH - RM - FOP - RAIS: Versões para geração da RAIS 2022 Ano-Base 2021](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024451952)

***Informações gerais sobre a RAIS 2022*** *Foi publicado no* [*Portal da RAIS*](https://www.rais.gov.br/sitio/index.jsf) *no dia 15/03/2022 o Manual e o Leiaute relativos ao Ano Base 2021. A adequação é apenas no campo de identificação do trabalhador* ***PIS/PASEP/NIT****, passando a ser facultativo, de acordo com o Manual de Orientação da RAIS ano-base 2021. O Programa Validador da RAIS –* ***GDRAIS2022****, está disponível no portal para download, então já é possível preparar-se para a transmissão da RAIS, uma vez que* ***para a linha RM, não será necessária adequação do produto****. As versões que atenderão a rotina serão as mesmas que atenderam a DIRF 2022:*

* *12.1.32.241 ou superiores;*
* *12.1.33.178 ou superiores;*
* *12.1.34.100 ou superiores.*

*Ressaltamos que, a entrega da RAIS para os Grupos 1 e 2 já foram substituídas pelo envio mensal dos eventos de remuneração no eSocial desde 2019, e para estes grupos está bloqueado o envio através do GDRAIS.*
