---
content_hash: cce55abc6596e9acc4e6509f6707f7dd071beba53cf84e13473f8623d0aeac65
fetched_at: '2026-06-29T00:10:01.539919+00:00'
page_id: '452718768'
product: rm
source: tdn-rm
title: Sugestão de Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718768
version: 6
---

**Sugestão de Férias**

**Início Per. Aquis.**Neste campo retorna a data início do período aquisitivo aberto. Caso o funcionário não tenha mais saldo no período aquisitivo aberto, será retornado o do próximo período.

**Fim Per. Aquis.**Neste campo retorna a data Fim do período aquisitivo aberto. Caso o funcionário não tenha mais saldo no período aquisitivo aberto, será retornado o do próximo período.

**Dias a Marcar**O campo "Dias a Marcar" se refere à quantidade de dias restantes para cadastrar sugestões de férias baseado no saldo do período aquisitivo. "Dias a Marcar" é diferente do "Saldo" exibido na marcação de férias pelo RM. Enquanto "Saldo" é calculado baseando-se na quantidade de avos que o funcionário tem na competência atual, "Dias a Marcar" irá considerar 30 dias para um novo período aquisitivo, sendo descontado a quantidade de dias de sugestões de férias já marcadas naquele período.

**Exemplo**

Período aquisitivo 20/09/2018 a 19/09/2019 - O período ainda não venceu.

No portal vai retornar 30 no campo 'Dias a Marcar'

Atenção

Este comportamento é diferente da interface de Marcação Férias de MDI pois no portal só é permitido marcar férias após o vencimento do período aquisitivo, então é retornado os 30 dias de direito, que é a quantidade que o funcionário terá de direito quando as férias vencerem.

Se o funcionário já tiver algum período de gozo dentro do período Aquisitivo aberto com dias menor que o saldo de direito, este campo retorna a quantidade restante.

**Exemplo**

Período aquisitivo: 01/01/2018 a 31/12/2018

Período de gozo: 02/01/2019 a 11/01/2019 - 10 dias

Quando o funcionário for solicitar um próximo período de gozo, o campo Dias a Marcar retornará 20

**Limite para Início de Gozo**  
Retorna a data Limite que o Funcionário tem que iniciar as suas férias. Caso seja informado uma data posterior a esta, é retornado uma mensagem para o funcionário informando que ultrapassou a data limite, não concluindo o cadastro.

**Observação**Como é feita esta validação de data limite, através do portal não é permitido que seja cadastro férias que podem refletir na dobra, mesmo que o dia atual já tenha ultrapassado esta data.

**Exemplo**Data Limite 01/04/2019

Início do período de gozo ou fim do período de gozo 02/04/2019

É retornado uma mensagem para o funcionário informando que o período de gozo ultrapassou o limite para início de férias.

**Data Início**  
Este campo o funcionário informa a data de início das férias. Ao salvar o sistema valida se esta data ultrapassa o limite para início de gozo, não podendo ser posterior a esta data e, a data Fim do período aquisitivo, sendo que a mesma deve ser posterior a esta data. Também é validado o parâmetro no Parametrizador | RM - Portal | Férias , campo "Nº dias de antecedência para alterações', onde o início de gozo deve ser acrescentado a quantidade de dias da data atual.

**Exemplo**Nº de dias de antecedência para a alterações: 30

Hoje é dia 01/01/2019

Data Início deve ser a partir do dia 31/01/2019

**Dias de Férias**  
Neste campo o funcionário deve informar a quantidade de dias de férias, não podendo o mesmo ser maior que 30. Também é validado o campo 'Nº máximo de dias de férias p/ férias partidas',no no Parametrizador | RM - Portal | Férias II, caso seja permitido cadastrar férias partidas. Neste caso a quantidade de dias não pode ser menor que a informada neste campo.

**Data Fim**  
Este campo o funcionário informa a data de fim das férias. Ao salvar o sistema valida se esta data ultrapassa o limite para início de gozo, não podendo ser posterior a esta data.

**Dias de Abono**

Neste campo o funcionário deverá informar a quantidade de dias de abono de férias caso deseje. Os dias de abono de férias serão somados ao dias de férias que o funcionário tem direito.

**Exemplo**Nº de dias de abono: 10

Nº de dias de férias: 20

Será considerado que o funcionário gozou no período aquisitivo 30 dias de férias.

**Observação 1:**

Este campo somente estará disponível para preenchimento, caso o parâmetro 'Permite cadastrar abono pecuniário', disponível em  RH|Folha de Pagamento| Configurações | Parametrizador |  RM Portal | Férias II, esteja marcado.

**Observação 2:**

A validação do mínimo de dias permitidos para férias partidas passa a considerar somente os dias de férias , quando o parâmetro 'Ativar alterações da Reforma Trabalhista de acordo com a Lei Nº13.467 de 13 de Julho de 2017' estiver marcado. Quando o parâmetro estiver desmarcado os dias de férias será somando aos dias de abono.

**Pagar 1ª Parcela do 13º**   
Durante o processo de marcação de férias para um funcionário, é possível marcar a flag "Pagar 1ª Parcela do 13º" e ela só poderá ser marcada uma vez durante o período aquisitivo. Caso a flag seja marcada em uma segunda sugestão de férias no mesmo período aquisitivo, o sistema irá emitir a mensagem "A 1ª parcela de 13º salário já foi solicitada em outro Período de Gozo."

**Filtro de usuário e perfil na Sugestão de Férias**

O envio de e-mail para os gestores (chefes/supervisor/Externo), além de observar as regras já existentes de chefe e subordinados, passou a filtrar os gestores do subordinado, aplicando o filtro de usuário e de perfil vinculado ao usuário e perfil dos gestores.
