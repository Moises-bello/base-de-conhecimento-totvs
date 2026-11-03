---
article_id: 38525483075991
category: Rental by ItUp Business
content_hash: 878d7b2b71e2556e2f0c05c0c60ba07337a47f55c09551b9eea91da4e32a8da7
fetched_at: '2026-06-28T22:36:20.581428+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Como verificar o número do
  pedido de venda do Custo Extra (LOCA007)
type: support-article
updated_at: '2026-02-20T14:52:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38525483075991-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Como-verificar-o-n%C3%BAmero-do-pedido-de-venda-do-Custo-Extra-LOCA007
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38525513204759) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
O Custo Extra (LOCA007) consta com o status de "Faturado". Como consigo localizar o número do Pedido de Venda gerado por esse lançamento?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - Todas as versões.  
  
**Solução**  
Quando um Custo Extra é faturado, o sistema grava o vínculo diretamente na tabela de origem. Para verificar essa informação, siga os passos abaixo:

1. Acesse a rotina **Consulta Genérica** (disponível na maioria dos módulos através do menu Consultas);
2. No campo de busca por tabela, digite **FPG** (Tabela de Custos Extras);
3. Utilize os "filtros" para localizar o registro desejado (ex: filtrar pelo número do Projeto ou da AS);
4. Localize o campo **FPG\_PVNUM** (**Pedido de Venda**);
5. O número contido nesta coluna corresponde ao Pedido de Venda gerado no momento do faturamento do Custo Extra.
