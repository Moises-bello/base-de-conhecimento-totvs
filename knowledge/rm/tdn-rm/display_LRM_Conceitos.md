---
content_hash: 09332d87fc16440612e0730f999bc559c59ac0249c7b07b01bbab2881830bff0
fetched_at: '2026-06-29T00:08:14.942920+00:00'
page_id: '244722009'
product: rm
source: tdn-rm
title: Conceitos
type: documentation
url: https://tdn.totvs.com/display/LRM/Conceitos
version: 8
---

Nesta seção serão descritas as regras de negócios que o TOTVS Incorporação atenderá.

# Período / Data

A receita contábil de locação deve ser reconhecida **mensalmente** edevecorresponder ao período de uso ou de disponibilização de uso, e enquanto durar o contrato de locação/ arrendamento e/ou suas cobranças, como por exemplo, cobranças ou pagamentos de valores rescisórios que podem exceder o tempo de vigência do contrato.

Para identificar em qual competência (mês/ano) o lançamento deve ser realizado o usuário deve levar em consideração a finalidade da locação, ou seja, se trata de arrendamento / locação anual ou padrão (minimo de 30 meses) ou locação por temporada (máximo de 90 dias). Além da finalidade deve ser considerado se a cobrança é mês vencido ou mês vincendo.

* **Mês Vencido**: o locatário/arrendatário usa o imóvel e a cobrança é feita no mês seguinte;
* **Mês Vincendo:** o locatário/arrendatário paga antes de usar o imóvel, ou seja a cobrança será feita no mês anterior ao uso no caso de temporada mas no caso de aluguel para contratos de longo prazo a cobrança ocorre no mesmo mês do uso sendo cobrado até o sexto dia conforme prevê a lei do inquilinato (Art. 42).

De acordo com o entendimento das características do contrato de locação o usuário preencherá o Tipo de Contabilização, a Destinação e a Cobrança Financeira, e através destas informações o sistema calcula a competência contábil, conforme mostra o quadro abaixo.

|  |  |  |  |
| --- | --- | --- | --- |
| **Tipo de Contabilização**  (Aluguel->Contrato de locação) | **Destinação**  (Aluguel->Cadastros->Tipo de Contrato) | **Cobrança Financeira**  (Aluguel->Cadastros->Tipo de Contrato) | **Competência contábil**  (Efeito gerado na contabilização) |
| **Linear** | Arrendamento Mercantil | Mês Vencido | Não depende de cobrança e tem início a partir de data base que pode ser início da vigência, início da locação, data do contrato ou outra data informada. |
| **Padrão** | Locação Anual | Mês Vencido | Mês anterior a cobrança |
| Mês Vincendo | No mês da cobrança (art 42, lei 8.245) |
| Locação por Temporada | Valor Fechado antecipado | Em caso de adiantamento não há provisão, assim a contabilização ocorre no pagamento financeiro (baixa ) |
| Mês Vencido | Mês anterior a cobrança |
| Mês Vincendo | A definir |

