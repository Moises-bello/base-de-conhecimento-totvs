---
article_id: 360041778474
category: Materiais - Compras (SIGACOM)
content_hash: a4fa420331c7e47b630fc2762cce2e46a600a3bf5d2530826316d34846565ca4
fetched_at: '2026-06-28T22:41:13.120973+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Alerta: Verifique
  os parâmetros definidos para este relatório - Impressão Pedido de Compras e Autorização
  de Entrega MATR110'
type: support-article
updated_at: '2022-02-01T13:26:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041778474-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Alerta-Verifique-os-par%C3%A2metros-definidos-para-este-relat%C3%B3rio-Impress%C3%A3o-Pedido-de-Compras-e-Autoriza%C3%A7%C3%A3o-de-Entrega-MATR110
---

**Ocorrência**

Alerta: Verifique os parâmetros definidos para este relatório - Impressão PC/AE

**Ambiente**

Protheus – Compras– A partir da versão 11.80  
  
**Causa**

Esse incidente ocorre, pois o relatório emitido pelo Browser do PC ou AE está lendo os perguntes definidos na rotina MATR110, assim os dados não são gerados corretamente.  
  
**Solução**

No módulo Compras, ao tentar imprimir o relatório via Browser através da rotina Pedido de compra (MATA121) ou Autorização de Entrega (MATA122) ocorre a mensagem: "Verifique os parâmetros definidos para este relatório no configurador para o usuário corrente."

Para solucionar essa ocorrência, foi implementado o ajuste para que o relatório emitido via PC ou AE possa imprimir o registro posicionado no Browser, ou seja, selecionar o registro que deseja imprimir, ir em **outras ações**, **Imprimir.**

Crie o parâmetro **MV\_PCHABPG** , esse parâmetro será responsável em executar a implementação informada acima:  
  
![](https://totvssuporte.zendesk.com/attachments/token/R5imFRoSuRExhvRWQhafFsoNB/?name=inline-759407647.png)

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
