---
content_hash: 23de14a0466891441efd31d1967f90d4dc6b3a5015a772ab4d5ba1b29b09c6da
fetched_at: '2026-06-29T00:08:57.114912+00:00'
page_id: '353273309'
product: rm
source: tdn-rm
title: Debug Remoto
type: documentation
url: https://tdn.totvs.com/display/LRM/Debug+Remoto
version: 5
---

**Debug Remoto**

Você pode depurar um aplicativo implantado em um computador remoto através do Visual Studio. Para fazer isso, você deve usar o depurador remoto do Visual Studio.

**Requisitos**

O computador remoto deve estar executando um dos seguintes sistemas operacionais:

* Windows 10 (não phone)
* Windows 8 ou 8.1 (phone não)
* Windows 7 Service Pack 1
* No Windows Server 2012 ou Windows Server 2012 R2
* Windows Server 2008 Service Pack 2, Windows Server 2008 R2 Service Pack 1

**Configuração de rede**

O computador remoto e o computador do Visual Studio devem ser conectados por uma rede, um grupo de trabalho, um grupo doméstico ou então conectados diretamente por meio de um cabo Ethernet. Não há suporte para a depuração entre dois computadores conectados por meio de um proxy. Depuração em uma conexão de baixa largura de banda, como dial-up da Internet, ou de alta latência, ou pela Internet entre países não é recomendado e pode falhar ou ser muito lento.

**Instruções para executar o depurador remoto**

Você deve encontrar o depurador remoto (msvsmon.exe) no computador com o Visual Studio Community, Professional ou Enterprise já instalado. Localize **msvsmon.exe** no diretório correspondente de sua versão do Visual Studio. Para o Visual Studio Enterprise 2017:

*Programa arquivos (x86) \Microsoft Visual Studio\2017\Enterprise\Common7\IDE\Remote Debugger\x86\msvsmon.exe*   
 *Programa arquivos (x86) \Microsoft Visual Studio\2017\Enterprise\Common7\IDE\Remote Debugger\x64\msvsmon.exe*

No computador remoto, onde será executado o RM.exe, crie uma pasta com o nome "Remote Debugger" no diretório onde o RM está instalado. Ex: "C:\TOTVS\CorporeRM\Remote Debugger".

Copie todos os arquivo da pasta contendo o arquivo **msvsmon.exe** para esta pasta recém criada no computador remoto.

**Configurar o depurador remoto**

1. Você deve ter permissões administrativas no computador remoto.

2. Localize o aplicativo **msvsmon.exe** no computador remoto e execute o mesmo. Você deve clicar com o botão direito no aplicativo e escolher a opção **executar como administrador**.

3. Ao executar o depurador remoto pela primeira vez, a caixa de diálogo abaixo será exibida.

4. Selecione os tipos de rede que você deseja usar. Pelo menos um tipo de rede deve ser selecionado. Se os computadores são conectados por meio de um domínio, você deve escolher o primeiro item. Se os computadores estiverem conectados por meio de um grupo doméstico ou de grupo de trabalho, você precisa escolher o segundo item ou o terceiro conforme necessário.

5. Escolha "**Configure remote** **debugging**" para configurar o firewall e iniciar a ferramenta.

6. Quando a configuração estiver concluída, a janela de depurador remoto é exibida.

7. Neste momento o depurador remoto está aguardando uma conexão. Anote o nome do servidor e o número da porta que será exibido, porque isso deve corresponder à configuração que você irá utilizar posteriormente no Visual Studio.

**Depurando através do Visual Studio**

1. Abra o projeto que se deseja depurar.

2. Compile o projeto.

3. Copie as DLL´s geradas juntamente com os arquivos \*.pdb para o computador remoto. Obs.: Lembre-se sempre de realizar o backup das DLL´s originais.

4. No Visual Studio, defina um **break point** em algum lugar no código que é facilmente acessado. Por exemplo, você pode definir um ponto de interrupção em um evento do botão.

5. Neste momento, estamos prontos para iniciar a depuração. Vá na opção **Debug – Attach** **To** **Process**, conforme figura abaixo:

6. Na opção "**Connection Target**" devemos escolher o computador remoto, cujo nome do servidor e o número da porta foram exibidos ao executar o arquivo **msvsmon.exe**. Veja figura abaixo:

7. Após selecionar o computador remoto, todos os processos iniciados no mesmo serão exibidos. Selecione então os processos **RM.exe** e **RM.Host.exe** e clique em **Attach**. Lembrando que o RM.exe deve ser selecionado apenas quando se quiser depurar a camada Client.

8. Feito isto, basta executar o processo que se deseja depurar que o Visual Studio irá parar no Break Point definido.

**Considerações Finais**

Para obter instruções detalhadas sobre debug remoto, consulte os links abaixo:

<https://docs.microsoft.com/pt-br/visualstudio/debugger/remote-debugging>

<https://msdn.microsoft.com/pt-Br/library/y7f5zaaa.aspx>
