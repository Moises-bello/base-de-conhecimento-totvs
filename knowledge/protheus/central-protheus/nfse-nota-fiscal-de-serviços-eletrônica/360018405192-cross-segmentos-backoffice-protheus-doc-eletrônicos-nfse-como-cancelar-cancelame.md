---
article_id: 360018405192
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 9605116ff55d591b2b80dee2a859a8bb27ab48d0202f35dadbc857342f9134a1
fetched_at: '2026-06-28T22:39:56.165360+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Como cancelar
  (cancelamento) NFTS
type: support-article
updated_at: '2025-07-18T14:43:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018405192-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Como-cancelar-cancelamento-NFTS
---

**Dúvida**Qual procedimento para realizar um Cancelar NFTS?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Para isso realize os seguintes passos abaixo:

1. Faça a exclusão do documento de entrada;  
  
2. Acesse a rotina de transmissão (**FISA022**).  
Obs.: Note que a nota excluída anteriormente não será apresentada na tela;  
  
3. **Clique em Cancelamento** e após isso o sistema apresentará os seguintes parâmetros abaixo para serem preenchidos:  
• DT Inicial Canc: Informe a data inicial para busca das notas canceladas no sistema.  
• DT Final Canc: Informe a data final para busca das notas canceladas no sistema.  
  
4. É apresentado um browser com os documentos autorizados que foram excluídos no período solicitado;  
  
5. Selecione os documentos a serem transmitidos e clique em '**Trans. Canc'**;  
  
6. Quando o processamento é realizado de forma correta, o sistema exibe uma tela contendo a mensagem de que a transmissão do Cancelamento foi concluída com sucesso;  
  
7. Após a transmissão, o monitoramento dessa transação pode ser feito por meio da ação Monitor para a certificação de que o Cancelamento foi autorizado pela Prefeitura.  
  
**Importante:** O cancelamento será transmitido apenas para notas com formulário próprio=SIM:  
[Detalhes sobre Formulário Próprio](https://tdn.totvs.com/pages/releaseview.action?pageId=521640651)
