---
article_id: 360033045753
category: Financeiro - Contas a Pagar
content_hash: 45f3b8c531ba5354a9dc5157c5e6f744c09015c5c95faf948876166f132ad3f4
fetched_at: '2026-06-28T22:38:09.746944+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINR480 - Erro SIGALOJA.DLL
  Incompatível '
type: support-article
updated_at: '2022-08-17T22:26:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033045753-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINR480-Erro-SIGALOJA-DLL-Incompat%C3%ADvel
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Ao emitir um Cheque através da Rotina **FINR480 Impressão de Cheques** é apresentado erro na dll SIGALOJA.DLL?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA330 - Todas as versões  
  
**Solução**Verificar se o *SmartClient* do cliente encontra-se na Versão 32Bits, uma vez que a dll SIGALOJA.DLL  somente opera em 32 Bits e se o arquivo SIGALOJA.DLL encontra-se no diretório *System* do Servidor do Protheus.

**Importante**  
Caso o cliente esteja na versão Lobo Guará que é utilizada em 64Bits, o cliente deverá ter o *AppServer* na Versão 64 Bits para aplicação, porém o *SmartClient* deverá ser na Versão 32Bits.
