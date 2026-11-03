---
content_hash: 2c2c2b43ef8f1227aa8f86b185eb535d41347bb908070f209cfc6f9b4f4668ef
fetched_at: '2026-06-29T00:11:38.221716+00:00'
page_id: '782303914'
product: rm
source: tdn-rm
title: Middleware - Relatório de Conferência de IRRF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=782303914
version: 80
---

false

**A partir das Versões:**

# Visão Geral do Programa

Esta funcionalidade tem como objetivo principal auxiliar na identificação de eventuais divergências entre os valores e bases de IRRF presentes no envelope de pagamento e os valores e bases reportados pelo RET.

Os dados apresentados são o resultado de uma análise comparativa entre os valores de IRRF enviados do RH ao governo por meio dos eventos S-1200, S-2299 e S-2399, e os valores que o Governo retorna por meio do evento S-5002.

O relatório é gerado não apenas quando há a retenção de IRRF, mas também quando há apenas a presença da base de cálculo do IRRF. Isso permite que o usuário não apenas verifique o valor do desconto, mas também as bases de cálculo envolvidas.

### Parametrização

Para utilização do Relatório de Conferência de IRRF, é necessário informar o servidor e porta que serão utilizados para execução desses serviços.

Acesse o menu Configurações | Parametrizador | eSocial | Configurações Gerais | Integração com Middleware | Outros parâmetros:

**Servidor/Porta API**: Servidor e porta onde o serviço de API"s RM está sendo executado. (**APiPort** do Host RM. No caso onde a ApiPort não foi discriminada nas configurações do Host, utilizar a HttpPort).   
**Servidor/Porta APP:** Servidor e porta onde o aplicativo THF está sendo executado. (Caso o servidor seja o Host RM, informar a **HttpPort**).

Para maiores informações sobre a configuração da **HttpPort** e **ApiPort**, acesse: [O que é e como configurar a HttpPort e ApiPort](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044519633-RM-Integra%C3%A7%C3%B5es-O-que-%C3%A9-e-como-configurar-a-HttpPort-e-ApiPort-).

**OBSERVAÇÃO: Se estiver executando o RM.Host.exe o mesmo deve ser executado com administrador.**

### Menu

Acesse o menu eSocial | Conferência INSS/FGTS/IRRF 

### Filtros

Clicando em "Relatório de Conferência de IRRF" será exibida a seguinte tela:

Preencha os campos abaixo, para aplicação do filtro: 

| Campo | Obrigatoriedade | Descrição |
| --- | --- | --- |
| **Período** | Obrigatório | Ano/Mês no formato AAAA/MM, para ser considerado no processamento das informações do painel. Competência da Folha de Pagamento que foi integrada com o governo. |
| **CPF** | Opcional | CPF do colaborador o qual se deseja buscar os valores de IRRF. |
| **Somente Divergências** | Opcional | Parâmetro que permite listar somente os casos que apresentaram alguma divergência de valores entre as colunas RH x Governo, ou listar todos os colaboradores que possuam valor de IRRF em sua remuneração, independente de divergência ou não.  Opções:   * **Sim**= lista somente colaboradores com divergência de valores nas colunas de valor. * **Não**= lista informações de todos os colaboradores que possuam valor de IRRF em sua remuneração. |
| **Somente Avisos** | Opcional | Parâmetro que permite listar somente os casos que apresentaram algum aviso devido diferença de valores entre os tipos de IR possíveis, seja retenção, base ou dedução  Opções:   * **Sim**= lista somente colaboradores com alerta nos tipos de IR. * **Não**= lista informações de todos os colaboradores que possuam valor de IRRF ou Base de IR em sua remuneração. |

IMPORTANTE

O painel conta com filtro adicional que pode ser encontrado clicando no botão "Busca Avançada". Os filtros podem ser aplicados em ambas as telas (Principal e Busca Avançada). Neste filtro é possível adicionar a condição de categoria e quantos funcionários devem ser retornados por página.

Lista de campos apresentados na tela de Busca Avançada:

| Campo | Obrigatoriedade | Descrição |
| --- | --- | --- |
| **Período** | Obrigatório | Ano/Mês no formato AAAA/MM, ou apenas Ano no formato AAAA, para ser considerado no processamento das informações do painel. Competência da Folha de Pagamento que foi enviado ao RET. |
| **Somente Divergências** | Opcional | Parâmetro que permite listar somente os casos que apresentaram alguma divergência de valores entre as colunas **Valor de Retenção RH**x**Valor de Retenção Governo**, ou listar todos os colaboradores que possuam valor de IRRF em sua remuneração, independente de divergência ou não.  Opções:   * **Sim**= lista somente colaboradores com divergência de valores nas colunas de valor. * **Não**= lista informações de todos os colaboradores que possuam valor de IRRF ou Base de IR em sua remuneração |
| **Categoria** | Opcional | Categoria do colaborador o qual se deseja buscar os valores de IRRF. |
| **CPF** | Opcional | CPF do colaborador o qual se deseja buscar os valores de IRRF. |
| **Funcionários por Página** | Opcional | Por Default são retornados 30 funcionários por página, mas pode-se definir uma quantidade maior ou menor. |

