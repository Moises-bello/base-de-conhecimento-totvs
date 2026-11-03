---
content_hash: 4654cd538cece17686302694a2c61c0b469856dbc39ad753a09f588ddab6af9e
fetched_at: '2026-06-29T00:09:17.721345+00:00'
page_id: '421388629'
product: rm
source: tdn-rm
title: Gerar Cheque Manual
type: documentation
url: https://tdn.totvs.com/display/LRM/Gerar+Cheque+Manual
version: 2
---

A geração de cheque manual é realizada através do processo "Gerar Cheque Manual" do cadastro de Extrato de Caixa.  
 O objetivo deste processo é realizar a geração de cheque para um registro manual de extrato de caixa. O cheque possuirá apenas o número (cheques a receber e a pagar) e um nominal (cheques a pagar).  
 Não é possível gerar cheque manual para: Mais de um registro ao mesmo tempo; Registro Cancelado; Registro Compensado; Registro de CPMF; Registro gerado pela baixa ou emissão/recebimento de cheque. Informações sobre alguns campos do processo:

**Número do Cheque**

Para extratos com a operação "Depósito Manual" o sistema apresenta por default o número informado no campo "Número Documento" na "Identificação" do registro de extrato de caixa.

Para extratos com a operação "Saque Manual" o sistema permite utilizar três opções:

* Usar número do Documento É apresentado por default o número informado no campo "Número Documento" na Identificação do Extrato de Caixa, não podendo ser alterado.
* Buscar cheque da Conta/Caixa O sistema informa um número de acordo com o último número de cheque informado no cadastro da conta/caixa utilizada no registro. Não podendo ser alterado.

**Exemplo**

No campo "Último Cheque" da pasta "Dados Adicionais" da Conta/Caixa é informado que o último cheque emitido é de número "000003". Ao marcar a opção "Buscar cheque da Conta/Caixa" o sistema apresenta por default o número "000004", ou seja, um número a mais do que o último cheque emitido. Ao gerar o cheque, o último número informado na conta/caixa é atualizado automaticamente.

* Informar cheque Manualmente Você pode informar o número que desejar.

**Dados do Cheque**

Nominal

Neste campo você pode informar um nominal para ser utilizado na impressão de cheques emitidos.

**Observação**  
 Ao gerar um cheque manual o número do documento do registro é alterado para o número do cheque.
