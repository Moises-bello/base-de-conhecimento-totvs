---
content_hash: fbc64fa86e65daa8e1b00f0210252e495bc500e1037797174df414b0f63c759a
fetched_at: '2026-06-29T00:08:22.093535+00:00'
page_id: '269071482'
product: rm
source: tdn-rm
title: Migração do Processo de Automação Comercial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269071482
version: 9
---

# Importação-Exportação de Automação Comercial / Migração Legado

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | **RM** | | |
| ****Segmento Executor:**** | **Construção e Projetos** | | |
| **Módulo:** | ***TOTVS Gestão de Estoque, Compras e Faturamento*** | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Conceito* | *ConConceitoAction* | | Layout do Gerador de Saída | GenLayoutAction | | | |
| **Chamado:** | *Não se aplica.* | | |
| **Requisito (ISSUE):** | CPMOV001-668 | | |
| **País:** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros:** |  | | |

### Objetivo

Com a intenção de facilitar os processos de integração do ERP com bases e sistemas legados, ou mesmo a extração de dados do ERP, a TOTVS disponibilizará os layouts de exportação e importação da Automação Comercial como objetos gerenciais padrões e distribuídos junto ao instalador da biblioteca RM.

## Definição da Regra de Negócio

 

**Exportação de Automação Comercial**

 

 Para realizar a exportação de Automação Comercial será criado o layout de exportação utilizando-se o Gerador de Saídas que é uma ferramenta criada para exportar dados de qualquer módulo da Linha RM através de um layout pré-definido pelo sistema.O arquivo gerado na exportação tem como base as tabelas TREDUCAOZ e TCUPOMFISCAL e seus relacionamentos e deverá ter o formato dos layouts abaixo:

 

### **Layout 1:**

Informações da Redução Z:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tamanho** | **Posição Inicial** | **Tipo** | **Descrição** |
| *Marca de Início* | 1 | 1 | CARACTER | Identificação da Linha (Valor fixo "R") |
| CODCOLIGADA | 5 | 2 | INTEIRO | Código da Coligada |
| PONTOVENDA | 10 | 7 | CARACTER | Ponto de Venda |
| NUMEROREDUCAO | 10 | 17 | INTEIRO | Número da Redução |
| DATAMOVIMENTO | 10 | 27 | DATA | Data de Movimento |
| DATAREDUCAO | 10 | 37 | DATA | Data de Redução |
| GRANDETOTAL | 10 | 47 | VALOR | Grande Total |
| CANCELAMENTOS | 10 | 57 | VALOR | Cancelamentos |
| DESCONTOS | 10 | 67 | VALOR | Descontos |
| ACRESCIMOS | 10 | 77 | VALOR | Acréscimos |
| ACRESCIMOSFIN | 10 | 87 | VALOR | Acréscimos Financeiros |
| COO | 10 | 97 | CARACTER | Ordem de Operação |
| CNSI | 10 | 107 | CARACTER | Contador Não Sujeito ICMS |
| GRANDETOTALANT | 10 | 117 | VALOR | Grande Total Anterior |
| COOANT | 10 | 127 | INTEIRO | Ordem Operação Anterior |
| SERIE | 4 | 137 | CARACTER | Série |
| CODTDO | 10 | 141 | CARACTER | Tipo de Documento |
| CODCOLCFO | 5 | 151 | INTEIRO | Coligada do Cliente Fornecedor |
| CODCFO | 25 | 156 | CARACTER | Código do Cliente Fornecedor |
| QTDEDOCCANCELADOS | 10 | 181 | INTEIRO | Quantidade de Documentos Cancelados |

Informações do Item de Redução Z:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tamanho** | **Posição Inicial** | **Tipo** | **Descrição** |
| *Marca de Início* | 1 | 1 | CARACTER | Identificação da Linha (Valor fixo "T") |
| TRIBUTACAOECF | 10 | 2 | CARACTER | Código Tributação |
| TOTALPARCIAL | 10 | 12 | VALOR | Totalizador Parcial |

