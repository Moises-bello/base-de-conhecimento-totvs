---
content_hash: 685f9e559d372a158d889e39bcf2070ae5abd1bd7ad764d440224d82299033e0
fetched_at: '2026-06-29T00:11:37.048920+00:00'
page_id: '776127842'
product: rm
source: tdn-rm
title: Funções de Fórmula para o Processamento da Contabilização por Competência do
  Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=776127842
version: 13
---

Na  do contrato, os  são utilizados para mapear e determinar as regras da contabilização dos processos da empresa. Podem ser configurados para utilização de fórmulas para calcular o valor a ser contabilizado.

Com o objetivo de auxiliar no processo da contabilização teve a criação das fórmulas BuscaCampoContrato, BuscaCampoContratoCont, BuscaCampoContratoServico, BuscaCampoContratoServicoCont, BuscaCampoContratoBolsa, BuscaCampoContratoBolsaCont, BuscaCampoParcelaCont, BuscaCampoParcelaServicoCont, BuscaCampoParcelaBolsaCont para retornar as informações que são contabilizadas no contrato do aluno. A seguir temos as descrições das fórmulas.

Funções para a contabilização do contrato do aluno

As funções de fórmula a seguir poderão ser utilizadas para retornar o conteúdo de um determinado campo processado na contabilização do contrato do aluno.

Todas as funções a seguir devem conter um contexto para ser processadas. Nesse contexto deve conter os campos **CodColigada, CodContrato, IdPerLet, RA** do contrato do aluno.

