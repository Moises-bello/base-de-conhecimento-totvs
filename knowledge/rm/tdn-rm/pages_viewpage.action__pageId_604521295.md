---
content_hash: c487d7a13258dd26bf2d0854fbc5580a4e9078bd139ac24c54b0541d39ce8086
fetched_at: '2026-06-29T00:10:58.224097+00:00'
page_id: '604521295'
product: rm
source: tdn-rm
title: Totvs Folha de Pagamento RM x TOTVS Moda - Transferência de Funcionário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=604521295
version: 4
---

**Integração Totvs Folha de Pagamento RM x TOTVS Moda - Transferência de Funcionário**

A Integração Totvs Folha de Pagamento RM x TOTVS Moda de Transferência de funcionário tem o objetivo de enviar os dados de transferências visando integrar estas informações para utilização dos dados com o BackOffice TOTVS Moda.

Para enviá-las, deve-se parametrizar primeiramente as seguintes informações:

**Mensagem: SETEMPLOYEEBRANCHTRANFER**

**Versão: 1.000**

Envio da transferência de funcionário para o TOTVS Moda.

**Exemplo de Json de Envio da mensagem:**

Dessa forma, a integração atenderá os seguintes objetivos:

Transferência de Funcionário: a transferência de funcionário é realizada através do processo de rescisão onde, o tipo de rescisão deve ser (5- Transferência sem ônus p/ Cedente ou 6- Transferência com ônus p/ Cedente). Este processo será gerado no TOTVS Folha de Pagamento e enviado para o sistema TOTVS Moda.

Para verificar se a integração dos dados foi enviada corretamente para o TOTVS Moda, após acionar os gatilhos citados acima acesse o módulo RM | RH | Integração | EA 2.0 | Mensagens | Gerenciamento de Mensagens, pesquise pelo registro com identificador "SETEMPLOYEEBRANCHTRANFER", clique na pasta 'Dados da execução' , onde poderá verificar os dados de execução da mensagem.
