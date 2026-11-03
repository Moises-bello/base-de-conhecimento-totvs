---
content_hash: c58beff952153e5c534b889b4ebbb26b9256e5bdf30a3bfb5ce12f78eb04a34f
fetched_at: '2026-06-29T00:11:21.150139+00:00'
page_id: '687766438'
product: rm
source: tdn-rm
title: 2.7.1 - Script WinForms
type: documentation
url: https://tdn.totvs.com/display/LRM/2.7.1+-+Script+WinForms
version: 43
---

## O que é?

Scripts Windows Forms são automações criadas utilizando o TOTVS Automação de Testes, uma ferramenta que permite a gravação e execução de interações com a interface gráfica (Windows Forms) do ambiente RM. Esses scripts simulam ações manuais no sistema, facilitando testes funcionais e de regressão.

## Para que serve?

A criação de scripts Windows Forms no TOTVS Automação de Testes serve para automatizar processos repetitivos de testes no ambiente RM, garantindo que funcionalidades do sistema sejam validadas de forma eficaz, rápida e sem a necessidade de interação manual contínua.

## Exemplo de Uso

Como cadastrarComo cadastrar1. Navegação para o cadastro.

1. Navegue no menu do TOTVS Automação de Testes e clique em: **Atividades →** **Windows** → **Script WinForms.**
2. Na tabela que será mostrada, clique no botão verde em destaque para criar **Atividade de Script WinForms.**
2. Link para Definir cabeçalho (Nome e nível de acesso)

