---
article_id: 21350595768215
category: Financeiro - Compensação Contas a Receber
content_hash: 406349fcb8a905571f8ae4778ec19ff4b0179de4ea7275267d6b20cb1a980eb8
fetched_at: '2026-06-28T22:37:40.441811+00:00'
product: protheus
section_id: 35056224784407
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA330 - Compensação
  de RA x NF com valor Residual
type: support-article
updated_at: '2026-03-04T17:42:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21350595768215-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA330-Compensa%C3%A7%C3%A3o-de-RA-x-NF-com-valor-Residual
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21350595741079) Tempo aproximado para leitura: **00:04 min**  
  
**Dúvida**  
Como posso baixar o saldo restante do Recebimento Antecipado (RA) após a compensação de adiantamento?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**

**Tolerância de valor residual para zerar o saldo após a compensação (MV\_TOLERPG)**

Quando, após a compensação, houver um saldo restante de centavos em um dos títulos, é possível configurar para que o sistema considere uma margem de tolerância e baixe o título em sua integralidade.

Esse valor de margem deve ser configurado através do parâmetro **MV\_TOLERPG** (as baixas de títulos a receber também realizam o mesmo tratamento através desse parâmetro).

**Exemplo** de como a rotina é impactada com o parâmetro:

1. Através da rotina **FINA330**, é selecionado um título de partida do tipo **RA** (adiantamento) em dólar. Seu valor convertido em reais é de **R$ 1.000,05**.

2. Na tela de seleção de títulos a serem compensados, são selecionados alguns títulos em reais totalizando **R$ 1.000,03** (diferença de 2 centavos em relação ao **RA**);

3. Para que todos os títulos envolvidos tenham seus saldos zerados ao final do processo de compensação, o parâmetro **MV\_TOLERPG** deve estar configurado com um valor igual ou maior a 0,02 (dois centavos), caso contrário a diferença remanescente ficará no saldo do título de adiantamento (ficando este em aberto).

**Saiba Mais**

[04. PARÂMETROS - Tolerância de Saldo - MV\_TOLERPG](https://tdn.totvs.com/pages/releaseview.action?pageId=505768648#par%C3%A2metros-par%C3%A2metros)
