---
content_hash: 860d39757957b11922580707385b677355a7a5ca53a7fa60af41c6e35af9e847
fetched_at: '2026-06-29T00:09:18.467293+00:00'
page_id: '421388702'
product: rm
source: tdn-rm
title: FIN - Retorno Bancário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388702
version: 5
---

A importação de arquivos de retorno é  um recurso do sistema, que consiste em baixar automaticamente ou atualizar o Lançamento Financeiro por meio de  importação de arquivos disponibilizados pela rede Bancária.  
Em se tratando de Cobrança, Pagamento e Débito Automático, a baixa será realizada automaticamente desde que o arquivo de retorno possua os dados necessários, assim como data de crédito, valor do crédito, motivo de ocorrência específica para baixas ou quitações,  entre outras informações requeridas.

Alguns arquivos de retorno reportam apenas atualizações para o lançamento financeiro, provenientes de transações entre empresa e Banco.  Um exemplo dessa transação é o arquivo de retorno que o Banco disponibiliza à empresa informando do processamento dos títulos. Ao importar esse arquivo a única alteração a ser feita é a atualização do STATUS.CNAB do lançamento para "Registrado" e não produzirá baixas.   
   
**Tabela de Item de Retorno Bancário** (FRETORNOBANCARIOITEM)

Objetivo

Inserir no banco de dados todos as linhas importadas no retorno bancário de pagamento, cobrança e débito automático.  
Existem dois objetivos na evolução desse processo. O primeiro é manter um log dos registros lidos no retorno bancário. O outro é permitir que o processo seja quebrado em duas fases: importação do arquivo no banco de dados e processamento do mesmo.

**Definição da Regra de Negócio**

Foram criados dois novos campos na tabela de Item de Retorno Bancário.

* O primeiro é o Sequencial do Item de Retorno (SEQITEMRETORNO) que irá compor, juntamente com o campo IDRETORNO, a chave primária da tabela FRETORNOBANCARIOITEM.
* O segundo campo, CHAVELAN, armazenará a chave de identificação do lançamento na linha detalhe do arquivo importado, o valor da mesma é usado para identificar a qual lançamento/boleto aquela linha está relacionada.

Todos os registros de detalhe lidos do arquivo de importação de retorno de cobrança, pagamento ou débito automático serão armazenados na tabela de Item de Retorno Bancário mesmo que ocorra erros no processo. As linhas importadas terão o campo CHAVELAN preenchidas.

Anteriormente o processo de checagem dos dados do retorno em relação aos lançamentos relacionados criava mais de uma linha na tabela de Item de Retorno Bancário caso o boleto identificado vinculado a mais de um lançamento. Esse comportamento não mais existirá, somente uma linha ficará gravada e na mesma armazenada somente o Identificador do boleto e os campos de valor (Valor Baixado, Multa, Juros, Desconto e Opcional 1 a 8), com exceção de Valor Líquido que terá os valores somados de todos os lançamento envolvidos, conterão os valores lidos do arquivo.

O campo de identificação do lançamento na tabela de Item de Retorno Bancário (IDLAN) somente será preenchido caso o retorno não seja por boleto. Assim, se o Identificador do Boleto (IDBOLETO) for preenchido, a Referência do Lançamento (IDLAN) ficará com valor nulo.

Erros durante o processo são gravados na coluna LOGRETORNO da FRETORNOBANCARIOITEM, para cada item do retorno, que por algum motivo não foi processado de acordo com o esperado.

**Tabelas Utilizadas**

FRETORNOBANCARIO – Retorno Bancário  
FRETORNOBANCARIOITEM – Item de Retorno Bancário.

Veja Também
