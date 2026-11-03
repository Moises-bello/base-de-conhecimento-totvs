---
content_hash: 5ef0e35efde0d249b314740a4e19362e7f5c70e3c8f97a085a2f0a2c0f002575
fetched_at: '2026-06-29T00:10:38.847837+00:00'
page_id: '545249943'
product: rm
source: tdn-rm
title: MP 927 - Pagamento de 1/3 de Férias na Rescisão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=545249943
version: 16
---

Conforme a MP 927, Art. 10, na hipótese de dispensa do empregado, o empregador pagará, juntamente com o pagamento dos haveres rescisórios, os valores ainda não adimplidos relativos às férias.

Quando as férias são antecipadas ao finalizar as mesmas o período é fechado e é aberto um novo período aquisitivo. O cálculo das verbas rescisórias verifica somente o período aquisitivo de férias aberto para calcular as férias proporcionais e/ou indenizadas.

Para atender a MP, orientamos fazer o lançamento do evento calculado por fórmula na rescisão se os mesmos forem devidos, usando uma das opções: Entrada de movimento, Grupo de eventos, Código Fixos, Eventos Programados, Incluir no Envelope de Pagamento, Importação de Movimento ou inserir nos Eventos Adicionais no parametrizador.

Considerando o cenário, onde o funcionário teve as férias de 2020 e 2021 concedidas, sem o pagamento de 1/3 de férias. No período vencido, o funcionário tinha 20 dias de direto. O mesmo foi concedido em Março/2020 com pagamento em abril/2020:

Após a finalização das férias concedidas acima foi criado um novo período aquisitivo de férias entre 01/08/2019 a 31/07/2020. Este período foi antecipado concedendo ao empregado 30 dias de férias, com pagamento para 06/05/2020 sem o pagamento do 1/3 de férias.

Ao finalizar as férias concedidas acima, foi criado um novo período aquisitivo de férias entre31/07/2020 a 31/07/2021:

Em Maio/2020 o funcionário foi demitido. O produto não irá calcular nenhuma verba de férias para o funcionário, pois o período aberto inicia em Agosto/2020.

Abaixo exemplificaremos fórmulas para calcular o adicional de férias devido.

**Fórmula para adicional de férias antecipado que deve ser pago de forma proporcional**

Passo 1: 

Criar a consulta SQL para retornar os funcionários que tiveram as férias concedidas antecipadas. Nesta consulta é retornado somente os funcionários com o período antecipado e o evento de base de Cálculo que tem o ⅓ de férias lançado, conforme orientado no documento 

sqlConsulta SQL- Pagamento de 1/3 de Férias Proporcionais

Passo 2:

Criar a fórmula abaixo que retorna os dados da consulta SQL criada no passo 1, que é referente ao valor de ⅓ de férias do período antecipado e que a data final do período aquisitivo é maior que a data de demissão:

Fórmula - Pagamento 1/3 Férias Proporcionais CHAPA
ENTAO
0
SENAO
SE FIMPERAQUIS1 > DTD E ( DATAPGTOFERIAS >= MTDATA(22,03,2020) E DATAPGTOFERIAS <= MTDATA(22,07,2020))
ENTAO
VALOREVENTO]]>

Executando a fórmula a mesma retornou o valor do evento de Base de Cálculo B099 lançado na Ficha Financeira do pagamento de férias antecipadas:

PASSO 3:

Criar um evento de provento e associar a fórmula neste provento:

**Fórmula para adicional de férias antecipado que deve ser pago de forma indenizadas**

Passo 1: 

Criar a consulta SQL para retornar os funcionários que tiveram as férias concedidas antecipadas. Nesta consulta é retornado somente os funcionários com o período vencido e o evento de base de Cálculo que tem o ⅓ de férias lançado, conforme orientado no documento 

sqlConsulta SQL - Pagamento de 1/3 de Férias Vencidas FIMPERAQUIS AND PFFINANC.CODEVENTO = 'B099']]>

 Passo 2:

Criar a fórmula abaixo que retorna os dados da consulta SQL criada no passo 1, que é referente ao valor de ⅓ de férias do período vencido e que a data final do período aquisitivo é menor que a data de demissão, não ultrapassando 2 períodos vencidos:

Fórmula - Pagamento de 1/3 de Férias Vencido CHAPA
ENTAO
0
SENAO
SE (DATAINICIOFERIAS > FIMPERAQUIS1 OU FIMPERAQUIS1 > DTD) E ( DATAPGTOFERIAS >= MTDATA(10,03,2020) E DATAPGTOFERIAS <= MTDATA(22,07,2020))
ENTAO
VALOREVENTO
]]>

Executando a fórmula a mesma retornou o valor do evento de Base de Cálculo B099 lançado na Ficha Financeira do pagamento de férias Vencidas:

PASSO 3:

Criar um evento de provento e associar a fórmula neste provento:

Quando executar o cálculo da rescisão inserindo o evento em algumas daquelas entradas sugeridas, os eventos serão lançados:

**eSocial**

O eSocial não divulgou nenhuma orientação com relação a alteração de rubricas até o momento. A orientação que foi passada é com relação do Tipo de pagamento para as férias conforme abaixo:

*"A Medida Provisória 927/2020 autoriza o pagamento de férias até o quinto dia útil do mês seguinte ao seu gozo e o pagamento do terço de férias e do abono pecuniário até o dia 20/12/2020. Portanto, como não é mais exigido que o valor de férias seja antecipado ao trabalhador, as rubricas de férias podem, opcionalmente, ser inseridas no S-1200 e o {ideDmDev} desse demonstrativo ser referido no evento S-1210, com {tpPgto} = [1], sem que seja necessário o envio de um S-1210 com {tpPgto} = [7] (recibo de antecipação de pagamento de férias)."*
