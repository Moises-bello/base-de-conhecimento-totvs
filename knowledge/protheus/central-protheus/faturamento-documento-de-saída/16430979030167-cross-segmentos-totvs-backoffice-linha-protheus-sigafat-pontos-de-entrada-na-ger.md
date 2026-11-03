---
article_id: 16430979030167
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 4be5eafb20e5d03074e0d18906ccfeb9fc67bd85070df1403dd9693f02ae880a
fetched_at: '2026-06-28T22:38:45.446982+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Pontos de Entrada
  na geração dos títulos pelo Faturamento
type: support-article
updated_at: '2023-07-31T20:51:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16430979030167-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Pontos-de-Entrada-na-gera%C3%A7%C3%A3o-dos-t%C3%ADtulos-pelo-Faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16430994582423) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Quais pontos de entrada posso utilizar para customizar a geração dos títulos pelo Documento de Saída?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**Segue relação de pontos de entrada que permitem alterar o comportamento do sistema na geração dos Títulos à Receber pelo processo de Faturamento (Emissão do Documento de Saída):

* [M460RTPD - executado antes do rateio das despesas acessórias](http://tdn.totvs.com/display/public/PROT/M460RTPD)
* [M460COND - Alteração de data inicial da Condição de Pgto. Chamado antes de gerar o cabeçalho da NF de saída](http://tdn.totvs.com/pages/releaseview.action?pageId=6784176)
* [M460FIM - Chamado após a gravação da NF de Saída, e fora da transação](http://tdn.totvs.com/pages/releaseview.action?pageId=6784180)
* [M461VTot - Verifica o total da Nota Fiscal e a condição de pagamento escolhida, antes de sua geração](http://tdn.totvs.com/pages/releaseview.action?pageId=6784607) (Esse ponto de entrada não é chamado na opção Prep. Doc. Saída da rotina MATA410, é chamado na opção Prep. Doc. Saída da rotina MATA460A).
* [MT461VCT - Alteração no vencimento e valor do título](http://tdn.totvs.com/pages/releaseview.action?pageId=6784498)
* [M4601DUP - Possibilita a alteração do número da primeira parcela dos títulos. As demais serão uma sequência alfanumérica destes](http://tdn.totvs.com/pages/releaseview.action?pageId=6784173)
* [M460MOED - Altera definição da moeda do título](http://tdn.totvs.com/pages/releaseview.action?pageId=6784589)
* [GEMXGRCVND - Manutenção na condição de pagamento no pedido de venda](http://tdn.totvs.com/pages/viewpage.action?pageId=6784609)

Para mais detalhes sobre condições de pagamento, verifique nossa documentação sobre o tema: [Condições de Pagamento (MATA360)](https://tdn.totvs.com/x/PdpSDg)