De acordo com a lei do inquilinato ([LEI No 8.245, DE 18  DE OUTUBRO DE 1991](http://www.planalto.gov.br/ccivil_03/leis/l8245.htm)) a cobrança antecipada ou vincenda pode ocorrer em duas hipóteses, na **Locação sem Garantia** ou na **Locação por Temporada;**

Locação Sem Garantia:

|  |
| --- |
| *“Art. 42. Não estando a locação garantida por qualquer das modalidades, o locador poderá exigir do locatário o pagamento do aluguel e encargos até o sexto dia útil do mês vincendo.”*  *( fonte: lei do Inquilinato, SEÇÃO VII -Das garantias locatícias)* |

Locação por Temporada:

|  |
| --- |
| *“Art. 43. Constitui contravenção penal, punível com prisão simples de cinco dias a seis meses ou multa de três a doze meses do valor do último aluguel atualizado, revertida em favor do locatário:*  *III - cobrar antecipadamente o aluguel, salvo a hipótese do art. 42 e da locação para temporada.”*  *( fonte: lei do Inquilinato, SEÇÃO VIII -* *Das penalidades criminais e civis)* |

|  |
| --- |
| *“Art. 48. Considera - se locação para temporada aquela destinada à residência temporária do locatário, para prática de lazer, realização de cursos, tratamento de saúde, feitura de obras em seu imóvel, e outros fatos que decorrem tão-somente de determinado tempo, e contratada por prazo não superior a noventa dias, esteja ou não mobiliado o imóvel.”*  *”* *Art. 49. O locador poderá receber de uma só vez e antecipadamente os aluguéis e encargos, bem como exigir qualquer das modalidades de garantia previstas no art. 37 para atender as demais obrigações do contrato.*  *Art. 50. Findo o prazo ajustado, se o locatário permanecer no imóvel sem oposição do locador por mais de trinta dias, presumir - se - á prorrogada a locação por tempo indeterminado, não mais sendo exigível o pagamento antecipado do aluguel e dos encargos.*  *( fonte: lei do Inquilinato, SEÇÃO II -* *Das locação para temporada)* |

De acordo com parecer da consultoria TOTVS não há necessidade de rateio dos períodos e dos valores contábeis quando a competência extrapolar um mês.

Exemplo:

*Período  de  locação  15/01/2016  a  14/02/2016,  com  vencimento  em  20/02/2016  no  valor  de  R$ 1.000,00, a contabilização deverá ser feita da forma como segue:*

*Contabilização 1  - Provisão em FEV/2016*

| D | C |
| --- | --- |
| *Alugueis a Receber (AC)*  *R$ 1.000,00* | *Receita de Alugueis *(R)**  **R$ 1.000,00** |

*Contabilização 2  - Pelo Recebimento Efetivo realizado em Fev/2016*

| D | C |
| --- | --- |
| *Caixa/Banco (AC)*  **R$ 1.000,00** | *Alugueis a Receber (AC)*  **R$ 1.000,00** |

*<http://tdn.totvs.com/pages/releaseview.action?pageId=235570461>*

A data de contabilização será a data correspondente ao fato gerador.

|  |  |
| --- | --- |
| **Fato Gerador** | **Data Sistêmica** |
| Contrato de locação | Parametrizada entre as opções:   * “Data de Início da Vigência”; * “Data de Início da Locação”; * “Data Manual”: |
| Aditivo | “Data do Aditivo” |
| Reajuste | “Data do Reajuste” |
| Escalonamento | Para Inclusões ocorridas com contratos já efetivados, considerar a “Data Inicial” do Período de escalonamento, mas a data do lançamento do contrato será a establecida no como base do contrato |
| Evento financeiro | “Data do Evento” |
| **Rescisão** | “Data da Rescisão” |

*O nome dos parâmetros podem ser alterado em tempo de projeto afim de obter maior aderência.*

 A **data de estorno** da contabilização é a mesma data da operação original, exceto em períodos fechados onde o estorno deve ocorrer no próximo período aberto (mesmo dia da contabilização original, mas mês e ano do próximo período aberto), caso o usuário deseje que o estorno ocorra no mesmo período do lançamento original deve abrir o período (processo contábil) correspondente para que o sistema seja capaz de gerar a contabilização. Se a escrituração contábil já estiver registrada no órgão competente não recomenda-se a abertura do período.

 A data de contabilização só poderá ser alterada se o perfil do usuário assim permitir (criar novo atributo para o perfil).

# Valor de Receita

Se o imóvel for próprio, ou seja, da empresa que usa o TIN, o valor a ser reconhecido como receita será o Valor do Aluguel, já se o imóvel for de terceiros, a administradora (que usa o TIN) deve reconhecer a receita referente a administração do imóvel, ou seja, a taxa de administração e a taxa de intermediação ou outras taxas que venham a ser criadas no futuro.

 Para as situações onde a administradora do imóvel possui parte da propriedade do bem deve ser considerado como receita o valor rateado destinado a ela, conforme percentual de propriedade estabelecido no cadastro de cada imóvel associado ao contrato de Locação, acrescido dos percentuais de administração aplicados a parte destinada aos demais proprietários. Este tratamento deverá ser realizado via recurso de formula RM associado ao evento contábil.

 Entende-se como Valor do Aluguel a remuneração paga ao proprietário pelo uso do imóvel, desta forma pode ser composto por um ou mais valores apresentados pelo sistema, sendo passível de parametrização pelo usuário afim de atender as normas vigentes. As despesas cobradas pelo locador contra o locatário, como IPTU ou reformas, etc., podem ser caracterizadas como despesas diretas e desta forma reconhecidas de forma linear, no entanto não compõe receita, assim sendo caberá ao usuário a devida identificação e parametrização do evento contábil (modelo de contabilização).

 O desconto é um valor redutor de receita que deve ser contabilizado em conta específica (redutora do ativo) e deve seguir o mesmo modelo de reconhecimento da receita, ou seja, linear ou não. A contabilização pode ser feita por imóvel ou pelo valor total do contrato ou mesmo por valor atribuído ao centro de custo e todas estas situações devem contempladas nos recursos destinados a contabilização do módulo de aluguel.

# Eventos Financeiros

Outra operação que poderá ser reconhecida como receita é a Luva ou CDU (Cessão de Direto de Uso) geralmente cobrada de imóveis comerciais localizados em *mall*, e cadastrada no TIN na forma de Evento Financeiro.  Somente o **Evento Financeiro Avulso** do TIN poderá ser contabilizado, e este tratamento ocorrerá no item do evento contábil relacionado ao contrato de locação. Os **Eventos Financeiros Agregados** não devem gerar contabilização por serem agregados diretamente a cobrança do contrato de locação o que pode gerar redundância na contabilização

Será criado no item do evento contábil um “aplicar” para Evento Financeiro Luva bem como funções de formula para buscar os valores correspondentes ao evento financeiro.

# Processos aptos a contabilização

Serão processos passiveis de contabilização:

|  |  |  |
| --- | --- | --- |
| **Processo** | **Ação** | **Resultado** |
| Contrato de Locação | Efetivar | Se a contabilização for automática e se tiver um evento contábil associado ao “contrato de locação”, gera contabilização. CASO CONTRÁRIO, não contabiliza e não avisa. |
| Voltar Situação do Contrato de Locação | Se a contabilização for automática e se tiver associado ao contrato de locação um evento contábil e houve a contabilização na efetivação, o sistema exclui a contabilização. CASO CONTRÁRIO, não dispara o processo de contabilização.  Lançamentos contábeis são excluídos se o período correspondente estiver “em aberto”, caso contrário são estornados. |
| Escalonamento | Salvar | Se o escalonamento for criado com o contrato ainda em preparação, não dispara de contabilização;  Se o escalonamento for criado com o contrato já Efetivado a contabilização será disparada utilizando o mesmo mesmo evento contábil do contrato de locação. |
| lançamento Financeiro | Gerar Lançamento Financeiro | Se a contabilização for automática e se tiver associado ao um evento contábil  ao “Lançamento financeiro” , gera contabilização. CASO CONTRÁRIO, não contabiliza e não avisa. |
| Excluir Lançamento Financeiro | Verificar se houve contabilização pelo Lançamento Financeiro, se:  **SIM**: exclui contabilização;  **NÃO**: não dispara processo de contabilização ;  Lançamentos contábeis são excluídos se o período correspondente estiver “em aberto. |
| Reajuste | Aplicar Reajuste | Se a contabilização for automática e se tiver um evento contábil associado ao “contrato de locação”, gera contabilização. CASO CONTRÁRIO, não contabiliza e não avisa. A Aplicação do processo de reajuste não implica na contabilização do valor equivalente de reajuste, pois isso depende da forma que o evento contábil foi criado e se nele há um item que considera o valor reajustado. |
| Voltar Reajuste | Verificar se houve contabilização do reajuste, se:  **SIM**: estorna ou exclui contabilização;  **NÃO**: não dispara processo de contabilização ;  Lançamentos contábeis são excluídos se o período correspondente estiver “em aberto”, caso contrário são estornados (para períodos fechados.) |
| Aditivo do Contrato de Locação | Efetivar | Se a contabilização for automática e se tiver um evento contábil associado ao “contrato de locação”, gera contabilização. CASO CONTRÁRIO, não contabiliza e não avisa.  O Valor a ser contabilizado será de acordo com parametrização do evento contábil criado pelo usuáiro. |
| Evento financeiro | Inclusão | Verifica se o evento é Avulso e se é do tipo Luva, se for permite que seja informado um Evento Contábil, senão não habilita o campo. |
| Salvar | Verificar se há evento contábil associado ao processo de Aditivo,  se:  **SIM**: dispara contabilização;  **NÃO**: não contabiliza e não avisa;  Os parâmetros de período de contabilização como “Linearização” devem ser herdados do contrato de locação associado. |
| Rescisão | Efetivar | Verificar se há evento contábil associado ao processo de Rescisão,  se:  **SIM**: dispara contabilização;  **NÃO**: não contabiliza e não avisa; |

*Novos processos e ações poderão ser incluídos ou alterados em tempo de projeto e depois da liberação do recurso no mercado, afim de obter melhor resultado.*

O disparo da contabilização em certos processos será determinado por parametrização que será detalhada na especificação técnica, mas se não houver evento contábil associado a contabilização não será realizada.

 Em todos os Recursos aptos a contabilização serão disponibilizados os processo: **Incluir Lançamento Contábil, Estornar Lançamento Contábil, Excluir Lançamento Contábil e Solicitar Tarefas;**

 Estas opções são alternativas para quando o processo de contabilização apresentar algum problema, como falta de dados ou mesmo valores incorretos, ou para contabilizações não automáticas ( “off line”);

 Na visão do Contrato de Locação deve haver no menu de “Anexo” a opção de visualizar Lançamentos Contábeis. A apresentação como anexo se justifica pelo fato de que um mesmo contrato de locação pode gerar vários lotes de contabilizações em diferentes processos. Cada mês gera um código de operação contábil distinto (IDOperação). Caso o lançamento seja estornado e um novo lançamento seja criado o identificador da operação contábil permanece o mesmo. Serão apresentado apenas os lançamentos válidos, ou seja, não serão apresentados os estornos e estornados.

 A contabilização poderá disparada automaticamente conforme parâmetros por coligada ou opções de contabilização manual via processo anexo a visão do contrato de locação ou pelo menu geral contabilização Global.

# Estorno e Exclusão Contábil

De acordo com o Conselho Federal de Contabilidade:

|  |
| --- |
| *“Retificação de lançamento contábil*  *31. Retificação de lançamento é o processo técnico de correção de registro realizado com erro na escrituração contábil da entidade e pode ser feito por meio de:*  *a) estorno;*  *b) transferência; e*  *c) complementação.*  *32.Em qualquer das formas citadas no item 31, o histórico do lançamento deve precisar o motivo da retificação, a data e a localização do lançamento de origem.*  *33. O estorno consiste em lançamento inverso àquele feito erroneamente, anulando-o totalmente.*  *34. Lançamento de transferência é aquele que promove a regularização de conta indevidamente debitada ou creditada, por meio da transposição do registro para a conta adequada.*  *35. Lançamento de complementação é aquele que vem posteriormente complementar, aumentando ou reduzindo o valor anteriormente registrado.*  *36. Os lançamentos realizados fora da época devida devem consignar, nos seus históricos, as datas efetivas das ocorrências e a razão do registro extemporâneo.*  *Em razão dessa alteração, as disposições não alteradas desta Interpretação são mantidas e a sigla da ITG 2000, publicada no DOU, Seção 1, de 22.3.11, passa a ser ITG 2000 (R1).*  *A alteração desta Interpretação entra em vigor na data de sua publicação.”*  *Fonte ITG 2000 (R1) – ESCRITURAÇÃO CONTÁBIL* |

