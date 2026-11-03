---
article_id: 360028356911
category: ADVPL - Classe e Função
content_hash: f3c447b12b5d1e69154a3f0b506cb8294ecb687217b9c2c7db5ac9f273cdf264
fetched_at: '2026-06-28T22:40:19.128147+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Erro NO _IX Função
  de usuário não compilada no repositório
type: support-article
updated_at: '2022-07-26T04:07:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028356911-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-NO-IX-Fun%C3%A7%C3%A3o-de-usu%C3%A1rio-n%C3%A3o-compilada-no-reposit%C3%B3rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min****Dúvida**Compilei via TDS dois fontes na base teste e quando entro na rotina ele dar erro NO \_IX Função de usuário não compilada no repositório. Porém ao gera o arquivo de fontes através do Shift+F6 e o fonte consta na relação

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028395511/mceclip0.png)  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Verifique as configurações no **catálogo de personalização** no configurador e valide se as funções estão desabilitadas

Acesse a rotina catálogo de personalização (**CFGA030**) no configurador em:  
Ambiente -> Cadastros -> Catálogo de personalização conforme imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028404812/mceclip1.png)

Identifique sua função (ZCADORC), clique em alterar conforme imagem abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028401811/mceclip2.png)

Ao expandir o campo "**Situação**" verifique se a opção está "**Desabilitado**" conforme imagem abaixo. Caso esteja desabilitada selecione a opção está "**Habilitado**":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028405292/mceclip3.png)

**Saiba mais**[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como desabilitar customizações através do catálogo de personalização do Configurador?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018286552)
