---
content_hash: 3f8a2dc5261dfb2b8eddae15a8061755696dda3a2c4598d1a09ac8af166767ef
fetched_at: '2026-06-29T00:09:54.914829+00:00'
page_id: '445660823'
product: rm
source: tdn-rm
title: Como validar os erros gerados no S-1299 anual?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=445660823
version: 8
---

Ao realizar a transmissão do S-1299 referente ao período de apuração anual (13º), algumas mensagens podem ser retornadas pelo RET. Estas mensagens podem tratar-se de erros ou avisos gerados pelo eSocial Web.

Abaixo, veja algumas das mensagens geradas, seus motivos e o que validar no sistema para ajuste:

Mensagens de Erro - S-1299• Erro 162***Código do Erro:***

162 - Descrição : O Trabalhador com CPF : XXXXXXXXXXX e Matricula : XXXXXXXXXXXXXX consta na base de dados do Ambiente Nacional do eSocial, mas não foi informada sua remuneração. Ação Sugerida: Verificar se a falta de informação e decorrente de dificuldades operacionais ou se e possível efetuar a regularização.

***Motivo:***

Esta mensagem indica que existem funcionários que possuem vínculo empregatício com a empresa, porém não foram enviados os eventos de remuneração (S-1200) para o ambiente do eSocial.

***Validações:***

1- Certifique-se que as categorias dos funcionários estão corretamente informadas no eSocial Web. Caso necessário ajuste da categoria, deve-se retificar o evento S-2200. No caso de troca de uma categoria **com** vínculo para uma **sem** vínculo empregatício, verifique a necessidade de exclusão do S-2200 com posterior envio do S-2300.

* [Como realizar o processo de retificação dos eventos S-2200, S-2205, S-2206, S-2300 e S-2306?](http://tdn.totvs.com/pages/viewpage.action?pageId=416842991)

2- Verifique se os eventos S-1200 referente ao período de apuração anual encontram-se aceitos pelo RET (Status '10 - Aceito RET' no RM ou '4 - Consistente' no TAF).

3 - Conforme regra de validação do eSocial:

*"Para aceitação do evento de fechamento, efetuar as seguintes verificações:*

*b) Validar a integridade entre os eventos de remuneração (S-1200) recepcionados e os*  
*trabalhadores "ativos" do RET, da seguinte forma:*

*b1) Todos os trabalhadores admitidos em período igual ou anterior ao período de apuração*  
*que não estejam desligados ou cujo desligamento seja posterior ao período de apuração*  
*devem possuir o respectivo evento de remuneração já encaminhado para o mesmo período*  
*de apuração, exceto:*

*- se o trabalhador estiver afastado durante todo o período de apuração em um dos*  
*seguintes códigos de afastamento [03,05,06,07,11,12,13,14,21,22,23,24,25,27,28,30,31];"*

No caso de afastamento por Acidente de Trabalho (motivo "*01 - Acidente/Doença do trabalho"*), o eSocial está retornando a mensagem de erro 162 informando que é necessário o envio da remuneração para o funcionário. Entretanto, este funcionário, quando afastado durante todo o ano, também não possui direito ao 13º.

Entramos em contato com a Central de Atendimento do eSocial visto que a regra de validação não condiz com a condição de pagamento. Fomos orientados a, nestes casos, lançar uma verba de base de cálculo sem incidência, com rubrica informativa (9989, por exemplo) e um valor simbólico. Encaminhar um S-1200 anual para o funcionário com esta verba informativa e posteriormente encaminhar o S-1299 de fechamento anual.

• Erro 163

***Código do Erro:***

163 - Descrição: O Trabalhador sem vinculo com Nome : XXXXXXXXXXXX , CPF : XXXXXXXXXXX, NIS : XXXXXXXXXXX e Categoria : XXX consta na base de dados do Ambiente Nacional do eSocial, mas não foi informada sua remuneração. Ação Sugerida: Verificar a situação do trabalhador e efetuar a regularização.

***Motivo:***

