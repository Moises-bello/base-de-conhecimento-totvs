---
content_hash: c9128c2e8be6219a82715f800686033d9ee0218bc43dda43a5096bbf39d0c1eb
fetched_at: '2026-06-29T00:08:06.167519+00:00'
page_id: '236586617'
product: rm
source: tdn-rm
title: ER_EDUEDU001-4_Funcionario_Responder_Avaliacao
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_EDUEDU001-4_Funcionario_Responder_Avaliacao
version: 131
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Educacional | **Módulo** | Edu |
| **Segmento Executor** | Educacional | | |
| **Projeto1** | [EDU 2016/2017](http://jiraproducao.totvs.com.br/browse/EDUEDU001) | **IRM1** | [EDUEDU001-3](http://jiraproducao.totvs.com.br/issues/?jql=cf%5B10062%5D+%3D+EDUEDU001-3 "EDUEDU001-3") |
| **Requisito1** | [EDUEDU001-4](http://jiraproducao.totvs.com.br/browse/EDUEDU001-4) | **Subtarefa1** | [EDUEDU001-24](http://jiraproducao.totvs.com.br/browse/EDUEDU001-24) |
| **Chamado2** |  | | |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Possibilitar que os funcionários das empresas parceiras possam responder avaliações institucionais.

## Definição da Regra de Negócio

**Requisito 1: Cadastro de funcionário da empresa parceira**

O cadastro de funcionários da empresa parceria até a versão 12.1.11 não possui vinculo com o cadastro de pessoas, no entanto, a partir da 12.1.12 este vinculo passa a ser requerido sempre que houver a necessidade de resposta de avaliações. O cadastro de funcionário sofrerá as seguintes alterações:

* Criação do campo código da pessoa (CODPESSOA) para estabelecer o vínculo entre o cadastro do funcionário e o cadastro de pessoa.
* Criação dos campos naturalidade (CODNATURALIDADE) e estado natal ( ESTADONATAL)
* Aumentar o tamanho do campo NOME para 120 caracteres
* O código da pessoa só será preenchido se houver a geração de uma avaliação a ser respondida pelo funcionário.
* Para acesso ao portal o código de usuário a ser considerado continuará sendo o definido no cadastro de funcionário da empresa parceira
* Quando o código da pessoa estiver preenchido os seguintes campos precisam estar sincronizados:

| Tabela: SEMPRESAFUNCIONARIO | Tabela: PPESSOA | Descrição | Observação |
| --- | --- | --- | --- |
| NOME | NOME | Nome do funcionário | Aumentar o campo da tabela SEMPRESAFUNCIONARIO de 100 para 120 |
| CPF | CPF | CPF do funcionário |  |
| TELEFONE | TELEFONE1 | Telefone de contato do funcionário |  |
| DTNASCIMENTO | DTNASCIMENTO | Data de nascimento do funcionário |  |
| CODNATURALIDADE | CODNATURALIDADE | Código da cidade natal do funcionário | Campo deve ser criado na SEMPRESAFUNCIONARIO |
| ESTADONATAL | ESTADONATAL | Estado natal do funcionário | Campo deve ser criado na SEMPRESAFUNCIONARIO |
| NPASSAPORTE | NPASSAPORTE | Número do passaporte do funcionário |  |
| PAISORIGEM | PAISORIGEM | País origem do passaporte do funcionário |  |
| DTEMISSAOPASSAPORTE | DTEMISSPASSAPORTE | Data de emissão do passaporte do funcionário |  |
| DTVALIDADEPASSAPORTE | DTVALPASSAPORTE | Data de validade do passaporte do funcionário |  |
| CARTIDENTIDADE | CARTIDENTIDADE | Carteira de identidade do funcionário |  |
| UFCARTIDENT | UFCARTIDENT | Unidade da federação da carteira de identidade |  |
| ORGEMISSORIDENT | ORGEMISSORIDENT | Órgão emissor da carteira de identidade |  |
| DTEMISSAOIDENT | DTEMISSAOIDENT | Data de emissão da carteira de identidade |  |

 

* Algumas informações são encontradas tanto no cadastro de funcionário da empresa parceira quanto no cadastro da pessoa, no entanto, não serão objeto da sincronização, são eles:

| Tabela: SEMPRESAFUNCIONARIO | Tabela: PPESSOA | Descrição |
| --- | --- | --- |
| EMAIL | EMAIL | E-mail do funcionário |
| RUA | RUA | Logradouro |
| COMPLEMENTO | COMPLEMENTO | Complemento do endereço |
| NUMERO | NUMERO | Número |
| BAIRRO | BAIRRO | Bairro |
| ESTADO | ESTADO | Unidade da federação |
| CODMUNICIPIO | CODMUNICIPIO | Código do município |
| CEP | CEP | CEP |
| IDPAIS | IDPAIS | Identificador do país |
| CODUSUARIO | CODUSUARIO | Código do usuário |

* Uma alteração nos campos de sincronização automática no cadastro de funcionário deve disparar a atualização das informações no cadastro de pessoa e em todos os funcionários vinculados a esta mesma pessoa. De forma inversa toda alteração em uma pessoa deve disparar a atualização em todos os funcionários vinculados a esta pessoa.
* O disparo das sincronizações é realizado para evitar impactos no book de relatórios e nas funcionalidades de estágio que exibem tais informações, bem como evitar impactos nos relatórios criados pelos clientes.
* Para a Experiência #8 do Fluig, foi criada a tela de Cadastro de Funcionários da empresa. Dessa forma, as alterações de tamanho campo e os novos campos criados devem ser replicadas para a tela de cadastro de funcionários da empresa parceira que está presente na Experiência #8 do Fluig. Nessa tela os campos devem ter o mesmo tratamento que na tela do sistema e do portal e deverão ser submetidos às mesmas regras de validação e preenchimento, como por exemplo a sincronização de dados com base em informações alteradas.
* Da mesma forma como existe a tela de cadastro de funcionário da empresa parceira pelo sistema e através de uma tela criada para a Experiência #8, como já foi citado, existe também essa tela no Portal Corpore.Net, onde as alterações de campos devem ser replicadas.
* A criação dos novos campos Estado Natal e Naturalidade também deve ser realizada na tela pública de solicitação de cadastro de funcionários da empresa e no formulário do Fluig no fluxo de solicitação de inclusão de funcionários de empresas parceiras. Para mais detalhes sobre como configurar essa funcionalidade no Fluig favor acessar o documento técnico disponível em: .

**Requisito 2: Mecanismo para geração de pessoa vinculada ao funcionário**

Nos casos em que os funcionários não possuam vinculo com uma pessoa e for necessário gerar um código de pessoa o sistema seguir os seguintes passos:

* Verificar o parâmetro "Validar unicidade de Pessoa por" no **Recursos Humanos | Configurações | Gerais | Validações**
  + Nome, Data de Nascimento, Estado natal e Cidade natal
  + CPF
* A partir do valor definido no parâmetro de unicidade:
  + Verifica se o funcionário possui as informações preenchidas, ou seja, se unicidade é por CPF os funcionários devem possuir esta informação preenchida. Caso não esteja preenchido o processo deve permitir a definição desta informação antes do próximo passo.
  + Verifica se a pessoa já está cadastrada através dos campos de unicidade
    - Não existe uma pessoa cadastrada: será gerada uma nova pessoa a partir dos dados do funcionário da empresa e o código da pessoa será inserido no registro do funcionário.
    - Encontrou uma pessoa cadastrada: busca o código da pessoa e atualiza o registro do funcionário
    - Possui mais de uma pessoa cadastrada: abre-se uma nova aba no processo para definir qual pessoa deve ser utilizada na associação

**Requisito 3: Processo de cadastro de avaliação institucional**

* 1º Passo:
  + Incluir a possibilidade de gerar avaliações institucionais para os funcionários da empresa parceira
* 2º Passo:
  + Selecionar os candidatos a partir do cadastro dos funcionários das empresas parceiras. Apenas usuários ativos devem ser listados.
  + Possibilitar a visualização das avaliações já geradas para o funcionário.
* 3º Passo:
  + Selecionar a avaliação
  + Selecionar período
  + Selecionar grupo
  + Objeto avaliado
    - Item avaliado
      * Curso (disponibilizar uma forma para seleção do curso) - para que seja possível gerar avaliações institucionais para funcionários de empresa, selecionando como item avaliado o "Curso", é necessário que a empresa possua convênio e público alvo cadastrados.
      * Pode-se definir um novo tipo de item avaliado
    - Especificar uma determinada pessoa - disponibilizar um lookup para selecionar a pessoa. Para geração de avaliações institucionais para funcionários de empresa, selecionando como item avaliado uma "Pessoa", NÃO é necessário que a empresa possua convênio e público alvo cadastrados.

**Requisito 4: Anexos para listar as avaliações vinculadas aos funcionários da empresa parceira**

Possibilitar que pelo cadastro do funcionário da empresa possam ser visualizadas as "provas realizadas", "pesquisas realizadas" e "provas e pesquisas pendentes" semelhante ao que já é realizado no cadastro de pessoa com a adição das actions abaixo como detalhes:

* this.DetailActions.Add("TstPessoasProvaAction", "CODIGO", "CODPESSOA");
* this.DetailActions.Add("TstPessoasPesquisaAction", "CODIGO", "CODPESSOA");
* this.DetailActions.Add("TstProvaPesquisaPendenteAction", "CODIGO", "CODPESSOA");

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Cadastro de funcionário da empresa parceira | Alteração | Atividades acadêmicas | Empresas | Funcionários da empresa | - |
| Cadastro de pessoa | Alteração | Gestão de pessoas | Acompanhamento | Pessoas | - |
| Processo de avaliação institucional | Alteração | Atividades acadêmicas | Avaliação Institucional | - |

## Dicionário de Dados

**Tabela: SEMPRESAFUNCIONARIO - novos campos**

 

|  |  |
| --- | --- |
| **Campo** | CODPESSOA |
| **Tipo** | INT |
| **Tamanho** | 4 |
| **Valor Inicial** |  |
| **Mandatório** | Sim (  ) Não (X) |
| **Descrição** | Vínculo do funcionário da empresa parceira com o cadastro de pessoas |
| **Título** | Identificador da pessoa |
| **Picture** |  |
| **Help de Campo** | Informar o código de pessoa do funcionário da empresa parceira |

|  |  |
| --- | --- |
| **Campo** | CODNATURALIDADE |
| **Tipo** | VARCHAR |
| **Tamanho** | 20 |
| **Valor Inicial** |  |
| **Mandatório** | Sim (  ) Não (X) |
| **Descrição** | Código da cidade natal do funcionário da empresa parceira |
| **Título** | Cidade natal do funcionário da empresa parceira |
| **Picture** |  |
| **Help de Campo** | Informar a naturalidade do funcionário da empresa parceira |

|  |  |
| --- | --- |
| **Campo** | ESTADONATAL |
| **Tipo** | VARCHAR |
| **Tamanho** | 2 |
| **Valor Inicial** |  |
| **Mandatório** | Sim (  ) Não (X) |
| **Descrição** | Estado natal do funcionário da empresa parceira |
| **Título** | Estado natal do funcionário da empresa parceira |
| **Picture** |  |
| **Help de Campo** | Informar o estado natal do funcionário da empresa parceira |

**Tabela: SEMPRESAFUNCIONARIO - aletração de campo**

|  |  |
| --- | --- |
| **Campo** | NOME |
| **Tipo** | VARCHAR |
| **Tamanho** | 120 |
| **Valor Inicial** |  |
| **Mandatório** | Sim (X) Não ( ) |
| **Descrição** | Nome do funcionário da empresa parceira |
| **Título** | Nome do funcionário da empresa parceira |
| **Picture** |  |
| **Help de Campo** | Informar o nome do funcionário da empresa parceira |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
