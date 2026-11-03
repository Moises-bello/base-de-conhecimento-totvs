---
content_hash: 7ef9ef9db78eeb54bd53b5953fd9d7fdfc633a6e087ffac30e858fba416c348f
fetched_at: '2026-06-29T00:10:07.067905+00:00'
page_id: '452719361'
product: rm
source: tdn-rm
title: Alteração Global de Salários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719361
version: 9
---

Neste módulo será possível realizar alteração salarial para um ou mais funcionários, ou ainda para todos de uma única vez.  
Para funcionários que utilizam Salários Compostos o usuário poderá optar por incluir, alterar ou excluir os eventos que compõem a remuneração destes funcionários.  
   
**Executando o processo de alteração salarial**   
Para realizar alteração salarial para funcionários, o usuário deverá acessar: Administração de Pessoal | Alterações Globais | Alterações Cadastrais | Alteração de Salários, selecionar o funcionário desejado, definir a data para alteração, definir o motivo pelo qual o funcionário terá seu salário alterado e definir qual tipo de ação será executada no momento da alteração, avançar etapa.   
   
**Motivo Alteração Salarial**  
Quando a alteração salarial for por "Dissídio" , deverão  ser cadastrados os motivos para realizar a alteração em Configurações | Parametrizador | eSocial | Motivos Alteração Salarial por Dissídio.

Na próxima tela o usuário deverá definir como será o cálculo do novo salário e executar o processo.  
   
**Reajustes de Aumentos Posteriores**  
O parâmetro "Definir competência final para o reajuste de aumentos posteriores", deve ser utilizado quando a empresa já realizou antecipação de parte do dissídio em competência diferente da data base.

**Exemplo:** Data Base da categoria: 01/09/2016  
               Data da Antecipação: 01/10/2016 - Percentual de antecipação 7%  
               Data do Acordo do Dissídio: 01/11/2016 - (Retroativo a 01/09/2016) Percentual do Dissídio: 11%

## Como fazer o aumento:

Devem ser realizadas 2 execuções de rotina:  
   
1° Correção salarial de Set/2016 em 11%  
    Percentual: 11%  
    Data de Mudança: 01/09  
    Competência final para o Reajuste: 09/2016  
   
2° Correção salarial de out/2016 em diante em 3,738317757% (Percentual aplicado sobre 7% que completará 11% de aumento )  
    Percentual: 3,738317757%  
    Data de Mudança: 01/10/2016  
    Competência Final para o Reajuste: (Não precisa Marcar esse parâmetro uma vez que a correção será até a competência atual)

**IMPORTANTE:**

O parâmetro não desconsidera automaticamente os funcionários admitidos após a data do dissídio, ou seja, a alteração salarial é sempre aplicada a esses funcionários. O entendimento é que o reajuste é necessário para garantir o salário atualizado, incluindo o cumprimento do piso salarial estabelecido pelo sindicato. Caso seja desejado excluir esses funcionários da alteração, será necessário utilizar um filtro na seleção de funcionários para excluí-los manualmente.

**Exemplo:**

Data Base da Categoria:         01/09/2016  
Data da Antecipação:             01/10/2016 => Percentual de antecipação 7%  
Data do Acordo do Dissídio:  01/11/2016 => Percentual do Dissídio: 11% (Retroativo a 01/09/2016)

Ao executar a rotina para um funcionário admitido em 01/11/2016, e informando a correção salarial referente a 09/2016 com o percentual de 11%, o sistema aplicará o percentual total de 11%, mesmo com a competência final sendo 10/2016, para garantir o cumprimento do valor mínimo exigido. Isso ocorre para assegurar que o salário do funcionário esteja ajustado ao valor mínimo necessário, conforme o percentual acordado.

* + - Percentual: 11%
    - Data de Mudança: 01/09/2016
    - Competência final para o Reajuste: 10/2016

**Realizando aumento salarial com data retroativa a um aumento**  
   
Para realizar alteração salarial para funcionários, o usuário deverá acessar: Administração de Pessoal | Alterações Globais | Alterações Cadastrais | Alteração de Salários, selecionar o funcionário desejado, definir a data para alteração menor que um aumento já realizado, definir o motivo pelo qual o funcionário terá seu salário alterado e definir qual tipo de ação será executada no momento da alteração, avançar etapa.   
Na próxima tela o usuário deverá definir como será o cálculo do novo salário e executar o processo.  
   
   
**Observação**  
   
Quando o aumento for retroativo, o sistema irá incluir para cada data de mudança posterior o valor ou percentual considerado no aumento.  
Todos os aumentos gerados que existia aumento, com data da mudança posterior, serão incluídos aumentos com o valor real ou percentual sobre o último aumento da data considerando o motivo de ajuste de dissídio informado na parametrização do Folha de Pagamento.  
   
   
**Exemplo de processo**  
Realizar um aumento de 10% com data de mudança 01/01/2012.  
   
