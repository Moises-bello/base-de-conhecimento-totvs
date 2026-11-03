---
content_hash: fca305dbf968d90096e2792cd17e1663004d86f0f2db239cb7649f2a863cbbb0
fetched_at: '2026-06-29T00:09:18.556897+00:00'
page_id: '421388725'
product: rm
source: tdn-rm
title: FIN - Débito Automático 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388725
version: 6
---

O processo Débito Automático é realizado mediante acordo entre a Empresa e o Cliente, que autoriza a cobrança de um determinado compromisso financeiro através de débito em suas contas correntes dispensando-lhe o envio de boletos de cobrança. O pagador (Pessoa Física ou Jurídica) autoriza ao Banco o débito de seus compromissos financeiros em sua conta corrente.

O recebedor (Pessoa Física ou Jurídica) disponibiliza um arquivo de remessa de débito automático  ao Banco contendo informações dos débitos a serem efetuados na conta corrente do pagador. O recebedor também poderá cancelar ou efetuar alterações em alguns dados do débito, antes que o mesmo seja efetuado.

O Banco é quem gerencia as contas correntes do recebedor e do pagador. Na data prevista, mediante informações obtidas em arquivo de remessa efetua o débito na conta corrente do pagador, executa a instrução de crédito na conta corrente do recebedor e envia informações sobre a efetivação do débito para o recebedor através de arquivo de retorno.

Caso ocorra alguma inconsistência na realização do débito, a não efetivação também será informada ao recebedor pelo arquivo de retorno.  
  
**Etapas do processo**

Convênio firmado entre Empresa e Banco para definir as regras do processo.

Unificamos no cadastro do Convênio toda a regra da integração Bancária. Em se tratando de Débito Automático quando o Convênio for cadastrado exclusivamente para o Débito Automático, informe apenas os dados pertinentes ao processo na pasta "Dados Adicionais".

Atualização dos Cadastros (Bancos, Agência, Conta Corrente, Convênio e Conta Caixa).

O layout FINLAY0005 - Débito Automático CNAB150– padrão Febraban existente no book de relatórios foi evoluído para que no campo identificador do registro "E" seja enviado o campo ID do Cliente/Fornecedor (FCFO.IDCFO) concatenado com o Dígito verificador do identificador de débito automático (FCFO.DIGVERIFICDEBAUTOMATICO).

Geração dos boletos de Débito Automático.

O Boleto como uma Entidade bem definida proporciona o agrupamento de Lançamentos Financeiros provenientes de qualquer segmento. É possível incluir um boleto agrupando Lançamentos gerados pelo Gestão Educacional e do Incorporação, por exemplo, sem distinção por segmento.

Geração do arquivo de remessa de débito automático pelo menu Boletos e envio ao Banco.

**Observações**

Para geração de remessa de lançamentos faturados, o sistema permite que o boleto faturado com status 'Pendente Remessa' seja remetido ao banco, para que ocorra a baixa desse boleto junto ao banco.

Processamento pelo Banco e envio de arquivo de retorno confirmando do processamento. Este primeiro arquivo, se importado na base de dados não produzirá baixas automáticas, apenas resultará na atualização do STATUS.CNAB dos Lançamentos. Havendo alguma rejeição, o Banco informará o motivo e a empresa então poderá gerar novas remessas para estes títulos.

Na data de vencimento, o Banco processa o débito automático.

O Banco envia à empresa um arquivo de retorno contendo informações de data de quitação bem como o valor debita e outras informações afins. A importação deste arquivo, cuja ocorrência caracteriza um "retorno", produzirá a baixa automática dos lançamentos.

Para lançamentos gerados a partir do TOTVS Educacional o boleto é gerado com valor zerado e o mesmo calculado no processo de remessa.
