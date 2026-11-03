---
content_hash: 165534970f1123f0c8cb831506e4208e1e2904be1799e216d1df0badf1f30d91
fetched_at: '2026-06-29T00:09:27.971171+00:00'
page_id: '423938594'
product: rm
source: tdn-rm
title: Variáveis que podem ser utilizadas no complemento de histórico contábil do
  Totvs Gestão Financeira 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938594
version: 14
---

[CCF]                             Código do Cli/For

[FAN]                             Nome Fantasia do Cli/For

[NOM]                            Nome do Cli/For

[RAZ]                             Nome do Cli/For

[NUM]                            Número do Documento

[HIS]                              Histórico

[HEX]                             Histórico de Extrato

[NOC]                            Nominal do Cheque

[DVF]                             Data de Vencimento da Fatura

[MDC]                            Mês de Competência

[NCH]                             Número do Cheque

[EMI]                              Data de Emissão

[VEN]                             Data de Vencimento

[CHA]                             Chapa do Funcionário

[FUN]                             Nome do Funcionário

[TDO]                             Código do Tipo de Documento

[DTD]                             Descrição do Tipo de Documento

[CXA]                             Código da Conta/Caixa

[DCX]                             Descrição da Conta/Caixa

[CT1]                              Código de Tab Op 1

[CT2]                              Código de Tab Op 2

[CT3]                              Código de Tab Op 3

[CT4]                              Código de Tab Op 4

[CT5]                              Código de Tab Op 5

[DTT1]                            Descrição de Tab Op 1

[DTT2]                            Descrição de Tab Op 2

[DTT3]                            Descrição de Tab Op 3

[DTT4]                            Descrição de Tab Op 4

[DTT5]                            Descrição de Tab Op 5

[DO1]                              Data Op 1

[D02]                               Data Op 2

[D03]                               Data Op 3

[D04]                               Data Op 4

[D05]                               Data Op 5

[REF]                               Referência do Lançamento

[DCH]                              Data do Cheque

[BAI]                                Data da Baixa

[DCI]                                Data Contábil da Inclusão

[NCI]                                Número Contábil da Inclusão

[NCB]                               Número Contábil da Baixa

[CCU]                               Código do Centro de Custo

[DEP]                               Código do Departamento

[DCG]                              Descrição do Centro de Custo Globa

[DDG]                              Descrição do Departamento Global

[CCL:"nome do campo"]  Valores dos Campos Complementares do Lançamento

[TAF:"nome do campo"]  Valores dos campos do Tipo de Aplicação Financeira

[VEX]                               Valor do Extrato

[SNU]                               Segundo Número do Lançamento

[CXT]                               Código da Conta/Caixa Transferência

[DCT]                               Descrição da Conta/Caixa Transferência

**Observações**

As variáveis acima quando inseridas no complemento de histórico não podem ter o tamanho aumentado ou diminuído pelos colchetes, as mesmas devem ser inseridas sem espaço da forma que o sistema sugere.

A variável [NOC] não irá funcionar no caso do cheque parcial, pois não seria possível escolher de qual cheque trazer o nominal.

A variável [CCL] contempla também o parâmetro "Histórico Padrão da Baixa Parcial". Se essa nova variável for colocada ali, os novos lançamentos gerados nas Baixas Parciais terão os Históricos com essa variável substituída pelos valores dos Campos Complementares do lançamento que geraram estas baixas parciais.

A variável data do cheque [DCH] apenas será levada corretamente no caso de apenas um cheque para um ou mais lançamentos.

No caso da utilização de cheques parciais, como existe mais de um cheque, esta data pode variar.

Ao utilizar a variável de campos complementares do lançamento digite a variável e o nome do campo desejado.

**Exemplo**

Você criou o campo complementar "DATACONFERENCIA" (nome informado no campo "Nome da Coluna", menu Cadastros | Campos Complementares | Lançamentos). Ao utilizar a variável, digite [CCL:DATACONFERENCIA]. Se você quiser utilizar mais de um campo, digite a variável para cada campo.

**Exemplo**

[CCL:DATACONFERENCIA] [CCL:RESPONSAVEL]

Ao utilizar a variável de campos do tipo de aplicação financeira digite a variável e o nome do campo desejado. O nome do campo deve ser o nome informado na tabela FTIPOAPLFIN.

**Exemplo**

Você deseja enviar os valores dos campos "Referência", "Descrição", "Código Conta/Caixa" e "Natureza". Ao utilizar a variável digite [TAF:IDTIPOAPLFIN] [TAF:NOME] [TAF:CODCXA] [TAF:TIPOAPLICACAO].
