---
article_id: 22704684549271
category: Financeiro - Consultas / Relatórios
content_hash: 503bd2f5d7063183b859e3d57073176dd9a4378ffbfea3e48f452af28243d6cc
fetched_at: '2026-06-28T22:37:58.430693+00:00'
product: protheus
section_id: 1500001539561
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINR960 - Não há dados
  a serem exibidos
type: support-article
updated_at: '2024-04-11T19:51:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22704684549271-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINR960-N%C3%A3o-h%C3%A1-dados-a-serem-exibidos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22704684512279) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No módulo Financeiro, ao tentar realizar a impressão do relatório **FINR960 - DME - Declaração de Moedas**, apresenta a mensagem de **"Não há dados a serem exibidos"**   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22704684520215)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**

Este incidente ocorre devido à falta de parametrizações para exibição dos dados no relatório.

**Solução**

Podemos validar algumas informações para exibição no relatório

1 - Avalie na rotina **FINA490 - Miscelânea > Arquivos > Tabela de Motivos de Baixa.** O motivo de baixa utilizado está definido para espécie 

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/22704700597783)**

2 - Para inclusão de um Recebimento Antecipado (**RA)** em espécie, é necessário marcar que o mesmo foi recebido dessa forma, conforme o print abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22705342115351)

3 - Verifique se o valor informado na nota ou movimento é acima do definido no parâmetro **MV\_VLRMDME** e contém o valor a ser considerado para **Declaração de Moedas em Espécie.**

**Saiba mais:**[https://tdn.totvs.com/pages/viewpage.action?pageId=542149755](Declara%C3%A7%C3%A3o%20de%20Moedas%20em%20Esp%C3%A9cie%20-%20DME%20-%20FINR960)
