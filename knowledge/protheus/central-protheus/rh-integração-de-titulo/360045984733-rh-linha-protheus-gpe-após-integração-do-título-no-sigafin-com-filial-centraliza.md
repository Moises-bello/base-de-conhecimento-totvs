---
article_id: 360045984733
category: RH - Integração de Titulo
content_hash: 88d612c4a14f4c1bd6699045b7cb332d02a52525aa316e5fdeffd1b0ff1bcac1
fetched_at: '2026-06-28T22:43:36.152156+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Após integração do título no SIGAFIN com filial
  centralizada, não é possível a exclusão pelo módulo SIGAGPE
type: support-article
updated_at: '2025-07-24T14:22:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045984733-RH-Linha-Protheus-GPE-Ap%C3%B3s-integra%C3%A7%C3%A3o-do-t%C3%ADtulo-no-SIGAFIN-com-filial-centralizada-n%C3%A3o-%C3%A9-poss%C3%ADvel-a-exclus%C3%A3o-pelo-m%C3%B3dulo-SIGAGPE
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33686636835351)**Tempo aproximado para leitura:00:02:00 min

**Dúvida**Após integração do título no SIGAFIN não é possível a exclusão pelo módulo SIGAGPE.

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de  Pessoal – A partir da versão 12.  
  
**Solução**

Na integração dos títulos com o financeiro, é enviada apenas a filial centralizadora e não a filial de origem do título.  
**Rotina GPEM670**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360064410933)

**Gravação do campo E2\_FILORIG:**  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063427554)  
  
Para que não seja perdida a referência do título que foi integrado, o campo **RC1\_FILCEN** também deverá gravar a filial que foi enviada para o financeiro no momento da integração.

**Tabela RC1 e manutenção de títulos:  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360064413593)  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360064413773)**

**Importante:**Caso o campo não seja preenchido,**a integração será realizada de forma correta (já com a correção)**, porém a rastreabilidade do título no financeiro poderá ser perdida e nesse caso, após integração do título não será mais possível a sua exclusão pelo módulo SIGAGPE.

Para ajuste, **os títulos que foram integrados anteriormente terão que ser integrados novamente** para que o processo de gravação ocorra corretamente , conforme apresentado acima. 

**Saiba Mais**  
[Artigos sobre Integração de Título](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
