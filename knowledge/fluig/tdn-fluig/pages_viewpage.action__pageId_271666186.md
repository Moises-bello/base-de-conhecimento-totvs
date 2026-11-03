---
content_hash: b2402b696d3c235fea2222208a9e2ee7f7e33fc587426f7d9ea7b5b341526ac8
fetched_at: '2026-06-28T21:35:24.813856+00:00'
page_id: '271666186'
product: fluig
source: tdn-fluig
title: Guia de atualização da plataforma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271666186
version: 93
---

Fique atento!

Esta página é válida a partir da **atualização 1.6** e **superiores**.

Caso possua a atualização **1.5.13 ou inferior** acesse

2.\*ndice

# Objetivo

---

O objetivo deste guia é apresentar os procedimentos necessários para efetuar a atualização do TOTVS Fluig.

Para acompanhar informações sobre Atualização programada e sobre o Ciclo de atualização obrigatório, acesse .

Plataforma em Cloud

A instalação, atualização ou configuração da plataforma para quem contratou o serviço de *Cloud* é realizada por uma equipe de atendimento específica. Para solicitar o atendimento, abra um *ticket* para a equipe de *Cloud* pela página de [suporte](http://suporte.totvs.com).

# Pré-requisitos

---

Veja a seguir os pré-requisitos necessários para a correta atualização da sua plataforma.

## Gerais

---

* É imprescindível **parar** todos os serviços antes de atualizar a plataforma: fluig, fluig\_Indexer, fluig\_Realtime, fluig\_memCached ou redis (para ambientes de alta disponibilidade ou com servidores de cache configurados) e Prizm (esse serviço só existe se você utiliza o Fluig Viewer localmente).

  Importante!

  Lembramos que, para ambientes de alta disponibilidade, todos os serviços devem estar parados e nenhum arquivo ou pasta deve estar aberto (isso inclui mapeamento de pastas ou arquivos).
* Realizar o backup da instalação, conforme descrito no guia .

* Antes de atualizar a plataforma no ambiente de produção,  e realize os testes necessários.

* Recomendamos que seja realizado o *download* sempre da **última versão do instalador**na [Central do cliente](https://suporte.totvs.com/portal/p/10098/download#000035).

  Importante!

  Ressaltamos que não disponibilizamos o instalador para **pacotes específicos**que não estejam disponíveis na Central do cliente. Sempre disponibilizamos o instalador para a última atualização disponível, que já contempla todas as correções e melhorias liberadas.
* Caso venha a ocorrer algum problema durante a instalação, antes de fazer o*rollback*, recomendamos salvar os arquivos **server.log** – localizado em [diretório\_instalação]\appserver\standalone\log (a partir da **2.0**) ou [diretório\_instalação]\appserver\domain\servers\fluig1\log (**1.6 até 1.8.2**) – e **install.log** (localizado em [diretório\_instalação]) e abrir *ticket* com essas evidências, para que o time de atendimento TOTVS Fluig possa analisar.

oculto

**Observação interna:**

O procedimento de atualização foi repassado ao artigo: <https://centraldeatendimento.fluig.com/hc/pt-br/articles/360033785473>

Caso tenham alterações, é necessário repassar a esse artigo!!!

## Atualização 2.0

---

A instalação da **atualização Voyager (2.0)** exige que a plataforma esteja no mínimo na **atualização Crystal Mist (1.8.2).**

* Caso seu ambiente esteja em uma atualização anterior, é necessário primeiramente atualizar para o pacote **mais** **recente da 1.8.2 (no mínimo 1.8.2-260127)**, disponível para *download* na Central do cliente. Após a atualização, basta subir os serviços, iniciar a plataforma e, só então, atualizar para a **Voyager (2.0)****.**

* Caso seu ambiente esteja na **atualização 1.8.2**, é necessário primeiramente atualizar para o pacote **mais** **recente da 1.8.2 (no mínimo 1.8.2-260127)**, disponível para *download* na Central do Clientes, subir os serviços,  iniciar a plataforma e, só então, atualizar para a **Voyager (2.0)****.**

Importante!

Para realizar o *download* das atualizações, acesse a [Central do cliente](https://suporte.totvs.com/portal/p/10098/download#000035), descompacte o arquivo conforme orientado e siga os [Procedimentos para efetuar a atualização.](https://tdn.totvs.com/pages/releaseview.action?pageId=271666186#Guiadeatualiza%C3%A7%C3%A3odaplataforma-Procedimentosparaefetuaraatualiza%C3%A7%C3%A3oatualiza%C3%A7%C3%A3o)

### Atualização 1.8

---

* A atualização para a 1.8.x deve ser efetuada apenas se a instalação atual estiver na atualização Crystal Lake (1.7.1). Para baixar o pacote da 1.7.1, acesse a [Central do cliente](https://suporte.totvs.com/portal/p/10098/download#000035/FLUIG%201.7/FLUIG/search/searchAll).

* Após a atualização para a Crystal Mist (1.8.2), acesse o recurso de [Indexação](http://tdn.totvs.com/pages/viewpage.action?pageId=234455757) e faça uma reindexação completa dos conteúdos do repositório da plataforma, marcando inclusive a opção para **Recriar o índice**.

  Nota:

  Na atualização Crystal Mist (1.8.2), o Servidor de indexação (Solr) foi atualizado para a versão 9.4.1.

### Atualização 1.7

---

* A atualização para a 1.7.x deve ser efetuada apenas se a instalação atual estiver na atualização Liquid (1.6.5). Para baixar o pacote da 1.6.5, acesse o [Central do cliente](https://suporte.totvs.com/portal/p/10098/download#000035/FLUIG%201.6/FLUIG/).

* Após a atualização para a Crystal Lake (1.7.1), acesse o recurso de [Indexação](http://tdn.totvs.com/pages/viewpage.action?pageId=234455757) e faça uma reindexação completa dos conteúdos do repositório da plataforma, marcando inclusive a opção para **Recriar o índice**.

#### Ajuste de processos e arquivos abertos para Fluig Indexer (Solr) em sistemas operacionais Linux

---

Atenção!

A partir da atualização 1.7.0, o TOTVS Fluig Plataforma passa a ser compilado sob a versão 11 do Java®. Por este motivo as mensagens de alerta, abaixo citadas, referentes ao serviço Fluig Indexer (Solr) durante a inicialização da plataforma, podem ser exibidas.

bashSolr warnings

Trata-se de variáveis de ambiente Linux utilizadas para definir um limite de arquivos abertos e um número máximo de processos rodando.

Os valores default no Linux para estas variáveis não são os ideais para alta performance do Fluig Indexer (Solr), por isso são sugeridos os valores desejáveis nestas mensagens.

Para realizar essa configuração, é necessário editar o arquivo /etc/security/limits.conf, e ao final dele inserir os seguintes valores:

bash/etc/security/limits.conf

Após a configuração e o reinício do servidor a mensagem não será mais exibida no log da plataforma.

### Atualização 1.6

---

Atenção!

Caso você tenha a plataforma com envio de e-mail configurado anterior à atualização 1.6.1, será necessário limpar os dados antigos de conexão do Servidor de e-mail pois a partir da atualização 1.6.1 essas configurações são feitas em tela.

* A atualização para a release 1.6.x deve ser efetuada apenas se a instalação atual estiver na release 1.5.13. Para baixar o pacote da 1.5.13, acesse o [Central do cliente](https://suporte.totvs.com/portal/p/10098/download#000035/FLUIG%201.5/FLUIG/).

* As bibliotecas JavaScript da plataforma foram atualizadas, portanto é preciso realizar novos testes com os formulários já cadastrados para garantir que não ocorram conflitos com versões mais antigas destas mesmas bibliotecas.

* Os desenvolvimentos sob a plataforma com dependências diretas do Java deverão ser recompilados com a versão Java 1.8.

* Os componentes da TOTVS Store devem ser atualizados para nova versão compatível com a release 1.6.

* Após a atualização, acesse o recurso de [Indexação](http://tdn.totvs.com/pages/viewpage.action?pageId=234455757) e faça uma reindexação completa dos conteúdos do repositório da plataforma, marcando inclusive a opção para **Recriar o índice**.

* A estrutura de pastas e arquivos no diretório de instalação da plataforma foram alteradas. As principais diferenças podem ser consultadas em .

* Caso utilize autenticação LDAP, siga os procedimentos descritos [aqui](https://suporte.totvs.com/portal/p/10098/suporte-fluig-noticias?id=532).

### Atualização 1.5

---

* Para atualização da plataforma para a release 1.5, consulte o guia .

### Atualização 1.2.8

---

* Clientes que estiverem utilizando a plataforma abaixo da atualização 1.2.8 devem entrar em contato com o [Suporte TOTVS Fluig](http://suporte.totvs.com/) antes de executar a atualização.

# Procedimentos para efetuar a atualização atualização

---

Para efetuar a atualização do TOTVS Fluig, é necessário seguir os passos descritos a seguir:

0.5falsesamplesfadetrue1Passo 1

* Efetue o *download* através do [Central do Cliente](https://suporte.totvs.com/portal/p/10098/download#000035) e descompacte o arquivo.

2Passo 2

* Pare os serviços Fluig, fluig\_Indexer, fluig\_RealTime e fluig\_MemCached ou redis (se tiver configurado).

Nota:

Caso tenha atualização 1.5.13 ou anterior instalado, os serviços serão: fluig, fluig\_MemCached e fluig\_RealTime.

Na instalação da atualização 1.6.0, por padrão, o serviço fluig\_MemCached não será criado. Nesta versão o servidor de aplicação mudou e trabalha com sistema de cache local, exceto em servidores de alta disponibilidade.

3Passo 3

* Execute o instalador e escolha a opção **Atualizar minha instalação** e clique em **Próximo**.

4Passo 4

* Na tela de Diretório para Atualização, selecione o diretório onde a plataforma está instalada.

* Clique em **Próximo** até o sistema apresentar a mensagem de que a atualização foi concluída com sucesso.

5Passo 5

* Caso a plataforma esteja operando em ***load balance***, é necessário realizar a configuração abaixo:

falseVersão1Atualizando para a 2.0

**01**. Localize a pasta WCMDIR, que está compartilhada entre todos os nós:

* abra em um editor de texto o arquivo **standalone.xml** localizado em [diretório\_instalação]/appserver/standalone/configuration;

* localize a propriedade de *binding* "**java:global/wcm/globalDataDir**", que informa o caminho da pasta compartilhada entre as instâncias.

]]>

**02**. Em seguida, copie o conteúdo do diretório [diretório\_instalação]/repository/wcmdir/ para o caminho encontrado no parâmetro acima **GLOBAL\_DATA\_DIR/wcmdir**.

2Atualizando para a 1.6 até a 1.8.2

**01**. Localize a pasta WCMDIR, que está compartilhada entre todos os nós:

* abra em um editor de texto o arquivo **domain.xml** localizado em [diretório\_instalação]/appserver/domain/configuration;

* localize a propriedade de *binding* "**java:global/wcm/globalDataDir**", que informa o caminho da pasta compartilhada entre as instâncias.

]]>

**02**. Em seguida, copie o conteúdo do diretório [diretório\_instalação]/repository/wcmdir/ para o caminho encontrado no parâmetro acima **GLOBAL\_DATA\_DIR/wcmdir**.

6Passo 6

* Inicie os serviços respeitando a seguinte ordem:

1. fluig\_MemCached ou redis (se tiver configurado)
2. fluig\_Indexer;
3. fluig\_RealTime;
4. fluig.

Importante!

Habilite o acesso ao serviço de versionamento da plataforma, liberando acesso ao endereço [https://version.fluig.com](https://version.fluig.com/) (porta 443), na rede local onde a plataforma está instalada.

Para verificar a disponibilidade do serviço de licenciamento, acesse o site [status.fluig.com](http://status.fluig.com).

# Atualização em ambiente Windows - Modo caractere

---

As instruções para realizar o atualização do TOTVS Fluig Plataforma e dos módulos separadamente estão informados abaixo:

0.5falsesamples4fadetrue1Fluig

* Abra o **Prompt de Comandos** no diretório onde o pacote de instalação foi descompactado e execute o comando abaixo. Se a plataforma foi instalada de forma completa ou seja, com todos os módulos, não será necessário atualizar os módulos Servidor de indexação e RealTime separadamente, sendo preciso apenas executar este comando:

bash]]>

* **Pronto**! Após o término da atualização será apresentada a mensagem "Atualização concluída" no console. Portanto sua plataforma foi atualizada.

2Servidor de indexação

* Abra o **Prompt de Comandos** no diretório onde o pacote de instalação foi descompactado e execute o comando abaixo caso deseje atualizar apenas o Servidor de indexação:

bash]]>

* **Pronto**! Após o término da atualização será apresentada a mensagem "Atualização concluída" no console. Portanto o Servidor de indexação foi atualizado corretamente.

Dica!

Se desejar implementar mais servidores na configuração Master/Slave, continue a instalação conforme os procedimentos descritos na documentação .

3RealTime

* Abra o **Prompt de Comandos** no diretório onde o pacote de instalação foi descompactado e execute o comando abaixo caso deseje atualizar apenas o serviços de RealTime:

bash]]>

* **Pronto**! Após o término da atualização será apresentada a mensagem "Atualização concluída" no console. Portanto o Servidor de indexação foi atualizado corretamente.

# Atualização em ambiente Linux - Modo caractere

---

As instruções para realizar o atualização do TOTVS Fluig Plataforma e dos módulos separadamente estão informados abaixo:

0.5falsesamples4fadetrue1Fluig

* Abra o **Console** no diretório onde o pacote de instalação foi descompactado e execute o comando abaixo. Se a plataforma foi instalada de forma completa ou seja, com todos os módulos, não será necessário atualizar os módulos Servidor de indexação e RealTime separadamente, sendo preciso apenas executar este comando:

bash]]>

* **Pronto**! Após o término da atualização será apresentada a mensagem "Atualização concluída" no console. Portanto sua plataforma foi atualizada.

2Servidor de indexação

* Abra o **Console** no diretório onde o pacote de instalação foi descompactado e execute o comando:

bash]]>

