---
content_hash: ddf6a10b0e6467f3e706849dea90eb5faa4c56f1f769119cc34ed43e661f110f
fetched_at: '2026-06-28T21:35:18.034295+00:00'
page_id: '146181573'
product: fluig
source: tdn-fluig
title: Desenvolvimento de formulário mobile
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=146181573
version: 223
---

# Índice

true.\*ndicenone

# Formulário *mobile*

---

No Fluig, é possível movimentar solicitações *workflow*, a partir de aplicativos. Devido a isso, ao salvar um formulário no Fluig, automaticamente o formulário mobile é gerado, de acordo com o mapeamento dos campos do formulário do processo.

Apesar do Fluig dispor da geração automática de formulários, existem diversas particularidades para o desenvolvimento de formulário mobile. Estas serão tratadas no decorrer deste guia.

# Recomendações para processos com formulário *mobile*

---

* **Formulário responsivo:** hoje no mercado existem variados tamanhos de telas e resoluções dos dispositivos, por isso qualquer formulário desenvolvido para mobile deve ser responsivo, ou seja, deve se adequar a qualquer tamanho de tela.
* **Estética:** a aparência visual e design do HTML devem ser atraentes para os usuários, conseguimos isso através de CSS, por isso recomendamos a utilização do Fluig Style Guide.
* **Usabilidade:** o formulário deve ser fácil de usar, contendo apenas os campos importantes para a tarefa ou processo.
* **Área de clique:** os elementos do HTML devem estar bem posicionados de forma que facilite a área de clique.

* **Posicionamento das ações:** as ações mais importantes devem estar posicionadas onde o usuário consegue alcançar facilmente, conforme a imagem abaixo.

* **Desenvolvimentos:**os desenvolvimentos devem ser feitos dentro dos eventos do processo ou de definições de formulário na Web, todos os eventos que são aplicados nos formulários Web também são aplicados nos formulários mobile. Para mais informações acesse o guia **[Desenvolvimento de Formulários](http://tdn.totvs.com/pages/viewpage.action?pageId=75270483)**.
* **Acesso a serviços internos**: o acesso a serviços internos pode ser feito através de Datasets via xmlRPC. Para mais informações, **[clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=146181573#Desenvolvimentodeformul%C3%A1riomobile-ConsumodeDatasetsviaxmlRPC)**.
* **Acesso a serviços externos:** recomendamos a utilização de Datasets para acessar serviços externos, esses Datasets são acessados no mobile via xmlRPC conforme descrito acima.
* **Nem todas informações precisam estar no formulário mobile:** o grande limitador do mobile é o tamanho de tela do dispositivo, por isso mapeie os campos que são mais importantes para que tenham prioridade no formulário. Existem campos que são de teor informativo e sem grande utilidade no processo ou tarefas, estes não precisam ser inclusos no formulário mobile.
* **Consultas aos datasets via Javascript em eventos para validação de formulários:** não é recomendada a consulta em Datasets dentro dos eventos **[beforeMovementOptions](https://tdn.totvs.com/pages/viewpage.action?pageId=270924158#EventosdeFormul%C3%A1rio-beforeMovementOptions)** e **[beforeSendValidate](https://tdn.totvs.com/pages/viewpage.action?pageId=270924158#EventosdeFormul%C3%A1rio-beforeSendValidate)**, pois cada requisição gera uma atividade assíncrona, cujo tempo de retorno pode interferir na lógica de validação definida.
* **Carregamento inicial do formulário dentro de Javascript**: dependendo da plataforma e da versão do sistema operacional, o tempo e a ordem de carregamento do formulário a partir de um .js pode resultar em um comportamento diferente do planejado.

0.5falsesamplesslide1Código que deve ser evitadojs2Como sugestão utilize

* Incluir a função metodoDeCarregamento() dentro de um *timeout*:

js

* Usar o método dentro do evento *onload*:

xml]]>

* **Formulários offline:** para a plataforma Android, o serviço da API pública [/public/ecm/dataset/search](http://fluig.totvs.com/api/public/ecm/dataset/search) não carregará os dados em modo *offline*, quando a requisição for realizada através do método POST.
* **Eventos de teclado na plataforma Android:** o evento *onkeypress*, atribuído para campos HTML, não é detectado pelo teclado da plataforma Android. Recomendamos utilizar o evento *oninput* e realizar os tratamentos necessários na chamada desse evento.

* A tag <input> possui a capacidade de suportar diferentes tipos de dados, dessa forma, como boa prática quando a mesma for utilizada, o atributo type deve ser definido, por exemplo:

js]]>

