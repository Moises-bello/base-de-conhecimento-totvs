---
content_hash: 0e712a030755b9a3d9b50249625d15829461bae16d80c0a33caae0ad4779b2c5
fetched_at: '2026-06-29T00:12:07.164466+00:00'
page_id: '919069947'
product: rm
source: tdn-rm
title: Angular Elements - Criando Componentes Novos e utilizando em Portal antigo
type: documentation
url: https://tdn.totvs.com/display/LRM/Angular+Elements+-+Criando+Componentes+Novos+e+utilizando+em+Portal+antigo
version: 3
---

# **1) Gerando módulos do Elements no projeto Angular 2+**

---

Antes de executar o build do projeto para elements é importante validar se o componente migrado possui uma referência no arquivo de módulo **app.module.elements.ts** que fará a construção para angular elements, assim ele será acessível por tags HTML no portal em migração, exemplo:

# **2)** **Gerando o pacote do Elements no projeto em Angular 2+**

---

Abra o terminal de comando dentro do projeto em angular com elements, e rode o comando do npm referente ao script que executa o build da aplicação para Angular Elements, exemplo:

# **3) Localizando os artefatos publicáveis**

---

Após execução do comando, localize onde foram gerados os artefatos publicáveis do build do elements, por padrão são gerados dentro da pasta "**dist**":

# **4) Movendo os** **artefatos** **publicáveis**

---

Dentro do diretório da geração dos arquivos, remova as pastas de "**assets**" e "**config**" e o arquivo **index.elements.html**pois os mesmos podem ser descartados, e caso sejam movidos para a aplicação em migração, poderão gerar inconsistências no sonar.

Copie o restante dos arquivos:

Depois cole-os na **pasta destino** onde ficarão os arquivos do **elements** para o **projeto em migração** (projeto que usará as telas geradas pelo elements):

# **5) Criando o componente no portal em migração**

---

Dentro do projeto em migração, localize o nó/diretório interno do app onde ficará o novo componente conforme estrutura planejada, normalmente usa-se o mesmo diretório da tela antiga (caso possúa) em um subdiretório/pasta de nome "**elements**", exemplo:

**Neste subdiretório precisão serem criados 4 arquivos novos, sendo eles:**

* **<nome do componente>.controller.js**
* **<nome do componente>.module.js**
* **<nome do componente>.route.js**
* **<nome do componente>.view.html**

# **5) Definição do arquivo****<nome do componente>.controller.js**

---

Dentro do arquivo de controller, inclua as linhas de:

* declaração de definição do controller (linhas 1, 2 e 22)
* Referência para o módulo correspondente (linhas 4 a 6)
* Injeção dos módulos compartilhados (linha 8)
* Constructor em forma de função com método de carregamento do componente e seus respectivos eventos customizáveis (linhas 10 a 21)

# **6) Definição do arquivo** **<nome do componente>.module.js**

---

Dentro do arquivo de módulo, inclua a definição de módulo do angularJS com o nome do módulo do componente

# **7) Definição do arquivo** **<nome do componente>.route.js**

---

Dentro do arquivo de rota, será necessário mapear as rotas configuradas no componente anterior em AngularJS para o novo componente do elements, conforme exemplo:

Para cenário do exemplo anterior foi criado um método de mapeamento dentro de um arquivo de mapeamento global da aplicação, conforme segue abaixo:

As rotas originais (do componente a ser substituído pelo novo componente em angular elements) podem ser encontradas no arquivo de configuração de rotas do componente bem como suas dependências de demais módulos e controllers, conforme exemplo:

# **8) Mapeamento do novo componente (elements) no portal migrado**

---

Dentro do arquivo de módulos do portal migrado, substitua os arquivos de módulo e rota antigos pelos novos criados para o componente em angular elements, exemplo:

**\*Lembre-se de incluir o subdiretório "/elements" caso tenha usado este padrão no seu projeto**
