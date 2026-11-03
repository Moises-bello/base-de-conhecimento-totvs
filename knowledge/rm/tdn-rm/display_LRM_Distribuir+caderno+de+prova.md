---
content_hash: 13f8bf8140182723944af2ce7d629d395a13e99ab97264cc5103e09955657656
fetched_at: '2026-06-29T00:09:29.832543+00:00'
page_id: '425458302'
product: rm
source: tdn-rm
title: Distribuir caderno de prova
type: documentation
url: https://tdn.totvs.com/display/LRM/Distribuir+caderno+de+prova
version: 2
---

O processo servirá para que seja estabelecido o vínculo entre os candidatos já alocados em uma sala de prova em cada uma das provas que ele fará naquele local. Ao ser executado, o processo irá gerar e armazenar um número de identificação único para cada uma das provas que o candidato irá realizar. O processo é também responsável por ligar os candidatos às respectivas provas, criadas no RM Testis, relativas à sua área de interesse. Esse vínculo é necessário para que os processos de importação de gabaritos, correção e classificação sejam executados.

Utilização do processo:

Prédio: se este campo for informado o processo irá realizar a distribuição de cadernos de provas somente para os candidatos alocados no prédio especificado.

Qtd de provas: este parâmetro pode ser usado se a instituição quiser que, em uma mesma sala, sejam aplicadas provas com gabaritos diferentes. Essa prática é utilizada para garantir que candidatos sentados em posições adjacentes não façam provas idênticas. Para atender estes casos, o sistema permite até 4 gabaritos alternativos para cada prova. Os candidatos irão fazer a mesma prova, contendo exatamente as mesmas questões. Porém, a prova de cada candidato apresentará as questões em uma seqüência diferente das de quem estiver sentado imediatamente à sua frente ou ao seu lado. O processo de distribuição irá definir a posição de cada candidato na sala, assim como o tipo de gabarito que ele deverá receber.

Este processo poderá ser executado quantas vezes forem necessárias para a área ofertada, verificando sempre o status da inscrição do candidato. Se o status da inscrição for diferente de inscrito para seleção, estes candidatos não serão considerados.

Após a execução deste processo, será possível gerar as informações para que a gráfica confeccione e empacote os cadernos de provas e os gabaritos. Esse intercâmbio será feito por meio do envio de arquivo texto no layout Arquivo Exportação de Candidatos para Gráfica.

E como facilidade foi criado um processo de Exportação de dados de candidatos para gerar um arquivo txt para ser enviado a gráfica com intuito de montar os cadernos de prova. Ele está disponível no menu de processos do processo seletivo.

**Pré - requisitos do processo**:  
 Deverão existir candidatos já alocados nos locais de prova
