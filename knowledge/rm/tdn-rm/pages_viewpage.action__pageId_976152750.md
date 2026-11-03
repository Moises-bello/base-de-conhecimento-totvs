---
content_hash: 838d5eb79dd5959035b2b196b24321b19f78e4ce02ce807006ab2d78d35a8c18
fetched_at: '2026-06-29T00:12:15.355316+00:00'
page_id: '976152750'
product: rm
source: tdn-rm
title: 03. Contratos 2.0 | Processos | Contabilização no Contrato, Integração Gestão
  Patrimonial e Arrendamento Mercantil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=976152750
version: 218
---

---

Para gerar contabilização no Contratos 2.0 é necessário algumas parametrizações:

* Definir os parâmetros em [Gestão de Estoque, Compras e Faturamento | Contratos | Contabilidade](https://tdn.totvs.com/x/ochEGQ)
* Definir o evento contábil no cadastro de

Como configurar o Evento Contábil6Parametrizações - Evento ContábilEventos Contábeis

Caminho: BackOffice > Gestão de Estoque, Compras e Faturamento > Cadastro > Eventos Contábeis (*Dentro do grupo contábeis*).

eventocontabilidentIdentificação

Ao criar o Evento Contábil em **Processos** defina a opção **Contrato**.

* No campo **Buscar Filial/Depto em:** e **Buscar Centro de Custo em:** selecione a opção **Item de Contrato**.
* No campo **Aplicar o Centro de Custo em:**selecione caso precisa dessa informação no lançamento contábil.

Para contabilizar com Centro de Custo além de configurar no evento para "Aplicar o Centro de Custo em", no contrato precisa ter ele informado no item ou em rateio de Centro de Custo.

itensItens Evento

No cadastro do Item do Evento Contábil, em **Aplicar** selecione a opção: **Item de Contrato** ou **Rateio Centro de Custo do Item**.

Definindo a Conta Contábil no evento que aceita **Rateio** de Centro de Custo, precisa ser definido no cadastro do Item **Aplicar: Rateio Centro e Custo do Item,** na aba Itens Gereciais definir **Aplicar em:** **Rateio Centro e Custo do Item** e informar a fórmula que precisa ser criada com a função SOMATABITMPARCELARATCCU.

Na opção **Origem da Conta**, defina **Informar Conta** ou **Tabela Default.**

Para a opção **Tabela Default**, serão apresentadas no campo **Busca default em**, os itens: Cliente/Fornecedor - Produto - Centro de Custo - Tabelas de Classificação do Produto (05 opções possíveis presentes no parâmetros do sistema)

As fórmulas são desenvolvidas somente para contabilização com opção Aplicar no **Item de Contrato** e **Rateio Centro de Custo do Item.**

5Parametrizações - FórmulasFunções de fórmulas a serem utilizadas no processo de Contabilização

As fórmulas não podem ser testadas através do executo de fórmulas da MDI, pois precisam do contexto de execução do processo.

SOMATABITMPARCELA

**Nome da função:** SOMATABITMPARCELA

**Contexto exigido**: O uso da função de fórmula "SOMATABITMPARCELA" exige o identificador do contrato e do item do contrato, campos ] 

**Retorno**: Retorna a soma dos valores da tabela TITMCNTPARCELA.

**Sintaxe**: A função de fórmula **SOMATABITMPARCELA**(STRING, STRING) exige dois parâmetros do tipo string, são eles:

<**Parâmetro 1**>

"VALORPRESENTE" - Use para somar o valor presente das parcelas de contratos de arrendamento mercantil.

"AMORTIZACAOJUROS" - Use para somar o valor de amortização das parcelas de contratos de arrendamento mercantil.

"VALORPARCELA" - Use para somar o valor das parcelas do contrato.

<**Parâmetro 2**>  

"C" - Considera na soma as parcelas de curto prazo de contratos de arrendamento mercantil.

"L" - Considera na soma as parcelas de longo prazo de contratos de arrendamento mercantil.