Informações do Cupom Fiscal:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tamanho** | **Posição Inicial** | **Tipo** | **Descrição** |
| *Marca de Início* | 1 | 1 | CARACTER | Identificação da Linha (Valor fixo "C") |
| CODCOLIGADA | 5 | 2 | INTEIRO | Código da Coligada |
| PONTOVENDA | 10 | 7 | CARACTER | Ponto de Venda |
| CRO | 5 | 17 | INTEIRO | Contador de Reinício de Operação |
| NUMERO | 10 | 22 | INTEIRO | Número do Cupom |
| COO | 10 | 32 | INTEIRO | Contador de Ordem de Operação |
| DATAEMISSAO | 10 | 42 | DATA | Data de Emissão |
| HORARIO | 10 | 52 | DATA | Horário de Emissão |
| CODCOLCFO | 5 | 62 | INTEIRO | Coligada do Cliente/Fornecedor |
| CODCFO | 25 | 67 | CARACTER | Cliente/Fornecedor |
| VALORLIQUIDO | 10 | 92 | VALOR | Valor do Cupom |
| DESCONTO | 10 | 102 | VALOR | Desconto do Cupom |
| ACRESCIMO | 10 | 112 | VALOR | Acréscimo do Cupom |
| VALORRECEBIDO | 10 | 122 | VALOR | Valor Recebido |
| CAIXA | 10 | 132 | INTEIRO | Número do Caixa |
| NUMEROREDUCAO | 10 | 142 | INTEIRO | Número da Redução |
| CANCELADO | 5 | 152 | INTEIRO | Eh cupom cancelado? |
| CNPJCPFADQUIRENTE | 20 | 157 | CARACTER | CNPJ/CPF do Adquirente |
| NOMEADQUIRENTE | 40 | 177 | CARACTER | Nome do Adquirente |

Informações de Item de Cupom Fiscal:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tamanho** | **Posição Inicial** | **Tipo** | **Descrição** |
| *Marca de Início* | 1 | 1 | CARACTER | Identificação da Linha (Valor fixo "I") |
| NUMEROITEM | 10 | 2 | INTEIRO | Número do Item de Cupom Fiscal |
| CODIGOPRD | 30 | 12 | CARACTER | Código do Produto |
| QUANTIDADE | 10 | 42 | VALOR | Quantidade |
| PRECOUNITARIO | 10 | 52 | VALOR | Preço Unitário |
| VALORBRUTO | 10 | 62 | VALOR | Valor Bruto do Item de Cupom |
| DESCONTO | 10 | 72 | VALOR | Desconto do Item de Cupom |
| ACRESCIMO | 10 | 82 | VALOR | Acréscimo do Item de Cupom |
| RATEIODESCONTO | 10 | 92 | VALOR | Rateio do Desconto do Cupom |
| RATEIOACRESCIMO | 10 | 102 | VALOR | Rateio do Acréscimo do Cupom |
| VALORLIQUIDO | 10 | 112 | VALOR | Valor do Item de Cupom |
| CANCELAMENTO | 10 | 122 | VALOR | Valor do Cancelamento do Item de Cupom |
| TRIBUTACAOECF | 10 | 132 | CARACTER | Código de Tributação ECF |
| CODNAT | 20 | 142 | CARACTER | Natureza |
| ALIQUOTA | 10 | 162 | VALOR | Alíquota do Tributo |
| CST | 3 | 172 | CARACTER | Código Situação Tributária |
| CANCELADO | 5 | 175 | INTEIRO | Eh item de cupom cancelado? |
| CODUND | 5 | 180 | CARACTER | Código da Unidade de Venda |

Informações de Pagamento do Cupom Fiscal:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tamanho** | **Posição Inicial** | **Tipo** | **Descrição** |
| *Marca de Início* | 1 | 1 | CARACTER | Identificação da Linha (Valor fixo "P") |
| NUMEROPARCELA | 10 | 2 | INTEIRO | Número do Pagamento |
| DEBITOCREDITO | 1 | 12 | CARACTER | Débito / Crédito |
| CODCPG | 5 | 13 | CARACTER | Condição de Pagamento |
| VALOR | 10 | 18 | VALOR | Valor do Pagamento |
| DATAVENCIMENTO | 10 | 28 | DATA | Data de Vencimento |
| CODFORMAPAGTO | 10 | 38 | CARACTER | Forma de Pagamento |
| BANCO | 4 | 48 | CARACTER | Banco |
| AGENCIA | 20 | 52 | CARACTER | Agência |
| CC | 20 | 72 | CARACTER | Conta/Corrente |
| CHEQUE | 20 | 92 | CARACTER | Número do Cheque |
| CODCOLCXA | 5 | 112 | INTEIRO | Coligada da Conta Caixa |
| CODCXA | 10 | 117 | CARACTER | Conta Caixa |
| CAMPOLIVRE | 10 | 127 | CARACTER | Campo Livre |
| NOMEEMITENTE | 30 | 137 | CARACTER | Nome do Emitente do Cheque |
| TELEMITENTE | 15 | 167 | CARACTER | Telefone do Emitente |