* **Pronto**! Após o término da atualização será apresentada a mensagem "Atualização concluída" no console. Portanto o Servidor de indexação foi atualizado corretamente.

Dica!

Se desejar implementar mais servidores na configuração Master/Slave, continue a instalação conforme os procedimentos descritos na documentação .

3RealTime

* Abra o **Console** no diretório onde o pacote de instalação foi descompactado e execute o comando:

bash]]>

* **Pronto**! Após o término da atualização será apresentada a mensagem "Atualização concluída" no console. Portanto o serviço de RealTime foi atualizado corretamente.

# Atualização com balanceamento de carga, alta disponibilidade e tolerância à falha - *Cluster*

---

O procedimento de atualização da plataforma em *cluster*, onde é possível ter balanceamento de carga, alta disponibilidade e tolerância a falha, é igual ao de ambientes com , porém o pacote de atualização deverá ser executado**em cada um dos nós** do ambiente. Os serviços FLUIG, fluig\_Indexer, fluig\_Realtime, Cache (Memcached ou Redis) e Prizm devem estar parados antes que o processo de atualização seja iniciado.

Atenção!

Se a atualização for realizada da versão 1.5.x para a versão 1.6, as configurações de balanceamento de carga, alta disponibilidade e tolerância a falhadeverão ser refeitas devido ao servidor de aplicação ter mudado. Para isso, siga a documentação .

$("b:contains('oculto')").parent().parent().hide();
]]>
