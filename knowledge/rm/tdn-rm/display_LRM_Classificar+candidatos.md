---
content_hash: c812889904be730145ad63a0ba0b81bcbf929df1c8731a32045af4c95c3a0ae6
fetched_at: '2026-06-29T00:09:36.256195+00:00'
page_id: '425459487'
product: rm
source: tdn-rm
title: Classificar candidatos
type: documentation
url: https://tdn.totvs.com/display/LRM/Classificar+candidatos
version: 50
---

O objetivo do processo de classificação é gerar o resultado do processo seletivo. Após a sua execução será possível à Instituição emitir as listagens de candidatos classificados e desclassificados.

Para classificar uma área ofertada, o usuário poderá utilizar uma das seguintes três formas:  
1- Classificação por Nota  
2- Classificação Manual  
3- Classificação por Ordem de Inscrição

Para saber mais sobre como é realizada a apuração do [concurso de bolsa](https://tdn.totvs.com/pages/editpage.action?pageId=663594324) [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=663602469).

**1- Classificação por Nota**  
Para executar a classificação por nota, primeiramente será necessário definir a etapa e as áreas ofertadas que serão classificadas. Poderá ser selecionada uma ou mais áreas ofertadas.      
Em seguida será apresentado ao usuário o passo no qual terá que selecionar a origem das notas que serão utilizadas na classificação.   
No caso da "Classificação por Nota", o sistema deverá ter sido alimentado com as notas dos candidatos, que pode ser feito pelas seguintes formas:  
   
**a-** Provas já Corrigidas no TOTVS Avaliação e Pesquisa:  
Essa forma de obtenção de notas exigirá que os candidatos já estejam vinculados às provas do TOTVS Avaliação e Pesquisa e as respostas dos candidatos já estejam introduzidas no sistema com auxílio do processo Importar Gabaritos. Após a importação das respostas, a correção de cada uma das provas deverá ser feita utilizando a funcionalidade de correção do TOTVS Avaliação e Pesquisa. O índice de acertos dos candidatos gerado na correção constitui a pontuação a ser usada na classificação.

Observação

A partir das **versões 12.1.31 (patch 12.1.31.172) e 12.1.32 (patch 12.1.32.112) e superiores,** foi criado um parâmetro "Desclassificar candidatos que não executaram a prova, não tiveram o gabarito importado ou possuem questões abertas sem correção.", este parâmetro, se desmarcado, permite classificar somente candidatos que tiveram a prova distribuída, executada, tiveram o gabarito importado ou que as questões abertas foram corrigidas através do ranking do TOTVS Avaliação e Pesquisa . Os demais candidatos serão ignorados e poderão ser classificados posteriormente.

**b-** Entrada Manual de Notas:  
Essa forma de obtenção de notas exigirá que os candidatos já estejam vinculados às provas do TOTVS Avaliação e Pesquisa e as notas serão obtidas da entrada manual por notas. Essa entrada é possível de ser acessada pelo menu "Processo Seletivo | Tabelas auxiliares | Notas | Candidatos por Prova" ou pelo menu "Processo Seletivo | Tabelas auxiliares | Notas | Prova por Candidato".

Observação

A partir das **versões 12.1.2306 (patch 12.1.2306.273), 12.1.2310 (patch 12.1.2310.227), 12.1.2402 (patch 12.1.2402.171), 12.1.2406 (patch 12.1.2406.103) e superiores**, foi criado um parâmetro "Desclassificar candidatos que não executaram a prova ou não tiveram as notas digitadas", este parâmetro, se desmarcado, permite classificar somente candidatos que tiveram a prova distribuída, executada e digitada pelo menu "Processo Seletivo | Tabelas auxiliares | Notas | Candidatos por Prova" ou pelo menu "Processo Seletivo | Tabelas auxiliares | Notas | Prova por Candidato". Os demais candidatos serão ignorados e poderão ser classificados posteriormente.

Dica quando utilizar notas do Enem

Caso a área de interesse ofertada possua uma etapa exclusiva para o processamento de candidatos com notas importadas do **Enem**, essa etapa não deve ter uma prova vinculada.   
Ao classificar, desmarque a opção **“Desclassificar candidatos que não realizaram a prova ou não tiveram as notas digitadas”**.

Nos cenários em que a etapa possuir prova vinculada e tratar notas do **Enem**, a opção **“Desclassificar candidatos que não realizaram a prova ou não tiveram as notas digitadas”** deverá estar marcada. Lembre-se de que, se o cálculo for por fórmula, ela deve considerar ambos os cenários.

**Importante:** Se a opção **“Desclassificar candidatos que não realizaram a prova ou não tiveram as notas digitadas”** estiver desmarcada e a etapa estiver vinculada a uma prova, o sistema não considerará o candidato para o processamento caso ele não possua notas informadas para a prova.

Para mais informações sobre importação de notas do Enem [clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=224102676)

**c-** Arquivo de Notas: Essa forma de obtenção de notas exigirá que os candidatos já estejam vinculados às provas do TOTVS Avaliação e Pesquisa. A instituição tem a opção de utilizar meios de correção de provas extra-sistema. Dessa forma, a obtenção de notas não passará pela execução do processo "Importar Gabaritos".  Ou seja, os gabaritos não serão lidos para o sistema e a funcionalidade de correção do TOTVS Avaliação e Pesquisa não será utilizada. Neste caso será necessário gerar, de alguma forma, um arquivo txt no layout "".  Conforme o layout, nesse arquivo não constará as respostas e sim as notas totais já computadas para cada uma das provas. O layout limita a nove o número de notas possíveis de serem informadas para cada candidato.

Ao utilizar o processo de classificação através do arquivo de notas e caso o parâmetro "Não permitir entrar com notas de candidatos ausentes" (Parâmetros → Parâmetros do sistema → Validação de entrada de notas) esteja marcado, o sistema sempre irá verificar os registros de presença dos candidatos, inserido através do processo , assim nas definições do processo de classificação o passo que define se deverá ou não ser consultado o registro de presença não será exibido pois o parâmetro geral do processo seletivo define a validação da presença como padrão.

**Observação**: à partir da versão 12.1.22 o sistema irá realizar duas validações:

1. O sistema irá validar o arquivo e ignorar linhas em que os dados dos candidatos forem inválidos, ou seja, validará se o candidato existe no processo seletivo.
2. Foi criado um parâmetro para definir se no processo o sistema irá considerar na classificação somente candidatos que estiverem no arquivo ou desclassifica os que não estiverem contidos no arquivo.

Após escolher a forma de obtenção de notas, será possível optar por considerar ou não o registro de presenças/ausências de candidatos na classificação. A situação do registro de presença será consultada, caso o parâmetro "Consultar o registro de presença de candidatos" estiver marcado. Neste caso o sistema não permitirá concluir a classificação se forem localizados candidatos (cuja inscrição não esteja cancelada) que não constem registros de presenças/ausência registrados para os mesmos. Quando estiver sendo considerado o registro de presença e houver candidatos com ausência em algum dos dias de seleção, serão desclassificados por esse motivo.   
   
Importante : Evoluído o processo de classificação para trabalhar com fórmulas . No cadastro de área ofertada, aba "Informações complementares" é possível agora definir uma fórmula de cálculo de pontuação.

Na nova MDI o Cadastro de Fórmula do Processo Seletivo está migrado para .NEt - Antes de salvar a fórmula é possível fazer o teste da funcionalidade, desde que, seja informada uma consulta SQL correta no contexto de teste. A sentença SQL informada deverá retornar ao menos um registro correspondente a uma inscrição, contendo os campos: CODCOLIGADA, IDPS, CODPESSOA, NUMEROINSCRICAO e ORDEMETAPA. Caso a consulta informada no contexto não esteja correta, ao tentar testar fórmulas que tenha alguma das funções de cálculo de pontuação, o sistema irá informar que o contexto está errado.  
   
As funções da fórmula para classificação são as seguintes:

|  |  |
| --- | --- |
| 1 -   PSOrdHorarioCod | Retorna a ordem do horário da prova a partir do seu código. |
| 2 -   PSOrdHorarioNome | Retorna a ordem do horário da prova a partir do seu nome. |
| 3 -   PSOrdCadernoCod | Retorna a ordem da prova no caderno a partir do seu código. |
| 4 -   PSOrdCadernoNome | Retorna a ordem da prova no caderno a partir do seu nome. |
| 5 -   PSCodProvaOrd | Retorna o código da prova a partir da sua ordem no caderno. |
| 6 -   PSCodProvaNome | Retorna o código da prova a partir do seu nome. |
| 7 -   PSNomeProvaOrd | Retorna o nome da prova a partir da sua ordem no caderno. |
| 8 -   PSNomeProvaCod | Retorna o nome da prova a partir do seu código. |
| 9 -   PSNotaProvaOrd | Retorna a nota obtida na prova a partir da ordem no caderno. |
| 10 - PSNotaProvaCod | Retorna a nota obtida na prova a partir do seu código. |
| 11 - PSValorProvaOrd | Retorna o valor da prova partir da sua ordem no caderno. |
| 12 - PSValorProvaCod | Retorna o valor da prova partir da seu codigo. |
| 13 - PSNotaMinimaOrd | Retorna a nota mínima de aprovação da prova a partir da sua ordem no caderno. |
| 14 - PSNotaMinimaCod | Retorna a nota mínima de aprovação da prova a partir do seu código. |
| 15 - PSPesoProvaOrd | Retorna o peso da prova partir da sua ordem no caderno. |
| 16 - PSPesoProvaCod | Retorna o peso da prova partir do seu código. |
| 17 - PSQtdQuestoesOrd | Retorna a quantidade de questões da prova a partir da sua ordem no caderno. |
| 18 - PSQtdQuestoesCod | Retorna a quantidade de questões da prova a partir do seu código. |
| 19 - PSNotaQuestaoOrd | Retorna a nota obtida em uma questão a partir da ordem da prova no caderno. |
| 20 - PSNotaQuestaoCod | Retorna a nota obtida em uma questão a partir do código da prova. |
| 21 - PSValorQuestaoOrd | Retorna o valor de uma questão a partir da ordem da prova no caderno. |
| 22 - PSValorQuestaoCod | Retorna o valor de uma questão a partir do código da prova. |
| 23 - PSRedacaoOrd | Retorna "S" se a prova for de redação e "N" se não for a partir da ordem no caderno. |
| 24 - PSRedacaoCod | Retorna "S" se a prova for de redação e "N" se não for a partir do seu código. |
| 25 - PSLinguaEstOrd | Retorna "S" se a prova for de língua estrangeira e "N" se não for a partir da ordem no caderno. |
| 26 - PSLinguaEstCod | Retorna "S" se a prova for de língua estrangeira e "N" se não for a partir do código . |
| 27 - PSAreaPermiteENEM | Retorna "S" se a área permite e "N" se não permite utilização do ENEM. |
| 28 - PSCandUtilizaENEM | Retorna "S" se o candidato optou e "N" se não optou pela utilização do ENEM. |
| 29 - PSNotaRedacaoENEM | Retorna a nota obtida na prova de redação do ENEM. |
| 30 - PSNotaObjetivaENEM | Retorna a nota obtida na prova de redação do ENEM. |
| 31 - PSEtapa | Retorna o número da etapa que está sendo classificada. |
| 32 - PSQtdProvas | Quantidade de provas da etapa. |
| 33 - PSSomaNotas | Soma das notas obtidas nas provas. |
| 34 - PSSomaNotasObjetivas | Soma da(s) notas na(s) prova(s) objetiva(s). |
| 35 - PSSomaNotasRedacao | Soma da(s) nota(s) na(s) prova(s) de redação. |
| 36 - PSSomaNotasLinguas | Soma da(s) nota(s) obtida(s) na(s) prova(s) de língua(s) estrangeira(s). |
| 37 - PSSomaValorProvas | Soma do(s) valor(es) da(s) prova(s). |
| 38 - PSSomaValorObjetivas | Soma do(s) valor(es) da(s) prova(s) objetiva(s). |
| 39 - PSSomaValorRedacao | Soma do(s) valor(es) da(s) prova(s) de redação. |
| 40 - PSSomaValorLinguas | Soma do(s) valor(es) da(s) prova(s) de língua(s) estrangeira(s). |
| 41 - PSExisteProvaPendente | Retorna "S" se o candidato possui prova pendente no Totvs Avaliação e Pesquisa e "N" se não tiver. |
| 42 - PSSetStatusInscritoSelecao | Altera o status de classificação do candidato na área ofertada para "Inscrito para seleção". |

**O cálculo da pontuação total**- Pode ocorrer de duas formas:  
   
**1-** Cálculo Fixo:  será aplicado quando não for informada no cadastro da área ofertada uma fórmula a ser usada.  As notas obtidas pelo candidato em cada uma das provas serão somadas.    
   
**2-** Cálculo por fórmula:  será aplicado quando for informada no cadastro da Área ofertada uma fórmula a ser usada.  A criação de fórmulas deverá ser feita através do cadastro de fórmulas de Globais disponível no menu "Cadastro => Fórmula". Uma vez criada, uma fórmula passará a estar disponível na lookup "Fórmula para cálculo de pontuação". No editor de fórmulas existe um conjunto de funções que permitem a construção das fórmulas. O nome dessas funções inicia com "PS" e servem para obtenção de dados dos candidatos e suas provas realizadas no momento de apuração da nota pelo processo de classificação.  
   
Tanto o cálculo fixo como o cálculo por fórmula resultam na pontuação utilizada para classificar o candidato. Ou seja, o candidato cujo cálculo resultar na maior pontuação será o melhor colocado e assim por diante. Após o cálculo da pontuação, se houver empate, será considerado melhor colocado pelo critério de desempate.  
   
Após conclusão do assistente, o sistema irá proceder com classificação de acordo com as parametrizações do usuário. O processo de classificação por nota levará em conta:

|  |  |
| --- | --- |
| A etapa | Se houver outra etapa o candidato será "Classificado para próxima etapa", senão, será "Classificado para chamada". |
| Utilização de fórmula de cálculo de nota | Definido no cadastro de Área ofertada do Processo Seletivo. |
| Critérios de desempate | Nota nas provas com maior peso e  prioridade,  Maior idade,   Número de inscrição. |
| Participação de treineiros | Não entram na classificação. |
| Não comparecimento no dia das provas | Utilizar registro de presença. |
| Desclassificar quando a nota obtida em alguma prova for zero? | Configurado na prova da área. |
| Desclassificar quando a nota obtida for abaixo do mínimo exigido? | Configurado na prova da área. |

**2 - Classificação Manual**  
A "Classificação Manual" é uma forma de classificação altamente flexível na qual o usuário é o responsável por digitar o status, a classificação e as notas dos candidatos. Nela não necessita vincular o candidato a nenhuma prova. **Ela é utilizada somente para áreas ofertadas sem etapas cadastradas.** Quando o usuário optar por essa forma de classificação, o assistente exibirá a listagem dos candidatos inscritos nas áreas. Ao selecionar a área, no grid será listado somente os candidatos inscritos nela.  
   
A interface ainda disponibiliza para os usuários os botões "Limpar", "Classificações" e "Ocultar/Exibir candidatos chamados".   
   
O botão limpar permite que o usuário retorne o valor original dos status de todos os candidatos. Ele permite também que todos os valores preenchidos para "Classificação" e "Pontuação" sejam excluídos.

* O botão "Classificação" permite que a classificação de cada candidato seja preenchida automaticamente das seguintes formas:

**1-** De acordo com a ordenação do grid: A ordem de classificação será baseada na ordem de inscrições na grid, depois disso todos os candidatos que estiverem com o status "Inscrito para seleção" terão o status alterado para "Classificado para chamada".   
   
**2-** De acordo com a pontuação: todos os candidatos que tiverem "Pontuação" terão o campo "Classificação" preenchido.  O preenchimento da "Classificação" ocorrerá da maior para a menor "Pontuação". Dessa forma, o candidato melhor classificado será o que tiver maior pontuação. Caso existam candidatos com a mesma pontuação, o sistema definirá aleatoriamente a ordem de classificação.  
  
 **3-** De acordo com o número de inscrição: A ordem de classificação será baseada no número de inscrição, depois os candidatos que estiverem com o status "Inscrito para seleção" terão o status alterado para "Classificado para chamada".   
   
**4-** Na grid "Sugerir próximo número de classificação".  Quando essa opção estiver selecionada, sempre que o usuário posicionar o cursor no campo "Classificação", se este estiver habilitado e ainda não tiver sido preenchido, será mostrado uma sugestão de classificação.

* O botão "Ocultar candidatos chamados" esconde ou mostra, no grid, os candidatos que já tiverem sido convocados em alguma chamada.  
  Para que seja possível avançar para a etapa de conclusão, será necessário que ao menos uma área ofertada da lista esteja validada.

Para alteração da pontuação no processo de classificação manual, somente os status abaixo permitem essa mudança:

* Desclassificado por meios ilícitos;
* Desclassificado por motivo de nota;
* Desclassificado por insuficiência de nota;
* Desclassificado por insuficiência de perfil;
* Desclassificado por entrevista;
* Candidato treineiro;
* Inscrito para seleção;
* Classificação pendente;
* Classificação pendente 1;
* Classificação pendente 2;
* Classificação pendente 3;
* Classificação pendente 4;
* Classificação pendente 5;
* Classificado para chamada;

Para a classificação por nota, somente serão considerados os status:

* Classificado para chamada;
* Classificação pendente;
* Classificação pendente 1;
* Classificação pendente 2;
* Classificação pendente 3;
* Classificação pendente 4;
* Classificação pendente 5;
* Inscrito para seleção;
Observação

Nas versões 12.1.23 (patch 12.1.23.203)  e 12.1.24 (patch 12.1.24.139), foi alterado para que o sistema não mostre candidatos com situação de inscrição como "Inscrito (pendente confirmação do pagamento)".

Para que estes candidatos sejam exibidos na classificação manual, deverá ser marcado o parâmetro "Exibir candidatos com status "Inscrito (pendente confirmação do pagamento)".

Caso seja feita alguma classificação para um candidato com status "Inscrito (pendente confirmação do pagamento)", sempre que for executada a classificação manual no respectivo processo seletivo, o sistema irá marcar por padrão o parâmetro "Exibir candidatos com status "Inscrito (pendente confirmação do pagamento)", esta ação é necessária para evitar possíveis inconsistências na ordem de classificação.

Nas versões 12.1.2306 (patch 12.1.2306.), 12.1.2310 (patch 12.1.2310.), 12.1.2402 (patch 12.1.2402.), 12.1.2406 (patch 12.1.2406.) e 12.1.2410 a tela foi alterada para não mostrar candidatos **não classificados** com situação de inscrição como "Inscrito (pendente confirmação do pagamento)".

Para que estes candidatos **não classificados** sejam exibidos na classificação manual, deverá ser marcado o parâmetro "Exibir candidatos com status "Inscrito (pendente confirmação do pagamento)".

Caso seja feita alguma classificação para um candidato com status "Inscrito (pendente confirmação do pagamento)", o parâmetro 'Exibir candidatos com status "Inscrito (pendente confirmação do pagamento)"' permanecerá disponível para ser marcado ou não. Desta forma, os candidatos **não classificados** somente serão exibidos no passo seguinte, no caso de o parâmetro estiver marcado.

Execuções simultâneas

Caso a classificação manual seja executada em mais de um computador ao mesmo tempo, somente os candidatos alterados serão gravados e caso o mesmo candidato seja alterado nas duas ou mais execuções, sempre irá prevalecer a última execução registrada no banco de dados.

Webservice

## **Webservice**

Quando o processo é executado pelo RM.exe, é adicionado ao fluxo os itens que fazem referencia a **ClassificacaoManualAreas** e  também itens referentes a **ListApuracaoConcursoBolsaClassificacaoManual**. Para garantir a paridade funcional entre o **RM.exe** e as integrações via **Webservice (SOAP ou REST)**, é obrigatório que a requisição contenha os itens referentes à **ClassificacaoManualAreas** e ao **ListApuracaoConcursoBolsaClassificacaoManual**.

 **O envio desses itens no XML/JSON deve seguir o mesmo padrão de preenchimento da interface do sistema, sendo uma condição indispensável para a integridade e a execução correta do processo.**

**3 - Classificação por Ordem de Inscrição**  
Das três formas de classificação, essa é mais simples. Esta poderá ser usada somente se o processo seletivo estiver marcado para utilizar "Controle de Vagas".    
  
Ao escolher essa forma de classificação, o usuário precisará apenas definir no passo seguinte qual ou quais as áreas ofertadas ele irá classificar dessa forma.   
  
Essa forma de classificação preenche a "Classificação" por ordem de inscrição de todos os candidatos com status "Inscrito para seleção" na área ofertada. O primeiro colocado será o primeiro candidato a ter se inscrito na área ofertada e assim por diante. Se existirem candidatos classificados anteriormente, a colocação irá respeitar a sequencia das execuções anteriores.  
    
**Novo!** **Classificação utilizando cotas federais** Quando o processo seletivo utilizar cotas federais, **SOMENTE** poderá ser utilizada a classificação por notas. As demais opções, classificação manual e por ordem de inscrição ficarão desabilitadas. Durante a classificação, se o processo seletivo trabalhar com cotas para instituições federais, para cada candidato serão processadas duas informações: "em qual grupo de cotas este candidato está inscrito?" e "qual a sua classificação interna deste grupo?". Isto se dará da seguinte forma:  
Informações necessárias: I1 - "Utiliza cota federal no processo seletivo?" I2 - "O candidato participará do programa de cotas?" I3 - "O candidato é egresso de ensino público?" I4 - "O candidato possui baixa renda familiar?" I5 - "O candidato é auto declarado preto, pardo ou indígena?" Grupos de cotas:  
**1**: Egressos de escola pública, com baixa renda familiar, que se auto declaram pretos, pardos ou indígenas. **2**: Egressos de escola pública, com baixa renda familiar, que NÃO se auto declaram pretos, pardos ou indígenas. **3**: Egressos de escola pública, que se auto declaram pretos, pardos ou indígenas. **4**: Egressos de escola pública, que NÃO se auto declaram pretos, pardos ou indígenas. **5** (Ampla concorrência): candidatos que não participam do programa de cotas   
"Em qual grupo de cotas o candidato está inscrito?":

* **Grupo 1**: Se I2, I3, I4 e I5 forem respondidos com "sim".
* **Grupo 2**: Se I2, I3 e I4 forem respondidos com "sim" e I5 for respondido com "não".
* **Grupo 3**: Se I2, I3 e I5 forem respondidos com "sim" e I4 for respondido com "não".
* **Grupo 4**: Se I2, I3 forem respondidos com "sim" e I4 e I5 forem respondidos com "não".
* **Grupo 5**: Se I2 ou I3 forem respondidos com "não".

**Como resultado**: este valor preencherá o campo "SPSOPCAOINSCRITO.TIPOCOTA".  
"Qual a classificação interna do grupo de cotas?": Identificado o grupo de cota que cada candidato pertence, será criada uma lista de classificação interna para cada um dos grupos: 1, 2, 3, 4.  Ou seja, para cada um dos cinco grupos será calculada a classificação numérica crescente, que representa a ordem decrescente de pontuação dentre os candidatos dos respectivos grupos. Caso o candidato não participe do programa de cotas (Se I1 ou I2 for respondido como não), o campo não será preenchido (valor NULL). **Como resultado**: este valor preencherá o campo "SPSOPCAOINSCRITO.CLASSIFICACAOCOTA".

Classificação de Inscritos com nota do ENEM sem prova

A partir da versão 12.1.2502 para que o candidato inscrito com nota do ENEM e que o processo seletivo não tenha prova seja classificado corretamente é necessário seguir as devidas configurações:

* O processo seletivo deve ter ao menos uma etapa;
* Deve ser configurada uma formula na área de ofertada utilizando as propriedades PSSetStatusClassificado e PSSetStatusDesclassificado;
  + Exemplo:
    - DECL NOTA1;  
      SETVAR(NOTA1, PSNotaNaturezaENEM);SE NOTA1>100  
      ENTAO PSSetStatusClassificado;  
      SENAO PSSetStatusDesclassificado  
      FIMSE  
      NOTA1;
    - Esse código recebe a nota do ENEM do candidato, nesse exemplo está recebendo somente a nota da prova de Natureza, valida se a nota é maior que o valor definido, caso seja maior define o candidato como classificado, caso seja menor define o candidato como desclassificado.
* Ao executar o processo de classificação de candidatos deve ser feita a seguinte configuração:
Quando o processo seletivo usar taxa de inscrição

O processo seletivo inclui a classificação dos candidatos com base em dois critérios principais:

1. **Ordem de Inscrição**: A ordem em que o candidato se inscreveu no processo seletivo.
2. **Status de Pagamento**: Se o candidato efetivou o pagamento necessário para prosseguir com o processo seletivo.

A classificação dos candidatos será realizada em duas etapas:

* **Primeiro**, o sistema verifica se o candidato pagou ou não.
* **Depois**, os candidatos que pagaram são classificados pela **ordem de inscrição**. Os candidatos que não pagaram ficam ao final da lista, independentemente da sua ordem de inscrição.

**Importante**: Candidatos que pagam depois não alteram a classificação dos candidatos que já pagaram. Eles serão sempre colocados na **última posição**.

#### **Exemplo de Classificação**

1. **Primeira Execução da Classificação**

   * **Candidatos**:

     + **Candidato 1**: Não pagou
     + **Candidato 2**: Pagou
     + **Candidato 3**: Pagou
   * **Resultado da Classificação**:

     + **Candidato 1**: Não pagou → Não classificado.
     + **Candidato 2**: Pagou → Classificação 1.
     + **Candidato 3**: Pagou → Classificação 2.

   **Observação**: O Candidato 1, embora tenha sido o primeiro a se inscrever, não foi classificado devido à falta de pagamento. O Candidato 2, que pagou, ocupa a **primeira posição** devido à sua inscrição inicial, e o Candidato 3 ocupa a **segunda posição**, pois pagou depois, mas foi o segundo a se inscrever.

---

1. **Segunda Execução da Classificação (Após o Candidato 1 Efetuar o Pagamento)**

   * **Candidatos**:

     + **Candidato 1**: Pagou
     + **Candidato 2**: Pagou
     + **Candidato 3**: Pagou
   * **Resultado da Classificação**:

     + **Candidato 2**: Pagou → Classificação 1 (primeiro, pois foi o primeiro a se inscrever).
     + **Candidato 3**: Pagou → Classificação 2 (segundo, pois se inscreveu depois do Candidato 2).
     + **Candidato 1**: Pagou → Classificação 3 (terceiro, pois pagou depois dos outros).

   **Observação**: O Candidato 2, que se inscreveu primeiro e já havia efetuado o pagamento, permanece em **primeiro lugar**. O Candidato 3, que pagou antes, mas se inscreveu depois do Candidato 2, ocupa a **segunda posição**. O Candidato 1, que pagou por último, é classificado em **terceiro lugar**.

---

#### **Considerações Importantes**

* **Critério de Pagamento**: A classificação dos candidatos é influenciada pelo **status de pagamento**.

  + **Candidatos que não pagaram** não serão classificados, independentemente da sua ordem de inscrição.
  + **Candidatos que pagaram** serão classificados com base na **ordem de inscrição**. O primeiro a se inscrever será o primeiro a ser classificado, o segundo a se inscrever será o segundo, e assim por diante.
* **Ordem de Inscrição**: A ordem de inscrição é relevante **para os candidatos que pagaram**. A posição dos candidatos será determinada com base nessa ordem. Candidatos que pagaram depois de outros não alteram a classificação dos candidatos que já pagaram.

#### **Fluxo de Classificação**

1. O sistema verifica se os candidatos efetuaram o pagamento.
2. **Candidatos que não pagaram** não serão classificados pelo processo.
3. **Candidatos que pagaram** são classificados pela **ordem de inscrição**.
   * O primeiro inscrito é classificado em **primeiro lugar**.
   * O segundo inscrito é classificado em **segundo lugar**.
   * O último inscrito é classificado em **último lugar**.

#### **Possíveis Cenários**

* **Cenário 1**: Todos os candidatos pagam antes de rodar a classificação. Neste caso, a classificação segue a **ordem de inscrição**.
* **Cenário 2**: Alguns candidatos não pagam e são desclassificados. Apenas os candidatos que pagaram são classificados, respeitando a **ordem de inscrição**.

---

**Conclusão**: A classificação dos candidatos no processo seletivo é determinada primeiro pelo **status de pagamento** (pagou ou não pagou). Somente candidatos que pagaram são classificados. Entre os candidatos que pagaram, a classificação será feita com base na **ordem de inscrição**. Candidatos que pagam depois não alteram a classificação dos outros e sempre serão classificados em **último lugar**.

Reclassificação de Candidatos

Disponível a partir da versão 12.1.2502. A partir da versão 12.1.2502 será possivel realizar a reclassificação de candidatos inscritos no processo seletivo sem alterar nenhuma informação de candidatos já matriculados.                                                     

A reclassificação pode ser executada para os processos de **"Classificação por Nota"** e **"Classificação Manual"**, selecionando a opção **"Reclassificação de Candidatos"** presente em ambas as opções de classificação.   

     1. **Reclassificação:**

1. * O sistema permitirá reclassificação dos candidatos que ainda não foram matriculados, mesmo que existam candidatos já matriculados na etapa.
   * **Importante:** Durante o processo de reclassificação, todos os candidatos vinculados ao processo seletivo selecionado serão considerados, exceto para aqueles com status de **"Compareceu à chamada" (matriculado)**, cuja posição permanecerá inalterada. As novas classificações serão ajustadas, ignorando as posições ocupadas pelos candidatos já matriculados. Por exemplo, se um candidato matriculado estiver na 2ª posição e outro candidato (ainda não matriculado) obtiver a pontuação necessária para essa colocação, ele será realocado para a próxima posição disponível — neste caso, o 3º lugar. A reorganização dos demais status será realizada com base na situação de cada candidato, o que pode ocasionar alterações nas posições na lista de classificação.
2. **Execução de Nova Classificação:**

   * As vagas ocupadas pelos candidatos já matriculados serão desconsideradas na nova classificação, garantindo que apenas as vagas remanescentes sejam utilizadas.
3. **Registro de Reclassificações Executadas:**

   * O sistema registrará cada nova classificação realizada, indicando o número correspondente (ex.: 1ª, 2ª, 3ª).
