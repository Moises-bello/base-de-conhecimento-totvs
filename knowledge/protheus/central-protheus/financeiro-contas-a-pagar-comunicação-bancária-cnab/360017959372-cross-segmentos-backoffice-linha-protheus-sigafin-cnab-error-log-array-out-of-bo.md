---
article_id: 360017959372
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 3ab76aef7c48f982f195d6064bc961a2fa152937a83f88dd28185bf75a840300
fetched_at: '2026-06-28T22:37:55.379400+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CNAB: Error log array
  out of bounds pode estar relacionado a Configuração Formato Datas nos Parâmetros
  Bancos'
type: support-article
updated_at: '2024-06-21T13:27:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017959372-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CNAB-Error-log-array-out-of-bounds-pode-estar-relacionado-a-Configura%C3%A7%C3%A3o-Formato-Datas-nos-Par%C3%A2metros-Bancos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**No módulo **Financeiro**, ao executar o **CNAB** pode ser exibido o mensagem   
***Error log (array out of bounds).*** **Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Este erro está relacionado a configuração de forma divergente do esperado pelo sistema. É possível que o erro ocorra devido a configuração do Parâmetros de datas encontrado no campo **EE\_TIPODAT** nos **Parâmetros de Bancos.**  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse Modulo **Financeiro**;  
2. Selecione **Cadastros**> **Parâmetros de Bancos (FINA130)**;  
3. Edite o campo **EE\_TIPODAT** para as possíveis condições.

![EE_TIPODAT.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013386792/EE_TIPODAT.png)  
  
Os formatos são:  
  
1 - ddmmaa  
2 - mmddaa  
3 - aammdd  
4 - ddmmaaaa  
5 - aaaammdd  
6 - mmddaaaa  
  
**Importante:**Verifique no layout do Banco e em seu arquivo de configuração a quantidade de posições, para para adequação do campo data **(SEE->EE\_TIPODAT)** com o número do formato descrito acima.
