---
article_id: 17033612485015
category: Encargos
content_hash: 0a928973af99075bb26b08e1315d40d1ada426aa5e31980c00ae163e93ab3bca
fetched_at: '2026-06-28T22:46:52.289356+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: 'RH - RM - FOP - Lançamento Contábil: coluna complemento em branco'
type: support-article
updated_at: '2025-01-07T18:31:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17033612485015-RH-RM-FOP-Lan%C3%A7amento-Cont%C3%A1bil-coluna-complemento-em-branco
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17033640957975) Tempo aproximado para leitura: **00:02:10 min****Ocorrência**No módulo Folha de Pagamento, ao realizar a geração dos lançamentos contábeis, a coluna **Complemento** fica em branco.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17033325405207)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Esse incidente ocorre devido o campo **Complemento do Histórico** não estar preenchido no cadastro dos encargos e eventos contabilizados.  
  
**Solução**Para solucionar essa ocorrência, deverá verificar se a contabilização que está sendo realizada é de encargo ou evento.  
  
Caso seja um lançamento contábil de encargo, acesse o cadastro do encargo, aba **dados contábeis** e preencha o campo **Complemento do Histórico**. Possivelmente ao gerar a contabilização este campo estava vazio. Desse campo que é visualizado no lote. Ele serve somente para uma identificação do lote para o histórico, por exemplo. Segue abaixo a demonstração.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17033372123287)

Caso seja um lançamento contábil de evento, deve-se acessar o cadastro do evento, aba **dados contábeis** e preencher o campo **Complemento do Histórico**.  
  
No cadastro de eventos a serem contabilizados, devem ser informados os dados contábeis necessários.  
  
Os campos de conta para débito e conta para crédito devem ser preenchidos com os grupos já existentes na base de dados, tabela dinâmica GRPCONT. Se for utilizar integração contábil é preciso marcar a opção de integração contábil ou por funcionário.  
  
Definir qual histórico será utilizado no lançamento em questão. Os itens desta tabela são cadastrados em **Encargos  | Cadastros | Histórico Padrão** – tabela CHISTP.  
  
O complemento do histórico é um campo texto com até 60 caracteres que pode ser informado para complementar o campo anterior.

**Saiba mais  
[RH - RM - FOP - Contabilização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019748711-RH-RM-FOP-Contabiliza%C3%A7%C3%A3o)**
