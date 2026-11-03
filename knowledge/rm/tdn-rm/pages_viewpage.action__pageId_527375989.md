---
content_hash: abb297e00e349fa027cdb2cfd2a338c4524de053ee9b6985d4b33230c1a7078d
fetched_at: '2026-06-29T00:10:32.567782+00:00'
page_id: '527375989'
product: rm
source: tdn-rm
title: Configurar Proteção de Dados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=527375989
version: 38
---

#ddd1solidInformações do Documento

**Versionamento**

---

Criação → Versão: v1.0

Revisão → Versão: v1.0

## **01. OBJETIVO**

Esse documento tem o objetivo de apresentar como cadastrar as informações referentes a proteção de dados no RM.

## **02. GDIC e GDICDATAPROTECTION**

       Existem duas tabelas principais referentes à proteção de dados:

* **GDIC**, a qual possui os campos:
  + **SENSIVEL:** Indica que um campo será marcado como sensível.
  + **PESSOAL:** Indica que um campo será marcado como pessoal.
  + **ANONIMIZAVEL**: Indica que um campo será marcado como passível de anonimização.
  + **CODCLASSIFICACAO**: Classificação dos tipos de dados definidos na legislação de Proteção de Dados
  + **CODCLASSIFICACAODETALHADO**: Classificação detalhada dos tipos de dados definidos na legislação de Proteção de Dados

* **GDICDATAPROTECTION**, a qual possui os campos:
  + **CODSISTEMA E CLASSNAME (MÓDULO):** - Indica o módulo a qual será vinculado um campo.
  + **CODENQUADRAMENTO:** Base Legal de Tratamento de dados Pessoais/Sensiveis. Indica os Códigos de Enquadramento do Dado Pessoal.
  + **DESCRICAOENQUADRAMENTO:** Descrição do Enquadramento do Dado Pessoal.
  + **JUSTIFICATIVACOLETA:** Justificativa de Coleta.

## **03. CONFIGURAR DICIONÁRIO DE DADOS**

        Para realizar o cadastro das informações referentes a proteção de dados, navegue em «Segurança», «Acesso», «Proteção de Dados», «Configurar Proteção de Dados».

        Após navegar na Ribbon e clicar no botão «Configurar Proteção de Dados», a visão «Configurar Dicionário de Dados» irá se abrir. Essa tela é uma visão que apresenta todas as colunas de todas as tabelas do sistema disponíveis através da tabela GDIC. Observe que a visão anexa «Configurar a Proteção de Dados Pessoais» também irá se abrir de forma automática.

Atenção

Para que o sistema tenha uma melhor performance as alterações realizadas neste cadastro podem demorar até 2 minutos para serem aplicadas.

ObservaçãoNessa visão não se poderá incluir ou excluir dados e apenas alguns campos (somente os que se referem a proteção de dados) poderão ser modificados.

Ao clicar no botão «Editar» o formulário abaixo será apresentado. Observe que a aba«Configurar a Proteção de Dados Pessoais» também aparece em conjunto com o formulário.

Essa tela possui 8 componentes, divididos em três grupos:

* **Geral** 
  + **Nome da Tabela:** Caixa de Texto com o nome da tabela do campo à receber a configuração de proteção de dados.
  + **Nome da Coluna:** Caixa de Texto com o nome do campo à receber a configuração de proteção de dados.

* **Definições de Proteção aos Dados**
  + **Pessoal:** Caixa de Marcação referente a configuração do campo como Pessoal. 
    - **OBS:** Ao marcar um campo como pessoal, as outras configurações (Sensível, Anonimizável, Código de Classificação e Código de Classificação Detalhado) estarão liberadas para modificação
  + **Sensível:** Caixa de Marcação referente a configuração do campo como Sensível.
  + **Anonimizável:**Caixa de Marcação referente a configuração do campo como Passível de Anonimização.
  + **Código de Classificação**: Lookup referente aos Códigos de Classificação disponíveis no RM, são eles:

| Id | Descrição |
| --- | --- |
| 0 | Sem Proteção |
| 1 | CPF |
| 2 | RG |
| 3 | Email |

 **Código de Classificação Detalhado:**Lookup referente aos Códigos de Classificação Detalhados disponíveis no RM, são eles:

| Id | Descrição |
| --- | --- |
| 0 | Sem Proteção |
| 1 | Nome |
| 2 | Número de Identificação |
| 3 | Endereço |
| 4 | Dados de Localização |
| 5 | Identificador Via Eletrônica |
| 6 | Cookies |
| 7 | Telefone |
| 8 | Raça ou Etnia |
| 9 | Convicções Religiosas |
| 10 | Convicções Filosóficas |
| 11 | Convicções Políticas |
| 12 | Filiação Sindical |
| 13 | Dados de Saúde |
| 14 | Vida Sexual |
| 15 | Dado Genérico |
| 16 | Dado Biométrico |
| 17 | Orientação Sexual |
| 18 | Descrição Livre |
| 19 | Imagem |
| 20 | Pessoal Identificável |
| 21 | Chave Interna Sistema |

* **Utilização**
  + **Módulos onde o campo é utilizado:** Apresenta todos os módulos onde o campo é utilizado de acordo com a tabela GDIC.

Observação

**Banco de Dados:**

As colunas PESSOAL, SENSIVEL, ANONIMIZAVEL, CODCLASSIFICACAO e CODCLASSIFICACAODETALHADO da GDIC são marcadas com default(0) no banco, portanto caso não haja modificação dos mesmos, o valor enviado ao banco é 0.

**Tela:**

