---
content_hash: efd5b3a53e57ca4291f2fc1c03cddd770c0cff7865f1f9c3074a0023d3362a3b
fetched_at: '2026-06-29T00:09:58.253761+00:00'
page_id: '452396260'
product: rm
source: tdn-rm
title: S-1060 – Tabela de Ambientes de Trabalho.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452396260
version: 4
---

O evento S-1060, tem a finalidade de enviar as informações de inclusão, alteração e exclusão dos registros na Tabela de Ambientes de Trabalho do empregador/contribuinte/órgão público. Neste evento serão descritos todos os ambientes de trabalho em que os trabalhados exerçam atividades. A definição do ambiente e suas delimitações é de responsabilidade do empregador/contribuinte/órgão público e quando se tratar de ambiente no exterior essa informação deve constar na descrição do ambiente.

As informações dessa tabela são utilizadas para a validação do evento S-2240 (Condições Ambientais de Trabalho).

O envio das informações referentes à tabela S-1060 deve ser anterior aos envios dos eventos S-2210 (Comunicação de Acidente de Trabalho) e S-2240 (Condições Ambientais do Trabalho – Fatores de Risco) e posterior ao envio dos eventos S-1000 (Informações do Empregador/Contribuinte/Órgão Público), S-1005 (Tabela de Estabelecimentos, Obras ou Unidades de Órgãos Públicos) e S-1020 (Tabela de Lotações Tributárias).

**Parametrizações necessárias**

Para habilitar o ambiente de trabalho é necessário verificar as configurações nos sistemas de Folha de Pagamento e Segurança e Saúde Ocupacional.

No Totvs Folha de Pagamento é necessário informar a data de obrigatoriedade dos eventos de SST.

Ambiente | Parâmetros | Folha de Pagamento – 06.07 – eSocial.

No Totvs Segurança e Saúde Ocupacional acessar: Ambiente | Parâmetros | Segurança e Medicina do Trabalho.

Processos: 23.00.08 – eSocial – Ambiente de Trabalho.

Será necessário configurar os parâmetros para o ambiente de trabalho.

**Observação:** Na definição da quantidade de caracteres deve-se observar as seguintes informações:

* Prefixo: Define a quantidade de caracteres que será utilizada para o prefixo;
* Coligada: Quantidade de caracteres deve ser superior a 2.
* Sequencial: Quantidade de caracteres deve ser superior a 6.

**Procedimentos para a criação do Ambiente de Trabalho.**

Os ambientes de trabalho são gerados para as seguintes situações:

* Prestação de Serviço;
* Posto de Trabalho;
* Local de Trabalho;
* Seção;
* Lotação;
* Lotação Tributária eSocial;
* Tarefa, Função ou Pessoa.

Prestação de Serviços: É o local onde o colaborador presta serviços para a empresa. O cadastro do ambiente de prestação de serviços é realizado diretamente no cadastro do ambiente de trabalho.

Posto de Trabalho: É o lugar ocupado pelo colaborador para desempenho de suas funções. Nessa seleção serão apresentados apenas os Postos de Trabalho que possuem funções vinculadas e que ainda não sejam cadastrados como Ambientes de Trabalho.

Local de Trabalho: São os locais de trabalho que são vinculados às seções. Nessa seleção serão apresentados apenas os Locais de Trabalho que possuem seções vinculadas e que ainda não sejam cadastrados como Ambientes de Trabalho;

Seção: Nessa seleção serão apresentadas todas as seções que ainda não sejam cadastradas como Ambientes de Trabalho e que estão mapeadas nas Avaliações de Risco;

Lotação: É o relacionamento entre seções e funções, ou seja, definição das seções em que as funções serão lotadas. Nessa seleção serão apresentadas apenas as funções e seções que possuem lotações cadastradas (no cadastro de função – quadro de lotação);

Lotação Tributária eSocial: É o relacionamento com os tomadores de serviços. Nessa seleção serão exibidas somente as lotações tributárias que possuam o tipo de lotação entre 3 e 9.

