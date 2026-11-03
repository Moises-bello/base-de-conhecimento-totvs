---
content_hash: 89603529aafc343fda7472552dc897184275a3f40977f6bc88847bd0cf4b75c4
fetched_at: '2026-06-29T00:12:09.182975+00:00'
page_id: '941245873'
product: rm
source: tdn-rm
title: Utilitários - Portal/App - Gestão - MultiPortal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=941245873
version: 11
---

## **Visão Geral**

Através dessa nova funcionalidade de ***MultiPortal***, as incorporadoras poderão trabalhar com mais de um Portal do Cliente, possibilitando separar portais por diferentes segmentos de atuação da empresa ou até por diferentes coligadas dentro da sua estrutura.

Dessa forma, será possível direcionar seus clientes à portais que tratam especificamente seu contexto, Como por exemplo:

* Investimentos de Alto Luxo: [luxo.exemplo.com.br](http://luxo.exemplo.com.br)
* Minha Casa Minha Vida: [mcmv.exemplo.com.br](http://mcmv.exemplo.com.br)
* Outros investimentos: [investimentos.exemplo.com.br](http://investimentos.exemplo.com.br)

Alerta

Atualmente, os contextos dos portais são definidos por coligada. Não é possível realizar a configuração por empreendimento, ou seja, apenas as coligadas podem ser selecionadas para exibição em cada portal.

## **Ativação e Perfil de Acesso**

Para habilitar o acesso a MultiPortais, marque a opção ***Usar MultiPortal***, disponível, na opção *Parâmetro de Aplicativo* em ***[Totvs Incorporação - Parâmetros - Portal do Cliente](https://tdn.totvs.com/pages/viewpage.action?pageId=435105047).***

Para ter acesso a este menu é preciso aplicar a permissão de segurança de acesso na opção do Perfil do Usuário:

**Nome da permissão:** MultiPortal

**Localização da permissão:** Gestão de Imóveis > Utilitários > Portal / App > Gestão > MultiPortal

## **Configurações Necessárias**

Para utilizar o **MultiPortal**, será necessário realizar dois tipos de configuração:

* **Externa ao RM**: Responsáveis pela definição e publicação dos endereços dos portais.
* **Interna ao RM**: Realizadas dentro do próprio sistema, para associar e parametrizar contexto e personalização dos portais previamente configurados.

Configsexternal\_configConfigurações externas

## **Configuração arquivo hosts**

No arquivos hosts, localizado em "C:\Windows\System32\drivers\etc\hosts" deve ser incluído no IP publico correto do servidor os endereços desejados de cada portal,

**Associações de Site no IIS e o MultiPortal**

Na maioria dos cenários, **não é necessário configurar associações específicas no IIS**. Basta:

* Deixar apenas **uma associação** no site, com **Nome do Host vazio** e **porta 80**.
* Configurar os domínios desejados no **arquivo hosts** (ou DNS corporativo), apontando para o IP do servidor.

Com isso, o portal funcionará normalmente sem necessidade de ajustes adicionais no IIS.

### Quando configurar portas no IIS:

Caso o cliente deseje utilizar uma **porta diferente da padrão (80/443)**, será necessário configurar essa porta nas **associações** do IIS.

## Exemplo:

* Se o portal for publicado em `http://pdc-x.com.br:8081`, nas associações do IIS deve estar configurados com a porta **8081**.

### Cenários específicos

Em situações mais complexas (ex.: múltiplos portais em caminhos físicos diferentes ou necessidade de domínios distintos para projetos separados), será necessário **analisar e configurar associações adicionais no IIS**, definindo nomes de host e portas de forma explícita para evitar conflitos.

internal\_configConfigurações no RM

## **Configuração MultiPortal RM**

Ao inserir um novo registro serão exibidos os seguintes campos:

Aba **Identificação**: Nesta aba serão parametrizados os dados para o acesso a cada PDC individualmente.

* + **Id do Portal:** Identifica cada um dos PDCs. Tem o seu preenchido automático pelo sistema. e é um campo não editável;
  + **Usuário Alteração:** Informa o nome do usuário que fez a última alteração na parametrização deste PDC. Tem o seu preenchido automático pelo sistema e é um campo não editável;
  + **Data Alteração:**Informa a data da última alteração na parametrização deste PDC. Assim como os dois campos acima, também tem o seu preenchido automático pelo sistema e é um campo não editável;
  + **Domínio Base do Portal:** É o endereço do domínio que servirá de base para acesso à este PDC. É importante é que o o domínio informado esteja idêntico ao domínio configurado no IIS. Nesse campo será preenchido geralmente da mesma forma de como era preenchido no FrameHTML do parâmetros Gerais
    - Regras de preenchimento:
      1. Schema obrigatório
         1. Sempre utilize `http://` ou `https://`, conforme configurado no ambiente/IIS.
         2. Exemplo: <https://pdc-x.com.br>
      2. Porta
         1. Se for **porta padrão** (80 para `http` ou 443 para `https`), **não precisa ser informada**.
         2. Se for **porta customizada**, deve ser incluída.
         3. Exemplos:
            1. Porta padrão → `https://pdc-x.com.br`
            2. `Porta customizada (8081) → https://pdc-x.com.br:8081`
      3. Sufixo `/Caminhovirtual (ex.:/FrameHTML)`
         1. Em ambientes **TCloud**, normalmente é necessário adicionar o sufixo `/FrameHTML` após a porta.
         2. Em ambientes **não TCloud**, geralmente não é necessário, mas talvez seja necessário uma analise pra saber se irá precisar ou não do sufixo, caso seja configurada um caminho virtual no IIS.
         3. Exemplos:
            1. Ambiente TCloud → `https://pdc-x.com.br/FrameHTML`
            2. Ambiente TCloud com porta customizada → `https://pdc-x.com.br:8081/FrameHTML`
            3. Ambiente não TCloud → `https://pdc-x.com.br`
  + **Título:** Informe o Título do PDC que será exibido ao usuário, quando ele realizar o acesso no endereço parametrizado.
  + **Descrição:** Informe a descrição para facilitar a identificação deste ambiente do PDC;
  + **Perfil Cor:** Selecione o Perfil de Cor que será o padrão para este PDC, de forma a diferenciá-lo visualmente ao usuário, dos demais PDCs. O perfil de cor é cadastrado no menu [*Personalizar*](https://tdn.totvs.com/display/LRM/Portal+do+Cliente+-+PDC+-+Personalizar) diretamente no PDC.

Após salvar este cadastro é preciso acessar o menu de anexo **Coligadas**.

* Anexo **Coligadas**: Neste cadastro serão associadas as coligadas que estarão disponíveis para acesso em cada PDC. Ao adicionar uma nova coligada, são exibidos os seguintes campos:
  + **Id do Portal:** Identifica cada um dos PDCs. Tem o seu preenchido automático pelo sistema. e é um campo não editável;
  + **Usuário Alteração:** Informa o nome do usuário que fez a última alteração na parametrização deste PDC. Tem o seu preenchido automático pelo sistema e é um campo não editável;
  + **Data Alteração:**Informa a data da última alteração na parametrização deste PDC. Assim como os dois campos acima, também tem o seu preenchido automático pelo sistema e é um campo não editável;
  + **Coligada:** Associe a coligada cujos contratos de vendas estarão disponíveis neste PDC. Caso tenha mais de uma coligada associada, é preciso inserir um novo registro de anexo para a outra coligada.
