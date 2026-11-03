---
content_hash: f043f4ffd4c3aaa923e280ebe17a5317fb06e502fbcda2322e6402f511830db1
fetched_at: '2026-06-29T00:09:34.076002+00:00'
page_id: '425459134'
product: rm
source: tdn-rm
title: Alocar candidatos em locais de prova
type: documentation
url: https://tdn.totvs.com/display/LRM/Alocar+candidatos+em+locais+de+prova
version: 6
---

Todo candidato ao realizar sua inscrição em um processo seletivo, escolhe um local para realização de prova dentre os disponíveis. Através deste local escolhido pelo candidato é que o processo saberá definir em qual cidade, campus e sala que o candidato será alocado para realizar as provas de seleção.

Os candidatos serão alocados por etapa. Na lista de cada forma de alocação estarão presentes as etapas de acordo com o que foi configurado para as áreas ofertadas do processo seletivo. Se o processo seletivo contiver mais de uma etapa, a alocação para a 2ª etapa e consecutivas ocorrerão apenas para candidatos já classificados na primeira etapa e que estejam com status "Classificado para próxima etapa". Se contiver somente uma etapa ou se for a primeira alocação ocorrerá verificação de status "Inscrito para seleção".

Na alocação manual o tratamento será o mesmo quando se tratar de mais de uma etapa na área ofertada, o candidato será alocado para cada etapa de acordo com seu status

## **Alocação Manual**

Neste processo será possível definir quatro configurações que irão determinar como será realizada a alocação dos candidatos. Abaixo segue a definição de cada uma:

**Alocar candidatos que não pagaram taxa de inscrição:** através desta configuração será possível determinar se os candidatos que ainda não pagaram a taxa de inscrição do processo seletivo serão alocados. Se esta opção não for marcada, todos os candidatos que estiverem com o status da inscrição igual a "Inscrito (pendente de confirmação de pagamento)" não serão alocados. Por isso é extremamente importante que o processo "Confirmar Inscrições" seja executado periodicamente.

**Alocar candidatos com documentação pendente:** através desta configuração será possível determinar se candidatos que não entregaram todos os documentos obrigatórios serão alocados. Pode ter sido definido que a 1ª opção de área de interesse do candidato exige a apresentação/entrega obrigatória de um ou mais documentos. Nesse caso, se essa opção não for marcada, o processo não irá alocar os candidatos para os quais constam documentos obrigatórios não marcados como entregues. A atualização do checklist de documentos é feita por meio da tela "Documentação do Candidato".

**Alocar candidatos por ordem alfabética:** através desta configuração será possível determinar que os candidatos sejam alocados respeitando a ordem alfabética dos respectivos nomes.

**Alocar candidatos por área de interesse ofertada:** através desta configuração será possível determinar que os candidatos sejam alocados de forma que cada sala contenha candidatos de uma única área de interesse ofertada. Desta forma a alocação irá agrupar os candidatos por áreas de interesse ofertadas.

**Alocar candidatos por forma de inscrição:** através dessa opção os candidatos poderão ser alocados separados de acordo com a forma de inscrição escolhida. Quando essa opção for utilizada, o processo não irá alocar em um mesmo local de prova os candidatos que se inscreveram utilizando formas de inscrição diferentes.

Será possível parametrizar a execução da alocação para que ocorra para uma ou mais áreas ofertadas da etapa selecionada.

Alocação Manual para local de prova online

A partir da versão **12.1.2410.299** o processo de **Alocação Manual** só será realizado para áreas de interesse que **não utilizem local de prova online.**

**Alocação de candidatos local de prova online**

Caso a área de interesse em que o candidato esteja se inscrevendo seja configurada com a opção **“Usa local de prova Online”** marcada, o candidato será alocado no local de prova online automaticamente ao final da inscrição. [Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=425458924#:~:text=Ao%20realizar%20o%20cadastro,dispon%C3%ADvel%20de%20prova%20online.).

A tabela auxiliar "Local" reflete diretamente nas regras de negócio deste processo, pois existem algumas informações muito importantes que são utilizadas na alocação, entre elas:

1. Número de lugares vertical.
2. Número de lugares horizontal.
3. Número de canhotos.
4. Suporte a necessidades especiais.

Durante a inscrição o candidato informa se é canhoto, neste caso quando o processo for executado será verificado se as salas de prova disponíveis possuem suporte a candidatos canhotos e os mesmo serão alocados de acordo com a disponibilidade informada no cadastro de locais. O mesmo acontece com a descrição de necessidades especiais. Durante a inscrição os candidatos informam se são portadores de alguma necessidade especial, e, se forem, os mesmos também serão alocados de acordo com a disponibilidade informada no cadastro de locais.

O processo considera as datas das etapas para alocar candidatos, ou seja, o sistema verificará se no local de prova há lugares disponíveis para o dia|hora que ocorrer a seleção de cada etapa.  Pode acontecer do processo não alocar todos os candidatos devido a falta de lugares. Neste caso o Log. do processo irá descrever todas as faltas identificadas para o usuário.  Uma vez que foram identificadas faltas de lugares para alocar todos os candidatos, basta cadastrar novos lugares de acordo com as necessidades necessárias e executar o processo novamente. Ao executar o processo novamente, os candidatos já alocados permanecerão sem nenhuma mudança e somente os que não foram alocados serão alocados nesta próxima execução. Somente candidatos com necessidades especiais do tipo "outras" não serão alocados por este processo, pois por se tratar de necessidades muito específicas deverão ser analisadas de forma individual pela instituição de ensino e alocadas manualmente de acordo com locais correspondentes. Para realizar a alocação manual basta utilizar o anexo do candidato "Local da Prova do Candidato".

É possível alocar os candidatos após ter sido realizado chamadas anteriores. Existindo inscrições no processo seletivo com status da inscrição= Inscrito para seleção, será possível alocar. Diferente deste status, somente o status Classificado para próxima chamada que poderá alocar.

No Log serão exibidas também as listagens de candidatos não alocados por pendência de pagamento ou entrega de documentação. A listagem de candidatos não alocados por não pagamento somente será exibida se o processo tiver sido parametrizado para fazer essa verificação. Da mesma forma, a listagem de candidatos não alocados por documentação pendente somente será exibida se o processo tiver sido parametrizado para fazer a verificação de documentação pendente.

**Pré-requisitos do processo**:  
**a)**Deverão existir inscrições realizadas para o processo seletivo.  
**b)** Deverão existir "Locais de Processo Seletivo" cadastrados para o processo seletivo, que não sejam locais de prova Online.  
**c)** As "Áreas de Interesse Ofertadas" para o processo seletivo deverão estar com as etapas definidas e com a opção de “Utiliza local de prova online” desmarcada.
