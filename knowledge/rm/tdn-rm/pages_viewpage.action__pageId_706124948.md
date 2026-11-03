---
content_hash: 797acaa0427c055b91d92d78a4921b041b126b43fa439f46ec63604a59029d2e
fetched_at: '2026-06-29T00:11:22.603962+00:00'
page_id: '706124948'
product: rm
source: tdn-rm
title: Passo a passo para utilização do aplicativo - Minha Contagem de Estoque
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=706124948
version: 22
---

Preparando o ambiente, siga os passos

1 - Instalar o aplicativo no celular que será utilizado para realizar a coleta de dados do inventário

* Google Play (<https://play.google.com/store/apps/details?id=com.totvs.minhacontagemestoque>)
* Apple Store (<https://apps.apple.com/app/minha-contagem-de-estoque/id1639410691>)

2 - Expor os WebServices do RM através do Host, editando o arquivo de configuração do Host no servidor (RM.Host.exe.config ou RM.Host.Service.exe.config) e colocando as Tags abaixo, dentro de *<appSettings>*:

     <add key="DEFAULTDB" value="BDTESTE"/>  → o value deve ser o mesmo nome do **ALIAS** da base de dados que irá ser utilizada.  
     <add key="APIPORT" value="8051"/>  → o value deve ser uma **porta disponível** para uso no servidor.

**Observação importante: Este arquivo de configuração deve conter apenas uma tag apontando a porta disponível e o banco de dados, caso tenha mais de uma tag apontando para portas diferentes ou banco de dados diferentes, o aplicativo não irá conectar corretamente.**

Mais informações as configurações do Host podem ser obtidas nestas páginas:



3 - O arquivo Alias.dat, deve conter essa base que foi colocada no host.

4 - Caso utilize o RM.Host.exe, o mesmo deve ser iniciado "*como Administrador*". Se utilizar o RM.Host.Service não é necessário pois o serviço já é iniciado com privilégios administrativos;

5 - Abra o aplicativo no celular e leia o QR Code de configuração ou clique em *"Não tenho QR Code. E agora?"*

**DICA!** O QR Code pode ser facilmente gerado utilizando recurso nativo no sistema, veja:

* + [Como gerar o QRCode de configuração](https://tdn.totvs.com/pages/viewpage.action?pageId=706146430)

6 - Se não possuir o QR Code, informe o IP do servidor em que o Host está sendo executado (configurado nos passos anteriores);

     Formato : [http://ipservidor:porta](http://ipmaquinaporta) (a porta se refere a mesma porta configurada no arquivo host)

     Exemplo : [http://192.168.12.123:8051](http://192.168.17.154:8051)

Atenção

Para que o App consiga acessar a base de dados o Celular em que está instalado deve estar na mesma rede do servidor do Host ou este deve estar acessível via Web. Para tanto, orientamos que siga os passos contidos  e, em caso de dúvidas, entre em contato com o suporte.

**Etapas no TOTVS Gestão de Estoque, Compras e Faturamento**

7 - Rodar o Atualizador da versão 12.1.2205 ou superior para atualizar a base de dados.

Atenção

O App é compatível com " TOTVS - Gestão de Estoque, Compras e Faturamento - BackOffice (Linha RM)", versão 12.1.2205 ou superior

8 - Utilização do inventário no Totvs Gestão de Estoque, Compras e Faturamento

Regras para o inventário poder utilizar o app "Minha Contagem de Estoque"

Lista somente os produtos que estão vinculados a um endereçamento de estoque, e o endereçamento deve ter código de barra associado:

[Endereçamento do produto](https://tdn.totvs.com/pages/viewpage.action?pageId=664205609)

Lista somente os produtos que possuem um código de barras associado:

[Defina o código de barra para o produto](https://tdn.totvs.com/pages/viewpage.action?pageId=423938817)

Atenção

Lista somente os inventários definidos com tipo "Produto" e "Lote"

9 - Pronto! Para mais detalhes sobre a utilização do app, confira nossa documentação completa.

Documentação Completa

* [Documentação - "Minha Contagem de Estoque"](https://tdn.totvs.com/display/LRM/Minha+Contagem+de+Estoque+-+APP)

10 - Requisito Essencial do Aplicativo.

* Para garantir o funcionamento adequado do aplicativo, é necessário autorizar o uso da câmera no dispositivo.

Dicas de Conexão

Ao tentar conectar, caso receba alguma mensagem de erro ou não consiga acessar o app verifique os itens abaixo:

* Verifique junto à sua infraestrutura a possibilidade de desativar o firewall na máquina hospedeira do host e/ou criar regras de entrada para permitir conexões na porta utilizada para as APIs do Host.

Uma alternativa para verificar se as conexões às APIs do Host estão sendo possíveis através do aparelho celular é tentar acessar pelo browser do próprio celular algum endereço da API, como o de verificação de versão, por exemplo:  <http://192.168.0.50:8051/api/est/v1/services/healthcheck> (lembrando de substituir o IP e Porta pelos valores utilizados pela empresa.

Se o resultado obtido no browser do celular for semelhante à imagem abaixo, quer dizer que o acesso à API está disponível e o celular conseguiu se conectar com sucesso. Neste caso o app "Minha Contagem de Estoque " também deveria conseguir se conectar.