Considerando a regra de validação do eSocial, esta mensagem trata-se de um aviso para alertar sobre a inexistência de eventos de remuneração para funcionários sem vínculo. Geralmente a mensagem é apresentada junto à outros erros como o 162, por exemplo, causando um entendimento equivocado de que trata-se de um erro propriamente dito.

***Validações:***

1- Certifique-se que as categorias dos funcionários estão estão corretamente informadas no eSocial Web. 

2 - Valide se não há nenhuma outra mensagem de erro juntamente à de código 163. Enquanto demais erros forem apresentados, a mensagem supracitada também será exibida no retorno do RET.

3 - Como não deve existir evento de pagamento (S-1210) para o período de apuração anual, verifique se a TAG {evtPgtos} foi gerada no S-1299 como "N". Caso a TAG esteja como "S", verifique se há algum S-1210 presente na fila de eventos do período de apuração anual e, caso positivo, exclua estes registros através do item "Processos | Excluir Eventos da Fila".

* [RM - eSocial - Exclusão individual dos eventos da Fila de Eventos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017738251-RM-eSocial-Exclus%C3%A3o-individual-dos-eventos-da-Fila-de-Eventos)
* [Mapeamento do Evento S-1299](http://tdn.totvs.com/display/LRM/Evento+S-1299#Leiautes-2)

Obs.: Ressaltamos a importância de realizar um Backup da base de dados sempre que excluir qualquer evento por questões de segurança.

• Erro 424

***Código do Erro:***

424 - Descrição : Rubrica não permitida em folha de decimo terceiro.

***Motivo:***

O erro nos indica que uma rubrica utilizada nas verbas de pagamento do 13º não é permitida pois não trata-se de uma rubrica específica para tal.

***Validações:***

1 - Certifique-se que o S-1010 relacionado à verba foi gerado com a rubrica adequada. Caso necessário ajustar a rubrica, deve-se retificar o S-1010 e também os S-1200 referente ao pagamento do 13º para os funcionários.

Veja abaixo algumas rubricas que podem causar a inconsistência:

*1000 - Salário, vencimento, soldo ou subsídio*  
*1003 - Horas extraordinárias*  
*1211 - Gratificações*  
*9200 - Desconto de Adiantamentos*

Entre outras...

2 - Verifique se no XML do S-1200 existem apenas verbas referentes ao período de pagamento do 13º. Caso existam verbas de Folha Mensal, o evento também será recusado. Certifique-se de estar utilizando os pacotes mais atuais do sistema que contemplam todo o processo de geração do XML de 13º de forma correta.

• Erro 761

***Código do Erro:***

761 - Descrição : Não foi localizada a remuneração do trabalhador CPF: XXXXXXXXXXX Matricula XXXXXXXXXX no período.

***Motivo:***

O erro nos indica que não foi localizado um evento de remuneração para o funcionário no período utilizado. Entretanto, identificamos que em sua grande maioria, este erro é apresentado para funcionários admitidos no mês de Dezembro e que não possuem direito ao recebimento do 13º salário.

***Atenção:** Neste caso, especificamente, caso a mensagem de inconsistência seja retornada exclusivamente com este erro (ou unicamente junto ao erro 163), sugerimos que seja realizado um contato com a Central de Atendimento do eSocial através do telefone 0800 730 0888, tendo em vista que não há nenhuma justificativa para a rejeição do fechamento do período.*

***Validações:***

1 - Verifique a data de admissão do funcionário dentro da competência.

2 - Conforme a regra de validação do fechamento do período, certifique-se de ter um S-2200 correspondente ao S-2190, caso o registro preliminar tenha sido encaminhado.

• Regra de Validação de Fechamento

Abaixo, para maiores esclarecimentos, segue regra de validação para fechamento da folha conforme Layout do eSocial.

* [Documentação Técnica eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)

  
falsefalse

**Produto:** Folha de Pagamento

false

**Rotina:** eSocial

false

**Versões:**

|  |
| --- |
| 12.1.22 |
| 12.1.21 |
| 12.1.20 |

falsefalse

**Status:** Em andamento

false

**Data:**

false

**Autores:**

Joyce Rodrigues Nereu