O **Estorno** contábil é um processo de correção e deve ser feito quando houver falha na escrituração contábil, ou se houver um cancelamento do fato gerador.

 Já a **exclusão** dos lançamentos contábeis ocorre enquanto o período ainda está em aberto e os lançamentos não foram integralizados (lote zero linha RM), desta forma ainda não houve registro formal do lançamento permitindo que o sistema corrija erros técnicos ou humano como erro de digitação ou erro sistêmico. A exclusão do lançamento contábil não afeta seu fato gerador (*ex. Contrato de locação, lançamento financeiro, etc.).*

Caso o lançamento esteja integralizado é possível excluir os lançamentos contábeis através do recurso de **Solicitação de Tarefa**, que permite a alteração de contabilização mesmo em lotes integralizados, desde que autorizado pelo usuário responsável (contador) e o período não esteja fechado.

Se Não for possível excluir os lançamentos devem ser **estornados** justificando o motivo (histórico).

*No Sistema Contábil (linha RM ou Protheus) os lançamentos de estorno são feitos para anular a contabilização "original" invertendo as partidas, o status do lançamento original fica com I (Incorreto) e o lançamento de estorno ficará com status = E (Estorno) se for gerada uma nova contabilização a nova partida terá o status = C (correto).*

Para estornar o lançamento será apresentada a tela com defaults que podem ser alterados, e nela deve constar a data, histórico padrão e complemento.

