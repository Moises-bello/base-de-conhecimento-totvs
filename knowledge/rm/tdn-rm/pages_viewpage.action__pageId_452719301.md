---
content_hash: b84debefdbe76ddc6dce48608af4e456b6a797e745f0d45a0a12e2386ddd55ac
fetched_at: '2026-06-29T00:10:05.738780+00:00'
page_id: '452719301'
product: rm
source: tdn-rm
title: Importação de batidas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719301
version: 47
---

O sistema TOTVS Automação de Ponto realiza o registro de marcações por meio do processo de Importação de Batidas. Para isso, as informações são extraídas das seguintes fontes de dados:

* Arquivo de Fonte de Dados ([AFD](https://tdn.totvs.com/display/LRM/Arquivo+Fonte+de+Dados+Tratado));
* Integração com [TSA/Suricato](https://tdn.totvs.com/pages/viewpage.action?pageId=244424906);
* Integração com a [Carol](https://tdn.totvs.com/pages/releaseview.action?pageId=441821303);
* Importação via [API](https://tdn.totvs.com/pages/viewpage.action?pageId=682054374):

ParâmetrosParâmetrosUtiliza Integração com o TSA

[Documentação](https://tdn.totvs.com/pages/viewpage.action?pageId=244424906)

**Ao utilizar a integração com o TSA, será possível [Importar batidas integradas via API.](https://tdn.totvs.com/pages/viewpage.action?pageId=682054374)**

Utiliza integração com a Carol

[Documentação](https://tdn.totvs.com/pages/releaseview.action?pageId=441821303)

Arquivo para importação

Nesse campo deve constar o caminho e nome do AFD de importação que deve ser do tipo texto (.txt), para que o sistema o leia no momento da importação.

Caso esteja utilizando a importação automática, informe o caminho de rede do arquivo, no qual deverá estar compartilhado. Exemplo: \\servidor\batidas.txt

Esse arquivo é gerado pelo equipamento de registro de ponto, nele são registradas as batidas dos funcionários.

O arquivo consumido pode utilizar:

* Layout customizável: faz referência à chapa ou ao código do crachá, esse último deve estar associado ao funcionário.
* Layout AFD da [Portaria 1.510/2009](https://tdn.totvs.com/pages/viewpage.action?pageId=452719378): faz referência apenas ao PIS.
* Layout AFD da [Portaria 671/2021](https://tdn.totvs.com/pages/viewpage.action?pageId=694109664): faz referência ao PIS/CPF do funcionário.
  + [Adequação da Portaria 671](https://tdn.totvs.com.br/pages/viewpage.action?pageId=795930155)

Para isso é necessário uma correta parametrização dos [Terminais de coleta](https://tdn.totvs.com/display/LRM/Terminais+de+Coleta) e do [Layout de relógio](https://tdn.totvs.com/pages/viewpage.action?pageId=452718923). Esse último, quando criado no sistema, deve estar precisamente de acordo com o arquivo que será gerado pelo Relógio de Ponto Eletrônico. 

Qualquer inconformidade estrutural na linha do arquivo gerará um alerta no log (warning) ou interrompe o processamento do registro correspondente.

Layout do relógio

**[Documentação](https://tdn.totvs.com/pages/viewpage.action?pageId=452718923)**

Períodos para importação

As batidas serão importadas do arquivo de acordo com o período informado na tela de importação de batidas.

O sistema sugere o período de importação conforme o período atual e ativo, também é possível definir livremente o início e fim da importação. 

Será permitido realizar a importação de Batidas utilizando  [Agendamento Por Período - Semanal, Quinzenal, Mensal e últimos dias](https://tdn.totvs.com/pages/viewpage.action?pageId=1052327757)

Terminal de coleta para histórico

[Documentação](https://tdn.totvs.com/display/LRM/Terminais+de+Coleta)

Acerta Natureza

A natureza da batida é uma informação fundamental para o cálculo da movimentação, caracterizando-a como uma entrada ou saída. No momento da importação o sistema precisa decidir a natureza de cada uma para ser registrada, lembrando que para cada batida de entrada deve existir uma batida de saída. E para tratar as adversidades e relações dessas batidas com a jornada planejada, o sistema disponibiliza algumas opções para acerto da natureza.

Se nenhum parâmetro for marcado para acerto de natureza, o sistema atribuirá à batida importada a natureza oposta à da batida anterior, e assim sucessivamente.

Ao selecionar “Considerando o horário planejado” ou “Considerando a jornada” é feito um cálculo para identificar a qual índice da jornada planejada a batida a ser importada está mais próxima antes de aplicar a natureza, visto que pode existir batidas fora do planejado. 

**Exemplo**

Horário vinculado ao funcionário:

01/01/2025   Índice 1: 08:00 as 14:00 – Trabalho   
 02/01/2025   Índice 2: 00:00 as 23:59 - Compensado

Batidas a serem importadas: 

 01/01/2025 13:00;

 01/01/2025 19:10;

As batidas em questão não pertencem ao mesmo índice. Ao aplicar o cálculo a batida das 19:10 está mais próxima do índice 2 e a batida das 13:00 mais próxima do índice 1. 

TiposConsiderando o período

A primeira batida do período a ser importada, não levará em consideração a última batida do período anterior, ou seja, o sistema calculará a natureza verificando se existe batida menor que a batida a ser importada somente no período, caso exista a natureza será a contrária da batida anterior. Caso não encontre nenhuma batida no período, o sistema calculará a natureza pela proximidade da natureza do horário planejado, assim como é feita a importação considerando o horário planejado.

Considerando o horário planejado

A importação levará em consideração o horário planejado no dia, ou seja, o horário cadastrado para o funcionário. O sistema calculará a natureza pela proximidade da natureza  com os  intervalos do horário planejado. Se no horário estiver cadastrado como saída a primeira batida do dia, esta será importada como saída.

**Exemplo:**

Se já existe a batida em vermelho, a importação será feita da seguinte maneira:

    
 

Considerando a jornada

O sistema calculará a natureza das batidas conforme a jornada(s) planejada(s) do funcionário. Ao invés de considerar a proximidade da natureza, é considerada a proximidade da jornada planejada. Tratando situações em que o funcionário tem mais de uma jornada planejada no dia, ou mesmo, funcionários que possuem jornada de um dia para o outro.  
  
**Exemplo:**  
Para situações em que o funcionário possui duas jornadas planejadas na mesma data conforme abaixo:   
  
   
Se já existe a batida em vermelho, a importação será feita da seguinte maneira:

Não altera a natureza das batidas que ultrapassem\_\_:\_\_ hsr

Caso esse tenha um valor diferente de zero horas, ele será usado para calcular se a batida importada manterá a mesma natureza da anterior.

Considera Natureza Fixa

Será fixado a Natureza da Batida como Entrada ou Saída, quando for ultrapassado o tempo mínimo entre as batidas parametrizado pelo usuário ou não houver batidas até 3 dias anteriores.  
Este parâmetro somente será habilitado caso o parâmetro 'Acerta Natureza Considerando o Período' estiver marcado, e o campo 'Não altera a natureza das batidas que ultrapassem xx:xx hrs' estiver preenchido.

Utilizando este parâmetro, a importação será feita em apenas um lote para ordenação das batidas, independente da quantidade de marcações, o que poderá onerar a performance. 

Prioriza crachá e não chapa para importação de batidas

Na importação de arquivo utilizando layout customizável, ao marcar esse parâmetro o sistema passa a considerar o crachá associado ao funcionário para importação. Caso a batida a ser registrada não estiver dentro do período de utilização do crachá, a mesma não será importada.  
Ao realizar a importação considerando o crachá e na base de dados tiver um crachá onde seu código for igual a uma chapa de funcionário, o sistema importará batida apenas para o funcionário que estiver associado ao crachá.  
Caso o layout do relógio contemple o terminal de coleta, a importação validará a utilização desse terminal pelo funcionário. O terminal pode ser associado para o funcionário através do processo ['Alterações Globais de Terminais de Acesso'](https://tdn.totvs.com/pages/viewpage.action?pageId=452719869).  
Caso o layout do relógio contemple [funções](https://tdn.totvs.com/pages/viewpage.action?pageId=452719507), o sistema desconsidera as opções para acerto de natureza e considera apenas os tratamentos das funções de relógio.

Considera a última linha importada

Esse parâmetro deve ser utilizado para a importação automática de batidas.

Executa recálculo do funcionário após importação

Ao selecionar esse parâmetro, após a importação, será executado o [processo de cálculo do ponto](http://Movimento- Calcular) utilizando o mesmo filtro de funcionário, considerando a seguinte parametrização:

A partir da release 12.1.2606, o parâmetro "Executa recálculo do funcionário após importação" só estará disponível para a seleção se o usuário tiver a permissão “[03.01.01] Calcular” habilitada.

Se um usuário não tiver a permissão necessária, mas selecionar um perfil de parâmetros que tenha a opção "Executa recálculo do funcionário após a importação" habilitada, a opção no menu aparecerá marcada e desabilitada, impedindo qualquer edição. Mesmo assim, o cálculo após a importação não será realizado, pois o usuário não possui a permissão necessária.

Exibe informação de inatividade do funcionário no log

Os funcionários de férias ou afastados terão suas batidas importadas normalmente, porém, ao fim do processo será apresentado um aviso para as datas que o funcionário deveria estar ausente.  
  
**Exemplo**  
Funcionário '00001' não está ativo na data 26/04/2010. Motivo Tipo Inatividade: AtestadoFolha - Descrição: Acidente grave no trabalho!

Funcionário com Múltiplos Vínculos

Durante a importação de marcações, caso o funcionário possua múltiplos vínculos, o sistema pode utilizar a aproximação por horário para definir a chapa correta. Esse processo contempla dados provenientes de Arquivo, TSA e Carol.

Inicialmente, ao processar as informações, o sistema gera uma lista com todas as chapas vinculadas ao PIS/CPF da marcação, independentemente da coligada, organizando-as de forma crescente pelo valor da chapa. Para definir qual das chapas receberá a marcação, são aplicados critérios eliminatórios em sequência.

A análise do sistema prossegue para a próxima etapa de validação apenas se restar mais de uma chapa na lista, quando restar apenas uma chapa, essa será associada à aquela marcação.

 Sequência de Validações Detalhada

Casos em que a chapa é removida da lista

1. Valida se a data da batida está no período admitido da chapa:
   * Data da marcação anterior à admissão,
   * Em casos de desligamento, se é posterior à data de demissão.
2. Verifica se está ativo o uso do cartão de ponto, para a chapa na data da marcação ou período definido da importação:
   * Sem data de importação definida: No dia específico da batida não utiliza cartão de ponto.
   * Com data de importação definida: Não utiliza cartão de ponto em algum momento durante o período da importação.
3. Caso o CPF seja de um funcionário professor (vínculos integrados ao TOTVS Educacional), é verificado para qual jornada de aulas planejadas a batida é compatível:
   * O parâmetro “Considera horário planejado do Chronus para o professor” na parametrização do funcionário está ativo e a chapa NÃO está integrada ao Módulo Educacional.
   * O horário da marcação não se enquadra no intervalo do horário de trabalho da chapa.

     Exemplo

     Um professor possui três chapas sob o mesmo CPF, chapa: C1, C2, C3.

     Esse CPF está parametrizado para usar horário de professor.

     A chapa C3 não está integrada ao RM Educacional.

     A batida não está dentro do intervalo do horário planejado da chapa C2 e fora do intervalo planejado da chapa C1.

     Dessa maneira a chapa C1 é removida da lista.

     O processo define a chapa restante “C2” como associada à aquela marcação, não sendo necessário realizar mais validações para definição de chapa pois restou apenas uma.
4. Caso a importação utilize Layout do Relógio será verificado quais chapas estão associadas à aquela coligada, se a coligada do relógio não corresponder a nenhuma das chapas, nenhuma chapa é removida da lista.

   Caso em que a chapa é removida da lista:

   * Uma ou mais chapas possuem a coligada igual a coligada do Layout de Relógio definido na importação e a chapa analisada possui a coligada diferente da coligada do layout.
5. É realizada a análise dos horários planejados associados às chapas, onde é verificada a escala mais aderente ao horário da marcação, por aproximação do horário planejado, caso os horários de uma chapa ou mais possua(m) a mesma distância da marcação, aquela/todas chapa(s) permanece(m) na lista.

         Caso em que a chapa é removida da lista:

1. * A jornada da chapa é mais distante do horário da marcação.

     Exemplo

     Considerando que os dois funcionários utilizam o mesmo PIS/CPF, a batida de 14:10h a ser importada será registrada para o funcionário 2.
2. Como último recurso, caso a lista possua mais de uma chapa, o sistema associa por padrão a primeira chapa da lista à aquela marcação.

Fluxograma

trueImportacaoCPFfalseautotopFluxogramatrue9141

Funcionalidades

* **Importar Batidas para visitantes:**  
  O TOTVS Automação de ponto permite o controle de visitantes na empresa, possibilitando a manutenção de batidas e as refeições. A importação de batidas para os visitantes é feita a partir do crachá associado.

* **Importar Batidas de Refeição:**  
  O sistema identifica as batidas de refeição pelo terminal de coleta ou pela função de relógio. As batidas de refeição são importadas para a pasta refeição no cadastro do funcionário ou visitantes. Essa funcionalidade é utilizada apenas pelas empresas que possuem refeitório e querem descontar a refeição do funcionário. A importação de batidas de refeição depende do cadastramento das refeições e do terminal de coleta de refeição.

* **Importação automática de batidas:**  
  É possível automatizar a importação de batidas, no qual o sistema efetuará o recolhimento automático das batidas dos arquivos gerados pelo relógio (o relógio deverá gerar automaticamente o arquivo). A partir de agora o agendamento de processos dos serviços globais é utilizado para programar a importação de batidas. As configurações para importação são realizadas normalmente, deve-se utilizar o parâmetro 'Considera a última linha importada', e em uma segunda etapa o agendamento dessa importação é realizada conforme o [Gerenciamento de Jobs](https://tdn.totvs.com/pages/viewpage.action?pageId=452719301).

* [Importação da Justificativa da Falta](https://tdn.totvs.com/pages/releaseview.action?pageId=674908037)
Ferramentas

Para facilitar a gestão e conferência das importações realizadas o sistema disponibiliza as ferramentas abaixo: 

* [Histórico de importações](https://tdn.totvs.com/pages/viewpage.action?pageId=452719001)
* [Log da importação](https://tdn.totvs.com/pages/viewpage.action?pageId=452719988)
* [Memória da importação](https://tdn.totvs.com/pages/viewpage.action?pageId=452719990)
Observações

1. O processo de cálculo não deve ser executado simultaneamente à compensação do banco de horas, mesmo que o parâmetro “Calcula funcionários com alterações manuais” esteja desmarcado, pois o contexto do recálculo será carregado antes da compensação conseguir bloquear o movimento do funcionário, e por consequência, o recálculo irá desfazer a compensação/lançamento de banco de horas.
2. Caso o funcionário esteja bloqueado, por exemplo devido ao bloqueio de funcionário com alterações manuais em sua movimentação, a importação não será realizada.
3. O processo de importação de marcações respeitará as parametrizações do  [funcionário](https://tdn.totvs.com/pages/viewpage.action?pageId=452719472) e [sindicato](https://tdn.totvs.com/display/LRM/Sindicato).

HelpWiki - RH - Automação de Ponto
