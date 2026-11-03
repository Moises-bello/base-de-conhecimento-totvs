---
content_hash: 6226eaeac085fc013896c9d4f82ac9b981a88ea96e4ad29d3900a9fb5d022a0b
fetched_at: '2026-06-29T00:11:20.721138+00:00'
page_id: '687737814'
product: rm
source: tdn-rm
title: Integração - RD Station
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=687737814
version: 118
---

#FF9000Introdução**A partir da versão 12.1.2209**, o Portal de Imóveis está apto a gerenciar aplicativos cadastrados no RD Station, através de uma configuração simples que pode ser realizada seguindo alguns passos importantes.  
  
  
  
  
#FF9000Introdução:

---

Neste material iremos entender como parametrizar e integrar o aplicativo do RD Station ao Portal de Imóveis, facilitando o gerenciamento e visualização de diversas funções tais como: 

* Webhooks;
* Contatos;
* Campos customizados;
* Códigos de monitoramento;
* Manipular os estágios de funil de seus contatos;
* Envio de eventos para os contatos.
* Esta apresentação abaixo possui informações referentes ao RD Station e suas principais funcionalidades.  
    
  250

## **Para realizar a integração com aplicativos do RD Station, consulte a documentação abaixo:**

---

RD STATIONAplicativos

**Cadastros de tipos de Aplicativos no RDStation para integração com o Portal de Imóveis:**

### **Integração com o Marketing:**

---

Para que este procedimento seja realizado é necessário uma conta do RD Station:  <https://accounts.rdstation.com.br/>

* Informe o usuário de acesso a sua conta;
* Login \ Senha:
* Clique em Acessar: Acessar RM Station Marketing

* Acesse a conta na app store do RD Station onde vocÊ será direcionado para este site: <https://appstore.rdstation.com/>

* Clique em Acesse sua conta:

* Insira suas credenciais de acesso:

* Selecione a opção: Meus Apps (Para visualizar os Apps já existentes) ou Quero Criar um aplicativo (para inclusão de um novo aplicativo);

* Informe o nome do aplicativo que deseja criar, e selecione a opção: **Aplicativo Privado**