### Processamento

Após escolher os filtros desejados, utilize o botão "Aplicar Filtros" para iniciar a coleta e processamento das informações, as quais serão apresentadas no painel.

Durante essa operação, uma barra de progresso é exibida abaixo do container de filtros.

Ao final do processamento, são apresentados os valores sintéticos da Retenção de IRRF, conforme demonstrado abaixo:

Exemplo utilizando filtro por CPF:

**Observação:** Todos os filtros selecionados são apresentados no container abaixo da barra de campos de filtros. Você pode remover um ou mais filtros clicando no "X" à direita de cada ícone ou utilizando o botão "Remover todos".

# Apresentação das Informações

**Cards Totalizadores da Consulta**

Estes cards totalizam os valores de retenção de IR encontrados nas duas fontes de informação (RH e Governo) e demonstra de forma sintética os resultados, desta forma, já é possível identificar se existem divergências nos valores de IRRF.

### **Pesquisa por CPF ou Nome**

O campo apresentado com um ícone de lupa, permite pesquisar entre os dados carregados na tela. A pesquisa é aplicada apenas para o CPF e Nome do colaborador.

### **Tabela Analítica por Pagamento a Colaborador**

A tabela apresentada exibe os valores de forma analítica por pagamento a colaborador. Caso o colaborador possua mais de um vínculo, e consequentemente, mais de um envelope de pagamento, a tabela apresentará os dados somados deste colaborador.

Nesta tabela, é apresentado apenas o Valor de Retenção do IRRF:

A tabela é apresentada com 30 colaboradores (podendo ser editado em Busca avançada opção **Funcionários por página**), para não carregar informações desnecessárias na tela e prejudicar a performance de navegação. Para carregar mais resultados, é possível clicar no botão "Carregar mais resultados".

### **Lista de Funcionários**

Neste quadro podemos identificar os funcionários que possuem divergências através do ícone e os funcionários que possuem somente avisos .

Ao expandir cada funcionário, será possível consultar os valores de retenção de Imposto de Renda (IR) de cada envelope de pagamento.

#### **Detalhamento do demonstrativo**

Ao clicar sobre o demonstrativo, serão apresentados os demais dados referentes aos tipos de Imposto de Renda (IR) existentes no demonstrativo selecionado. 

* No cabeçalho, é possível identificar a qual demonstrativo os dados apresentados se referem.
* Na lista de consolidação, são exibidos os tipos de Imposto de Renda (IR) presentes no demonstrativo, sendo possível expandir cada um deles para visualização detalhada.
* A descrição de cada tipo de IR está associada à incidência de IR indicada nas rubricas presentes em cada envelope de pagamento.

### Exportar Relatório

Clicando no botão **Exportar** é possível salvar os dados Sintéticos gerados em .XLS.

**Exemplo Sintético**: Exporta os valores sintéticos apresentados na primeira tela.

  

**Exemplo Analítico:** Exporta os valores detalhados apresentados ao clicar no perfil individual de cada funcionário.

**Analítico**: Clicando no botão **Exportar** é possível salvar os dados detalhados gerados em .XLS.

# Observações

Os grupos de colunas relativas a valores possuem as seguintes indicações:

* **RH:** Valores de IRRF existentes no envelope de pagamento, provenientes do sistema de Folha de Pagamento.
* **Governo**: Dados interceptados no momento da consulta de retorno do governo do evento S-5002. Esses eventos ficam gravados na fila de eventos, juntamente com os eventos de pagamento.

## Sugestões de Análises

Apresentando divergência de valores, estas devem ser analisadas e identificadas as causas, que podem ser:

* + Rubricas com incidências incorretas que geram bases e valores diferentes no Governo.
  + Inclusões, exclusões ou alterações nas bases e/ou valores operados diretamente no Portal eSocial.

**Tipos de IR vs Incidência IR:**

1. A descrição da tabela abaixo representando o grupo dos códigos relacionados;
2. A descrição de cada código da tabela abaixo está na tabela , caso seja um código não existente nesta tabela, o texto apresentado será o mesmo descrito na documentação técnica do evento S-5002
3. Alguns códigos são aglutinados em outro. Exemplos.:
   1. 11 - Remuneração e 13 - Férias. No evento S-5002 e no relatório são aglutinados no código 11,
   2. 31 - Remuneração e 33 - Férias. No evento S-5002 e no relatório são aglutinados no código 31,