# Rescisão Contratual

A rescisão contratual indica o termino antes do período previsto e portanto pode gerar efeitos contábeis como:

* Se o cliente já tiver provisionado períodos superiores a data de rescisão

Deverá excluir tais provisões;

* Se houver devolução por parte do cliente

Deverá provisionar os novas receitas do cliente;

* Se houver devolução por parte da Empresa

Deve provisionar despesas ou reduções de receitas

 Neste contexto o sistema deve permitir:

* gerar lançamentos contábeis com data superior a rescisão se for de evento contábil de rescisão.
* não deve permitir o disparo de contabilizações ou re-contabilizações de períodos superiores a data de encerramento ou rescisão.

# Descontos

Podem ser aplicados dois tipo de Descontos, o Desconto Comercial e o Desconto Financeiro.

**O Desconto Comercial** é aplicado no Contrato de Locação, sendo incondicional e causando alteração no valor original de cada cobrança. Ainda no Contrato de Locação pode ser feito o desconto por escalonamento, ou seja uma redução no valor do contrato por período determinado e sobre este valor ser aplicado mais um percentual ou valor de desconto, mesmo nestas situações permanecem incondicionais e com impacto no valor original da cobrança. Por ser um desconto incondicional afeta a base de cálculo de impostos que incidem sobre a receita sendo, portanto, redutor de receita, assim na contabilidade deve ser registrado em conta contábil específica.

O **Desconto Financeiro** pode ser condicionado a uma determinada situação, como por exemplo, pagamento em dia ou antecipado sendo tratado pelo módulo financeiro.

###
