---
content_hash: 954ddcbbb0f88a73f6362ab10a97e44f9531540f36493359bf2a3b2721b9da3d
fetched_at: '2026-06-29T00:11:32.366969+00:00'
page_id: '746519023'
product: rm
source: tdn-rm
title: Debug Remoto - Ferramentas TCloud
type: documentation
url: https://tdn.totvs.com/display/LRM/Debug+Remoto+-+Ferramentas+TCloud
version: 5
---

**Link para video demonstrando os passos para fazer o debug: <https://drive.google.com/file/d/1QPwzg5iguB9Inqbhfzectiry37O_WyvB/view?usp=share_link>**

**1** - Você precisará baixar a ferramenta de acesso para sftp. <https://winscp.net/eng/index.php>

**2** - Acesse o portal do Tcloud (<https://tcloud.totvs.com.br/login>) os dados para login é usuario e senha de rede totvs, em seguida pesquise pelo código do cliente no campo conta que se encontra no superior da tela, caso não encontre ou não tenha acesso a visão dos ambientes do cliente pesquisado solicitar permissão ao cloud totvs.  
Após acessar você selecionará o ambiente de Troubleshoot. Neste ambiente você terá acesso aos serviços e caminhos para acessar o mesmo externamente.

**3** - Compile a versão RM que irá debugar do cliente, separe as dlls e pdbs do seu produto e transfira para o servidor. Para fazer a transferência você irá precisar parar os serviços de host, isso poderá ser feito pelo acesso no tcloud. O nome do serviço de host no tcloud é "Appserver"

**4** - Pare os serviços "Devops Product Init" e "Devops Tools Update" pois os mesmos são utilizados para realinhar os configs do ambiente. Isso impede que as alterações efetuadas nos configs sejam permanentes até o fim do debug.

**5** - Após acessar o ambiente Tcloud Troubleshoot você terá acesso ao botão no início do ambiente "Informações do ambiente", neste você tem o caminho do "Endereço para o debug remoto".

**6** - Após acessar o ambiente Tcloud Troubleshoot você terá uma visão com vários links e um deles é "Credenciais de SFTP" o caminho e dados de login e senha são utilizados para acessar a instalação do ambiente e configs, através do client de acesso a sftp que você baixou na web de acordo com o Passo 1.  
A instalação do RM está no diretório raiz em: totvs/corporeRM/RM.Net (todas as dlls da instalação se encontram aqui)  
Os configs se encontram no diretório raiz em: files/config no arquivo "configglobal.json"

**7** - Transfira as dlls e pdbs utilizando o cliente que está acessando o diretorio da instalação para a pasta RM.Net.

**8** - Modifique o confique incluindo a tag "IsolateProcess = false" para as configurações de host.

**9** - Reinicie os serviços do host acessando pelo Tcloud o ambiente do cliente.

**10** - Dentro do ambiente no Tcloud acessando o Troubleshoot acima de serviços tem um desenho de um bug  clique no link e então selecione a ação desejada "Iniciar", selecione a versão do seu visual studio e clique em enviar para iniciar o serviço "MSVSMON.EXE" (este serviço deverá estar alinhado a sua versão do Visua Studio assim como o Patch).

**11** - Agora vá no seu Visual Studio e selecione - connection type: "Remote (No authentication)", connection target: "Endereço completo do passo 5"

Se ocorrer erro para encontrar reclamando do MSVSMON.EXE, repita o passo 10.

Após obter sucesso, selecione para o campo - Attach to: "Managed (.Net 4.x)" e então atach o host do ambiente encontrado.

**12** - Você precisará do cliente do RM para executar os processos, para isso acesse o TCloud e vá no botão informações do ambiente e terá o descritivo "Smartclient:" copie o caminho e cole no browser, faça o download do smartcliente do RM e log normalmente.

**13 - DICA:** Faça um debug simples em uma abertura de visão, ocorrendo sucesso. Poderá ir ao processo ou visão na qual você deseja debugar.  
Não obtendo sucesso, refaça o passo 7, pode ser que tenha que fazer varias vezes ele.
