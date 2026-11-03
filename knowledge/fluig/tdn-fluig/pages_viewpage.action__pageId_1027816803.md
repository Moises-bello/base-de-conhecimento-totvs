---
content_hash: 893d69a3d2a8d3367dfe42eb875857987685fe06fe68ed4673e9329916720594
fetched_at: '2026-06-28T21:35:17.193036+00:00'
page_id: '1027816803'
product: fluig
source: tdn-fluig
title: Guia de migração da plataforma do Windows para Linux
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1027816803
version: 40
---

Fique atento!

Esta página é válida a partir da **atualização 2.0** e **superiores**.

2

# Objetivo

---

O objetivo deste guia é apresentar os procedimentos recomentados para efetuar uma migração do TOTVS Fluig de um servidor Microsoft Windows para Linux.

# Preparação

---

* Defina previamente as configurações do ambiente para que sejam informados corretamente durante a fase de instalação e posteriores.  
  trueExemplo  
  URL pública, servidor SMTP.

* trueGreenrecomendado: derrube todos os serviços do Fluig antes de começar a migração.

# Instalação

---

Atenção!

* Utilize, para o Linux, uma versão do Fluig igual a versão instalada no Microsoft Windows.

* Durante a execução do instalador, informe nas configurações do banco de dados o mesmo nome do banco sendo utilizado atualmente.

* Apenas execute a instalação, não inicie o Fluig.

Realize uma instalação em Linux seguindo os procedimentos de uma nova instalação conforme documentado em .

Em seguida, faça os ajustes necessários na instalação.

## Ajustes de ambiente

---

Realize os ajustes de ambientes necessários – configurações de memória do servidor, por exemplo – no arquivo **appserver/bin/standalone.conf**.

## Importação das configurações

---

Substitua o arquivo **appserver/standalone/configuration/standalone.xml** por uma cópia do mesmo arquivo encontrado na instalação do servidor Microsoft Windows.

# Ajustes no standalone.xml

---

Uma vez que o arquivo **appserver/standalone/configuration/standalone.xml** foi copiado a partir do servidor Windows, estará configurado com informações – nome do servidor, endereço IP do servidor, caminhos da instalação – apontando para o servidor Windows. Será necessário alterar para as configurações do novo servidor. Para isso, abra o arquivo **appserver/standalone/configuration/standalone.xml** em seu editor de texto simples favorito (vi, nano, etc) e faça as seguintes alterações:

Atenção!

* O Microsoft Windows comumente utiliza como separador de pastas o caracter **"\"**, enquanto que o Linux utiliza o caracter **"/"**. Portanto, é importante lembrar de, sempre que alterar partes de um caminho, substituir o **"\"** por **"/"** em todo o restante do caminho.

* Os exemplos utilizados a seguir usam como base as seguintes informações:
  + Servidor antigo (Windows) → Endereço IP: **192.168.1.100**; hostname: **fluig-windows**; pasta de instalação: **C:\fluig**.
  + Servidor novo (Linux) → Endereço IP: **192.168.2.50**; hostname: **fluig-linux**; pasta de instalação: **/opt/fluig**.
standaloneip-addressEndereço IP

* Troque o endereço IP do servidor antigo (por exemplo: **192.168.1.100**) para o IP do servidor novo (por exemplo: **192.168.2.50**).

Exemplos de configurações comumente encontradas com o endereço IP (mas não limitado a apenas esses e nem sempre todos esses existem):

xml







]]>hostnameHostname

* Troque o hostmane do servidor antigo (por exemplo: **fluig-windows**) para o hostname do servidor novo (por exemplo: **fluig-linux**).

Exemplos de configurações comumente encontradas com o hostname (mas não limitado a apenas esses e nem sempre todos esses existem):

xml






]]>pathCaminhos

* Troque os caminhos do servidor antigo (por exemplo: **c:\fluig**)  para o caminho do servidor novo (por exemplo: **/opt/fluig**).

  Atenção!
  + Em servidores Microsoft Windows, o caminho pode aparecer na forma **C:\fluig**, **C:\\fluig** ou ainda **C:/fluig**. É importante procurar pelas três formas.
  + Não esqueça de trocar o "**\**" por "**/**".

Exemplos de configurações comumente encontradas com o caminho (mas não limitado a apenas esses e nem sempre todos esses existem):

xml









]]>

# Volume com os arquivos

---

Um dos principais motivadores de uma migração de um servidor Microsoft Windows para um servidor Linux, é a falta de confiabilidade do Microsoft Windows como servidor de arquivos. Portanto, é muito importante migrar o volume (arquivos) para um servidor Linux também.

Em ambientes onde haverá apenas um servidor do Fluig, o volume pode ser movido para o mesmo servidor Linux onde o Fluig será instalado, mantendo uma estrutura muito semelhante à instalação no servidor Windows.

