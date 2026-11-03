---
content_hash: 6579840b8d968d435b57e5ce5bed779610b4a03b2a89be903d29e2cae19933f9
fetched_at: '2026-06-29T00:11:36.853637+00:00'
page_id: '773518737'
product: rm
source: tdn-rm
title: TCGI - Comissão - Fórmulas da Comissão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=773518737
version: 16
---

SALDOCOMISSIONADO

| COMISSAOMETAQTD  \*Versão 12.1.2310 | Retorna a quantidade de todas as vendas no mês da comissão. Primeiro argumento o tipo de cálculo da meta da comissão nome do campo Legenda: (0 = Todas as Coligadas; 1 = Coligada da Comissão; 2 = Empreendimento da Comissão; 3 = Meta da Comissão) |
| --- | --- |
| **CONTEXTO** | Usa como contexto a chave da tabela "XCOMISSOESITEM". |
| **SINTAXE** | COMISSAOMETAQTD(TipoComissaoCalculoMeta) |

Importante!

Para acessar todas as funções de fórmula do TCGI:

| TABCOMISSOES | Retorna o valor de um campo da tabela de comissão. | Primeiro argumento nome do campo. Segundo argumento tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora) |
| --- | --- |
| **CONTEXTO** | Usa como contexto a chave da tabela "XCOMISSOES". |
| **SINTAXE** | TABCOMISSOES('CampoReferencia','TipoDeRetorno') |

| TABCOMISSOESCOMPL | Retorna o valor de um campo da tabela de campos complementares da comissão da venda. Primeiro argumento nome do campo. Segundo argumento tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora) |
| --- | --- |
| **CONTEXTO** | Usa como contexto a chave da tabela "XCOMISSOES". |
| **SINTAXE** | TABCOMISSOESCOMPL('CampoReferencia','TipoDeRetorno') |

| TABCOMISSOESITEM | Retorna o valor de um campo da tabela de item da comissão. Primeiro argumento nome do campo. Segundo argumento tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora) |
| --- | --- |
| **CONTEXTO** | Usa como contexto a chave da tabela "XCOMISSOES". |
| **SINTAXE** | TABCOMISSOESITEM('CampoReferencia','TipoDeRetorno') |

| TABCOMISSOESITENS | Retorna o valor de um campo da tabela de item da comissão a partir do código da função. Primeiro argumento código da Função. Segundo argumento nome do campo. Terceiro argumento tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora) |
| --- | --- |
| **CONTEXTO** | Usa como contexto a chave da tabela "XCOMISSOES". |
| **SINTAXE** | TABCOMISSOESITENS(CodigoFuncao,'CampoReferencia','TipoDeRetorno') |

| TABCOMISSOESITEMPARCELA | Retorna o valor de um campo da tabela de parcela do item da comissão. Primeiro argumento nome do campo. Segundo argumento tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora) |
| --- | --- |
| **CONTEXTO** | Usa como contexto a chave da tabela "XCOMISSOES". |
| **SINTAXE** | TABCOMISSOESITEMPARCELA('CampoReferencia','TipoDeRetorno') |

| VALORTOTALCOMISSAO | Retorna o valor total da comissão (Soma os itens da comissão) |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XCOMISSOES" |
| **SINTAXE** | VALORTOTALCOMISSAO |

| VALORSALDOCOMISSAO | Retorna o valor do saldo da comissão (Soma os itens da comissão) |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XCOMISSOES" |
| **SINTAXE** | VALORSALDOCOMISSAO |

| PERCENTUALTOTALCOMISSAO | Retorna o valor total do percentual da comissão (Soma os itens da comissão) |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XCOMISSOES" |
| **SINTAXE** | PERCENTUALTOTALCOMISSAO |

| QTDECOMISSIOANDOSCOMISSAO | Retorna a quantidade de comissionados da comissão (Soma os itens da comissão) |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XCOMISSOES" |
| **SINTAXE** | QTDECOMISSIOANDOSCOMISSAO |

