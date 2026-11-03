---
article_id: 13605406296215
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 0d47155183db8761e2e25a5b74c76274c955699d3de34d87a7fe1b5bb528ae57
fetched_at: '2026-06-28T22:38:45.412843+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Devoluções
  de compras ao faturar geram título único do tipo "NDF"
type: support-article
updated_at: '2023-05-24T17:42:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13605406296215-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Devolu%C3%A7%C3%B5es-de-compras-ao-faturar-geram-t%C3%ADtulo-%C3%BAnico-do-tipo-NDF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**O título de devolução de compra, está gerando no contas a pagar, do tipo "NDF"  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**

Quando em uma compra/venda onde é negociado o pagamento em 4 vezes e por algum motivo qualquer ocorre a desistência da compra dentro do prazo de devolução.

Nesse caso é emitido uma nota de devolução do produto, para desfazer essa compra/venda.

O sistema não parcela o título de devolução (apesar da condição de pagamento selecionada) e gera apenas um título, com a data em que a compra está sendo desfeita, com o mesmo intuito, que é desfazer o pagamento/recebimento (não ocorrerá mais visto que o produto fora devolvido).

Em devoluções, no "Contas A Pagar (FINA750)". Um título do tipo "NDF" e outro "NF".  
   
O sistema trata internamente e abate o valor NDF do NF respectivo, é assim que é ajustado. Não é criado contas a receber nem um contas a pagar negativo. O sistema entende que cada NDF tem seu par que foi gerado no documento de entrada.  
   
O sistema subtrai a NDF na NF entrada ou seja, se você:

> Título NF 10 (entrada) tem seu título "NDF" 10 (devolução)
>
> O sistema realiza 10-10 = 0 (zerando a entrada, ficando correto, não baixando duas vezes)

Caso queira algum comportamento diferente, avalie pontos de entrada no momento do faturamento (Rotinas MATA460A/MATA461): [Pontos de Entrada - Faturamento - Protheus 12](https://tdn.totvs.com/x/owQhH)

**Saiba mais**

[FAT0089 - Condições de Pagamento (MATA360)](https://tdn.totvs.com/x/PdpSDg)
