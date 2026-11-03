---
content_hash: b20a8e584025ca0857ac5d5fd967318b15eb2a7c82d59b09452d744564fa63df
fetched_at: '2026-06-29T00:05:47.980267+00:00'
page_id: '1020394255'
product: rm
source: tdn-rm
title: Assistente de Configuração - Reforma Tributária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1020394255
version: 19
---

true

# **01. Visão Geral**

O **Assistente de Configuração da Reforma Tributária** foi desenvolvido para orientar o usuário, de forma simples e estruturada, na adaptação do sistema às exigências da Reforma Tributária. Seu objetivo é garantir que as etapas essenciais sejam realizadas corretamente, reduzindo falhas de parametrização e assegurando que a empresa esteja preparada para operar dentro das novas regras tributárias. O assistente ficará disponível nos seguintes módulos:

* Gestão Fiscal → Utilitários → Assistente de Configuração.
* Gestão de compras, estoque e faturamento → Utilitários → Assistente de Configuração.

Por meio de uma sequência guiada de telas, o assistente automatiza rotinas fundamentais, como inclusão inicial dos Tributos, definição de Vigências de Alíquotas, cadastro de Regras Tributárias, importação da tabela CST e cClassTrib, associação dos novos Tributos com os Tipos de Movimento, validações de consistência, sendo essas as configurações iniciais mínimas necessárias para a adaptação à Reforma Tributária. Cada etapa foi projetada para ser intuitiva, oferecendo orientações claras e verificações automáticas que evitam divergências e omissões.

Ao final do processo, o usuário terá todas as bases estruturais da Reforma Tributária devidamente configuradas, permitindo que o sistema calcule os novos tributos com precisão, garantindo segurança, conformidade e qualidade das informações fiscais.

Disponíveis à partir dos patches

* 12.1.2502.250
* 12.1.2506.205
* 12.1.2510.135

---

# **02.** **Demonstração das funcionalidades**

Clique aqui para ver ...

# **03.** **Funcionalidades**

60%VídeosleftfadePágina InicialPágina Inicial / Inserção de TributosPágina Inicial

## Tela – Página Inicial e Inserção de Tributos (Assistente de Configuração – Reforma Tributária)

Esta tela é a etapa inicial do **Assistente de Configuração da Reforma Tributária** e tem como objetivo verificar automaticamente se a base atende aos pré-requisitos mínimos para a criação dos tributos IBS e CBS. Ela funciona como um *checkpoint* antes do início da instalação guiada, garantindo que o ambiente esteja apto a prosseguir sem erros.

Visão da primeira tela...

### **1. Verificação de Pré-Requisitos**

Na parte superior, o sistema apresenta uma lista de validações essenciais, indicando com ícones se cada item está ou não conforme. Entre os pré-requisitos verificados estão:

* Ausência de um dos Tributos IBS e CBS considerando um tributo para cada abrangência: Federal, Estadual, Municipal e Estadual/Municipal.
* Ausência de Vigências configuradas para IBS e CBS (2025–2026).
* Inexistência de Regras Tributárias para os novos tributos.
* Importação pendente das tabelas CST e cClassTrib.
* Falta de vínculo dos novos tributos nos Tipos de Movimento.

Essas validações são atualizadas a medida em que as etapas são avançadas.

### **2. Bloco de Informações Importantes**

A seção **Configuração dos Requisitos Iniciais** traz instruções e avisos ao usuário, incluindo:

* Um alerta destacando que as novas regras entrarão em vigor em breve.
* A explicação de que estes requisitos iniciais são fundamentais para garantir o funcionamento correto do módulo fiscal.
* Uma visão geral do processo, informando que a configuração será feita em **5 passos guiados**, com mínimo esforço do usuário.

### **3. Benefícios do Fluxo**

O texto apresenta o que o assistente garante:

* Aderência às definições legais da Reforma Tributária;
* Redução de riscos de rejeição de documentos fiscais;
* Configuração padronizada e auditável.

Ao final dessa etapa, o usuário tem clareza de que o sistema automatizará boa parte da configuração necessária.

