---
content_hash: 575a0d77d76aebb5da7baea3724900998b6bfaf8905b207ee7b1fd6927cadad4
fetched_at: '2026-06-29T00:10:47.542439+00:00'
page_id: '558246499'
product: rm
source: tdn-rm
title: Integração RH RM X QUÍRONS NG
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=558246499
version: 89
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Configurações TOTVS Gestão de Pessoas (RM)**
4. **Carga Inicial**

## **01. VERSÕES**

false

**A partir dos patches:**

- [DT - Integração RM X Quírons - Permitir envio do percentual de Insalubridade e Periculosidade na API](https://tdn.totvs.com/pages/viewpage.action?pageId=864353887)
- [DT - Integração RM X Quírons - API retorna a lista do líderes diretos dos Subordinados](https://tdn.totvs.com/pages/viewpage.action?pageId=859060885)
- [DT - Integração RM X Quírons - API Exclusão de Funcionários](https://tdn.totvs.com/pages/viewpage.action?pageId=880064597)

## **02. VISÃO GERAL**

Neste artigo, será descrito o passo a passo necessário para a correta parametrização da integração entre o sistema **Quírons (NG)** e o **Módulo de Recursos Humanos (RH)**. O objetivo é garantir que os dados trafeguem de forma consistente e automatizada entre os dois ambientes, otimizando os processos de gestão de pessoas, como admissões, desligamentos, apontamentos e folha de pagamento.

A seguir, detalharemos cada etapa envolvida na configuração, destacando os pré-requisitos, as parametrizações no sistema, os campos obrigatórios e as validações necessárias para o sucesso da integração.

## **Introdução**

O mercado atual exige que operações complexas e a manipulação de grandes volumes de dados sejam realizadas de forma cada vez mais ágil e com menores custos. No setor de Recursos Humanos, essa realidade não é diferente. Com processos cada vez mais detalhados, especialmente nas áreas de **medicina e segurança do trabalho**, é fundamental que os profissionais da área tenham ferramentas eficazes e rápidas para o controle e acompanhamento das rotinas funcionais da empresa.

Diante dessa necessidade e da importância estratégica do RH, softwares especializados em **medicina ocupacional** e **segurança do trabalho** têm se tornado fundamentais para as organizações. Foi nesse contexto que surgiu a necessidade de desenvolver uma solução que **automatize cadastros e rotinas funcionais diretamente no ERP**, por meio de uma **interface de integração eficiente e segura**.

### QUÍRONS

O **Quírons** é um software desenvolvido pela **NG**, empresa com ampla experiência na área de gestão em medicina e segurança do trabalho. Com mais de30 anos de atuação no mercado, a NG se destaca como pioneira na administração de processos funcionais, oferecendo soluções consolidadas e com diversos cases de sucesso. O Quírons foi criado para atender às exigências legais e operacionais dessa área crítica, promovendointegração eficiente entre os sistemas de saúde ocupacional e os ERPs corporativos.

> *Mais informações podem ser consultadas diretamente no site do parceiro NG.* [Link](https://www.ngi.com.br/historia/).

### REQUISITOS:

* Versão: 12.1.29
* Possuir acesso à Internet.
* Estrutura de rede estável, para que haja trafego de dados sem interrupção.
* RM devidamente configurado e serviço Rest habilitado em seu host. Exemplo da configuração, [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044519633-Cross-Segmentos-Backoffice-RM-Integra%C3%A7%C3%A3o-O-que-%C3%A9-e-como-configurar-a-HttpPort-e-ApiPort-).
* TI do cliente deve liberar para acesso externo o IP e Porta.

### ENTIDADES DA INTEGRAÇÃO:

* Enviados Para o sistema Quírons:
  + Funcionário *(módulo responsável Folha)*
  + Pessoa *(módulo responsável Vitae)*
  + Dependente *(módulo responsável Folha)*
  + Histórico funcional
  + Histórico de Treinamento
  + Departamento
  + Cargo
* Buscados pelo o sistema Quírons:
  + Tipos de Afastamento
  + Centro de custo
  + Turnos de Trabalho
  + Tipos de Estabilidade
  + Cursos
  + Funções
  + Histórico de Atestados

* Dados enviados para o RM pelo o sistema Quírons:
  + Necessidade de Treinamento
  + Afastamentos *(módulo responsável Folha)*
    - Quando é gerado um afastamento a situação do funcionário é alterada seguindo as regras do [Novo Atestado](https://tdn.totvs.com/display/public/LRM/Novo+atestado).
  + Condições diferenciadas de trabalho
  + Abonos
  + Estabilidade

## **03.** **CONFIGURAÇÕES INICIAIS** **TOTVS GESTAÇAO DE PESSOAS (RM)**

### 03.01 - Cadastro da Integração

Para habilitar a integração com o sistema **Quírons (NG)** no TOTVS Gestão de Pessoas (RM), é necessário realizar a configuração inicial acessando o seguinte caminho no sistema: RH | Gestão de Pessoas | Configurações | Cadastro Integrações.

No menu **Cadastro de Integrações - RH**, o próximo passo é criar uma nova integração específica para a NG. Para isso:

* Clique em **Novo** para iniciar a criação da integração.
* Preencha os campos solicitados, conforme as orientações e parâmetros exigidos para o correto funcionamento da comunicação entre os sistemas. Link [Cadastro de Integrações - RH](https://tdn.totvs.com/pages/viewpage.action?pageId=557683861)

### 03.02 - Inclusão da Integração

Ao incluir uma nova integração para a NG no TOTVS Gestão de Pessoas (RM), siga as orientações abaixo:

* **Código do Parceiro:** selecione o código referente à NG, que geralmente é **0**.
* **URL Base das APIs:** insira a URL correspondente ao ambiente desejado:

  + Ambiente de produção: `https://app.quirons.com/ttalk/`
  + Ambiente de homologação: `https://sandbox.quirons.com/ttalk/`

> **Atenção:**
>
> * **Não marque** a opção **“Utiliza para todas as Coligadas”**, pois cada coligada terá um usuário diferente no sistema Quírons, a menos que o mesmo usuário seja utilizado para todas as coligadas.
> * **Desmarque** o campo **Ativo** inicialmente; este deverá ser marcado somente após concluir toda a parametrização.

* **Usuário e senha:** informe o usuário e a senha fornecidos pelo Quírons que serão utilizados na autenticação da integração.

Por fim, **salve** a configuração para registrar a integração.

Acesse o **Anexos** nesta mesma tela e clique em **Entidades Integração:**

Neste anexo, deve-se preencher o restante da URL para cada uma das entidades que participam da integração. São, ao todo, **7 entidades** com seus respectivos complementos de URL:

| Entidade | Complemento da URL |
| --- | --- |
| Pessoa | `person?branchId=X` |
| Funcionário | `employee?branchId=X` |
| Histórico Funcional | `functionalhistory?branchId=X` |
| Dependente | `dependant?branchId=X` |
| Histórico de Treinamento | `traininghistory?branchId=X` |
| Cargo | `position?branchId=X` |
| Departamento | `department?branchId=X` |

---

**Observação importante:**  
No complemento da URL, substitua o caractere **X** pelo código da filial da coligada para validar a conexão durante os testes. Essa substituição é necessária **apenas para o teste de conexão inicial**. Após a validação, basta retornar o caractere **X** para o campo, pois **não é necessário criar registros separados para cada filial**.

Após preencher o complemento da URL para cada entidade, utilize o botão **Testar Conexão** para validar se a comunicação com a API destino está funcionando corretamente.

* Caso a conexão seja bem-sucedida, nenhuma mensagem de erro será exibida.
* Se houver problemas na conexão, uma mensagem de erro será apresentada, indicando que a API destino não foi encontrada ou que há algum problema de comunicação.

**Importante:**  
Realize o teste de conexão para todas as entidades listadas. Somente após todos os testes serem aprovados com sucesso é possível prosseguir para as próximas etapas da parametrização.

### 03.03 - Parametrizador

Acesse o menu Configurações | Parametrizador | 07.00.15 – Integração com Terceiros e APIs | 07.00.15.01 – APIs.

Nesta etapa do parametrizador **API Tipo Afastamento**, devem ser informados e vinculados os **Tipos de Afastamentos** e **Motivos de Afastamentos** que serão utilizados no sistema **Quírons**.

Essa associação é fundamental para garantir a correta integração dos afastamentos registrados no Quírons com o módulo de RH do TOTVS. Sem essa vinculação adequada, os dados de afastamento poderão ser inconsistentes ou não sincronizados corretamente.

> **Observação:**  
> Esta funcionalidade está disponível a partir da versão **12.1.34** do sistema.

Foi incluído um novo parâmetro destinado à inclusão de um **tipo de RNT (Registro de Necessidade de Treinamento)**, que deve ser utilizado sempre que a NG enviar informações relacionadas à **Necessidade de Treinamento**.

É fundamental que este parâmetro seja preenchido corretamente para que a integração funcione de forma adequada e os dados de treinamento sejam integrados com sucesso.

### 03.04 - Cursos

Para que a integração da **Necessidade de Treinamento** funcione corretamente, é necessário que os cursos envolvidos possuam **Características Pessoais específicas** configuradas no sistema. Para isso, acesse o menu:  Cursos | Anexos | Características Pessoais.

Nessa tela, devem ser cadastradas as características relacionadas aos cursos que serão integrados, garantindo que o sistema reconheça e trate corretamente essas informações durante o processo de sincronização.

As **Características Pessoais** vinculadas aos cursos devem ser configuradas com apenas **três níveis de prioridade**, que representam:

1. **Indispensável**
2. **Desejado**
3. **Recomendado**

Após concluir todas as parametrizações mencionadas, incluindo o cadastro das características pessoais com os níveis adequados, a integração estará pronta para ser **ativada** no sistema.

## **04.** **GERAÇÃO E ENVIO DAS MENSAGENS DE INTEGRAÇÃO**

### 04.01 - Geração das Mensagens

É possível gerar as mensagens para **todas as entidades da integração** executando o processo de **Carga Inicial**. Link

Acesse o caminho RH | Gestão de Pessoas | Configurações | Carga Inicial.

**Observação:**  
Para garantir a integridade dos dados dependentes do funcionário (como Histórico Funcional, Treinamento e Dependente), recomenda-se que o cadastro do **funcionário seja enviado primeiro**, antes desses dados relacionados.

### 04.02 - Fluxo de Mensagens após Ativação

Após a ativação da integração, sempre que forem realizadas alterações nos cadastros de:

* Funcionário
* Pessoa
* Dependente

Ou quando uma turma for finalizada, mensagens automáticas serão geradas para serem enviadas ao sistema NG.

Estas mensagens ficam armazenadas no menu RH | Gestão de Pessoas | Configurações | Fila de Mensagens API **-** Link [Fila de Mensagens - RH](https://tdn.totvs.com/display/LRM/Fila+de+Mensagens+-+RH)

No menu **Fila de Mensagens API**, siga os passos para envio:

1. Selecione as mensagens que deseja enviar.
2. Acesse o menu **Processos** e escolha a opção **Enviar Mensagens**.

O sistema enviará as mensagens selecionadas para o Quírons. As respostas recebidas serão armazenadas diretamente nos registros correspondentes, com o seguinte tratamento:

* **Campo Retorno:** será preenchido com o retorno de sucesso.
* **Campo Erro:** será preenchido caso ocorra alguma falha no processamento da mensagem, detalhando o motivo do erro para que o usuário possa realizar o tratamento necessário.

Todas as mensagens que apresentarem erro podem ser reenviadas após a correção dos problemas identificados.

## 

## **05.** **DOCUMENTAÇÃO**

* [NG](https://www.ngi.com.br/historia/)
* [Cadastro de Integrações - RH](https://tdn.totvs.com/pages/viewpage.action?pageId=557683861)
* [Fila de Mensagens - RH](https://tdn.totvs.com/display/LRM/Fila+de+Mensagens+-+RH)
* [Integração - WebServices - O que é e como configurar a HttpPort e ApiPort?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044519633-Cross-Segmentos-Backoffice-RM-Integra%C3%A7%C3%A3o-WebServices-O-que-%C3%A9-e-como-configurar-a-HttpPort-e-ApiPort)
