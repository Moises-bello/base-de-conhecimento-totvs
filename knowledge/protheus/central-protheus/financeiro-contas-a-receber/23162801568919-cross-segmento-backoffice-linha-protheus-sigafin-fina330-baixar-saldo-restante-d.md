---
article_id: 23162801568919
category: Financeiro - Contas a Receber
content_hash: 131e499b87f4a98e169c2c3eb38a6b5d052c2e14825c72ac05076089936b8517
fetched_at: '2026-06-28T22:38:12.828523+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA330 -  Baixar saldo
  restante de título após compensação contas a receber de forma automática
type: support-article
updated_at: '2024-04-30T19:57:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23162801568919-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA330-Baixar-saldo-restante-de-t%C3%ADtulo-ap%C3%B3s-compensa%C3%A7%C3%A3o-contas-a-receber-de-forma-autom%C3%A1tica
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23162793914007) Tempo aproximado para leitura: **0****0:02:00 min****Dúvida**Baixar saldo restante de título após compensação contas a receber de forma automática  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - Todas as versões  
  
**Solução**1. Quando após a **compensação contas a receber** houver um saldo restante de centavos em um dos títulos, é possível configurar para que o sistema considere uma margem de tolerância e baixe o título em sua integralidade.  
Esse valor de margem deve ser configurado através do parâmetro **MV\_TOLERPG** (as baixas de títulos a receber também realizam o mesmo tratamento através desse parâmetro).

2. Através da rotina **FINA330**, é selecionado um título de partida do tipo **RA (adiantamento)** em dólar. Seu valor convertido em reais é de R$ 1000,05;

3. Na tela de seleção de títulos a serem compensados, são selecionados alguns títulos em reais totalizando R$ 1000,03 (diferença de 2 centavos em relação ao **RA**);

4. Para que todos os títulos envolvidos tenham seus saldos zerados ao final do processo de compensação, o parâmetro **[MV\_TOLERPG](https://tdn.totvs.com/pages/releaseview.action?pageId=225949954)** deve estar configurado com um valor igual ou maior a 0,02 (dois centavos), caso contrário a diferença remanescente ficará no saldo do título de adiantamento (ficando este em aberto).

Saiba Mais  
[DT MV TOLERPG TOLERANCIA BAIXA CR](https://tdn.totvs.com/pages/releaseview.action?pageId=225949954)
