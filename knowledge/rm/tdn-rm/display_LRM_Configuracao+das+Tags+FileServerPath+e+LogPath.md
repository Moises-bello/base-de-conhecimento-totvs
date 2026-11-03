---
content_hash: b91ed5fb0ec88213e3b9d7e798da7502b8ac8633d6c7f2ba579f5c2d5be419cc
fetched_at: '2026-06-29T00:06:09.439221+00:00'
page_id: '203754419'
product: rm
source: tdn-rm
title: Configuracao das Tags FileServerPath e LogPath
type: documentation
url: https://tdn.totvs.com/display/LRM/Configuracao+das+Tags+FileServerPath+e+LogPath
version: 31
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       O objetivo deste documento é mostrar os procedimentos para gravar arquivos gerados em pasta compartilhada, e mostrar como é feita as Configurações das tags FileServerPath e LogPath**.**

# Gravar Arquivos Gerados em Pasta Compartilhada:

---

       Para realizar a gravação de arquivos em pasta compartilhada, proceda com as seguintes orientações abaixo:

       Crie uma pasta compartilhada. Neste exemplo, terá o nome de **ARQUIVOS**

Permissões

É de suma importância que a permissão desta pasta seja criteriosamente definida, a fim de evitar que acessos indevidos ou mal-intencionados sejam realizados à pasta compartilhada

Para facilitar o fluxo, será definido para **exemplificação**, a permissão da pasta ARQUIVOS como compartilhamento para todos. Este tipo de permissão não é de forma alguma recomendado e deve ser utilizado apenas para **testes**.

Atenção:

Utilizar apenas uma única pasta compartilhada na rede em todos os arquivos de configuração.

Utilizar somente pastas compartilhadas na rede.

Não é possível o uso de pastas "MAPEADAS" sejam elas localmente ou via TS por problemas de incompatibilidade dos serviços do Windows conforme informado no link [Serviços e Unidades Redirecionadas](https://msdn.microsoft.com/en-us/library/windows/desktop/ms685143(v=vs.85).aspx).

Finalize todos os aplicativos TOTVS que estejam iniciados na máquina;

Acesse o diretório: C:\totvs\CorporeRM\RM.Net e execute o aplicativo: "RM.Host.ServiceManager.exe" (clicando em desinstalar);

Ainda na pasta RM.Net, edite (em bloco de notas) os arquivos: "RM.Host.exe.config", "RM.Host.Service.exe.config" e "RM.Host.JobRunner.exe.config" **(do Servidor de APP e Jobs)** em seguida clique em propriedades e desmarque o atributo "Somente leitura", aplique e salve. Acrescente as seguintes Tags:

• <add key="FILESERVERPATH" value="\\SERVIDOR\PASTA" />

• <add key="LOGPATH" value="\\SERVIDOR\PASTA" />

* **Observação:** caso utilize [múltiplos hosts](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018408952-Framework-Linha-RM-Frame-Balanceamento-nativo-M%C3%BAltiplos-hosts), efetue a configuração em todos os arquivos config, por exemplo, RM.Host.exe.config, RM.Host1.exe.config, RM.Host2.exe.config / RM.Host.Service.exe.config, RM.Host.Service1.exe.config, RM.Host.Service2.exe.config, etc. false

  Acesse as propriedades da pasta criada e confirme o caminho de rede para inserir corretamente nos arquivos .config

  Onde lê-se SERVIDOR informe o nome do Servidor, e onde lê-se PASTA informe o nome da pasta. Salve as alterações feitas e feche os arquivos.

 Abaixo o exemplo de um arquivo alterado.

xmlExemplo



















]]>

* Ainda na pasta RM.Net execute novamente o aplicativo "RM.Host.ServiceManager.exe" (clicando em instalar);
* Após apresentar a Label INICIADO (em negrito na tela deste aplicativo) acesse novamente o sistema, realizando os testes.
* Confirme as permissões da conta para inicializar o serviço do Host, por exemplo, conta de usuário administrador do domínio:

falseObservação:

Para a instalação em 3 camadas, os procedimentos devem ser realizados nos servidores de APP e JOBS.

# Configuração das Tags FileServerPath e LogPath:

---

**Nota**: **FileServerPath:**

     Definir um único diretório para geração e leitura de arquivos, assim todos os Hosts do ambiente irão gerar os arquivos somente nesse diretório. Desta forma, em ambientes que trabalham em N camadas, devemos adicionar a Tag nos arquivos "RM.Host.exe.config", "RM.host.Service.exe.config" e "RM.Host.JobRunner.exe.config**"**de todos os servidores de APP e Job.

**Exemplo:** <add key=“FileServerPath” value=“\\Servidor\Pasta” />

**LogPath:**

     Definir o caminho onde serão gerados os logs do sistema.

**Exemplo**: <add key=“LogPath” value= “\\Servidor\Pasta” />

false

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.XX

false

**Processo:** Configuração das tags FileServerPath e LogPath

falsefalse

**Status:** Finalizado

false

**Data:** 29/08/2016

false

**Autores:**
