---
content_hash: 8be2c1f4c203acbfdff4aae3df83df18529b9db485f7edb4b3e82cde236938e0
fetched_at: '2026-06-29T00:11:55.808274+00:00'
page_id: '864340179'
product: rm
source: tdn-rm
title: 13 - Download - Agent
type: documentation
url: https://tdn.totvs.com/display/LRM/13+-+Download+-+Agent
version: 17
---

## O que são?

O Agent é um **Client** que facilita a comunicação entre o TOTVS Automação de Testes e a máquina onde as Atividades ou Projetos serão executados. É obrigatório instalá-lo na máquina onde o usuário realizará essas tarefas. Sem o Agent, não será possível executar nenhuma atividade no servidor em questão.

## Para que servem?

O Agent serve para:

* **Execução de Testes**: Realiza a execução dos testes automatizados nas aplicações, garantindo que as funcionalidades sejam validadas conforme definido pelos scripts de teste.
* **Comunicação**: Facilita a comunicação entre o servidor, a ferramenta de automação de testes e a máquina de teste, permitindo o envio e recebimento de comandos, bem como a obtenção dos resultados dos testes.
* **Atualização Automática**: O Agent possui uma funcionalidade de auto-update, que garante que ele esteja sempre na versão mais recente compatível com o servidor do TOTVS Automação de Testes.

# Exemplo de Uso

Como Baixar e Executar.Como Baixar e Executar1. Navegação para Download 

1. Navegue no menu TOTVS Automação de Testes e clique em **Downloads** → **Agent** e o Download do arquivo .**zip** contendo o Agent será instalado automaticamente.
2. Após o download, descomprima o arquivo para um diretório na sua máquina. Recomenda-se realizar essa ação no diretório **C:\** para facilitar à procura dessa pasta.

2. Execução do Agent

O Agent é um executável que gera um processo no sistema operacional, permanecendo em execução contínua enquanto uma sessão de usuário estiver ativa. Para que ele funcione de forma constante em um servidor, é essencial que seja iniciado por um usuário cuja sessão permaneça sempre ativa na máquina. Isso garante que o Agent esteja sempre disponível para executar projetos, sempre que necessário.

## 2.1 - Ações Antes de Executar o Agent:

1. Verifique se todos os arquivos na pasta do Agent estão desbloqueados. Para automatizar essa verificação, execute o seguinte comando no diretório usando o cmd:
2. Certifique-se de que o arquivo *appsettings* está configurado corretamente, apontando para a URL completa do Host do seu TOTVS Automação de Testes na tag *HostAddress*. Abaixo, segue um exemplo de configuração correta desse arquivo:

## 2.2 - Realizando a Execução:

1. Após descomprimir a pasta em questão, entre nela e procure pelo executável **TotvsAutomacaoAgent**.
2. Execute o aplicativo em questão como **Administrador**.

3. Com isso, será aberto um console que registrará a execução da inicialização do Agent naquele servidor. Se tudo correr bem, a última linha do log aparecerá conforme mostrado abaixo, sem registrar nenhum erro. Você poderá então verificar na tabela de Servidores se o servidor em questão está Online. Clique [aqui](https://tdn.totvs.com/display/LRM/5.+Servidores) para saber como visualizar o Status do seu Servidor.

**Dica:** Para executar este programa sempre como Administrador, sem precisar solicitar permissão a cada vez, siga este passo a passo:

1. Clique com o botão direito no executável e selecione "Propriedades".
2. Na aba "Compatibilidade", marque a opção "Executar este programa como administrador".
3. Clique em "Aplicar" e depois em "OK".

Após realizar essas configurações, o aplicativo será executado em modo administrador com apenas dois cliques.

Atualização do Agent

Sempre que precisar atualizar o Agent, você pode baixá-lo novamente e repetir o processo de instalação original. No entanto, o Agent também conta com um recurso de autoatualização que automatiza esse procedimento.

O recurso de auto-update verifica se a versão do Agent instalada no seu ambiente corresponde à versão disponível no host do TOTVS Automação de Testes. Caso as versões sejam diferentes, o Agent será atualizado automaticamente.

Esse processo de autoatualização só ocorre quando o Agent está ocioso e funciona da seguinte maneira:

1. **Verificação de Versão:** O Agent compara sua versão com a versão disponível no host do TOTVS Automação de Testes.

   * **Se as versões forem idênticas**, nenhuma ação é tomada.
   * **Se as versões forem diferentes**, o processo de atualização é iniciado.
2. **Finalização e Preparação:** O Agent é finalizado para garantir que a atualização ocorra de maneira segura e sem conflitos.
3. **Download dos Arquivos:** Os arquivos necessários para a atualização são baixados automaticamente.
4. **Atualização:** Os arquivos são substituídos no diretório onde o Agent está instalado.
5. **Reinício do Agent:** Após a conclusão da atualização, o Agent é reiniciado automaticamente, garantindo que a nova versão esteja em execução.

Este processo garante que o Agent esteja sempre atualizado, sem a necessidade de intervenção manual, mantendo a compatibilidade com o host do TOTVS Automação de Testes.

---

# Saiba mais

Sem o Agent, o TOTVS Automação de Testes não poderá se comunicar com a máquina de teste, impossibilitando a execução de testes automatizados.

O Agent possui uma funcionalidade de auto-update. Ele verifica automaticamente a versão do Agent em relação ao host do TOTVS Automação de Testes. Se houver uma discrepância, o Agent baixa e instala a atualização quando estiver ocioso.

 Para garantir acesso total às funcionalidades do sistema e evitar problemas de permissão, o Agent deve ser configurado para sempre executar como administrador.

Utilize uma conta de serviço que nunca faça logout no servidor onde o Agent está hospedado. Isso garante que o processo do Agent permaneça sempre em execução.

# FAQ

**P:****Como posso garantir que o Agent esteja funcionando corretamente após a instalação?**

R: Após instalar o Agent, você pode realizar um teste de conexão com o servidor do TOTVS Automação de Testes para garantir que ele esteja funcionando corretamente.

**P: O que devo fazer se não conseguir baixar o agent?**

R:Verifique se o navegador bloqueou o download do Agent. Em caso positivo, configure o navegador para não bloquear esse download.

**P: O que devo fazer se não conseguir iniciar a execução do Agent?**

R:Certifique-se de que o usuário responsável por iniciar o Agent possua controle total sobre a pasta do Agent e permissões para executá-lo como Administrador. Além disso, verifique se o arquivo *appsettings* está configurado corretamente e se os arquivos da pasta Agent não estão bloqueados.
