---
content_hash: a7a0613ac111e57574559e7a9f01d451a3cc2dd25c2ac62faa5bac635895386c
fetched_at: '2026-06-28T21:35:28.655338+00:00'
page_id: '668197293'
product: fluig
source: tdn-fluig
title: Tradução de Formulários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=668197293
version: 2
---

# Índice

true.\*ndicenone

# Objetivo

---

O objetivo deste guia é descrever a tradução de formulários avançados no TOTVS Fluig Plataforma.

# Pré-requisitos

---

Antes de iniciar o desenvolvimento de formulários, assista aos vídeos *how to* no item [Criação de formulários](http://tdn.totvs.com/x/fv4lE).

# Tradução de formulários

---

Para traduzir formulários é necessário utilizar a função i18n.translate(“literal\_da\_tradução”) nos pontos do arquivo HTML que devem ser traduzidos, conforme exemplo a seguir:

html/xmli18n.translate("nm\_cliente")
  
i18n.translate("contato\_cliente")
]]>As literais e seus respectivos valores são informados em arquivos de propriedades com a extensão .properties para cada um dos idiomas desejados. Os idiomas suportados para a tradução são os mesmos suportados pelo Fluig:  

Português (pt\_BR);

Inglês (en\_US);

Espanhol (es).

Os arquivos contendo as literais têm a seguinte nomenclatura:

**Português:** nome\_do\_formulario\_pt\_BR.properties;

**Inglês:** nome\_do\_formulario\_en\_US.properties;

**Espanhol:** nome\_do\_formulario\_es.properties.

Os arquivos de propriedades são criados de acordo com os passos apresentados a seguir:

0.5falsesamplesfadetrue1Passo1

* Para gerar os arquivos de propriedades, na visão *Explorador de Pacotes,* deve-se acessar o arquivo HTML do formulário a ser traduzido, clique com o botão direito e acessar a opção *Externalizar Strings*.

**Figura 1 - Menu Contextual Externalizar Strings.**

2Passo 2

* Os arquivos contendo as literais são criados na pasta do formulário.

**Figura 2 - Arquivos Properties na Pasta do Formulário.**

3Passo 3

* Informe os valores correspondentes às literais para o idioma de cada arquivo.

**Figura 3 - Edição de um Arquivo Properties.**

Ao exportar um formulário para o Fluig, os arquivos de propriedades contendo as literais são publicados como anexos dele.  
O formulário é apresentado no idioma que está configurado para o usuário corrente.

# Traduzindo Eventos de formulários

---

Da mesma forma que é possível traduzir a interface do formulário é possível traduzir também mensagem retornadas nos eventos do formulário. Para isso basta utilizar a função i18n.translate dentro dos eventos passando uma propriedade que esteja pré-definida no arquivos .properties deste mesmo formulário. Abaixo exemplo de uma implementação que irá retornar para o usuário uma mensagem de acordo com o definido no arquivo properties.

javascript
