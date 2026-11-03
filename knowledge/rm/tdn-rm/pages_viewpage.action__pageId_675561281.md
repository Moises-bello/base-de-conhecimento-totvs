---
content_hash: 2a5c1b07926da81bb7a6d20cf34b10e6bfc1c48da8c516fc2be87a5a2214113d
fetched_at: '2026-06-29T00:11:17.011565+00:00'
page_id: '675561281'
product: rm
source: tdn-rm
title: Inventário  
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=675561281
version: 6
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | Totvs Inventário Mobile |
| **Versões:** | 12.1.29 |
| **Ocorrência:** | Inventário Mobile |
| **Ambiente:** |  |
| **Passo a passo:** | 1 - Instalar o aplicativo pela loja (ou APK) no celular que será utilizado para a coleta.  2 - Expor os WebServices do RM através do Host, editando o arquivo de configuração do Host no servidor (RM.Host.exe.config ou RM.Host.Service.exe.config) e colocando as Tags abaixo, dentro de *<appSettings>*:       <add key="DEFAULTDB" value="BDTESTE"/>  → o value deve ser o mesmo nome do **ALIAS** da base de dados que irá ser utilizada.      <add key="APIPORT" value="8051"/>  → o value deve ser uma **porta disponível** para uso no servidor.    **Observação importante: Este arquivo de configuração deve conter apenas uma tag apontando a porta disponível e o banco de dados, caso tenha mais de uma tag apontando para portas diferentes ou banco de dados diferentes, o aplicativo não irá conectar corretamente.**  Mais informações as configurações do Host podem ser obtidas nestas páginas: [Como Expor os Web Services do RM através do Host](https://tdn.totvs.com/pages/viewpage.action?pageId=89620766) e [Configurando HttpPort e ApiPort.](https://tdn.totvs.com/display/LRM/Configurando+HttpPort+e+ApiPort)  3 - O arquivo Alias.dat, deve conter essa base que foi colocada no host.  4 - Caso utilize o RM.Host.exe, o mesmo deve ser iniciado "*como Administrador*". Se utilizar o RM.Host.Service não é necessário pois o serviço já é iniciado com privilégios administrativos;  Faça o Download do App através do QRcold abaixo, ou digite Meu patrimônio na Play Store.  5 - Abra o aplicativo no celular e leia o QR Code de configuração ou clique em *"Não tenho QR Code. E agora?"*  6 - Se não possuir o QR Code, informe o IP do servidor em que o Host está sendo executado (configurado nos passos anteriores);       Formato : [http://ipservidor:porta](http://ipmaquinaporta/) (a porta se refere a mesma porta configurada no arquivo host)       Exemplo : [http://192.168.12.123:8051](http://192.168.17.154:8051/)     | Atenção  Para que o APP consiga acessar a base de dados o Celular em que está instalado deve estar na mesma rede do servidor do Host ou este deve estar acessível via Web. Para tanto, orientamos que siga os passos contidos [neste documento](https://tdn.totvs.com/pages/viewpage.action?pageId=244911449) e, em caso de dúvidas, entre em contato com o suporte de Frame Work. | | --- |      * Após realizar as parametrizações acima, acesse a API abaixo no browser no seu computador para verificar se conexão esta ok.  <http://localhost:8051/api/pat/v1/versions>   |  | | --- |   Api que busca os dados de versão do host que está sendo usado, deve retornar este resultado.   * **Etapas no TOTVS Gestão Patrimonial**   7 - Rodar o Atualizador da versão 12.1.29 ou superior para atualizar a base de dados.  8 - Cadastrar os inventários no Totvs Gestão Patrimonial   | Cadastro   * [Cadastro do Inventario.](https://tdn.totvs.com/pages/viewpage.action?pageId=539698834) | | --- |   9 - Rodar o processo Gerar Lista de Patrimônios no Totvs Gestão Patrimonial    | Processo                                                                                                                                           * [Gerar lista de patrimônios](https://tdn.totvs.com/pages/viewpage.action?pageId=552577805) | | --- |   10 - Pronto! Para mais detalhes sobre a utilização do app, confira nossa documentação completa.   | Acesso APP Meu patrimônio   * [Login Meu Património](https://tdn.totvs.com/pages/viewpage.action?pageId=549505682) | | --- | |
| **Observações:** | **[Documentação completa.](https://tdn.totvs.com/pages/viewpage.action?pageId=539698831)** |
