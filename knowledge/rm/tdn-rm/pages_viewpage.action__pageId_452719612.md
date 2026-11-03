---
content_hash: 9969fc097254276d4df85514275a210e7e740727908c7cd78a793bc484ed1497
fetched_at: '2026-06-29T00:10:08.954691+00:00'
page_id: '452719612'
product: rm
source: tdn-rm
title: Compensação/Lançamento do Banco de Horas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719612
version: 3
---

**Compensação/Lançamento do Banco de Horas**

---

O banco de horas é um recurso utilizado pela grande maioria das empresas, que ao invés de pagar as extras e/ou descontar atrasos e faltas, guardam as horas no banco durante um período determinado e compensa o saldo até o final desse período. Ou seja, o banco de horas é uma forma de pagamento da hora extra, e posteriormente, ao invés do dinheiro, pode utilizar de horas de folga.  
O controle de banco de horas pode ser utilizado para permitir um melhor aproveitamento das horas dos empregados, realizando extras nos momentos de picos e folgando nos momentos de diminuição de serviço. Na hipótese de rescisão, o saldo do banco também poderá ser pago ou descontado.  
Esta prática se torna legal ao ser acordada em convenção coletiva ou acordo coletivo de trabalho com a participação do Sindicato da categoria. Portanto, cabe ao empregador garantir que as regras adotadas sejam válidas perante a Justiça Trabalhista, que se mantêm de forma rígida ao manifestar sua autenticidade.

ATENÇÃO: O processo de recálculo não deve ser executado simultaneamente à compensação do banco de horas, mesmo que o parâmetro **Calcula funcionários com alterações manuais** esteja desmarcado, pois o contexto do recálculo será carregado antes da compensação conseguir bloquear o movimento do funcionário, e por consequência, o recálculo irá desfazer a compensação/lançamento de banco de horas.  
   
O TOTVS Automação de Ponto permite gerenciar o banco de horas dos funcionários e a compensação das horas que estão no banco e/ou lançar para movimentação. Disponibilizando também o histórico de todas as compensações realizadas por funcionário, que conta com uma grande ferramenta de análise da compensação em forma de memória.  
A compensação pode ser feita para o banco de horas diário ou o banco de horas por período, lembrando que ao trabalhar com o diário as ocorrências serão registradas diariamente no banco. Já por período, as extras, atrasos e faltas são totalizadas em eventos conforme o período e faixas. Portanto, há regras e parametrizações cabíveis para cada tipo de banco ao realizar a compensação/lançamento.

**Observação**Ao realizar a compensação/lançamento o sistema validará se o funcionário trabalha com banco de horas diário ou por período.  
   
Primeiramente é necessário decidir o funcionário ou o grupo de funcionários que terá(ão) a movimentação gerenciada e posteriormente informe o tipo do banco e o período que será considerado. Para facilitar uma posterior utilização do processo com parametrizações já utilizadas, informe uma descrição e salve um perfil de parâmetros.  
   
Informe também um período para compensação e/ou lançamento das horas. O conceito de retroagir, utilizada em versões anteriores, tornou-se obsoleto e agora precisamos apenas definir a data início e fim para o processo, desde que o início sempre seja menor que o fim. Utilize o parâmetro 'Considera limite de dias conforme parametrização' para que a compensação considere o período conforme limite cadastrado no sindicato do funcionário.  
   
Entendendo melhor o processo, podemos distinguir a compensação do lançamento e até realizar os dois consecutivamente. Basicamente a compensação refere-se à forma com que os débitos e créditos do banco serão abatidos, e utilizando apenas a compensação esse resultado será mantido no banco, para possivelmente lançar para movimentação do funcionário. O lançamento consiste apenas em lançar as horas do banco para o movimento conforme opções disponíveis, tendo antes compensado ou não. Veja bem as opções?

* *Compensação do banco de horas:* O sistema apenas compensa os débitos e créditos, e o que sobrou permanece no banco de horas, sem realizar o lançamento para a movimentação;
* *Compensação e lançamento do banco de horas:* O sistema compensa os débitos e créditos, e o que sobrou é lançado para a movimentação do funcionário;
* *Lançamento do banco de horas:* O sistema apenas realiza o lançamento sem realizar a compensação dos débitos e créditos.

**Observação**Estes processos só deverão ser feitos após fechar o ponto do funcionário, pois ao fazer o lançamento de horas para o movimento o sistema travará o cálculo do funcionário.  
   
Para facilitar o entendimento e evitar resultados inesperados, realize o processo utilizando a simulação da compensação e ou lançamento, e nesse caso será realizada apenas uma demonstração de como seria o resultado do processo e nenhuma alteração será realizada no banco. A simulação será registrada e poderá ser visualizada acessando a 'Memória da Compensação' do histórico. Veja mais detalhes nas informações referentes ao 'Histórico de Compensação e ou Lançamento'.  
   
Conhecendo então o processo, em que temos como base o tipo do banco e para cada tipo decidimos pagar ou compensar conforme seleção, podemos entender agora as formas com que o processo será realizado ao utilizar a compensação e/ou lançamento.  
   
Opções de Compensação  
Opções de Lançamento  
   
 

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Histórico da Compensação/Lançamento  
   
   
   
   
HelpWiki - RH - Automação de Ponto
