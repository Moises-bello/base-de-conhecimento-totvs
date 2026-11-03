---
article_id: 360053217454
category: RH - Integração de Titulo
content_hash: 9e549c6036d47db5b88c82c72fb6f3319219a8c09982b212513004429b514227
fetched_at: '2026-06-28T22:43:36.449791+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema permite integrar títulos com data anterior
  ao informado no parâmetro MV_DATAFIN
type: support-article
updated_at: '2025-07-23T20:07:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053217454-RH-Linha-Protheus-GPE-Sistema-permite-integrar-t%C3%ADtulos-com-data-anterior-ao-informado-no-par%C3%A2metro-MV-DATAFIN
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33657898637975)**Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Sistema permite integrar títulos com data anterior ao informado no parâmetro MV\_DATAFIN.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17.  
  
**Solução**  
O parâmetro **MV\_DATAFIN** determina a data em que serão iniciadas as movimentações financeiras.

Para as operações de inclusão, exclusão e alterações de Contas a Receber e a Pagar FINA040 e  **FINA050**, o Sistema sempre verifica a data definida no parâmetro **MV\_DATAFIN**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088568274)

Caso a data da operação seja inferior à data definida no parâmetro, não será permitido realizar nenhuma destas operações, independente do tipo de documento utilizado - NF, PA, RA, BOL, etc.  
 **Exemplo:** **MV\_DATAFIN** = 20200801

Se informar data base dia 01/08/2020 o sistema permite realizar inclusão nesta data, porem não permite dia 31/07/2020 para trás.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088569334)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089720893)

**Saiba Mais:**  
[Artigos sobre Integração de Título](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
