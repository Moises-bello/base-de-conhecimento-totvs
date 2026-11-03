---
content_hash: 182150113877219ae57ce0cf5f8b499133afc2aec702df4a9601ed2c8b247930
fetched_at: '2026-06-29T00:10:07.838833+00:00'
page_id: '452719449'
product: rm
source: tdn-rm
title: De/Para de Endereço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719449
version: 2
---

Para gerar a informação das tags no arquivo "S-2200 - Evento Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador":

* paisNascto - código do país de nascimento do trabalhador, conforme tabela de países da RFB
* paisNacionalidade - código do país de nacionalidade do trabalhador, conforme tabela de países da RFB

Os passos abaixo devem ser executados:  
    
 Cadastrar no módulo de BackOffice / Gestão Fiscal /Cadastros / Globais / Mais / Endereço:

* Classificação de Tipo de Rua
* Classificação de País
* Classificação de Município

Cadastrar o código do País conforme RFB no módulo de BackOffice / Gestão Fiscal /Cadastros / Globais / Mais:

* Países – Anexo Codificação de Pais
* Municípios – Anexo Codificação de Municípios
* Endereço / Tipo de Rua – Anexo Codificação de Tipo de Rua

Cadastrar no parametrizador do módulo RH / Folha de Pagamento:

* Conceito de Classificação para Tipo de Rua (De/Para) = que deve ser o código cadastrado em Classificação de Tipo de Rua
* Conceito de Classificação para Códigos de Município = que deve ser o código cadastrado em Classificação de Município
* Conceito de Classificação para Códigos de Países = que deve ser o código cadastrado em Classificação de País

As nacionalidades utilizadas nos cadastros de funcionários devem ser associadas ao código de País equivalente. Essa associação funciona a partir da seleção de uma nacionalidade e de um país, ambos em campos correspondentes.   
    
 Existe o País cadastrado no módulo de Gestão Fiscal e este País deve ser associado com o cadastro de Nacionalidade do módulo de Folha de Pagamento. No cadastro de Nacionalidade no módulo de Folha de Pagamento existe uma coluna que deve ter o código correspondente do módulo de Gestão Fiscal, este código será informado através da Associação da Nação com o País.  
    
 A cada seleção, clicar no botão "Associar". Repita as seleções a cada associação realizada. Realize esse procedimento apenas para as nacionalidades utilizadas nos cadastros de funcionários.  
    
 Todos os passos acima devem ser executados para a correta parametrização do módulo de Folha de Pagamento na geração no eSocial com informações de País, Município e Rua.

|  |  |
| --- | --- |
|  | Informações Complementares |

[eSocial](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452718787)