Informações de Relacionamento Item de Cupom x Item de Movimento:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tamanho** | **Posição Inicial** | **Tipo** | **Descrição** |
| *Marca de Início* | 1 | 1 | CARACTER | Identificação da Linha (Valor fixo "J") |
| SERIE | 8 | 2 | CARACTER | Série |
| NUMEROMOV | 12 | 10 | CARACTER | Número do Movimento |
| CODFILIAL | 10 | 22 | INTEIRO | Filial |
| CODTDO | 10 | 32 | CARACTER | Documento |
| CRO | 5 | 42 | INTEIRO | Contador de Reinício de Operação |
| NUMEROSEQUENCIAL | 10 | 47 | INTEIRO | Sequencial do Item de Movimento |

### **Layout 2:**

Informações da Redução Z:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tamanho** | **Posição Inicial** | **Tipo** | **Descrição** |
| *Marca de Início* | 1 | 1 | CARACTER | Identificação da Linha (Valor fixo "R") |
| CODCOLIGADA | 5 | 2 | INTEIRO | Código da Coligada |
| PONTOVENDA | 10 | 7 | CARACTER | Ponto de Venda |
| NUMEROREDUCAO | 10 | 17 | INTEIRO | Número da Redução |
| DATAMOVIMENTO | 10 | 27 | DATA | Data de Movimento |
| DATAREDUCAO | 10 | 37 | DATA | Data de Redução |
| GRANDETOTAL | 20 | 47 | VALOR | Grande Total |
| CANCELAMENTOS | 20 | 67 | VALOR | Cancelamentos |
| DESCONTOS | 20 | 87 | VALOR | Descontos |
| ACRESCIMOS | 20 | 107 | VALOR | Acréscimos |
| ACRESCIMOSFIN | 20 | 127 | VALOR | Acréscimos Financeiros |
| COO | 10 | 147 | CARACTER | Ordem de Operação |
| CNSI | 10 | 157 | CARACTER | Contador Não Sujeito ICMS |
| GRANDETOTALANT | 20 | 167 | VALOR | Grande Total Anterior |
| COOANT | 10 | 187 | INTEIRO | Ordem Operação Anterior |
| SERIE | 4 | 197 | CARACTER | Série |
| CODTDO | 10 | 201 | CARACTER | Tipo de Documento |
| CODCOLCFO | 5 | 211 | INTEIRO | Coligada do Cliente Fornecedor |
| CODCFO | 25 | 216 | CARACTER | Código do Cliente Fornecedor |
| QTDEDOCCANCELADOS | 10 | 241 | INTEIRO | Quantidade de Documentos Cancelados |

Informações do Item de Redução Z:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tamanho** | **Posição Inicial** | **Tipo** | **Descrição** |
| *Marca de Início* | 1 | 1 | CARACTER | Identificação da Linha (Valor fixo "T") |
| TRIBUTACAOECF | 10 | 2 | CARACTER | Código Tributação |
| TOTALPARCIAL | 20 | 12 | VALOR | Totalizador Parcial |