**Tipos:**Definições de formulário mobile suporta os tipos abaixo:

* text
* textArea
* radio
* select
* combobox
* checkbox.
* email (3)
* tel (3)
* range (3)
* date (3)
* time (1)(3)
* week (2)(3)
* number
* hidden
* password

#f2f2f2#f2f2f2

**(1)** Existe um bug no Android Lollipop (5.0) que inviabiliza o uso do tipo *time*. Para mais informações, [clique aqui](https://code.google.com/p/chromium/issues/detail?id=434695);

**(2)** O campo *week* não é suportado pelo iOS;

**(3)** Existe um bug no Android Jelly Bean (4.1, 4.2 e 4.3) que inviabiliza o uso do tipo *select*. Para mais informações, [clique aqui](https://code.google.com/p/android/issues/detail?id=42518#c12), [aqui](http://stackoverflow.com/questions/12090899/android-webview-jellybean-should-not-happen-no-rect-based-test-nodes-found/15153292#15153292) e [aqui](http://stackoverflow.com/questions/13438189/android-webview-in-different-tabs). Como medida de correção, a sugestão é utilizar o componente de Zoom: [Desenvolvimento de Formulários - Zoom](http://tdn.totvs.com/pages/viewpage.action?pageId=75270483#DesenvolvimentodeFormul%C3%A1rios-Zoom).

Atenção

Não está homologada a implementação de evento que utilizem *Gestures* (*swipe*, *longpress*, *tap*, entre outros) em formulário no Fluig Mobile.

# Benefícios

---

**Porque devo usar formulários no mobile?**

* Permite iniciar/movimentar solicitações de qualquer dispositivo móvel, independente de sua localização geográfica;
* Acesso rápido as informações, mostrando apenas informações mais relevantes;
* Permite a continuidade do processo, mesmo fora do ambiente empresarial;
* Através do recurso "Processo *Off-line*" é possível preencher informações mesmo sem acesso a internet, para futura sincronização.

# Criando um formulário mobile

---

Informações

Ao criar formulários para dispositivos móveis, é importante adotar algumas diretrizes para assegurar uma experiência eficaz para o usuário e garantir que a disposição dos campos e botões não comprometa a usabilidade. Nesse sentido:

* Evite posicionar os botões personalizados do formulário em áreas que concorram com o espaço reservado para o botão flutuante, geralmente utilizado ao acessar um processo ou tarefa. Isso visa garantir que os usuários não enfrentem dificuldades ao inserir dados no formulário.
* Garanta que os botões e campos do formulário sejam adaptáveis a diferentes tamanhos de tela e orientações, proporcionando uma experiência consistente em diversos dispositivos.
* Evite sobrecarregar a tela com múltiplos botões inferiores no formulário, dando prioridade à ação principal associada ao botão flutuante. Isso simplifica a interação do usuário, focando na funcionalidade mais relevante.
Atenção!

Ao realizar customizações, atente-se para que a renderização seja feita de forma correta em navegadores mobile. A customização deve estar compatível com o Safari para iOS e Chrome para Android.

Versões mínimas de cada plataforma que devem ser consideradas durante o desenvolvimento

| Versão mínima de cada plataforma | Versão mínima de cada browser |
| --- | --- |
| Android 4.0 (Ice Cream Sandwich) | Webkit 534.30 |
| iOS 7 | Mobile Safari 9537.53 |

No Fluig é possível criar definições de formulários de diferentes maneiras, utilizando o Fluig Studio, através da modelagem de processos *workflow* ou através de upload de formulário na navegação de documentos.

Acompanhe a seguir, movimentando-se pelas abas abaixo, as formas de criação de formulários:

Atenção!

Formulários de processos que possuem versões em rascunho não são carregados quando o usuário está offline (sem conexão com a internet). Somente informações do rascunho do processo são apresentadas.

0.5falseinstall-windowsfadetrue1Fluig StudioSelecione a linguagem

**Fluig Studio**

Para incluir um novo formulário com suporte a dispositivos móveis, desenvolva um único formulário que atenda todos requisitos para o funcionamento na web e mobile, e realize o procedimento padrão para **[exportação de formulário](https://tdn.totvs.com/pages/viewpage.action?pageId=73894420#Guiar%C3%A1pidodaplataforma-Exportandoumformul%C3%A1rio)**.

2Formulário mobile em processosTermo de uso

**Configuração de formulário mobile em processos**

É possível permitir a criação do Formulário mobile também através do **Gerador de Formulário**, conforme os passos abaixo:

**01.** Crie ou edite um processo existente e acionar o item **Formulário**;

---

**02.** Selecione a pasta destino onde o formulário será publicado, também atribua um título e descrição. Após isso, clique em **Criar Formulário**;

---

**03.**  Inclua os campos e em cada um deles, selecione se este será também adicionado ao formulário para dispositivos móveis, clicando na opção **Formulário Mobile?**.

falseInformação

Nem todos os campos mapeados no formulário do processo podem ser mapeados para o formulário em dispositivos m´oveis. Os campos que podem ser mapeados exibem a opção **Formulário mobile?**

3Upload via navegação de documentosInstalação do fluig

**Upload via navegação de documentos**

No upload via navegação de documentos é feito uma publicação de um formulário único, que deve atender os requisitos de funcionamento para web e mobile.

Atenção

As definições de formulários geradas pelos métodos de criação acima elencados, precisam ser editados e caso necessite de algum desenvolvimento especial, eles são gerados automaticamente contendo os itens básicos para seu funcionamento.

Atenção

Ao contrário da web, o comportamento da função *setHidePrintLink* no mobile não esconde o botão de impressão. Mas também não permite que o usuário efetue a impressão do formulário.

# Carregando dados do dataset em modo o*ffline*

---

Para realizar o carregamento dos dados do dataset em modo *offline* no formulário do processo, é necessário relacionar o dataset ao campo zoom faz uso durante o modo *offline.*Acompanhe a seguir, o procedimento para configuração do carregamento:

1Localizar o formulário

**Localizar o formulário**

**01.** Dentro do ECM, localize o formulário que está sendo utilizado no processo e em seguida acione **Propriedades**.

Datasets do Formulário

**Datasets do formulário**

**02.** Após clicar nas propriedades do formulário, navegue até a aba **Datasets do Formulário** e relacione o dataset ao qual está sendo utilizado no campo zoom.

Atenção

Após definir as configurações, é necessário efetuar a limpeza de cache no aplicativo e realizar uma nova consulta.

Acesse nossa documentação e saiba mais sobre como **[Habilitar dataset offline no mobile](https://tdn.totvs.com/pages/viewpage.action?pageId=235598394#Plataforma%E2%9D%99Datasets-Habilitardatasetofflinenomobile)**.

# Desenvolvimento de formulário mobile

---

Com a inclusão de formulários que suportem a visualização em dispositivos móveis, é possível movimentar solicitações *workflow* e realizar o preenchimento das informações de formulários com maior mobilidade e agilidade.

## Funções mobile

---

### getAttachments

É uma função que retorna uma Promise com a lista dos anexos do formulário.  Funciona de forma offline.

No exemplo abaixo foi utilizado um await para aguardar a lista dos arquivos que pode ser vazia, caso não haja anexos.

jsChamada no JS

O objeto retorna sempre um json que é uma lista de arquivos. Cada arquivo pode ou não ter os dados, conforme abaixo:

jsEclipsetrue#f2f2f2#f2f2f2

Caso não tenha a informação no arquivo anexado, o valor será null por padrão.

**Exemplo de chamada no JS de forma async**:

js

### beforeValidateAttachments

---

Este evento acontece ao clicar em "enviar" no navegador antes de abrir a tela de movimentação. Por isso, esse código deve ser implementado em um arquivo javascript vinculado ao formulário html. Ele recebe um parâmetro que é a lista de todos os anexos que estão vinculados no formulário e é muito útil para algumas validações antes mesmo de ser enviado para o servidor. 

js

* Os dados sempre serão uma lista de arquivos com os valores:

powershellEclipsetrue

## Pai x Filho e Zoom para dispositivos móveis

---

A partir do TOTVS Fluig Plataforma 1.5.2 (*server*), temos uma técnica para utilização de Pai e Filho e Zoom que facilita o desenvolvimento sobre a plataforma. Usando o [Fluig Style Guide](http://style.fluig.com/) tudo ficará mais responsivo e esses dois componentes se adequam a web e ao mobile.

#f2f2f2#f2f2f2

Leia mais detalhes na nossa documentação: [Desenvolvimento de Formulários - Zoom](https://tdn.totvs.com/pages/viewpage.action?pageId=663066946#Personaliza%C3%A7%C3%A3odeformul%C3%A1rios-Zoom) e [Desenvolvimento de Formulários - Pai x Filho](https://tdn.totvs.com/pages/viewpage.action?pageId=668198714#Personaliza%C3%A7%C3%A3odeformul%C3%A1riosContinua%C3%A7%C3%A3o-PaixFilho).

Atenção

* O Fluig dispõe de um serviço nativo para consumo de dados de datasets no componente de zoom. Não é permitido o uso de serviços personalizados para este componente.

* Procure utilizar um número limitado de campos em componentes de Zoom para que se adequem melhor ao tamanho de tela. A utilização de um grande número de campos, ou do zoom dentro outros componentes, pode comprometer a visualização dos dados.
Atenção - Trabalhando com tabelas

* Não é recomendada a utilização de *underscore* - "\_\_\_" - na propriedade *name* de uma coluna (tag *<td>*) em formulários que utilizem Pai x Filho pois a mesma não é renderizada no mobile.

### Inserir anexos da solicitação diretamente do formulário

---

Há uma maneira bem simples para salvar anexos upload através de um botão no formulário. Para isso é necessário inserir no evento ***onclick*** do ***button*** o método ***showCamera***:

Atenção

Não é recomendada a troca do nome da função para o método **showCamera no iOS**. Isso faz com que o método não funcione conforme o esperado. 

xml
]]>

O parâmetro passado na função ***JSinterface.****showCamera*** é uma String e corresponde ao nome do anexo que será salvo na listagem de anexos daquela solicitação.

Também é possível limitar o acesso ao componente, deixando-o com acesso somente à câmera, galera ou explorador de arquivos do dispositivo utilizado, abaixo mostramos o exemplo de implementação de cada um deles:

falsesample1Acesso somente à câmera

Para que o componente showCamera permita o acesso **apenas a câmera** do dispositivo, é necessário informar um parâmetro em seu código de acordo com o exemplo abaixo:

xml2Acesso somente à galeria

Para que o componente showCamera permita o acesso **apenas a galeria** do dispositivo, é necessário informar um parâmetro em seu código de acordo com o exemplo abaixo:

xml3Acesso somente ao explorador de arquivos

Para que o componente showCamera permita o acesso **apenas ao explorador de arquivos** do dispositivo, é necessário informar um parâmetro em seu código de acordo com o exemplo abaixo:

xmlDica!

Ao acessar formulários que utilizam o componente **showCamera** no My Fluig, é possível anexar diferentes tipos de arquivos, como PDF, DOCX, XLSX, entre outros formatos. Os anexos podem ser adicionados por meio do explorador de arquivos correspondente ao dispositivo utilizado.

A partir da atualização 1.5.5

O método ***JSinterface.showCamera***, também é aplicado na plataforma web. Acessando o Fluig Plataforma pelo navegador, ao clicar em um botão utilizando o recurso você será direcionado para a aba **Anexos** e uma janela será exibida para a seleção dos arquivos.

Acessando a aba de **Anexos** será possível realizar o *upload* de apenas um arquivo por vez.

#f2f2f2#f2f2f2

Tentar selecionar mais que um causará erro.

### Desabilite o evento Pull to refresh do componente nativo

---

Há uma maneira bem simples para desabilitar o evento de Pull to refresh responsável por atualizar os dados do formulário. Para isso é necessário inserir o método **disablePullToRefresh**:

xml
function disablePullToRefresh(){
return true;
}
]]>

### Como identificar se estou usando o mobile nos eventos?

---

Com esse recurso é possível aplicar um desenvolvimento e/ou restrição somente no formulário mobile, independente da Web. Assim posso definir que um processo ou atividade vai receber um valor diferenciado ou que determinada atividade não pode ser executada pelo mobile via desenvolvimento.

Existe duas formas de fazer tal desenvolvimento:

**Eventos do Formulário**

---

Todos os eventos que recebem no método o form podem fazer um desenvolvimento exclusivo para o formulário mobile:

* AfterProcessing
* AfterSaveNew
* BeforeProcessing
* DisplayFields
* EnableFields
* InputFields
* ValidadeForm

Para utilizar o evento é necessário fazer a seguinte chamada: **form.getMobile()**, onde retornará um booleano indicando se é um formulário mobile ou não. Exemplo:

javascript

**Eventos do Processo**

* beforeMovementOptions
* beforeSendValidate

Importante

 Os eventos "beforeMovementOptions" e "beforeSendValidate" serão executados no dispositivo mobile antes mesmo de serem enviados para o servidor.

Para mais informações sobre estes eventos acesse a página [Desenvolvimento de Workflow](https://tdn.totvs.com/x/widbB).

Nos eventos de processo, a propriedade **WKMobile** identifica se a ação foi realizada pelo dispositivo móvel. Ela pode ser utilizada nos eventos do processo conforme exemplo:

javascript

### Consumo de Datasets via xmlRPC

---

O acesso de datasets pelo mobile é realizado com o xmlPRC, desse modo é possível trocar de informações com Fluig via AJAX. Para utiliza-lo, basta acionar as seguintes importações no HTML do formulário:

javascript
]]>

O acesso aos Datasets é igual à web, a seguir são apresentados alguns exemplos:

**Datasets internos Fluig**

---

Este tipo de Dataset permite navegar em dados das entidades do próprio Fluig Plataforma, como usuários, grupos, processos ou tarefas por exemplo. Esses datasets são pré-definidos, por isso não podem ser alterados pelo usuário. A lista com os datasets disponíveis pode ser consultada .

jstrue 0){
document.getElementById("colleagueName").value = colleagues[0].colleagueName;
document.getElementById("login").value = colleagues[0].login;
}else{
alert("Nenhum Usuário Encontrado");
}]]>#f2f2f2#f2f2f2