### **4. Ação Disponível**

No rodapé da tela, caso os tributos IBS e CBS não estejam cadastrados, o assistente informa que, ao avançar, o sistema fará a **criação automática dos tributos CBS, IBS (Base), IBS\_MUN e IBS\_UF**.  
O botão **Inserir Tributos** inicia efetivamente o processo automático de criação.  
  
Atenção! Caso o usuário não possua permissão para inserção de Tributos, é apresentado uma mensagem sinalizando que ele não poderá prosseguir, essa permissão é necessária nos 3 primeiros passos.

Configuração de Vigência de AlíquotasConfiguração de Vigência de AlíquotasConfiguração de Vigência de Alíquotas

## Tela – Configuração de Vigência de Alíquotas (Assistente de Configuração – Reforma Tributária)

Esta etapa do assistente é responsável por definir o **período de Vigência das Alíquotas dos novos tributos (CBS e IBS)** conforme previsto na legislação da Reforma Tributária. Ela só é exibida após a verificação inicial de pré-requisitos, garantindo que a base esteja preparada para receber as novas parametrizações.

Visão da tela de vigência de Alíquotas...

### **1. Informações de Vigência**

A tela exibe o período padrão determinado pela legislação:

* **Data Início:** 01/01/2025
* **Data Fim:** 31/12/2026

Essas datas correspondem ao intervalo inicial obrigatório de aplicação das novas alíquotas durante a fase de transição.

Caso não exista vigência cadastrada na base, o assistente realizará o cadastro automaticamente utilizando essas datas.

### **2. Seleção dos Tributos**

As Vigências devem ser criadas para os seguintes tributos:

* **CBS – Contribuição sobre Bens e Serviços**
* **IBS\_UF – Imposto sobre Bens e Serviços (Estadual)**

Caso os tributos tenham sido criados pelo próprio Assistente, no passo inicial, ou exista somente um tributo de cada tipo, eles serão automaticamente selecionados para o usuário. Caso contrário o usuário deve escolher o tributo correspondente para a aplicação.

### **3. Mensagens Informativas**

Acima do painel principal, o assistente destaca:

* Que a vigência de alíquotas ainda não existe na base.
* Que, caso o usuário prossiga, as vigências serão criadas automaticamente com base na legislação.

Essas mensagens orientam o usuário e evitam erros de duplicidade.

### **4. Ação Disponível**

No canto inferior direito, o botão **"Inserir Vigências"** inicia o processo automático de:

* Criação do período de vigência
* Associação dos tributos CBS e IBS Estadual ao período informado
* Preparação da base para as próximas etapas do assistente
Configuração de Regras TributáriasConfiguração de Regras TributáriasConfiguração de Regras Tributárias

## Tela – Configuração de Regras Tributárias (Assistente de Configuração – Reforma Tributária)

Esta tela corresponde à etapa em que o sistema orienta o usuário na criação e associação das **Regras Tributárias** para os novos tributos da Reforma Tributária (CBS, IBS Estadual e IBS Municipal). Ela aparece após a definição de vigências e demais pré-requisitos.

Visão da tela de Regras Tributárias...

### **1. Painel de Tributos**

Do lado esquerdo, há a lista dos tributos envolvidos:

* **CBS – Contribuição sobre Bens e Serviços**
* **IBS\_UF – Imposto sobre Bens e Serviços (Estadual)**
* **IBS\_MUN – Imposto sobre Bens e Serviços (Municipal)**

Caso os tributos tenham sido criados pelo próprio Assistente, no passo inicial, ou exista somente um tributo de cada tipo, eles serão automaticamente selecionados para o usuário. Caso contrário o usuário deve escolher o tributo correspondente para a aplicação.

### **2. Painel de Regras a serem Associadas**

No lado direito, é apresentada uma lista com algumas de Regras Tributárias de operações mais comuns, contendo:

* **Checkbox** para seleção
* **CST** (Código de Situação Tributária)
* **CClassTrib** (Classificação Tributária)
* **Descrição** da operação