Informações do Cupom Fiscal:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tamanho** | **Posição Inicial** | **Tipo** | **Descrição** |
| *Marca de Início* | 1 | 1 | CARACTER | Identificação da Linha (Valor fixo "C") |
| CODCOLIGADA | 5 | 2 | INTEIRO | Código da Coligada |
| PONTOVENDA | 10 | 7 | CARACTER | Ponto de Venda |
| CRO | 5 | 17 | INTEIRO | Contador de Reinício de Operação |
| NUMERO | 10 | 22 | INTEIRO | Número do Cupom |
| COO | 10 | 32 | INTEIRO | Contador de Ordem de Operação |
| DATAEMISSAO | 10 | 42 | DATA | Data de Emissão |
| HORARIO | 10 | 52 | DATA | Horário de Emissão |
| CODCOLCFO | 5 | 62 | INTEIRO | Coligada do Cliente/Fornecedor |
| CODCFO | 25 | 67 | CARACTER | Cliente/Fornecedor |
| VALORLIQUIDO | 20 | 92 | VALOR | Valor do Cupom |
| DESCONTO | 20 | 112 | VALOR | Desconto do Cupom |
| ACRESCIMO | 20 | 132 | VALOR | Acréscimo do Cupom |
| VALORRECEBIDO | 20 | 152 | VALOR | Valor Recebido |
| CAIXA | 10 | 172 | INTEIRO | Número do Caixa |
| NUMEROREDUCAO | 10 | 182 | INTEIRO | Número da Redução |
| CANCELADO | 5 | 192 | INTEIRO | Eh cupom cancelado? |
| CNPJCPFADQUIRENTE | 20 | 197 | CARACTER | CNPJ/CPF do Adquirente |
| NOMEADQUIRENTE | 40 | 217 | CARACTER | Nome do Adquirente |

Informações de Item de Cupom Fiscal:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tamanho** | **Posição Inicial** | **Tipo** | **Descrição** |
| *Marca de Início* | 1 | 1 | CARACTER | Identificação da Linha (Valor fixo "I") |
| NUMEROITEM | 10 | 2 | INTEIRO | Número do Item de Cupom Fiscal |
| CODIGOPRD | 30 | 12 | CARACTER | Código do Produto |
| QUANTIDADE | 20 | 42 | VALOR | Quantidade |
| PRECOUNITARIO | 20 | 62 | VALOR | Preço Unitário |
| VALORBRUTO | 20 | 82 | VALOR | Valor Bruto do Item de Cupom |
| DESCONTO | 20 | 102 | VALOR | Desconto do Item de Cupom |
| ACRESCIMO | 20 | 122 | VALOR | Acréscimo do Item de Cupom |
| RATEIODESCONTO | 20 | 142 | VALOR | Rateio do Desconto do Cupom |
| RATEIOACRESCIMO | 20 | 162 | VALOR | Rateio do Acréscimo do Cupom |
| VALORLIQUIDO | 20 | 182 | VALOR | Valor do Item de Cupom |
| CANCELAMENTO | 20 | 202 | VALOR | Valor do Cancelamento do Item de Cupom |
| TRIBUTACAOECF | 10 | 222 | CARACTER | Código de Tributação ECF |
| CODNAT | 20 | 232 | CARACTER | Natureza |
| ALIQUOTA | 20 | 252 | VALOR | Alíquota do Tributo |
| CST | 3 | 272 | CARACTER | Código Situação Tributária |
| CANCELADO | 5 | 275 | INTEIRO | Eh item de cupom cancelado? |
| CODUND | 5 | 280 | CARACTER | Código da Unidade de Venda |

Informações de Pagamento do Cupom Fiscal:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tamanho** | **Posição Inicial** | **Tipo** | **Descrição** |
| *Marca de Início* | 1 | 1 | CARACTER | Identificação da Linha (Valor fixo "P") |
| NUMEROPARCELA | 10 | 2 | INTEIRO | Número do Pagamento |
| DEBITOCREDITO | 1 | 12 | CARACTER | Débito / Crédito |
| CODCPG | 5 | 13 | CARACTER | Condição de Pagamento |
| VALOR | 20 | 18 | VALOR | Valor do Pagamento |
| DATAVENCIMENTO | 10 | 38 | DATA | Data de Vencimento |
| CODFORMAPAGTO | 10 | 48 | CARACTER | Forma de Pagamento |
| BANCO | 4 | 58 | CARACTER | Banco |
| AGENCIA | 20 | 62 | CARACTER | Agência |
| CC | 20 | 82 | CARACTER | Conta/Corrente |
| CHEQUE | 20 | 102 | CARACTER | Número do Cheque |
| CODCOLCXA | 5 | 122 | INTEIRO | Coligada da Conta Caixa |
| CODCXA | 10 | 127 | CARACTER | Conta Caixa |
| CAMPO LIVRE | 10 | 137 | CARACTER | Campo Livre |
| NOMEEMITENTE | 30 | 147 | CARACTER | Nome do Emitente do Cheque |
| TELEMITENTE | 15 | 177 | CARACTER | Telefone do Emitente |