Para atualizações anteriores ao TOTVS Fluig Plataforma 1.5.6, substituir a linha 3 por:

javascript

**Datasets internos formulário**

---

Este tipo de Dataset permite navegar nos dados existentes em formulários de uma determinada definição de formulário publicada no Fluig. Para que uma definição de formulário seja disponibilizada como Dataset, é necessário preencher o campo **Nome Dataset** na publicação da definição de formulário. O

valor informado será utilizado para a busca do Dataset no Fluig;

javascript#f2f2f2#f2f2f2

Para fazer o download de um exemplo de formulário utilizando xmlPRC clique .

**Chamadas assíncronas**

---

A partir do TOTVS Fluig Plataforma 1.5.6, é possível realizar chamadas assíncronas:

javascript 0){
document.getElementById("colleagueName").value = colleagues[0].colleagueName;
document.getElementById("login").value = colleagues[0].login;
}else{
alert("Nenhum Usuário Encontrado");
}
}, error: function(jqXHR, textStatus, errorThrown) {}
});
]]>javascriptsampleImportante!

* A geolocalização funciona apenas em ambientes **https**. Em ambientes http o navegador não permite informar a geolocalização.
* Essa técnica pode ser aplicada em Android quanto em iOS.
1Geolocalização em formulários

Para utilizar a geolocalização em formulários, basta incluir esse script no html:

javascript";
var lat = position.coords.latitude;
var longi = position.coords.longitude;
document.getElementById("latitude").value = lat;
document.getElementById("longitude").value = longi;
}
function showError(error)
{
switch(error.code)
{
case error.PERMISSION\_DENIED:
doc.innerHTML="Pedido de Geolocalização negado pelo usuário."
break;
case error.POSITION\_UNAVAILABLE:
doc.innerHTML="Informação de localização não está disponível."
break;
case error.TIMEOUT:
doc.innerHTML="Solicitação de localização não retornou em tempo hábil (timeout)."
break;
case error.UNKNOWN\_ERROR:
doc.innerHTML="Erro desconhecido."
break;
}
}]]>2Geolocalização em páginas

Para utilizar a geolocalização em páginas, processos e na home é bem simples, basta incluir esse script no html:

javascript";
var lat = position.coords.latitude;
var longi = position.coords.longitude;
document.getElementById("latitude").value = lat;
document.getElementById("longitude").value = longi;
}
function showError(error)
{
switch(error.code)
{
case error.PERMISSION\_DENIED:
doc.innerHTML="Pedido de Geolocalização negado pelo usuário."
break;
case error.POSITION\_UNAVAILABLE:
doc.innerHTML="Informação de localização não está disponível."
break;
case error.TIMEOUT:
doc.innerHTML="Solicitação de localização não retornou em tempo hábil (timeout)."
break;
case error.UNKNOWN\_ERROR:
doc.innerHTML="Erro desconhecido."
break;
}
}]]>

