---
article_id: 31688172050839
category: Financeiro - Aplicação / Emprestimos
content_hash: 11fd73dbfafa38cc217f74b1f337ec68c3188931b6479fdfe9e03ea69fcded0b
fetched_at: '2026-06-28T22:37:59.388203+00:00'
product: protheus
section_id: 1500001550542
source: central-protheus
title: Cross Segmentos - TOTVS BackOffice (Linha Protheus) - FINA716 - ERRO 500 -
  Não foi possível efetuar o pagamento variable does not exist NA181VLIOF
type: support-article
updated_at: '2025-04-28T11:39:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31688172050839-Cross-Segmentos-TOTVS-BackOffice-Linha-Protheus-FINA716-ERRO-500-N%C3%A3o-foi-poss%C3%ADvel-efetuar-o-pagamento-variable-does-not-exist-NA181VLIOF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31688156979223) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No módulo Financeiro, ao tentar realizar a amortização de empréstimos, ocorre o erro 500 - Não foi possível efetuar o pagamento variable does not exist NA181VLIOF  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31688156979607)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Esse incidente ocorre, pois a parametrização do sistema está incorreta para algum dos LP´s abaixo, passando a variável **NA181VLIOF** nas informações de valores 

**580 - Inclusão de Aplicação / Empréstimo Financeira**  
**581 - Exclusão de Aplicação / Empréstimo**  
**582 - Apropriação de Aplicação / Resgate de Empréstimo**  
**584 - Estorno da Apropriação de Aplicação**  
**585 - Resgate de Aplicação Financeira**  
**586 - Estorno Empréstimo / Estorno de Resgate**

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse os LP´s e procure se a variável **NA181VLIOF** está sendo informada.   
2. Substitua a variável por um campo fixo e efetue posteriormente a amortização  
3. Valores disponíveis para contabilização de Resgate de Aplicação e Empréstimo:

E5\_VALOR (Valor do Resgate)  
EH\_VALREG (Baixa do Valor do Resgate Curto/Longo Prazo)  
EH\_VALIRF (Pagamento do Valor do IRF)  
EH\_VALIOF (Apropriação do IOF)  
EH\_VALSWAP (Valor do SWAP)  
EH\_VALISWP (Apropriação do IRF s/ SWAP)  
EH\_VALOUTR (Pagamento das Despesas)  
EH\_VALGAP (Pagamento do GAP)  
EH\_VALCRED (Valor do Crédito)  
EH\_VALJUR (Apropriação dos Juros)  
EH\_VALVCLP (Valor da Variação Cambial a Longo Prazo)  
EH\_VALVCCP (Valor da Variação Cambial a Curto Prazo)  
EH\_VALVCJR (Valor da Variação Cambial dos Juros)  
  
**Saiba mais**  
[Aplicações e empréstimos - FINA716 - Financeiro P12](https://tdn.totvs.com/pages/releaseview.action?pageId=680254799)  
[Cross Segmento - Backoffice linha Protheus - SIGAFIN - FINA716 Como é contabilizado pelo LP 582 e 585 na apropriação e no resgate dos rendimentos mês a mês de uma aplicação por cotas FAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14683550030487-Cross-Segmento-Backoffice-linha-Protheus-SIGAFIN-FINA716-Como-%C3%A9-contabilizado-pelo-LP-582-e-585-na-apropria%C3%A7%C3%A3o-e-no-resgate-dos-rendimentos-m%C3%AAs-a-m%C3%AAs-de-uma-aplica%C3%A7%C3%A3o-por-cotas-FAF)  
[FIN0038\_LPAD\_Contablizacao\_LP585\_Resgate\_Aplicação\_Emprestimo](https://tdn.totvs.com/pages/releaseview.action?pageId=334338694)
