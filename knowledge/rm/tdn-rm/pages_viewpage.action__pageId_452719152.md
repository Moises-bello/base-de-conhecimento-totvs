---
content_hash: 3587168090144bc25474321a187d783ce4f19f8b96ca851ec6fcde6cdc698baf
fetched_at: '2026-06-29T00:10:03.749200+00:00'
page_id: '452719152'
product: rm
source: tdn-rm
title: Relatório do Espelho do Cartão de Ponto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719152
version: 30
---

**Relatório do Espelho do Cartão de Ponto**

**Importante:**

O nome do funcionário será impresso por padrão considerando o *"Nome Social".Caso seja necessário imprimir pelo* Nome Civil , deverá confirmar o parâmetro na etapa 3 do relatório ["Imprimir apenas Nome Civil"](https://tdn.totvs.com/pages/viewpage.action?pageId=698288682).

O Relatório do Espelho do Cartão de Ponto é uma representação visual do cartão de ponto do funcionário (Batidas, atrasos, extras, abonos) no período indicado. Serve, junto com a assinatura, para comprovar junto ao Ministério do Trabalho o ponto eletrônico do trabalhador e como relatório demonstrativo de dados necessários para controle gerencial.  
   
Este relatório poderá ser parametrizado para a emissão em conformidade com as necessidades do cliente. Esta parametrização será feira no módulo "Relatório do Espelho do Cartão de Ponto" e, se houver necessidade, no gerador de relatórios através do RM Reports com a flexibilidade de re-nomear campos, ocultar campos, adicionar novos, criar fórmulas, criar consultas.  
   
**Informações importantes sobre a geração do espelho do cartão:**  
   
É possível gerar o relatório do espelho para um ou mais funcionários utilizando a seleção por código de quebra da seção e a seleção de funcionários.

O período de geração do espelho será informado pelo usuário conforme necessitar.

A função exibida no relatório é selecionada a partir do histórico de funções do funcionário considerando a Data fim definida, ou  
seja, será impresso no relatório a função que o funcionário exercia na Data fim definida na geração do relatório.  
   
O horário será impresso no espelho de acordo com a informação da data informada no parâmetro "Informar Quadro de Horário com base na data:" sendo que este parâmetro será apenas para a informação da data. Para não imprimir o Quadro de Horário será necessário colocar como visível = Não no relatório dentro do RM Reports.  
   
As anotações pessoais podem ser informadas no Espelho do cartão de acordo com a seleção, neste caso também será necessário que no RM Reports esteja com o campo Visível = Sim.  
   
**Observação:**  
As anotações pessoais são feitas dentro do cadastro do funcionário. Podem ser efetuadas nos sistemas RM Chronus e RM Labore.  
   
Os abonos serão impressos no dia da ocorrência de acordo com a seleção de código ou descrição. Ou seja, se não houver batida no dia considerado como abonado, será impresso o código e/ou a descrição do abono, logo a frente do dia mas, se houver batida, a impressão será feita após as batidas. Para imprimir a descrição de abono no final do espelho será necessário que no RM Reports esteja Visível = Sim.   
   
É possível imprimir abonos em jornadas não trabalhadas. Quando selecionado será impresso   a descrição dos abonos em dias que não há jornada de trabalho . Exemplo: Batida Nula, Feriado.

**Observação:**  
O código e a descrição do abono somente serão apresentados se existir a ocorrência calculada na data para o abono correspondente. A informação é gravada na tabela aocorrenciacalculada.   
   
Quando for solicitado  para imprimir apenas Horas a pagar/descontar apenas as horas extras, os atrasos e as faltas que serão pagas/descontadas dos funcionários, não mostrando as horas que serão compensadas e que serão encaminhadas para o banco de horas.  
**Observação:**  
Esta opção é apenas para Banco de Horas diário por Ocorrências.   
   
Quando imprimir horas compensando dia a dia será impresso apenas as horas que excederem a compensação.  
**Observações:**  
1.  Esta compensação será feita apenas para funcionários com banco de horas diário por ocorrência.   
2.  Estas horas que serão compensadas são apenas aquelas que estão no banco de horas do funcionário. As horas extras pagas, os atrasos e faltas descontadas no movimento do funcionário não entrarão para a compensação do espelho.   
3.  Não irá considerar o campo pagar/descontar no módulo ocorrências coletadas para a compensação.   
   
Há a possibilidade de imprimir as batidas efetuadas em dias que o funcionário está de férias ou afastado e também de imprimir o espelho dos funcionários que estão na situação de férias ou afastado dentro do período atual mesmo sem ter movimentação.  
   
Pode-se imprimir a falta por suspensão em cada dia da falta.  
**Observações:**  
1.  Se a falta for por suspensão e não tiver nada informado no campo "Motivo" no módulo Falta por Suspensão, ao imprimir o relatório do espelho de cartão de ponto do funcionário selecionando esta opção, o sistema irá imprimir no lugar das batidas do funcionário a palavra "Suspensão".  
2.  Esta opção só será habilitada quando o parâmetro "Utiliza justificativa de exceções" estiver marcado no parâmetro do sistema, ou para os funcionários que possuírem banco de horas diário por ocorrência.  
   
A opção de imprimir data de transferência será utilizada pelos funcionários que foram demitidos por transferência no sistema RM Labore. Marcando esta opção o sistema irá trazer para os novos registros dos funcionários, ou seja, para o registro em que o funcionário estará na situação de ativo, a data de transferência no relatório espelho de cartão de ponto.   
**Atenção:**  
Estas informações devem constar no espelho de cartão de ponto dos funcionários para ajudar a conferência dos cálculos do sistema, para informar a transferência do funcionário e também para a fiscalização.  
   
As descrições serão utilizadas para cada coluna de batidas conforme a necessidade.  
**Observação:**  
Se o parâmetro "Imprimir Descanso e Compensado" estiver marcado e o campo Folga/Descanso estiver em branco será informado Desc (mais o intervalo da folga cadastrado no grupo de descanso).  
**Exemplo:**  
Desc ( 00:00 - 24:00 )  
   
É possível a imprimir o motivo da folga cadastrada para o funcionário no Espelho do Cartão de Ponto em cada dia que houver a folga para o funcionário.  
**Observação:**  
Esta opção de cadastro de folgas somente é aceita para funcionários com Horário do tipo flexível, compensação por período ou semanal, e o parâmetro compensa falta não pode estar marcado. Desta forma, ao informar FOLGA para o funcionário e o motivo o sistema passará a imprimir no espelho do cartão.  
   
Na frente dos dias de descanso e compensado poderá ser impresso as suas descrições, bem como, o horário dos mesmos  
**Observação:**  
Para os funcionários que possuem cálculo por jornada o sistema irá imprimir apenas os descansos do grupo de descanso.  
   
O status das batidas serão "C" para coletado e "D" para digitado.  
   
Ao discriminar horas a compensar do banco de horas por período será verificado se o funcionário possui banco de horas por período e se os parâmetros utiliza compensação de extras, atrasos, faltas estão marcados, caso estejam, o sistema passará a imprimir na frente das horas um 'C' informando que é compensado. Será feita a totalização dessas horas no final do espelho.  
**Observações:**  
Este parâmetro deverá ser usado para funcionários com banco de horas por período e que utilizam compensação manual de horas (extras, atrasos ou faltas) parametrizado no cadastrado do funcionário. E todas as horas extras, atrasos e faltas devem estar parametrizadas como compensar. Caso tenha alguma hora de extras, atrasos ou faltas que são enviadas para o movimento como pagar ou descontar não deve ser utilizado esse parâmetro.  
   
Caso seja definido para  imprimir a descrição dos feriados, ou seja, se não houver batida no dia considerado como feriado, será impresso a descrição dos feriados logo a frente do dia; mas, se houver batida, a impressão será feita abaixo do dia.  
**Observação:**  
Se esta opção estiver selecionada, o sistema realiza a impressão da descrição do feriado no relatório, mesmo que o funcionário não considere feriados. ( Parâmetro "Considera Feriados" desmarcado no Cadastro de Funcionários).   
   
É possível imprimir descrição dos feriados apenas para funcionários que consideram feriados no cálculo. Para que seja impresso a descrição do feriado que foi considerado para o cálculo da movimentação do funcionário será verificado se o parâmetro "Considera Feriados" no cadastro do funcionário está marcado e se o parâmetro "Não considera feriados no cálculo" não está marcado no cadastro do horário do funcionário.  
**Observação:**  
A opção "Considera feriados no cálculo" só será habilitado se a opção "Imprime descrição dos feriados" estiver marcada.

**Observação:**Ao selecionar  a opção "Imprimir a descrição da atitude" se a extra for "Não Autorizada" será demonstrada na visualização do espelho em frente a hora realizada o \* (Asterisco).

Há a possibilidade de imprimir horário contíguo para funcionário que utiliza, ou seja, será emitido o relatório do espelho do cartão de ponto com as batidas referentes à jornada no dia que se iniciou a jornada.  
**Observação:**  
Para isso o funcionário deve possuir o cálculo da movimentação por jornada, o seja ter o horário do tipo flexível com compensação diária e possuir cadastros nas pastas de Parâmetros de Jornada e Histórico de Jornadas.  
**Exemplo:**  
00005 ALESSANDRA LOPES DE ABREU   
005360 - 00013 Representante Técnico Vendas  
   
28/12/2004 TER 16:00 05:00 | 05:23 | 13:00 | | | 07:00 |  
29/12/2004 QUA 22:00 06:00 | | 08:00 | | | 07:00 |

O relatório do espelho do cartão por default passará a imprimir o "Nome Social"  informado no cadastro do funcionário em informações Pessoais aba identificação.

Utilize  o parâmetro  ["Imprimir apenas Nome Civil"](https://tdn.totvs.com/pages/viewpage.action?pageId=698288682) ,caso seja necessário a emissão considerando o Nome Civil.

O relatório do espelho de cartão de ponto é impresso obedecendo a seguinte ordem: Seção e chapa. Outra ordenação poderá ser escolhida, sendo que a opção por seção será sempre default**.**

**Observação:**

É possível realizar a geração do relatório do espelho do cartão do ponto enviando para o Totvs Assinatura Eletrônica .

O usuário deverá permitir acesso nos perfis e realizar as configurações necessárias. Maiores informações : ["Enviar relatório para assinatura eletrônica"](https://tdn.totvs.com/pages/viewpage.action?pageId=697270099) .

**Observações:**  
1.    O sistema não ordena o relatório do espelho do cartão de ponto quando o Campo Complementar quando o Tipo do Campo for Texto.  
2.   O sistema não gravará no perfil dos parâmetros do espelho de cartão de ponto o código do campo complementar, pois este código pode ser Desativado no cadastro de campo complementar.  
   
O relatório a ser gerado deve ser importado em RM Reports para ser selecionado no processo de gerar o espelho do relatório.

O Relatório do Espelho de Ponto poderá ser personalizado sempre que for necessário, mas para isto será preciso importar o relatório oficial, exportar para um diretório local e depois importar novamente. Isto deve ser feito para manter a integridade do relatório original, oficial da TOTVS.

**Cabeçalho:**

A imagem salva nas informações da coligada é utilizada no cabeçalho de cada relatório, sendo assim indicamos que o tamanho em bytes seja o menor possível no máximo 150kb, para evitar lentidão na geração do arquivo do relatório de espelho de ponto.

**Imprimir horário contíguo**

O parâmetro **'Imprimir horário contíguo'** permite que as batidas do espelho sejam impressas de forma contínua. Esse parâmetro pode ser selecionado durante a geração do relatório.

Se o parâmetro estiver marcado, o relatório será gerado no formato contíguo, ou seja, as batidas serão impressas com base na data de referência da jornada. Se o parâmetro estiver desmarcado, as batidas serão impressas de acordo com a data em que foram registradas.

### Exemplos de Cenários:

* + **Cenário 1**

    - **Imprimir horário contíguo**: Marcado
    - **Resultado**: As batidas serão impressas no formato contíguo.
  + **Cenário 2**

    - **Imprimir horário contíguo**: Desmarcado
    - **Resultado**: As batidas serão impressas na data em que foram registradas.

|  |  |
| --- | --- |
|  | Como Fazer |

---

[Parametrização e configuração do relatório espelho de ponto no gerador de relatórios](http://totvsconnect.blogspot.com.br/2012/11/parametrizacao-e-configuracao-do)  
[Como Fazer - Parametrização do Relatório do Espelho do Cartão.NET](http://tdn.totvs.com/pages/viewpage.action?pageId=149882506)