Informações de Relacionamento Item de Cupom x Item de Movimento:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tamanho** | **Posição Inicial** | **Tipo** | **Descrição** |
| *Marca de Início* | 1 | 1 | CARACTER | Identificação da Linha (Valor fixo "J") |
| SERIE | 8 | 2 | CARACTER | Série |
| NUMEROMOV | 35 | 10 | CARACTER | Número do Movimento |
| CODFILIAL | 10 | 45 | INTEIRO | Filial |
| CODTDO | 10 | 55 | CARACTER | Documento |
| CRO | 5 | 65 | INTEIRO | Contador de Reinício de Operação |
| NUMEROSEQUENCIAL | 10 | 70 | INTEIRO | Sequencial do Item de Movimento |

### **Layout 3:**

Informações da Redução Z:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tamanho** | **Posição Inicial** | **Tipo** | **Descrição** |
| *Marca de Início* | 1 | 1 | CARACTER | Identificação da Linha (Valor fixo "R") |
| CODCOLIGADA | 5 | 2 | INTEIRO | Código da Coligada |
| PONTOVENDA | 10 | 7 | CARACTER | Ponto de Venda |
| NUMEROREDUCAO | 10 | 17 | INTEIRO | Número da Redução |
| DATAMOVIMENTO | 10 | 27 | DATA | Data de Movimento |
| DATAREDUCAO | 10 | 37 | DATA | Data de Redução |
| GRANDETOTAL | 20 | 47 | VALOR | Grande Total |
| CANCELAMENTOS | 20 | 67 | VALOR | Cancelamentos |
| DESCONTOS | 20 | 87 | VALOR | Descontos |
| ACRESCIMOS | 20 | 107 | VALOR | Acréscimos |
| ACRESCIMOSFIN | 20 | 127 | VALOR | Acréscimos Financeiros |
| COO | 10 | 147 | CARACTER | Ordem de Operação |
| CNSI | 10 | 157 | CARACTER | Contador Não Sujeito ICMS |
| GRANDETOTALANT | 20 | 167 | VALOR | Grande Total Anterior |
| COOANT | 10 | 187 | INTEIRO | Ordem Operação Anterior |
| SERIE | 4 | 197 | CARACTER | Série |
| CODTDO | 10 | 201 | CARACTER | Tipo de Documento |
| CODCOLCFO | 5 | 211 | INTEIRO | Coligada do Cliente Fornecedor |
| CODCFO | 25 | 216 | CARACTER | Código do Cliente Fornecedor |
| QTDEDOCCANCELADOS | 10 | 241 | INTEIRO | Quantidade de Documentos Cancelados |

Informações do Item de Redução Z:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tamanho** | **Posição Inicial** | **Tipo** | **Descrição** |
| *Marca de Início* | 1 | 1 | CARACTER | Identificação da Linha (Valor fixo "T") |
| TRIBUTACAOECF | 10 | 2 | CARACTER | Código Tributação |
| TOTALPARCIAL | 20 | 12 | VALOR | Totalizador Parcial |

Informações do Cupom Fiscal:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tamanho** | **Posição Inicial** | **Tipo** | **Descrição** |
| *Marca de Início* | 1 | 1 | CARACTER | Identificação da Linha (Valor fixo "C") |
| CODCOLIGADA | 5 | 2 | INTEIRO | Código da Coligada |
| PONTOVENDA | 10 | 7 | CARACTER | Ponto de Venda |
| CRO | 5 | 17 | INTEIRO | Contador de Reinício de Operação |
| NUMERO | 10 | 22 | INTEIRO | Número do Cupom |
| COO | 10 | 32 | INTEIRO | Contador de Ordem de Operação |
| DATAEMISSAO | 10 | 42 | DATA | Data de Emissão |
| HORARIO | 10 | 52 | DATA | Horário de Emissão |
| CODCOLCFO | 5 | 62 | INTEIRO | Coligada do Cliente/Fornecedor |
| CODCFO | 25 | 67 | CARACTER | Cliente/Fornecedor |
| VALORLIQUIDO | 20 | 92 | VALOR | Valor do Cupom |
| DESCONTO | 20 | 112 | VALOR | Desconto do Cupom |
| ACRESCIMO | 20 | 132 | VALOR | Acréscimo do Cupom |
| VALORRECEBIDO | 20 | 152 | VALOR | Valor Recebido |
| CAIXA | 10 | 172 | INTEIRO | Número do Caixa |
| NUMEROREDUCAO | 10 | 182 | INTEIRO | Número da Redução |
| CANCELADO | 5 | 192 | INTEIRO | Eh cupom cancelado? |
| CNPJCPFADQUIRENTE | 20 | 197 | CARACTER | CNPJ/CPF do Adquirente |
| NOMEADQUIRENTE | 40 | 217 | CARACTER | Nome do Adquirente |

