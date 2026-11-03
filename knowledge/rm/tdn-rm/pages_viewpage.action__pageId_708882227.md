---
content_hash: 608387be71ca390c56e278b21cbcbac4c94982650fabc9fca3953c1601a084b5
fetched_at: '2026-06-29T00:11:25.433256+00:00'
page_id: '708882227'
product: rm
source: tdn-rm
title: Conversão de unidades de medidas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=708882227
version: 27
---

falseConversãotrueÚnica unidade medida

## **01. Contexto**

Nesse exemplo será mostrada a configuração necessária no RM para um item controlado, prescrito e faturado com a mesma unidade de medida.

Esse é o exemplo mais comum e iremos focar apenas nas configurações necessárias para a conversão de unidade de medida.

Utilizaremos a unidade CO ( Comprimido ) para exemplificar o contexto.

## **02. Cadastro da unidade de medida**

A unidade base do RM é UN ( unidade ), nesse exemplo não será necessário nenhuma conversão entre unidade, logo iremos apenas associar a unidade CO com a unidade base.

Acesso: Cadastros > Estoque > Cadastros de estoque > Unidades de medida / fatores

## **03. Cadastros do produto**

No cadastro de produto será necessário definir a unidade de controle com a unidade definida no item anterior, no caso a unidade CO

Acesso: Cadastros > Estoque > Produto

Na tabela de preço associada ao atendimento é necessário definir a unidade de faturamento para o lançamento em conta,

o volume de faturamento nesse contexto também não terá nenhum regra, pois, a unidade é a mesma de controle, logo não heverá necessidade de conversão.

Acesso: Cadastros > Estoque > Produto > Informações TOTVS Saúde > Tabela de Preço

Associação da unidade de medida ao produto para a prescrição

Acesso: Cadastros > Estoque > Produto > Informações TOTVS Saúde > Unidade de dosagem

## **04. Prescrição**

Uma ilustração da prescrição do item no PEP RM onde é selecionada a unidade associada ao produto, nesse

caso serão lançados 2 comprimidos para cada horário de acordo a frequência selecionada.

## **05. Painel de dispensação**

No painel serão confirmados e processados os itens pela unidade de controle, porém o lançamento em conta é realizado conforme configuração da tabela de preço.

Acesso: Farmácia > Gestão da farmácia > Painel de dispensação

**05.1 Item solicitado**

Essa imagem exibe o item conforme prescrito

**05.2 Item confirmado**

**05.3 Item processado**

## **06. Lançamento em conta**

Após o processamento o item deve ser lançado em conta com a unidade definida na tabela de preço

Acesso: Faturamento > Particular e Convênios > Elaboração de contas

Várias unidades de medida

## **01. Contexto**

Nesse exemplo será mostrada a configuração necessária no RM para um item controlado em frasco de 20ML,

prescrito em GT (gotas) ou ML (Mililitro) e faturado em ML. Esse exemplo é mais complexo e precisa de configurações para

que o RM possa converter as unidades, iremos focar apenas nas configurações necessárias para a conversão de unidade de medida.

Utilizaremos as unidades FR20 ( Frasco 20 ML), GT (Gotas) e ML (Mililitro).

## **02. Cadastro das unidades de medida**

**02.1 Cadastro da unidade ML**

Acesso: Cadastros > Estoque > Cadastros de estoque > Unidades de medida / fatores

A unidade base do RM é UN ( unidade ), nesse exemplo iremos associar a unidade ML com a unidade base.

**02.2 Cadastro da unidade FR20**

Acesso: Cadastros > Estoque > Cadastros de estoque > Unidades de medida / fatores

Cada frasco do medicamento possui o equivalente a 20ML, logo será necessário realizar o cadastro com o fator de conversão que represente o volume do frasco, 1 frasco / 20 ML.

## **03. Cadastros do produto**

**03.1 Cadastro de estoque**

Acesso: Cadastros > Estoque > Produto

No cadastro de produto será necessário definir a unidade de controle com a unidade definida no item anterior, no caso a unidade FR20

**03.2 Cadastro Informações TOTVS - Saúde**

Acesso: Cadastros > Estoque > Produto > Informações TOTVS Saúde 

No cadastro do produto no contexto da saúde devemos informar a quantidade de gotas/ml e o volume em ml da apresentação do medicamento.

O RM envia para o backoffice a quantidade multiplicada pelo fator de conversão, porém em alguns casos o resultado desse

cálculo pode ser uma fração do item de acordo com sua unidade de medida de controle, ou seja, não será o equivalente a 1 item no controle de estoque.

Para que ao enviar para o estoque e dar baixa seja realizada a baixa equivalente a 1 item é necessário configurar o parâmetro

(Arredondamento na quantidade enviada para o backoffice) conforme imagem abaixo, do contrário será dispensado o valor fracionado. 

Ex.: 1 item que possui um volume de 20ML e 10 gotas é o equivalente a 1ML, quando solicitado 20 gotas serão dispensadas apenas 2 ML, ou seja, 10% do item. 

      20 gotas = 2 ML

      Fator de conversão 1 / 20 = 0,05

      Cálculo dose: 2 \* 0,05 = 0,1

