---
content_hash: d6f62b7ada6c621473d6bcea17db7b9836b54de6233109c352a12d0755375418
fetched_at: '2026-06-29T00:11:56.485870+00:00'
page_id: '866529609'
product: rm
source: tdn-rm
title: Encargos - Base de INSS e Base de INSS 13º conforme DCTFWeb
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=866529609
version: 13
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

O TOTVS Folha de Pagamento possui encargos que retornam a Base de INSS parte empresa separados os valores que contemplam o Cálculo da Folha atual e dissídio. Além disso não consideram o histórico de percentual de INSS e percentual redutor para empresas que possuem o beneficio da desoneração da Folha. Caso o usuário queira contemplar em uma base única os valores de Folha mensal e dissídio e aplicar o percentual cadastrado no histórico conforme é feito pela DCTFWeb, o mesmo deve fazer por fórmula.

Foram criados dois novos encargos para retornar a Base de INSS conforme a DCTFWeb:

* + Encargo tipo **T**:  Base INSS DCTFWeb
  + Encargo tipo **U**: Base INSS 13º Salário DCTFWeb

A base será composta com o eventos lançados na Ficha Financeira do colaborador referente ao pagamento mensal + os eventos de dissídio lançados na PFVERBASDIS e PFVERBASDISFER. Logo, será o retorno das bases dos encargo serão:

* + Encargo tipo T: Tipo 3 - Base: incidência de INSS + Tipo R - Base: incidência de INSS Dissídio
  + Encargo tipo U: Tipo H - Base: incidência de INSS de 13º salário + Tipo S - Base: incidência de INSS de 13º salário Dissídio

Além disto, para estes novos encargos foi disponibilizado a opção para considerar o Histórico de Percentual para INSS da Seção e percentual de Redução cadastrado no Período de Apuração do eSocial.

## **02. EXEMPLO DE UTILIZAÇÃO**

Encargos - Informando Porcentagem

Os encargos criados permitem informar o percentual, conforme abaixo:

 

Gerando o encargo, será aplicado na base retornada o percentual de 28,80%:

Encargos - Parâmetro 'Considerar Históricos de percentuais de INSS'

**Habilita Histórico de INSS no Cadastro de Seção**

O parâmetro 'Considerar históricos de percentuais de INSS' só será exibido nos cadastros de encargos do Tipo T e U e só será permitido marcar o mesmo caso o Parâmetro 'Habilita histórico de INSS no cadastro de Seção' estiver marcado em Parametrizador | Folha Normal | Encargos Sociais

Quando o campo 'Considerar históricos de percentuais de INSS' estiver marcado, irá considerar os percentuais para Empresa, Acidente de trabalho e Terceiros conforme cadastrado em Seções | Anexo | Histórico de Percentuais para INSS da seção centralizadora, com vigência na competência informada no processo de geração do encargo:

Quando o parâmetro 'Considerar históricos de percentuais de INSS' estiver marcado, o campo Porcentagem ficará desabilitado, conforme abaixo:

 

Gerando os encargos, cada percentual será aplicado na base retornada e somado. A logica utilizada será:

* Encargo = ((base INSS) \* % empresa / 100)+ ((base INSS) \* % (FAP \* SAT) / 100) + ((base INSS) \* % Terceiros / 100):
* Encargo = ((base de INSS 13º) \* % empresa / 100)+ ((base de INSS 13º) \* % (FAP \* SAT) / 100) + ((base INSS) \* % Terceiros / 100

Aplicando os percentuais do cadastro acima, o cálculo do encargo ficará conforme abaixo. Quando o parâmetro estiver marcado no cadastro de encargos, será informado no log:

**Utiliza Quebra de FPAS**

Quando a base está parametrizada para utilizar Quebra de FPAS, será considerando o histórico de percentuais para INSS conforme a quebra informada em Parametrizador | eSocial | Configurações Gerais | Lotação Tributária.

Caso não tenha configuração de percentual na seção conforme a quebra FPAS, será considerado a seção centralizadora do Colaborador. No cenário abaixo temos dois colaboradores, um lotado na seção 01.01 e outro na seção 01.02:

Temos a informação de percentuais na seção 01.02. Na geração de encargo, para o funcionário chapa 00002 será considerado os percentuais abaixo:

Porém não temos a informação de percentuais na 01.01. Na geração do encargo, para o funcionário 00007 será considerado os percentuais da centralizadora 01:

**Descriminar Percentual de Terceiros**

Quando este parâmetro estiver marcado, será calculado o percentual de terceiros considerando cada percentual informado no anexo do histórico de percentuais para INSS:

Na seção 01.02 temos 2 registros de percentuais:

Gerando os encargos, além dos percentuais Empresa e Acidente de trabalho, cada percentual de terceiros será aplicado na base retornada e somado. A logica utilizada será quando existir mais de 1 registro de terceiro:

* Encargo = ((base INSS) \* % empresa / 100)+ ((base INSS) \* % (FAP \* SAT) / 100) + ((base INSS) \* % Terceiros\_1 / 100)+ ((base INSS) \* % Terceiros\_2 / 100)
* Encargo = ((base de INSS 13º) \* % empresa / 100)+ ((base de INSS 13º) \* % (FAP \* SAT) / 100) + ((base de INSS 13º) \* % Terceiros\_1 / 100)+ ((base de INSS 13º) \* % Terceiros\_2 / 100)

**Alíquota FAP**

Para alíquota FAP será considerado o valor encontrado no cadastro disponível em Seção | Anexos | FAP por estabelecimento Empresarial da seção centralizadora, que esteja dentro da vigência da competência informada no processo de Geração dos Encargos. Caso não encontre cadastro dentro da vigência, será buscado o valor da tabela de valores fixos. Se também não encontrar registro dentro da vigência, será retornado zero:

FAP por estabelecimento Empresarial

FAP cadastrado dentro da vigência:

Na geração de encargos, considerou este valor para aplicar na alíquota do acidente de trabalho:

Tabela de valores Fixos

No cenário abaixo o registro do FAP por estabelecimento está fora da vigência e na tabela de valores fixos, o valor fixo com a finalidade alíquota FAP está vigente e com valor = 1,00

 

Foi considerado o valor da tabela de valores fixos:

FAP por estabelecimento Empresarial e Tabela de Valores fixos fora da Vigência

No cenário abaixo não existe alíquota FAP dentro da vigência da Geração do Encargo:

 

Neste caso retornou zero para a alíquota FAP:

Atenção

Para os encargos do tipo T e U o parâmetro 'Aplicar percentual FAP por filial' sempre ficará desabilitado. A utilização da alíquota FAP só será aplicada quando o parâmetro 'Considerar os históricos de percentuais de INSS' estiver marcado, dentro das regras exemplificada acima.

Encargos - Parâmetro 'Considerar Percentual Redução (Lei 12.546/2011)

O parâmetro 'Considerar Percentual de Redução (Lei 12.546/2011)' só será exibido nos cadastros de encargos do Tipo T e U e só será permitido marcar o mesmo caso no cadastro de Informações do Empregador em eSocial | Cadastros, o indicativo de desoneração da Folha seja **1 - Empresa enquadrada nos critérios da legislação vigente** ou **2 - Município enquadrado nos critérios da legislação vigente**.

No cadastro de Encargos, o campo abaixo fica habilitado para o usuário:

O percentual de redução será retornado o valor do campo 'Percentual de Redução (Lei 12.546/2011)' do cadastro de Período de apuração do eSocial da competência da geração. No caso do 13º Salário, só será verificado o Indicativo de período apuração como anual na competência 12:

 

Gerando os encargos considerando histórico de percentuais de INSS na competência 12/2022. A logica utilizada será:

* Encargo = ((base INSS) \* % empresa / 100)\*  %redução /100+ ((base INSS) \* % (FAP \* SAT) / 100) + ((base INSS) \* % Terceiros / 100)
* Encargo = ((base de INSS 13º) \* % empresa / 100)\*  %redução /100+ ((base de INSS 13º) \* % (FAP \* SAT) / 100) + ((base de INSS 13º) \* % Terceiros / 100

Repare que o percentual de redução só será aplicado na parte empresa:

 

Gerando usando porcentagem informada no cadastro na competência 12/2022. A logica utilizada será:

* Encargo = ((base INSS) \* % encargo / 100)\*  %redução /100
* Encargo = ((base de INSS 13º) \* % encargo / 100)\*  %redução /100

 

Gerando os encargos considerando histórico de percentuais de INSS na competência 06/2022. Neste caso, como na competência 06 não existe o período de apuração anual, para o  encargo U - Base INSS 13º Salário DCTFWeb, será considerado o mesmo percentual de redução do período de apuração mensal:

Gerando os encargos, em ambos considerou o percentual de redução de 5%:

 

Quando não é informado o indicativo, retorna mensagem e o mesmo não é considerado para o cálculo, não zerando o recolhimento da parte empresa do encargo.

Gerando o encargo para competência 12/2022, para o encargo T foi considerado o percentual de 3,5, para o encargo U não foi considerado nenhum percentual de redução. É retornada mensagem no log:

 

## **03. TABELAS UTILIZADAS**

PENCARGO

PFENCARGO

PPARAMADICIONAIS

PESOCIALEMPREGADOR

PESOCIALFOLHAMENSAL

PVALFIX

PSECAO

PSECAOFAPESTABELECIMENTO

PSECAOFAPALIQUOTA

PSECAODADOSINSS

PSECAODADOSINSSPERCENT

## **04. DEMAIS INFORMAÇÕES**

* [Histórico de Percentuais para INSS](https://tdn.totvs.com.br/pages/viewpage.action?pageId=496388652)
* [Quebra de FPAS na mesma filial](https://tdn.totvs.com.br/pages/viewpage.action?pageId=842272518)
* [Período de Apuração eSocial](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719936)
* [Informações do empregador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718306)
* [FAP por Estabelecimento Empresarial](https://tdn.totvs.com.br/display/LRM/TTIDF1_DT_FAP_Estabelecimento_Empresarial)
