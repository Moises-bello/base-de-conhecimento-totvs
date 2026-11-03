---
content_hash: d3dd19b437eb52c0442671ca1c8b81dab06bb89e533c62b26c9ca50501974a5d
fetched_at: '2026-06-29T00:09:36.230342+00:00'
page_id: '425459485'
product: rm
source: tdn-rm
title: Critérios de Desempate
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459485
version: 10
---

Esse cadastro tem por objetivo a definição de critérios de desempate na classificação de candidatos por nota. Poderão ser cadastrados N critérios por Área Ofertada/Etapa e ordenados em ordem de prioridades.  
O cadastro será composto dos campos: Processo Seletivo, Área ofertada, Etapa da área ofertada, Ordem de prioridade, Tipo de critério, Tipo de ordenação.  
   
Os critérios disponíveis para serem utilizados são:

* Idade;
* Número de inscrição;
* Prioridade de prova;
* Nota da prova de redação do Enem;
* Nota da prova objetiva do Enem;
* Total das provas objetivas;
* Total das provas de redação;
* Total das provas de língua estrangeira;
* Fórmula

**Importante**  
Os tipo de ordenação disponível: crescente ou decrescente e serão utilizados para todos os tipos de critérios diferentes de ***"***Fórmula". Poderão ser cadastrados mais de um tipo de critério para uma mesma etapa e a mesmos serão considerados por ordem de prioridade. Quando selecionado o tipo de critério "Fórmula" será habilitado o campo para informar a fórmula que será utilizada. Para a criação da mesma é possível utilizar funções especifica de critérios de desempate entre dois candidatos. Todas as funções tem como parâmetro o número do candidato que se deseja a informação Candidato 1 ou 2 e se iniciam com as iniciais PSDN .   
As funções disponíveis são:

|  |  |
| --- | --- |
| **Função** | **Descrição** |
| PSDNCandidatoTreineiro | Retorna "S" se o candidato é treineiro e "N" caso não seja treineiro |
| PSDNAnoENEMCandidato | Retorna o ano de realização do ENEM do candidato |
| PSDNCandUtilizaENEM | Retorna "S" se o candidato optou e "N" se não optou pela utilização do ENEM |
| PSDNNotaRedacaoENEM | Retorna a nota obtida na prova de redação do ENEM |
| PSDNNotaObjetivaENEM | Retorna a nota obtida na prova objetiva do ENEM |
| PSDNSomaNotas | Soma das notas obtidas nas provas |
| PSDNSomaNotasObjetivas | Soma da(s) notas na(s) prova(s) objetiva(s) |
| PSDNSomaNotasRedacao | Soma da(s) nota(s) na(s) prova(s) de redação |
| PSDNSomaNotasLinguas | Soma da(s) nota(s) obtida(s) na(s) prova(s) de língua(s) estrangeira(s) |
| PSDNSomaValorProvas | Soma do(s) valor(es) da(s) prova(s) |
| PSDNSomaValorObjetivas | Soma do(s) valor(es) da(s) prova(s) objetiva(s) |
| PSDNSomaValorRedacao | Soma do(s) valor(es) da(s) prova(s) de redação |
| PSDNSomaValorLinguas | Soma do(s) valor(es) da(s) prova(s) de língua(s) estrangeira(s) |
| PSDNNumeroOpcaoCandidato | Retorna o número da opção do candidato |
| PSDNNaturalidadeCandidato | Retorna a naturalidade do candidato |
| PSDNTipoSexoCandidato | Retorna o tipo do sexo do candidato |
| PSDNPaisCandidato | Retorna o país do candidato |
| PSDNEstadoCandidato | Retorna o estado do candidato |
| PSDNCidadeCandidato | Retorna a cidade do candidato |
| PSDNAreaCod | Retorna o Id da área ofertada do candidato |
| PSDNAreaNome | Retorna o nome da área ofertada do candidato |
| PSDNTotalEtapas | Retorna o total de etapas da área ofertada do candidato |
| PSDNTotalHorarios | Retorna o total de horários em uma etapa específica |
| PSDNNotaClassificacao | Retorna a nota que classificou o candidato em sua área de interesse |
| PSDNOrdHorarioCod | Retorna a ordem do horário da prova a partir do seu código |
| PSDNOrdHorarioNome | Retorna a ordem do horário da prova a partir do seu nome |
| PSDNOrdCadernoCod | Retorna a ordem da prova no caderno a partir do seu código |
| PSDNOrdCadernoNome | Retorna a ordem da prova no caderno a partir do seu nome |
| PSDNCodProvaOrd | Retorna o código da prova a partir da ordem do horário e respectiva ordem no caderno |
| PSDNCodProvaNome | Retorna o código da prova a partir do seu nome |
| PSDNNomeProvaOrd | Retorna o nome da prova a partir da sua ordem no caderno |
| PSDNNomeProvaCod | Retorna o nome da prova a partir do seu código |
| PSDNNotaProvaOrd | Retorna a nota obtida na prova a partir da sua ordem no caderno |
| PSDNNotaProvaCod | Retorna a nota obtida na prova a partir do seu código |
| PSDNValorProvaOrd | Retorna o valor da prova partir da sua ordem no caderno |
| PSDNValorProvaCod | Retorna o valor da prova partir da seu codigo |
| PSDNNotaMinimaOrd | Retorna a nota mínima de aprovação da prova a partir da sua ordem no caderno |
| PSDNNotaMinimaCod | Retorna a nota mínima de aprovação da prova  a partir do seu código |
| PSDNPesoProvaOrd | Retorna o peso da prova partir da sua ordem no caderno |
| PSDNPesoProvaCod | Retorna o peso da prova partir do seu código |
| PSDNQtdQuestCod | Quantidade de questões em uma prova a partir do seu código |
| PSDNQtdQuestOrd | Quantidade de questões em uma prova a partir da sua ordem no caderno |
| PSDNNotaQuestCod | Nota obtida em uma questao a partir do código da prova |
| PSDNNotaQuestOrd | Nota obtida em uma questao a partir da ordem no caderno |
| PSDNValorQuestCod | Valor de uma questao a partir do código da prova |
| PSDNValorQuestOrd | Valor de uma questao a partir da ordem no caderno |
| PSDNRedacaoOrd | Retorna "S" se a prova for de redação e "N" se não for a partir da ordem no caderno |
| PSDNRedacaoCod | Retorna "S" se a prova for de redação e "N" se não for a partir do seu código |
| PSDNLinguaEstOrd | Retorna "S" se a prova for de língua estrangeira e "N" se não for a partir  da ordem no caderno |
| PSDNLinguaEstCod | Retorna "S" se a prova for de língua estrangeira e "N" se não for a partir do código |
| PSDNQtdProvas | Quantidade de provas da etapa |
| PSDNDataNascimento | Retorna a data de nascimento do candidato |
| PSDNNumeroInscricao | Retorna a data de nascimento do candidato |
| PSDNPrioridadeProvaCod | Retorna a prioridade da prova pelo código da prova |
| PSDNPrioridadeProvaOrd | Retorna a prioridade da prova por ordem no caderno |
| PSDNColigadaCandidato | Retorna a coligada do candidato |
| PSDNIdPSCandidato | Retorna o IDPS do candidato |
| PSDNCandidatoPossuiDeficiencia | Retorna "S" se o candidato possui alguma deficiência e "N" caso não possua |
| PSDNCandidatoPossuiDeficienciaAuditiva | Retorna "S" se o candidato possui deficiência auditiva e "N" caso não possua |
| PSDNCandidatoPossuiDeficienciaFala | Retorna "S" se o candidato possui deficiência na fala e "N" caso não possua |
| PSDNCandidatoPossuiDeficienciaFisica | Retorna "S" se o candidato possui deficiência física e "N" caso não possua |
| PSDNCandidatoPossuiDeficienciaIntelectual | Retorna "S" se o candidato possui deficiência intelectual e "N" caso não possua |
| PSDNCandidatoPossuiDeficienciaMental | Retorna "S" se o candidato possui deficiência mental e "N" caso não possua |
| PSDNCandidatoPossuiDeficienciaOutras | Retorna "S" se o candidato possui outras deficiências e "N" caso não possua |
| PSDNCandidatoPossuiDeficienciaVisual | Retorna "S" se o candidato possui deficiência visual e "N" caso não possua |
| PSDNCandidatoPossuiReabilitacao | Retorna "S" se o candidato possui reabilitação e "N" caso não possua |

Durante a classificação de candidatos por nota, quando houver empate entre candidatos o sistema irá realizar o desempate pelos critérios cadastrados na Área Ofertada/Etapa.

|  |
| --- |
| **Exemplo de fórmula de critério de desempate:** |
| DECL NOTA1, NOTA2; /**declaração de variáveis**/    /\*zerando o valor das variáveis \*/  SETVAR(NOTA1, 0);  SETVAR(NOTA2, 0);    SETVAR(NOTA1, PSDNNotaRedacaoENEM(1));/**incrementando nas váriáveis a nota de enem do candidato 1**/  SETVAR(NOTA2, PSDNNotaRedacaoENEM(2));/**incrementando nas váriáveis a nota de enem do candidato 2**/    SE NOTA1 > NOTA2 /**comparando se a nota do candidato 1 é maior que a nota do candidato 2**/       ENTAO '1' /**se a nota do candidato 1 é maior que a do candidato 2 então o candidato 1 fica com a menor colocação**/       SENAO '2' /**se a nota do candidato 1 não é maior que a do candidato 2 então o candidato 2 fica com a menor colocação**/  FIMSE |
