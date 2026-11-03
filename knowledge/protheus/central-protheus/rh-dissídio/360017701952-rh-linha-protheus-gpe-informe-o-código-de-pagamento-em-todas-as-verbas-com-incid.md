---
article_id: 360017701952
category: RH - Dissídio
content_hash: b60d8592a8917dbe10cf0fd3b7a60dffb486a43308b5beafbc60bc8ba4aa6a69
fetched_at: '2026-06-28T22:43:44.241502+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Informe o código de pagamento em todas as verbas
  com incidência para o dissidio
type: support-article
updated_at: '2025-08-20T14:30:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017701952-RH-Linha-Protheus-GPE-Informe-o-c%C3%B3digo-de-pagamento-em-todas-as-verbas-com-incid%C3%AAncia-para-o-dissidio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34317201302807) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Ao calcular o dissídio apresenta a mensagem: "Informe o código de pagamento em todas as verbas com incidência para o dissidio. Somente após este procedimento o calculo poderá ser efetuado.“ O que fazer?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12  
  
**Solução**Esta mensagem é exibida devido a existir verbas, onde na aba Dissídio Retroativo, o campo Dissídio Retroativo (RV\_COMPL\_) está com **Sim** e no campo  Verba p/ Dissídio (RV\_CODCOM\_) não há verba preenchida, conforme a imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013200772)

Para solucionar essa dúvida, realize os seguintes passos:

1. Para saber qual é, mais facilmente, acesse Consultas - Cadastros - Genéricos;  
  
2. Abra a tabela SRV (Verbas);  
  
3. Vá em Filtrar - e crie o seguinte Filtro:

Dissid. Ret = S - adiciona

e - Adicionar

Verb. P. Diss = ( Branco ) - Adiciona.

Temos na documentação abaixo uma sugestão de vinculo para as principais verbas. Importante ressaltar que é apenas uma sugestão, o usuário que estiver realizando a configuração pode vincular as verbas, principalmente as verbas particulares da empresa como bônus e premiações na verba que quiser visualizar a diferença na folha de pagamento.

[MP - GPE - Qual a configuração que antecede o cálculo do dissídio retroativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054351414-MP-GPE-Qual-a-configura%C3%A7%C3%A3o-que-antecede-o-c%C3%A1lculo-do-diss%C3%ADdio-retroativo?source=search)

Saiba Mais:  
[Página Centralizadora do Dissídio (GPEM690)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)
