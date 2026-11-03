---
article_id: 4429556858007
category: Faturamento - Cadastros
content_hash: ae1f074152cd4977d6857c73211b88cc0b008c3afc8fd939cd034a6b1e45b9f8
fetched_at: '2026-06-28T22:38:35.466485+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Numeração Automática no Código
  do Cliente (A1_COD)
type: support-article
updated_at: '2024-04-30T21:04:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4429556858007-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Numera%C3%A7%C3%A3o-Autom%C3%A1tica-no-C%C3%B3digo-do-Cliente-A1-COD
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22503538138647) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao copiar o cadastro de cliente/fornecedor não preenche o código de cliente automático.  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Causa**As funções GetSXENum e GetSX8Num não existem por padrão no campo de Código do Cliente (A1\_COD), alguns clientes inserem a validação manualmente, porém algumas particularidades não são tratadas pela função, veja mais detalhes em "Passo 2 - Função no Dicionário" no link:

* [Ajuste de Numeração automática dos Formulários (Tabelas / ALIAS) no Protheus](https://tdn.totvs.com/x/P4YKDg)

**Solução**A orientação da TOTVS, conforme documentação citada acima, é que seja utilizada uma função customizada para tratar o controle de numeração, apenas com a inserção das funções GetSXENum e GetSX8Num, em alguns cenários, podem ocorrer erros no controle de numeração.

Abaixo indicamos um exemplo de função, lembrando que trata-se apenas de um exemplo, caso necessite customizar, solicite o acompanhamento de seu analista programador:

```
#Include 'TOTVS.ch'  
  
User Function NextSA1Cod()  
Local cNum := GETSXENUM("SA1","A1_COD")  
  
DbSelectArea("SA1")  
SA1->(DbSetOrder(1))  
While (DbSeek(xFilial("SA1")+cNum))  
ConfirmSX8()  
  
cNum := GETSXENUM("SA1","A1_COD")  
Enddo  
  
DbCloseArea()  
RollbackSx8()  
Return cNum
```

**Saiba mais:**

* [Ajuste de Numeração automática dos Formulários (Tabelas / ALIAS) no Protheus](https://tdn.totvs.com/x/P4YKDg)
