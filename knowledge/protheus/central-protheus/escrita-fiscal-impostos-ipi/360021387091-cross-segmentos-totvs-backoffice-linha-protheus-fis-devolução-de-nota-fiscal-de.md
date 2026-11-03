---
article_id: 360021387091
category: Escrita Fiscal - Impostos - IPI
content_hash: b4f3ceb32133decb6686d8b42093849c45fede015bcdbba4589382431833a602
fetched_at: '2026-06-28T22:39:29.011494+00:00'
product: protheus
section_id: 1500001538641
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Devolução de nota
  fiscal de entrada com IPI '
type: support-article
updated_at: '2023-04-10T12:47:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021387091-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Devolu%C3%A7%C3%A3o-de-nota-fiscal-de-entrada-com-IPI
---

**Duvida:**

Devolução de nota fiscal de entradas com calculo do IPI 

**Ambiente**Protheus - Faturamento - A partir da versão 11.80  
  
**Solução**

Devolução com IPI

A nota fiscal de devolução é espelho da Nota fiscal de origem, sendo assim, o IPI deve ser calculado na nota fiscal de entrada.  
  
**Cadastro de produtos - SB1**  
Aliq IPI= preenchido

**Cadastro de TES - SF4**  
Calcula ipi = sim  
L. fiscal ipi = outros

Dessa forma o sistema grava o cálculo do IPI para posterior devolução.

Para devolução da nota fiscal com cálculo do IPI e destaque do IPI no campo de observações :

calcula ipi = sim  
L. fiscal ipi = outros

Cod trib ipi = 50  
  
Ao consultar a planilha financeira o valor do IPI estará calculado, correto.  
O ipi faz parte do valor da Nota Fiscal e deve ser calculado.

Para o destaque do IPI em observações do Danfe  
  
**Nota de devolução com IPI**

Com a nova validação, o valor do IPI deve ser gerado na tag <vIPI>. No caso de devolução, o parâmetro MV\_IPIDEV deve estar preenchido com a opção T para que a transmissão da nota seja efetuada e o valor do IPI seja destacado no campo Dados Adicionais do DANFE.

Após alteração da TES e do Parâmetro refazer o pedido de vendas / chamando Cliente / Produto e TES para refazer a Tabela CD2

Para impressão do Danfe abrir um chamado junto a equipe de NFe.
