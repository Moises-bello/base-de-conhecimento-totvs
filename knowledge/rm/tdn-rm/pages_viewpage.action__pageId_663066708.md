---
content_hash: e52d47e99fe9ea413a0dbd5709e583030046d20c461373d288b1d71805e429dc
fetched_at: '2026-06-29T00:11:16.157662+00:00'
page_id: '663066708'
product: rm
source: tdn-rm
title: Robots.txt e Indexação em Buscadores/Rastreadores
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=663066708
version: 6
---

O Portal RM poderá bloquear sua indexação em buscadores/rastreadores como o Google por padrão. Esta medida de segurança vem para assegurar que informações confidenciais não sejam exibidas em buscas do Google por exemplo.

Esta documentação tem como objetivo explicar de forma sucinta como esse bloqueio ocorrerá e medidas que podem ser tomadas caso seja desejado que o Portal RM determinado apareça publicamente em buscadores.

Não recomendamos que essa medida de segurança seja desabilitada/removida, pois pode expor arquivos de seu **Portal** publicamente em *rastreadores* pela internet.

---

## O arquivo Robots.txt

O arquivo **Robots****.txt** é usado em larga escala à muito tempo, sendo padronizado para a maior parte dos rastreadores presentes na internet, e trabalha permitindo ou negando a indexação automática desses buscadores:

Como diz o Google