[Clique aqui para obter as informações do cabeçalho](https://tdn.totvs.com/pages/viewpage.action?pageId=859591806)

3. Preenchimento dos CamposVersão

Especifica a versão da atividade em questão. O objetivo de versionar uma atividade é para quando necessitamos ter mais de uma atividade em versões diferentes. Isso irá nos auxiliar a ter um histórico de atualizações e assegurar que as mudanças feitas sejam rastreáveis e reversíveis, se necessário.

Se for necessário utilizar mais de uma versão do RM no seu ambiente, é recomendado que a versão da atividade seja compatível com o sistema RM em uso. Caso contrário, pode-se optar por uma versão padrão de sua preferência.

*Exemplo utilizando a versão do RM*

*Exemplo utilizando a versão padrão*

Descrição de Atividade 

Fornece uma descrição detalhada da atividade, explicando seu propósito e operações, facilitando a compreensão e manutenção futura.

Servidor para gravação

Selecione o servidor onde o script será gravado. O servidor deve estar previamente cadastrado.

(Clique [aqui](https://tdn.totvs.com/display/LRM/5.+Servidores#Cria%C3%A7%C3%A3odeumgrupo--1297575106) para obter mais informações sobre os servidores).

O Agent deve estar iniciado e o ambiente RM em execução.

Preparação do Ambiente RM

## Preparação do Ambiente RM

Passo a passo para configuração do ambiente WinForms:

* Fazer o download e seguir a documentação dos [Plugins WinForms](https://tdn.totvs.com/display/LRM/Plugin+Winforms+-+Download).
* Verificar o ambiente do RM**:**

  + A pasta **TestFlow** deve estar no diretório **TOTVS/CorporeRM/RM.Net**
  + Certifique-se de que o RM está instalado e funcionando corretamente no [Servidor](https://tdn.totvs.com/display/LRM/5.+Servidores#Cria%C3%A7%C3%A3odeumgrupo--1297575106) onde irá gravar o seu Script WinForms.
* Executar o Agent do TOTVS Automação de Testes:

  + Verifique se o [Agent](https://tdn.totvs.com/display/LRM/Download+-+Agent) do TOTVS Automação de Testes está em execução no servidor e se ele está sendo executado como administrador.
* Carregar o host do RM:

  + Abra o Host do RM como administrador no servidor onde irá utilizar.
* Abra o CMD e digite o comando: `netstat -ao`. Em seguida, verifique se há um serviço em execução na porta 5000.
* Criar um atalho para o RM.exe:

  + Localize o arquivo Rm.exe no servidor.
  + Crie um atalho para ele e, na linha de comando do atalho, adicione o seguinte parâmetro: `" /automationtest"`. Este parâmetro permite a gravação das telas do RM. e desativa qualquer janela ou formulário que seja aberto após o login.
  + Exemplo:
* Iniciar o RM pelo atalho:
  + Execute o RM através do atalho criado, certificando-se de que está a ser executado como administrador.

Com esses passos, o ambiente estará preparado para a gravação do Script WinForms.

Variáveis de Ambiente

As Variáveis de Ambiente são utilizadas para configurar e personalizar o comportamento da Atividade. Elas permitem definir valores específicos ou dinâmicos que podem ser usados durante a execução dos testes, assegurando que o teste execute conforme o ambiente em que o mesmo é executado. As Variáveis de Ambiente são cadastradas no cadastro de Ambiente onde informamos os valores fixos ou de forma dinãmica no cadastro de Script SQL.

Consulte quais campos permitem o uso das Variáveis de Ambiente nessa Atividade:

[Script WinForms - Variáveis de Ambiente.](https://tdn.totvs.com/pages/viewpage.action?pageId=874592146)

Gravando Script WinForms1. Renderização de Componentes

## Renderização de Componentes

* Com o ambiente devidamente configurado, o TOTVS Automação de Testes permite a leitura e execução remota de componentes C#. Os componentes exibidos na tela são renderizados em tempo real, e os scripts são gravados utilizando os nomes desses componentes.

* Ao clicar em um item renderizado, a ação será registrada à direita, exibindo o passo a passo. O clique no TOTVS Automação de Testes também será executado no RM. Essa ação será gravada no TOTVS Automação de Testes e reproduzida no RM.

Interações com os Componentes 

## Interações com os Componentes

Após selecionar a ação desejada, o sistema cria automaticamente uma nova entrada na Timeline, localizada à direita da interface. Esta entrada incluirá todos os parâmetros específicos da ação escolhida.

Ao clicar no componente desejado, um pop-up será exibido com três opções de ações disponíveis para o componente:

* **Click**: Executa um clique simples no componente.
* **Duplo Click**: Realiza dois cliques consecutivos no componente.
* **Setar Texto**: Permite inserir texto no componente, preenchendo o campo com o valor informado no modal.

Na Timeline de Ações é possível: 

**Alterar a ordem que as Ações são executadas:**

Reorganização da Sequência de Ações

## Reorganização da Sequencia de Ações

Você pode reorganizar a sequência de execução das ações gravadas, simplesmente arrastando-as para a posição desejada, garantindo total controle sobre a ordem de execução. Essa funcionalidade é útil para ajustar a lógica das operações sem a necessidade de regravar o script.

**Adicionar Ações de timer (delay antes de executar a próxima ação)**;

Seção Entre Ações

## Seção entre ações

Os campos relacionados ao Tipo de Tempo**:** Fixo ou Randômico servem para definir como o intervalo entre as ações será configurado no script.

**Fixo**: Define um intervalo constante entre cada ação do script. Ao escolher este tipo, o tempo entre as ações será sempre o mesmo, conforme configurado.

* Aqui você define o tempo exato de espera entre a execução de cada ação.

**Randômico**: Neste modo, o intervalo entre as ações é variável. O sistema irá gerar tempos aleatórios dentro de um intervalo mínimo e máximo, permitindo uma variação no tempo de espera entre cada ação.

* Aqui você define o tempo de espera entre as ações varia aleatoriamente dentro do intervalo definido

**Configurar o tempo de espera do Script após abrir uma janela antes de executar a próxima ação;**

Seção Aguardar Janelas

## Seção Aguardar Janela

Esta funcionalidade permite definir o tempo de espera do script após a abertura de uma janela, garantindo que ela esteja totalmente carregada antes da próxima ação. A opção Aguardar Janelas é crucial para manter a estabilidade do script, evitando que ele interaja com uma interface ainda não preparada.

**Fixo**: Aqui, você define um tempo constante de espera entre a abertura da janela e a próxima ação. Quando configurado, o Script sempre aguardará o mesmo tempo definido, garantindo consistência na execução.****Randômico:**** Aqui, você define um tempo de espera aleatório dentro de um intervalo, garantindo que a janela seja carregada antes de continuar o Script, simulando variações no tempo de resposta****.****

**Configurar o tempo entre ações baseado no desempenho durante a execução do Script Winforms no computador:**

Seção Memória e CPU

* **Quando a memória atingir (%)**: Define o limite de uso de memória (em percentual) que, ao ser alcançado durante a execução do script, aciona o aumento dos timeouts. Esse parâmetro permite que o sistema ajuste automaticamente o tempo de espera entre as ações quando o uso de memória atinge o valor definido.

  + **Aumente os timeouts em (vezes)**: Determina o fator de aumento dos timeouts. Por exemplo, se definido como "2", o tempo de espera entre as ações será dobrado quando o limite de memória for atingido.
* **Quando a CPU atingir (%)**: Estabelece o percentual de uso da CPU que, ao ser alcançado durante a execução do Script, também acionará o aumento dos Timeouts. Isso é útil para evitar sobrecarga quando o processamento do computador está próximo do limite.

  + **Aumente os timeouts em (vezes)**: Define o multiplicador para aumentar o tempo de espera entre as Ações quando o limite de uso da CPU for atingido. Assim como no campo de memória, o valor aqui indicado será aplicado para ajustar o tempo entre as ações proporcionalmente ao nível de uso da CPU.

2. Exemplo Prático

## Exemplo Prático

Um analista do produto RM precisa automatizar a validação de cadastros no sistema, especificamente para o cadastro de "Tipo de Característica Imobiliária". Para isso, ele utilizará o **ScriptWinForms** do **TOTVS Automação de Testes** para simular interações com o sistema RM e validar a criação correta dos dados.

Após configurar o Script, o analista pode optar por executar a sequência completa de ações programadas. O TOTVS Automação de Testes então reproduz automaticamente todos os cliques, inserções de texto e interações previamente configuradas no sistema RM, simulando com precisão o comportamento do usuário. Durante essa execução, o sistema realiza o cadastro da nova característica imobiliária conforme as etapas definidas, garantindo que os dados sejam inseridos corretamente e que o fluxo do processo seja fiel ao que seria realizado manualmente.

Além disso, o **TOTVS Automação de Testes** permite monitorar o progresso da execução em tempo real, identificando possíveis falhas ou erros no processo. Se algum problema for detectado, o analista pode revisar o Script, ajustar ações ou parâmetros, e reexecutar o teste até que o cadastro seja validado com sucesso. Isso assegura não apenas a automação do processo, mas também a confiabilidade na criação de novos cadastros no ambiente RM.

*Ações gravadas do Script Winforms no TOTVS Automação de Testes*

*Script WinForms em execução no RM*

3. Troubleshooting (Resolução de Problema)

## Troubleshooting (Resolução de Problema)

Os componentes **WinForms** podem não ser totalmente renderizados na tela, resultando em elementos que não aparecem ou não estão totalmente visíveis, o que pode comprometer a interação e o correto funcionamento do Script Automatizado. Este problema pode ocorrer devido a atrasos no carregamento da interface, uso excessivo de recursos do sistema, ou resolução de tela inadequada, exigindo ajustes no tempo de espera ou validação da interface antes da execução das ações.

## Sintoma

A tela não renderiza completamente todos os componentes, resultando em elementos ausentes ou incompletos, o que pode prejudicar a usabilidade e execução do sistema. Além disso, arquivos podem estar bloqueados pelo Windows, impedindo o acesso ou modificação, o que geralmente ocorre devido a permissões insuficientes, processos em execução ou restrições de segurança do sistema operacional.

***Arquivos bloqueados pelo Windows***

## Resolução

Para resolver o problema, é necessário desbloquear as DLLs na pasta do TOTVS Automação de Testes, pois o Windows pode estar bloqueando o download e execução desses arquivos por questões de segurança.

Siga os seguintes passos:

1. Pressione as teclas "Windows + R" e digite o comando "gpedit.msc"
2. Na esquerda expanda as pastas para **Configuração do Usuário** >  **Modelos Administrativos** > **Componentes do Windows** > **Gerenciador de Anexos** e abra o item Não preservar informações de zona em anexos de arquivo.
3. Altere o estado do Checkbox de **Não configurado** para **Habilitado** e, em seguida, clique em Aplicar e **OK**.
4. Faça o download dos Plugins novamente através do TOTVS Automação de Testes. (Clique [aqui](https://tdn.totvs.com/display/LRM/Plugin+Winforms+-+Download) para saber mais sobre os plugins WinForms)
5. Extraia o zip instalado no diretório do RM.exe

Após a conclusão dos passos, os componentes **WinForms** serão completamente carregados e estarão prontos para utilização. Certifique-se de que todas as dependências foram corretamente instaladas para garantir o funcionamento ideal.

---

# Saiba mais

Caso o RM seja aberto antes do Agent, não será criado o serviço para que o TOTVS Automação de Testes enxergue o seu ambiente.

Lembre-se de carregar o RM através de um atalho que contenha em sua linha de comando o parâmetro /automationtest.

Durante a gravação no ScriptWinForms, certifique-se de que cada ação gravada esteja na ordem correta, a fim de evitar conflitos no seu script.

Para facilitar a localização do componente a ser clicado na tela de gravação do Script Winforms, utilize a combinação de teclas CTRL + F.

Por se tratar de um nível superior na pirâmide de testes, este tipo de teste tende a ser mais demorado e exige uma atenção redobrada, pois envolve a validação de múltiplos componentes e a integração entre eles.

# FAQ

**P: Ao selecionar o servidor desejado, a conexão com a atividade de WinForms não foi estabelecida. Qual é a solução para esse problema?**

R: Verifique se o Agent está online e funcionando corretamente, e assegure-se de que o ambiente RM foi aberto utilizando o atalha com a tag "/automationtest" e também está ativo e operando normalmente. Além disso, verifique se a pasta **TestFlow** está no diretório **TOTVS/CorporeRM/RM.Net.**

**P: Como verificar se o Agent está funcionando corretamente para a execução da Atividade de Script WinForms?**

R**:** Abra o CMD e digite o comando: `netstat -ao`. Em seguida, verifique se há um serviço em execução na porta 5000

**P: Posso clicar em algum componente no RM durante a execução durante a Atividade do ScriptWinForms?**

R: Se o componente a ser clicado estiver corretamente configurado no ScriptWinForms e alinhado com o timeout das ações, a execução não será afetada. No entanto, é aconselhável evitar quaisquer situações que possam gerar conflitos, assegurando uma execução fluida e sem interrupções no ScriptWinForms.