Os campos «Pessoal», «Sensível» e «Anonimizável», «Código de Classificação» e «Código de Classificação Detalhado» são obrigatórios, porém os três primeiros, como são booleanos, irão como Verdadeiro ou Falso para o banco, não sendo possível persistir valores diferentes destes, mas os outros dois, como são texto, passarão por uma regra de validação de valores nulos ou vazios, podendo uma exceção ser apresentada, caso esses campos não estejam preenchidos.

## **04. CONFIGURAR A PROTEÇÃO DE DADOS PESSOAIS**

         Para realizar o cadastro das informações referentes a proteção de dados, navegue em «Segurança» «Proteção de Dados» «Configurar Proteção de Dados» «Anexo: Configurar a Proteção de Dados Pessoais»

         Essa tela é uma visão que apresenta todas as configurações de dados pessoais para as colunas marcadas como pessoais disponíveis através da tabela GDICDATAPROTECTION.

         Ao clicar no botão «Novo» ou «Editar» o formulário abaixo será apresentado.

Essa tela possui 6 componentes, divididos em dois grupos:

* **Geral** 
  + **Módulo:**Lookup referente ao módulo do sistema (Código do Sistema + Nome de Classe) cujo campo será vinculado.
  + **Nome da Tabela:** Caixa de Texto com o nome da tabela do campo à receber a configuração de proteção de dados.
  + **Nome da Coluna:** Caixa de Texto com o nome do campo à receber a configuração de proteção de dados.

* **Definições de Proteção aos Dados:**
  + **Código do Enquadramento:**Lookup referente aos Códigos de Enquadramento do Dado Pessoal, são eles:

| Id | Descrição |
| --- | --- |
| 1 | Obrigação Contratual |
| 2 | Obrigação Legal |
| 3 | Consentimento |
| 4 | Execução de Políticas Públicas |
| 5 | Estudo por Órgão de Pesquisas |
| 6 | Exercício Regular de Direito |
| 7 | Para Proteção da Vida |
| 8 | Para Tutela de Saúde |
| 9 | Interesse Legítimo |
| 10 | Proteção de Crédito |

**Descrição do Enquadramento:** Caixa de Texto com a Descrição do Enquadramento do Dado Pessoal.  
**Justificativa de Coleta:** Caixa de Texto com a Justificativa de Coleta.

Observação

**Tela:**

Apenas campos marcados anteriormente como Pessoais podem ter registros incluídos através da tela acima, portanto, certifique-se de ter marcado a caixa de Marcação «Pessoal» na visão de «Configurar Dicionário de Dados».

Caso os campos «Módulo», «Código do Enquadramento», «Descrição do Enquadramento» e «Justificativa de Coleta» não estejam preenchidos uma exceção será levantada, pois todos esses campos são obrigatórios.

O Registro será considerado duplicado quando os Campos «Módulo», «Nome da Tabela», «Nome da Coluna» e «Código do Enquadramento»

## **05. CAMPOS COMPLEMENTARES**

        Para realizar o cadastro das informações referentes a proteção de dados em campos complementares basta ir em «+ Campos Complementares» dentro de um módulo qualquer, que contenha o conceito de campos complementares.

        Iremos usar de exemplo o Módulo «Folha de Pagamento»**.**

        Acesse «Folha de Pagamento», «Administração de Pessoal», «Cadastros», «+ Campos Complementares», «Funcionários»

        A Visão de campos complementares agora contempla três novas colunas, que são:

* **Anonimizável**
* **Pessoal**
* **Sensível**

       Como mostrado na imagem abaixo:

        Ao clicar no botão «Editar» ou «Incluir» uma tela de edição será apresentada como a imagem abaixo:

        Observe que ao clicar em «Anexos» um menu irá aparecer e a opção «Configurar o Dicionário de Dados» estará disponível para ser executada. 

        Ao clicar na opção «Configurar o Dicionário de Dados» o fluxo será idêntico à configuração realizada no **Item****03. CADASTRO GERAL - CONFIGURAR DICIONÁRIO DE DADOS** e **04. CADASTRO GERAL - CONFIGURAR A PROTEÇÃO DE DADOS PESSOAIS**.

Observação

Caso um campo complementar seja desativado, **as informações referentes a Proteção de Dados na GDIC e GDICDATAPROTECTION, para àquele campo,** serão apagados e a opção «Configurar o Dicionário de Dados» no menu «Anexos», **também para àquele campo**, será desativada.

## **06. METADADOS**

        Para realizar o cadastro das informações referentes a proteção de dados em Metadados basta ir em «Serviços Globais», «Metadados», «Persistência», «Tabela».

        A o Layout da Tela de Tabela do Metadados foi alterada para comportar duas outras abas no Grupo «Geral».

        O Grupo Geral hoje compreende três abas, que são:

* **Definições de Campos**
* **Dicionário de Dados**
* **Proteção de Dados**

       Na aba «Dicionário de Dados» estão todos os campos referentes a proteção de Dados da GDIC, são eles:

* **Pessoal**
* **Sensível**
* **Anonimizável**
* **Código de Classificação**
* ****Código de Classificação Detalhado****

      Como apresentado na imagem abaixo:

       Na aba «Proteção aos Dados» estão todos os campos referentes a proteção de Dados da GDICDATAPROTECTION, são eles:

* **Módulo**
* **Código do Enquadramento**
* **Descrição do Enquadramento**
* **Justificativa de Coleta**

      Como apresentado na imagem abaixo:

       O Funcionamento é semelhante ao dos itens **Item****03. CADASTRO GERAL - CONFIGURAR DICIONÁRIO DE DADOS** e **04. CADASTRO GERAL - CONFIGURAR A PROTEÇÃO DE DADOS PESSOAIS**.

Observação

Todos os campos das abas «Dicionário de Dados» e «Proteção aos Dados» são obrigatórios caso o campo «Pessoal» esteja marcado.
