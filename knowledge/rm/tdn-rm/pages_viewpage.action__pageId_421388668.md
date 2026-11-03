---
content_hash: d7918dbb5272d26ef8541aacfaa998e20eca1dfb367cca370530b404771bd182
fetched_at: '2026-06-29T00:09:18.106255+00:00'
page_id: '421388668'
product: rm
source: tdn-rm
title: Baixa ou quitação do Lançamento Financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388668
version: 34
---

O processo Baixa ou quitação consiste em atualizar o Lançamento Financeiro registrando os dados que comprovem a sua quitação. Este processo está relacionado à atualização dos saldos das contas caixa e à contabilização. A baixa poderá ser realizada manualmente ou por importação de arquivos de retorno.   
A principal tabela que grava as informações das baixas realizadas é a FLANBAIXA.

No processo de baixa ou quitação do titulo:

* Poderão ser utilizados um ou vários meios de pagamento.
* Através do Anexo "Baixas do Lançamento", poderão ser visualizados todos os meios de pagamento utilizados na baixa.
* Será gravado no extrato de caixa tantos registros quantos forem os meios de pagamento utilizados.
* Todas as informações referentes à baixa ficarão armazenadas no lançamento de origem.
* Poderá haver o cancelamento de um item de baixa e o lançamento ficará com o status de parcialmente quitado.
* Não é permitida a baixa simultânea de lançamentos com e sem cheque, isto porque a representação de um cheque emitido é através de um extrato de caixa gerado para um item de baixa com status "Cheque". Assim, quando já existe um cheque, não é criada uma nova baixa, mas apenas ocorre alteração do seu status, comportamento diferente para lançamentos sem cheque. Uma forma de contornar essa situação é usar o cheque como uma forma de pagamento no processo de baixa.

Observação:

* Em relação ao processo de baixa manual, independente do SGBD (Sistema de Gerenciamento de Banco de Dados) seja SQL ou ORACLE, é recomendado que o número máximo de lançamentos a serem baixados simultaneamente não ultrapasse a quantidade de 10.000 (10 mil) registros por processo.

**Campos Complementares para Itens de Baixa**

Os campos criados serão carregados para a aba "Campos Complementares" dos novos registros dos itens de baixa gerados e na tela de baixa de lançamento (etapa "Edição do Lançamento"). Caso exista valor default para algum campo, ele será automaticamente carregado e disponibilizado para alteração na tela do item de baixa,  permitindo que o valor seja alterado. A exclusão do registro de campo complementar do item de baixa acontecerá no momento da exclusão do Item de Baixa. 

Observação: os campos complementares de item de baixa não serão exibidos para itens de baixa derivados de borderô. Somente no momento da baixa manual ou via retorno bancário é que os campos serão disponibilizados.

**Motivo de Baixa (Protheus)**

O campo ficará disponível quando a integração com o Protheus estiver ativa (TOTVS Educacional x BackOffice Protheus), quando o lançamento baixado for proveniente do Educacional e estiver vinculado a um boleto de cobrança ou de débito automático. Nesse campo será possível selecionar um dos itens da tabela dinâmica com o motivo de baixa por meio de pagamento.

* Na “Baixa Simplificada” o campo ficará disponível e será possível informar o motivo da baixa na tela "Dados da Baixa".
* Na “Baixa Completa” o campo será apresentado na visão de “Edição de Meios de Pagamento”.
* Para Retorno de Cobrança e Retorno de Débito Automático padrão ou em lote, a opção ficará disponível na tela de "Dados da Importação".

Observação:

* Em qualquer uma das formas de baixa (Manual ou Retorno), quando não informado no campo nenhum item da tabela dinâmica com o “Motivo de Baixa Protheus” ou o valor da baixa for igual a zero, o valor retornado pela mensageria será o código default do Protheus “007”.
* O cadastro de Tabela Dinâmica em Serviços Globais é por produto, para que os itens cadastrados sejam apresentados na tela de baixa será preciso cadastrar a tabela e seus itens para o produto "Gestão Financeira".

Parametrização para preenchimento via retorno do Motivo de Baixa na integração com Protheus:

Ambiente → Parâmetros → TOTVS Gestão Financeira → Baixa → Baixa7/7  
Informar os campos motivo de baixa por tipo de pagamento (Cartão de Débito, Cartão de Crédito e PIX)

Caso nenhum dos campos seja informado, o processo segue com o código default ou em branco de acordo com processo padrão.

**Valores Opcionais**

Os campos de valores opcionais cadastrados ficarão indisponíveis para alteração no processo de baixa quando a origem do lançamento for do TIN e quando houver integração com o Protheus com EAI 2.0 ativa. Dessa forma, caso seja necessário alterar o valor, será preciso entrar na tela de manutenção do lançamento (disponível ao dar duplo clique no id do lançamento localizado na coluna à esquerda da tela) a ser baixado e fazer a alteração do valor do campo opcional e posteriormente seguir normalmente com o processo de baixa.

**Controlar concorrência na baixa de lançamentos**

Para controlar a concorrência na baixa é necessário habilitar o parâmetro: "Controlar Concorrência na baixa de Lançamentos" disponível em Ambiente | Parâmetros | TOTVS Gestão Financeira | Contas a Pagar / Receber | Baixa | Manutenção de baixa | Baixa 2/5.

Funcionalidade

Quando dois os mais usuários executarem simultaneamente algum dos processos citados acima, somente um dos usuários conseguirá realizar a baixa com sucesso. A baixa será bloqueada por concorrência para os demais usuários.

Ao final do processo que está sendo executado pelo usuário o(s) lançamento(s) baixado(s) será(ão) desbloqueado(s). Caso por algum motivo inesperado na execução do serviço o(s) lançamento(s) fique(m) bloqueado(s), será necessário utilizar o processo "Corrigir Lançamentos Bloqueado por Concorrência" localizado na aba "Utilitários | Ajuste na Base" para que o mesmo seja desbloqueado. O sistema permitirá o desbloqueio na execução do processo para o usuário que efetuou o bloqueio ou por um usuário supervisor.

**Controle de aprovação para lançamentos a pagar (a partir da versão** 12.1.33)

Com o controle de aprovação de lançamentos a pagar habilitado, para lançamento a pagar, somente será possível executar o processo de baixa quando o status de controle de aprovação do lançamento estiver nos status "Aprovado" ou "Não se aplica".

Veja Também

 Informações Complementares

[Baixa Via Web Service](https://tdn.totvs.com/display/LRM/Baixa+Via+Web+Service)
