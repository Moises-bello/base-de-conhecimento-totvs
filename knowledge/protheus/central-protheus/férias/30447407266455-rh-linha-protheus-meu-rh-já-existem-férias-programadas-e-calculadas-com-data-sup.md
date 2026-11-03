---
article_id: 30447407266455
category: FÉRIAS
content_hash: c8a97b309340fe0439b912bb3738f62290369c7395b0a1203cfe3249af5d4410
fetched_at: '2026-06-28T22:44:34.488427+00:00'
product: protheus
section_id: 10299705719575
source: central-protheus
title: RH - Linha Protheus - Meu RH - Já existem férias programadas e calculadas com
  data superior. O que analisar nesse cenário, após aprovar férias.
type: support-article
updated_at: '2025-11-05T21:03:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30447407266455-RH-Linha-Protheus-Meu-RH-J%C3%A1-existem-f%C3%A9rias-programadas-e-calculadas-com-data-superior-O-que-analisar-nesse-cen%C3%A1rio-ap%C3%B3s-aprovar-f%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30447407244055) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Já existem férias programadas e calculadas com data superior. O que analisar nesse cenário, após tentativa de aprovar férias, vindas do App Meu RH?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**Ao aprovar férias no módulo 07, proveniente do App Meu RH, a rotina traz este alerta.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30447407247255)  
  
Há uma condição onde se não houver nenhuma programação e dados na SRH, tabela de cálculo de férias, os pedidos de férias precisam ter uma ordem cronológica.  
  
No caso, essa validação ocorre pois há uma requisição de férias realmente com data maior que a registrada.  
  
**Exemplo:**  
Um funcionário tem férias já programadas nos campos de 1ª programação para Julho/2025 com 10 dias de programação, essa solicitação está aprovada e já entrou no Controle de Dias de Direito nos campos de 1ª programação.   
  
Se o funcionário solicitou nesse caso uma programação de 10 dias para Julho/2025, a 2ª programação por uma questão cronológica só pode ser superior à data de retorno deste primeiro pedido.  
Com isso, se o funcionário tentar solicitar férias como 2ª programação para Abril/2025, o Protheus vai emitir esse alerta, por conta que a 1ª programação ser de Julho e a 2ª programação seria para Abril.  
  
Como essa validação está no fonte, não há um parâmetro ou forma de alterá-la.  
Caberá nesse caso somente, uma adequação no processo de pedido de férias, sempre de forma cronológica, onde a 1ª programação nunca pode ser superior às 2º ou 3ª.  
  
**Saiba Mais**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
