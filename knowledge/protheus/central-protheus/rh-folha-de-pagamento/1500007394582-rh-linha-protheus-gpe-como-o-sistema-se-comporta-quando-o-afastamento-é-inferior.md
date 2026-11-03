---
article_id: 1500007394582
category: RH - Folha de Pagamento
content_hash: 3535070b2fdf4699c6a43ee584eba6d6261fa5b60be540a8bf3ebb20efcaf7e4
fetched_at: '2026-06-28T22:44:13.602574+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como o sistema se comporta quando o afastamento
  é inferior a 15 dias e outro superior a 15 dias (com sequência)
type: support-article
updated_at: '2025-10-08T22:53:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007394582-RH-Linha-Protheus-GPE-Como-o-sistema-se-comporta-quando-o-afastamento-%C3%A9-inferior-a-15-dias-e-outro-superior-a-15-dias-com-sequ%C3%AAncia
---

**Dúvida**  
Como o sistema se comporta quando o **afastamento é inferior a 15 dias e outro superior a 15 dias (com sequência)?**

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

No exemplo foi informado o **tipo de ausência 004** para **afastamento inferior a 15 dias** e outro **superior a 15 dias (com sequência)**:

![](https://tdn.totvs.com/download/attachments/608545018/image2021-4-12_22-22-31.png?version=1&modificationDate=1618276954930&api=v2)

O afastamento de **2 dias continuou na verba padrão** e o **afastamento que passou de 15 dias foi pago na verba informada no campo RCM\_PDSUP** do tipo de ausência. O valor da verba nova não entrou na base para o desconto de INSS e da contribuição patronal:

Verba 747 = 28,88% X R$ 600,00= R$ 173,28

![](https://tdn.totvs.com/download/attachments/608545018/image2021-4-12_22-23-11.png?version=1&modificationDate=1618276995013&api=v2)  
  
  
**Saiba Mais**  
Acesse o *link* a seguir para documentação completa: <https://tdn.totvs.com/pages/releaseview.action?pageId=608545018#Exemplosdec%C3%A1lculo-1811452821>
