---
content_hash: bf597bc471ab5fcc1e93bb479403ee0b219c71adac71b4982af18e18976110f9
fetched_at: '2026-06-29T00:09:58.297514+00:00'
page_id: '452415182'
product: rm
source: tdn-rm
title: 04- Implantação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452415182
version: 8
---

Figura 1 - Processo de implantação

Na figura 1 podemos ver o processo de implantação do aplicativo Retenção de Alunos, que está detalhado abaixo:

### **1) Instalação e configuração do Carol Conector (2C)**

Inicialmente é necessário instalar e configurar o Carol Conector (2C) para acessar a fonte de dados que será utilizada. Embora o 2C permita que outros tipos de fontes de dados sejam utilizados, o Retenção de alunos já está preparado para se integrar, de forma nativa, ao ERP de gestão educacional TOTVS. Clique aqui e saiba mais.

### 2) Envio dos dados para a CAROL (2C)

Nesta etapa as informações das fontes de dados utilizadas serão enviadas para CAROL, especificamente para as Staging Tables. Outro detalhe importante é que este é um processo contínuo, ou seja, após a carga inicial, o 2C deverá continuar em execução para que o Retenção de Alunos continue recebendo as atualizações dos alunos da instituição.

### 3) Processo de qualidade dos dados

Neste ponto são executadas regras para se extrair das Staging Tables as informações realmente úteis para a aplicação. Estas regras já foram definidas previamente na plataforma CAROL, quando o Retenção de Alunos foi desenvolvido, e as informações tratadas serão copiadas para os Data Models.

### 4) Parametrização do app

Nesta etapa, devem ser configurados os parâmetros da aplicação conforme as especificidades de cada instituição de ensino. Esta parametrização é importante pois constitui o meio pelo qual a solução entende o contexto em que a instituição se insere e gera os resultados conforme a realidade do cliente. [Clique aqui e saiba mais](http://tdn.totvs.com.br/pages/viewpage.action?pageId=330836353).

### 5) Geração do modelo preditivo

Utiliza inteligência artificial para identificar padrões de comportamento dos estudantes a partir da análise das informações existentes nos Data Models. [Clique aqui e saiba mais](http://tdn.totvs.com/pages/viewpage.action?pageId=329029342).

### 6) Geração da lista e perfis de prováveis evasores

Utiliza o modelo preditivo gerado para recomendar uma lista de estudantes que potencialmente possam evadir, agrupando estes possíveis evasores em grupos com características semelhantes. [Clique aqui e saiba mais](http://tdn.totvs.com/pages/viewpage.action?pageId=329029342).

### 7) Ações de retenção

Finalmente, a instituição poderá utilizar o Retenção de Alunos para avaliar o cenário dos potenciais alunos evasores e planejar as ações de retenção.
