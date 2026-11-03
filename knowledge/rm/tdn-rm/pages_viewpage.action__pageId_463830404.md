---
content_hash: 766461e1dcc5de149e20f062ca1804be6272b1a0e7cacd484ec4c58d585c2b56
fetched_at: '2026-06-29T00:10:15.322621+00:00'
page_id: '463830404'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Utilitarios - Assistente de Cobranca
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=463830404
version: 7
---

O processo Assistente de Cobrança foi criado para simplificar a cobrança de débitos dos seus clientes, possibilitando o envio de emails (incluindo o boleto ou não) e SMS de cobrança para cada lançamento selecionado, podendo criar agendamentos ou ser executado manualmente, facilitando campanhas de cobrança de recebíveis em atraso, campanha para adiantamento de recebíveis ou outras campanhas.

# Configuração:

Para a utilização do Assistente de cobrança, é necessário que a configuração de e-mails e / ou de SMS estejam corretas.

Para mais detalhes sobre a configuração de e-mails, .

Para mais detalhes sobre a configuração de SMS, .

# Funcionamento:

## Seleção de lançamentos

Na tela de seleção de lançamentos, o usuário  irá definir o filtro a ser usado para buscar os lançamentos desejados.  
Este filtro segue o padrão dos filtros da linha RM e o usuário poderá usar os filtros já criados para a tela de Lançamentos financeiros. Os lançamentos que estiverem de acordo com o filtro selecionado serão exibidos na tela.  
Será enviado e-mail / SMS para o Cliente / Fornecedor de cada lançamento retornado pelo filtro. Não será realizado nenhuma forma de agrupamento de e-mails, SMSs ou lançamentos, sendo processado individualmente cada lançamento.

**Importante**:

Lançamentos a Receber devem possuir o **Status CNAB** como **Registrado**.

Não podem ser usados parâmetros para filtrar os lançamentos. Este processo será executado no servidor, e, para isto, é necessário que os parâmetros sejam dinâmicos. Exemplo: Vencimento = $Hoje - 10

Para maiores informações sobre criação de filtros,

## Parametrização do processo

## 

Nesta tela o usuário irá definir como será o contato com seu cliente:

**Enviar cobrança por e-mail:**

Se marcada esta opção, serão enviados e-mails para os Clientes associados a cada lançamento. Caso sejam selecionados 10 lançamentos de um mesmo cliente, serão enviados 10 e-mails para ele.

As configurações para isto são:

* **Anexar boleto**: Esta opção define se será anexado o boleto junto ao e-mail. Caso não seja possível gerar ou localizar o boleto do lançamento, um alerta será emitido e a cobrança para os lançamentos sem boletos não serão enviadas.
* **Relatório que irá compor o CORPO do e-mail**: Aqui deve ser selecionado o relatório que será enviado para os clientes.
  + O relatório deve ser criados conforme a necessidade e neles deve haver os parâmetros "COLIGADA" e "IDLAN" ou deve possuir a FLAN como tabela principal. O processo irá definir o valore dos parâmetros ou, caso não existam, será passado o filtro do lançamento.
* **Assunto do e-mail**: Define o texto que será incluído no campo Assunto. Será o mesmo texto para todos os e-mails
* **Nome**: Nome que irá ser exibido como o Remetente que está enviando o e-mail
* **E-Mail**: Endereço de e-mail que irá ser exibido como do Remetente que está enviando o e-mail

**Enviar cobrança por SMS:**

Se marcada esta opção, serão enviados SMS para os Clientes associados a cada lançamento. Caso sejam selecionados 10 lançamentos de um mesmo cliente, serão enviados 10 e-mails para ele.

Para o envio de SMS, por se tratar de mensagem curta para celular e sem opções de configurações de layout, a única parametrização possível é a definição do texto que será enviado para cada cliente.

Para possibilitar a customização da mensagem para cada lançamento, foram disponibilizados os mnemônicos abaixo, que serão substituídos nos SMSs por dados de cada lançamento:

[CLI]: Nome do cliente  
[CONT]: Número do contrato  
[VLR]: Valor líquido  
[VCTO]: Data de vencimento  
[BARR]: Linha digitável do código de barras

Para finalizar, basta executar o processo que os e-mails e SMSs serão enviados conforme definido.

# Agendamento do processo:

É possível realizar o agendamento do processo, para que execute periodicamente conforme parametrização realizada. Para maiores informações sobre agendamento de processos, [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005088792-RM-Frame-Como-agendar-a-execu%C3%A7%C3%A3o-de-um-processo-).
