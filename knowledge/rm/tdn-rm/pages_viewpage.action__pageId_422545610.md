---
content_hash: 34f9082b56db642cc834a4db690978290bce41b4b8829f0b7c5fce78673cf240
fetched_at: '2026-06-29T00:09:19.553488+00:00'
page_id: '422545610'
product: rm
source: tdn-rm
title: GIA (RS)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545610
version: 15
---

São obrigados a apresentar a Guia de Informação e Apuração do ICMS (GIA) os contribuintes classificados no CGC/TE na categoria Geral referente a cada um dos estabelecimentos. Os contribuintes de que trata o capítulo X, 1.3.1, alíneas “a” e “b” e 1.3.2 da IN 45/98 com tratamento especial no CGC/TE, e as Prefeituras inscritas no CGC/TE com a finalidade exclusiva de ter acesso a informações disponibilizadas pela Secretaria da Fazenda na Internet, ficam dispensados da apresentação da GIA

**Anexo I**  
 Serão listadas as operações de entrada, exceto importação. Estas operações serão informadas totalizando por CFOP nível sintético.

****Anexo**II**  
 Discriminação dos créditos recebidos por transferência: será preenchido conforme os lançamentos de Outros Créditos com o Tipo "Crédito" e Subtipo "Recebimento de Crédito". Será totalizado por CGC/TE Origem e Código.  
 **CGC/TE Origem**: Se a Referência informada no Lançamento de Outros Créditos for um Documento Fiscal cadastrado, receberá a Inscrição Estadual do participante do Documento Fiscal. Se a Referência informada for um Documento Fiscal NÃO cadastrado, receberá a Inscrição Estadual informada na referência;

**Código**: Se a Referência informada no Lançamento de Outros Créditos for um Documento Fiscal cadastrado, será preenchido conforme o campo Classificação CFOP, localizado na pasta Outros Dados do Cadastro de Naturezas Fiscais. Se a Referência informada for um Documento Fiscal NÃO cadastrado, será preenchido conforme o campo "Motivo Referência".

****Anexo**V**  
Discriminação das saídas: serão totalizadas por CFOP, nível sintético, todas as operações de saída.  
  
****Anexos**VA e VB**  
 Nas operações informadas no Anexo V, existindo valor em Isento de ICMS, o sistema gera um Anexo VA. Existindo valor em Outros de ICMS, o sistema gera um Anexo VB.  
 Os campos Código Isentas e Código Outras serão preenchidos conforme o campo Classificação CFOP, localizado no Cadastro de Naturezas de Operação.

**Anexo VI**  
 Discriminação dos créditos transferidos: será preenchido conforme os lançamentos de Outros Débitos com o Tipo "Débito" e Subtipo "Transferência de Crédito". Será totalizado por CGC/TE Origem e Código.  
 **CGC/TE Origem**: Se a Referência informada no Lançamento de Outros Débitos for um Documento Fiscal cadastrado, receberá a Inscrição Estadual do participante do Documento Fiscal. Se a Referência informada for um Documento Fiscal NÃO cadastrado, receberá a Inscrição Estadual informada na referência;

**Código**: Se a Referência informada no Lançamento de Outros Débitos for um Documento Fiscal cadastrado, será preenchido conforme o campo Classificação CFOP, localizado na pasta Outros Dados do Cadastro de Naturezas Fiscais. Se a Referência informada for um Documento Fiscal NÃO cadastrado, será preenchido conforme o campo "Motivo Referência".

****Anexo**VII**  
 Refere-se às operações com Substituição Tributária.   
 CR ENTRADAS rf. ST.: somatório do Valor ST das operações de Entrada. Gera o Anexo VIIa.  
 DB SAÍDAS rf. ST.: somatório do Valor ST das operações de Saída. Gera o Anexo VIIb.  
 Outros Créditos e Outros Débitos: total de lançamentos de Outros Débitos e Créditos dos tipos: Crédito, Estorno de Débito, Débito e Estorno de Crédito, cujo tributo associado é do tipo ICMS ST. O histórico associado a estes campos preenche os campos Texto Outros Créditos e Texto Outros Débitos.

****Anexos**VIIa e VIIb**  
 Base de Cálculo: valor da base de cálculo ST.  
 Crédito/Débito: valor ST das operações de Entrada/Saída.

****Anexo**VIII**  
 Refere-se às guias GNR/GNRE cujo vencimento encontra-se dentro do período selecionado na tela da rotina.  
 ICMS Próprio: 0 (zero).  
 ICMS ST: valor pago na guia.

****Anexo**X**  
 Refere-se às guias Normais e GNR/GNRE cujo vencimento encontra-se fora do período selecionado na tela da rotina.  
 **ICMS Próprio**: valor da guia normal ou 0 (zero), no caso de guias GNR/GNRE.

**ICMS ST**: 0 (zero), no caso de guia normal, ou o valor pago da guia GNR/GNRE cujo vencimento encontra-se fora do período selecionado na tela da rotina.

****Anexo**XI**  
Detalhamento de Entradas/Saídas por UF nas operações interestaduais.

****Anexo**XII**  
Detalhamento de Entradas/Saídas por País nas operações de importação e exportação.  
 Código do País: é buscado do anexo "Codificação de Pais", caso contrário, é buscado do próprio cadastro de País na pasta Identificação.

****Anexo**XVI**  
 Serão selecionados que atendam a seleção abaixo:

* A Natureza (campo "CODNAT" tabela "DNATUREZA") deverá ser igual a 5.414, 5.415, 5.904, 1.414, 1.415 ou 1.904 que correspondem à Vendas Fora do Estabelecimento;
* Natureza tem que ser do tipo Fiscal;
* Lançamentos que não tenham sejam Notas Fiscais que acobertam Cupom Fiscal (campo "ESCRITURADOMANUAL" da tabela "DLAF" diferente de "1" ou esteja nulo.
