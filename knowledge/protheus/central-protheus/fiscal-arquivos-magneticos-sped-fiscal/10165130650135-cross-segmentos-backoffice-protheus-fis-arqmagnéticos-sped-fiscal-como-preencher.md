---
article_id: 10165130650135
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 6d28ed40ed25fd1829d694e57a7ba0269e5fdf04a81ec5172e7f6abf52cd8c2d
fetched_at: '2026-06-28T22:42:03.596174+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Sped Fiscal
  - Como preencher o campo 07_NR_PARC do 0300 para número de parcelas menor que 48?
type: support-article
updated_at: '2022-11-11T21:11:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10165130650135-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sped-Fiscal-Como-preencher-o-campo-07-NR-PARC-do-0300-para-n%C3%BAmero-de-parcelas-menor-que-48
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como preencher o campo **07\_NR\_PARC** do **0300** do **Sped Fiscal** quando o número de parcelas é menor que 48?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

No padrão, o Protheus valida o conteúdo no parâmetro **MV\_LC102** para gerar o número de parcelas no campo  **07\_NR\_PARC.**  O parâmetro, por padrão, tem conteúdo **48,** o que indica que o contribuinte tem direito de se creditar do **CIAP** em **48** parcelas, conforme legislação que rege o **CIAP.**

No cenário em que o contribuinte, possui o direto de se creditar do CIAP  em quantidade de parcelas inferior à 48 **(campo Num. Parc. - F9\_QTDPARC diferente de 48)**  é preciso preencher o campo **Parc Reduz = (F9\_PARCRED)** **= 1-Sim**  na rotina **MATA905 "Manutenção CIAP"**.

Dessa forma, passa a ser validado primeiramente o conteúdo do campo **Parc Reduz = (F9\_PARCRED)****= 1-Sim** em conjunto com o campo **Num. Parc. (F9\_QTDPARC** ao invés do conteúdo do parâmetro **MV\_LC102**.   
  
Assim,  o campo **07\_NR\_PARC** do registro **0300** e o campo **09\_NUM\_PARC** do registro **G125** são gerados corretamente conforme conteúdo do campo **Num. Parc. (F9\_QTDPARC**
