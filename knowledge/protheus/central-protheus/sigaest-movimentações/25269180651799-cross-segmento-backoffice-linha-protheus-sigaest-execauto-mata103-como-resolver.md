---
article_id: 25269180651799
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 92fdb7606bb284b483ff1065e412a5b163599b3f1e29335a9cf3034acfb96a0a
fetched_at: '2026-06-28T22:38:55.523753+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - ExecAuto MATA103 -
  Como resolver o erro A100SBLOT em notas de Devolução de Venda?
type: support-article
updated_at: '2025-03-12T12:27:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25269180651799-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-ExecAuto-MATA103-Como-resolver-o-erro-A100SBLOT-em-notas-de-Devolu%C3%A7%C3%A3o-de-Venda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25269180630039) Tempo aproximado para leitura: **00:02:13 min** **Dúvida**Como rodar o ExecAuto da rotina MATA103 sem enfrentar a mensagem: "*AJUDA: A100SBLOT O produto está configurado para controlar sublote e o sublote não foi informado*"?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**No MsExecAuto() da rotina MATA103, possui especificidades para produtos com controle de Sublote.

Nas operações de Documento de Entrada do tipo **Devolução**, definido no campo F1\_TIPO (linha 47 do exemplo em anexo ao final do artigo), subentende-se que houve um Documento de Saída deste produto onde o Sistema delegou um lote e um Sublote na venda. Neste caso, no Documento de Entrada. **é necessário, no ExecAuto, definir através do campo D1\_NUMLOTE para o mesmo registrar a Nota de Entrada de devolução com o mesmo Sublote que o produto teve na nota de saída. Isso é o que vai fazer o processo concluir sem o erro A100SBLOT.**

Já na inserção do Documento de Entrada de devolução em tela do Protheus, quando o usuário vincula com o Documento de Saída (***Outras Ações -> Retornar*** OU ***Incluir*** -> ***Outras Ações -> Origem***), o Sistema já vai puxar os dados da nota origem, o produto, lote E sublote conforme a venda.

Observação: Documentos de Entrada do tipo Normal, ou seja, não sendo uma nota de devolução, quando o produto controla Sublote não há a necessidade de inserir o D1\_NUMLOTE. Este campo é gerado automaticamente pelo Sistema ao concluir a Nota. Seja via ExecAuto, seja via tela.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