Informações de Item de Cupom Fiscal:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tamanho** | **Posição Inicial** | **Tipo** | **Descrição** |
| *Marca de Início* | 1 | 1 | CARACTER | Identificação da Linha (Valor fixo "I") |
| NUMEROITEM | 10 | 2 | INTEIRO | Número do Item de Cupom Fiscal |
| CODIGOPRD | 30 | 12 | CARACTER | Código do Produto |
| QUANTIDADE | 20 | 42 | VALOR | Quantidade |
| PRECOUNITARIO | 20 | 62 | VALOR | Preço Unitário |
| VALORBRUTO | 20 | 82 | VALOR | Valor Bruto do Item de Cupom |
| DESCONTO | 20 | 102 | VALOR | Desconto do Item de Cupom |
| ACRESCIMO | 20 | 122 | VALOR | Acréscimo do Item de Cupom |
| RATEIODESCONTO | 20 | 142 | VALOR | Rateio do Desconto do Cupom |
| RATEIOACRESCIMO | 20 | 162 | VALOR | Rateio do Acréscimo do Cupom |
| VALORLIQUIDO | 20 | 182 | VALOR | Valor do Item de Cupom |
| CANCELAMENTO | 20 | 202 | VALOR | Valor do Cancelamento do Item de Cupom |
| TRIBUTACAOECF | 10 | 222 | CARACTER | Código de Tributação ECF |
| CODNAT | 20 | 232 | CARACTER | Natureza |
| ALIQUOTA | 20 | 252 | VALOR | Alíquota do Tributo |
| CST | 3 | 272 | CARACTER | Código Situação Tributária |
| CANCELADO | 5 | 275 | INTEIRO | Eh item de cupom cancelado? |
| CODUND | 5 | 280 | CARACTER | Código da Unidade de Venda |

Informações de Pagamento do Cupom Fiscal:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tamanho** | **Posição Inicial** | **Tipo** | **Descrição** |
| *Marca de Início* | 1 | 1 | CARACTER | Identificação da Linha (Valor fixo "P") |
| NUMEROPARCELA | 10 | 2 | INTEIRO | Número do Pagamento |
| DEBITOCREDITO | 1 | 12 | CARACTER | Débito / Crédito |
| CODCPG | 5 | 13 | CARACTER | Condição de Pagamento |
| VALOR | 20 | 18 | VALOR | Valor do Pagamento |
| DATAVENCIMENTO | 10 | 38 | DATA | Data de Vencimento |
| CODFORMAPAGTO | 10 | 48 | CARACTER | Forma de Pagamento |
| BANCO | 4 | 58 | CARACTER | Banco |
| AGENCIA | 20 | 62 | CARACTER | Agência |
| CC | 20 | 82 | CARACTER | Conta/Corrente |
| CHEQUE | 20 | 102 | CARACTER | Número do Cheque |
| CODCOLCXA | 5 | 122 | INTEIRO | Coligada da Conta Caixa |
| CODCXA | 10 | 127 | CARACTER | Conta Caixa |
| CAMPO LIVRE | 10 | 137 | CARACTER | Campo Livre |
| NOMEEMITENTE | 30 | 147 | CARACTER | Nome do Emitente do Cheque |
| TELEMITENTE | 15 | 177 | CARACTER | Telefone do Emitente |

