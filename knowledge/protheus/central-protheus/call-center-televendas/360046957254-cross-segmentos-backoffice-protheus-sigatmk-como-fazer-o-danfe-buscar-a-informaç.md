---
article_id: 360046957254
category: Call Center - Televendas
content_hash: 91d756a41141a14534a73fcf1dcd7c8a09d24086938a598c94ebb2780350451a
fetched_at: '2026-06-28T22:41:30.242512+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - Como fazer o Danfe buscar
  a informação do campo UA_ENDENT
type: support-article
updated_at: '2024-04-29T13:06:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046957254-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Como-fazer-o-Danfe-buscar-a-informa%C3%A7%C3%A3o-do-campo-UA-ENDENT
---

**Dúvida**

Após alterar o campo **UA\_ENDENT** da condição de pagamento do atendimento televendas(**TMKA273**), ao faturar a nota e gerar o **Danfe**, o endereço de entrega  permaneceu o cadastro do cliente (**MATA030**). Como fazer o Danfe buscar a informação do campo **UA\_ENDENT**?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGATMK - A partir da release 12

**Solução**

Não há parametrização para essa busca , por que o **Xml**  que é gerado na transmissão da nota, busca a informação do **endereço de entrega** do campo **A1\_ENDENT, do cadastro de cliente.**

No Call Center, por padrão de sistema, o campo **UA\_ENDENT** também recebe  a informação do campo **A1\_ENDENT**, portanto, se mudar apenas no Call Center, no momento do atendimento **televendas**,  não será enviada nenhuma mudança para o Xml do programa **Spednfe**, uma vez que a informação buscada está no campo **A1\_ENDENT**e não no campo **UA\_ENDENT** , posteriormente, o Xml é quem envia a informação para o **Danfe**.  
  
No Sped, para geração do Danfe, existe o parâmetro **MV\_NFEDEST** (**[MP - NFE - Como gerar as TAGS de cliente de entrega e cliente de retirada no XML ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028872711-MP-NFE-Como-gerar-as-TAGS-de-cliente-de-entrega-e-cliente-de-retirada-no-XML-?source=search)**) para considerar o endereço entrega do Pedido de vendas (**MATA410**) ao invés do cadastro do cliente, porém, não há tratamento similar para o atendimento do Call Center.  
  
O tratamento teria que partir da rotina de **SPED** para considerar uma informação no Xml diferente da tabela  **SA1** de cadastro de cliente, neste caso, teria que ajustar o Xml para buscar o campo **UA\_ENDENT**(*em caso de dúvidas para esse processo contate a equipe de atendimento **SED/TSS**.)*  
  
Diferente disso, teria que alterar diretamente no cadastro do cliente, o campo **A1\_ENDENT,** com o mesmo endereço que utiliza no Call Center, no campo **UA\_ENDENT.**
