---
article_id: 360000120768
category: RH - Dissídio
content_hash: f6999631d0ad137fcbc24f48908176664e162c582d3433ea2cb2f0b801e4925f
fetched_at: '2026-06-28T22:43:44.250825+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Informe o código de pagamento em todas as verbas
  com incidência para o dissídio
type: support-article
updated_at: '2025-08-20T14:32:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000120768-RH-Linha-Protheus-GPE-Informe-o-c%C3%B3digo-de-pagamento-em-todas-as-verbas-com-incid%C3%AAncia-para-o-diss%C3%ADdio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34317245202839) Tempo aproximado para leitura: 00:00:30 min**

**Ocorrência**Informe o código de pagamento em todas as verbas com incidência para o dissídio  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Causa**Informe o código de pagamento em todas as verbas com incidência para o dissídio  
  
**Solução**Ao tentar efetuar o cálculo do dissídio retroativo **GPEM690** o sistema emite a seguinte mensagem:  
"Informe o código de pagamento em todas as verbas com incidência para o dissidio"  
  
Esta mensagem é apresentada pois no cadastro de verbas existe alguma verba com **sim**no campo **Dissid Ret** e sem **Verba P Diss** informada.  
![](https://totvssuporte.zendesk.com/attachments/token/EvJkkKPFh6iQ9DopBpnFyazL6/?name=inline-1131387524.png)​  
  
Para descobrir de uma maneira mais fácil qual a verba que apresenta este problema, efetue o seguinte procedimento:  
-Via Consulta Genérica, acesse a tabela SRV e efetue um filtro no campo **RV\_COMPL\_** = S e **RV\_CODCOM\_**= (Branco);  
-Ao identificar o código da verba, faça a alteração pelo cadastro de verbas e salve.

Saiba Mais:  
[Página Centralizadora do Dissídio (GPEM690)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)
