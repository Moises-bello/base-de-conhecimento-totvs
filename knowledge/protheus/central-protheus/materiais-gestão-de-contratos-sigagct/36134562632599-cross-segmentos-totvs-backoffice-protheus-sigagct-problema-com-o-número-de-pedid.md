---
article_id: 36134562632599
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 31adf2bed5d926eeba43d0ec19247ab58c77dda82fe2d230fefd9f0e3e63004c
fetched_at: '2026-06-28T22:37:24.047128+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Problema com o número
  de Pedido de Compras gerado ao Encerrar e ao Estornar a Medição
type: support-article
updated_at: '2026-01-19T15:11:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36134562632599-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Problema-com-o-n%C3%BAmero-de-Pedido-de-Compras-gerado-ao-Encerrar-e-ao-Estornar-a-Medi%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36134562624151) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Ao gerar a gravação do pedido de compra ao encerrar a medição, o sistema apresenta um número de pedido de compra diferente do que foi gerado, e ao Estornar esta medição deste pedido de compra gerado, o sistema não está executando a operação, retornando a mensagem abaixo, com "C7\_NUM := "em branco" pesquisa não encontrada com os dados acima":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36134562625047)

**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**

Conforme ocorrências existentes da mesma mensagem, no caso da medição em específico, orienta-se a verificação e analise dos registros das tabelas CXJ e CNE, se as mesmas possuem as informações corretas no campos CXJ\_NUMPED, CXJ\_ITEMPE e CNE\_PEDIDO do Pedido gerado na tabela SC7 no encerramento desta medição, e caso não estejam preenchidos pode-se fazer o teste em homologação realizando o devido preenchimento/manutenção do registro com o numero do pedido que de fato foi gerado pela medição nesses campos, e posteriormente realizando um novo teste como estorno da medição, verificando se a mensagem no estorno não mais ocorre.

Para manutenção de registros em banco de dados, orienta-se a realização por analista com conhecimento do processo, e caso necessário, verificar o apoio por um analista especialista em loco, junto ao ESN Totvs que lhes atendem.

Caso na realização de novas medições e encerramentos esteja ocorrendo sem a gravação destes campos, **conforme ocorrências mapeadas desta situação**, orienta-se a aplicação e teste em **ambiente de homologação realizando um novo processo de inclusão de medição desde o inicio**, além do pacote atual do SIGAGCT,**com também o pacote mais atuais do SIGACOM** e demais abaixo, que estão de acordo com o teste que realizamos e a medição foi incluída e encerrada corretamente.  
   
- GCT: <https://tdn.totvs.com/pages/releaseview.action?pageId=679961416>  
- COM: <https://tdn.totvs.com/pages/viewpage.action?pageId=522011099>  
   
   
Aplicar sempre mantendo os fontes mais atuais na aplicação e realizar um novo cadastro de medição.  
   
 

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Documentação Gestão de Contratos do TDN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4441027145623)

[Guia de Referencia - Gestão de Contratos - Protheus 12](https://tdn.totvs.com/pages/viewpage.action?pageId=224127467)

[FAQs - Gestão de Contratos](https://tdn.totvs.com/x/O_tgDQ)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
