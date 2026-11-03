---
article_id: 360025266252
category: Financeiro - Contas a Receber
content_hash: 1af0300fde4bc91e5e49d74642ea7f803249f1263063195afbec01cb10fb3a49
fetched_at: '2026-06-28T22:38:12.675429+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: MP - SIGAFIN - Numeração dos títulos gerados na liquidação a receber
type: support-article
updated_at: '2021-04-28T15:17:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025266252-MP-SIGAFIN-Numera%C3%A7%C3%A3o-dos-t%C3%ADtulos-gerados-na-liquida%C3%A7%C3%A3o-a-receber
---

**Dúvida**Como é gerada a numeração dos títulos gerados na rotina de liquidação a receber?

**Ambiente**Microsiga Protheus – Financeiro – A partir da versão 12.1.17  
  
   
**Solução**Com a readequação da rotina de Liquidação a receber (FINA460), que ocorreu em Outubro/2018, a nova rotina não possui controle de numeração através de parâmetros, como era feito anteriormente na própria FINA460 através do parâmetro MV\_NUMLIQ e na rotina FINA280 através do parâmetro MV\_NUMFAT.

 A rotina irá sugerir uma numeração através da seguinte métrica definida no fonte da rotina:

- Caso seja definido um prefixo na pergunta (F12) **Prefixo do título a ser gerado**, o sistema procurará pelo maior número (E1\_NUM) que utiliza o prefixo definido, e acrescentará 1.

Exemplo: Em meus parâmetros (F12), defini o prefixo **FAT** e meu registro com a maior numeração deste prefixo foi 500000000, desse modo, será sugerido a numeração 500000001, sempre com o prefixo FAT. Caso seja o primeiro, irá ser retornado o valor 000000001.

![](http://tdn.totvs.com/download/attachments/340363674/image2018-2-23_16-5-36.png?version=1&modificationDate=1519412736000&api=v2)

- Caso o prefixo seja alterado, a contagem irá começar do zero, sugerindo também a numeração 000000001 ou a partir da maior numeração deste prefixo definido.

- Se o parâmetro não foi definido, O prefixo permanecerá em branco e a numeração seguirá a mesma regra, sempre buscando o maior numero gerado e somando 1.
