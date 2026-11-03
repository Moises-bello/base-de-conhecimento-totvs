---
article_id: 4404858428183
category: Financeiro - Consultas / Relatórios
content_hash: 715be1afea1b9547421030785f1dd0fa86cd932360906642feecd1dd3b0ed2d4
fetched_at: '2026-06-28T22:37:58.498783+00:00'
product: protheus
section_id: 1500001539561
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINR460 - Erro SIGALOJA.DLL
  Incompatível '
type: support-article
updated_at: '2023-01-25T23:45:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404858428183-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINR460-Erro-SIGALOJA-DLL-Incompat%C3%ADvel
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:04:00 min**

**Dúvida**Ao emitir um Cheque através da Rotina **FINR460 Impressão de Cheques especiais** é apresentado erro na dll SIGALOJA.DLL?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA330 - Todas as versões  
  
**Solução**Verificar se o *SmartClient* do cliente encontra-se na Versão 32Bits, uma vez que a dll SIGALOJA.DLL  somente opera em 32 Bits e se o arquivo SIGALOJA.DLL encontra-se no diretório *System* do Servidor do Protheus.

**Importante**  
Caso o cliente esteja na versão Lobo Guará que é utilizada em 64Bits, o cliente deverá ter o *AppServer* na Versão 64 Bits para aplicação, porém o *SmartClient* deverá ser na Versão 32Bits.

**Saiba mais**[Impressoras Homologadas Financeiro - FINR460](https://tdn.totvs.com/display/public/mp/Impressoras+Homologadas+Financeiro+-+FINR460+--+11391)[MP - SIGALOJA - Impressoras de Cheque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/235231008-MP-SIGALOJA-Impressoras-de-Cheque?source=search)  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINR480 - Erro SIGALOJA.DLL Incompatível](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033045753-MP-SIGAFIN-FINR480-Erro-SIGALOJA-DLL-Incompat%C3%ADvel-?source=search)  
[MP - SIGALOJA - Incompatibilidade de DLL com as releases 17, 23, 25 e 27](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038118953-MP-SIGALOJA-Incompatibilidade-de-DLL-com-as-releases-17-23-25-e-27?source=search)  
[MP - SIGALOJA - Atualização de DLL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058164873-MP-SIGALOJA-Atualiza%C3%A7%C3%A3o-de-DLL?source=search)
