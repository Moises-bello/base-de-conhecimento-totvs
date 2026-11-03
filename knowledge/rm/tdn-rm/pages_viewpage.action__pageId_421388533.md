---
content_hash: 2b8d96c4aa8107274a109bfa886c90ae69e5f8e63049ee07f6089e2d6e696329
fetched_at: '2026-06-29T00:09:16.946557+00:00'
page_id: '421388533'
product: rm
source: tdn-rm
title: Ajuste de transações com cartão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388533
version: 34
---

Este processo foi implementado para realizar a comunicação junto às soluções de e-commerce utilizadas no TOTVS Gestão Financeira, selecionando as transações de pagamentos via cartão de crédito/débito cujos status precisam ser ajustados.

Para utilizar este processo é preciso ter a permissão liberada. Em Serviços Globais | Segurança | Perfis, edite o perfil do usuário logado e localize a permissão [03.05.02] Ajuste de Transações.

O processo irá selecionar e atualizar os registros das transações que estiverem com os seguintes status, conforme os modelos abaixo:

* BuyPage Cielo: Sistema Acessado, Pagamento Pendente, Pagamento Efetuado, Pagamento Confirmado e Leitura de Pagamento Confirmado.
* Checkout Cielo: Sistema Acessado, Pagamento Confirmado e Pagamento Autorizado.
* IFrame Getnet: Cancelamento Pendente.
* CyberSource: Pagamento Confirmado**\***, Pagamento Autorizado, Cancelamento Pendente e Cancelamento Negado**\*\***.   
  \* Este status será gerado quando o boleto/lançamento financeiro não for baixado automaticamente no TOTVS Gestão Financeira por algum motivo, como por exemplo uma inconsistência na contabilização da baixa em algum desses títulos envolvidos.  
  \*\* Será registrado em casos onde o cliente tenha feito a solicitação de cancelamento pelo canal da adquirente e posteriormente solicitado o cancelamento também pelo processo de "Solicitação de Cancelamento" no TOTVS Gestão Financeira. Dessa forma, o cancelamento solicitado pelo TOTVS Gestão Financeira assumirá o status "Cancelamento Negado" após o processamento do ajuste de transações.
* eRede: Sistema Acessado, Pagamento Confirmado, Pagamento Autorizado e Cancelamento Pendente.
* SiTef: Pagamento Confirmado (pega somente transações onde o lançamento relacionado está com o campo Baixa Pendente como "Sitef").

Para cada registro que estiver com estes status acima, o processo irá verificar na adquirente/gateway de pagamento o status da transação e atualizará no TOTVS Gestão Financeira.

Observação: Essa verificação na adquirente/gateway não é feita para o SiTef.

### **Ajustar transação Sitef com pagamento solicitado**

Este processo deve ser executado sobre os registros selecionados na visão e tem como objetivo ajustar transações Sitef que estejam com o status **Pagamento solicitado** e cujo lançamento esteja bloqueado com baixa pendente do tipo Sitef.

Para que o processo seja executado corretamente, é necessário que na sessão de caixa onde a operação foi realizada exista um registro de histórico de pagamento como "Transação SiTef pendente" e seja informado o meio de pagamento utilizado e os dados da transação no sistema Sitef: número de parcelas, NSU, NSUSitef, código de autorização do emissor de cartão.

Após a execução, a transação passará a conter o histórico **Pagamento confirmado**. Se for identificada a sessão de caixa onde o recebimento dos títulos foram iniciados, será incluído um log na sessão informando que a transação TEF foi confirmada. Em seguida, o lançamento será desbloqueado, a baixa do(s) título(s) será realizada e será incluído um histórico na transação de Pagamento concluído. Caso ocorra erro na baixa, a transação ficará com status "Pagamento confirmado" e seu ajuste deve ser feito através do processo geral de ajuste de transação.

O processo estará disponível quando a coligada estiver parametrizada para usar o TEF na Sessão de Caixa, em *Gestão Financeira | Ambiente | TOTVS Gestão Financeira | Contas a Receber | Caixa | TEF | TEF na Sessão de Caixa.*

 Informações Complementares

* [DT - Ajuste de transação](https://tdn.totvs.com/pages/viewpage.action?pageId=515694203)
