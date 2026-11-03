---
content_hash: e11cdcaa5c4a2d3485182816c4df2aa5ad1e3b04e40e78eee0a1f06ba930ab27
fetched_at: '2026-06-28T21:35:17.301823+00:00'
page_id: '1040985360'
product: fluig
source: tdn-fluig
title: Primeiros passos no desenvolvimento de widgets
type: documentation
url: https://tdn.totvs.com/display/fluig/Primeiros+passos+no+desenvolvimento+de+widgets
version: 43
---

# Pré-requisitos do ambiente

---

Antes de iniciar a criação de uma *widget*, certifique-se de que sua máquina atende aos requisitos técnicos abaixo. Estes componentes são essenciais para que o desenvolvimento e a comunicação com o TOTVS Fluig ocorram sem falhas.

## Kit de desenvolvimento Java (JDK)

---

**O que é:** ferramenta necessária para compilar e desenvolver código Java.

Atenção!

Certifique-se de instalar o **JDK da Oracle**. É obrigatório ter o JDK completo e não apenas o JRE, visto que o JRE serve exclusivamente para executar os programas, e não para criá-los.

## IDE Eclipse e *plugin* Fluig Studio

---

Para desenvolver para a plataforma, utilizamos o Eclipse com ferramenta específica da TOTVS.

* **Versões suportadas:** é necessário utilizar o **Eclipse 2019-R9 (2019-09)** ou o **Eclipse Luna**, pois atualmente são as únicas versões homologadas pela TOTVS.
* **Extensão:** o *plugin* **Fluig Studio** deve estar instalado e configurado. É fundamental garantir que o *plugin* esteja exatamente na mesma versão do servidor Fluig do seu ambiente.

Caso haja divergência entre a versão do seu *plugin* e a do servidor, consulte a documentação de Instalação do Fluig Studio para realizar o *downgrade* ou *upgrade* de versão do *plugin*.

Dica!