As funções  BuscaCampoContratoCont, BuscaCampoContratoServico, BuscaCampoContratoServicoCont, BuscaCampoContratoBolsa e BuscaCampoContratoBolsaCont são compatíveis apenas com o modelo de contabilização que [Registra separadamente contabilizações de cancelamento e aumento](https://tdn.totvs.com/x/M-9bGQ). Caso não esteja sendo utilizado este modelo, para provisões de contrato, deverá ser utilizada a fórmula BuscaCampoContrato.    

| Nome | Descrição | Parâmetros | Exemplo |
| --- | --- | --- | --- |
| BUSCACAMPOCONTRATO | Tem como objetivo retornar o conteúdo de um determinado campo do contrato do aluno (tabela: SCONTRATO). | * **Nome do campo**. * **Tipo**: Tipo do valor do campo informado.   + **"V"**: Valor   + **"I"**: Inteiro   + **"D"**: Data   + **"S"**: Texto | BUSCACAMPOCONTRATO('VALORSERVICO','V') |
| BUSCACAMPOCONTRATOCONT | Tem como objetivo retornar o conteúdo de um determinado campo da contabilização do contrato do aluno (tabela: SCONTRATOCONT). | * **Nome do campo**. * **Tipo**: Tipo do valor do campo informado.   + **"V"**: Valor   + **"I"**: Inteiro   + **"D"**: Data   + **"S"**: Texto | BUSCACAMPOCONTRATOCONT('VALORSERVICO','V') |
| BUSCACAMPOCONTRATOSERVICO | Tem como objetivo retornar o conteúdo de um determinado campo do serviço presente na contabilização do contrato do aluno (tabela: SCONTRATOSERVICO). | * **Nome do campo**. * **Tipo**: Tipo do valor do campo informado.   + **"V"**: Valor   + **"I"**: Inteiro   + **"D"**: Data   + **"S"**: Texto | BUSCACAMPOCONTRATOSERVICO('VALOR','V') |
| BUSCACAMPOCONTRATOSERVICOCONT | Tem como objetivo retornar o conteúdo de um determinado campo da contabilização do serviço presente no contrato do aluno (tabela: SCONTRATOSERVICOCONT).   O contexto para essa fórmula deverá ter a tabela SContratoServicoCont e os campos CodContrato, IdPerLet  e Ra da tabela SContratoCont. Desta forma, o editor de fórmula identificará qual contrato pertencerá a contabilização do serviço. | * **Nome do campo**. * **Tipo**: Tipo do valor do campo informado.   + **"V"**: Valor   + **"I"**: Inteiro   + **"D"**: Data   + **"S"**: Texto | BUSCACAMPOCONTRATOSERVICOCONT('VALOR','V') |
| BUSCACAMPOCONTRATOBOLSA | Tem como objetivo retornar o conteúdo de um determinado campo da bolsa presente na contabilização do contrato do aluno (tabela: SCONTRATOBOLSA). | * **Nome do campo**. * **Tipo**: Tipo do valor do campo informado.   + **"V"**: Valor   + **"I"**: Inteiro   + **"D"**: Data   + **"S"**: Texto | BUSCACAMPOCONTRATOBOLSA('VALOR','V') |
| BUSCACAMPOCONTRATOBOLSACONT | Tem como objetivo retornar o conteúdo de um determinado campo da contabilização da bolsa presente no contrato do aluno (tabela: SCONTRATOBOLSACONT).   O contexto para essa fórmula deverá ter a tabela SContratoBolsaCont e os campos CodContrato, IdPerLet  e Ra da tabela SContratoCont. Desta forma, o editor de fórmula identificará qual contrato pertencerá a contabilização da bolsa. | * **Nome do campo**. * **Tipo**: Tipo do valor do campo informado.   + **"V"**: Valor   + **"I"**: Inteiro   + **"D"**: Data   + **"S"**: Texto | BUSCACAMPOCONTRATOBOLSACONT('VALOR','V') |

Funções para a contabilização das parcelas no contrato do aluno

As funções de fórmula a seguir poderão ser utilizadas para retornar o conteúdo de um determinado campo processado na contabilização da parcela no contrato do aluno.

Todas as funções a seguir devem conter um contexto para ser processadas. Nesse contexto deve conter os campo **CodColigada, CodContrato, IdPerLet, RA** do contrato do aluno.

As funções BuscaCampoParcelaCont, BuscaCampoParcelaServicoCont, BuscaCampoParcelaBolsaCont são compatíveis apenas com o modelo de contabilização que [Registra separadamente contabilizações de cancelamento e aumento](https://tdn.totvs.com/x/M-9bGQ). 

| Nome | Descrição | Parâmetros | Exemplo |
| --- | --- | --- | --- |
| BUSCACAMPOPARCELACONT | Tem como objetivo retornar o conteúdo de um determinado campo da contabilização da parcela do contrato do aluno (tabela: SPARCELACONT). | * **Nome do campo**. * **Tipo**: Tipo do valor do campo informado.   + **"V"**: Valor   + **"I"**: Inteiro   + **"D"**: Data   + **"S"**: Texto | BUSCACAMPOPARCELACONT('VALORSERVICO','V') |
| BUSCACAMPOPARCELASERVICOCONT | Tem como objetivo retornar o conteúdo de um determinado campo da contabilização do serviço presente na parcela do contrato do aluno (tabela: SPARCELASERVICOCONT).   O contexto para essa fórmula deverá ter a tabela SParcelaServicoCont e os campos CodContrato, IdPerLet  e Ra da tabela SParcelaCont. Desta forma, o editor de fórmula identificará qual contrato pertencerá a contabilização do serviço da parcela. | * **Nome do campo**. * **Tipo**: Tipo do valor do campo informado.   + **"V"**: Valor   + **"I"**: Inteiro   + **"D"**: Data   + **"S"**: Texto | BUSCACAMPOPARCELASERVICOCONT('VALOR','V') |
| BUSCACAMPOPARCELABOLSACONT | Tem como objetivo retornar o conteúdo de um determinado campo da contabilização da bolsa aplicada na parcela do contrato do aluno (tabela: SPARCELABOLSACONT).   O contexto para essa fórmula deverá ter a tabela SParcelaBolsaCont e os campos CodContrato, IdPerLet  e Ra da tabela SParcelaCont. Desta forma, o editor de fórmula identificará qual contrato pertencerá a contabilização da bolsa que foi aplicada na parcela. | * **Nome do campo**. * **Tipo**: Tipo do valor do campo informado.   + **"V"**: Valor   + **"I"**: Inteiro   + **"D"**: Data   + **"S"**: Texto | BUSCACAMPOPARCELABOLSACONT('VALOR','V') |