Tarefa, função ou pessoa: Refere-se ao ambiente de trabalho genérico, quando não há vinculação à nenhuma das situações anteriores

**Criação de Ambientes – Prestação de Serviços**.

O ambiente de trabalho de prestação de serviços primeiro é criado, para depois ser feita a vinculação dele aos funcionários.

Totvs Segurança e Saúde Ocupacional | Cadastros | Ambiente de Trabalho (eSocial)

Todos os campos dos cadastros são de preenchimento obrigatório.

Ao selecionar o tipo de ambiente de prestação de serviços uma nova aba é exibida, para o preenchimento das informações referentes à empresa. O preenchimento dessas informações é obrigatório.

**Criação de Ambientes de Posto de Trabalho, Local de Trabalho, Seção, Lotação, Lotação Tributária eSocial.**

A criação do ambiente de trabalho para **Posto de Trabalho, Local de Trabalho, Seção, Lotação, Lotação Tributária eSocial**, será feita automaticamente sempre que houver a inclusão de um desses registros, respeitando algumas situações.

* Posto de trabalho: Só irá gerar o ambiente se houver ao menos 1 função ativa associada;
* Local de Trabalho: Só irá gerar o ambiente se houver ao menos 1 seção ativa associada;
* Seção: Só irá gerar ambiente de trabalho para seção, quando houver uma avaliação de risco vigente para a seção.
* Lotação: Irá gerar o ambiente de acordo com o quadro de lotação vinculado à função;
* Lotação Tributária eSocial: Irá gerar apenas para lotações tributária com os tipos de lotação 03 a 09 associadas.

**Observação:** Para a geração correta do evento S-1060, será necessário acessar o ambiente de trabalho criado e preencher o campo descrição, pois este campo é obrigatório no XML do evento. O campo nome será gerado automaticamente de acordo com o nome do tipo do ambiente.

**Criação de Ambientes de Trabalho a partir de Processo.**

Outra opção para a geração dos ambientes de trabalho é no processo constante na rotina de Ambiente de Trabalho. Neste processo serão gerados os registros no cadastro de ambiente de trabalho, desde que observadas as situações citadas acima.

A partir deste processo, na etapa "Selecione o tipo de ambiente de trabalho", ao marcar uma das opções, para a opção selecionada, o sistema restringirá a geração dos registros de Ambientes de Trabalho, para aqueles registros que possuam avaliação de riscos vigentes.

**Observação:** No processo "Gerar ambiente de Trabalho", o campo “Descrição” do ambiente de trabalho só será preenchido automaticamente quando essa informação já constar no cadastro existente. Caso esta informação não exista, será necessário acessar o ambiente de trabalho criado e preencher, pois esta informação é obrigatória para o envio do evento S-1060.

**Criação de ambiente de trabalho por Tarefa, Função ou Pessoa**

O ambiente de trabalho por Tarefa, função ou pessoa, é um ambiente genérico e será gerado na carga inicial ou no processo de ambiente de trabalho, quando houver Avaliação de Risco mapeados para 'Tarefa, Função ou Pessoa'.

**Criação de Gatilhos de Ambientes de Trabalho a partir de Carga Inicial.**

A partir da rotina de Carga inicial, será possível a geração dos ambientes de trabalho já existentes no sistema, desde que as mesmas atendam às situações citadas no tópico anterior.

A carga inicial é gerada no Totvs Folha de Pagamento, na rotina de geração de gatilhos dos eventos iniciais em: Totvs Folha de Pagamento | eSocial | Gerar Gatilhos Eventos Iniciais.

**Gatilhos para a fila de eventos:**

Toda nova inclusão de ambiente de trabalho irá gerar, automaticamente, um gatilho para o evento S-1060 na fila de eventos. Para a geração do XML, basta selecionar os registros e executar o processo “Gerar XML”.3

Veja mapeamento dos campos que serão informados: Evento [S-1060.](http://tdn.totvs.com/display/LRM/Evento+S-1060).
