---
article_id: 4414484278167
category: Faturamento - Cadastros
content_hash: fe707faf721d1ac943202d59aa371649f0d80afa5c6ac791e3d10d9db5903860
fetched_at: '2026-06-28T22:38:36.659368+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus)- SIGAFAT - Exceção de datas
  de pagamento em condição de pagamentos.
type: support-article
updated_at: '2021-11-30T14:15:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414484278167-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Exce%C3%A7%C3%A3o-de-datas-de-pagamento-em-condi%C3%A7%C3%A3o-de-pagamentos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**

Existe dentre os tipos de condição de pagamento uma opção para excluir alguns dias de vencimento?

Por exemplo, tem como ter uma condição de pagamento com vencimento em 30/60/90 que não caia nos dias 05/15/20 e 25?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.  
  
**Solução**

Por padrão do sistema não há uma condição de pagamento com dias de exceção, somente por regra.  
  
Caso nenhum dos Tipos de Condição disponíveis atenda plenamente a particularidade de sua necessidade, poderá utilizar o TIPO 9, que é o Tipo utilizado quando não há um tipo que automatize a regra do cliente.  
Detalhes abaixo e no link: [Condição\_de\_Pagto\_Tipo\_9](https://tdn.totvs.com/pages/viewpage.action?pageId=238034990)  
  
Ou caso preferir seguem os pontos de entrada da rotina:  
  
M460RTPD - executado antes do rateio das despesas acessórias: [http://tdn.totvs.com/display/public/PROT/M460RTPD](https://tdn.totvs.com/display/public/PROT/M460RTPD)  
M460COND - Alteração de data inicial da Condição de Pgto. Chamado antes de gerar o cabeçalho da NF de saida: [http://tdn.totvs.com/pages/releaseview.action?pageId=6784176](https://tdn.totvs.com/pages/releaseview.action?pageId=6784176)  
M460FIM - Chamado apos a gravação da NF de Saída, e fora da transação: [http://tdn.totvs.com/pages/releaseview.action?pageId=6784180](https://tdn.totvs.com/pages/releaseview.action?pageId=6784180)  
M461VTot - Verifica o total da Nota Fiscal e a condição de pagamento escolhida, antes de sua geração: [http://tdn.totvs.com/pages/releaseview.action?pageId=6784607](https://tdn.totvs.com/pages/releaseview.action?pageId=6784607)  
OBS: O ponto de entrada não é chamado na opção Prep. Doc. Saída da rotina MATA410, é chamado na opção Prep. Doc. Saída da rotina MATA461.  
MT461VCT - Alteração no vencimento e valor do título: [http://tdn.totvs.com/pages/releaseview.action?pageId=6784498](https://tdn.totvs.com/pages/releaseview.action?pageId=6784498)  
M4601DUP - Possibilita a alteração do número da primeira parcela dos títulos. As demais serão uma sequência alfanúmerica destes: [http://tdn.totvs.com/pages/releaseview.action?pageId=6784173](https://tdn.totvs.com/pages/releaseview.action?pageId=6784173)  
M460MOED - Altera definição da moeda do título: [http://tdn.totvs.com/pages/releaseview.action?pageId=6784589](https://tdn.totvs.com/pages/releaseview.action?pageId=6784589)  
GEMXGRCVND - Manutenção na condição de pagamento no pedido de venda - [http://tdn.totvs.com/pages/viewpage.action?pageId=6784609](https://tdn.totvs.com/pages/viewpage.action?pageId=6784609)
