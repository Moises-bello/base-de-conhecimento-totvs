---
article_id: 20316460881175
category: Originação de Grãos (OG)
content_hash: e276b0088ee87f82b0e87468923c3c98013fdef035923f3a185be693b27d4626
fetched_at: '2026-06-28T22:45:45.230357+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Venda - Geração de romaneio com o controle físico
  ou fiscal
type: support-article
updated_at: '2025-06-13T21:09:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20316460881175-Agro-Linha-Protheus-AGR-Venda-Gera%C3%A7%C3%A3o-de-romaneio-com-o-controle-f%C3%ADsico-ou-fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20316460859671) Tempo aproximado para leitura: **00:00:50 min****Ocorrência**  
No módulo **Comercialização (Linha Protheus) - Originação de Grãos (OG)**, ao realizar o processo para gerar romaneios de venda é apresentada a ocorrência **Geração de romaneio sem a quantidade física e somente com a quantidade fiscal**.  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Causa**Esse incidente ocorre, pois é preciso realizar o processo para gerar romaneios de venda no Sistema.  
  
**Solução**  
Para solucionar essa ocorrência, realize o cenário, **romaneio de venda** com parâmetro **MV\_AGOCLAS - Utiliza classificação por Local** ativo:  
Realizado uma **saída por venda** gerando uma **NF - Nota Fiscal** com quantidade estimada de **kg 20.000**. No **destino/cliente** ao receber realiza a pesagem de **Kg - Quilograma** **25.000**, uma divergência de **Kg** **5.000**.  
No Sistema registro no romaneio de saída que a quantidade de destino foi **Kg 25.000** para controle, nas quantidade e saldos de saída do contrato fica registrado esta divergência.  
Necessário gerar uma **NF** **de saída para complementar** o excedente de **Kg 5.000** recebido pelo cliente, esta **NF** pode ser gerado pelo romaneio sem pesagem somente com a quantidade fiscal.  
  
**Saiba mais**  
Para maiores informações acesse:

[Agro - Linha Protheus - AGR - Gerar romaneio sem quantidade física](https://totvssuporte.zendesk.com/knowledge/articles/10651731363479/pt-br?brand_id=1509248)   
[Agro - Linha Protheus - AGR - Gerar romaneio sem quantidade física - Compra](https://totvssuporte.zendesk.com/knowledge/articles/10932935018391/pt-br?brand_id=1509248)
