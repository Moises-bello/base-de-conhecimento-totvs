---
article_id: 4407458674327
category: Contabilidade Gerencial - Procedures, Parâmetros,Campos, Gatilho
content_hash: da189187150ed50050c48c314113c1be2cf3abc9ef18557630a10c4fb7758bf6
fetched_at: '2026-06-28T22:41:01.411893+00:00'
product: protheus
section_id: 1500001537361
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - MV_TPVALOR RELATÓRIO
  DE SALDO E RELATÓRIO DE MOVIMENTO '
type: support-article
updated_at: '2022-05-23T16:56:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407458674327-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-MV-TPVALOR-RELAT%C3%93RIO-DE-SALDO-E-RELAT%C3%93RIO-DE-MOVIMENTO
---

**Dúvida**

Ao configurar o parâmetro MV\_TPVALOR = S (Sinal), os valores são exibidos com sinal de + (Positivo) ou - (Negativo), obedecendo quais  critérios ?  
  
**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 12  
  
**Solução**Ao configurar o parâmetro [MV\_TPVALOR](https://tdn.totvs.com/pages/viewpage.action?pageId=615605914) = S (Sinal), os valores são exibidos com sinal de + (Positivo) ou - (Negativo), obedecendo os seguintes critérios:

Veja :

* <https://tdn.totvs.com/pages/viewpage.action?pageId=146966519>=

* Para relatórios de movimentos é considerado somente o tipo do lançamento, caso seja de crédito o sinal é Positivo (+), caso seja débito é  Negativo ( - ), semelhante a movimentos financeiros.
* Para relatórios de saldos é considerado além do tipo do lançamento, a condição normal da conta a ser exibida.   
  Exemplo: Caso a conta seja do tipo Crédito, e o saldo da conta também é credora, o sinal é positivo, porém caso o saldo da conta estiver devedor, o sinal é negativo.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407452749847/mceclip0.png)

**Exemplo de Relatórios:**

* Rel. Movimentos: Conta x 6 Meses (CTBR260).
* Rel. Movimentos: Razão Contábil (CTBR400).

Para Relatórios que tem vínculo com Centro de Custo a regra acima é ordenada pelo Campo Cond. Normal (CTT\_NORMAL) no cadastro de centro de custo sendo levado em consideração apenas quando o lançamento possui centro de custo atrelado

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407458604183/mceclip1.png)

* \* Para Centro de Custo com o campo Cond. Normal (CTT\_NORMAL) igual a 0 será considerado a condição normal da Conta.

* \*\* A regra acima vale apenas para relatórios onde a comparação é feita entre a entidade Conta Contábil e as demais entidades (Item Contábil, Centro de Custo e Classe de Valor).

Exemplo de Relatório.

CTBR145 (Contas x Centro de Custo)

* \*\*\* Para os demais casos a configuração deverá ser feita utilizando a condição normal da entidade devendo ser configurada como (1-Despesa ou 2-Receita).

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407452786199/mceclip2.png)

[MV\_TPVALOR - Configuração do Parâmetro](https://tdn.totvs.com/pages/releaseview.action?pageId=146966519)

[Razão por Item (CTBR480 - SIGACTB) - Saldo Anterior MV\_TPVALOR](https://tdn.totvs.com/pages/releaseview.action?pageId=630003385)
