---
article_id: 360021142752
category: Controle de Documentos (SIGAQDO)
content_hash: 3a2b2363a391326f6b61516ddacec0b30f2b1cc6fa881aa8cd74dd45962a1452
fetched_at: '2026-06-28T22:42:28.931038+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Arquivos com extensão diferente de
  .doc
type: support-article
updated_at: '2022-03-18T14:16:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021142752-Manufatura-Linha-Protheus-SIGAQDO-Arquivos-com-extens%C3%A3o-diferente-de-doc
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:45 min  
  
Dúvida**É possível incluir arquivos com extensão diferente de **.doc** no módulo **SIGAQDO - Controle de Documentos**?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Solução**O **SIGAQDO** possui integração apenas com o **Word**.   
Para incluir arquivos de outras extensões, é necessário preencher no **QDOA050 - Cadastro do Documento** o campo **Doc Int/Ext**como **Externo**, no local mostrado na imagem abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018094572/mceclip2.png)

**Importante**:  
O **Documento Interno** utiliza a integração do Protheus com o **MS Office Word** para que ao criar um novo documento seja aberto o **Word** que utilizará o modelo **.dot** cadastrado na rotina **QDOA020 - Tipo de Documento**. Quando o documento for **Interno** somente o **Word** poderá ser utilizado para a criação do documento. Este documento será criptografado pelo Sistema e só poderá ser aberto pelo Protheus.   
  
O **Documento Externo**não é criado a partir de nenhuma integração. Ao criar o documento externo é exibido a caixa de seleção contendo o servidor e máquina local, onde poderá anexar um documento criado anteriormente que pode ser de qualquer extensão: **.xls**, **.pdf**, **.txt**, etc.  Não há criptografia para o tipo **Externo**.   
  
Por este motivo, o modelo **.dot** será usado apenas no **Documento Interno** que utiliza o **Word**. Para **Documentos Externos** poderá utilizar qualquer extensão, desde de que o computador utilizado possua o *software* para visualização da extensão de arquivo utilizada.
