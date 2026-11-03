---
article_id: 360051968154
category: RH - Contabilização
content_hash: c148682e7069c5d32814514d2dc7dea3d5677247381e18d4b3ae0ebb13a82f74
fetched_at: '2026-06-28T22:43:46.155603+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Reprocessamento da rotina PCOA310 - Processo 000085
type: support-article
updated_at: '2021-06-07T13:24:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051968154-RH-Linha-Protheus-GPE-Reprocessamento-da-rotina-PCOA310-Processo-000085
---

**Dúvida**Ao reprocessar a rotina PCOA310 do Processo 000085 (folha), o sistema apresenta todas as verbas do Acumulado (tabela SRD) e não apenas as verbas configuradas para o PCO.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Acessar a Rotina PCOA310, PCO ->Miscelânea -> Reprocessamentos-> Lançamentos.  
Posicionar sobre o processo e clicar em Reprocessar.    
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084426373/mceclip0.png)

2. Será apresentada a tela de filtro para reprocessamento das verbas do Acumulado (tabela SRD). Caso **o filtro não seja aplicado, esse reprocessamento****apresentará todas as verbas do acumulado (tabela SRD)**, desconsiderando o cadastro da Verba na tabela SRV (RV\_LANCPCO), uma vez que foi desenhada para integração,  por exemplo na implantação do PCO no meio do ano e necessite integrar a partir de janeiro.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083266534/mceclip2.png)  
  
Preencher os Campos, Período de?/ Período Ate?   
  
Dentro do período deve ser informado o filtro que a rotina deverá executar na tabela Origem, em nosso exemplo a tabela SRD, podendo ser utilizado por exemplo : data de pagamento, roteiro, competência e verbas, entre outros.   
  
Clique em Editar e defina o filtro do que irá reprocessar.
