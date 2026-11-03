---
article_id: 24760133390103
category: PONTO ELETRÔNICO
content_hash: 5a828ec378d7bf6002d290fbdc2476e637c7101906802f8ccd361bd51cf283ec
fetched_at: '2026-06-28T22:44:36.480758+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - Meu RH - Como evitar marcações de ponto duplicadas no
  App Meu RH
type: support-article
updated_at: '2025-03-12T18:52:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24760133390103-RH-Linha-Protheus-Meu-RH-Como-evitar-marca%C3%A7%C3%B5es-de-ponto-duplicadas-no-App-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24760133345047) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como evitar marcações de ponto duplicadas no App Meu RH?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - MEU RH - Todas as versões  
  
**Solução**Quando um funcionário realizar uma marcação de ponto no **App Meu RH por Geolocalização**, será possível determinar os **minutos de diferença**, para que, **uma segunda marcação seja automaticamente desprezada.**  
  
**[Neste caso no parâmetro MV\_DESPMIN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403030035223)**, será necessário indicar quantos minutos serão utilizados para que, **marcações naquele intervalo sejam desprezadas.**  
  
O conteúdo padrão deste parâmetro é 05, ou seja, até 05 minutos de diferença haverá essa referência:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24760146919575)  
  
Após configuração do parâmetro, **se o funcionário já realizou uma marcação de ponto**, com um intervalo menor ou igual a 5 minutos, o App Meu RH trará o seguinte cenário:  
  
- **primeira marcação realizada as 12:18**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24760146920855)  
  
Neste caso, se o funcionário tentar incluir uma segunda marcação 5 minutos após, **no caso sendo as 12:23, o App Meu RH não irá permitir:**  
![Marcação 1223.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/24760133353495)  
  
Porém, permitirá se a marcação **tiver 06 minutos de diferença.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24760133355159)  
  
**Saiba Mais**  
[**CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI para acessar a documentação de referência sobre o MEU RH**](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
