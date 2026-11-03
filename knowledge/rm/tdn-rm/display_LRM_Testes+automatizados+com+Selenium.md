---
content_hash: 15288a496e30429dacbb968b973c9fa573a8475a03272e2e3c8b840d32604068
fetched_at: '2026-06-29T00:11:39.175278+00:00'
page_id: '788603875'
product: rm
source: tdn-rm
title: Testes automatizados com Selenium
type: documentation
url: https://tdn.totvs.com/display/LRM/Testes+automatizados+com+Selenium
version: 24
---

## O que são?

Os testes automatizados com Selenium no TOTVS Automação de Testes são executados através de **Atividades C#**, com um template C# específico já disponível para simplificar a integração e execução do Selenium diretamente na ferramenta de Automação de Testes.

## Para que serve?

Eles ajudam a garantir que aplicações web funcionem corretamente, permitindo:

* **Automação de Testes Funcionais**: Simular o comportamento de usuários e verificar se a aplicação responde conforme esperado.
* **Testes Regressivos**: Reexecutar testes após alterações no código para garantir que novas atualizações não quebrem funcionalidades existentes.
* **Eficiência**: Reduzir o tempo e o esforço necessários para testar manualmente as funcionalidades de uma aplicação, aumentando a produtividade.

## Links Uteis

1. Selenium documentação oficial: <https://www.selenium.dev/pt-br/documentation/>
2. Download do ChromeDriver: <https://googlechromelabs.github.io/chrome-for-testing/>

Como cadastraConfiguração do ambiente

## Configuração do Ambiente

Para executar testes de interface web (Web UI) em seus projetos do TOTVS Automação de Testes, é fundamental configurar corretamente o ambiente Selenium. O WebDriver atua como uma ponte entre seus scripts de teste e o navegador.

## Escolha do Navegador e WebDriver

Primeiramente, defina em qual navegador seus testes serão executados. A escolha mais comum e recomendada para a maioria dos cenários é o Google Chrome.

* Google Chrome: Utiliza o ChromeDriver. É o mais popular, com excelente suporte e ferramentas de desenvolvimento.
* Mozilla Firefox: Utiliza o GeckoDriver. Uma alternativa robusta e de código aberto.

Recomendação: Inicie utilizando o Google Chrome e o ChromeDriver.

## Baixar e Armazenar o ChromeDriver

A etapa mais crítica da configuração é garantir que a versão do seu ChromeDriver seja **exatamente a mesma** da versão do navegador Google Chrome instalado na máquina de execução (seja seu computador local ou um servidor de testes).

> **IMPORTANTE: Sincronização de Versões** O Google Chrome atualiza-se automaticamente. Toda vez que o navegador for atualizado para uma nova versão principal (ex: de 127.x para 128.x), o ChromeDriver correspondente para de funcionar. Você precisará baixar a nova versão do driver e sobrescrever o arquivo antigo para que seus testes voltem a rodar.

**Como baixar a versão correta:**

1. **Verifique a versão do seu Google Chrome:**

   * Abra o Chrome, clique nos três pontos no canto superior direito (`⋮`).
   * Vá em **Ajuda > Sobre o Google Chrome**.
   * Anote a versão completa (ex: `127.0.6533.88`). O mais importante são os primeiros números: `127`.
