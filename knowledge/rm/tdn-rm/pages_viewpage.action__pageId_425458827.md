---
content_hash: 503e2d12cd23b50b928673fd0e8d2c0a22dc6d8b963278d0ce6e6259395b0413
fetched_at: '2026-06-29T00:09:32.339271+00:00'
page_id: '425458827'
product: rm
source: tdn-rm
title: Geração da Contabilização por competência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458827
version: 47
---

---

A geração da contabilização por competência pode ser realizada acessando-se o menu *Financeiro/Contábil | Geração | Contabilidade* ou então através do processo '*Gerar contabilização'* disponível dentro do menu *Financeiro/Contábil | Contratos* podendo ser realizada para os contratos que forem selecionados ou para todos os contratos disponíveis nesta visão. Para esta última forma, utilize *Filtros* apropriados que retorne na visão somente os contratos desejados.

Para a execução deste processo, indique:

**1 - Operação**: Indique se deseja gerar a *Contabilização* ou gerar *Estorno* de alguma contabilização já realizada.

**− Contabilização:**Se, por exemplo, for indicado **02/2015** no período para a contabilização de um contrato cuja competência contábil se inicia em 01/2015, serão incluídos os lançamentos contábeis referentes às competências de janeiro e fevereiro/2015.   
Na próxima execução, se for indicado 03/2015, somente a contabilização referente à competência de março será incluída, a menos que o valor do contrato tenha sofrido alguma alteração e, se este for o caso, além do lançamento referente à contabilização da competência indicada, o sistema incluirá automaticamente os lançamentos necessários para acertar a contabilização do valor do contrato.

**Observação**A primeira vez em que a contabilização de um contrato é executada, o sistema inclui um lançamento referente à contabilização do valor TOTAL do contrato e em seguida o(s) lançamento(s) referente(s) à contabilização da realização ou apropriação mensal conforme a competência indicada. Se o contrato não sofrer alteração em seu valor total, mês a mês será realizada somente a apropriação mensal conforme a competência indicada, porém, se o contrato sofrer alguma alteração em seu valor, no momento em que for solicitada a contabilização da próxima competência, o sistema incluirá o lançamento da respectiva competência e também outro lançamento para registrar a alteração, sendo que este lançamento será incluído de acordo com o ***modelo*** de contabilização definido nos parâmetros deste sistema. A contabilização das competências será realizada sempre de forma sequencial.

**− Estorno:**Ao indicar um mês/ano para estorno, os lançamentos serão estornados desde a última competência contabilizada até a competência informada, também de forma sequencial. Se, por exemplo, o contrato já tivesse sido contabilizado até a competência 06/2015 e precisássemos estornar os três últimos meses contabilizados, teríamos que indicar para estorno a competência **04/2015**. Neste caso, as contabilizações estornadas seriam referentes às competências 06/2015, 05/2015 e 04/2015 inclusive.

**Observação**  
Se os lançamentos ainda estiverem no Lote N, ao executar o processo de contabilização utilizando-se a opção *Estorno* os lançamentos serão excluídos do lote.  
Se os lançamentos já tiverem sido integrados ao lote oficial da contabilidade, Lote 0, eles não poderão mais ser excluídos e, ao realizar o *Estorno* serão incluídos, então, novos lançamentos de estorno, que basicamente são lançamentos ao contrário do original, com o intuito de *'anular ou cancelar'* o efeito contábil anterior. Estes receberão o status '**E** = Estorno' e serão incluídos no lote criado especificamente para receber os estornos. O lançamento original, que está no Lote 0, não será excluído, mas terá o status alterado para '**I** = Incorreto'.

**Temos a possibilidade de estonar todas as contabilizações, sem informar mês/ano**No processo de estorno que não for informado o Mês/Ano ao clicar em executar será apresentado uma mensagem "Foi selecionado a opção de estorno sem informar mês/ano, com isso todos os registros contabilizados serão estornados", caso queira seguir todas as contabilizações do contrato serão estornadas.  
  
**O processo de estorno é executado também para as provisão de aumento e cancelamento**No processo de estorno que for informado o Mês/Ano e ao clicar em executar todos os registros provisão juntamente com a apropriação de aumento e cancelamento serão estornados.  
Por exemplo, o contrato tivesse sido contabilizado até a competência 06/2015, no mês 07/2015 ocorreu uma alteração no contrato que foi contabilizado a provisão de aumento, apropriação de aumento e apropriação mensal.  
Se necessário estornar essa provisão e apropriação de aumento hoje ao estornar informando a competência 07/2015, além de estornar a apropriação de aumento e apropriação mensal, também será estornado a provisão de aumento.

