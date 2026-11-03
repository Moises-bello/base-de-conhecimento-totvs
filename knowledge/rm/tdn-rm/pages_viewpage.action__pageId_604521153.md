---
content_hash: ec5ffd5a914d709a4bf39f5355efabd361c13247c7ce1bb7f00b5d58f3b1b9f4
fetched_at: '2026-06-29T00:10:58.222302+00:00'
page_id: '604521153'
product: rm
source: tdn-rm
title: Totvs Folha de Pagamento x TOTVS Moda - Cadastro de Seção
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=604521153
version: 5
---

**Integração Totvs Folha de Pagamento RM x TOTVS Moda - Cadastro de Seção**

A Integração Totvs Folha de Pagamento RM x TOTVS Moda de Cadastro de Seção tem o objetivo de enviar os dados de seções visando integrar estas informações para utilização dos dados com o backoffice TOTVS Moda.

Para enviá-las, deve-se parametrizar primeiramente as seguintes informações:

**Mensagem: DEPARTAMENT**

**Versão: 1.000**

Envio de cadastro de seção para o TOTVS Moda.

**Exemplo de Json de Envio da mensagem:**

Dessa forma, a integração atenderá os seguintes objetivos:

1) Incluir seção: o cadastro de seção é gerado no TOTVS Folha de Pagamento e enviado para o sistema TOTVS Moda.  
2) Alteração de seção: a alteração de seção é gerada no TOTVS Folha de Pagamento e enviada para o sistema TOTVS Moda.  
3) Exclusão de seção: a exclusão de seção é gerada no TOTVS Folha de Pagamento e enviada para o sistema TOTVS Moda.

**Observação:**

Ao fazer a integração da Seção com o BackOffice TOTVS Moda é necessário verificar se o Centro de Custo informado é um Centro de Custo integrado do BackOffice TOTVS Moda. O processo faz a consistência do campo e caso o centro de custo não foi integrado, retornar erro que pode ser verificado na informação da execução da mensagem.

Para verificar se a integração dos dados foi enviada corretamente para o TOTVS MODA, após acionar os gatilhos citados acima acesse o módulo RM | RH | Integração | EA 2.0 | Mensagens | Gerenciamento de Mensagens, pesquise pelo registro com identificador "DEPARTAMENT", clique na pasta 'Dados da execução' , onde poderá verificar os dados de execução da mensagem.
