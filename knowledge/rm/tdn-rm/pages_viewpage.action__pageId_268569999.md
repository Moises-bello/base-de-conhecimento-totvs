---
content_hash: 613a7de864cf8bf1bba5914f7f1f2a966b249f872953e49253bb3e55ee7d79e4
fetched_at: '2026-06-29T00:08:20.127645+00:00'
page_id: '268569999'
product: rm
source: tdn-rm
title: TVJULV_DT_ECF_Automatismo_Lançamentos_Lalur_B
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268569999
version: 10
---

# ECF - Escrituração Contábil Fiscal

# Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Fiscal* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *ECF* | *Escrituração Contábil Fiscal* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Contas* | *Cadastro Contas Lalur parte B* | | *Lançamentos* | *Cadastros de Lançamentos Lalur parte B* | | *Encerramento* | *Encerramento do Período de Apuração* | | *Evento Tribuário* | *Cadastro do Evento Tributário* | |
| **Cadastros Iniciais:** |  |
| **Parâmetro(s):** | *Não se Aplica* |
| **Ponto de Entrada:** | *Não se Aplica* |
| **Chamados Relacionados** | *TVJULV* |
| **Requisito (ISSUE):** | *FIS000428* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server; Oracle* |
| **Tabelas Utilizadas:** | DPERIODO; DCONTAINFORMACAO; DPROCJUDEVCTRB;  DCONTALALURB; DITMEVCTRB; |
| **Sistema(s) Operacional(is):** | Windows |

# **Legislação**