*"O robots.txt é um arquivo de texto simples que segue o [Protocolo de exclusão de robôs](https://en.wikipedia.org/wiki/Robots_exclusion_standard#About_the_standard)(em inglês). Um arquivo robots.txt é constituído por uma ou mais regras. Cada regra bloqueia (ou permite) o acesso de um determinado rastreador a um caminho de arquivo especificado no site. A menos que você especifique o contrário no arquivo robots.txt, o rastreamento de todos os arquivos é permitido de forma implícita." -* Google: [LINK](https://developers.google.com/search/docs/advanced/robots/create-robots-txt?hl=pt-br)

Este arquivo será enviado automaticamente na instalação do Portal RM, conforme demonstrada na estrutura de pastas abaixo:

---

## Adicionando uma permissão de indexação

Caso seja necessário, é possível que apenas subdiretórios específicos da sua aplicação sejam permitidos. Dessa forma, mesmo que o diretório-pai esteja bloqueado, os diretórios que foram explicitamente liberados ainda poderam ser encontrados e indexados pelos rastreadores. O exemplo abaixo define bem esse comportamento, onde o bloqueio ocorre no diretório FrameHTML, porém o caminho /FrameHTML/web/app/Edu/PortalEducacional foi explicitamente liberado, utilizando a diretiva Allow, e dessa forma, pode ser indexado:

User-agent: \*  
Disallow: /FrameHTML

User-agent: \*  
Allow: /FrameHTML/web/app/Edu/PortalEducacional

E testando:

## Validade do arquivo Robots.txt

O arquivo robots.txt deve seguir algumas regras de validação para funcionar corretamente, algumas, de maior importância estão definidas abaixo:

### Deve existir na pasta raiz do site, não sendo válido para subdiretórios

Os rastreadores buscaram o arquivo robots.txt diretamente na raiz do site, assim sendo, caso não esteja localizado corretamente, não funcionará:

* **Certo:**<http://meusite.com/robots.txt>
* **Errado:**<http://meusite.com/Corpore.Net/robots.txt>

### Distinção entre Maiúsculas e Minúsculas

Os rastreadores irão diferenciar maiúsculas e minúsculas durante a leitura do robots.txt, então é importante compreendermos que os seguintes exemplos são totalmente distintos dentro do contexto dos rastreadores:

* <http://meusite.com/Corpore.Net>
* [http://meusite.com/Corpore.net](http://meusite.com/Corpore.et)
* <http://meusite.com/corpore.net>
* <http://meusite.com/corpore.Net>

Como diz o Google

*"O URL do arquivo robots.txt faz distinção entre maiúsculas e minúsculas, assim como outros URLs." -* Google: [LINK](https://developers.google.com/search/docs/advanced/robots/robots_txt)

### Distinção entre diferentes escritas de um possível mesmo site

Os rastreadores irão diferenciar escritas de sites e subdomínios durante a leitura do robots.txt, então é importante compreendermos que os seguintes exemplos são totalmente distintos dentro do contexto dos rastreadores:

* <http://example.com/>
* <http://shop.www.example.com/>
* <http://www.shop.example.com/>

Para mais informações acerca de como o arquivo Robots.txt é interpretado, acesse: [LINK](https://developers.google.com/search/docs/advanced/robots/robots_txt)

---

## Meu Portal RM continua sendo indexado. E agora?

Caso, mesmo após a atualização, o **Portal RM** continue aparecendo em buscas do Google por exemplo, talvez o acesso ao arquivo ***robots.txt*** esteja sendo negado ou esteja em um lugar incorreto.

Caso seu arquivo **robots.txt** esteja localizado corretamente conforme o passo-a-passo a baixo, pode ser que ele ainda não tenha sido lido pelos *rastreadores* e por isso, seu **Portal RM** ainda apareça no cache das buscas online.

O arquivo robots.txt só será lido pelos buscadores caso esteja na raiz do seu site. Leia a seção **Validade do Arquivo Robots.txt** para mais informações.

### Nesse caso, o que fazer?

Primeiramente, abra o **Gerenciador do Serviços de Informações da Internet (IIS)**da máquina onde está hospedado seu Portal RM:

Após, busque pelo site em que seu **Portal RM (Corpore.Net)** está hospedado. Caso tenha seguido a instalação via *instalador do Portal RM*, o **Corpore.Net** estará contido dentro do site **Default Web Site**

Como dito acima, a indexação em buscadores só obedecerá o arquivo **robots.txt** caso este esteja contido na raiz do site. Nesse caso, a primeira verificação que faremos é se o arquivo **robots.txt** está contido nesta raiz.

Compreenda que, dentro da estrutura do **IIS**, o **Default Web Site** é a raiz do seu site, enquanto o **Corpore.Net** é uma aplicação hospedada nesse site. Por isso que, nessa estrutura, o arquivo **robots.txt** não funcionará estando contido apenas na pasta do **Corpore.Net**

---

Primeiramente, clique com o botão direito no **Default Web Site**e em seguida em **Explorar (Explore)**

Uma pasta será aberta, possivelmente no caminho *C:\inetpub\wwwroot.*Esta é a raiz do seu site, dessa forma, é aí que o arquivo robots.txt deve estar. Caso não possua nenhum arquivo robots.txt nesta pasta, como no exemplo abaixo, precisaremos copiá-lo:

Voltaremos ao IIS e abriremos a pasta raiz do **Corpore.Net**, seguindo os mesmos passos acima:

A pasta onde o **Corpore.Net** está instalado irá abrir. Copiaremos o arquivo robots.txt contido nesta pasta e o colaremos na pasta raiz que tínhamos aberto antes:

Download do arquivo Robots.txt

Caso seu Corpore.Net não possua o arquivo ***robots.txt*** para ser copiado, é possível baixá-lo no link: 

### Testando...

Para testar se o arquivo **robots.txt** está contido em seu local correto, acesse-o por meio do seu navegador, seguindo a sintaxe: ***[MEUSITE]/robots.txt***. O arquivo deve abrir corretamente:

Aguarde alguns dias para a atualização dos indexadores e logo suas regras serão aplicadas corretamente. Caso deseje ver o resultado mais rapidamente, é possível utilizar ferramentas online de teste do arquivo robots.txt, tal qual [Testar Robots.txt - Google](https://support.google.com/webmasters/answer/6062598?hl=pt-BR) e [Testar robots.txt - Technical SEO](https://technicalseo.com/tools/robots-txt/)

Para criar um arquivo robots.txt personalizado ou permitir a indexação de páginas específicas, consulte a documentação da Google: <https://developers.google.com/search/docs/advanced/robots/create-robots-txt?hl=pt-br>