"T" - Considera na soma todas as parcelas do contrato.

**Exemplo**: SOMATABITMPARCELA('VALORPARCELA', 'T')

Nesse caso a fórmula vai retornar a soma de VALORPARCELA de todas parcelas do contrato e o retorno é do tipo VALOR.

SOMATABITMPARCELARECLASSIFICADA

**Nome da função:** SOMATABITMPARCELARECLASSIFICADA:

**Contexto exigido**: O uso da função de fórmula "SOMATABITMPARCELARECLASSIFICADA" exige o identificador do contrato e do item do contrato, campos ] 

**Retorno**: Retorna a soma dos valores da tabela TITMCNTPARCELA, considerando apenas parcelas que estão sendo reclassificadas.

**Sintaxe**: A função de fórmula **SOMATABITMPARCELARECLASSIFICADA**(STRING, DATA) exige um parâmetro do tipo string:

<**Parâmetro 1**>

"VALORPRESENTE" - Use para somar o valor presente das parcelas de contratos de arrendamento mercantil.

"AMORTIZACAOJUROS" - Use para somar o valor de amortização das parcelas de contratos de arrendamento mercantil.

"VALORPARCELA" - Use para somar o valor das parcelas do contrato.

**Exemplo**: SOMATABITMPARCELARECLASSIFICADA('VALORPRESENTE')

Nesse caso a fórmula vai retornar a soma de VALOR PRESENTE de todas parcelas classificadas entre a data de curto prazo e a data atual.

SOMATABITMPARCELAREAJUSTADA

**Nome da função:** SOMATABITMPARCELAREAJUSTADA:

**Contexto exigido**: O uso da função de fórmula "SOMATABITMPARCELAREAJUSTADA" exige o identificador do contrato e do item do contrato, campos ] 

**Retorno**: Retorna a soma dos valores da tabela TITMCNTPARCELA, considerando apenas parcelas que estão sendo Reajustadas.

**Sintaxe**: A função de fórmula **SOMATABITMPARCELAREAJUSTADA**(STRING,  STRING) exige três parâmetros do tipo string, são eles:

<**Parâmetro 1**>

"VALORPRESENTE" - Use para somar o valor presente das parcelas de contratos de arrendamento mercantil.

"AMORTIZACAOJUROS" - Use para somar o valor de amortização das parcelas de contratos de arrendamento mercantil.

"VALORPARCELA" - Use para somar o valor das parcelas do contrato.

<**Parâmetro 2**>  

"C" - Considera na soma as parcelas de curto prazo de contratos de arrendamento mercantil.

"L" - Considera na soma as parcelas de longo prazo de contratos de arrendamento mercantil.

"T" - Considera na soma todas as parcelas do contrato.

**Exemplo**: SOMATABITMPARCELAREAJUSTADA('VALORPARCELA', 'T')

Nesse caso a fórmula vai retornar a soma de VALOR PARCELA de todas parcelas reajustadas.

SOMATABITMPARCELAADITIVADA

**Nome da função:** SOMATABITMPARCELAADITIVADA:

**Contexto exigido**: O uso da função de fórmula "SOMATABITMPARCELAADITIVADA" exige o identificador do contrato e do item do contrato, campos ] 

**Retorno**: Retorna a soma dos valores da tabela TITMCNTPARCELA, considerando apenas parcelas que estão sendo Reajustadas.

**Sintaxe**: A função de fórmula **SOMATABITMPARCELAADITIVADA**(STRING,  STRING) exige três parâmetros do tipo string, são eles:

<**Parâmetro 1**>

"VALORPRESENTE" - Use para somar o valor presente das parcelas de contratos de arrendamento mercantil.

"AMORTIZACAOJUROS" - Use para somar o valor de amortização das parcelas de contratos de arrendamento mercantil.

"VALORPARCELA" - Use para somar o valor das parcelas do contrato.

<**Parâmetro 2**>  

