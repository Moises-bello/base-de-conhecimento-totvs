---
article_id: 26614289927831
category: Financeiro - Comissão
content_hash: 8cca1641bd420b2ad405919811c5d060c1a3f4ab57bb7d557a13b06d78756f97
fetched_at: '2026-06-28T22:37:50.876435+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - MATA490 - Cancelar
  comissão sem interface
type: support-article
updated_at: '2024-09-27T12:42:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26614289927831-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-MATA490-Cancelar-comiss%C3%A3o-sem-interface
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26616539617559) Tempo aproximado para leitura: **00:05:00****min**

**Dúvida**  
Como cancelar uma comissão paga sem interface de pagamento configurada no cadastro de vendedor?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**

Por padrão, não é possível cancelar a comissão que não esteja vinculada ao **Cadastro do Fornecedor** ou **folha de pagamento**.

Ao tentar excluir o pagamento na manutenção de comissões, será exibida o **HELP: A490COMPAG**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26614650864279)

Neste caso, é necessário cancelar a baixa do título para que a comissão seja gerada novamente.

**Importante**

Quando o pagamento da comissão ocorre, mesmo que o parâmetro **MV\_COMIDEV** esteja definido como **F**, uma comissão negativa será gerada, pois o pagamento foi realizado. Caso o pagamento não tivesse ocorrido, a comissão seria excluída.

**Saiba mais**

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Pontos de Entrada da rotina MATA490](Cross%20Segmento%20-%20TOTVS%20Backoffice%20(Linha%20Protheus)%20-%20SIGAFAT%20-%20Pontos%20de%20Entrada%20da%20rotina%20MATA490)