| QTDECOMISSIOANDOSCOMISSAOFUNCAO | Retorna a quantidade de comissionados da comissão (Soma os itens da comissão) por função |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XCOMISSOES" |
| **SINTAXE** | QTDECOMISSIOANDOSCOMISSAOFUNCAO(Código da função) |

| PERCENTUALCOMISSIONADO | Retorna o percentual do comissionado (empresa + cliente) da comissão |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XCOMISSOESITEM" COM JOIN "XCOMISSOES" |
| **SINTAXE** | PERCENTUALCOMISSIONADO |

| VALORCOMISSIONADO | Retorna o valor do comissionado (empresa + cliente) da comissão |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XCOMISSOESITEM" COM JOIN "XCOMISSOES" |
| **SINTAXE** | VALORCOMISSIONADO |

| **SALDOCOMISSIONADO** | Retorna o saldo que falta gerar das parcelas do comissionado (empresa + cliente) da comissão  \*12.12310 |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XCOMISSOESITEM" COM JOIN "XCOMISSOES" |
| **SINTAXE** | SALDOCOMISSIONADO |

| COMISSAOMETAVALOR  \*Versão 12.1.2310 | Retorna o valor de todas as vendas no mês da comissão. Primeiro argumento o tipo de cálculo da meta da comissão nome do campo Legenda: (0 = Todas as Coligadas; 1 = Coligada da Comissão; 2 = Empreendimento da Comissão; 4 = Meta da Comissão) |
| --- | --- |
| **CONTEXTO** | Usa como contexto a chave da tabela "XCOMISSOESITEM". |
| **SINTAXE** | COMISSAOMETAVALOR(TipoComissaoCalculoMeta) |

| COMISSAOMETAQTD  \*Versão 12.1.2310 | Retorna a quantidade de todas as vendas no mês da comissão. Primeiro argumento o tipo de cálculo da meta da comissão nome do campo Legenda: (0 = Todas as Coligadas; 1 = Coligada da Comissão; 2 = Empreendimento da Comissão; 3 = Meta da Comissão) |
| --- | --- |
| **CONTEXTO** | Usa como contexto a chave da tabela "XCOMISSOESITEM". |
| **SINTAXE** | COMISSAOMETAQTD(TipoComissaoCalculoMeta) |

| COMISSAOMETAEMPRVALOR  \*Versão 12.1.2310 | Retorna o valor de todas as vendas no mês da comissão para o empreendimento filtrado. Primeiro argumento o código do empreendimento que deseja filtrar as vendas. |
| --- | --- |
| **CONTEXTO** | Usa como contexto a chave da tabela "XCOMISSOESITEM". |
| **SINTAXE** | COMISSAOMETAEMPRVALOR(CodEmpreendimento) |

| **DATAGERACAOPARCELACOMISSAO**  \*Versão 12.1.2310 | Retorna a data do último dia da geração da parcela na comissão |
| --- | --- |
| **CONTEXTO** | Usa como contexto a chave da tabela "XCOMISSOESITEM". |
| **SINTAXE** | DATAGERACAOPARCELACOMISSAO |

| **EXISTEPARCELACOMISSAODATAGERADA**  \*Versão 12.1.2310 | Retorna se existe parcela gerada na competência pesquisada (1 = Verdadeiro; 0 = Falso) |
| --- | --- |
| **CONTEXTO** | Usa como contexto a chave da tabela "XCOMISSOESITEM". |
| **SINTAXE** | COMISSAOMETAEMPRQTD(Data)   * Data - Data Pesquisada, mas a comparação é somente competência |

| **TOTALPAGOVENDAORIGINAL**  \*Versão 12.1.2310 | Retorna o valor total original baixado da venda |
| --- | --- |
| **CONTEXTO** | Usa como contexto a chave da tabela "XVENDA". |
| **SINTAXE** | TOTALPAGOVENDAORIGINAL |

| VALORVENDACOMPONENTE  \*Versão 12.1.2310 | Retorna o valor total de um componente específico |
| --- | --- |
| **CONTEXTO** | Usa como contexto a chave da tabela "XVENDA". |
| **SINTAXE** | VALORVENDACOMPONENTE |

