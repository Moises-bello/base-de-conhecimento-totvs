---
article_id: 35870107730839
category: Financeiro - Compensação Contas a Receber
content_hash: 445e00e1afcf3dfffa6fa48778e018934ef902dbfbb8889ba0f5429c05ab043a
fetched_at: '2026-06-28T22:37:40.465772+00:00'
product: protheus
section_id: 35056224784407
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - Contas a
  Pagar - FINA340 - Chave de busca no estorno da compensação
type: support-article
updated_at: '2025-10-24T20:46:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35870107730839-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Financeiro-Contas-a-Pagar-FINA340-Chave-de-busca-no-estorno-da-compensa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35870107717655) Tempo aproximado para leitura: 00**:05:00 min**  
  
**Dúvida**  
Como funciona a chave de busca de títulos compensados no processo de estorno/exclusão da compensação a pagar.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**  
O sistema realiza a busca pela **chave única do título** definida em **SX2->X2\_UNICO = X2\_CHAVE = SE2 (E2\_FILIAL + E2\_PREFIXO + E2\_NUM + E2\_PARCELA + E2\_TIPO + E2\_FORNECE + E2\_LOJA)**.  
   
Conforme descrito, o índice único também considera o campo **Filial**. Contudo, em ambientes **compartilhados**, esse filtro não é aplicado, pois o sistema grava apenas o **código da empresa**.

Então, em cenários que possuí o mesmo número de **Prefixo + Número + Parcela + Tipo para o mesmo fornecedor e loja será apresentado os títulos para compensação, mesmo que não tenham sidos compensados com a nota posicionada.**

---

**NOTITSEL no Estorno de Compensação**  
Ao apresentar o assistente **NOTITSEL** durante o estorno de compensação, valide o campo **E5\_FILORIG** nos registros da compensação.  
Além disso, verifique se os campos que compõem a chave (**Prefixo + Número + Parcela + Tipo + Fornecedor + Loja**) das tabelas **SE2** e **SE5** possuem **tamanhos correspondentes** entre si, garantindo a consistência dos dados.  
   
Saiba mais:   
[Compensação contas a pagar - FINA340 - Financeiro P12](https://tdn.totvs.com/pages/viewpage.action?pageId=504794483)
