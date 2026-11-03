---
article_id: 4414425980823
category: Comércio Exterior - Easy Export Control - Cadastros
content_hash: 30a0cc4509e6d154861efcba40406eb47380fc24d2b0ff98203614c7f491dbee
fetched_at: '2026-06-28T22:36:57.280473+00:00'
product: protheus
section_id: 1500001549302
source: central-protheus
title: ' Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - AJUDA:CCBLOCKED  Conta
  corrente bloqueada para novas movimentações'
type: support-article
updated_at: '2022-06-09T20:08:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414425980823--Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-AJUDA-CCBLOCKED-Conta-corrente-bloqueada-para-novas-movimenta%C3%A7%C3%B5es
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Ao informar a data de embarque na rotina de embarque de exportação (EECAE100), e salvar aparece a mensagem de validação abaixo:

```
A gravação não ocorreu devido à impossibilidade de integração com o módulo Financeiro. Verifique o Log Viewer para maiores detalhes:  
  
AJUDA:CCBLOCKED   
Conta corrente bloqueada para novas movimentações  
movimentações  
  
Tabela SE1 29/11/2021 15:19:57  
- cMotBx :=NORMAL  
- cBanco :=CX1  
- cAgencia :=00001  
- cConta :=0000000001 < -- Invalido  
- dBaixa :=29/11/2021  
- cHist070 :=Emb.:EMBTREINA001   
- nTxMoeda := 5.43  
- nValRec := 1030.34  
--------------------------------------------------------------------------------  
  
Erro na contratação.
```

Qual o procedimento necessário para que esta validação não seja exibida?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões  
  
**Solução**Esta mensagem de validação esta ocorrendo porque o banco **CX1** esta com o campo **A6\_BLOCKED = 1 e** com a data do campo **A6\_DTBLOQ** preenchida  na rotina de cadastro de bancos (**EECAC110**) que significa que o banco esta bloqueado. Este banco é o Caixa Geral padrão do ERP, é utilizado no momento de baixar a nota fiscal no embarque de exportação (EECAE100) e não pode ser bloqueado. 

![BANCO_BLOQUEADO.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4414425882903/BANCO_BLOQUEADO.PNG)

Para dar continuidade ao processo altere o conteúdo do campo **A6\_BLOCKED=2 .**