Mas se o ambiente possuir (ou haver a intenção de possuir) mais de um servidor Fluig, é imprescindível que o volume esteja em algum servidor de arquivos que seja compartilhado (comumente via NFS).

Portanto:

* faça a cópia dos arquivos do volume atual (Windows) para o volume novo (Linux);

* monte um caminho (por exemplo: **/opt/volume**) apontando para o compartilhamento, em caso de uso de um servidor de arquivos dedicado.

## Aplicativos customizados

---

Se possuir aplicativos não padrão, sejam desenvolvidos por equipes internas, por terceiros ou mesmo baixado na *Store* oficial do Fluig, esses estarão na pasta própria.

Em uma instalação padrão, encontram-se na pasta "**appserver/apps**".

Esses aplicativos precisam ser disponibilizados manualmente para a nova instalação.

Em uma instalação padrão, com um único servidor Fluig, basta copiar o conteúdo da pasta *apps* do servidor atual (por exemplo: **C:\fluig\appserver\apps**) para a pasta *apps* do novo servidor (por exemplo: **/opt/fluig/appserver/apps**).

Já em uma instalação em que a pasta *apps* não esteja no local padrão, é necessário:

* copiar os aplicativos para uma localização acessível ao Fluig no novo servidor. Por exemplo, em um ambiente com um servidor de arquivos dedicado, poderia estar na pasta "**/opt/volume/apps**";

* ajustar a configuração que indica o caminho. Para isso, edite o arquivo **appserver/standalone/configuration.xml**, procure por algo como:

  xml]]>

  e substitua por algo como:

  ]]>

## Caminho customizado do volume

---

Se o volume está em um local diferente do local padrão da instalação (**FLUIG\_DIR/repository**), é preciso configurar esse caminho.

Para isso, edite o arquivo **appserver/standalone/configuration.xml**, procure pela propriedade **java:global/wcm/globalDataDir**.

Será encontrado algo como:

xml
]]>

Ajuste para algo como:

xml
]]>Nota:

É importante manter sufixo "**/wcmdir**".

# Banco de dados

---

O caminho da instalação também é salvo em alguns registros de algumas tabelas e, portanto, precisam ser ajustados também.

Para isso, conecte no banco de dados com algum cliente dele e execute alguns *updates*.

## Tabela FDN\_TENANTDATA

---

Encontre os registros que precisam ser alterados na empresa "**0**" (dados globais), com um comando como este (a sintaxe está para o banco MySQL, é necessário ajustar de acordo com o banco):

sql

Retornará algo semelhante a isso:

Atualize os registros usando comandos semelhantes a esses:

sql

Consulte os registros alterados para conferência:

sql

Retornará algo semelhante a isso:

A seguir, encontre os registros que precisam ser alterados na(s) empresa(s) criada(s), com um comando como esse:

sql 0 order by tenantdata\_id;]]>

Retornará algo semelhante a isso:

Atualize os registros usando comandos semelhantes a esses:

sql

Consulte os registros alterados para conferência:

sql

Retornará algo semelhante a isso:

Nota:

O exemplo acima pressupõe que há apenas uma empresa criada, com o TENANT\_ID=1234. Se houver mais empresas, é preciso repetir os procedimentos para cada uma delas, tomando o cuidado de informar o caminho correto para o volume de cada uma.

Por segurança, é interessante verificar se existe (e consequentemente corrigir) mais algum registro apontando para o caminho antigo. Por exemplo, com um comando como esse:

sql

## Tabela FDN\_PARAMGERAL

---

Encontre os registros que precisam ser alterados com um comando como este (a sintaxe está para o banco MySQL, é necessário ajustar de acordo com o banco).

### Analytics

---

Encontre e corrija o caminho onde são salvos os dados do Analytics:

sqlsql

### Solr

---

Encontre e corrija o caminho da instalação do Solr:

sqlsql

### Outras propriedades

---

Encontre e corrija o caminho em outras propriedades:

sqlsql

Por segurança, é interessante verificar se existe (e consequentemente corrigir) mais algum registro apontando para o caminho antigo. Por exemplo, com um comando como esse:

sql

## Tabela FDN\_VOLUMESITE

---

Encontre os registros que precisam ser alterados com um comando como este (a sintaxe está para o banco MySQL, é necessário ajustar de acordo com o banco):

sql

Retornará algo semelhante a isso:

Importante observar a coluna **VOLUMESITE\_ID**, pois ela contém a chave dos registros que precisam ser alterados.

Atualize os registros usando comandos semelhantes a esses:

sql

Consulte os registros alterados para conferência:

sql

Retornará algo semelhante a isso:

Importante!

As tabelas tratadas aqui são as tabelas padrão e registros padrão. Se possuir tabelas e/ou registros customizados que apontam para o volume, será necessário ajustar manualmente.