Informe os dados do APP nos campos:   
***Nome do aplicativo (informe um nome que você dará ao seu app criado);***  
***Categoria: Selecione Marketing;***  
***Idiomas do Aplicativo: (informe o idioma de preferencia que você utilizará);***  
***Site da empresa: (informe o site da sua empresa;***  
***URLs de Callback:*** ***(abaixo iremos instruir como criar o código para utilização); Após a geração da URL (Basta inserir o Cod neste campo e salvar as informações da tela)***

URL de Callback

**Criando uma URL de Callback:**

---

Para criar uma URL de Callback acesse o Portal de Imóveis > Backend > Integração > Adicionar , neste momento será gerado uma URL de Callback (neste momento a mesma será copiada para a área de transferência e deverá ser incluída no campo URLs de Calback (no RD Station) no momento da inclusão do Aplicativo.

Ainda na tela de integração, é possível clicar no botão URL Callback (Copiar URL), onde a mesma também poderá ser copiada.

* Neste momento será apresentada a tela onde foi criado os códigos do: Client\_ID e Client\_Secret.  
  Copie o código Client\_ID e em seguida retorne ao Portal de Imóveis no menu de Integração, clique no botão Editar deste aplicativo que está sendo configurado onde será apresentada a tela com os dados a serem preenchidos.  
  Cole o código no campo Client\_ID e em seguida retorne ao RD Station e desta vez copie o código Client\_Secret que deverá ser colado no campo Client\_Secret no Portal de Imóveis.
* Realizado estes passos, clique em salvar.

* ***Veja no menu integração > Aplicativos do Portal de Imóveis onde (ao clicar em Editar) os códigos que anteriormente foram copiados do site do RD Station serão colados respectivamentes;***

  
  

* Cole o código no campo Client\_ID e Client\_Secret (em seguida clique em salvar)

  

**Gerando o CODE de autorização.**

---

Neste momento será necessário gerar um código de autorização. Para realizar esta parametrização, acesse o Portal de Imóveis > Backend > Integração > (no Aplicativo que será configurado) ao final da linha > Clique em Editar > Gerar código no RD , esta ação irá redirecionar para o site do RD Station onde deverá ser selecionado o site que terá o acesso permitido (clique em continuar e na outra tela exibida: conectar), instantaneamente o CODE será gerado no Portal de imóveis para aquele aplicativo.

Com este conjunto de informações, é possível validar se a integração está validada ao clicar no botão Testar Integração.

Ao clicar neste botão será integrado e apresentado na tela estas informações.

Este processo possibilitará realizar chamadas das APIs no RD Station.  
  
Link documentação de criação do appstore   
para configurar no PI:  
<https://developers.rdstation.com/reference/criar-aplicativo-appstore>

**Integração com o CRM:**

---

* Este tópico ensina como criar os parametros da integração com CRM no RD Station e gerar o Token para integração.   
  Para geração do Token acesse as instruções no link:   
  <https://ajuda.rdstation.com/s/article/Gerar-e-visualizar-Token?language=pt_BR>   
    
  ***Observação:** Importante lembrar que após o Token gerado (se em algum momento) o usuário clicar em desativar Token (esta chave será excluída) sendo necessário gerar uma nova chave que deverá ser informada novamente no portal de imóveis.*
* Acesse o Portal de imóveis e acesse o menu: Backend > Integração > RD Station >Aplicativos, clique em ***Adicionar*** e em seguida Selecione CRM.
* Informe o token e em seguida clique em salvar.

**Importante: Evolução na Integração CRM (A partir da versão 12.1.2606)**

Se você utiliza o Portal de Imóveis na versão 12.1.2606 ou superior, a integração com o RD Station CRM evoluiu! A autenticação agora é feita de forma simplificada, utilizando o mesmo padrão de segurança do RD Station Marketing, via App Store.

Como configurar na nova versão: O processo é idêntico ao do Marketing. Basta acessar Integração > Aplicativos, selecionar a categoria "CRM" e preencher o Client ID e Client Secret gerados no seu aplicativo privado da RD.

Campos Personalizados

### **Configuração de campos no RD Station integrados com o Portal de Imóveis:**

---

Nesta seção iremos visualizar como configurar os campos no RD Station que serão associados no Portal de Imóveis.

Para que este procedimento seja realizado é necessário acessar o RD Station, acessando o menu: Converter > Campos Personalizados

Neste momento selecione a opção: Criar campo personalizado

Utilizaremos como exemplo a inclusão do campo Estado Civil. Preenchendo os campos que serão relacionados. Ao final salve o registro incluído.

Acesse o portal de Imóveis, no menu: Integração > Campos personalizados

Clique em Sincronizar campos;

Os campos serão sincronizados e apresentados no Portal.   
Em nosso exemplo realize a edição do campo Estado Civil afim de que as chaves possam ser associadas as tabelas.

Associe os campos respectivos e em seguida clique em salvar.

**Configurando Campos Personalizados no RD Station CRM:**

Para facilitar a gestão de informações, clientes na versão 12.1.2606+ possuem uma tela exclusiva para a criação de campos personalizados diretamente no RD Station CRM, sem precisar sair do Portal.

**Como criar um novo campo pelo Portal:**

* Acesse o menu Integração > Campos personalizados.
* Clique no botão **Adicionar campo**.
* Preencha as informações:
  + **Entidade:** O sistema já preenche automaticamente como "Negociação".
  + **Campo:** Selecione a informação do Portal (ex: Empreendimento, Bloco, Unidade, Data da proposta) que alimentará o RD. Dica: Ao selecionar campos como "Empreendimento", o sistema carrega as opções ativas do seu banco de dados automaticamente.
  + **Label:** Digite o nome visual do campo para o corretor no RD.
  + **Tipo:** Defina se será Texto, Data, Seleção Única ou Múltipla.
  + Também poderá definir uma **ordem** para o campo personalizado e se depois de ser salvo, ao editar, se **p****ermitir adicionar nova opção**.
* Clique em **Criar**. O campo será gerado no RD Station CRM e no PI.

**Observação**: ao criar o campo personalizado diretamente pelo RD Station CRM ele será automaticamente integrado ao Portal de imóveis.

Inclusão de Leads

### **Introdução:**

---

Nesta seção iremos visualizar a atualização de um Lead após uma venda ser enviada para o backoffice.

Observações:

Como Pré- Requisito, é necessário realizar a integração do Portal de imóveis com o RD Station para que os dados gerados sejam integrados:  
  
**Saiba mais acessando o link abaixo:**  
[RD Station - Token WebHook - Cadastro de Leads enviados pelo RD](https://tdn.totvs.com/pages/viewpage.action?pageId=687737814#RDSTATION-1513287362)

**Procedimentos para utilização:**

---

Para que este procedimento seja realizado é necessário acessar o RD Station incluído um Lead. Ao acessar esta tela observe alguns campos relevantes:

* **Nome do Lead**;
* **Cargo;**
* **Estágio do Funil;**
* **Dono do Lead**: Este campo, ao ser preenchido, irá registrar o nome do corretor no Portal de Imóveis. É importante observar que, para que o nome do corretor seja preenchido corretamente no momento da integração, ele deve já estar cadastrado no Portal de Imóveis com este mesmo e-mail informado no campo.  
  Em seguida marque a opção:  observando que a mesma estará sendo apresentada como a imagem abaixo:

Ao acessar o portal de imóveis observe que o cadastro já estará apresentando o registro integrado:

No portal de imóveis, a alteração da situação do lead para **'Banco'** atualiza os dados no RD Station e **desmarca a opção de oportunidade**. Caso o lead volte a manifestar interesse, será necessário marcar a oportunidade novamente de forma manual.

**OBS:** Ao cadastrar leads no RD Station, informe o número de celular no campo “Celular” com o formato: 55 (31) 99999-9999

Integração com Backoffice

### **Incluindo uma proposta no portal de imóveis e enviando para o backoffice:**

---

Para que o Lead seja atualizado, será necessário incluir uma Proposta para este Lead e em seguida avançar esta para o Backoffice.

Ao realizar esta ação o sistema irá informar que haverá uma atualização deste Lead no RD Station.

A venda Foi gerada para o Backoffice.

Acesse novamente o RD Station e observe que o registro deste Lead foi atualizado para Cliente.

Status do LEAD

### **Motivo de desistência, alterando o Status do Lead no rd station:**

---

É possível que o SDR informe o motivo de desistência de uma proposta (no menu de interesse) e neste momento o RD Station irá atualizar o status deste Lead.

Estágio do Funil: **Cliente**

Observe que foi informado um interesse que possui uma situação de desistência (Perdido). Neste momento o sistema irá atualizar o estágio do funil deste cliente no RD STATION.

Estágio do Funil atualizado para Lead, e foi desmarcada a opção **Marcar oportunidade.**

Observação

Caso este Lead já possua uma proposta gerada para o Backoffice, o mesmo terá seu status alterado para **Cliente** (como visualizamos acima).  
Nesta condição, ao acessar a GUIA interesses (não será possível alterar uma **situação de Interesse para o Status PERDIDO.**Caso o usuário teste realizar esta ação o sistema retornará a seguinte mensagem:

**Interesse do cliente fica como "Perdido" no PI (Modelo Novo)**

Quando um cliente (Lead) é atendido no PI, pode acontecer de ele não seguir com a compra naquele momento. Nesses casos, o interesse dele pode ser marcado como "Perdido", e o Lead vai para o Banco de Leads.  
Mas se esse cliente voltar a demonstrar interesse e for marcado novamente como Oportunidade no RD Station, é importante entender o que deve ser feito no PI para retomar o atendimento.

Comportamento no sistema, na prática:

 1. O Lead entra no sistema PI

* O cliente é captado no RD Station.
* Quando é marcado como Oportunidade, ele entra automaticamente no fluxo de atendimento do PI.

2. Interesse é marcado como Perdido

* No PI, você acessa o cadastro do cliente.
* Vai na aba Interesse e preenche:

  + Situação: Perdido
  + Motivo: por exemplo, Preço Alto

* O sistema entende que aquele cliente não quer mais comprar.
* Resultado: o cliente é movido para o Banco de Leads, saindo do atendimento ativo.

 3. Cliente volta a demonstrar interesse no RD

* No RD Station, o cliente é marcado novamente como Oportunidade.

Importante: O que acontece nesse momento?

* O cliente sai do Banco de Leads e vai para em atendimento:
* Ele volta sozinho para o atendimento no PI.
* Toda vez que um lead já **existente em banco** manifesta novo interesse, é registrada uma anotação (timeline) com o nome do empreendimento e da mídia de origem.
Time Line \ Dados Externos

Para que a Time Line possa ser apresentada e atualizada na edição de um Lead, estes dados são originados a partir do momento em que as informações são preenchidas na TIMELINE na edição do Lead.

Já os dados externos são originados a partir das informações inseridas neste registro através da Integração com o RD Station.

Acompanhamento de Engajamento e Negociações na Tela de Pessoas (Versão 12.1.2606+)

Para que o corretor entenda todo o contexto do Lead antes de uma venda, a visão de "Pessoas" no Portal de Imóveis foi evoluída para exibir dados em tempo real do RD Marketing e CRM.

**Como visualizar:** Ao abrir o cadastro de um Prospect, desde que as integrações estejam ativas, duas novas caixas aparecerão na lateral direita:

* **RDStation Marketing (Botão Lead):** Exibe informações de captação, origem da oportunidade, etapa do funil e campos customizados respondidos pelo cliente.
* **RDStation CRM (Botão Negociações):** Mostra as negociações em andamento, status, previsão de fechamento e as anotações do corretor feitas diretamente no RD, centralizando o histórico.

**Simulação de Proposta Direto da Negociação (A partir da versão 12.1.2606)**

Para tornar o processo de vendas ainda mais ágil, o corretor pode iniciar a simulação de uma proposta diretamente do modal de "Negociações (RD Station CRM)".

Ao abrir as negociações de um cliente na tela de Pessoas, um botão **"Simular"** estará disponível dentro de cada card de negociação.

**Como realizar a simulação:**

1. No Portal de Imóveis, acesse o menu de **Pessoas** e abra o cadastro do cliente desejado.
2. No menu lateral direito, localize o quadro "RDStation CRM" e clique no botão **Negociações**.
3. O sistema abrirá uma janela com os *cards* de todas as negociações ativas desse cliente. Localize a negociação que deseja evoluir para uma venda e clique no botão **Simular**.
4. **Redirecionamento Inteligente:** O sistema utilizará a informação de "Empreendimento Procurado" daquela negociação e abrirá automaticamente o **Mapa de Disponibilidade** do empreendimento correto.
5. No mapa, selecione a unidade e o bloco desejados e clique novamente no botão **Simular**.

**O que acontece a seguir:**

* **Preenchimento Automático:** Você será redirecionado para a tela de "Preencher Proposta". O cliente (comprador) já virá preenchido e a negociação do RD CRM já estará vinculada, a mesma selecionada por você na tela de pessoas.
* **Cálculo Automático (Plano Padrão):** Se o empreendimento selecionado possuir um plano de financiamento padrão (default), a proposta será aberta **já salva e com o plano de pagamento totalmente calculado**, eliminando a necessidade de montar as parcelas manualmente.

  *(Nota: caso o empreendimento não possua um plano padrão, a aba de condições de pagamento abrirá em branco para preenchimento manual).*

  **Como configurar o Plano Padrão (Modalidade) no TOTVS RM:**

  **Passo a passo no RM:**

  1. Acesse o módulo Gestão de Imóveis e vá até a aba **Venda**.
  2. Clique no ícone **Empreendimento.**
  3. Na lista, selecione o empreendimento desejado e clique em **Editar** (ícone de lápis).
  4. Na tela de edição, olhe o menu lateral esquerdo. Dentro do grupo **Dados Gerais**, clique na opção **Informações**.
  5. Localize o campo **Modalidade** e clique no botão de busca (`...`) ao lado dele.
  6. A janela de "Modalidade de Venda" será aberta. Selecione qual será a modalidade padrão e clique em OK.
  7. Salve o cadastro do empreendimento.
* **Sincronização de Campos:** Ao salvar a proposta, os campos personalizados configurados para o RD Station (como Bloco, Unidade, Valor e Situação) são preenchidos e sincronizados com o CRM de forma automática.
Parâmetros

Trata-se de uma lista de parâmetros relacionados a integração do RD Station:   
Este parâmetros podem ser configurados acessando ***Backend / Integração / RD Station / Aplicativos:***

* ***Aplicativos*:** São os aplicativos possíveis de serem cadastrados e integrados com o Portal de Imóveis.

### **Parâmetros**

---

* ***RD Station - Token WebHook - Cadastro de Leads enviados pelo RD*:**Para que o RD Station envie um lead para o PVI no momento em que ele for marcado como "Oportunidade" é necessário definir um token (chave de segurança para garantir identidade) onde o RD Station enviará nas requisiçoes de cadastro lead. **informe um nome neste campo: Exemplo: portaltotvs123456 (em seguida copie esta chave)**  
    
  Na página principal do RD Station selecione a opção Integrações:  
    
    
    
  Selecione a opção de Webhooks e em seguida clique em configurar:  
    
    
    
  Selecione a opção criar Webhook preenchendo as informações do nome, URL do portal **(veja observação abaixo)** e o Gatilho oportunidade em seguida salve estas configurações.  
    
    
    
    

  - URL: Nesta parte deverá ter uma atenção mais específica, observe que na primeira parte será informada o acesso ao Portal de Imóveis, em seguida para compor a URL informe o endereço: api/webhook/rdstation/ e para finalizar a chave que foi gerada no Portal de imóveis (nos parâmetros de Pessoas). Clique em “Salvar Webhook”  
  Veja o exemplo detalhado:

OBSERVAÇÃO

Abaixo segue a parametrização do Whebhook anterior a versão 12.1.2209,  observe que os parâmetros disponibilizados encontram-se em outra Guia, conforme orientações abaixo:  
Acesse:***Backend / Integração / RD Station / Aplicativos:***

* ***RD Station - Token WebHook - Cadastro de Leads enviados pelo RD*:**Para que o RD Station envie um lead para o Portal de Imóveis no momento em que ele for marcado como "Oportunidade" é necessário definir um token (chave de segurança para garantir identidade) onde o RD Station enviará nas requisições de cadastro lead.

Para mais informações, sobre como enviar o Lead para o Portal de Imóveis, veja o vídeo abaixo do nosso How-To:

Painel de Ofertas do Empreendimento

Ao acessar o painel de empreendimentos, quando integrado ao RD Station, teremos uma lista de subunidades disponíveis e seus status como *disponível*, *em proposta*, *vendido*, dentre outras.  
Quando o status da subunidade é "*disponível*", poderemos passar a ofertá-la como um produto diretamente no RD Station, inserindo algumas informações básicas relacionadas a esta oferta.

**Para dar inicio a oferta do produto, realize as ações abaixo:**  
  
1) Acesse o Menu empreendimentos, escolha o empreendimento que será utilizado e clique na opção Painel:

2) Na tela apresentada clique na subunidade em questão e selecionar "*RD Station: Ofertar Produto*".

Serão apresentadas as informações a seguir:

* **Nome**: O sistema automaticamente carrega o nome do empreendimento, do bloco e da subunidade por padrão. O usuário pode alterar o nome caso seja necessário.
* **Descrição**: A descrição do produto que será exibida no RD Station. O campo é livre para edição pelo usuário.
* **Tabela de preço**: O sistema irá listar todas as tabelas de preço associadas a subunidade, possibilitando a escolha da tabela de preço associando-a ao produto ofertado.
* **Lead**: O Portal faz a busca dos Leads que vieram do RD Station (Leads marcados como oportunidade no RD Station). Ao selecionar um lead, o sistema irá listar as oportunidades de quaisquer campanhas que o Lead esteja associado bem como outras informações importantes. Vale lembrar que a busca pode ser feita pelo nome, e-mail ou telefone do Lead.
* **Oportunidade**: Serão listadas todas as oportunidades de quaisquer campanhas que o Lead esteja participando. Ao selecionar a oportunidade, serão preenchidos os detalhes abaixo, estes campos são informativos e buscados diretamente do RD Station:
  + **Campanha**: A campanha atrelada a oportunidade.
  + **Empresa / Cliente:** A empresa associada ao Lead;
  + **Campos personalizados**: Caso existam campos personalizados associados ao lead, eles serão mostrados aqui.
  + ****Produtos associados a oportunidade**: O sistema irá enumerar a quantidade de produtos já associados a determinada oportunidade.**

3) Uma mensagem será apresnetada para usuário informando que a integração com o RD Station CRM foi concluída.

4) Ao acessar o RD Station CRM , selecione na oportunidade o registro do Lead que foi informado no Portal de Imóveis (clique no registro) 

