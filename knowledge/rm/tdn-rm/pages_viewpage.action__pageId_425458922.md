---
content_hash: e6dc37ed613457c3e64b9648c21f960fca8127b26862c682ee72750a5f23a3a5
fetched_at: '2026-06-29T00:09:32.790175+00:00'
page_id: '425458922'
product: rm
source: tdn-rm
title: Personalização de Plano de Pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458922
version: 14
---

---

Ao cadastrar o contrato do aluno é possível indicar um Plano de Pagamento, previamente cadastrado no sistema, para que as parcelas para pagamento deste contrato sejam automaticamente criadas conforme o plano indicado, otimizando assim a criação do contrato.

Muitas das vezes, no entanto, é preciso modificar as parcelas criadas para atender a demandas específicas. Nestes casos a instituição de ensino pode utilizar o processo de ‘*Personalização do plano de pagamento’* que consiste basicamente em utilizar um Plano de Pagamento como *modelo* e em seguida modifica-lo, personalizando-o conforme necessário, seguindo, contudo, regras previamente definidas.

Para utilizar este recurso, primeiramente é necessário indicar o Plano de Pagamento a ser utilizado como modelo durante a personalização. Esta indicação é feita dentro do cadastro de *‘Parametrização por Curso|Aba <<Configuração matrícula>>’*. Feita esta associação do plano modelo para personalização à Parametrização por curso, no cadastro do contrato do aluno o botão ***‘Personalizar’*** ficará habilitado para utilização, porém as seguintes regras serão validadas:

- Não será permitida a personalização do plano caso já existam lançamentos financeiros gerados para o contrato.  
- As parcelas que por ventura já existirem cadastradas no contrato, serão todas substituídas pelas parcelas personalizadas.  
- Os serviços eventualmente definidos como ‘Obrigatórios’ no Plano de Pagamento modelo deverão obrigatoriamente fazer parte do plano personalizado.

 Ao acionar o botão ***‘Personalizar’*** será aberta uma nova tela com as informações contidas no Plano de Pagamento modelo, para que assim você possa personalizar o plano para o contrato que estiver sendo editado.

Todos os serviços presentes no plano modelo serão listados nesta tela com suas respectivas informações apresentadas de forma resumida e condensada em uma linha para cada serviço.

Você poderá incluir um novo serviço para esta personalização ou excluir um dos serviços presentes, basta clicar no respectivo botão.

Para que as informações de cada serviço sejam expandidas, clique no sinal [+] na linha de cada serviço, assim serão apresentadas detalhadamente as parcelas previstas para cada serviço, com as suas respectivas informações para que você, assim, as personalize conforme necessário.

Na linha de cada serviço estarão disponíveis os botões para *incluir* ou para *excluir* parcelas para o serviço. As novas parcelas incluídas respeitarão as informações da última parcela existente para o serviço, dando sequência aos dados como No., Vencimento e Competência. O valor da parcela incluída manualmente deverá ser digitado.

Se na coluna *Qde parcela*, presente na linha que contém o resumo do serviço, for indicada uma nova quantidade de parcelas, todas as parcelas previstas para o serviço em questão serão excluídas e automaticamente novas parcelas, na quantidade indicada, serão incluídas sendo que o valor base do serviço será rateado entre as parcelas criadas. As outras informações das parcelas respeitarão a sequência normal.  Se, ainda na linha que contém o resumo do serviço, for indicado um novo valor na coluna *Valor personalizado*, o sistema perguntará se deseja ratear este valor entre as parcelas deste serviço que tenham valor fixo, caso a sua resposta seja *Não*, você poderá em seguida indicar, como queira, o valor de cada parcela.

Para excluir uma parcela existente, selecione-a e clique no respectivo botão para *excluir*.

Na parte de baixo da tela será apresentado um resumo dos valores com as seguintes informações:

- **Origem do(s) serviço(s):** indica qual origem do serviço está sendo totalizada. Teremos uma linha para cada tipo de origem e linhas distintas para serviços definidos como obrigatórios ou não. As Origens podem ser:

- **Plano modelo:** indica que o total apresentado nesta linha se refere a serviços utilizados no plano de pagamento modelo.

- **Personalização:**indica que o total apresentado nesta linha se refere a novos serviços incluídos na personalização e que não são utilizados no plano de pagamento modelo.

 -**Serviço(s) obrigatório(s):** serão apresentadas totalizações separadas conforme a obrigatoriedade dos serviços:

- Obrigatórios = **Sim**: indica que o total apresentado nesta linha se refere a serviços definidos como ‘Obrigatórios’ no plano de pagamento modelo. Os serviços definidos como ‘Obrigatórios’ no plano modelo devem obrigatoriamente estar presente no plano personalizado, ou seja, não poderão ser excluídos. Os seus valores base, no entanto, poderão sofrer alterações, desde que a permissão para esta modificação tenha sido assinalada no cadastro do plano modelo ou caso o usuário tenha permissão especial para modificação conferida ao seu Perfil.

- Obrigatórios = **Não**: indica que o total apresentado nesta linha se refere a serviços presentes no plano de pagamento modelo, porém, não são ‘Obrigatórios’ no plano personalizado, ou seja, se desejarem, estes serviços poderão ser totalmente excluídos na personalização.

 - **Total valor base do plano:** indica o total do valor dos serviços cadastrados no plano de pagamento modelo.

 - **Total do valor personalizado:** indica o total do valor dos serviços que serão praticados no plano personalizado.

 - **Diferença (valor base do plano X valor personalizado):** sempre que o valor base do plano modelo estiver diferente do valor personalizado, esta diferença será apresentada. A diferença ocorrerá quando o valor base de um serviço que fizer parte do plano modelo for modificado, seja mudando manualmente o valor sugerido para alguma parcela, seja incluindo nova parcela para um dos serviços ou ainda excluindo alguma destas parcelas, o sistema fará este controle indicando a diferença.

 - **Aplicar valor na(s) parcela(s) selecionada(s):** Sempre que houver diferença entre o valor base e o valor personalizado, o usuário poderá optar por realizar a distribuição automática desta diferença fazendo um rateio entre as parcelas, para isto, selecione primeiramente as parcelas que irão participar do rateio e clique no respectivo botão.  
Assim:  
- Se o valor parametrizado estiver maior que o valor base, será apresentada uma diferença (+) e, ao clicar neste botão, este valor será rateado e ***removido*** do valor de cada parcela selecionada, eliminando assim a diferença.  
- Da mesma forma, se o valor parametrizado estiver menor que o valor base, será apresentada uma diferença (-) e, ao clicar neste botão, este valor será rateado e ***acrescentado*** ao valor de cada parcela selecionada para também, eliminar a diferença.

Ao clicar neste botão o sistema fará o ajuste da diferença automaticamente, *removendo* ou *acrescentando* os respectivos valores rateado às parcelas selecionadas, porem nada impede que o ajuste seja feito por você, manualmente, no valor de cada parcela. Lembrando mais uma vez que conforme parametrização anterior, o sistema permitirá finalizar a personalização do plano, mesmo que haja diferença entre os valores.

Se desejar restaurar as informações originais do Plano de Pagamento modelo, clique no respectivo botão, mas atenção, pois com isso, a personalização realizada até o momento será perdida.

Ao final do processo, será listado um *LOG* com o resumo das informações de pagamento personalizadas para o contrato.

Na tela de cadastro dos contratos que tiverem o seu Plano de Pagamento personalizado, será apresentada a aba *‘Personalização do plano de pagamento’* com algumas informações sobre a personalização realizada no plano de pagamento destes contratos.

A partir dos patches das versões **12.1.2602, 12.1.2510.157, 12.1.2506.228 e 12.1.2502.266**, após a execução do processo de personalização do plano de pagamento, o campo referente ao plano de pagamento será atualizado na tabela de contrato, conforme o plano de pagamento que foi personalizado através do processo.