"C" - Considera na soma as parcelas de curto prazo de contratos de arrendamento mercantil.

"L" - Considera na soma as parcelas de longo prazo de contratos de arrendamento mercantil.

"T" - Considera na soma todas as parcelas do contrato.

**Exemplo**: SOMATABITMPARCELAADITIVADA('VALORPARCELA', 'T')

Nesse caso a fórmula vai retornar a soma de VALOR PARCELA de todas parcelas aditivadas.

SOMATABITMPARCELAMEDIDA

**Nome da função:** SOMATABITMPARCELAMEDIDA:

**Contexto exigido**: O uso da função de fórmula "SOMATABITMPARCELAMEDIDA" exige o identificador do contrato e do item do contrato, campos ] 

**Retorno**: Retorna a soma dos valores da tabela TITMCNTPARCELA, considerando apenas parcelas que estão sendo Reajustadas.

**Exemplo**: SOMATABITMPARCELAMEDIDA

Nesse caso a fórmula vai retornar o valor da medição de todas as parcelas

SOMATABITMPARCELARATCCU

**Nome da função:** SOMATABITMPARCELARATCCU:

**Contexto exigido**: O uso da função de fórmula "SOMATABITMPARCELARATCCU" exige o identificador do contrato e do item do contrato, campos ] 

**Retorno**: Retorna a soma dos valores da tabela TITMCNTPARCELA, conforme sua classificação e considerando o percentual do centro de custo informado.

**Sintaxe**: A função de fórmula **SOMATABITMPARCELARATCCU**(STRING,  STRING) exige três parâmetros do tipo string, são eles:

<**Parâmetro 1**>

"VALORPRESENTE" - Use para somar o valor presente das parcelas de contratos de arrendamento mercantil.

"AMORTIZACAOJUROS" - Use para somar o valor de amortização das parcelas de contratos de arrendamento mercantil.

"VALORPARCELA" - Use para somar o valor das parcelas do contrato.

<**Parâmetro 2**>  

"C" - Considera na soma as parcelas de curto prazo de contratos de arrendamento mercantil.

"L" - Considera na soma as parcelas de longo prazo de contratos de arrendamento mercantil.

"T" - Considera na soma todas as parcelas do contrato.

**Exemplo**: **SOMATABITMPARCELARATCCU**('VALORPARCELA', 'T')

Nesse caso a fórmula vai retornar o valor das parcelas aplicando o percentual do centro de custo informado por parâmetro, se o item do contrato não tem o centro de custo informado então retorna valor 0.

SETABITMPARCELAAUMENTA

**Nome da função:** SETABITMPARCELAAUMENTA:

**Contexto exigido**: O uso da função de fórmula "SETABITMPARCELAAUMENTA" exige o identificador do contrato e do item do contrato, campos ] 

**Retorno**: Conforme o impacto de valor positivo ou negativo na tabela TITMCNTPARCELA, retorna se o efeito do processo vai ser de AUMENTAR o valor do item, caso não seja de aumentar então quer dizer que vai DIMINUIR.

1) Quando for utilizado buscar default em uma Tabela de Classificação a regra de preenchimento das contas contábeis buscará  primeiro na classificação contábil vinculada no item do contrato, caso não seja atendido buscará  na classificação do produto que esta vinculado no item do contrato.

2) Os mnemônicos que podem ser utilizados nos complementos dos históricos nos eventos contábeis são:

| Mnemônico | Descrição |
| --- | --- |
| CCF | Código do Fornecedor |
| NOM | Nome Fantasia do Fornecedor |
| FAN | Nome Fantasia do Fornecedor |
| RAZ | Razão Social do Fornecedor |
| COD | Código do Contrato |
| HIS | Histórico do Contrato |
| CTR | Nome do Contrato |
| DCTR | Data do Contrato |
| OBS | Observação do Contrato |

Atenção

