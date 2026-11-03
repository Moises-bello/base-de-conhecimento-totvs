---
content_hash: 423cd55e9944d40c746f1d5e438eb149d5ee5b289e917f94cb553f4ba33d58f8
fetched_at: '2026-06-29T00:11:59.947700+00:00'
page_id: '877860490'
product: rm
source: tdn-rm
title: Recursos - Atividade C#
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=877860490
version: 2
---

A função **Recursos** em uma **Atividade de C#** no TOTVS Automação de Testesgerencia os objetos e serviços que a atividade pode **necessitar** (consumir) ou **oferecer** (disponibilizar) para outras atividades no fluxo de testes. Esses recursos facilitam a integração e reutilização de componentes, garantindo que dados e ferramentas possam ser compartilhados de forma eficiente entre diferentes atividades.

#### 1. Necessita (Recursos Consumidos)

* **Recursos consumidos** são aqueles que a atividade precisa para ser executada corretamente. Esses recursos podem ser fornecidos por outras atividades ou configurados no início do fluxo de teste.

  Exemplos de recursos que uma Atividade de C# pode consumir:

  + **Conexões de banco de dados**: Para realizar consultas ou operações de leitura/escrita.
  + **Instâncias de WebDriver**: Para automação de interações com navegadores usando Selenium.
  + **Parâmetros de execução**: Como credenciais de usuário, URLs, ou dados de entrada que a atividade precisará processar.

  **Exemplo:**

  `var dbConnection = context.Resources.OfType<IRdbConnectionResource>().First().Value;`

#### 2. Oferece (Recursos Disponibilizados)

* **Recursos oferecidos** são aqueles que a atividade gera ou disponibiliza para que outras atividades utilizem posteriormente no fluxo de teste. Eles podem incluir objetos instanciados durante a execução da atividade ou dados processados que serão necessários em atividades subsequentes.

  Exemplos de recursos que uma Atividade de C# pode oferecer:

  + **WebDriver**: Configurado e pronto para ser reutilizado em outras atividades que necessitem de automação web.
  + **Resultados de processamento**: Informações geradas pela atividade, como status de testes ou dados extraídos de uma página web.

  **Exemplo:**
* `context.Resources.Add(_seleniumManager, "Selenium Manager");`

#### 3. Recursos de Atividade no TOTVS Automação de Testes

* As **Atividades C#** na ferramenta podem consumir e oferecer recursos, garantindo que o fluxo de teste seja eficiente e organizado. Isso permite que uma atividade forneça dados ou instâncias de objetos para outra, mantendo a continuidade e a reutilização dos mesmos.

  **Exemplo de uso em contexto**:

  1. Uma atividade cria uma instância de **WebDriver** e adiciona ao contexto.
  2. Atividades subsequentes reutilizam o **WebDriver** sem a necessidade de nova instanciação, otimizando o processo.