Dica

Para baixar um exemplo de formulário com geolocalização clique .

Veja o exemplo (**form-mobile-waze**) em nosso repositório [aqui](https://git.fluig.com/projects/SAMPLES/repos/projetos/browse).

ImportanteEsta técnica funciona apenas em ambiente **HTTPS** a partir do Android 6.0 e iOS 10.

### Explorando o input file no mobile

---

É possível manipular arquivos diretamente do formulário mobile através do input file, onde no aplicativo mobile é possível acessar arquivos do dispositivo ou incluir uma imagem diretamente da câmera. Importante observar que ao escolher um ou mais arquivos através desse componente, esses arquivos

não serão anexados à solicitação em questão, uma vez que essa funcionalidade é exclusiva do recurso showCamera descrito nessa documentação.

Exemplo de implementação]]>

Um ponto para observar é que, ao realizar o upload direto da câmera, não é possível adicionar várias fotos simultaneamente, mesmo quando o parâmetro 'multiple' é especificado, sendo este um comportamento do próprio sistema operacional. O cenário de múltiplo upload pode ser realizado acessando os

arquivos já existentes do dispositivo.

falsesamples1Veja o recurso na prática

### Formulário único

---

A partir da **atualização 1.5** do Fluig Plataforma os formulários da web e do *mobile* devem ser criados de forma única. Sendo assim, o formulário deve atender tanto o *mobile* quanto a web.

