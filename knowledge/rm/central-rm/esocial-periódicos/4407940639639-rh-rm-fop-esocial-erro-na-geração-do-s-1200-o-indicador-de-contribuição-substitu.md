---
article_id: 4407940639639
category: esocial - Periódicos
content_hash: 560bb4addd9310c0bf4557fd2eb86118dcdafa4cafaecdad0e75b90fa398ce62
fetched_at: '2026-06-28T22:47:09.357949+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro na geração do S-1200: O Indicador de Contribuição
  Substituída deve possuir os valores 1, 2 ou 3'
type: support-article
updated_at: '2025-07-02T17:26:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407940639639-RH-RM-FOP-eSocial-Erro-na-gera%C3%A7%C3%A3o-do-S-1200-O-Indicador-de-Contribui%C3%A7%C3%A3o-Substitu%C3%ADda-deve-possuir-os-valores-1-2-ou-3
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24453911067031) Tempo aproximado para leitura: **00:02:30 min****Ocorrência**Ao gerar o XML do S-1200 é apresentado erro: **O Indicador de Contribuição Substituída deve possuir os valores 1, 2 ou 3**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407939207319)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões  
  
**Causa**O erro geralmente ocorre quando não consta preenchido o campo Indicador de Contribuição Substituída no cadastro do funcionário. Tal campo corresponde à *tag* **indSimples**, do Leiaute do S-1200.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24454705995671)

Conforme descrito no Leiaute, o preenchimento da *tag* é obrigatório apenas no caso de empresas optantes pelo **Simples Nacional** com a sua contribuição previdenciária substituída e não substituída (código **03** na **Tabela 8 - Classificação Tributária**, vide abaixo).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24454706001431)

**Solução**Para ajuste do erro citado, siga os passos abaixo:

1. Edite o cadastro do funcionário e acesse o menu lateral **Informações para cálculo | Parâmetros**;  
1.1. Preencha o campo **Indicador de Contribuição Substituída**com uma das opções válidas no leiaute;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24454706007703)

2. Depois de preencher os campos supracitados, o XML será gerado corretamente com o grupo **indSimples** preenchido.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24454706020119)