2. **Acesse o painel oficial de downloads do Chrome for Testing:**

   * O link oficial para encontrar os drivers é: **[Chrome for Testing availability](https://googlechromelabs.github.io/chrome-for-testing/)**
3. **Baixe o ChromeDriver correspondente:**

   * Na página, procure pela versão do seu navegador (ex: `127.0.6533.88`).
   * Na coluna "chromedriver", clique no link correspondente à sua plataforma (normalmente `win64`) para baixar o arquivo `.zip`.
4. **Armazene o arquivo:**

   * Crie uma pasta de fácil acesso em seu ambiente, por exemplo: `C:\TotvsAutomacao\drivers\`.
   * Descompacte o arquivo baixado e coloque o executável `chromedriver.exe` dentro desta pasta.

## Configurar o Caminho do Driver no Helper (Dentro do código da atividade C#)

Agora que o `chromedriver.exe` está na sua máquina, você precisa informar ao helper do TOTVS Automação onde encontrá-lo. Isso é feito através do objeto `_seleniumManager`, que simplifica a inicialização e o gerenciamento do WebDriver.

Utilize o método **`SetupChromeDriver()`**, que recebe como parâmetros o caminho para o **diretório** do driver e as opções de inicialização do Chrome.

> **Atenção:** O caminho a ser informado no método é o da **PASTA** que contém o `chromedriver.exe`, e não o caminho completo do arquivo executável.

**Exemplo de implementação:**

No seu código de inicialização de testes, você fará algo semelhante ao exemplo abaixo.

Criação da Atividade

## Passos para Criar uma Atividade C# com Selenium

1. Criação da Atividade C#

## Criação da Atividade C#:

Crie sua **Atividade C#** no TOTVS Automação de Testes.

* Antes de escrever qualquer código, clique em **Carregar Template** e selecione o **Template Selenium**.
2. Desenvolvimento do Teste 

## Desenvolvimento do Teste

O teste Selenium deve ser implementado dentro do método `Test`. Você tem duas opções para organizar os testes:

* **Atividade com vários testes**: Nessa abordagem, você agrupa diversos testes dentro de uma única Atividade C#, onde cada teste é tratado como um **passo** separado. Isso facilita o controle do progresso da atividade como um todo.
* **Várias atividades com um teste por atividade**: Neste caso, cada atividade C# contém apenas um teste. O **WebDriver** é instanciado uma vez e adicionado ao contexto, permitindo sua reutilização em outras atividades no mesmo projeto.
3. Boas práticas de Teste 

## Boas Práticas de Teste

Siga o padrão **Arrange, Act e Assert** para estruturar seu código de forma clara e fácil de manter:

* **Arrange**: Prepare o ambiente e os dados necessários para o teste, como configurar o navegador, carregar a página e definir os elementos de teste.
* **Act**: Execute as ações do teste, como interagir com os elementos da página (clicar em botões, preencher formulários, etc.).
* **Assert**: Verifique o resultado, validando se as ações realizadas produziram o comportamento esperado (ex.: login bem-sucedido ou exibição correta de uma mensagem).
4. Registro de Resultados e Status

## Registro de Resultados e Status

**Registro de Resultados e Status**:

* Para cada teste, registre o resultado no log:c#RDark
* Defina o status da atividade conforme o resultado de cada teste:
  + - **Adicionar alerta em caso de falha**:c#RDark
* Marcar o teste como falhado:

c#RDark

* Concluir a atividade após o último teste:

RDark

* Abaixo está uma imagem que exemplifica a execução de vários testes Selenium dentro de uma única Atividade C#.

4. Exemplo de Organização de Teste 

## Exemplo de Organização de Teste

* Organize seus testes de forma estruturada, tratando cada teste como um **passo** dentro da Atividade C#. Assim, cada teste representa uma etapa clara e separada no fluxo da atividade, facilitando o controle e a rastreabilidade dos resultados.

#### Arrange

c#RDark

#### Act

c#RDark

#### Assert

c#RDark

### Cadastro de Servidor

#### Arrange

c#RDark

#### Act

c#RDark

*Resultado:*

* Definindo os status dos testes em cada passo da atividade. A variável **"step"**, do tipo `int`, é incrementada no início de cada etapa para acompanhar o progresso e registrar o status de cada teste.

Certifique-se de fechar o navegador após cada passo, se necessário, ou no último passo, utilizando `Dispose` para liberar os recursos do **WebDriver**.

5. Instanciar e Reutilizar o WebDriver no TOTVS Automação de Testes

## Instanciar e Reutilizar o WebDriver no TOTVS Automação de Testes -Linha RM

Para otimizar o uso do **WebDriver** em suas atividades C#, siga estas etapas:

1. **Instancie o WebDriver uma única vez**:

   * Ao iniciar a atividade C#, crie o WebDriver apenas uma vez. Isso evita a necessidade de instanciá-lo repetidamente em cada teste, melhorando a eficiência do código.
2. **Adicione o WebDriver ao contexto do TOTVS Automação de Testes**:

   * Após instanciá-lo, adicione o WebDriver ao contexto da atividade, permitindo que ele seja reutilizado por outras atividades ao longo do projeto:c#RDarkO método `context.Resources.Add<T>()` registra o WebDriver como um recurso disponível para todas as atividades subsequentes que fazem parte do fluxo de testes.
3. **Acessar o WebDriver em outras atividades**:

   * Em qualquer atividade posterior, você pode acessar o WebDriver a partir do contexto do TOTVS Automação de Testes, garantindo que o mesmo objeto seja utilizado de maneira eficiente:c#RDark().First().Value;]]>

     Ao criar os testes, siga o padrão **Arrange, Act e Assert**
6. Fechamento do WebDrive

## Fechamento do WebDriver

**Definir o status e conclusão do teste**:

* Ao final do seu teste, defina o status e a conclusão para que o sistema registre corretamente o resultado da atividade:

  + **Adicionar alerta** em caso de alguma observação importante:c#RDark
    - **Marcar o teste como falhado** se o teste não for bem-sucedido:RDark
    - **Marcar o teste como completo** no final da execução bem-sucedida:RDark
Exemplo Prático

## Exemplo Prático

Imagine que um analista de TI do **sistema RM** precise automatizar o processo de login no **Portal do Aluno** do módulo educacional, garantindo que os alunos possam acessar suas contas e visualizar suas notas de forma confiável. O objetivo dessa automação é validar que o login seja realizado corretamente, verificando se o sistema autentica o aluno com sucesso. Após o login, o teste também deve confirmar se o aluno consegue acessar a área de **consulta de notas** sem falhas, assegurando que a funcionalidade esteja operando conforme esperado após atualizações ou manutenções no sistema.

*Utilização do Selenium no template da Atividade C#*

Helper Selenium

O **Helper Selenium** foi desenvolvido dentro da engine **Selenium** do **TOTVS Automação de Testes** com o objetivo de facilitar a criação de testes automatizados. Ele oferece uma série de métodos práticos para instanciar e gerenciar o **WebDriver**, além de manipular elementos da interface de forma eficiente e precisa.

Esse Helper simplifica todo o processo de automação de testes com o Selenium, fornecendo métodos pré-configurados para:

* **Instanciar e configurar WebDrivers**.
* **Interagir com elementos da interface** (como botões, campos de texto e links).
* **Controlar o fluxo de navegação** em páginas web.
* **Gerenciar o comportamento do navegador** (como esperar por condições específicas, clicar em elementos e preencher campos).

## Métodos do Helper Selenium e suas Funções

1. Instanciar o WebDriver

## Instanciar o WebDriver

* **Instanciar o WebDriver do Chrome com opções**:

  c#RDark
* **Instanciar o WebDriver do Chrome de um diretório específico**:

  c#RDark
* **Instanciar um WebDriver diferente do Chrome com opções (Exemplo: Firefox)**:

  c#RDark
* **Atualizar a largura e altura da janela do WebDriver**:

  c#RDark
2. Interação com a Interface

## Espera por Elementos

* **Esperar por um elemento usando `By` e um tempo em milissegundos**:

  c#RDark
* **Esperar por um elemento pelo ID**:

  c#RDark
* **Esperar utilizando uma função de expressão e o WebDriver**:

  c#RDark drv.FindElement(By.Id("botao")), 5000);]]>
* **Esperar até que o elemento seja clicável usando `ExpectedConditions`**:

  c#RDark

#### Outras Esperas por Condição e Tempo

* **Esperar até o elemento existir usando o ID e um tempo limite**:

  c#RDark
* **Esperar até o elemento ser clicável usando o ID e um tempo limite**:

  c#RDark
* **Esperar até o elemento existir usando `By`**:

  c#RDark
* **Esperar até o elemento ser clicável usando `By`**:

  c#RDark
* **Esperar até o elemento existir utilizando seletor CSS**:

  c#RDark
* **Esperar até o elemento ser clicável utilizando seletor CSS**:

  c#RDark
3. Interação com Elementos

## Interação com Elementos

* **Clicar em um elemento**:

  c#RDarkc#RDark
* **Navegar para uma URL**:

  + **Por string**:c#RDark
  + **Utilizando um objeto `Uri`**:c#RDark
* **Maximizar a janela do navegador**:

  c#RDark
* **Preencher um campo de texto**:

  c#RDarkc#RDark
4. Finalizar e Liberar Recursos

## Finalizar e Liberar Recursos

* **Encerrar o WebDriver e liberar recursos**:c#RDark
5. Utilização do WebDriver em Múltiplas Atividades

## Utilização do WebDriver em Múltiplas Atividades

* **Adicionar o WebDriver ao contexto do TOTVS Automação de Testes**: Para reutilizar o WebDriver em outras atividades, adicione-o ao contexto:c#RDark

---

Saiba mais

O Agent do TOTVS Automação de Testes utiliza a versão **108.0.5359.71** do **Chromedriver**, compatível com o **Chrome versão 108.0.5359.126**. Caso precise usar uma versão diferente do **Chromedriver**, será necessário instanciá-la manualmente na Atividade C#. Consulte a documentação do **Helper Selenium** para mais detalhes sobre como carregar drivers personalizados.

A cada atividade fechar o navegador se necessário. Caso faça isto você deverá instanciar novamente o web driver a cada atividade. Você pode fazer o dispose (Quit) na última atividade de teste.

# FAQ

**P: O que acontece se eu não fechar o WebDriver após um teste?**

R: Se o WebDriver não for fechado corretamente após o teste (usando `webDriver.Quit()`), o navegador pode permanecer em execução em segundo plano, consumindo recursos e potencialmente causando problemas de desempenho nos testes subsequentes.

**P: O TOTVS Automação de Testes suporta testes de API usando Selenium?**

R: Não diretamente. O Selenium é focado na automação de navegadores para testes de interface de usuário. Para testes de API, você pode usar outra ferramenta de automação de API, como o Postman, em combinação com o TOTVS Automação de Testes.