| SETCOMISSIONADO  \*Versão 12.1.2310 | Define o comissionado no momento da geração da comissão, só pode ser usado nas fórmulas de calcular valor ou percentual do comissionado. Essa função é usada quando um determinada pessoa está vinculada a equipe/imobiliária. |
| --- | --- |
| **CONTEXTO** | Usa como contexto a chave da tabela "XCOMISSOESITEM". |
| **SINTAXE** | SETCOMISSIONADO(codcolCFO, codCFO)   * codcolCFO - Coligada do comissionado a ser trocado na regra * codCFO - Código do comissionado a ser trocado na regra |

| SETCOMISSIONADOFORNECEDOR  \*Versão 12.1.2310 | Define a empresa que o comissionado irá receber no momento da validação da integração da comissão. Essa função é usada quando um determinada pessoa tem um empresa e a gestão da comissão é feita com a pessoa física e o pagamento para a pessoa jurídica. |
| --- | --- |
| **CONTEXTO** | Usa como contexto a chave da tabela "XCOMISSOESITEM". |
| **SINTAXE** | SETCOMISSIONADOFORNECEDOR(codcolCFO, codCFO)   * codcolCFO - Coligada do comissionado a ser trocado na regra * codCFO - Código do comissionado a ser trocado na regra |

| SETCOMISSIONADOMETA  \*Versão 12.1.2310 | Define a a meta que o comissionado irá receber no momento da geração da comissão.  Só pode ser usado nas fórmulas de calcular valor ou percentual do comissionado. Essa função é usada quando um determinada pessoa está vinculada a equipe/imobiliária e deseja troca a meta no momento da geração da comissão |
| --- | --- |
| **CONTEXTO** | Usa como contexto a chave da tabela "XCOMISSOESITEM". |
| **SINTAXE** | SETCOMISSIONADOMETA(idMeta)   * idMeta- Id da Meta |

| SETDELETACOMISSIONADO  \*Versão 12.1.2310 | Apaga a comissão de um comissionado no momento da geração da comissão.  Só pode ser usado nas fórmulas de calcular valor ou percentual do comissionado. Essa função é usada quando um determinada pessoa não terá comissão por uma condição, então apagamos ela no momento da geração da comissão |
| --- | --- |
| **CONTEXTO** | Usa como contexto a chave da tabela "XCOMISSOESITEM". |
| **SINTAXE** | SETDELETACOMISSIONADO |

| TIPORECALULOCOMISSAO  \*Versão 12.1.2310 | Retorna o tipo de recálculo que a comissão está executando: 1 - Para recálculo padrão , 2- Para recálculo por competência |
| --- | --- |
| **CONTEXTO** | Usa como contexto a chave da tabela "XCOMISSOESITEM". |
| **SINTAXE** | TIPORECALULOCOMISSAO |

| TABCOMISSOESITEMCOMPL  \*Versão 12.1.2506 | Retorna o valor de um campo da tabela de campos complementares da comissão da venda. Primeiro argumento nome do campo. Segundo argumento tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora).    TABCOMISSOESITEMCOMPL ( STRING,STRING )    INDEFINIDO |
| --- | --- |
| **CONTEXTO** | Usa como contexto a chave da tabela "Item da Comissão". |
| **SINTAXE** | TABCOMISSOESITEMCOMPL |

Exemplo Fórmula

Neste exemplo, a comissão tem um percentual máximo de 6%, podendo reduzir esse valor se o corretor der mais que 8% de desconto no valor do imóvel.

Valor da tabela de Preço do Imóvel R$ 100.000,00

Valor de Desconto R$ 10.000,00

Percentual de desconto 10%

Desta forma irei reduzir a comissão em 2% = (10% - 8%) que será reduzido do corretor esse valor. A Comissão do corretor é 3% e ele receberá apenas 1%.

Veja a fórmula do Percentual Máximo da Comissão

Baixe a fórmula

Fórmula no correto e a ordem de cálculo dele é 5 para ser o último a calcular e os demais coloquei 1

Veja a fórmula de cálculo de percentual de limite do corretor

Baixe a fórmula