Consulte o [Guia de instalação Fluig Studio](https://tdn.totvs.com/pages/viewpage.action?pageId=73078179) e [Como fazer - Instalar Eclipse 2019-R9 + Fluig Studio](https://academy.fluig.com/theme/totvs_fluig_academy/landpage.php?course=95) para o passo a passo detalhado.

Para a boa utilização do Fluig Studio, algumas configurações são necessárias [Configuração para uso inicial do Fluig Studio](https://tdn.totvs.com/pages/viewpage.action?pageId=172297237).

Atenção!

O Eclipse Luna não é compatível com a atualização Voyager 2.0 do Fluig.

# Configuração do servidor e criação do projeto

---

Para iniciar o desenvolvimento no TOTVS Fluig, o primeiro passo prático é configurar a comunicação com o seu ambiente e criar um projeto no Eclipse para organizar os seus arquivos.

Dica!

Consulte [Criando um projeto Fluig no Studio](https://tdn.totvs.com/display/fluig/Criando+um+projeto+fluig+no+Studio) para o passo a passo detalhado.

## Passo 1: selecionar a Perspectiva Fluig

---

Antes de clicar em qualquer menu, certifique-se de que você está na **Perspectiva Fluig**. No canto superior direito do Eclipse, verifique se o ícone do Fluig está selecionado. Isso habilita os menus específicos da plataforma.

falsenovo-usuariotrue1Passo 1

* **Selecione a perspectiva do Fluig.**

## Passo 2: configurando o servidor (Fluig Server)

---

O Eclipse precisa saber para onde enviar os arquivos.

falsenovo-usuario1Passo 1

* **Criar um novo servidor.**

  + Procure a aba Servers. Se não encontrar, vá em Window > Show View > Other... > Fluig > Fluig Servers.
  + Clique com o botão direito sobre **Servers** e selecione **Novo***>***Fluig Server**.

2Passo 2

* **Autenticação e definição do ambiente. Nesta tela, insira as credenciais essenciais para o "*deploy*":**

  + **Nome servidor:** um nome para você identificar o servidor. Ex.: "Servidor Produção".
  + ***Host*:** o endereço completo. Ex.: `http://lab.fluig.com`.
  + **Usuário e Senha**: devem ser de um usuário com perfil de Administrador no TOTVS Fluig.

    Dica!

    Em ambientes integrados com Identity, utilize as credenciais de login do Identity.
  + Clique em ***Finish*** para concluir a criação do servidor.

3Passo 3

* Clique **duas vezes** no servidor para validar a configuração.

## Passo 3: criando o projeto

---

O projeto funciona como uma pasta raiz que conterá todos os seus componentes: *widgets, layouts, datasets.*

falsenovo-usuario1Passo 1

* Vá em **Arquivo** > **Novo** > **Projeto Fluig**.

2Passo 2

* **Nome do projeto:** digite o nome do seu projeto. Ex.: `Projeto_Treinamento_Widgets, fluig, etc`.
* Clique em **Finish**.

Importante!

O Eclipse criará uma estrutura de pastas. A pasta que nos interessa é a **WCM**, onde ficam os componentes de *Web Content Management*.

## Criando a *widget*: primeiros passos

---

Criar uma *widget* no Fluig é como construir uma peça de Lego inteligente. Ela terá um visual (HTML), um comportamento (JavaScript), um estilo próprio (CSS) e poderá falar vários idiomas (i18n). Vamos ao passo a passo no seu ambiente de desenvolvimento (Eclipse com *plugin* Fluig Studio):

falsenovo-usuario1Passo 1

1. Abra a pasta do seu projeto, localize a pasta **WCM** e, dentro dela, a pasta **Widget**.
2. Clique com o botão direito sobre a pasta **Widget** e selecione **New > Widget**.
3. Uma janela de configuração será aberta:
   1. **Código:** o ID único da sua *widget* no banco de dados. **Regra**: use apenas letras minúsculas, números e *underline*. Ex.: `minha_primeira_widget`.
   2. **Nome:** o nome amigável que o usuário verá no catálogo de *widgets* ao editar uma página. Ex.: "Minha primeira *widget*".
   3. **Descrição:** explique brevemente o propósito dela.
4. Na mesma tela de criação, haverá a opção de escolher um ***Template***.
   1. Selecione a opção **"Nenhum".**
   2. Ao escolher **"Nenhum"**, clique em **Next**.
   3. Uma nova janela de configuração será aberta:
      1. **Código/Nome/URL do desenvolvedor:** preencha com seus dados ou os da sua empresa.
      2. **Categoria:** fundamental! É a "pasta" onde sua *widget* vai aparecer no menu do Fluig. Anote o nome exato.
      3. **Renderizador:** mantenha **Freemarker**. É o motor de templates oficial do Fluig.
      4. **Suporte mobile:** marque se a *widget* terá suporte ao aplicativo mobile Fluig.
2Passo 2

Ao finalizar, o Fluig Studio gerará a seguinte estrutura limpa. É crucial entender o papel de cada arquivo:

3Passo 3

Detalhando os arquivos na prática:

* **application.info?**:guarda tudo o que você preencheu na criação. Se você precisar mudar o ícone (`application.icon`) ou a categoria, é aqui que fará a alteração.

Curiosidade!Se você precisar mudar o ícone da *widget* ou a categoria dela no futuro, é neste arquivo que você fará a alteração.

* **view.ftl** (interface visual): é o HTML processado pelo Freemarker. Aqui, aplicamos o Fluig Style Guide.

Dica!Evite usar estilos *inline* ou cores *hardcoded*. Use painéis, a grade do Style Guide (`row`, `col-md-*`) e os utilitários de espaçamento do Fluig (`fs-mt-16`, etc.).

Exemplo prático (view.ftl):

js

### ${i18n.getTranslation('widget.title')}

${i18n.getTranslation('widget.description')}
