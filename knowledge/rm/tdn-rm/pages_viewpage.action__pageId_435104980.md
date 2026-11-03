---
content_hash: 0672ed2184f42002597cb6632e841e38f89e1211814e1209f514bd220863a72e
fetched_at: '2026-06-29T00:09:47.195409+00:00'
page_id: '435104980'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Aluguel - Contrato de Locação - Reajustes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435104980
version: 19
---

### Definições:

---

O reajuste tem a função de permitir ao cliente realizar e agendar o cálculo de reajuste sobre os contratos de aluguel de uma, algumas ou várias coligadas ao mesmo tempo, que o usuário tenha permissão de acesso. É necessário um contrato de locação  efetivado e que a data de reajuste esteja dentro da vigência atual do contrato.

Nas telas de "Aplicar Reajuste", "Desfazer Reajuste" e "Agendar Reajuste" de contrato de aluguel será criado um filtro de coligada para permitir o usuário filtrar apenas uma coligada ou todas as coligadas.

Caso o Desconto do Contrato de Locação esteja com a opção "Aplicar Reajuste" marcado, ele terá o seu valor reajustado conforme a variação calculado pelo Reajuste. Dessa forma o Valor Final do Contrato será alterado.

Ao Aplicar o Reajuste, é atualizado o histórico de Valores do Contrato de Locação, que se encontra na tabela "XALGCONTRATOLOCHISTVALOR". No caso do Contrato possuir  Desconto por M², no histórico é registrado o Tipo de Desconto como "Valor Final do Contrato" e o Valor do Desconto é obtido através da seguinte fórmula: Valor Desconto por m² \* Área Locada.

É possível realizar reajustes nos: Contratos de Locação, Fundo promocional e condomínio.

### Reajustes em fundo promocional:

---

Neste iremos entender como realizar reajustes em fundo promocioal (utilizando um índice diferente do que está informado no contrato de locação - Dados do reajuste.)

A partir desta parametrização o sistema possibilitará parametrizar os dados do reajuste (informando um índice) no contrato e também na guia "outros reajustes. Esta configuração possibilitará o usuário selecionar (no momento do Reajuste) qual a cotação que será utilizada para cálculo do reajuste.

No exemplo abaixo, observe que possuímos 2 moedas parametrizadas. A moeda IGPM (foi informada para ser utilizada para reajustes do contrato) e a IGPM1 (informada em outros valores), onde a mesma (neste exemplo abiaxo) será **utilizada para reajustes de fundo promocional.**

**OBS: A opção de fundo promocional (existente em outros valores) estará disponível para utilização a partiir da versão 12.1.2306 *(o que irá permitirá qu a utilização de um outro indice realize um reajuste*** ***para o fundo promocional diferente do índice informado no contrato).***

O resultado poderá ser visualizao ao acessar o histórico do fundo promocional observando que o índice utilizado para este reajuste foi o IGPM1 (que utilizamos em nosso teste)

### Reajustes em Condomínio:

---

O Reajuste de Condomínio possibilitará (calcular um índice diferente do que está informado no contrato de locação - Dados do reajuste.)

A partir desta parametrização o sistema possibilitará parametrizar os dados do reajuste (informando um índice) no contrato e também na guia "outros reajustes. Esta configuração possibilitará o usuário selecionar (no momento do Reajuste) qual a cotação que será utilizada para cálculo do reajuste.

### Pré requisitos:

---

No cadastro do empreendimento, será necessário associar uma Cobrança por Orçamento:

Edite o empreendimento > Selecione: Associação de Cobrança por empreendimento.

Na guia Cobrança Fixa por Subunidade será necessário realizar a inclusão de uma cobrança com um valor informado para que possa ser reajustado.

Após informar este valor clique em salvar.  
Lembrando que este valor será o que irá ser reajustado de acordo com as parametrizações informados no menu Dados de Reajustes do contrato de Locação.

### Parametrizando os dados do Reajuste para condomínio:

---

Neste processo será necessário definir no contrato os dados de reajuste.

No exemplo abaixo, observe que possuímos 2 moedas parametrizadas. A moeda IGPM2 (foi informada para ser utilizada para reajustes do contrato) e a IGPM (informada em outros valores), onde a mesma será utilizada (neste exemplo abaixo) para **reajustes de condominio.**

Este processo permite que o gestor do contrato ao executaro reajuste permita que o valor do orçamento fixo também possa ser reajustado.

Em seguida será necessário realizar o processo de reajuste: Processos > Aplicar Reajuste

Na tela apresentada o usuário poderá aplicar o reajuste selecionando a entidade que será reajustada, neste caso será a entidade referente a Condomínio.

Processo de reajuste concluído:

Para visualizarmos a aplicação deste processo nos valores da cobrança por orçamento, acesse novamente o cadastro do empreendimento, e em seguida realize a edição do empreendimento ao qual utilizamos para o contrato de locação. Ao acessar clique no menu: Associação de Cobrança por Orçamento > Na tela de identificação já será possível visualizar o valor reajustado, o mesmo anteriormente possuía o valor de R$ 2.500,00

Ao selecionar a Guia: Histórico de alteração de valor, observe que é apresentada a memória de cálculo com os valores de reajustes bem detalhados.

### Desfazer Reajuste:

---

Ao selecionar a opção de desfazer o reajuste, serão exibidos os reajustes vigentes.   
Basta selecionar o registro que será desfeito informando o motivo referente a necessidade deste processo, e em seguida clique em executar.

Observações complentares

* Este reajuste não irá alterar os lançamentos de fechamento de condomínio que já foram gerados.
* O menu "Agendar Reajuste" somente ficará habilitado em ambientes 3 camadas.