Histórico salarial antes do aumento:

|  |  |  |
| --- | --- | --- |
| **Data Mudança** | **Salário** | **Motivo Mudança** |
| 01/01/2012 00:00 | 1.200,00 | 01 |
| 01/03/2012 00:00 | 1.250,00 | 01 |
| 01/03/2013 00:00 | 1.400,00 | 01 |
| 01/03/2013 00:10 | 1.500,00 | 01 |

Histórico Salarial após o aumento de 10% com data 01/01/2012

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Data Mudança** | **Data Processamento** | **Salário** | **Motivo Mudança** | **Desc. Motivo** |
| 01/01/2012 00:00 | 01/03/2013 00:00 | 1.200,00 | 01 | Admissão |
| 01/01/2012 00:10 | 01/03/2013 00:30 | 1.320,00 | 01 | Admissão |
| 01/03/2012 00:00 | 01/03/2012 00:00 | 1.250,00 | 01 | Admissão |
| 01/03/2012 00:10 | 01/01/2012 00:10 | 1.370,00 | 09 | Ajuste de Dissídio |
| 01/03/2013 00:00 | 01/03/2013 00:10 | 1.400,00 | 01 | Admissão |
| 01/03/2013 00:10 | 01/03/2013 00:20 | 1.500,00 | 01 | Admissão |
| 01/03/2013 00:20 | 01/01/2012 00:10 | 1.620,00 | 09 | Ajuste de Dissídio |

Todos os reajustes com o motivo 09 são referentes ao ajuste de dissídio sendo que, a data de referência será a data de mudança do aumento inicial, neste caso 01/01/2012 00:10  
   
Caso o parâmetro "Reajustar os aumentos posteriores considerando o valor do aumento salarial" esteja marcado, o sistema irá somar nos aumentos que já ocorreram valor da diferença do salário novo com o salário da época.  
**Exemplo:**  
Se o salário é de 1.500,00 e teve um aumento de 10%, o salário foi para 1.650,00. Com isso teve um aumento de 150,00. Este valor será atribuído nos aumentos posteriores.  
   
   
É obrigatório o preenchimento do parâmetro "Motivo Alteração Salarial Dissídio/Aumento retroativo", nas restrições cadastrais do funcionário, na parametrização do Folha de Pagamento. Quando o mesmo não estiver preenchido, o sistema retornar uma mensagem, informando que o campo não foi preenchido, não permitindo executar o processo de alteração global de salários.   
   
   
**Realizando aumento salarial por percentual**   
Para realizar aumento salarial por percentual, o usuário deverá acessar: Administração de Pessoal | Alterações Globais | Alterações Cadastrais | Alteração de Salários, selecionar o funcionário desejado, definir a data para alteração, definir o motivo pelo qual o funcionário terá seu salário alterado e marcar o campo: "Alteração", avançar etapa.   
Na tela seguinte marcar o campo: "Percentual" e definir qual será a porcentagem de aumento que o funcionário terá, avançar etapa. O sistema deverá executar o processo e registrar a alteração no histórico salarial do funcionário.   
   
   
**Observação**  
   
Marcando o parâmetro "Aumentar número de casas decimais" permite informar um percentual com até 10 casas decimais.  
   
O sistema possuí uma forma do usuário calcular o percentual que será aplicado sobre uma antecipação de aumento salarial.   
Após acessar: Administração de Pessoal | Alterações Globais | Alterações Cadastrais | Alteração de Salários, selecionar o funcionário desejado, definir a data para alteração, definir o motivo pelo qual o funcionário terá seu salário alterado e marcar o campo: "Alteração", avançar etapa.   
Na tela seguinte, o usuário deve clicar em "Calcular perc. de aumento complementar", inserir as informações nos campos "Percentual total" e "Percentual já aplicado" e clicar em calcular. Feito isto, o sistema retorna o percentual que deve ser aplicado no reajuste. Caso queira utilizar o percentual no processo de alteração global de salários, basta marcar o parâmetro "Utilizar perc. calculado no processo".  
   
   
**Realizando aumento salarial por fórmula**   
Para realizar aumento salarial por fórmula, o usuário deverá acessar: Administração de Pessoal | Alterações Globais | Alterações Cadastrais | Alteração de Salários, selecionar o funcionário desejado, definir a data para alteração, definir o motivo pelo qual o funcionário terá seu salário alterado e marcar o campo: "Alteração", avançar etapa.   
Na tela seguinte marcar o campo: "Fórmula" e informar a fórmula de alteração, avançar etapa. O sistema deverá executar o processo e registrar a alteração no histórico salarial do funcionário.   
   
