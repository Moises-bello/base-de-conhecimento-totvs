---
article_id: 4416801082007
category: Materiais - Compras (SIGACOM)
content_hash: edc7dc862bb79eef150b5586a28bcdce407d64427215ca25598c7ea923b13355
fetched_at: '2026-06-28T22:41:15.831150+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como emitir a Nota
  de Devolução de Venda quando a Filial da Nota Origem mudou ?
type: support-article
updated_at: '2021-12-23T14:53:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416801082007-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-emitir-a-Nota-de-Devolu%C3%A7%C3%A3o-de-Venda-quando-a-Filial-da-Nota-Origem-mudou
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:00min** **Dúvida**Como emitir a Nota de Devolução de Venda quando a Filial da Nota Origem mudou e não existe mais ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões  
  
**Solução**

* A Filial foi fechada? Há a necessidade de ser registrada a Nota de Entrada de Devolução em outra filial.

Desabilite o parâmetro MV\_VLDNFO = .F. que deixará de validar a nota de origem de sua Nota.

Neste caso será necessário emitir a nota de Devolução pela Rotina de Documento de Entrada (MATA103) preenchendo manualmente os campos D1\_NFORI , D1\_SERIORI e D1\_ITEMORI com número da Nota, Série e Item da Nota de Origem.

**Observação:** De acordo com a norma técnica 2020.007, os campos de origem no item do documento de entrada, ficarão desabilitados para serem informados manualmente, pois, a origem deve ser buscada pelo padrão com a localização da saída.

Porém para os casos onde o sistema não localize a origem ou mesmo a nota de saída não esteja no sistema, temos o parâmetro MV\_VLDNFO = .F. no qual se desabilitado e com o MATA103 com data superior a 28/10/2021,os campos ficarão habilitados para serem informados manualmente.

Se não habilitar os campos de origem, será necessário aplicar a correção abaixo para validação em ambiente de teste.

* Pacote de correção Issue *DMANMAT02-35223* - 12.1.27:<https://r.totvs.io/p/1049056> ; 12.1.33:<https://r.totvs.io/p/1049057> ;
* Expedição Continua Compras - <https://tdn.totvs.com/pages/viewpage.action?pageId=522011099>

**IMPORTANTE:** Os procedimentos aqui indicados são exclusivamente para viabilizar a inclusão os registros no sistema. Para esclarecimentos fiscais/contábeis, recomendamos que entre em contato com a Assessoria Fiscal/Contábil de sua empresa.

***Saiba Mais :***

[MP - SIGACOM - Como desabilitar mensagem de validação de Nota Fiscal Origem no Documento de Entrada ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020261731-MP-SIGACOM-Como-desabilitar-mensagem-de-valida%C3%A7%C3%A3o-de-Nota-Fiscal-Origem-no-Documento-de-Entrada-?source=search)

[PÁGINA CENTRALIZADORA DO](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)[COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
