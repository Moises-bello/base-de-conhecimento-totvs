---
content_hash: 332679c9d809cd77b5608a0fceb1cda5ee0d4c3d3267d90ca64faf4d7c9872df
fetched_at: '2026-06-29T00:10:58.214019+00:00'
page_id: '604520722'
product: rm
source: tdn-rm
title: Totvs Folha de Pagamento x TOTVS Moda - Cadastro de Função
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=604520722
version: 6
---

**Integração Folha de Pagamento RM  x TOTVS Moda - Cadastro de Função**

A Integração Folha de Pagamento RM x TOTVS Moda no cadastro de função tem o objetivo de enviar os dados de funções visando integrar estas informações para utilização dos dados com o backoffice TOTVS Moda.

Para enviá-las, deve-se parametrizar primeiramente as seguintes informações:

**Mensagem: ROLE**

**Versão: 1.000**

Envio da função do funcionário para o TOTVS Moda.

**Exemplo de Json de Envio da mensagem:**

Dessa forma, a integração atenderá os seguintes objetivos:

1) Incluir função: o cadastro de função é gerado no TOTVS Folha de Pagamento RM e enviado para o sistema TOTVS Moda.  
2) Alteração de função: a alteração de função é gerada no TOTVS Folha de Pagamento RM e enviada para o sistema TOTVS Moda.  
3) Exclusão de função: a exclusão de função é gerada no TOTVS Folha de Pagamento RM e enviada para o sistema TOTVS Moda.  
4) Cópia de função entre coligadas: a cópia de função é gerada no TOTVS Folha de Pagamento RM e enviada para o sistema TOTVS Moda.   
5) Para verificar se a integração dos dados foi enviada corretamente para o TOTVS Moda, após acionar os gatilhos citados acima acesse o módulo RM | RH | Integração | EA 2.0 | Mensagens | Gerenciamento de Mensagens, pesquise pelo registro com identificador "ROLE", clique na pasta 'Dados da execução' , onde poderá verificar os dados de execução da mensagem.
