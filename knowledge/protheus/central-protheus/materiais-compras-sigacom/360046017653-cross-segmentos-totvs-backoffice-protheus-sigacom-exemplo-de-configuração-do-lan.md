---
article_id: 360046017653
category: Materiais - Compras (SIGACOM)
content_hash: b60d96ed16c5907dc251a4001e0561f9f2dcb2db8191bc3ce6b7fb4192cfcda1
fetched_at: '2026-06-28T22:41:12.839215+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus -  SIGACOM -  Exemplo de configuração
  do lançamento de Pedido de compras com rateio por centro de custo - 000052/08
type: support-article
updated_at: '2026-01-08T10:56:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046017653-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Exemplo-de-configura%C3%A7%C3%A3o-do-lan%C3%A7amento-de-Pedido-de-compras-com-rateio-por-centro-de-custo-000052-08
---

**Dúvida**  
Exemplo de configuração do Lançamento de Pedido de compras com rateio por centro de custo - 000052/08

**Ambiente**  
Protheus– Compras – A partir da versão 11.80  
  
**Solução**

Integração PCO:

- Ative o parâmetro MV\_PCOINTE = 1" SIM "

**Acesse a rotina PCOA040 e selecione o lançamento 000052/08.**

Para configuração dos lançamento *000052/08*, referente ao valor do lançamento, gentileza utilizar as seguintes configurações:

*-> Configuração do lançamento de bloqueio:*  
AKI\_VALOR1 = GDFieldGet("C7\_TOTAL", nOrigN, Nil, aOrigHeader, aOrigACols) \* (GDFieldGet("CH\_PERC", \_nLinhaR) / 100)  
  
O bloqueio é chamado na validação da linha do rateio (LinhaOk), na validação do grid do rateio (TudoOk) e na validação do grid do pedido (TudoOk), dessa forma, o sistema consegue verificar os valores corretamente.  
  
*-> Configuração do lançamento:*  
AKC\_VALOR1 = Posicione("SC7",1,SCH->CH\_FILIAL+SCH->CH\_PEDIDO+SCH->CH\_ITEMPD,"C7\_TOTAL") \* (SCH->CH\_PERC/100)  
  
O lançamento é chamado na gravação do pedido após os dados já estarem persistidos na base de dados, onde percorre-se item a item do pedido e cada item do rateio e obtemos o valor correspondente ao percentual.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
