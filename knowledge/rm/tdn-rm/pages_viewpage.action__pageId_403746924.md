---
content_hash: 3f7a5d4177bed62e6734b4e8d3e4c941ee61b59e5ecdcb3764302f2caa31e3ab
fetched_at: '2026-06-29T00:09:11.333535+00:00'
page_id: '403746924'
product: rm
source: tdn-rm
title: Cadastro de Fórmulas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=403746924
version: 6
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

Existe no RM a possibilidade de cadastrar fórmulas que podem ser utilizadas em diversas ocasiões. As fórmulas facilitam a utilização do sistema garantindo maior agilidade.

O cadastro de Fórmulas nos aplicativos RM terá, basicamente, três principais objetivos, dentre eles:

* Seleção (restrição da aplicabilidade de alguma operação).
* Definição da forma de cálculo de eventos específicos, inclusive do tipo "base de cálculo", que servem de referência para outros cálculos.
* Relacionamento de valores entre os eventos.

O editor de fórmulas possui um campo de texto para que você monte as estruturas das fórmulas. Usando o editor de fórmulas, as funções e comandos desejados para a criação da fórmula serão movidos para o campo de texto, bastando clicar duas vezes sobre as opções função, comando ou parâmetro.

## **02. EXEMPLO DE UTILIZAÇÃO**

Cadastro de Fórmulas

Funções podem ser escritas com letras maiúsculas e/ou minúsculas. Na fórmula só poderão ser incluídas até 50 constantes.

Para acessar o cadastro de Fórmulas, **acesse**: Serviços Globais > Administração > Fórmulas.

Para testar as fórmulas, é preciso definir um “Contexto”, ou seja, Clique no ícone para selecionar o contexto da execução da fórmula, isto é, para qual ou quem a fórmula será executada.

A caixa de diálogo Seleção de Contexto será apresentada. Clique no ícone para testar a fórmula. Caso o contexto ainda não tenha sido selecionado, a caixa de diálogo Seleção de Contexto será apresentada automaticamente.

### Crítica Global

O parâmetro crítica global permite que uma fórmula possa ser usada em uma crítica global dos sistemas, a fim de fazer a validação ou cálculo necessário para o processo que a usar.

**Exemplo**No sistema de Folha de Pagamento esta opção é marcada para indicar que a fórmula deverá ser processada para todos os funcionários selecionados durante o processo de Crítica da Folha (Rotinas | Crítica da Folha). Fórmulas de crítica servem para verificar se determinado evento foi ou não calculado para um funcionário ou grupo de funcionários.

### Fórmula de Seleção

O parâmetro Fórmula de Seleção deverá ser marcada para distinguir todas as fórmulas que são usadas como seleção.

**Exemplo**Nos módulos dos relatórios internos do módulo Automação de Ponto, como relatório do Espelho de Cartão de Ponto, pode-se utilizar uma fórmula para selecionar alguns funcionários. No campo de Fórmula de seleção só serão listadas as fórmulas que estiverem com o parâmetro "Fórmula de seleção" marcado.

### Acompanhar execução e salvar no arquivo

No módulo Serviços Globais é possível gerar arquivos de LOG de fórmulas, que tem como finalidade registrar em um arquivo informações sobre a execução da fórmula. Para gerar um arquivo de LOG de fórmula é necessário clicar duas vezes sobre um registro de fórmula na tela de visão das fórmulas.

O parâmetro ‘Acompanhar execução e salvar no arquivo:’ permite exibir o arquivo com os dados da LOG após o término do Resultado da fórmula.   
Abaixo deste campo o sistema apresenta o campo de texto onde é apresentado o nome e extensão do arquivo onde os dados do LOG serão gravados. Ao acionar o botão Resultado, o sistema executa o cálculo da fórmula e apresenta seu valor.

Para testar Fórmula Automaticamente ao Salvar, Marque esta opção para que o sistema automaticamente teste a fórmula quando esta for salva. O resultado da fórmula será apresentado no campo resultado.

No cadastro de fórmulas também são exibidas a data e hora da última alteração realizada na fórmula, bem como o Usuário responsável, que exibe o usuário que realizou a última alteração na fórmula.

**Observação**

A fórmula não precisa ser gravada para que o teste seja executado. O resultado de uma fórmula será apresentado com N casas decimais, conforme o produto que o usuário estiver utilizando.

**Exemplo**Caso o usuário esteja utilizando o módulo Folha de Pagamento, o resultado será exibido com 4 (quatro) casas decimais.

### Aplicação das fórmulas

Uma aplicação para as fórmulas são os campos complementares, onde têm a função de validar um determinado valor, como por exemplo, a utilização de fórmula para validação de pré-requisito de disciplinas, cálculo de insumos.

Para validar o campo complementar basta associar a fórmula desejada ao campo complementar, para que esta valide o conteúdo do campo complementar quando você incluir um valor para ele.

Outra finalidade é o seu uso em consultas SQL e relatórios do sistema. Pelos relatórios você inclui as fórmulas deslocando o componente de fórmulas e associando-o a uma fórmula cadastrada no sistema. Já nas Consultas SQL as fórmulas devem ser incluídas passando um comando específico para informar que você está utilizando uma fórmula do sistema.

**Exemplo**

SELECT CHAPA, SALARIO FROM PFUNC

WHERE CHAPA = :FRM\_CHAPA;

### **Fórmulas em VB.NET**

No módulo Globais é possível criar e executar fórmulas em VB.Net. Esta funcionalidade tem como objetivo permitir que usuários também utilizem da linguagem [VB.net](http://VB.net) para elaborar e executar fórmulas no RM.exe, além das Fórmulas RM.

Na aba administração, selecione a action Fórmulas. Após definir e executar um filtro, selecione agora um Sistema e logo após a opção Novo, para que a janela para inserção de uma nova Fórmula seja exibida. Preencha os campos Código e Título. No campo Linguagem, selecione a opção VB. NET.

Insira no campo destinado a elaboração das fórmulas, uma fórmula válida elaborada na linguagem VB.NET . Acione o botão Contexto, informe um contexto para execução e execute-o.

Ao acionar o botão Resultado, o sistema irá exibir o resultado da fórmula inserida na linguagem VB.NET.

Selecione a opção Salvar e o sistema registrará a fórmula em VB.NET, exibindo a mesma na listagem de fórmulas do sistema.

false

**Versão:** 12.01.XX
