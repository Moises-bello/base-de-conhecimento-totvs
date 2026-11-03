---
article_id: 1500000672781
category: PONTO ELETRÔNICO
content_hash: 198a47d4fc8cdce6e4e0849430757b78fd011ad98fec6f3b928ecaad54dc2946
fetched_at: '2026-06-28T22:44:36.721557+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - MEU RH - Qual a configuração para definir o período de
  manutenção das batidas\marcações
type: support-article
updated_at: '2022-11-18T16:45:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000672781-RH-Linha-Protheus-MEU-RH-Qual-a-configura%C3%A7%C3%A3o-para-definir-o-per%C3%ADodo-de-manuten%C3%A7%C3%A3o-das-batidas-marca%C3%A7%C3%B5es
---

**Dúvida**Qual a configuração para definir o período de manutenção das batidas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - MEU RH - A partir da versão 12.33  
  
**Solução**O sistema usa os parâmetros MV\_DABERTO, MV\_PAPONTA e MV\_PONMES.  
  
1) **MV\_PAPONTA** - Período para apontamento das marcações  
  
2) **MV\_PONMES** - Período de Apontamento em aberto para a apuração das marcações/apontamentos no Ponto eletrônico.   
  
3) **MV\_DABERTO** - Informe a quantidade de dias corridos após o fim do período para manutenção do ponto pelos funcionários.   
  
Exemplo prático:  
Parâmetro MV\_DABERTO = 2  
Período de apontamento: 01/07/2022 a 31/07/2022  
  
O período, efetivamente, termina em 31/07, com o MV\_DABERTO = 2, **serão adicionados mais 2 dias**, formando uma nova data de término em 02/08/2022.   
  
Assim, os usuários poderão realizar manutenção das marcações do período até essa data. E a partir do dia 03/08/2022 não será mais possível realizar nenhuma manutenção.  
  
**Saiba Mais**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)  
[**CLIQUE AQUI** como configurar: MV\_PAPONTA e MV\_PONMES](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115015809548-MP-PON-Per%C3%ADodo-de-apontamento-desconfigurado-Como-configurar-MV-PAPONTA-e-MV-PONMES)
