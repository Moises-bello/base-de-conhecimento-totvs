---
content_hash: 7280d3a8d497630f301b5e9728774413af120e6f7c83dc0fce9a9eadaad6f307
fetched_at: '2026-06-29T00:10:25.121293+00:00'
page_id: '501467680'
product: rm
source: tdn-rm
title: Utilizando atividade de Conceito
type: documentation
url: https://tdn.totvs.com/display/LRM/Utilizando+atividade+de+Conceito
version: 11
---

## **ÍNDICE**

1. **Visão Geral**
2. **Exemplo de utilização**

**01. VISÃO GERAL**

      A atividade "Conceito" tem por função...

**02. EXEMPLO DE UTILIZAÇÃO**

      Descrição dos campos da atividade "Conceito":

**Atividade:**

* **Nome:** Nome da atividade
* **Classe Base:** Descrição da classe base da atividade.
* **Descrição:** Descrição da atividade
* **Habilitado:** Define se a atividade estará em uso ou não.

**Diversos:**

* **Nome do arquivo de Log:** Nome do arquivo de Log.

**Manipuladores:**

* **Completed:** Especificação do modo a ser chamado antes da conclusão.
* **Initialized:** Especificação do método a ser chamado antes de iniciar a execução da atividade.

**Parâmetros:**

* **Definição dos Parâmetros:** Definição dos parâmetros de execução da Fórmula Visual.
* **Parâmetros da Fórmula Visual:**Acesso as tabelas de parâmetros da Fórmula Visual.
* **Parâmetros de Execução:** Especifica o suporte para a inicialização transacionada.

  + **CaseSensitive:** Indica se cadeias de comparação dentro do DataSet diferenciam maiúsculas de minúsculas.
  + **DataSetName:** Nome do DataSet.
  + **EnforceConstraints:** Indica se as regras de restrição devem ser seguidas.
  + **Locale:** Indica uma localidade com a qual serão comparadas as cadeias de caracteres do DataSet.
  + **Namespace:** Indica o espaço para nome do uri de XML para o elemento raiz apontado por este DataSet.
  + **Prefix:** Indica o prefixo do espaço para o nome usado neste DataSet.
  + **Relations:** A coleção que retém as relações deste DataSet.
  + **RemotingFormat:** Formato remoto do arquivo.
  + **Tables:** A colação que retém as tabelas deste DataSet.

**RM.NET:**

* **Campos:** Acesso aos valores dos campos da tabela principal da atividade.
* **Conjunto de Dados:** Especifica o suporte para a inicialização transacionada.
* **Contexto:** Acesso aos dados do contexto da aplicação.
* **Dados do Usuário:** Dados do usuário (OwnerData) dos parâmetros da execução da Fórmula Visual.
* **Iniciar Transação:** Determina se a Fórmula Visual deve iniciar uma transação com o Banco de Dados ao iniciar a sua execução.
* **Referências:** Lista de referências externas da Fórmula Visual.
* **Tabelas:** Acesso às tabelas da fonte de dados da atividade.
* **WorkflowId:** Permite a execução de um grupo de atividades em uma sequência.

    Como exemplo, vamos utilizar uma atividade para executar um Conceito utilizando parâmetro do tipo txt onde a conexão de origem é Banco de Dados e a conexão de destino é txt.

     Em seguida é necessário configurar os parâmetros da atividade, que no exemplo é do tipo Texto.

    Segue abaixo o passo a passo para execução da fórmula:

    Após a criação da fórmula, adicione as seguintes atividades no Fluxo de Trabalho Sequencial como mostra na imagem abaixo:

    No exemplo utilizado a atividade executa um determinado Conceito criado passando os parâmetros que nele contém.   
    No campo IDConceito você deverá informar o conceito que deseja que a atividade executa, no caso do exemplo o ID é 1.  
    O campo parâmetro é preenchido automaticamente de acordo com os parâmetros que você utilizou ao criar o conceito.  
    **Obs.:** Se os parâmetros forem do tipo Filtro, Lookup e Lista de Objetos eles não serão exibidos para preenchimento na atividade devido às limitações dos componentes de Fórmula Visual. Todos os demais serão exibidos.  
    Após adicionado as informações da atividade a ser executada clique em "Salvar e Executar" e verifique se a fórmula foi executada e se o registro foi concluído corretamente.

    Registro do arquivo txt criado corretamente:

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** Uitlizando atividade de conceito

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
