---
content_hash: 9c3597968338d048a13d028932c2cb7d69d422589c43f158016c6f6a27813f66
fetched_at: '2026-06-29T00:05:48.580660+00:00'
page_id: '1025242366'
product: rm
source: tdn-rm
title: 04.3 - Criar menus personalizados para integrar e acessar outras aplicações
  externas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1025242366
version: 15
---

Com este recurso, a instituição pode criar menus personalizados para integrar e acessar outras aplicações externas pelo Meu eduCONNECT/ TOTVS Educa Mobile.

A TOTVS **não se responsabiliza** por alterações em arquivos decorrentes de customizações realizadas pelo cliente. Portanto, é indispensável que, antes de cada atualização de patch ou versão, o cliente realize o backup de suas modificações e as reaplique após o processo, uma vez que o conteúdo original pode ser sobrescrito.

Servidor web

As customizações dos **conteúdos escritos devem ser realizadas em cada servidor web existente.**

Acesso ao arquivo de configuração do menu

Acessar o arquivo **"Educamobile\Areas\Educacional\Menu.xml"**, no diretório onde está instalado o **TOTVS Educa Mobile**.

Para customizar o menu do **TOTVS Educa Mobile**, utilize a estrutura XML abaixo. O sistema disponibiliza um modelo de menu comentado para que a própria instituição realize seus ajustes a partir desse exemplo.

Detalhamento das Tags de configuração

Cada campo possui uma função específica para a renderização e o comportamento do link no aplicativo:

* **`<Tag>`** Define o valor padrão "0" para novos itens customizados.
* **`<Caption>`** Define o nome (rótulo) que será exibido para o usuário no menu do aplicativo. No exemplo: "Aplicação Externa (Professor)".
* **`<Image>`**Indica o caminho do ícone que será exibido ao lado do nome do menu. Deve apontar para o diretório de imagens do portal.
* **`<ExternalURL>`**O endereço (URL) completo da aplicação externa que será aberta ao clicar no menu.
* **`<TipoUser>`**Define qual perfil terá visibilidade deste item.

  + **P**: Professor
  + **A**: Aluno
* **`<SetContext>`**(S/N) Define o valor padrão "S" para novos itens customizados.
* **`<Module>`**(S/N) Define o valor padrão "S" para novos itens customizados.
Executar a abertura em um navegador externo

Por padrão, o Meu eduCONNECT e o TOTVS Educa Mobile **redirecionam o acesso para URLs internas do portal e do aplicativo**. Caso a instituição deseje que o link seja aberto externamente no navegador do dispositivo, é necessário observar as seguintes considerações:

Incluir o parâmetro na URL de destino dentro do arquivo Menu.xml

Para que um item do menu seja aberto em um navegador separado, é necessário incluir o parâmetro **`openInBrowser`** na *querystring* da URL

Configuração de Links Externos com envio de contexto

Para abrir links em um navegador externo mantendo o envio de parâmetros de contexto (como a Coligada), a instituição deve seguir os passos abaixo:

#### **1.** Configuração do Menu XML

No arquivo `Menu.xml`, a tag `<ExternalURL>` deve apontar para o diretório de customização do servidor:

* **URL: `http://ENDERECO_SERVIDOR/EducaMobile/Custom/`**

#### **2.** Criação do Arquivo de Redirecionamento

No servidor, acesse a pasta `Educamobile\Custom` e crie um arquivo chamado `index.html`. Este arquivo será responsável por capturar os dados da sessão e redirecionar o usuário.

#### **3.** Implementação da Lógica (Regra de Negócio)

O script abaixo deve ser inserido no arquivo `index.html`. Ele realiza a ponte entre o TOTVS Educa Mobile e a sua aplicação externa:

> **// 1. Captura os parâmetros da URL atual (como o host)**  
> const params = new URLSearchParams(window.location.search);  
> const host = params.get('h');
>
> **// 2. Define a URL de destino desejada (incluindo a tag para abrir no navegador)**  
> const urlDestino = "[https://www.totvs.com/?openInBrowser](https://www.totvs.com/?openInbrowser)";
>
> **// 3. Consulta a API do Educa Mobile para recuperar os dados da sessão do usuário**  
> const xhr = new XMLHttpRequest();  
> xhr.open('GET', '<http://ENDERECO_SERVIDOR/EducaMobile/EduSessao/GetSession>');  
> xhr.responseType = 'json';
>
> xhr.onload = function () {  
>     if (xhr.status === 200) {  
>         **// Concatena a URL de destino com os dados de contexto (ex: CodColigada)**  
>         const urlFinal = `${urlDestino}&codcoligada=${xhr.response.Contexto.CodColigada}`;
>
> **// Verifica se o acesso é via aplicativo Meu eduCONNECT**  
>         if (window.NavigationChannel) {  
>             **// Para o  caso do app**  
>             window.NavigationChannel.postMessage(urlFinal);  
>         } else {  
>             **// Para o caso do TOTVS Educa Mobile**  
>             window.open(urlFinal, '\_blank');  
>         }  
>     }  
> };  
> xhr.send();



#### **4.** Arquivo de exemplo

Disponibilizamos abaixo um arquivo de exemplo para que a instituição possa realizar o download e a customização, seguindo o padrão estabelecido.

> ```
> 250
> ```

Correção para Links que não Carregam no iOS (iPhone)

Alguns links configurados no menu do aplicativo abrem normalmente em dispositivos Android, mas apresentam uma tela em branco ou não carregam em dispositivos iOS (iPhone).

### **Por que isso acontece?**

Gostaríamos de esclarecer que **isso não é um erro de desenvolvimento do nosso aplicativo**, mas sim um reflexo das rigorosas políticas de segurança do sistema da Apple. Quando tentamos exibir um site da internet "embutido" dentro do aplicativo (como se fosse uma janela interna), o iOS pode barrar o carregamento por dois motivos principais:

* **Bloqueio de conexões:** O iPhone impede ativamente o carregamento de sites que não sejam considerados 100% seguros ou que tenham elementos de outras páginas misturados.
* **Proteção do site original:** Muitos sites utilizam uma "trava" de segurança invisível que proíbe a sua exibição dentro de outros aplicativos (como medida para evitar a clonagem da página, por exemplo). Enquanto o Android às vezes ignora essa trava, o iPhone a obedece estritamente e bloqueia o acesso.

### **A Solução Adotada**

Para garantir que todos os usuários consigam acessar os conteúdos sem erros, independentemente do dispositivo que utilizam, a solução é fazer com que o aplicativo **force a abertura desses links diretamente no navegador nativo do celular** (como Safari ou Chrome), em vez de tentar exibi-los por dentro do app.

### 🛠️ **Instruções de Configuração (Como aplicar a correção)**

Para que um item do menu seja aberto em um navegador separado, o responsável pela configuração deve alterar o arquivo `Menu.xml`, incluindo o parâmetro `openInBrowser` na *querystring* da URL de destino.

**Exemplos Práticos:**

* ❌ **Como está hoje (Bloqueia no iOS):** `https://www.siteexemplo.com/pagina`
* ✅ **Como deve ficar (Correção aplicada):** `https://www.siteexemplo.com/pagina?openInBrowser`

> **⚠️ Atenção:** Caso a URL já possua outros parâmetros (e já utilize o símbolo `?`), você deve adicionar a instrução no final do link usando o símbolo `&`. *Exemplo:* `https://www.siteexemplo.com/pagina?id=123&openInBrowser`