4. [Documentação técnica do governo](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.2/index.html/index.html#evtIrrfBenef)

| Descrição do tipo de IR | Códigos Relacionados |
| --- | --- |
| Rendimentos Tributáveis | 11, 12, 14 |
| Retenções do IRRF | 31, 32, 34 |
| Rendimento não tributável ou isento do IRRF | 70, 71, 72, 73, 74, 75, 76, 77, 700, 701, 79, 7900 |
| Deduções da base de cálculo do IRRF | 41, 42, 46, 47, 51, 52, 54, 61, 62, 63, 64, 67 |
| Exigibilidade suspensa - Rendimento tributável | 9011, 9012, 9014 |
| Exigibilidade suspensa - Retenção do IRR | 9031, 9032, 9034, 9832, 9832, 9834 |
| Exigibilidade suspensa - Dedução da base de cálculo do IRRF | 9041, 9042, 9046, 9047, 9052, 9054, 9061, 9062, 9063, 9064, 9067 |
| Compensação judicial | 9082, 9083 |

## Detalhamento do grupo de colunas da Lista de Funcionários

| Campos | Descrição | Atributo | Campo | Detalhamento |
| --- | --- | --- | --- |
| **Nome** | Nome do trabalhador | name | PESOCIALTOTALIZADORESCPF.NOME, PPESSOA.NOME |
| **CPF** | CPF do Trabalhador | cpfNumber | PESOCIALTOTALIZADORESCPF.CPF, PPESSOA.CPF |
| **Valor Retenção RH** | Valor de retenção de IRRF Total do Trabalhador | erpValue | PESOCIALTOTALIZADORESCPF.VALORIRRF | VALORIRRF13 | VALORIRRFPLR |
| **Valor Retenção Governo** | Valor de retenção de IRRF Total do Trabalhador | retValue | PESOCIALTOTALIZADORESCPF.VALORIRRFRET | VALORIRRF13RET | VALORIRRFPLRRET |

## Detalhamento ao expandir o grupo Lista de Funcionários

PESOCIALTOTALIZADORESAUTONOMOS e PESOCIALTOTALIZADORES detém todos os valores do IRRF, onde PESOCIALTOTALIZADORESAUTONOMOS é somente para autônomos e PESOCIALTOTALIZADORES para funcionários.

| Campos | Descrição | Atributo | Campo | Detalhamento |
| --- | --- | --- | --- |
| **Demonstrativo** | Código do demonstrativo (recibo) do Trabalhador | demonstrativeId | PESOCIALTOTALIZADORESAUTONOMOS | PESOCIALTOTALIZADORES.DETALHES JSON ($.DetalhesIRRF[].IdDemonstrativo) |
| **Categoria** | CPF do Trabalhador | cpfNumber | PESOCIALTOTALIZADORESCPF.CPF |
| **Período de Referência** | Período de Referência | referencePeriod | PESOCIALTOTALIZADORESAUTONOMOS | PESOCIALTOTALIZADORES.DETALHES JSON ($.DetalhesIRRF[].PeriodoReferente) |
| **Valor Retenção RH** | Valor de retenção de IRRF Total do Trabalhador | erpValue | PESOCIALTOTALIZADORESAUTONOMOS | PESOCIALTOTALIZADORES.DETALHES JSON ($.DetalhesIRRF[].ValorERP) |
| **Valor Retenção Governo** | Valor de retenção de IRRF Total do Trabalhador | retValue | PESOCIALTOTALIZADORESAUTONOMOS | PESOCIALTOTALIZADORES.DETALHES JSON ($.DetalhesIRRF[].ValorRet) |
| **Data de Pagamento** | Data de Pagamento do demonstrativo | payday | PESOCIALTOTALIZADORESAUTONOMOS | PESOCIALTOTALIZADORES.DETALHES JSON ($.DetalhesIRRF.DataPagamento) |
| **Origem (Tipo de Pagamento)** | Evento de Origem do demosntrativo | origin | PESOCIALTOTALIZADORESAUTONOMOS | PESOCIALTOTALIZADORES.DETALHES JSON ($.DetalhesIRRF[].TipoRetencao) |

# Informações Técnicas da API IRRFRetValues

A **IRRFRetValues**é um método GET da API **GPEreportEsocialBaseConfer.**   
Em resumo, o método POST da API **GPEreportEsocialBaseConfer**retorna o Id da requisição e o processamento do relatório é executado de forma assíncrona, o método GET **IRRFRetValues**obtém a resposta deste processamento. Exemplos de execução abaixo:

* [GPEreportEsocialBaseConfer](https://tdn.totvs.com/pages/releaseview.action?pageId=784226379)
* [IRRFRetValues](https://tdn.totvs.com/pages/releaseview.action?pageId=784226379)

Exemplo de EndPoint: <http://localhost:8104/rest/api/rh/esocial/v1/GPEreportEsocialBaseConfer>

Requisição POST

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Identificador da empresa** | (1-1) | companyId | string | Código da Empresa |
| **Período** | (1-1) | paymentPeriod | string | Período de apuração |
| **Tipo de Tributo** | (0-1) | tribute | string (default: 0) | 1 - Relatório de INSS  2 - Relatório de FGTS  3 - Relatório de IRRF |
| **Somente divergências** | (0-1) | differencesOnly | boolean (default: false) | Indica se os funcionários com diferenças devem ser retornados ou não |

## Tabelas utilizadas

PESOCIALTOTALIZADORES, PESOCIALTOTALIZADORESCPF, PESOCIALTOTALIZADORESAUTONOMOS e PESOCIALTOTALCPFRUBRICASIRRF

## Veja detalhes quando utiliza o TAF Full:
