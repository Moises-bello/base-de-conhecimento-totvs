---
article_id: 1500008007141
category: REQUISIÇÕES
content_hash: d5ab96887dee8be5cd72cb43624f14f34b85dcaeb09ac0403b045aaf64b501cf
fetched_at: '2026-06-28T22:44:37.642184+00:00'
product: protheus
section_id: 10299632459799
source: central-protheus
title: RH - Linha Protheus - MEU RH - Para qual e-mail é enviado WorkFlow de solicitações
  realizadas através do MEU RH
type: support-article
updated_at: '2025-09-16T17:54:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008007141-RH-Linha-Protheus-MEU-RH-Para-qual-e-mail-%C3%A9-enviado-WorkFlow-de-solicita%C3%A7%C3%B5es-realizadas-atrav%C3%A9s-do-MEU-RH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24762662858007)Tempo aproximado para leitura: 00:01:00 min****Dúvida**Para qual e-mail é enviado *WorkFlow* de solicitações realizadas através do MEU RH?  
  
**Ambiente**TOTVS RH (Linha Protheus) - MEU RH - Todas as versões  
  
**Solução**1. No MEU RH quando é realizado solicitações como por exemplo, realizar a inclusão de batida de ponto no espelho de ponto, é encaminhado um e-mail para o gestor informando que existem batidas para serem aprovadas, isso ocorre de acordo com a estrutura de hierarquia para aprovação que a empresa utiliza.  
  
**Para saber mais como configurar o *Workflow* acesse:**  
[MP - MEU RH - Como configurar o E-mail de Workflow de solicitações do MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055230453-MP-MEU-RH-Como-configurar-o-E-mail-de-Workflow-de-solicita%C3%A7%C3%B5es-do-MEU-RH?source=search)  
  
2. Caso a empresa utilize estrutura de hierarquia para aprovação das solicitações, será encaminhado um e-mail para o gestor, será enviado o workflow para o e-mail que esta configurado na RD0 campo RD0\_EMAIL, esse campo por padrão utiliza o DE/PARA do campo RA\_EMAIL.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24762662862743)  
  
3. O relacionamento dos campos da SRA e RD0 é realizado através do arquivo MSRELRDZ que se encontra na pasta system do Protheus, a tabela de relacionamento entre esses cadastros é a RDZ.  
  
[RH - Linha Protheus - APD - Como conferir relacionamento do funcionário com o participante](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024677334-RH-Linha-Protheus-APD-Como-conferir-relacionamento-do-funcion%C3%A1rio-com-o-participante?source=search)  
  
**Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