* A contabilização será executada caso o evento esteja definido no cadastro de .   
  Se nenhum evento estiver definido, presume-se que a contabilização não será gerada durante a execução dos processos.
* **Restrições de edição de campos:** Quando houver contabilização gerada alguns campos do contrato e item do contrato, terão a edição bloqueadas. Para ver quais são esses campos, [clique aqui](https://tdn.totvs.com/x/iM9eNw).
Histórico de Contabilidade e Patrimônio

Após contabilização e integração com patrimônio, na visão de contratos e itens você terá a visão dos históricos. Para ver quais são esses campos, [clique aqui](https://tdn.totvs.com/x/iM9eNw). 

Inclusão de Contabilidade

Este processo solicitará ao TOTVS Gestão Contábil a inclusão da contabilização inicial dos contratos selecionados.

Após selecionar os contratos e executar o processo pela visão do contrato, será atualizado as informações contábeis do contrato e incluindo todas as contabilizações. 

Uma das exigências para executar o processo com sucesso, independente de qual tabela será buscado o default contábil, é que no cadastro da Conta Contábil a opção de uso de Rateio esteja desabilitada, como indicado na imagem:

Exclusão da Contabilidade

Este processo solicitará ao TOTVS Gestão Contábil a exclusão da contabilização inicial dos contratos selecionados.

Esse processo só é executado para contratos que não foram integrados ao lote oficial.

Após selecionar os contratos e executar o processo pela visão do contrato,  será atualizado as informações contábeis do contrato deletando todas as contabilizações. 

Estorno da Contabilidade

Este processo solicitará ao TOTVS Gestão Contábil o estorno da contabilização inicial dos contratos selecionados.

Esse processo só é executado para contratos que a contabilização esteja integrada ao Lote oficial da Contabilidade (ZERO).

Após selecionar os contratos e executar o processo pela visão do contrato,  será atualizado as informações contábeis do contrato estornando as contabilização inicial e gerando o lançamento no lote de estorno definido. 

Solicitar Exclusão de toda a Operação Contábil

Este processo solicitará ao TOTVS Gestão Contábil a exclusão de toda a operação contábil (contabilização e estorno) dos contratos selecionados.

Se o contrato exitir mais de uma contabilização no cenário acima, o processo realizará para todas.

Esse processo só é executado para contratos que tiveram sua contabilização estornadas.

Após selecionar os contratos e executar o processo pela visão do contrato, será gerada uma solicitação ao Contábil de exclusão de toda a contabilidade.

Após a execução desta tarefa no Contábil, será atualizado as informações contábeis do contrato deletando todas as contabilizações. 

Informações Adicionais

[Tarefas - TOTVS Gestão Contábil](http://tdn.totvs.com/pages/viewpage.action?pageId=423938586)

Contabilização do Reajuste de Preço

Na execução do processo **Reajuste de Preço** a contabilização é gerada automaticamente, contabilizando o valor do Reajuste dos contratos selecionados.

Este processo solicitará ao TOTVS Gestão Contábil a inclusão do lançamento de contabilização no lote definido nos parâmetros.

Na execução do processo de **Cancelar Reajuste de Preço** será excluído ou estornado toda a operação contábil dos contratos selecionados.

Exclusão da contabilização para contratos que não foram integrados ao lote oficial e Estorno da contabilização para contratos que esteja integrada ao Lote oficial (ZERO).

Para mais detalhes sobre o processo, [clique aqui.](https://tdn.totvs.com/x/NlLkNw)

Contabilização do Medição

Na execução do processo **Medição** a contabilização é gerada automaticamente, contabilizando o valor da Medicação dos itens selecionados. 

Este processo solicitará ao TOTVS Gestão Contábil a inclusão do lançamento de contabilização no lote definido nos parâmetros.

Na execução do processo de **Cancelar Medicação**será excluído ou estornado toda a operação contábil dos contratos selecionados.

Exclusão da contabilização para contratos que não foram integrados ao lote oficial e Estorno da contabilização para contratos que esteja integrada ao Lote oficial (ZERO).

Para mais detalhes sobre o processo, [clique aqui.](https://tdn.totvs.com/x/AcntNw)

Contabilização do Aditivo

Na execução do processo de **Gerar Aditivo** a contabilização é gerada automaticamente, contabilizando o valor aditivado das parcelas dos itens selecionados. 

Este processo solicitará ao TOTVS Gestão Contábil a inclusão do lançamento de contabilização no lote definido nos parâmetros.

Na execução do processo de **Cancelar Aditivo**será excluído ou estornado toda a operação contábil dos contratos selecionados.

Exclusão da contabilização para contratos que não foram integrados ao lote oficial e Estorno da contabilização para contratos que esteja integrada ao Lote oficial (ZERO).

Para mais detalhes sobre o processo, [clique aqui.](https://tdn.totvs.com/x/K8jtNw)

Contabilização do Encerramento do Contrato

Na execução do processo de Encerramento de Contrato a contabilização é gerada automaticamente quando o status do contrato estiver parametrizado com a opção **Cancelamento** habilitada e, adicionalmente, quando o tipo de contrato possuir um **evento contábil de baixa** devidamente vinculado.  
Este processo solicitará ao TOTVS Gestão Contábil a inclusão do lançamento de contabilização no lote definido nos parâmetros.

Não é possível realizar o estorno contábil pelo módulo de Contratos. Esse procedimento deve ser efetuado exclusivamente no módulo Contábil.

Arrendamento Mercantil (Legislação IFRS 16 - CPC06)

Para a gestão dos contratos de Arrendamento Mercantil a empresa arrendatária irá incluir um contrato de natureza Arrendamento Mercantil que terá **um****item** de tipo de faturamento **“Periódico”.**

No contrato de Arrendamento Mercantil será gerado as seguintes contabilizações ou integração do patrimônio:

Inclusão de ContabilidadeA contabilização não é gerada automaticamente será necessário realizar processo, mesma regra acima descrita.Reajuste de Preço e Aditivo

Contabilização gerada automaticamente no momento da execução do processo, mesma regra acima descrita.

Reclassificação Contábil

O processo de **Reclassificar Contabilidade**do contrato tem como objetivo de incrementar a "Data Fim Curto Prazo" de um item de contrato de arrendamento, e com a mudança desta data,  reclassificar as parcelas de "Longo Prazo" que ficarem anterior ou igual a nova data para "Curto Prazo".

Na execução do processo **Reclassificar Contabilidade** a contabilização é gerada automaticamente, contabilizando os meses a incrementar para o Curto Prazo os contratos selecionados.

Este processo solicitará ao TOTVS Gestão Contábil a inclusão do lançamento de contabilização no lote definido nos parâmetros.

Na execução do processo de **Cancelar Reclassificar Contabilidade** será excluído ou estornado toda a operação contábil dos contratos selecionados.

Para mais detalhes sobre o processo, [clique aqui.](https://tdn.totvs.com/x/Nrz7Nw)

Amortização Juros

Os movimentos gerados pelo faturamento dos contratos de arrendamento deverão ser enviados para o item do movimento, para isso o movimento precisa estar parametrizado para .

O campo "Amortização Juros " no item de movimento que receberá o valor da "Amortização Juros" da Parcela que foi faturada.   
Este campo criado no item do movimento poderá ser utilizado para contabilizar os encargos mensalmente das parcelas do contrato, portanto o movimento que recebe o faturamento do contrato para o item periódico terá que ter um evento parametrizado conforme a regra contábil da empresa aplicada para esta contabilização.

Fórmula TABITM para contabilizar campo Amortização Juros

**Nome da função:** TABITM

**Contexto exigido**: O uso da função de fórmula "TABITM" **exige o identificador do contrato e do item do contrato, campos ]**

**Retorno**: Retorna valor de um campo do item do movimento.

**Sintaxe**: A função de fórmula **TABMOV**(CAMPO, TIPO) exige dois parâmetros, são eles:

<**Parâmetro 1**>

"TAXAJUROS" - Use para retornar o valor de amortização de arrendamento mercantil levado para o item do movimento. 

<**Parâmetro 2**>

      "V" = Considera o valor do campo TAXAJUROS da tabela TITMMOV

**Exemplo**: TABITM('TAXAJUROS','V')

Importante ressaltar que este campo não ajustará nos valores do tipo de movimento, ele tem única função de contabilização do juros mensalmente.

Pagamento das Parcelas dos Contratos

Contabilização será tratada no evento contábil de baixa do módulo Gestão Financeira.

Integração do contrato com o Módulo Gestão PatrimonialPatrimônio do Contrato

Os contratos poderão ser inseridos no módulo gestão patrimonial pelo valor presente através do processo [Integrar Aquisições Por Contrato](https://tdn.totvs.com/pages/viewpage.action?pageId=668180079).

Vínculo Contrato de Arrendamento Mercantil

Para contrato vigentes que não possui vinculo com módulo de Patrimônio, foi criado o processo no TOTVS Patrimônio que permite . Com a criação desse vinculo, os processos de Aditivo, Reajuste e Alteração de Status do tipo cancelamento executados no contrato passarão a enviar automaticamente as ocorrências de acréscimo ou baixa para o módulo patrimonial.

Aditivo Valor, Reajuste e Alteração de Status (Acréscimo ou Baixa)

**A partir da versão 12.1.2506.181** contratos que estão integrados ao módulo Gestão Patrimonial, ao executar o processo de Aditivo, Reajuste e Alteração de Status do tipo cancelamento  será gerado automaticamente as ocorrências de acréscimo ou baixa parcial no módulo patrimonial.

* O valor enviado para ocorrência será a diferença do valor presente antes do processo - valor presente depois de executar o processo  
  - Aditivo aumenta ou reajuste ficará com tipo ocorrência: Acréscimo  
  - Aditivo diminui ficará com tipo ocorrência: Baixa Parcial
* Ao realizar o cancelamento do aditivo ou reajuste será realizado o cancelamento da ocorrência.

OS Contratos que estão integrados ao módulo Gestão Patrimonial, ao executar o processo de Alteração de Status para cancelamento do contrato será gerado automaticamente as ocorrências de baixa total no módulo patrimonial. Mais detalhe sobre Status do Contrato, [clique aqui.](https://tdn.totvs.com/x/wcpEGQ)

Baixa Parcial e Total

Na ocorrências de Baixa deverá ser parametrizado o Motivo de Baixa em parâmetros [Gestão de Estoque, Compras e Faturamento | Contratos | Patrimônio](https://tdn.totvs.com/x/ochEGQ)

No TOTVS Patrimônio o **Período Atual de Cálculo** deve ser igual:

* A Data de Inicio Vigência ao executar o processo de aditivo
* A Data de Reajuste ao executar o processo de Reajuste
* A Data de Alteração ao executar o processo de Alteração de Status
Aditivo de Prazo (Revisão de Vida Útil)

**A partir da versão 12.1.2506.195** contratos integrados ao módulo Gestão Patrimonial, ao executar o processo de Aditivo de Prazo será gerada automaticamente a revisão de vida útil no módulo patrimonial.

Aditivo de Prazo (Revisão de Vida Útil)

 Para gerar a revisão de vida útil, o cenário de cálculo deve ser informado em parâmetros [Gestão de Estoque, Compras e Faturamento | Contratos | Patrimônio](https://tdn.totvs.com/x/ochEGQ)

No TOTVS Patrimônio o **Período Atual de Cálculo** deve ser igual:

* A Data de Inicio Vigência da primeira parcela que será gerada pelo Aditivo de Prazo.
Depreciação do Bem Direito de Uso

A contabilização da depreciação será tratada no processo de depreciação mensal do módulo Gestão Patrimonial.
