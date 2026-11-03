---
content_hash: f52e4780ce80da364b3578b96a9b697f1f37246f5b87bd505c2a4b5ea68dc231
fetched_at: '2026-06-29T00:09:18.577723+00:00'
page_id: '421388727'
product: rm
source: tdn-rm
title: FIN - Pagamento Eletrônico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388727
version: 9
---

A remessa de Pagamento eletrônico automatiza o pagamento dos títulos através de integração com a rede Bancária por meio de arquivos de remessa e de retorno.   
Este processo envolve pagamentos de compromissos que podem ser efetuados através de PIX (transferência, QR-Code e FGTS), DOC, TED, crédito em conta, cheque administrativo, ordem de pagamento (OP), pagamento com autenticação ou títulos em cobrança, entre outros.

**Entidades Participantes**

* Pagador: Pessoa Física ou Jurídica que entrega os Pagamentos ao Banco para serem efetuados.
* Banco do Pagador: Banco que detém os Pagamentos a serem efetuados.
* Favorecido: Pessoa Física ou Jurídica a que se destina o pagamento.
* Banco do Favorecido**:**Banco que detém a conta corrente do Favorecido, a qual é creditada na efetivação do pagamento.

**Fluxo de Informações**

O Pagador agenda, junto ao Banco Pagador, os Pagamentos a serem efetuados pelo Banco. Caso seja agendado um pagamento bloqueado é necessário enviar uma informação para liberar a execução do pagamento posteriormente e, nos casos em contrário, se foi agendado um pagamento liberado é possível fazer o bloqueio do mesmo. Também é possível o Pagador efetuar alterações em alguns dados dos pagamentos, antes que o mesmo seja efetuado.

O Banco Pagador, na data prevista, efetua o débito na conta corrente do Pagador e executa a instrução para crédito do pagamento ao Favorecido. Este crédito poderá ser efetuado de acordo com as opções disponíveis no cadastro do Cliente/Fornecedor, Anexos /  Dados Bancários / Forma de Pagamento.

**Etapas do processo**

Convênio firmado entre Empresa e Banco para definir as regras do processo. Unificamos no cadastro do Convênio toda a regra da integração Bancária. Em se tratando de Pagamento Eletrônico, quando o Convênio for cadastrado exclusivamente para Pagamento não é necessário informar os dados da pasta "Dados Adicionais".

Atualização dos Cadastros (Bancos, Agência, Conta Corrente, Convênio e Conta Caixa).

Geração do Borderô de Pagamento.

Autorização ao Borderô e remessa pelo mesmo. - Selecione o Borderô e em seguida o usuário com permissão, deverá "autorizá-lo"  através do menu:  Processos / Autorização de Borderô de pagamento. - Para gerar a remessa, selecione o Borderô , Processos / Remessa Pagamento. Você poderá cadastrar uma remessa durante o processo ou então pelo menu:  Movimentações Bancárias / Integração Bancária / Cadastro Bancário / Cadastro Pagamento.

Processamento pelo Banco e envio de arquivo de retorno confirmando o processamento. Este primeiro arquivo, se importado na base de dados não produzirá Baixas automáticas, apenas resultará na atualização do STATUS.CNAB dos Lançamentos. Havendo alguma rejeição, o Banco informará o motivo e a empresa então poderá gerar novas remessas para estes títulos.

Na data de pagamento o Banco processa conforme instruções do arquivo de remessa.

O Banco envia à empresa um arquivo de retorno contendo informações de data de quitação, bem como o valor pago e outras informações afins. A importação deste arquivo, cuja ocorrência caracteriza um "retorno", produzirá a baixa automática dos lançamentos.

**Gera sequencial do lançamento na Remessa**

Ao gerar a remessa de pagamento padrão SIACC, para cada lançamento financeiro enviado, será gravado no campo FLAN.SEQSIACC um valor de identificação único daquela operação e o mesmo enviado nos dados do registro no arquivo de remessa. Caso o número sequencial chegue a 999.999 o sequencial volta para 1.  
A faixa de numeração usada nesse padrão é gerada pelo banco a partir da solicitação da empresa.

 Veja Também