O usuário pode selecionar múltiplas regras, conforme a necessidade da empresa. Caso sejam necessárias outras regras, de acordo com a natureza da empresa, podem ser criadas posteriormente no cadastro de Regras Tributárias.

### **3. Ação Disponível**

O botão **“Associar Regras”** finaliza a etapa, gerando automaticamente:

* Criação e associação das regras aos tributos CBS, IBS\_MUN e IBS\_UF
Importação da tabela CST e cClassTribImportação da tabela CST e cClassTribImportação da tabela CST e cClassTrib10

## Tela – Importação da tabela CST e cClassTrib (Assistente de Configuração – Reforma Tributária)

Esta tela corresponde à etapa em que o sistema executa o processo que acessa a API do governo responsável por prover a lista de CST/Classificações Tributárias.

Visão da Tela de Importação CST/Classificações Tributárias

Para saber mais sobre esse processo [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=1011567535).

Essa etapa é opcional, caso o usuário opte por acessar a processo em outro momento, é habilitado um botão Avançar que salta essa etapa.

Associação de Tipos de MovimentoAssociação de Tipos de MovimentoAssociação de Tipos de Movimento10

## Tela – Associação de Tipos de Movimento (Assistente de Configuração – Reforma Tributária)

Esta etapa do assistente trata do vínculo entre os novos tributos da Reforma Tributária (CBS, IBS Estadual, IBS Municipal e IBS Base) e os **Tipos de Movimento** utilizados pela operação da empresa. É uma das etapas essenciais para garantir que os novos tributos sejam aplicados corretamente nas movimentações fiscais e operacionais. 

Visão da Tela de Associação de Tipos de Movimentos

### **1. Objetivo da tela**

Nesta etapa, o usuário deve selecionar **quais Tipos de Movimento** passarão a utilizar os novos tributos (CBS e IBS).

A tela exibe todos os Tipos de Movimento que atualmente possuem os tributos ICMS, IPI, PIS, COFINS ou ISS e permite que o usuário escolha para quais deles o sistema deve incluir automaticamente os tributos da Reforma Tributária.

### **2. Seleção de Tributos**

À esquerda, o usuário encontra a lista dos tributos configurados anteriormente:

* **CBS – Contribuição sobre Bens e Serviços**
* **IBS\_UF – Imposto sobre Bens e Serviços (Estadual)**
* **IBS\_MUN – Imposto sobre Bens e Serviços (Municipal)**
* **IBS – Base de IBS (cálculo genérico)**

Caso os tributos tenham sido criados pelo próprio Assistente, no passo inicial, ou exista somente um tributo de cada tipo, eles serão automaticamente selecionados para o usuário. Caso contrário o usuário deve escolher o tributo correspondente para a aplicação.

Há também um campo para informar a **Fórmula de Base de Cálculo**, necessária para o correto cálculo do tributo na operação.

### **3. Lista de Tipos de Movimento**

No painel à direita, a tabela exibe todos os Tipos de Movimento que já possuem vínculo com tributos antigos.

Cada linha apresenta:

* **Checkbox** — marcação dos movimentos que receberão o novo tributo
* **Código do Tipo de Movimento**
* **Descrição**

O usuário pode selecionar quantos Tipos de Movimentos forem necessários para associar aos tributos e fórmula escolhida.

### **4. Funções Disponíveis**

### **Associar Tributos:**

Insere os Tributos selecionados na lista de Tributos do Item dos Tipos de Movimento marcados, incluindo:

* Cadastro da linha de tributo no Item do Tipo de Movimento
* Aplicação da Fórmula de Base de Cálculo
* Configurações necessárias para CBS e IBS

**Informações Importantes:**O processo insere a Fórmula informada em todos os Tipos de Movimento selecionados. Caso seja necessário associar fórmulas distintas, o processo pode ser repetido quantas vezes forem necessárias.  
Ao associar um tipo de movimento ele deixa de ser exibido no grid.

### **Avançar:**

Permite prosseguir para a próxima etapa finalizando ou não as associações.  
  
**5. Restrição de acesso****Atenção!** Apenas usuários que possuem permissão para inserir movimentos estão autorizados a realizar essa operação.

---
