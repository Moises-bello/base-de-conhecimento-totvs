---
content_hash: 77aec2648665e3a52f96231f0d78dfd582cdb64f5557dde62af0782de9018a09
fetched_at: '2026-06-29T00:05:54.348500+00:00'
page_id: '1077778942'
product: rm
source: tdn-rm
title: Página de Checkout
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1077778942
version: 8
---

5%90%InstalaçãotrueInstalacaoInstalação

**Baixando o instalador**

Acesse o [portal de downloads](https://suporte.totvs.com/portal/p/10098/download#company/), baixe o arquivo TOTVS RM Portal de acordo com a versão desejada na extensão .msi

Importante

Recurso disponível a partir da release 12.1.34

---

---

**Instalando o portal**

1 - Inicie a instalação

2 - Durante a instalação, selecione o tipo Personalizada

3 - Na instalação personalizada são apresentados todos portais disponíveis da Linha RM, por default todos os recursos serão instalados, neste momento deixe habilitado apenas o Portal Checkout.

Informações

Durante a instalação você pode selecionar mais de um portal para ser instalado ao mesmo tempo.

4 - Nas configurações, habilitamos o serviço de API. Se você pulou esta etapa, acesse [este link](https://tdn.totvs.com/pages/viewpage.action?pageId=639955763#Configuracoes-65018) para realizar a configuração, antes de seguir.

É nesse momento que precisamos informar as portas do Host (**Port**) e do serviço de API (**ApiPort**) da Biblioteca RM.

As informações preenchidas na primeira linha desta tela serão utilizadas para a configuração da webconfig que contém as regras do rewrite, porém também é possível editá-las posteriormente.

5 - Conclua a instalação

Configuracao\_IISConfiguração Obrigatória (IIS)

Ao finalizar a instalação do Portal, será criado um site no IIS com o nome FrameHTML.

O site é criado e toda a comunicação do IIS acontece na pasta **C:\TOTVS\CorporeRM\FrameHTML**

**Informando URL do serviço de API**

No diretório de instalação do Portal **C:\TOTVS\CorporeRM\FrameHTML\Web\App\Fin\Checkout\config\** abra o arquivo de configuração **config.json**.

1config.jsontrue

Na opção "**rmApiServer"** informe a URL do servido de API configurada anteriormente na etapa de [configuração da API](https://tdn.totvs.com/pages/viewpage.action?pageId=639955763#Configuracoes-API).

Exemplo: <http://10.173.17.242:8051/api/>

Importante

A **URL** informada **precisa** ser de acesso **externo**, informando IP ou domínio, **nunca** usar localhost, pois caso contrário o portal estará acessível apenas na própria máquina.

Após configurar o arquivo config.json, é necessário limpar o cache do navegador, caso contrário, o arquivo de configuração antigo será mantido por um tempo.

A Tag **rmApiServer** deve obrigatoriamente **terminar com barra "/"**

---

---

**Definindo permissão**

O IIS realiza interações com a pasta do site e ele deve ter permissão total de acesso a pasta.

É necessário inserir nas propriedades da pasta **C:\TOTVS\CorporeRM\FrameHTML** o controle total para o usuário **IIS\_IUSRS** do IIS (**NOMEDAMAQUINA\IIS\_IUSRS)**

Validando comunicação IIS x Pasta instalação

Uma das melhores formas de testar a comunicação do IIS com a pasta é abrir o site logo após essas configurações através da opção Procurar Site.

Se o site for aberto confome demonstrado abaixo é porque a comunicação entre a pasta e o IIS está corretamente configurada.

Caso encontre algum erro nesse passo vá até a seção de [Erros e Soluções](https://tdn.totvs.com/pages/viewpage.action?pageId=700486136).

Configuracao\_RewriteConfiguração Opcional (Rewrite)Importante

Esta configuração deve ser utilizada apenas quando a instalação do **Portal Checkout** e o **Host** estão em **domínios diferentes**. 

Esse componente permite que a URL do site seja reescrita durante a navegação. 

**Instalando o Rewrite e o ARR**

Se você utilizou o instalador, já foi solicitado a instalação do [Rewrite](https://www.iis.net/downloads/microsoft/url-rewrite)

Fazer o download do [Microsoft Application Request Routing (ARR)](https://www.microsoft.com/en-us/download/details.aspx?id=47333). 

Realizar a instalação dos componente acima no mesmo servidor do Portal Checkout

---

---

**Habilitando o proxy do ARR**

Acessar o recurso Application Request Routing Cache, nas ações clicar em Server Proxy Settings e marcar a opção **Enable proxy**

---

---

**Configurando regras de Rewrite**

Existem duas regras, a primeira é utilizada para direcionamento de APIs onde **NÃO** é necessário passar o alias selecionado, e a segunda é utilizada para as api's onde é necessário passar o alias selecionado (**Ambiente Multi Tenant**).

Atenção

Caso já existam regras no Rewrite diferentes das regras especificadas a seguir, favor avaliar a possibilidade de removê-las, pois pode impactar as requisições ao Host.

**1ª Regra:**

1. Acessar o IIS -> Acessar o Portal Checkout **(FrameHTML | Web | App | Fin | Checkout)** Clicar no site **Portal Checkout-> URL Rewrite**
2. Dar um duplo click no ícone URL Rewrite e em seguida clicar em: Adicionar uma *Rule* do tipo *Inboud Rule.*
3. Inserir as seguintes informações
   1. No campo "**Name**" informar um nome para a regra que está sendo criada
   2. Na opção: *Match URL, no campo: "**Pattern**" inserir as informação: api/(.\*)*
   3. Na opção: *"**Actions"**, no campo: Rewrite URL informar o link: [http://nome\_da\_maquina\_do\_host:porta/api/{R:1](http://localhost:8052/%7BR:1)}*

**2ª Regra:**

1. Acessar o IIS -> Acessar o Portal Checkout  **(FrameHTML | Web | App | Fin | Checkout )** Clicar no site **Portal Checkout -> URL Rewrite**
2. Dar um duplo click no ícone URL Rewrite e em seguida clicar em: Adicionar uma *Rule* do tipo *Inboud Rule.*
3. Inserir as seguintes informações
   1. No campo "**Name**" informar um nome para a regra que está sendo criada
   2. Na opção: *Match URL, no campo: "**Pattern**" inserir as informação: aliasname\.(.\*)/api/(.\*)*
   3. Na opção: *"**Actions"**, no campo: Rewrite URL informar o link: [http://{R:1}.nome\_da\_maquina\_do\_host:porta/api/{R:](http://localhost:8052/%7BR:1)2}*
   4. Marcar a opção: *"**Stop processing of subsequent rules"***

Atenção

A porta utilizada deve ser a mesma que está configurada na tag ApiPort na etapa de [configuração de API](https://tdn.totvs.com/pages/viewpage.action?pageId=639955763).

---

---

**Ajustando URL do serviço de API**

No diretório de instalação do Portal **C:\TOTVS\CorporeRM\FrameHTML\Web\App\Fin\Checkout\config\** abra o arquivo de configuração **config.json**.

1config.jsontrue

Na opção "**rmApiServer"**informe o caminho do portal conforme publicado no IIS.

Exemplo: [http://10.173.17.242:8051/](http://10.173.17.242:8051/api/)FrameHTML/Web/App/Fin/Checkout/api/  
Importante

A **URL** informada **precisa** ser de acesso **externo**, informando IP ou domínio, **nunca** usar localhost, pois caso contrário o portal estará acessível apenas na própria máquina.

Após configurar o arquivo config.json, é necessário limpar o cache do navegador, caso contrário, o arquivo de configuração antigo será mantido por um tempo.

A Tag **rmApiServer** deve obrigatoriamente **terminar com barra "/"**

https-opcionalUtilizar Protocolo HTTPS (Opcional)

**Para habilitar o acesso via HTTPS, siga estes passos essenciais:**

1. **Habilite o SSL no Host:** Siga rigorosamente o procedimento descrito na documentação oficial da TOTVS, disponível neste link: [Framework (Linha RM) - Habilitar SSL no Host](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6935374831127-Framework-Linha-RM-Frame-Habilitar-SSL-no-Host).
2. **Associe a Porta e o Certificado no IIS:** No Gerenciador do IIS, acesse as configurações do site (associações) e adicione uma nova associação para o protocolo HTTPS, geralmente na porta 443, vinculando o certificado SSL correspondente.

   Observações

   **Para adicionar um certificado, siga estes passos no Gerenciador do IIS:**

   1. **Selecione o servidor:** Na árvore de conexões à esquerda, clique no nome do seu servidor.
   2. **Abra os Certificados:** Na tela principal (ícones), dê um duplo-clique em **"Certificados de Servidor"**.
   3. **Adicione o certificado:** No painel "Ações" à direita, clique em **"Criar Solicitação de Certificado"** para gerar um novo, ou em **"Importar"** para adicionar um certificado já existente."

Principais Erros

**Ainda não está conseguindo acessar o portal?**

Segue abaixo algumas possíveis causas para os erros que você pode estar enfrentando:

**Certificado configurado, mas o erro persiste?**

Tente abrir no navegador o seguinte endereço (substitua a palavra **domínio** pelo seu domínio e **porta** pela porta da API configurada no host):  
`https://dominio:porta/API/cmp/v1/vendorAuth/UserAuthenticated`

Se aparecer alguma mensagem de erro semelhante à da imagem abaixo, é possível que ainda faltem configurações no certificado SSL.

**Possíveis causas:**

* O certificado SSL pode não estar corretamente configurado para o domínio utilizado.
* A porta especificada pode não estar devidamente configurada ou aberta no servidor.

Recomendamos revisar essas configurações para garantir que o certificado e a porta estejam corretamente ajustados.

config-validationValidação dos arquivos de config

Este tópico descreve os principais pontos de configuração do portal RM Checkout que devem ser validados em caso de problemas de acesso, carregamento da página ou comunicação com a API.

# Configuração do arquivo index.html

No arquivo **index.html**, localizado na raiz do portal, verifique se a tag **base href** está configurada com caminho relativo.

**Trecho do arquivo:**

`<head>  
    <meta charset="utf-8">  
    <title>Checkout</title>  
    <base href="./">  
</head>`

> A utilização de `./` permite que o portal funcione corretamente em diferentes diretórios virtuais configurados no IIS, evitando problemas no carregamento dos recursos da aplicação.

---

# Configuração do arquivo web.config

No arquivo **web.config**, localizado na raiz do portal, verifique se a regra de rewrite das rotas Angular está apontando para o arquivo **index.html** utilizando caminho relativo.

**Trecho do arquivo:**

`<rule name="Angular Routes" stopProcessing="true">  
    <match url=".*" ignoreCase="true" />  
    <conditions logicalGrouping="MatchAll">  
        <add input="{REQUEST_FILENAME}" matchType="IsFile" negate="true" />  
        <add input="{REQUEST_FILENAME}" matchType="IsDirectory" negate="true" />  
    </conditions>  
    <action type="Rewrite" url="./index.html" />  
</rule>`

A utilização de `./index.html` garante que o portal funcione corretamente quando publicado em diretórios virtuais do IIS, evitando falhas de navegação e carregamento das rotas da aplicação.

---

# Configuração do arquivo config.json

No arquivo **config.json**, localizado na raiz do portal, verifique se o parâmetro **rmApiServer** está apontando para o endereço correto da API do RM.

**Trecho do arquivo:**

`{  
     "rmApiServer": "http://localhost:8052/api/"  
}`

O endereço deve seguir o formato:

```
http://<servidor>:<porta>/api/
```

Esta configuração é responsável pela comunicação entre o portal e a API do RM. Caso o endereço esteja incorreto, o portal poderá apresentar falhas de carregamento ou erros ao consultar informações do sistema.

---

# Configuração da URL de Pagamento no TOTVS RM

No RM, acesse o Assistente de Implantação de Processos e localize o processo **02.02.08 - TOTVS RM Checkout**.

**Caminho:**

```
Financeiro → Ambiente → Parâmetros → TOTVS Gestão Financeira → Contas a Receber → TOTVS RM Checkout
```

No processo **TOTVS RM Checkout**, verifique se o campo **URL de Pagamento** está preenchido corretamente.

**Exemplo:**

```
http://SERVIDOR/FrameHTML/Web/App/Fin/Checkout/payments?
```

A URL deve ser composta pelo nome da máquina (ou DNS), pelo caminho de publicação do portal no IIS e pelo sufixo `/payments?`.

Esta configuração é utilizada pelo RM para redirecionar os usuários para a página de pagamento do portal. Caso esteja incorreta, a abertura da página poderá falhar ou direcionar para um endereço inexistente.

---

### Checklist de validação

Antes de iniciar os testes do Checkout, valide os seguintes itens:

* `index.html` com `<base href="./">`
* `web.config` com rewrite para `./index.html`
* `config.json` apontando para a API correta (`http://servidor:porta/api/`)
* Campo **URL de Pagamento** preenchido corretamente

0solid

---

---

560px

 [Voltar para o Menu Principal](https://tdn.totvs.com/display/LRM/Portal+do+Fornecedor)

---

---

div.theme-default .ia-splitter #main {
margin-left: 0px;
}
.ia-fixed-sidebar, .ia-splitter-left {
display: none;
}
#main {
padding-left: 10px;
padding-right: 10px;
overflow-x: hidden;
}
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
]]>