Para criar formulários com este novo padrão verifique o [Fluig Style Guide](http://style.fluig.com/).

### Anexos de formulário

---

1. **Download de anexos:** este procedimento será automático, porém apenas os anexos do formulário são baixados.
2. **Download de anexos em processos *offline*:** durante o *download* dos processos *offline* os anexos do formulário são baixados e estarão disponíveis para utilização de maneira *offline*.

Importante

* Para o funcionamento de anexos do formulário, o caminho dos arquivos devem ser relativos e não podem ser externos.
* No sistema operacional Android não é recomendado carregar anexos do formulário via requisições como XMLHttpRequest. O carregamento do conteúdo de arquivos via caminhos relativos já é suficiente.
Dica!

Recomendamos a leitura da documentação Eventos de formulários na seção das funções [getAttachments](https://tdn.totvs.com/pages/viewpage.action?pageId=270924158#EventosdeFormul%C3%A1rio-getAttachments) e [sendAttachments](https://tdn.totvs.com/pages/viewpage.action?pageId=270924158#EventosdeFormul%C3%A1rio-sendAttachments). Referentes ao retorno e envio das informações dos anexos.

### Guia de estilos off-line

---

Agora é possível utilizar o guia de estilos em modo off-line sem a necessidade de qualquer conexão a internet, ficou bem mais fácil e independente personalizar seu formulário para processo off-line. Uma vez ao dia o Fluig Mobile ira verificar novas atualizações, caso alguma atualização esteja disponível, o download da mesma será feita automaticamente de forma rápida e transparente, sem precisar se atentar a formas manuais e demoradas para atualização. O guia de estilos off-line está disponível tanto para Android como para IOS.

### Versões mínimas dos browsers suportados

---

Cada uma das plataformas utiliza um browser diferente para a renderização dos formulários. Esta informação deve ser considerada durante o desenvolvimento para evitar problemas de compatibilidade com os arquivos JavaScript/CSS. Acesse a  e veja a versão mínima dos browsers de cada plataforma que deve ser considerada durante o desenvolvimento.

### Atualizar anexos de javascript de formulário mantendo sua versão ao importar para o Eclipse

---

No arquivo html do formulário, é necessário fazer a referência ao arquivo javascript como no exemplo abaixo:

const head = document.getElementsByTagName('head')[0];
const script = document.createElement('script');
script.src = `testeMobile.js?${Date.now()}`;
script.type = 'text/javascript';
head.appendChild(script);
]]>

O código acima faz com que ao importar o formulário mantendo sua versão, será gerada uma data na referência do arquivo, invalidando o cache do aplicativo My Fluig
