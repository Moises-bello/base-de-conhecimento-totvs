---
content_hash: 19167a889fbcd05e360f13181d8cdedec47d4f647186e76597296c4b2a5bf958
fetched_at: '2026-06-29T00:11:05.508552+00:00'
page_id: '631852671'
product: rm
source: tdn-rm
title: FAQ - PIX
type: documentation
url: https://tdn.totvs.com/display/LRM/FAQ+-+PIX
version: 20
---

**Posso ter acesso a conta transitória do Banco Original?**

Hoje esta conta não possui  acesso devido o produto ser de uma conta transitória de repasse (Desburocratizada), não há Gerente ou mesmo número de conta para acessar. 

A função da conta será apenas de repassar os valores PIX para a conta destino aberta pelo representante legal no portal Shipay/Original.

**Existe legislação do BACEN que regulamente o funcionamento de contas bancárias transitórias?**

Sim. Esta conta “transitória”, é uma conta de pagamento (pré-paga PJ), a regulamentação acerca de contas de pagamento, consta no link: [https://www.in.gov.br/web/dou/-/resolucao-n-96-de-19-de-maio-de-2021-32123374](https://www.in.gov.br/web/dou/-/resolucao-n-96-de-19-de-maio-de-2021-321233745)

**Tenho auditoria interna/externa e preciso ter acesso ao extrato da conta do Banco Original. Como faço?**

A conta do Banco do Original não prevê acesso a extratos.

Para fins de auditoria, existe a plataforma Confirmation > <https://am-pt.confirmation.com/>  na qual o Banco Original é cadastrado e pode auxiliar neste processo. Esta plataforma é para o auditor, sendo os custos da empresa auditora.

**Gostaria de incluir um novo CNPJ para recebimento com PIX, como devo proceder?**

Deve ser  comunicado ao time pelo e-mail [suporte.pix@totvs.com.br](mailto:suporte.pix@totvs.com.br) para que sejam iniciados os cadastros e liberação de acessos necessários. As demais etapas, serão orientadas após este contato.

**Como posso incluir novos usuários para acessar o portal da Shipay?**

Para cadastro de novos usuários, deve ser enviado ao e-mail [suporte.pix@totvs.com.br](mailto:suporte.pix@totvs.com.br) a solicitação com os seguintes dados:

* Nome completo
* E-mail
* Telefone com DDD
* CPF

**Como faço a parametrização do PIX no Educacional?**

**Além do** ***Portal do Aluno*****, existe outra forma de pagamento via PIX?**

Sim. O TOTVS Pagamento Instantâneo está disponível também no App Meu eduCONNECT, Processo Seletivo e Módulo de Caixa.

Módulo de Caixa >

**É possível enviar o Qr Code do PIX via e-mail ou junto com o boleto?**

O QR Code é válido por 1 hora após ser gerado, por isso, no momento não possuímos outras formas de disponibilização além do Portal do Aluno, Processo Seletivo, Meu eduCONNECT ou Módulo de Caixa.

**Como deve ser criado o evento contábil para inserir nos parâmetros do PIX?**

O evento deve ser gerado no processo de Extrato de Caixa.

Confira na documentação auxiliar:

**É possível ter duas contas para o mesmo CNPJ?**

Não é possível. É permitida somente 1 conta por CNPJ para recebimento do PIX.

Esta conta já deverá ser existente para o CNPJ em questão, e deve ser a mesma do CNPJ.

**Ao tentar gerar QR Code, é exibido o erro:**

"Houve um erro ao realizar a comunicação com o outro serviço. Authentication failed"

Conferir se as URL's abaixo estão liberadas no servidor de Job:

<https://raas.varejo.totvs.com.br/pay-hub/transacting>

 [https://NOMEDOCLIENTE.rac.totvs.app/totvs.rac/user](https://MUDAR.rac.totvs.app/totvs.rac/user)

[https://NOMEDOCLIENTE.rac.totvs.app/totvs.rac/connect/token](https://nomedocliente.rac.totvs.app/totvs.rac/connect/token)

ATENÇÃO: Nas duas últimas URL's note que após o **https://** está escrito **"NOMEDOCLIENTE"** na URL abaixo:

No campo **NOMEDOCLIENTE** é necessário inserir o nome que consta na tenant cadastrada nos parâmetros do TOTVS Gestão financeira.

**Ao tentar gerar QR Code, é exibido o erro:**

"Houve um erro ao realizar a comunicação com o outro serviço. Token has expired".

Se trata de um erro momentâneo de *timeout*, e pode ser realizada a nova tentativa imediatamente.

Caso persistir, o time de produto (Varejo) deve ser acionado.

**Ao tentar gerar QR Code, é exibido o erro:**

"Ocorreu um erro ao solicitar o token de acesso"

Neste caso, a tenat do cliente foi criada diferente da disponibilizada na URL no RASS e foi necessário o time de varejo criar nova tenant.

**A transação não está gerando TID no extrato de caixa**

Este problema ocorre quando o tipo primitivo do meio de pagamento não está marcado como Pagamento Instantâneo (PIX).

Solução: É necessário excluir o meio de pagamento incorreto e criar um novo com a opção de PIX. Em seguida, inserir nos parâmetros do sistema.

**Ao rodar a conciliação é exibida a mensagem de erro 500 Internal Server Error**

Isso ocorre devido ao tipo de parametrização do cliente ser por recebimento por filial.

Solução: Esta inconsistência foi corrigida nos patchs:

12.1.32.273 12.1.33.236 12.1.34.141

**Ao rodar a conciliação, no RM é exibida a mensagem de erro ao solicitar o token e no Portal ao gerar QR Code:**

"Houve um erro ao realizar a comunicação com o outro serviço. Unknown error".

O cliente havia alterado dados na chave de PIX do RASS (Client ID e Client Secret).   
Foi necessário o time de produto (Varejo) criar nova chave para normalização.

**Ao rodar a conciliação, no RM é exibida a mensagem de erro: URL do TOTVS não foi informada.**

Solução: Quando o cliente tem parametrização somente por filial é necessário, inserir nas configurações a tenant e usuário e senha:

**Ao rodar a conciliação, no RM a execução é concluída, mas é exibida a mensagem de erro: Arquivo coligada 1 id. conciliação 10 não possui transações.**

Este caso ocorre por dois motivos:

**1º** O cliente não possui intenção de conciliação.

Solução: Esta intenção deve ser realizada pelo time de produto (Varejo)

**2º** A API de conciliação não está trazendo os arquivos

Solução: Acionar o time de produto (Varejo), para que seja verificado, e que possam reprocessar as transações via API.

**Ao rodar a conciliação, no RM apresenta erro nas transações com a mensagem:**

*Erro na conciliação Id. 1631 - Operação.   - TID. e81d63fc-9426-46a6-b8d3-e14064ea290d - NSU.  -Parcela. 1 Mensagem: Campo 'Valor' no extrato de caixa é obrigatório.*  
*Por favor, verificar se documento de geração do extrato de caixa tem o campo preenchido, ou se o extrato de caixa relacionado ao documento tem o campo preenchido.*

O problema é no arquivo de conciliação, onde o valor líquido vem zerado. Para confirmar:

Movimentações Bancárias > Conciliação

Selecione o ID referente a conciliação e clique em Anexos > Operação de Venda

Solução: O time de produto (Varejo) deve ser acionado para correção e reprocessamento do título.

**Pagamento expirado no TOTVS e aprovado na Shipay**

Este caso ocorre em algumas situações de expiração do QR Code e atraso na atualização do status na comunicação TOTVSxShipay

Solução: Após confirmação do Status APROVADO na Shipay (o que indica que houve repasse do pagamento), é necessário realizar um procedimento via banco de dados para alteração do status no sistema:

**\*PROCEDIMENTO:**

Para que o sistema identifique e altere o status, é preciso fazer o seguinte processo:

Se o título tiver sido baixado manualmente é necessário cancelar a baixa.

- Update para alterar o status da transação que estava expirada para **solicitada**.

UPDATE FINTEGRACAOCARTAO SET IDSTATUS = 1 WHERE REQUESTID = 'COLOCAR O IDENTIFICADOR DE TRANSAÇÃO TPD AQUI'

Obs: O TPD é o ID de pagamento indicado na coluna "Identificador transação TPD" no sistema TOTVS.

Em seguida, rodar o ajuste de transação para verificar se o pagamento foi identificado na shipay e no Totvs passou para **concluído** e fez a baixa.