**2 - Período para contabilização**: Ao executar este processo, informe **até** qual mês/ano deseja efetuar a contabilização do contrato ou o seu estorno. O mês/ano aqui informado deve estar dentro do período de competência contábil. Para mais informações sobre o período de competência contábil, consulte [Contabilidade - Parâmetros](http://tdn.totvs.com/pages/viewpage.action?pageId=425459120).  
 ****Temos a possibilidade de contabilizar somente a provisão d**e contrato****- Contabiliza apenas provisão:** Marcando essa opção indica que será realizado a contabilização ou estorno somente da provisão do contrato na execução do processo, sem a opção marcada será realizado a contabilização do contrato mais a apropriação mensal, caso a provisão do contrato não exista.   
Existe também a opção nos parâmetros do sistema, *Ambiente | Parâmetros | TOTVS Educacional | Integração | Contabilidade  | Contabilidade 2/2,*que podemos indicar se será feito somente a provisão do contrato "Contabiliza apenas a provisão do contrato", com essa opção marcada mesmo informando o "Período de Contabilização" será executado somente a provisão dos contratos ainda não diferidos, para os contratos diferidos será apropriado mensalmente conforme data de contabilização, para mais informações acesse 

**3 - Data de Contabilização**: Os lançamentos gerados pelo processo de contabilização por competência, por padrão, terão como data, o último dia do mês correspondente à sua competência. Se desejar que esta seja a regra para a data dos lançamentos a serem gerados, deixe o campo 'Data de Contabilização' em branco, porém, se desejar informar uma data específica para os lançamentos a serem gerados, indique-a neste campo, contudo, a data informada não poderá ser maior que a data atual do sistema.

**4 - Data de Contabilização do Estorno**: os lançamentos gerados de estorno, por padrão, terão como data, o dia que está sendo realização o estorno. Se desejar que esta seja a regra para a data dos lançamentos a serem gerados, deixe o campo 'Data de Contabilização' em branco, porém, se desejar informar uma data específica para os lançamentos a serem gerados, indique-a neste campo, contudo, a data informada não poderá ser maior que a data atual do sistema.

**Temos a possibilidade de executar filtros mais completos e também opção de log detalhado do evento contábil quando contabilizado apenas um contrato, conforme descrito abaixo:**

**5 - Habilitar multi contexto:**Esta opção possibilita ao usuário selecionar um filtro que especifique quais os contextos deverão ser processados, ao marcar a opção "Habilitar multi contexto" é obrigatório informar um filtro que se aplica a Coligada, Filial e Nível de ensino.  
A opção "Habilitar multi contexto" só ficará visível se o processo de contabilização / estorno for chamado fora da visão de contratos e com o fracionamento de processos habilitado, para mais informações, [clique aqui.](http://tdn.totvs.com/pages/viewpage.action?pageId=466323952) 

**6 - Filtro Genérico**: Este é o filtro padrão do sistema, onde é possível aperfeiçoar as buscas com informações básicas como Cod. Contrato, Responsável Acadêmico e Período Letivo.

**7 - Filtro por Período Letivo / Matriz Aplicada:** Nesse filtro podemos escolher o Período letivo, Curso, Habilitação, Matriz Curricular e Turno.   
Caso o cliente pretenda contabilizar todos os contratos de um determinado curso, é obrigatório nesse filtro que preencha o período letivo e curso, então o sistema irá contabilizar todos os contratos que estão elegíveis para  serrem contabilizados. 

**8 - Filtro por Consulta SQL****:**  Nesse filtro é possível montar uma consulta SQL da maneira que desejar. Importante ressaltar que a consulta SQL utilize os campos CODCOLIGADA, RA, CODCONTRATO, IDPERLET.

**9 - Log de analise do processamento do Evento Contábil:**O Log de evento contábil habilitado auxiliar na identificação da(s) causa(s) da diferença entre débito e crédito das partidas geradas, para mais informações, [clique aqui.](http://tdn.totvs.com/pages/viewpage.action?pageId=425458707)

**Temos a possibilidade de executar o diagnostico dos contratos, que será** **responsável****por validar as regras de contabilização.**

**10 - Diagnóstico:** Diagnóstico é uma funcionalidade que permite executar uma analise nos contratos validando as regras que estabelecem se os contratos podem ou não ser contabilizados, tais como: 

* Contrato cancelado
* Contrato sem parcelas
* Situação de matrícula que não gera contabilização por competência
* Período letivo encerrado para contabilização
* Contrato do tipo acordo
* Data de competência fora do período de contabilização
* Parcelas contábeis contabilizadas com IDOPERACAO NULO
* Contratos com parcelas que não contabilizam por competência

Após a execução da analise serão geradas advertências no log de contabilização que poderão ser consultas posteriormente, para os contratos que não forem gerados advertência será gerado um log com status analisado com sucesso, que indica que o contrato está apto a ser contabilizado.

É importante ressaltar que a analise não será executada para os contrato que já estiver contabilizado ou existir algum log com status de erro ou advertência, nesse caso o log será mantido.  

**- Executar contabilização em modo de diagnóstico:**Indique se o *Diagnóstico* deverá ser executado, nesse momento não serão contabilizados contratos. 

Exemplo: Contratos com Período letivo encerrado

Log de advertência com a mensagem: Período letivo [ 2019\_1 ] encerrado para contabilização. Contrato: 10582 do aluno 20180448

- Contratos contabilizados pelo no modelo antigo não terão log de diagnostico gravado.

Para mais informações sobre a funcionalidade de Diagnóstico,
