---
article_id: 4416749179159
category: Gestão de Armazenagem (WMS)
content_hash: 4e91baafc54f30044800724762a63c7a3fc5564662957fee9ee3320eab032202
fetched_at: '2026-06-28T22:45:48.186017+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Logística - Linha Protheus - WMS - WMSA520 não permite a troca para produto
  com controle de localização e sem controle de WMS
type: support-article
updated_at: '2022-04-06T18:37:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416749179159-Log%C3%ADstica-Linha-Protheus-WMS-WMSA520-n%C3%A3o-permite-a-troca-para-produto-com-controle-de-localiza%C3%A7%C3%A3o-e-sem-controle-de-WMS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:20 min** **Dúvida** **WMSA520 - Troca de Produto** não permite a troca para produto com controle de localização e sem controle de **WMS**?  
  
**Ambiente**TOTVS Logística - TOTVS WMS (Linha Protheus) - Gestão de Armazenagem (SIGAWMS) -  A partir da versão 12  
  
**Solução**A mensagem **WMSA52022 - Produtos com controle de localização e sem controle de WMS não são permitidos para a troca -** é apresentada devido a regra de negócio do produto padrão, que determina que é possível trocar apenas para um produto que não controle **WMS - *Warehouse Management System* -** e não controle localização, visto que a rotina de **troca de produto** realiza a alocação automática no mesmo endereço que o produto origem se encontra.

![WMSA520.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4416749253527/WMSA520.PNG)

Nos casos que não atendem a regra acima, deve ser efetuada a retirada do produto no armazém, via requisição ou pedido e, então, a entrada do novo produto, via documento de entrada, devolução ou inventário.  
  
**Saiba mais**  
Veja mais informações a respeito no *link* da documentação a seguir: [8682571 DLOGWMSMSP-9785 DT Alteração para permitir desmontar produto que não controla WMS (WMSA520)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=546260142)
