---
content_hash: a9b104ad911f04fb87ad16078e3571c2c3abe72f87936716cba9e420b4cab691
fetched_at: '2026-06-29T00:11:21.203759+00:00'
page_id: '689067178'
product: rm
source: tdn-rm
title: 2.3.2 - Comparação de Banco
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=689067178
version: 34
---

## O que é?

Esta atividade tem como objetivo realizar a comparação detalhada no banco entre dados previamente definidos em um "mock" e dados retornados por uma consulta SQL específica na base onde o teste foi executado. O processo se resume em validar se os dados são iguais entre o "Mock" (resulado esperado) e os dados que foram criados através do seu teste automatizado.

## Para que serve?

Esta atividade é utilizada para validar a execução dos seus Projetos de Teste. Por exemplo, imagine que você tem uma atividade que realiza o cadastro de informações em uma base de dados. Com esta atividade, você pode verificar se o cadastro foi concluído com sucesso, confirmando que todas as informações foram inseridas corretamente. Isso inclui garantir que todos os campos da tabela relacionados ao cadastro estão preenchidos corretamente e que os valores registrados estão de acordo com o esperado. Assim, você assegura a integridade e precisão dos dados inseridos no banco.

## Exemplo de Uso

Como cadastrarComo Cadastrar 1. Navegação para o cadastro

 1. Navegue no menu do TOTVS Automação de Testes e clique em: **Atividades** → **Banco de Dados**→ **Comparação de Banco.**

 2. Na tabela que será mostrada, clique no botão verde em destaque para iniciar o cadastro.

2. Link para Definir cabeçalho (Nome e nível de acesso)