Com o parâmetro desabilitado será baixado 0,1 item de estoque e com o parâmetro habilitado será baixado 1 item de estoque

Nos parâmetros de integração com o backoffice ainda temos um parâmetro ( Envia a quantidade na unidade de controle para o backoffice )

que define qual a unidade de medida que é enviada ao backoffice para sua movimentação, no caso exemplificado se o parâmetro não estiver

habilitado o RM Saúde enviará a unidade de medida do faturamento, ou seja, mililitro (ML).

**03.3 Cadastro Tabela de Preço**

Acesso: Cadastros > Estoque > Produto > Informações TOTVS Saúde > Tabela de Preço

Na tabela de preço associada ao atendimento é necessário definir a unidade de faturamento para o lançamento em conta, o volume de faturamento nesse contexto também precisa ser representado com o fator de conversão para aplicar a devida regra, pois, a unidade de controle, prescrição e faturamento são diferentes.

Caso o produto seja faturado por unidade diferente em outra tabela é necessário apenas alterar a tabela de preço, as demais configurações para que o cálculo seja realizado são as mesmas.

**03.4 Cadastro Unidades de dosagem**

Acesso: Cadastros > Estoque > Produto > Informações TOTVS Saúde > Unidade de dosagem

Associação da unidade de medida ao produto para a prescrição

Unidades sendo exibidas no PEP RM

**03.4.1 Equivalência de dosagem**

Se cadastrada a Equivalência de dosagem o RM Saúde usará essa informação para converter a unidade prescrita para a unidade de controle e quando necessária a unidade de faturamento irá aplicar o fator de conversão cadastrada na tabela de preço do convênio.

A partir da versão 2602

Disponível na versão 2602

## **04. Padrão de concentração / Padrão de Prescrição**

Acesso: Cadastros > Cuidados com o paciente > Prescrição Médica > Padrão de concentração

Cadastros > Cuidados com o paciente > Prescrição Médica > Padrão de prescrição

É necessário criar um padrão de concentração que represente o medicamento e esse padrão deve ser associado ao padrão de prescrição juntamente com o medicamento

## **05. Prescrição**

No PEP poderemos prescrever por 4 unidades de medidas devidamente configuradas, a de controle (FR20),

gotas (GT) que possui relação com a ML, de faturamento (ML) e miligramas (MG).

**05.1 Prescrição em frasco**

Abaixo temos a imagem da prescrição do item no PEP RM onde é selecionada a unidade associada ao produto,

nesse caso será lançado 1 frasco 20ML para cada horário de acordo a frequência selecionada, deverá ser dispensado 1 frasco de 20ML (FR20) e cobrado 20 ML.

**05.2 Prescrição em gotas**

Abaixo temos a imagem da prescrição do item no PEP RM onde é selecionada a unidade associada ao produto,

nesse caso serão lançadas 20 gotas para cada horário de acordo a frequência selecionada, deverá ser dispensado 1 frasco de 20ML (FR20) e cobrado 2 ML.

**05.3 Prescrição em mililitros**

Abaixo temos a imagem da prescrição do item no PEP RM onde é selecionada a unidade associada ao produto,

nesse caso serão lançadas 10 ML para cada horário de acordo a frequência selecionada, deverá ser dispensado 1 frasco de 20ML (FR20) e cobrado 10 ML.

**05.4 Prescrição em mililgramas**

Abaixo temos a imagem da prescrição do item no PEP RM onde é selecionada a unidade associada ao produto,

nesse caso serão lançadas 250 MG para cada horário de acordo a frequência selecionada, deverá ser dispensado 1 frasco de 20ML (FR20) e cobrado 5 ML.

## **05. Painel de dispensação**

Acesso: Farmácia > Gestão da farmácia > Painel de dispensação

No painel serão confirmados e processados os itens pela unidade de controle (FR20), porém o lançamento em conta é realizado conforme

configuração da tabela de preço (ML).

## **06. Lançamento em conta**

Acesso: Faturamento > Particular e Convênios > Elaboração de contas

Após o processamento o item deve ser lançado em conta com a unidade definida na tabela de preço (ML).

Abaixo podemos ver na imagem os 3 lançamentos em conta para cada prescrição realizada.

## **07. Movimento de estoque ( RM Nucleus)**

Acesso: Cadastros > Estoque > Produto >Movimentações do produto

Na seguinte imagem podemos ver as movimentações realizadas e suas quantidades como afetaram o estoque,

conforme configurado sempre vamos baixar 1 unidade de controle, pois, utilizamos o parâmetro para arredonda a quantidade enviada ao estoque.

Caso estivesse configurado no acumulado teríamos baixado 47 ML., similar ao lançamento em conta.

Duas unidades de medida

## **01. Contexto**

Nesse exemplo será mostrada a configuração necessária no RM para um item controlado em comprimido de 500MG,

prescrito em MG (miligrama) ou CO (comprimido) e faturado em MG.

Esse exemplo precisa de configurações para que o RM possa converter as unidades,