Informações de Relacionamento Item de Cupom x Item de Movimento:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tamanho** | **Posição Inicial** | **Tipo** | **Descrição** |
| *Marca de Início* | 1 | 1 | CARACTER | Identificação da Linha (Valor fixo "J") |
| SERIE | 8 | 2 | CARACTER | Série |
| NUMEROMOV | 35 | 10 | CARACTER | Número do Movimento |
| CODFILIAL | 10 | 45 | INTEIRO | Filial |
| CODTDO | 10 | 55 | CARACTER | Documento |
| CRO | 5 | 65 | INTEIRO | Contador de Reinício de Operação |
| NUMEROSEQUENCIAL | 10 | 70 | INTEIRO | Sequencial do Item de Movimento |

**Importação de Automação Comercial**

Para realizar a importação, será utilizado a ferramenta Conceito, que compõe o TOTVS Business Conector (TBC). Este Conceito tem como Objetivo incluir os dados da Redução Z e Cupom Fiscal de acordo com os dados contidos no arquivo de importação informado dentro do Conceito.

Neste caso o arquivo para importação deve ter o mesmo layout apresentado nas tabelas acima, podendo ser gerado manualmente ou pela exportação do arquivo através do Gerador de Saídas.

Na geração do conceito o usuário poderá informar os seguintes parâmetros:

 - **Cliente\Fornecedor identificado por CPF/CNPJ:** Para buscar o código do cliente através do CPF/CNPJ informado no campo CODCFO.

**Tabelas Utilizadas**

* TREDUCAOZ: Redução Z
* TREDUCAOZITEM: Item de Redução Z
* TCUPOMFISCAL: Cupom Fiscal
* TCUPOMFISCALITM: Itens de Cupom Fiscal
* TCUPOMFISCALFIN: Pagamentos do Cupom Fiscal.
* TCUPOMFISCALRELAC: Item de Cupom x Item de Movimento

## Procedimento para Implantação

**Exportação de Automação Comercial**

Para realizar a exportação de automação comercial utiliza-se o **Gerador de Saídas**.

Neste caso deve-se primeiro importar o Layout de Exportação disponibilizado na pasta de Objetos Gerenciais, localizada no diretório de instalação do totvs (\CorporeRM\ObjetosGerenciais).

* Acesse o **Gerador de Saídas**, no módulo **Integrações**, e navegue para a aba **Integrações | Gerador de Saídas | Layouts**.
* Na visão da tela do Gerador de Saídas, selecione a opção **Processos | Importar Layout**. Selecione o arquivo de layout disponível na pasta de objetos gerenciais e informe um nome e a categoria para a importação.

**Importação de Automação Comercial**

Para realizar a importação de automação comercial, é necessário importar o layout de importação através da ferramenta **Conceito**, que compõe o **TOTVS Business Conector** (TBC).

Neste caso deve-se primeiro importar o layout de importação disponibilizado na pasta de Objetos Gerenciais, localizada no diretório de instalação do totvs (\CorporeRM\ObjetosGerenciais).

* Acesse o **Conceito**, no módulo **Integrações**, e navegue para a aba **Integrações | Conceito**.
* Na visão da tela do Conceito, selecione a opção **Processos | Importar de Conceito**. Selecione o arquivo de conceito disponível na pasta de objetos gerenciais e informe o nome para a importação.

## Procedimento para Utilização

**Exportação de Automação Comercial**

1. Acesse o **Gerador de Saídas**, no módulo **Integrações**, e navegue para a aba **Integrações | Gerador de Saídas | Layouts**.
2. Na visão da tela do Gerador de Saídas, selecione o layout na visão e execute o processo em **Processos | Geração de Saídas**
3. Após a conclusão do processo o arquivo com os dados selecionados estará disponível em: C:\totvs\CorporeRM\RM.Net\Saídas (Caso o sistema esteja instalado na pasta default do sistema).

**Importação de Automação Comercial**

1. Acesse o **Conceito**, no módulo **Integrações**, e navegue para a aba **Integrações | Conceito**.
2. Na visão da tela do Conceito, selecione o conceito na visão e execute o processo em **Processos | Processar novo conceito**selecionando o arquivodesejado no mesmo formato do layout de exportação.
3. Após a conclusão do processo os registros de Cupom Fiscal e Redução Z informados no arquivo de importação estarão atualizados no sistema.
