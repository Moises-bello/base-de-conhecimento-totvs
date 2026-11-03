---
content_hash: 180f530aaceb48bb424e427b873ae7444e96f04bdcba0d54f3dd0c8e947f0f29
fetched_at: '2026-06-29T00:08:27.483249+00:00'
page_id: '271413377'
product: rm
source: tdn-rm
title: Serviço de host não inicia ou erro de Broker
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271413377
version: 10
---

# Serviço de host não inicia ou erro de Broker

|  |  |
| --- | --- |
| **Produto:** | Framework |
| **Versões:** | 11.8X / 12.1.X |
| **Ocorrência:** | Serviço de Host não inicia ou erro de Broker |
| **Ambiente:** | Framework |
| **Passo a passo:175px** | Importante A partir da versão ***12.1.2209*** não existirá mais a opção de apagar o arquivo **\_Broker.Dat**, pois essa ação não se faz mais necessário na linha RM.     Introdução Sempre que ocorrer erro de Broker,  queda do serviço de host sem nenhum motivo aparente, serviço de host não inicia, serão válidas algumas verificações conforme descrito abaixo:    **Passo a Passo**  Antes de qualquer coisa, o teste mais rápido a ser feito, é desinstalar o serviço de host:   1. Acesse UNIDADE:\totvs\CorporeRM\RM.Net e execute como administrador o aplicativo RM.Host.ServiceManager.exe; 2. Marque a flag "**Deletar \_Broker.Dat**" e instale o serviço novamente; 3. Clique em desinstalar; 4. Instale novamente o serviço e verifique se a inconsistência persiste.   Porém, este erro pode ser de serviço de host não iniciado ou não localizado. NÃO INICIADO Os motivos deste erro podem ser bloqueios de conexão por aplicativos/ferramentas de segurança, tais como:   1. 1. Antivírus bloqueando    2. Firewall    3. Outro programa utilizando a porta 80:50    4. UAC (Controle de Conta de Usuário) habilitado do Windows Server 2008, Vista, 7, 8 e 10.    5. Windows Defender   Outras opções são:  Na pasta UNIDADE:\totvs\corporerm\rm.net executar o arquivo RM.Host.ServiceManager.exe  Nesta tela você deverá desinstalar o serviço e instalar novamente.  Nesta etapa terá 3 opções  de instalação:  NetworkService, Local System ou Informando usuário e senha específicos (senha do administrador de Rede)  Caso o serviço não seja iniciado em uma das opções, testar as demais citadas.  Deverá ser verificado se na pasta RM.NET (C:\CorporeRM\RM.Net), os arquivos RM.Host.Service.exe.config e RM.Host.exe.config, estão com mesmo endereço onde está localizado os arquivos Exe RM.Host.ServiceManager.exe e RM.Host.exe.  Exemplo abaixo:    xmlRM.Host.ServiceManager.exe / RM.Host.exetrue                    \*\* este endereço tem que estar igual a pasta física onde se encontra o exe do serviço\*\*                                      Se mesmo após todas as tentativas acima o serviço ainda não estiver iniciando, verificar antivírus, Firewall, UAC  e porta 8050. ObservaçãoSe estiver em 3 camadas, verifique o servidor onde está sendo executado o serviço.  NÃO LOCALIZADO. Se estiver tentando abrir um aplicativo, e o mesmo estiver em 3camadas, deverá ser observado se o arquivo .config (ex: RMFluxus.exe.config, RM.exe.config (localizados em UNIDADE:\TOTVS\CorporeRM\RM.Net) / web.config (arquivo de configuração do RM Portal (UNIDADE:\TOTVS\CorporeRM\Corpore.Net))) está buscando informação do servidor correto.    xml RMFluxus.exe.configtrue        \*\* nome do servidor\*\*        ]]>   ObservaçãoVerificar ainda, se a tag deste arquivo estiver true e no servidor de aplicação no arquivo config do serviço de host (RM.Host.Service.exe.config) estiver com a tag 3 camadas false, ou vise e versa, o erro também ocorrerá. |
| **Observações:** | ARQUIVO DE LOG DE ERROS Caso haja falhas na subida do *Host* como *Serviço*, o arquivo **\_brokerErrors.log** será gerado na pasta raiz da instalação.  Este arquivo contém as mensagens de falhas ocorridas ao tentar subir o *Host*.  Exemplo: |
