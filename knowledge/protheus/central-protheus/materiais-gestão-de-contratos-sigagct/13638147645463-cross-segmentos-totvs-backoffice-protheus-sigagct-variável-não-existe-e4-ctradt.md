---
article_id: 13638147645463
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 522d18b7e925961df876611d4b43366b1275b3bace5c91035180900a8f91cd5d
fetched_at: '2026-06-28T22:37:24.194505+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - variável não existe
  E4_CTRADT na POSITIONE(APLIB080.PRW) 11/04/2022 17:10:46 linha: 4785'
type: support-article
updated_at: '2024-08-13T11:51:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13638147645463-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-vari%C3%A1vel-n%C3%A3o-existe-E4-CTRADT-na-POSITIONE-APLIB080-PRW-11-04-2022-17-10-46-linha-4785
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00**:05:00 min****Ocorrência**Error log: variável não existe E4\_CTRADT na POSITIONE(APLIB080.PRW) 11/04/2022 17:10:46 linha: 4785  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - A partir da versão 12.1.33  
  
**Causa**No módulo de Gestão de Contratos (SIGAGCT) no momento da confirmação da medição de um contrato da rotina Nova Medição **CNTA121**

*variável não existe E4\_CTRADT na POSICIONE(APLIB080.PRW) 04/11/2022 17:10:46 linha : 4785*

Este error.log é causado pela ausência do campo E4\_CTRADT ***no dicionário de dados.*****Solução**  
  
**Solução**

Para solucionar esta ocorrência, execute os seguintes passos:  
1. Entre no menu configurador Banco de Dados\Dicionário\Banco de Dados\Dicionário de Dados;  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10171082570391)  
2. Localize a tabela de condições de pagamento **do SE4** e clique no botão editar;  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13637942982935)  
  
3. Selecione a opção campos e clique no botão **incluir** ;  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13638015810967)  
  
4. Crie o campo E4\_CTRADT, com as seguintes configurações:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13638020304791)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13638028702103)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13638030427799)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13638045257879)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13638047441943)

5. Uma vez que o campo foi criado e salvo, clique no **ícone verde.**

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10171281526295)

6. Após clicar no botão **atualizar banco de dados** , é importante que nenhum usuário esteja utilizando o sistema para que o campo seja cadastrado corretamente.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13638126983319)  
  
7. Valide se o **erro** não ocorre.

Saiba mais:

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - FAQ Gestão de Contratos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115005126608-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-FAQ-Gest%C3%A3o-de-Contratos?source=search)