[Clique aqui para obter as informações do cabeçalho](https://tdn.totvs.com/pages/viewpage.action?pageId=859591806)

3. Preenchimento dos CamposVersão

Especifica a versão da atividade em questão. O objetivo de versionar uma atividade é para quando necessitamos ter mais de uma atividade em versões diferentes. Isso irá nos auxiliar a ter um histórico de atualizações e assegurar que as mudanças feitas sejam rastreáveis e reversíveis, se necessário.

Se for necessário utilizar mais de uma versão do RM no seu ambiente, é recomendado que a versão da atividade seja compatível com o sistema RM em uso. Caso contrário, pode-se optar por uma versão padrão de sua preferência.

*Exemplo utilizando a versão do RM*

*Exemplo utilizando a versão padrão*

Descrição

Fornece uma descrição detalhada da atividade, explicando seu propósito e operações, facilitando a compreensão e manutenção futura.

Cenário de ExecuçãoContexto

Ao selecionar esta opção, a consulta informada na atividade será executada na base de dados restaurada no Projeto de Testes ao qual a Atividade pertence, ou seja, a base de dados que será utilizada é a base do contexto. Deve-se criar um *mock* para a comparação, que deve ser recuperado no momento da criação desta Atividade. Falaremos de Mock detalhadamente mais abaixo.

Base Específica

Ao selecionar esta opção, a consulta informada na atividade será executada em uma base de dados informada manualmente. Nesse caso, é necessário fornecer a [**Credencial de banco de dados**,](https://tdn.totvs.com.br/display/LRM/1+-+Banco+de+Dados) independentemente do banco restaurado pelo Projeto de Teste.

Deve-se criar um *Mock* para a comparação, que deve ser recuperado no momento da criação desta Atividade, clicando no botão "Recuperar informações de Mock" e depois informar o "Servidor" (local que o agente está em execução) e a  [**Credencial de banco de dados**](https://tdn.totvs.com.br/display/LRM/1+-+Banco+de+Dados) para obter os dados (Mock). Falaremos de Mock detalhadamente mais abaixo.

É obrigatório que no cadastro da credencial informada seja preenchido o nome da base de dados (SQL) ou nome do pluggable (Oracle).

Script Sql

Utilize esse campo para escrever o script Sql que deve ser executado na sua base.

Evite utilizar em suas sentenças a expressão SELECT \* FROM TABELA, uma vez que o uso de uma sentença tão genérica pode causar problemas, como por exemplo:

1. Campos novos forem criados e sua comparação não for atualizada.
2. Se sua tabela contiver campos que não são fixos, ou seja, que atualizam o seu valor no momento da criação ou edição. Campos como: **Data de criação, Data de Atualização, Data de Deleção.**

Você não será impedido de salvar sua comparação de banco, mas será mostrado um alerta em laranja na tela, avisando-o desse risco.

O script Sql fornecido será utilizado para recuperar as informações do Mock da sua base de referência e também será executado na base de teste, seja ela restaurada no projeto (contexto) ou específica.

Mock

Mocks em banco de dados são ***simulações*** ou versões ***não reais*** de interações com o banco, usadas principalmente em testes automatizados de software. Quando se utiliza mocks, as interações reais com o banco de dados são substituídas por respostas programadas, que imitam o comportamento esperado do banco. Isso permite testar a lógica de negócios sem acessar o banco de dados diretamente, o que torna os testes mais rápidos, isolados e determinísticos.

O uso de mocks é útil para evitar problemas como:

* Dependência de dados reais ou do estado do banco.
* Dificuldades de reproduzir certos cenários.
* Redução do tempo de execução dos testes.

Ao usar mocks, em vez de consultar um banco de dados real, os testes são configurados para retornar valores específicos previamente definidos, simulando os resultados de consultas, inserções, atualizações ou exclusões.

Recuperar informações de Mock

1. Clique na opção "Recuperar Informações de Mock" na tela de Comparação de Banco.
2. Ao selecionar esta opção, será exibida a janela Escolher Servidor.

#### Campos disponíveis:

* **Servidores (obrigatório)**:  
  É necessário selecionar um servidor que será utilizado para recuperar as informações do Mock.
* **Credencial de banco de dados (obrigatório)**:  
  Selecione o Banco de Dados onde o Script SQL será executado.

  É obrigatório que no cadastro da credencial informada seja preenchido o nome da base de dados (SQL) ou nome do pluggable (Oracle).

**O mock será realizado executando a consulta informada na base de dados referente à Credencial de banco de dados definida anteriormente.**

Para recuperar o mock de uma determinada consulta em uma determinada base de dados, o Agent deve estar sendo executado como administrador na máquina que consiga comunicar com esse servidor de banco.

Editar Informações de Mock 

A funcionalidade Editar Informações de Mock permite que o usuário configure manualmente os dados simulados (mock) que serão utilizados em atividades que exigem acesso a banco de dados, como comparação de banco ou execução de scripts SQL/Oracle. Ela é essencial para garantir testes seguros, sem afetar ambientes reais.

### Aplicações Práticas

* **Testes Controlados**: Facilita testes com alterações rápidas ou múltiplos cenários de conexão.
* **Evita Impactos Reais**: Protege dados de produção ao testar com parâmetros fictícios.

Ao clicar em **"**Editar Informações de Mock", é exibida uma tabela com os campos utilizados na comparação. Cada linha representa um registro e os campos podem ser editados diretamente. Isso permite personalizar o conteúdo esperado conforme a lógica da sua automação.

### Benefícios

* **Rapidez**: Facilita a configuração de cenários de teste.
* **Flexibilidade**: Permite simular diferentes bases de dados.
Variáveis de ambiente

As Variáveis de Ambiente são utilizadas para configurar e personalizar o comportamento da Atividade. Elas permitem definir valores específicos ou dinâmicos que podem ser usados durante a execução dos testes, assegurando que o teste execute conforme o ambiente em que o mesmo é executado. As Variáveis de Ambiente são cadastradas no cadastro de Ambiente onde informamos os valores fixos ou de forma dinãmica no cadastro de Script SQL.

Consulte quais campos permitem o uso das Variáveis de Ambiente nessa Atividade:

[Comparação de Banco - Variáveis de Ambiente.](https://tdn.totvs.com/pages/releaseview.action?pageId=863909804)

Saiba mais sobre [Ambientes](https://tdn.totvs.com/display/LRM/4+-+Ambientes).

Exemplo prático

Imagine que você faz parte da equipe de Fiscal e precisa testar o seguinte fluxo: **realizar o cadastro de uma nova moeda no sistema.**

Para isso, você criou um projeto de teste que realiza a inserção desse registro na base de dados por meio de uma chamada HTTP. Esse projeto automatiza o processo de cadastro, mas é necessário verificar se o registro foi inserido corretamente na base restaurada.

Para garantir essa verificação, é essencial criar uma atividade de comparação que valide o resultado. Nesse caso, você configurará um *mock* dos campos que precisam ser validados, ou seja, os valores esperados para cada campo do registro criado, como o código da moeda, o nome, a descrição e outros atributos relevantes. A atividade de comparação irá comparar esses valores mockados com os valores efetivamente inseridos na base de dados durante a execução do teste.

Dessa forma, o projeto de teste estará completo, pois, além de executar a ação de cadastro, ele também garantirá que o registro foi inserido corretamente, validando a integridade e a consistência dos dados armazenados. Esse fluxo proporciona uma abordagem mais robusta, automatizada e confiável para testar o processo de cadastro de moeda, evitando erros manuais e garantindo a precisão da operação.

Visualização do Log de Execução.

Se a comparação for executada com erro, será possível identificar as discrepâncias entre a base gabarito/mock e o banco de teste (onde a automação foi executada) por meio do log de execução do projeto de teste. O log fornecerá informações detalhadas sobre as divergências encontradas.

Quando ocorre um erro, as linhas que apresentarem diferenças serão exibidas na aba **DIFERENÇAS**. Nessa aba, os campos que apresentarem inconsistências serão destacados em negrito e na cor **vermelha**, facilitando a identificação visual dos problemas. Além disso, todos os campos que contêm diferenças serão listados em uma coluna específica chamada *CAMPOS DIFERENTES*. Esta coluna detalhará exatamente quais campos apresentaram variações, permitindo uma análise precisa das discrepâncias.

Essa funcionalidade oferece uma visão clara e organizada das divergências, agilizando o processo de correção e garantindo que o teste possa ser ajustado de maneira eficiente. Além disso, o uso de logs detalhados e a exibição de erros em formato visual ajudam a identificar rapidamente os problemas, permitindo ações corretivas imediatas.

---

# Saiba mais

Sempre que utilizar uma Atividade de Restauração de Banco de Dados, deixe a limpeza automática do TOTVS Automação de Testes apagar a base. Isso ajudará a preparar o seu ambiente para uma próxima execução das automações.

Nunca utilize "select \*" para validar a comparação dos bancos de dados. Pode haver campos de datas que irá comprometer seu resultado.

# FAQ

**P: Recebi o seguinte erro ao rodar a minha comparação: Column 'X' does not belong to table. O que fazer?**

R: A base restaurada não está com os scripts atualizados. Sua comparação faz referência uma coluna que não existe mais. Para isso, execute a atualização dessa base de dados ou ajuste a consulta da comparação para excluir essa coluna.

**P: Recebi o seguinte erro ao rodar a minha comparação: Log: Colunas de tipos diferentes nas tabelas possuem a mesma posição. O que fazer?**

R: A posição das colunas nas comparações estão diferentes. Para resolver isso, ajuste a sua consulta da comparação informando somente os campos utilizado no lugar de SELECT \* FROM.

**P: Recebi o seguinte erro ao rodar a minha comparação: Log: Houve diferenças na comparação do banco de Dados. O que fazer?**

R: Verifique se houve algum erro nas atividade executadas anteriormente. O problema pode estar no meu teste que não retornou o resultado esperado.
