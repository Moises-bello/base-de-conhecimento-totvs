---
article_id: 360014288952
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: e0d002c4541ba0363b3a566d12288a9d353051c8adc0fc646dd091818d49f511
fetched_at: '2026-06-28T22:41:48.296399+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAATF  - ATFA012 O erro no
  método SETPROPERTY: Campo N3_DTBAIXA não encontrado. on FWFORMVIEWSTRUCT:SETPROPERTY'
type: support-article
updated_at: '2023-11-30T15:20:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014288952-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA012-O-erro-no-m%C3%A9todo-SETPROPERTY-Campo-N3-DTBAIXA-n%C3%A3o-encontrado-on-FWFORMVIEWSTRUCT-SETPROPERTY
---

**Ocorrência**No módulo **Ativo Fixo** ao tentar realizar excluir um bem  é apresentada a mensagem:   
O erro no método SETPROPERTY: Campo N3\_DTBAIXA não encontrado. on FWFORMVIEWSTRUCT:SETPROPERTY  
  
**Ambiente**  
Protheus – Ativo Fixo – A partir da versão 12.1.17  
  
**Causa**

Essa mensagem esta sendo apresentada pela ausência do campo N3\_DTBAIXA  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique a existência desse campo N3\_DTBAIXA , na sua SX3 no banco de dados;  
2. Na tabela SN3, veja se o campo esta marcado como "usado";  
3. Este e demais problemas de dicionário ocorrendo em seu ambiente poderão ser corrigidos com execução do UPDDISTR após atualização dos arquivos da systemload disponíveis no portal do cliente.
