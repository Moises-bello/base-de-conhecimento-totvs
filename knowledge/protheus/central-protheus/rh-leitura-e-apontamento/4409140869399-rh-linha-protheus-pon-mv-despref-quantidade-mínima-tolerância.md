---
article_id: 4409140869399
category: RH - Leitura e Apontamento
content_hash: 2ceb8f65206b25adbfb1a135fe6136265007950ba42ac774feb3f798b28315c3
fetched_at: '2026-06-28T22:44:45.988300+00:00'
product: protheus
section_id: 32419281460119
source: central-protheus
title: RH - Linha Protheus - PON - MV_DESPREF Quantidade mínima tolerância
type: support-article
updated_at: '2025-11-11T17:48:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409140869399-RH-Linha-Protheus-PON-MV-DESPREF-Quantidade-m%C3%ADnima-toler%C3%A2ncia
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33885967632407) Tempo aproximado para leitura: 01:30:00 min** **Dúvida**Configuração parâmetro MV\_DESPREF quantidade mínima tolerância.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Este parâmetro **MV\_DESPREF** tem como finalidade configurar a tolerância para quantidade de marcações diária ou minutos entre marcações que será considerado sem desprezar as marcações de refeições.  
  
**Parâmetro MV\_DESPREF**   
**Tipo** : C  
**Descrição**: Informar o Tipo e a Qtde de Min.de Tolerância entre uma Marcação ou Outra ou a Qtde Máxima de Marcações Permitidas p/ um Mesmo Horário:"M"nn ou "N"nn.  
**Conteúdo** : "M"nn ou "N"nn  
  
**M** <=> Indica que nn estão representados em Minutos e;  
**N** <=> Indica que nn representa o Limite de Marcações.  
**nn** <=> Minutos ou Qtd. de marcações.  
  
**Exemplo**: M05 <=> Entre uma Marcação e outra, desprezar tudo o que for superior a 05 Minutos  
N01 <=> Considerar no Máximo 01 Marcação com a Mesma Data e Horário. Ou seja, não gravará as refeições com mesma data e horário.   
  
Cenário 1 com o **MV\_DESPREF=N01**![](https://centraldeatendimento.totvs.com/hc/article_attachments/30121315135767)  
  
Funcionário bate a refeição dia 18/02/2025 as 12:30 e no arquivo sobe duplicado a mesma refeição. Com o conteúdo N01, só vai gravar uma marcação.   
No relógio constam 05 batidas de refeições, onde dia 18/02 as 12:30 está duplicada:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30121292128535)  
  
Na leitura das batidas de refeições constam 05 lidas, porém 04 gravadas:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30121315140503)  
  
Veja que em manutenção por refeições gravou apenas as 04 batidas de refeições:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30121292130839)  
Cenário 1 com o **MV\_DESPREF=M05  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30121315145239)**Batidas do mesmo dia com intervalo menor que cinco minutos: Exemplo dia 16/02/2025 batidas 12:30 e 12:34, não será lida a de 12:34, veja:  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/30121292132247)**Veja que no LOG da leitura de refeições gravou apenas 01 batida: 12:30  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/30121315147415)**Veja como ficou nas manutenções de Refeições:  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/30121292134039)  
  
  
  
Saiba mais:**[Manual do ponto eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[MV\_DESPREF - Quantidade mínima tolerância](https://tdn.totvs.com.br/display/public/PROT/MV_DESPREF+-+Quantidade+minima+tolerancia+--+10246)  
[RH - Linha Protheus - PON - Como efetuar os cadastros das refeições para Leitura no Ponto Eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018129092-RH-Linha-Protheus-PON-Como-efetuar-os-cadastros-das-refei%C3%A7%C3%B5es-para-Leitura-no-Ponto-Eletr%C3%B4nico)
