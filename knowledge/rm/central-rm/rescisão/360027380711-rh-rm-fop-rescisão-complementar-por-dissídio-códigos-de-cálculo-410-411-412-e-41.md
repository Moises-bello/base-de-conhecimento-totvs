---
article_id: 360027380711
category: Rescisão
content_hash: 67a184023f4b2b7b3b3cf4e3d0a9fb1afb841be52b36ccc76675ded5389ddb14
fetched_at: '2026-06-28T22:46:55.326717+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - Rescisão Complementar por Dissídio: códigos de cálculo 410,
  411, 412 e 413'
type: support-article
updated_at: '2025-01-22T19:23:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027380711-RH-RM-FOP-Rescis%C3%A3o-Complementar-por-Diss%C3%ADdio-c%C3%B3digos-de-c%C3%A1lculo-410-411-412-e-413
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29426925600535) Tempo aproximado para leitura: **00:02:30 min  
  
Ocorrência**Ao realizar o processo de calcular Rescisão Complementar por Dissídio, no final do processo é emitida a  mensagem de erro: **ATENÇÃO! Para a Rescisão Complementar por dissídio, passou a ser necessário criar 4 novos eventos com os seguintes códigos de cálculo:**  
  
[Código de Cálculo 410 - Base de FGTS de Diferença Salarial na Rescisão](https://tdn.totvs.com/pages/releaseview.action?pageId=485444881#:~:text=C%C3%B3digo%20de%20C%C3%A1lculo%20410%20%2D%20Base%20de%20FGTS%20de%20Diferen%C3%A7a%20Salarial%20na%20Rescis%C3%A3o,-Skip%20to%20end&text=Base%20de%20c%C3%A1lculo%20do%20tipo,rescis%C3%A3o%20complementar%20referente%20diss%C3%ADdio%20coletivo.)  
[Código de Cálculo 411 - Estorno Base INSS Dissídio Retroativo Folha na Rescisão](https://tdn.totvs.com/pages/releaseview.action?pageId=485444950#:~:text=C%C3%B3digo%20de%20C%C3%A1lculo%20411%20%2D%20Estorno%20Base%20INSS%20Diss%C3%ADdio%20Retroativo%20Folha%20na%20Rescis%C3%A3o,-Skip%20to%20end&text=Base%20de%20c%C3%A1lculo%20do%20tipo,tenham%20incid%C3%AAncia%20em%20INSS%20folha.)  
[Código de Cálculo 412 - Base de FGTS de Diferença Salarial de 13º Salário na rescisão](https://tdn.totvs.com/pages/releaseview.action?pageId=485444973)  
[Código de Cálculo 413 - Estorno Base INSS Dissídio Retroativo 13º Salário rescisão](https://tdn.totvs.com/pages/releaseview.action?pageId=485444980)  
  
**Os novos eventos deverão ter a mesma parametrização dos eventos com códigos de cálculo 69, 114, 109 e 115.**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**No processo do cálculo da Diferença Salarial por Dissídio o Totvs Folha de Pagamento calcula os eventos de códigos de cálculos 114 e 69. Quando o usuário processa o cálculo de uma Rescisão complementar por dissídio estando no mesmo período da Diferença salarial por dissídio, o sistema estava substituindo os valores destes eventos.  
  
**Solução**Para sanar a situação e evitar possíveis conflitos, foram criados os códigos de cálculo mencionados. Assim, para solucionar a ocorrência, realize os seguintes passos:  
  
1. Acesse: **Administração de Pessoal | Eventos | Eventos.**  
2. Cadastre os novos eventos com os códigos de cálculo abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29426955542167)  
  
[Código de Cálculo 410 - Base de FGTS de Diferença Salarial na Rescisão](https://tdn.totvs.com/pages/releaseview.action?pageId=485444881#:~:text=C%C3%B3digo%20de%20C%C3%A1lculo%20410%20%2D%20Base%20de%20FGTS%20de%20Diferen%C3%A7a%20Salarial%20na%20Rescis%C3%A3o,-Skip%20to%20end&text=Base%20de%20c%C3%A1lculo%20do%20tipo,rescis%C3%A3o%20complementar%20referente%20diss%C3%ADdio%20coletivo.)  
[Código de Cálculo 411 - Estorno Base INSS Dissídio Retroativo Folha na Rescisão](https://tdn.totvs.com/pages/releaseview.action?pageId=485444950#:~:text=C%C3%B3digo%20de%20C%C3%A1lculo%20411%20%2D%20Estorno%20Base%20INSS%20Diss%C3%ADdio%20Retroativo%20Folha%20na%20Rescis%C3%A3o,-Skip%20to%20end&text=Base%20de%20c%C3%A1lculo%20do%20tipo,tenham%20incid%C3%AAncia%20em%20INSS%20folha.)  
[Código de Cálculo 412 - Base de FGTS de Diferença Salarial de 13º Salário na rescisão](https://tdn.totvs.com/pages/releaseview.action?pageId=485444973)  
[Código de Cálculo 413 - Estorno Base INSS Dissídio Retroativo 13º Salário rescisão](https://tdn.totvs.com/pages/releaseview.action?pageId=485444980)  
  
3. Após a criação dos eventos, execute novamente o processo realizado e veja se a mensagem será solucionada.  
  
**Importante**Código de cálculo **410** deve ter a mesma parametrização do código de cálculo **69.**Código de cálculo **411** deve ter a mesma parametrização do código de cálculo **114.**Código de cálculo **412** deve ter a mesma parametrização do código de cálculo **109.**Código de cálculo **413** deve ter a mesma parametrização do código de cálculo **115.**  
**Saiba Mais**  
[Rescisão complementar por Dissídio](http://tdn.totvs.com.br/pages/releaseview.action?pageId=485450778)  
[RH - RM - FOP - Códigos de Cálculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412890806807-RH-RM-FOP-C%C3%B3digos-de-C%C3%A1lculo)