iremos focar apenas nas configurações necessárias para a conversão de unidade de medida. Utilizaremos as unidades CO ( Comprimido de 500MG) e MG (miligrama).

## **02. Cadastro das unidades de medida**

Acesso: Cadastros > Estoque > Cadastros de estoque > Unidades de medida / fatores

**02.1 Cadastro da unidade ML**

A unidade base do RM é UN ( unidade ), nesse exemplo iremos associar a unidade CO e a unidade base UN com o fator de conversão igual a 500.

**02.2 Cadastro da unidade MG**

Cada comprimido possui o equivalente a 500MG, logo será necessário associar o cadasto de miligrama com a unidade base associada ao cadastro do comprimido.

## **03. Cadastros do produto**

**03.1 Cadastro de estoque**

Acesso: Cadastros > Estoque > Produto

No cadastro de produto será necessário definir a unidade de controle com a unidade CO

**03.2 Cadastro Informações TOTVS - Saúde**

Acesso: Cadastros > Estoque > Produto > Informações TOTVS Saúde 

O RM envia para o backoffice a quantidade multiplicada pelo fator de conversão, porém em alguns casos o resultado desse

cálculo pode ser uma fração do item de acordo com sua unidade de medida de controle, ou seja, não será o equivalente a 1 item no controle de estoque.

Para que ao enviar para o estoque e dar baixa seja realizada a baixa equivalente a 1 item é necessário configurar o parâmetro

(Arredondamento na quantidade enviada para o backoffice) conforme imagem abaixo, do contrário será dispensado o valor fracionado. 

Ex.: 1 item que possui um volume de 500MG equivalente a 1CO, quando solicitado 100MG serão dispensadas apenas 0,2 CO, ou seja, 20% do item. 

      50 MG = 0,1 CO

      Fator de conversão 1 / 500 = 0,002

      Cálculo dose: 100 \* 0,002 = 0,2

Com o parâmetro desabilitado será baixado 0,2 item de estoque e com o parâmetro habilitado será baixado 1 item de estoque

Nos parâmetros de integração com o backoffice ainda temos um parâmetro ( Envia a quantidade na unidade de controle para o backoffice )

que define qual a unidade de medida que é enviada ao backoffice para sua movimentação, no caso exemplificado se o parâmetro não estiver habilitado o

RM Saúde enviará a unidade de medida do faturamento, ou seja, mililitro (MG).

**03.3 Cadastro Tabela de Preço**

Acesso: Cadastros > Estoque > Produto > Informações TOTVS Saúde > Tabela de Preço

Na tabela de preço associada ao atendimento é necessário definir a unidade de faturamento para o lançamento em conta,

o volume de faturamento nesse contexto também precisa ser representado com o fator de conversão para aplicar a devida regra, pois,

a unidade de controle, prescrição e faturamento são diferentes.

**03.4 Cadastro Unidades de dosagem**

Acesso: Cadastros > Estoque > Produto > Informações TOTVS Saúde > Unidade de dosagem

Associação da unidade de medida ao produto para a prescrição

Unidades sendo exibidas no PEP RM

## **04. Padrão de concentração / Padrão de Prescrição**

Acesso: Cadastros > Cuidados com o paciente > Prescrição Médica > Padrão de concentração

Cadastros > Cuidados com o paciente > Prescrição Médica > Padrão de prescrição

É necessário criar um padrão de concentração que represente o medicamento e esse padrão deve ser associado ao padrão de prescrição juntamente com o medicamento

## **05. Prescrição**

No PEP poderemos prescrever por 2 unidades de medidas devidamente configuradas, a de controle (CO) e faturamento (MG).

**05.1 Prescrição em comprimido**

Abaixo temos a imagem da prescrição do item no PEP RM onde é selecionada a unidade associada ao produto,

nesse caso será lançado 1 comprimido para cada horário de acordo a frequência selecionada, deverá ser dispensado 1 comprimido (CO) e cobrado 500 MG.

**05.2 Prescrição em miligrama**

Abaixo temos a imagem da prescrição do item no PEP RM onde é selecionada a unidade associada ao produto,

nesse caso serão lançadas 500 miligramas para cada horário de acordo a frequência selecionada, deverá ser dispensado 1 comprimido (CO) e cobrado 500 MG.

## **05. Painel de dispensação**

Acesso: Farmácia > Gestão da farmácia > Painel de dispensação

No painel serão confirmados e processados os itens pela unidade de controle (CO), porém o lançamento em conta é realizado conforme configuração da tabela de preço (MG).

## **06. Lançamento em conta**

Acesso: Faturamento > Particular e Convênios > Elaboração de contas

Após o processamento o item deve ser lançado em conta com a unidade definida na tabela de preço (MG).

Abaixo podemos ver na imagem os 2 lançamentos em conta para cada prescrição realizada.

## **07. Movimento de estoque ( RM Nucleus)**

Acesso: Cadastros > Estoque > Produto >Movimentações do produto

Na seguinte imagem podemos ver as movimentações realizadas e suas quantidades como afetaram o estoque,

conforme configurado sempre vamos baixar 1 unidade de controle, pois, utilizamos o parâmetro para arredonda a quantidade enviada ao estoque.