**Exemplo de fórmula para aumento salarial – funcionários mensalistas**

RC \* 1.50 = Através desta fórmula o usuário terá um aumento de 50% em seu salário.

**Exemplo de fórmula para aumento salarial – funcionários horistas**

HC \* 1.10 \* J = Através desta fórmula o usuário terá um aumento de 10% no seu salário/ hora.  
   
**Exemplo de fórmula para aumento salarial para funcionários com salário composto**  
**Para alterar todos os salários compostos no cadastro do funcionário:** VALSALCOMP (EVTSALCORRENTE) \* 1.10  
Esta fórmula aumentará cada salário composto cadastrado dentro da pasta do funcionário em 10%.  
**Para alterar apenas um dos salários compostos no cadastro do funcionário:** VALSALCOMP ('0002') \* 1.10 Esta fórmula aumentará o evento de salário composto '0002' cadastrado dentro da pasta do funcionário em 10%.  
   
**Para alterar um salário composto em uma data** VALSALCOMPDATA ('0001', '01/01/2000')\*1.10  
Esta fórmula aumentará o evento de salário composto '0001' cadastrado dentro da pasta do funcionário em uma data.  
**Exemplo de fórmula para alteração de jornada para funcionários com salário composto** SE EVTSALCORRENTE = '0002' ENTAO 100 SENAO 200 FIMSE Esta fórmula irá lançar para o funcionário 100 minutos de jornada se o evento for o "0002" caso contrário, irá lançar 200 minutos de jornada.  
   
**Observação**  
É possível realizar também alteração de jornada para os funcionários, basta informar a fórmula de alteração no campo: "Fórmula de Alteração de Jornada", tal fórmula deverá ser expressa em minutos. Para funcionários que usam salário composto e a alteração salarial global for feita por fórmula, esta fórmula de jornada será obrigatória e poderá ter valor igual a zero. Para funcionários que não usam salário composto esta fórmula de jornada não poderá ser igual a zero.  
   
**Realizando aumento salarial através das tabelas salariais do RMVitae**   
Para realizar aumento salarial para funcionários, o usuário deverá acessar: Administração de Pessoal | Alterações Globais | Alterações Cadastrais | Alteração de Salários, selecionar o funcionário desejado, definir a data para alteração, definir o motivo pelo qual o funcionário terá seu salário alterado e marcar o campo: "Alteração", avançar etapa.   
Na tela seguinte marcar o campo: "Tabelas Salariais do RMVitae", avançar etapa. O sistema deverá executar o processo buscando informações registradas nas tabelas salariais do RMVitae que estão vinculadas à função do funcionário em questão.  
   
**Observação**  
Este campo somente estará visível se o usuário possuir integração com o Totvs Gestão de Pessoas. O usuário poderá optar em realizar o aumento salarial dos funcionários conforme a tabela salarial cadastrada no Totvs Gestão de Pessoas, considerando a estruturação em níveis e faixas. Para correta alteração salarial através das tabelas salariais do RMVitae, o parâmetro: "Considerar os salários das tabelas salariais" deverá estar marcado nas definições de parametrização do Totvs Gestão de Pessoas. **Realizando aumento salarial por percentual para funcionários que possuem salário composto** Para realizar aumento salarial por percentual para funcionários que possuem salário composto, o usuário deverá acessar: Administração de Pessoal | Alterações Globais | Alterações Cadastrais | Alteração de Salários, selecionar o funcionário desejado, definir a data para alteração, definir o motivo pelo qual o funcionário terá seu salário alterado, marcar o campo: "Salário Composto" e marcar o campo: "Alteração", avançar etapa.  
Na tela seguinte marcar o campo: "Percentual" e definir qual será a porcentagem de aumento que o funcionário terá, avançar etapa.  
Na tela seguinte marcar o(s) evento(s) desejados que o funcionário terá a alteração processada, avançar etapa. O sistema deverá executar o processo e registrar a alteração no histórico salarial do funcionário.   
   
**Realizando aumento salarial por fórmula para funcionários que possuem salário composto** Para realizar aumento salarial por fórmula para funcionários que possuem salário composto, o usuário deverá acessar: Administração de Pessoal | Alterações Globais | Alterações Cadastrais | Alteração de Salários, selecionar o funcionário desejado, definir a data para alteração, definir o motivo pelo qual o funcionário terá seu salário alterado, marcar o campo: "Salário Composto" e marcar o campo: "Alteração", avançar etapa.   
Na tela seguinte marcar o campo: "Fórmula" e informar a fórmula para alteração, avançar etapa.  
Na tela seguinte marcar o(s) evento(s) desejados que o funcionário terá a alteração processada, avançar etapa. O sistema deverá executar o processo e registrar a alteração no histórico salarial do funcionário.   
   
