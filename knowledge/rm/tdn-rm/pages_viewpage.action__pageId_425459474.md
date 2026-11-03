---
content_hash: 4aab205061129afbfc06ac2ead7d768cbf80cc3679a6f22f56fe92198f41dedd
fetched_at: '2026-06-29T00:09:36.148526+00:00'
page_id: '425459474'
product: rm
source: tdn-rm
title: Gerar / Cancelar Classificação Geral
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459474
version: 3
---

O processo "Classificação Geral" será disponibilizado na forma de Assistente. O usuário irá utilizar esse  processo para  produzir a classificação geral de um processo seletivo. O usuário poderá executar o processo tanto para gerar a classificação geral ou para excluí-la, caso ela já tenha sido gerada anteriormente.  A Opção "Excluir classificação" só estará habilitada se for detectado que foi gerada uma classificação geral.

O que é a Classificação geral? A classificação geral é a listagem na qual constam todos os candidatos que foram classificados para chamada em suas respectivas áreas de interesse. Essa listagem permite que a instituição organizadora possa comparar o desempenho dos candidatos entre si independentemente da classificação em sua área ofertada escolhida.

Será possível saber, por exemplo, qual candidato entre todos os classificados obteve o melhor desempenho.

Como é feito o cálculo? O processo irá recuperar a lista de candidatos classificados para chamada em suas áreas de interesse.  Para esses candidatos será calculada pontuação que servirá de base para classificação geral.  
O cálculo da pontuação geral poderá ocorrer de duas formas:

**a)** Cálculo fixo => Ocorrerá sempre que não for informada uma fórmula de classificação geral. A pontuação do candidato usada será a mesma que ele obteve na  classificação da sua área de interesse.  
**b)** Cálculo por fórmula => Ocorrerá sempre que for informada uma fórmula de classificação geral. A pontuação do candidato será obtida através da aplicação dessa fórmula. Serão disponibilizadas no cadastro de fórmulas as seguintes funções que poderão estar envolvidas no cálculo da pontuação:

|  |  |
| --- | --- |
| 1 - PSCGAreaID | Retorna o ID da área ofertada do candidato |
| 2 - PSCGAreaNome | Retorna o Nome da área ofertada do candidato |
| 3 - PSCGTotalEtapas | Retorna o total de etapas da área |
| 4 - PSCGTotalHorarios | Retorna o total de horários em uma etapa específica |
| 5 - PSCGNotaClassificacao | Retorna a nota que classificou o candidato em sua área de interesse |
| 6 - PSCGClassificacao | Retorna a classificação do candidato em sua área de interesse |
| 7 - PSOrdHorarioCod | Retorna a ordem do horário da prova a partir do seu código. |
| 8 - PSCGOrdHorarioNome | Retorna a ordem do horário da prova a partir do seu nome. |
| 9 - PSCGOrdCadernoCod | Retorna a ordem da prova no caderno a partir do seu código. |
| 10 - PSCGOrdCadernoNome | Retorna a ordem da prova no caderno a partir do seu nome. |
| 11 - PSCGCodProvaOrd | Retorna o código da prova a partir da sua ordem no caderno. |
| 12 - PSCGCodProvaNome | Retorna o código da prova a partir do seu nome. |
| 13 - PSCGNomeProvaOrd | Retorna o nome da prova a partir da sua ordem no caderno. |
| 14 - PSCGNomeProvaCod | Retorna o nome da prova a partir do seu código. |
| 15 - PSCGNotaProvaOrd | Retorna a nota obtida na prova a partir da sua ordem no caderno. |
| 16 - PSCGNotaProvaCod | Retorna a nota obtida na prova a partir do seu código. |
| 17 - PSCGValorProvaOrd | Retorna o valor da prova partir da sua ordem no caderno. |
| 18 - PSCGValorProvaCod | Retorna o valor da prova partir da seu codigo. |
| 19 - PSCGNotaMinimaOrd | Retorna a nota mínima de aprovação da prova a partir da sua ordem no caderno. |
| 20 - PSCGNotaMinimaCod | Retorna a nota mínima de aprovação da prova a partir do seu código. |
| 21 - PSCGPesoProvaOrd | Retorna o peso da prova partir da sua ordem no caderno. |
| 22 - PSCGPesoProvaCod | Retorna o peso da prova partir do seu código. |
| 23 - PSCGQtdQuestOrd | Retorna a quantidade de questões da prova a partir da sua ordem no caderno. |
| 24 - PSCGQtdQuestCod | Retorna a quantidade de questões da prova a partir do seu código. |
| 25 - PSCGNotaQuestOrd | Retorna a nota obtida em uma questão a partir da ordem da prova no caderno. |
| 26 - PSCGNotaQuestCod | Retorna a nota obtida em uma questão a partir do código da prova. |
| 27 - PSCGValorQuestOrd | Retorna o valor de uma questão a partir da ordem da prova no caderno. |
| 28 - PSCGValorQuestCod | Retorna o valor de uma questão a partir do código da prova. |
| 29 - PSCGRedacaoOrd | Retorna "S" se a prova for de redação e "N" se não for a partir da ordem no caderno. |
| 30 - PSCGRedacaoCod | Retorna "S" se a prova for de redação e "N" se não for a partir do seu código. |
| 31 - PSCGLinguaEstOrd | Retorna "S" se a prova for de língua estrangeira e "N" se não for a partir da ordem no caderno. |
| 32 - PSCGLinguaEstCod | Retorna "S" se a prova for de língua estrangeira e "N" se não for a partir do código. |
| 33 - PSCGAreaPermiteENEM | Retorna "S" se a área permite e "N" se não permite utilização do ENEM. |
| 34 - PSCGCandUtilizaENEM | Retorna "S" se o candidato optou e "N" se não optou pela utilização do ENEM. |
| 35 - PSCGNotaRedacaoENEM | Processo Seletivo - Retorna a nota obtida na prova de redação do ENEM. |
| 36 - PSCGNotaObjetivaENEM | Retorna a nota obtida na prova objetiva do ENEM. |
| 37 - PSCGQtdProvas | Quantidade de provas da etapa. |
| 38 - PSCGSomaNotas | Soma das notas obtidas nas provas. |
| 39 - PSCGSomaNotasObjetivas | Soma da(s) notas na(s) prova(s) objetiva(s). |
| 40 - PSCGSomaNotasRedacao | Soma da(s) nota(s) na(s) prova(s) de redação. |
| 41 - PSCGSomaNotasLinguas | Soma da(s) nota(s) obtida(s) na(s) prova(s) de língua(s) estrangeira(s). |
| 42 - PSCGSomaValorProvas | Soma do(s) valor(es) da(s) prova(s). |
| 43 - PSCGSomaValorObjetivas | Soma do(s) valor(es) da(s) prova(s) objetiva(s). |
| 44 - PSCGSomaValorRedacao | Soma do(s) valor(es) da(s) prova(s) de redação. |
| 45 - PSCGSomaValorLinguas | Soma do(s) valor(es) da(s) prova(s) de língua(s) estrangeira(s). |

Em caso de dois ou mais candidatos empatarem o desempate ocorrerá, respectivamente, de acordo com os critérios:  
a) Idade: o candidato mais velho será o melhor classificado b) Número de inscrição: caso haja empate por idade, candidato com o menor número de inscrição será o melhor classificado.  Ou seja, aquele que se inscreveu primeiro receberá a melhor classificação.

O processo de geração poderá ser executado várias vezes, sempre atualizando por completo a listagem de classificação geral.

**Pré-requisito para gerar a classificação** Será possível a execução deste processo somente após a classificação de todas as áreas ofertadas do Processo Seletivo. Essa condição será verificada logo após o usuário selecionar a opção Gerar classificação e tentar avançar para o próximo passo do assistente. As áreas consideradas como não classificadas são as que possuírem candidatos ativos com status "inscrito para seleção" ou "classificado para próxima etapa".  Ou seja, não será possível avançar se for detectado que existem áreas ofertadas à classificar.

Os candidatos desclassificados por qualquer motivo não serão classificados pelo processo de classificação geral.

**Impactos**  
Cadastro do Processo Seletivo : A utilização da fórmula depende do campo "Fórmula para classificação geral" do cadastro Processo Seletivo.

Cadastro Inscrições do Candidato: A classificação geral e a respectiva pontuação que a resultou serão mostradas no cadastro de inscrições WinForms.

Relação com o Portal: A divulgação desta listagem de classificação geral no Portal será pelo link "Classificação geral" e será exibido somente após a chamada dos candidatos aprovados para o Processo seletivo. Também será possível visualizar pela área privada do candidato no serviço Histórico/Resultados. A exibição deste serviços podem ser parametrizados nos Parâmetros do Sistema (F8).