5) Será aberto o formulário com os dados respectivos da oportunidade e será exibido no menu Produto e Serviçõs o produto que foi integrado através do painel do Portal de imóveis:

Modelo de Fluxos automatizados - Marketing \ CRM

## **Objetivo da Automação para CRM:**

O Fluxo automatizado para CRM, como o próprio nome já diz, é quando você deixa de realizar processos manuais e parametriza esta ação de forma automática. Ou seja, algo é executado sem a sua ajuda, sem você precisar executar. No RD Station existem diversas formas de automatizar e hoje vamos mostrar como ir do zero à automatização e disponibilizaremos o passo a passo de como montar 2 modelos processos automatizados aos quais recomendamos e que possibilitará realizar ações no sistema.

Observações:

É importante frisar, que se o usuário queira utilizar apenas a integração com o RD Station Marketing, a configuração já existente do Webhook poderá ser mantida. ***[(saiba mais:](https://tdn.totvs.com/pages/releaseview.action?pageId=687737814#RDSTATION-1513287362) [Configurando Webhook)](https://tdn.totvs.com/pages/releaseview.action?pageId=687737814#RDSTATION-1513287362)***  
Também existe a possibilidade de utilizar esta integração **sem a parametrização Webhook,** isto é possível se o usuário queira utiliza a automação de marketing para enviar uma oportunidade para o portal de imóveis. Para realizar esta parametrização sugerimos os exemplos abaixo para que possam ser desenvolvidos na empresa.

Veja o que estas automações irão realizar:  
  
**A primeira automação** será desenvolvida para incluir um Lead no fluxo de um funil assim que o mesmo for inserido no sistema;

**A Segunda automação** possibilitará enviar um Lead para o Portal de imóveis, assim que o usuário decidir que o mesmo já se trata de uma oportunidade;

Para que esta automação possa ser desenvolvida serão necessárias criações de campos personalizados nos módulos de Marketing e CRM, e estes campos irão conversar entre si através de atividades (gatilhos) oferecidos pelo RD Station que possibilitarão que as ações disparem gatilhos (executando processos) que são definidos pelo próprio usuário (ADM).

Abaixo iniciaremos o passo a passo para que possa ser desenvolvido estas automações.  
  
Veja a seguir:

1001 - Configurando Campos Personalizados no Marketing 

## **Configurando Campos Personalizados no RD Station Marketing:**

---

Para que este procedimento seja realizado é necessário acessar sua conta do RD Station Marketing: **<https://app.rdstation.com.br/dashboard>**

Após acessar o **RD Station Marketing** iremos criar os campos personalizados aos quais iremos associa-los para iniciar a preparação de nosso site para realizar as automações.

* No menu Converter (selecione campos personalizados).

* Será apresentada a opção para criar campo personalizado (selecione este botão);

* Observe que o campo personalizado que iremos incluir possui algumas definições que deverão ser seguidas.   
  **- O Tipo de campo** será *Campo de seleção - Caixa de seleção;*  
  **- O Enunciado do campo** servirá para apresentar o campo na tela, como prática geralmente mantemos o mesmo nome informado no tipo de campo;  
  **- Opções de campo:** Digite no primeiro campo a palavra SIM e no segundo campo a palavra NÃO, estas palavras irão compor este campo personalizado, para que o usário na tela ao visualizar este campo possa utilizar uma destas opções para que a ação seja executada. Ao final clique em salvar para que este campo seja incluído.
2 - Configurando Campos Personalizados no CRM:

## **Configurando Campos Personalizados no RD Station CRM:**

---

Para configurar um campo personalizado no **RD Station CRM** acesse sua conta: **<https://crm.rdstation.com/app#/settings>**  
Ao acessar a página serão apresentados diversos menus, dentre eles o menu: Configurações, ao selecionar este menu, observe que serão listadas para o usuário opções para que o mesmo possa selecionar.

* Selecione: Campos personalizados;

* Clique em Adicionar novo campo;

* Observe que nesta tela existe um botão que ao ser selecionada irão apresentar 3 opções: Oportunidade, Empresas\Clientes e Contatos.   
  Neste nosso exemplo iremos selecionar **oportunidade;** isto refere-se que ao selecionar a opção oportunidade (este campo que iremos inserir em nosso exemplo será apresentado ao acessar a guia de oportunidades.

* Após acessar a tela com as opções a serem selecionadas observe os campos que serão preenchidos conforme a imagem abaixo.  
  - Nome do campo personalizado: Refere-se ao campo que será apresentado na tela para o usuário, com esta informação o usuário irá determinar qual será a ação ou opção que irá selecionar. Neste nosso exemplo quando este campo for apresentado no formulário de oportunidade, o usuário irá optar pelas opções a serem escolhidas SIM ou NÃO *(estas opções irão executar o gatilho com a ação automatizada) **que veremos logo a seguir nos exemplos 1 e 2 dos tópicos 4 e 6 deste material;***  
  - Campo de seleção: Selecione a opção: Escolha múltipla, que possibilita o usuário selecionar SIM ou NÃO no formulário;  
  - Tipo: Informe as palavras SIM e NÃO para que estas opções fiquem disponíveis para seleção.  
  - Visível: Indica que este campo ficará visível no formulário oportunidade, podendo ser desabilitado a qualquer momento em que não esteja sendo mais utilizado.  
    
  Ao final clique em salvar.

* Ao retornar para a tela principal, observe que o campo personalizado já encontra-se disponibilizado na opção selecionada: Oportunidades.   
  Ainda nesta tela veja que será necessário marcar a opção: **VISÍVEL** , se esta opção não estiver marcada, a mesma deverá ser marcada (conforme a imagem abaixo).  
  Ao marcar esta opção será apresentada uma mensagem de confirmação ***(Clique em sim para prosseguir);***

Para facilitar a gestão de informações, clientes na versão 12.1.2606+ possuem uma tela exclusiva para a criação de campos personalizados diretamente no RD Station CRM, sem precisar sair do Portal.

**Como criar um novo campo pelo Portal:**

* Acesse o menu Integração > Campos personalizados.
* Clique no botão **Adicionar campo**.
* Preencha as informações:
  + **Entidade:** O sistema já preenche automaticamente como "Negociação".
  + **Campo:** Selecione a informação do Portal (ex: Empreendimento, Bloco, Unidade, Data da proposta) que alimentará o RD. Dica: Ao selecionar campos como "Empreendimento", o sistema carrega as opções ativas do seu banco de dados automaticamente.
  + **Label:** Digite o nome visual do campo para o corretor no RD.
  + **Tipo:** Defina se será Texto, Data, Seleção Única ou Múltipla.
  + Também poderá definir uma **ordem** para o campo personalizado e se depois de ser salvo, ao editar, se **p****ermitir adicionar nova opção**.
* Clique em **Criar**. O campo será gerado no RD Station CRM e no PI.

**Observação**: ao criar o campo personalizado diretamente pelo RD Station CRM ele será automaticamente integrado ao Portal de imóveis.

3 - Sincronização de Usuários e Corretores com o RD CRM (Versão 12.1.2606+)

## **Sincronização de Usuários e Corretores com o RD CRM (Versão 12.1.2606+):**

---

Para que o "Dono do Lead" seja consistente entre os sistemas, é fundamental que os corretores do Portal de Imóveis estejam vinculados aos seus perfis no RD Station CRM.

**Vinculação Automática no Cadastro:** Com a integração do CRM ativa, ao criar/ativar ou inativar um novo usuário no Portal, o sistema verifica automaticamente se aquele e-mail já existe no RD. 

* **Com sucesso:** O vínculo é feito, a mensagem "Vinculado ao RDStation CRM" aparece e um ícone da RD fica visível ao lado do nome do corretor na listagem.
* **Não encontrado:** O usuário é criado no Portal, porém nenhuma mensagem de vínculo é exibida.

**Sincronização em Lote (Para bases existentes):** Se você já possui corretores cadastrados e acabou de ligar a integração, não precisa editar um por um.

1. Acesse a tela de **Integração > Aplicativos**.
2. Na linha da integração CRM, clique no botão de ações (**...**) e depois em **Vincular corretores**.
3. O sistema sincronizará de uma só vez todos os usuários ativos do Portal que possuam correspondência no RD CRM, garantindo o alinhamento da base.
4 - Atualização Automática de Etapas e Fechamento de Venda com o RD CRM (Versão 12.1.2606+)

## **Atualização Automática de Etapas e Fechamento de Venda com o RD CRM (Versão 12.1.2606+):**

---

Durante todo o ciclo comercial, o Portal de Imóveis mantém o RD Station CRM atualizado em tempo real. A cada avanço no status da proposta no Portal (como Em Andamento, Aprovada ou Cancelada), o sistema sincroniza os dados com a negociação correspondente no CRM com base nos campos personalizados criados. Para saber como configurar Campos Personalizados clique em [Saiba Mais.](https://tdn.totvs.com/pages/viewpage.action?pageId=687737814#RDSTATION-854665619)

Nessas transições, os campos personalizados — como Empreendimento, Bloco, Unidade, Valor e a própria **Situação da Proposta** — são atualizados automaticamente, garantindo que o time de vendas tenha a visão exata do andamento do negócio sem precisar consultar o ERP.

**Fechamento Automático:** A etapa final dessa integração ocorre após a aprovação e o envio da proposta para o Backoffice. Quando a proposta atinge o status de **"Vendido"** no Portal de Imóveis, o sistema reflete essa conversão no CRM de duas formas: atualiza o campo personalizado de situação e altera o status nativo da negociação para ganho, aplicando a marcação de **VENDIDA**.

Essa sincronização de ponta a ponta garante que os relatórios de conversão e os indicadores das equipes de marketing e vendas permaneçam integralmente alinhados aos resultados de faturamento.

5- Combinação de campos no CRM e Marketing :

## **Combinação de campos do RD Station CRM com Marketing :**

---

Após criar os campos personalizados no CRM e no Marketing será necessário combinar (integrar) estes campos entre si. Em resumo: Ligar um ao outro.  
Para realizar esta configuração realize o seguinte processo:

* No **RD Station CRM** acesse sua conta: **<https://crm.rdstation.com/app#/settings> ;**
* Clique o menu: Configurações;
* Na lista de opções da página  selecione: RD Station Marketing;

* Nesta tela selecione a opção: Adicionar combinação de campo;

* Em seguida serão apresentados 2 campos, onde no primeiro campo deverá ser selecionado o campo personalizado que você criou no Marketing, e no segundo campo, será selecionado o que foi criado no CRM;
* Após selecioná-los, clique em Adicionar;

* Será apresentada a mensagem informando que as alterações foram aplicadas e na lista os campos serão apresentados;

6 - Incluindo Gatilhos de automação - Exemplo 1:

## **Gatilhos de automação - Exemplo 1 :**

---

Neste primeiro exemplo iremos criar uma automação de Fluxo que possibilitará o *Envio automático de um Lead para o CRM assim que o mesmo for incluído pelo usuário na base de Lead*;  
  
**Envio automático de um novo Lead para o CRM**

* Para que a Automação seja configurada acesse sua conta do RD Station Marketing: **<https://app.rdstation.com.br/dashboard>**  
  Ao acessar a página, clique o menu: Relacionar e selecione a opção Automação de Marketing, este menu possibilitará que o usuário possa ter aceso as atividades para inclusão de ações que podem ser realizadas de forma automatizadas no sistema.;

* Selecione a opção: Criar Fluxo;

* Informe um nome para este Fluxo de Automação, como exemplo: Entrada de Leads, em seguida clique em continuar;

* No painel apresentado a esquerda selecione as opções para que seja montada as instruções de acordo com as ações definidas:  
  - Todos Leads que (esta opção informa que na ação será utilizados todos os Leads inseridos no sistema);  
  - Foram marcados como oportunidade  
    
  *Ou seja, esta atividade que foi criada irá validar todos os Leads incluídos no sistema que possuem a opção Oportunidade Marcada*

* Em seguida clique na opção + destacada na tela;

* Observe que neste momento serão apresentadas outras ações para serem selecionadas, navegue nas ações e localize: Criar Oportunidade no CRM, em seguida marque esta ação e arraste a mesma na direção do símbolo + conforme a seta indicada na imagem;

* Após arrastar e soltar, observe que a ação ficará associada com a outra atividade já criada e outras opções para seleção serão apresentadas para serem preenchidas.  
  - Criar a oportunidade no funil: Selecione o Funil existente no site que receberá esta automação;  
  - Na etapa: Informe a etapa a qual esta automação será iniciada. Isto indicará a automação este lead ao ser inserido na base de Lead (onde no cadastro é informado este funil e esta etapa) neste momento este Lead será incluído automaticamente para o CRM.  
  - Atribuir para uma pessoa: Informar um usuário que receberá as oportunidades  
    
  Ao final clique em Salvar e Ativar.

* Serão apresentadas as opções de ativação, nesta tela não precisa realizar nenhuma ação, bastando clicar em: Ativar Fluxo;

* Com isto concluímos a inclusão desta automação que possibilita o envio automático de um novo Lead para o CRM;

Observações:

A utilização desta automação dispensa a necessidade da parametrização do Webhook.   
Para maiores informações referentes a este recurso acesse a página:  [Parâmetros > Webhook](https://tdn.totvs.com/pages/viewpage.action?pageId=687737814#RDSTATION-1513287362)

URL Webhook

**Veja como criar o Link que será utilizado na tela acima:**  
  
- URL: Nesta parte deverá ter uma atenção mais específica, observe que na primeira parte será informada o acesso ao Portal de Imóveis, em seguida para compor a URL informe o endereço: api/webhook/rdstation/ e para finalizar a chave que foi gerada no Portal de imóveis (nos parâmetros de Pessoas). Clique em “Salvar Webhook”  
Veja o exemplo detalhado:  
  
  
***Mais informações no link: [Configurações de URL](https://tdn.totvs.com/pages/viewpage.action?pageId=687737814#RDSTATION-1513287362)***

* Serão apresentadas as opções de ativação, nesta tela não precisa realizar nenhuma ação, bastando clicar em: **Ativar Fluxo;**

* Com isto concluímos a inclusão desta automação que possibilita o envio automático de um Lead para o Portal de imóveis;

7 - Na Prática: Enviando o Lead para o CRM

## **Enviando o Lead para o CRM utilizando automação de Marketing**

---

#### **Acesse sua conta do RD Station Marketing:** **<https://app.rdstation.com.br/dashboard>**

* No menu relacionar, selecione Base de Leads;

* Insira um novo Lead;

* Inclua os dados deste Lead, realizando o cadastro como de costume na rotina da empresa.   
  Ao final clique em Salvar. *(OBS: os dados utilizados nestes exemplos são fictícios).*

* Neste momento ao acessar o CRM, observe que o Registro deste Lead foi inserido automaticamente no Fluxo do CRM.  
  Com isto concluímos que esta automação realizou corretamente suas ações parametrizadas.

8 - Gatilhos de automação - Exemplo 2 :  

## **Gatilho de automação - Exemplo 2:**

### Neste segundo exemplo iremos criar uma automação de Fluxo que possibilitará o *Envio automático de um Lead para o Portal de imóveis assim que o mesmo for selecionado como uma oportunidade.*

* Para que a Automação seja configurada acesse sua conta do RD Station Marketing:**<https://app.rdstation.com.br/dashboard>**  
  Ao acessar a página, clique o menu: Relacionar e selecione a opção Automação de Marketing, este menu possibilitará o usuário possa ter aceso as atividades para inclusão de ações que podem ser realizadas de forma automatizadas no sistema.;

* Selecione a opção: Criar Fluxo;

* Informe um nome para este Fluxo de Automação, como exemplo: Envia Lead para o Portal de Imóveis, em seguida clique em continuar;

* No painel apresentado a esquerda selecione as opções para que seja montada as instruções de acordo com as ações definidas:  
  **- Todos Leads que:** (esta opção informa que na ação será utilizados todos os Leads inseridos no sistema);  
  **- Campo do Lead:**Campo ao qual a automação irá percorrer  
  **- Integração no Portal de Imóveis:***(refere-se ao nome do campo personalizado que foi configurado no Tópico 1 deste material).***- é igual a SIM:** Trata-se da condição do filtro que irá realizar a ação, ou seja, quando for selecionado SIM então o gatilho realizará uma determinada ação.
* Em seguida clique na opção + destacada na tela;

* Observe que neste momento serão apresentadas outras ações para serem selecionadas, navegue nas ações e localize: Enviar Leads para Integração, em seguida marque esta ação e arraste a mesma na direção do símbolo + conforme a seta indicada na imagem;

* Após arrastar esta atividade na tela, uma guia será apresentada na lateral para que seja informado o Link que possui as informações do Webhook que irá sincronizar este gatilho com o Portal de Imóveis. Para relembrar como realiza esta parametrização veja logo abaixo uma imagem dos parâmetros do Portal de imóveis onde é informada a chave ToKen e em seguida com esta chave é criada a URL para ser utilzada nesta parametrização;

URL Webhook

**Veja como criar o Link que será utilizado na tela acima:**  
  
- URL: Nesta parte deverá ter uma atenção mais específica, observe que na primeira parte será informada o acesso ao Portal de Imóveis, em seguida para compor a URL informe o endereço: api/webhook/rdstation/ e para finalizar a chave que foi gerada no Portal de imóveis (nos parâmetros de Pessoas). Clique em “Salvar Webhook”  
Veja o exemplo detalhado:  
  
  
***Mais informações no link: [Configurações de URL](https://tdn.totvs.com/pages/viewpage.action?pageId=687737814#RDSTATION-1513287362)***

* Serão apresentadas as opções de ativação, nesta tela não precisa realizar nenhuma ação, bastando clicar em: **Ativar Fluxo;**

* Com isto concluímos a inclusão desta automação que possibilita o envio automático de um Lead para o Portal de imóveis;

9 - Na prática: Envio automático de um Lead para o portal de imóveis quando é transformado em oportunidade 

**Na prática: Envio automático de um Lead para o portal de imóveis quando é transformado em oportunidade**

---

* No **RD Station CRM** acesse sua conta: **<https://crm.rdstation.com/app#/settings> ;**
* Clique o menu: Oportunidades;

* Selecione o Lead que será enviado para o Portal de Imóveis;

* Arraste este fluxo e inclua o mesmo como um interesse;

* Ao selecionar o Lead clique no nome do mesmo para que as opções deste Lead sejam apresentadas;

* Neste momento observe na guia aberta, as informações presentes formulário dos Dados da Oportunidade com a opção do gatilho que criamos.  
  Veja que a opção oferece duas ações sendo que ao selecionar **SIM este Lead será marcado automaticamente como uma oportunidade** (será apresentada no rodapé uma informação que demonstra que o Campo personalizado foi atualizado), neste instante o Lead será enviado para o portal de imóveis. Conforme evidenciado na figura abaixo.

* Registro enviado para o portal de imóveis;

***OBS: importante lembrar ao usuário que o registro poderá demorar alguns minutos para atualização entre as integrações caso o site esteja passando por alguma atualização***.