**Exemplo de fórmula para alteração de salário composto**  
**Para alterar todos os salários compostos no cadastro do funcionário:**

VALSALCOMP (EVTSALCORRENTE) \* 1.10

Esta fórmula aumentará cada salário composto cadastrado dentro da pasta do funcionário em 10%.

**Para alterar apenas um dos salários compostos no cadastro do funcionário:**

VALSALCOMP ('0002') \* 1.10

Esta fórmula aumentará o evento de salário composto '0002' cadastrado dentro da pasta do funcionário em 10%.  
   
**Para alterar um salário composto em uma data**

VALSALCOMPDATA ('0001', '01/01/2000')\*1.10  
Esta fórmula aumentará o evento de salário composto '0001' cadastrado dentro da pasta do funcionário em uma data.  
   
**Realizando reprogramação salarial para funcionários que possuem salário composto**  
   
**Incluindo evento de salário composto**  
Para realizar a reprogramação salarial para funcionários que possuem salário composto, o usuário deverá acessar: Administração de Pessoal | Alterações Globais | Alterações Cadastrais | Alteração de Salários, selecionar o funcionário desejado, definir a data para alteração, definir o motivo pelo qual o funcionário terá seu salário alterado, marcar o campo: "Salário Composto", e "Reprogramar evento que compõe salário composto" e escolher a ação: "Incluir", avançar etapa.   
Na tela seguinte, através de fórmulas o usuário deverá informar qual será o valor do evento e qual será a jornada deste evento. Por fim, na última tela do processo escolher o evento que será incluído para o funcionário, avançar etapa. O sistema deverá executar o processo e incluir o evento para o funcionário.  
   
**Excluindo evento de salário composto**  
   
Para realizar a reprogramação salarial para funcionários que possuem salário composto, o usuário deverá acessar: Administração de Pessoal | Alterações Globais | Alterações Cadastrais | Alteração de Salários, selecionar o funcionário desejado, definir a data para alteração, definir o motivo pelo qual o funcionário terá seu salário alterado, marcar o campo: "Salário Composto", e "Reprograma evento que compõe salário composto" e escolher ação: "Excluir", avançar etapa.   
Na tela seguinte escolher o evento que será excluído do salário composto do funcionário, avançar etapa. O sistema deverá executar o processo e excluir o evento que compõe o salário do funcionário.  
   
   
**Observação:**   
Marcando o parâmetro: "Lançar evento para funcionário que não usa salário composto", os eventos escolhidos serão lançados para todos os funcionários da seleção, inclusive para aqueles que não possuem salário composto.  
   
**Realizando cancelamento de alteração salarial** Para realizar o cancelamento de uma alteração salarial, o usuário deverá acessar: Administração de Pessoal | Alterações Globais | Alterações Cadastrais | Alteração de Salários, selecionar o funcionário desejado, definir a data para alteração, definir o motivo pelo qual o funcionário terá seu salário cancelado e definir qual tipo de ação será executada, avançar etapa.   
Na próxima tela o usuário deverá executar o processo.  
   
   
**Observação**  
   
Ao processar o cancelamento, o sistema irá cancelar o aumento com maior data da mudança informada.   
Será cancelado todos os motivos de dissídio, respeitando as seguintes condições:  
a. Motivo de mudança igual ao motivo de ajuste de dissídio;  
b. Data de mudança do aumento cancelado igual a data de referência dos registros de ajuste de dissídio.  
   
   
**Realizando cancelamento de alteração salarial registrando alterações**  
   
Para realizar o cancelamento de uma alteração salarial registrando alterações, o usuário deverá acessar: Administração de Pessoal | Alterações Globais | Alterações Cadastrais | Alteração de Salários, selecionar o funcionário desejado, definir a data para alteração, definir o motivo pelo qual o funcionário terá seu salário cancelado, marcar o campo: "Cancelamento" e "Registra a Alteração", avançar etapa.   
Na próxima tela o usuário deverá executar o processo. Ao selecionar essa opção, o sistema irá cancelar a alteração salarial selecionada e registrar este processo no histórico salarial.   
   
**Realizando cancelamento de alteração salarial apenas na data informada** Para realizar o cancelamento de uma alteração salarial apenas na data informada, o usuário deverá acessar: Administração de Pessoal | Alterações Globais | Alterações Cadastrais | Alteração de Salários, selecionar o funcionário desejado, definir a data para alteração, definir o motivo pelo qual o funcionário terá seu salário cancelado, marcar o campo: "Cancelamento" e "Apenas na data informada", avançar etapa.   
Na próxima tela o usuário deverá executar o processo. Ao selecionar essa opção, o sistema irá cancelar todas as alterações salariais selecionadas apenas na data informada no campo: "Data da Mudança".

|  |  |
| --- | --- |
|  | Informações Complementares |

---

eSocial