[Link da Legislação](http://tdn.totvs.com/pages/viewpage.action?pageId=268570059)

# **Implementações**

Após os estudos dos controles que são necessários na Parte B, identificamos dois possíveis automatismos:

* Automatismos na **constituição de saldo** na conta da Parte B do Lalur e
* Na **utilização de saldo** da conta da Parte B do Lalur na apuração do lucro real.

A constituição de saldo em conta da Parte B do Lalur para posterior adição ou exclusão, seja em conta existente ou em nova conta, pode ser proveniente de lançamentos de adição e/ou exclusão realizados na Parte A do Lalur.

Regras:

* Se o valor a ser controlado na Parte B for proveniente de uma Adição na Parte A  
   - A conta da Parte B terá natureza de “**Exclusão**”.

* Se o valor a ser controlado na Parte B for proveniente de uma Exclusão na Parte A  
  - A conta da parte B terá Natureza de “**Adição**”.

* Se for referente à Prejuízo apurado no período  
  - A conta da parte B terá Natureza de “**Prejuízo Fiscal**”.

Neste caso, é preciso identificar o Código do lançamento (tabela dinâmica do Registro M300/M350 da ECF) que originou a conta da Parte B.

# **Cadastros Contas\Lançamentos Lalur Parte B**

## **Conta da Parte B do Lalur**

Menu: RM\Gestão Fiscal\Obrigações Principais\Lalur Parte B\Contas\Anexos\Informações Fiscais

Foi criado o anexo Informações Fiscais e incluído neste anexo o campo "CNPJ da pessoa jurídica relacionada"

* **CNPJ da pessoa jurídica relacionada**: Neste campo deve ser informado o CNPJ da outra pessoa jurídica envolvida no evento que originou a conta, por exemplo, CNPJ da investida, da antecessora, etc.

Esse campo será utilizado para gerar o campo 11 do Registro M010: “CNPJ\_SIT\_ESP - CNPJ da outra pessoa jurídica relacionada com evento originário da conta”.

Menu: RM\Gestão Fiscal\Obrigações Principais\Lalur Parte B\Contas\Pasta Tributos\

Inclusão de novo campo no cadastro:

* **Código da Tabela Dinâmica da ECF** (pasta Tributos): Este campo terá lookup para o Cadastro da Tabela Dinâmica da ECF. Deve ser informado nesse campo o código do lançamento na parte A do e-Lalur e/ou do e-Lacs que deu origem à conta.

Essa informação será utilizada para gerar os campos 5 (Código do Lançamento de origem) e 6 (Descrição do lançamento de origem) do Registro M010 - IDENTIFICAÇÃO DA CONTA NA PARTE B DO e-LALUR E DO e-LACS na rotina da ECF.

## **Lançamentos da Parte B do Lalur**

Menu: RM\Gestão Fiscal\Obrigações Principais\Lalur Parte B\Lançamentos\Pasta Processos Judiciais e Administrativos\

Criar **Anexo** no Lançamento da Parte B do Lalur com lookup para o **Cadastro de Processo Judicial e Administrativo** onde o usuário deverá informar todos os processos judiciais ou administrativos que embasaram movimentações na parte B do e-Lalur ou do e-Lacs com tratamento diverso das regras fiscais. Cada processo associado ao Lançamento deve gerar um Registro M415 na ECF.

**IMPORTANTE!**

Esse Anexo deve ser utilizado apenas para os valores que **NÃO** afetam a Parte A, ou seja, somente para deduções\compensações do tributo. Nos demais casos, adições, exclusões e compensação de prejuízo, o Processo Judicial/Administrativo deve ser informado no Item Tributário, dentro do Evento Tributário.

**Implementar Recurso “Replicar lançamento para a CSLL”**

Ao salvar o lançamento na conta da Parte B para o tributo do Tipo “IRPJ”, perguntar ao usuário se ele deseja replicar o lançamento para o tributo do Tipo “CSLL”.

O usuário respondendo “Sim” o sistema deve criar outro lançamento com os mesmos dados alterando apenas o **Tributo**.

**IMPORTANTE!**

Esse recurso só deve existir na inclusão. Na edição não deve ser apresentado para evitar duplicidade de lançamentos.

**Implementação do Processo: “Lançamentos Lalur B em Lote”**

Menu: RM\Gestão Fiscal\Obrigações Principais\Lalur Parte B\Contas do Lalur Parte B\Processos\Inclusão de Lançamentos Lalur B em Lote

Este processo possui o objetivo de incluir vários lançamentos de uma única vez, quando os mesmos possuírem as mesmas características, alterando apenas a Data e/ou o Valor.

Este processo só pode ser executado para uma conta de cada vez em função das particularidades de cada conta (tributos envolvidos, período, valor etc.).

Na execução do processo, o usuário deve preencher as seguintes informações:

1. **Tributo** (obrigatório) – Se houver apenas um tributo associado à conta o sistema preenche o tributo automaticamente, como já é feito atualmente para os lançamentos manuais.
2. **Centro de Custo**.
3. **Intervalo** (obrigatório) – Informar a data inicial e final dos lançamentos. Faz-se necessário que os períodos de apuração que compreende o intervalo estejam com status “**Aberto**”.
4. **Periodicidade** (obrigatório) – Contendo as opções “**Mensal**” e “**Trimestral**”. O sistema deve inserir um lançamento por mês ou trimestre dentro do intervalo informado pelo usuário, sempre no último dia do período.
5. T**ipo de Valor** (obrigatório) – Contendo as opções: **Valor Fixo** – Para esta opção apresentar campo para preenchimento do valor; **Quotas fixas** – Nesta opção, o sistema irá dividir o saldo atual da conta em parcelas iguais dentro do período informado.
6. **Valor** – Deve ser apresentado e preenchido se o “Tipo de Valor” for “**Valor fixo**”.
7. **Tipo do Lançamento** (obrigatório) - Contendo as opções: Débito; Crédito; Constituição de Saldo
8. **Realização de Valores diferidos** (obrigatório) – Contendo as opções: Sim; Não
9. **Histórico**

**IMPORTANTE**!

O saldo atual da conta deve considerar todos os lançamentos já realizados.

**Fornecer a possibilidade de replicar lançamentos para o tributo CSLL:** Para replicar os lançamentos para o tributo CSLL que estiver associado à conta da Parte B, basta selecionar o tributo CSLL na caixa "Replicar lançamentos para o tributo CSLL" na tela dos parâmetros do processo então serão gerados os lançamentos lalur b exatamente com os mesmos dados do tributo IRPJ, alterando apenas o Tributo.

Na execução do processo, o sistema deve criar os lançamentos para a conta selecionada de acordo com as informações preenchidas pelo usuário com a “**Origem**” do lançamento como   “**Manual**”.

Este processo deve executar as mesmas regras de consistência que já existem hoje para o lançamento manual: período de apuração deve estar aberto, o saldo da conta deve suportar o valor do lançamento, etc. Caso haja algum lançamento a ser realizado que não satisfaça alguma das consistências, o sistema deve apresentar o mesmo no log e prosseguir com os demais.

*Exemplo:**Inserir lançamentos mensais a débito para a conta “01.001” no período de 01/01/2016 à 31/12/2016 para o tributo IRPJ. Supondo que o mês de Janeiro/2016 esteja encerrado, o sistema deve inserir os lançamentos de fevereiro à dezembro e mostrar no log que não conseguiu incluir o lançamento de janeiro porque o período de apuração estava encerrado.*

Na aba “Processos Judiciais/Administrativos” o usuário deverá informar todos os processos judiciais ou administrativos, caso existam, que embasam os lançamentos que serão criados na parte B do e-Lalur ou do e-Lacs com tratamento diverso das regras fiscais, conforme descrito no Item 2.1.2, abaixo.

Observação: Esta pasta só deve ser exibida quando a conta selecionada for de Natureza “**Dedução/Compensação de Tributo**”.

# **Cadastro Evento Tributário**

Menu: RM\Gestão Fiscal\Obrigações Principais\Eventos Tributários\Estrutura\Pasta Regras Tributárias\Item do Evento Tributário

Pasta “Efeito na Parte B”

Deve ser criado a pasta “**Efeito na Parte B**” que deve ser apresentada quando a Origem da Informação for “**Contábil**” e apenas para os Grupos de Adições do Lucro, Adições por Doação e Exclusões do Lucro.

Esta pasta deve conter os seguintes campos:

* **Efeito na Parte B do Lalur**, com as opções:
  + Não se aplica
  + Constituir saldo da Conta
  + Baixar saldo da Conta

* **Conta da Parte B do Lalur** - Campo não obrigatório contendo a conta da Parte B que será afetada pelo valor processado para o Item Tributário e que receberá o respectivo lançamento.

Regras:

* Nos Grupos de Adições do Lucro e Adições por Doação:
  + Se o efeito for “**Constituir saldo na Conta**”, devem ser apresentadas somente contas da Parte B com natureza de “**Exclusão**”.
  + Se o efeito for “**Baixar saldo da Conta**”, devem ser apresentadas somente contas da Parte B com natureza de “**Adição**”.

* No Grupo de Exclusões do Lucro:
  + Se o efeito for “**Constituir saldo na Conta**”, devem ser apresentadas somente contas da Parte B com natureza de “**Adição**”.
  + Se o efeito for “**Baixar saldo da Conta**”, devem ser apresentadas somente contas da Parte B com natureza de “**Exclusão**”.

Flag “Gerar Lançamento automático”

No Grupo “**Compensação de Prejuízo/BC Negativa**” criar o campo “**Gerar lançamento automático no encerramento**” na pasta Dedução/Compensação.

 Hoje, o sistema simula o valor da compensação do prejuízo baseado no percentual limite informado para o Item Tributário. Após simular, o usuário precisa sair do Evento, acessar a conta da Parte B e incluir o lançamento manual para que o valor seja considerado na apuração. Com o novo campo marcado, o lançamento de baixa do saldo do prejuízo será feito automaticamente pelo sistema durante o encerramento do período.

Ainda na pasta “Dedução/Compensação” permitir ao usuário informar o valor “100” no campo “Percentual”, para que a geração automática do lançamento da compensação no encerramento atenda à atividade rural que permite compensar 100% do lucro.

Pasta “Processos Judiciais/Administrativos”

Deve ser criado uma pasta no Item Tributário com lookup para o Cadastro de Processo Judicial e Administrativo onde o usuário deverá informar todos os processos judiciais ou administrativos que embasaram movimentações na parte A do e-Lalur ou do e-Lacs com tratamento diverso das regras fiscais.

Cada processo associado ao Item Tributário deve gerar um Registro M315 (IRPJ) ou M365 (CSLL) na ECF.

# **Apuração**

Processo “Gerar Lançamentos Automáticos (Efeitos na Parte B)”

Menu: RM\Gestão Fiscal\Obrigações Principais\Período de Apuração\Processos\Gerar Lançamentos Automáticos (Efeito na Parte B)

Criar Processo no Período de Apuração, para inclusão automática dos lançamentos na Parte B do Lalur, tendo como origem os itens tributários que possuem um efeito na Parte B parametrizado para constituir ou baixar saldo na conta da Parte B do Lalur e, também, o valor do Prejuízo Fiscal apurado no período.

Ao executar o processo o sistema deve apresentar uma grid contendo uma lista com os itens do Detalhamento da Apuração cujo Item Tributário correspondente tenha um efeito informado e, também, para os prejuízos apurados no período, se for o caso.

Nessa grid, caso a conta da Parte B que receberá o lançamento tenha sido informada no Item Tributário, será apresentada automaticamente. Se não houver conta da Parte B informada no Item Tributário, o sistema deve apresentar no campo correspondente um lookup para o Cadastro de Contas da Parte B para que o usuário selecione e/ou crie a conta.

A grid deve conter as seguintes colunas:

**Efeito**: Constituição de Saldo ou Baixa de Saldo. Essa informação está no Item Tributário correspondente.

**Conta Lalur**: Trazer como default a conta associada ao efeito no Item Tributário correspondente. Apresentar o lookup para o Cadastro de Contas da Parte B.

**Tipo do Lançamento**: Débito, Crédito ou Constituição de Saldo. Regras:

* Se o Efeito for “**Constituir saldo na Conta**”, o Tipo será “**Constituição de Saldo**”.
* Se o Efeito for “**Baixar saldo da Conta**”:

Nos Grupos de **Adições do Lucro** e **Adições por Doação**, o Tipo será “**Débito**”

* No Grupo de **Exclusões** do Lucro, o Tipo será “**Crédito**”.
* Para lançamentos dos prejuízos apurados no período o Tipo será “**Constituição de Saldo**”.

Valor processado para o Item Tributário e que foi gravado no Detalhamento da Apuração ou o valor do prejuízo apurado no período (Período de Apuração, pasta Detalhamento).

* **Código da Tabela Dinâmica da ECF**: Código da ECF que está informado no Item no Detalhamento da Apuração.
* **Descrição do Código da Tabela Dinâmica da ECF**.

**Observação:** O único campo editável da grid do Processo será a Conta da Parte B do Lalur.

O preenchimento dos campos do lançamento na conta da parte B deve seguir às seguintes regras:

* **Conta Lalur Parte B**: receberá a conta que foi informada na grid do Processo.

* **Tributo**: deve receber o tributo que está associado ao Período de Apuração.

* **Histórico**: preencher com o texto quando for:

1. **Constituição de saldo**: “*Constituição de saldo da conta referente lançamento de* (colocar o nome do Grupo onde está o item tributário) *referente à* (descrição do código da tabela dinâmica da ECF associado ao item tributário)”.
2. **Baixa de saldo**: “*Baixa de saldo da conta referente lançamento de* (colocar o nome do Grupo onde está o item tributário) *referente à* (descrição do código da tabela dinâmica da ECF associado ao item tributário)”
3. **Prejuízo Apurado no Período**: *“Prejuízo Fiscal/Base de Cálculo Negativa* (Operacional ou Não Operacional) *apurado(a) no período.”.*

* **Data**: receberá a data final do período de apuração.

* **Valor**: valor processado e gravado no Detalhamento da Apuração ou o valor do prejuízo do período de apuração.

* **Id. Detalhamento da Apuração:** deve ser preenchido com o identificador do detalhamento da apuração equivalente ao item do Evento Tributário que foi processado.

**EXEÇÃO!** Esse campo **NÃO** deve ser preenchido para o lançamento do prejuízo do período porque o lançamento precisa ser gerado no Registro M410 da ECF.

Regras do Processo:

* O Período de Apuração deve estar “Encerrado”.
* Esse processo só poderá ser executado para um Período de Apuração por vez.
* Ao reabrir o Período de Apuração, o sistema deve apagar os lançamentos que foram inseridos de forma automática para aquele período (verificar pela Data do Lançamento).

**IMPORTANTE**

Na apuração pelo Lucro Real Anual, deve-se atentar para não duplicar a parametrização do automatismo proposto neste documento no Evento Tributário que será utilizado para encerrar o Período de Apuração do ajuste anual. Realizar essa parametrização, tanto no Evento Tributário das Estimativas mensais como no Evento Tributário do ajuste anual irá duplicar todos os valores nas contas visto que os valores foram lançados mensalmente.

Lançamento automático da Compensação de Prejuízos/BC Negativa

Menu: RM\Gestão Fiscal\Obrigações Principais\Período de Apuração\Processos\Encerramento Período

Quando o novo campo “**Gerar lançamento automático no encerramento**” estiver marcado no Item Tributário, no encerramento do período de apuração o sistema deve inserir um lançamento automático na Parte B do Lalur, considerando as seguintes regras:

* **Conta Lalur Parte B**: receberá a conta associada ao Item Tributário que está sendo processado.
* **Tributo**: deve receber o tributo que está sendo apurado e que também está informado no Evento Tributário.
* **Histórico**: preencher com o texto “*Compensação de Prejuízos Fiscais apurados em Períodos Anteriores.*”
* **Data**: receberá a data final do período de apuração que está sendo encerrado.
* **Valor**: o valor do prejuízo que foi calculado pela simulação com base no limite de dedução que foi informado para o Item Tributário.

**IMPORTANTE**

Na apuração do lucro real anual, a apuração é acumulativa. O sistema desconsidera todos os lançamentos já realizados e calcula um novo valor, na simulação. Para efetuar o lançamento automático, ele precisa, no entanto, considerar o valor total já lançado na conta e efetuar lançamento apena da diferença: a maior à Crédito na conta e a menor, à Debito na conta.

Exemplo:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Valor limite da compensação (acumulado)** | **Valor acumulado até o mês anterior** | **Diferença** | **Tipo do Lançamento** |
| **Janeiro/x1** | 100,00 | 0 | 100,00 | Crédito |
| **Fevereiro/x1** | 180,00 | 100,00 | 80,00 | Crédito |
| **Março/x1** | 150,00 | 180,00 | (30,00) | Débito |

* **Tipo**: Crédito ou Débito (ver informações acima).
* **Id. Detalhamento da Apuração:** deve ser preenchido com o identificador do detalhamento da apuração equivalente ao item do Evento Tributário que foi processado.

Se existir mais de uma conta de prejuízo informada no Grupo, o sistema deve processar da mais antiga para a mais nova, considerando a Data de Início da vigência da conta.

# **ECF - Escrituração Contábil Fiscal**

Menu: RM\Gestão Fiscal\Obrigações Acessórias\Gerador Saídas\Layout ECF

- Incluir nos Registros M300 os registros Referentes aos  processos Judiciais e Administrativos.

|  |  |  |  |
| --- | --- | --- | --- |
| Registros gerados com este Layout M315, M365, M415 0..N | | | |
| Campo | ECF | Gestão Fiscal | Observação |
| REG |  |  | Texto Fixo Conforme Código do Registro |
| IND\_PROC | Tipo do Processo: 1 - Judicial 2 – Administrativo | DPROCESSOJUDICIAL.TIPO |  |
| NUM\_PROC | Número do Processo | DPROCESSOJUDICIAL.NUMERO |  |

Origem da informação “**Contábil**” com efeito na Parte B

Os Registros M300 e M350, quando o Item Tributário estiver parametrizado para afetar a Parte B do Lalur através da constituição de saldo na conta ou da baixa do saldo da conta, terá o indicador de relacionamento “**3 – Com Conta da parte B e Conta Contábil**” (Campo 5 - IND\_RELACAO).

Devem ser gerados os registros “filhos” M305/M355 e M310/M360 contendo, respectivamente, a conta da Parte B que foi movimentada e a conta contábil, ambas parametrizadas no Item Tributário.

Exemplo:

|M300|8|Despesas Operacionais - Parcelas Não Dedutíveis|A|3|38245,32|Despesas não dedutíveis|

|M305|01.002|38245,32|D|

|M310|3.1.1.06.002||38245,32|D|
