---
content_hash: 190c1e221044a939fc572220598995468244a37d7e2f43cf3cbf88c2e1da517e
fetched_at: '2026-06-29T00:11:16.957797+00:00'
page_id: '674557249'
product: rm
source: tdn-rm
title: Reajuste de valores em parcelas de contratos
type: documentation
url: https://tdn.totvs.com/display/LRM/Reajuste+de+valores+em+parcelas+de+contratos
version: 22
---

## Índice

## Processo

Este processo tem o objetivo de permitir o reajuste de valores em parcelas com ou sem lançamento de um ou mais contratos.

Os contratos serão selecionados através de um filtro que também possibilitará a utilização multicontexto.

É possível realizar o reajuste de parcelas utilizando um percentual ou um valor fixo.

O processo *"Reajuste de valores em parcelas de contrato"* está disponível à partir das versões: 12.1.34.125 e 12.1.2205.

O processo poderá ser configurado para utilizar o fracionamento de Jobs, conforme a documentação disponibilizada, abaixo, e utilizando a classe de job *"EduReajusteParcelasContratoSliceableData"*:

* [Configuração de fracionamento de jobs.](https://tdn.totvs.com/x/lpR-I)

---

## Permissões

A permissão para o acesso ao menu do processo deverá ser concedida através do caminhos:

***Caminho***: Educacional | Currículo e Oferta | Financeiro / Contábil | Contratos | Contratos | Reajuste de valores em parcelas de contratos

Através dos parâmetros educacionais, no anexo do perfil do usuário, será possível restringir a utilização do filtro de multi contexto no processo.

---

## Valor de reajuste

O processo permitirá o reajuste dos valores, sempre acrescendo ao valor original da parcela. Esse acréscimo poderá ser realizado utilizando um valor fixo ou um valor percentual.

Exemplo 1 - Reajuste valor fixo

* Parcela 1 - Valor: R$ 100.00

Valor de reajuste: R$ 40.00

**Valor reajustado: R$ 140.00**

Exemplo 2 - Reajuste valor percentual

* Parcela 1 - Valor R$ 200.00

Valor de reajuste: 10.00%

**Valor reajustado: R$ 220.00**

Informações importantes:

* Serão consideradas apenas parcelas de contratos que não estão cancelados;
* Serão consideradas apenas parcelas com valores fixos;
* Serão consideradas apenas parcelas criadas com o tipo de parcela *"Parcela do plano"*;
* Serão consideradas apenas parcelas que não tenham lançamentos gerados;

O campo de valor será formatado conforme a parametrização do número de casas decimais configurada nos parâmetros do Financeiro:

***Caminho***: *Contas a Receber | Manutenção de Lançamentos |  Lançamento | Opções Gerais | "Nº de casas decimais"*

---

## Reajustar valores de parcelas com lançamentos

A opção *"Reajustar valores de parcelas com lançamentos"*, quando habilitada, permite que os valores de parcelas com lançamentos sejam regerados com o valor de reajuste definido. Para que as parcelas com lançamentos sejam reajustadas, o sistema deve atender às seguintes regras:

* O parâmetro *"Permite regerar lançamentos"* habilitado;
* Status do boleto *"Em aberto";*
* As parcelas devem ser do tipo "Plano";
* O lançamento não pode estar baixado;
* O lançamento não pode ter bolsa de crédito associada;
* O lançamento deve ser de uma parcela com valor fixo.

Caso o parâmetro parâmetro *"Regerar lançamentos cancelados"* esteja habilitado, os boletos com status "Cancelado" também serão regerados com o valor de ajuste definido.

***Caminho***: *Educacional | Integração |  Financeiro | Educacional | Fin - Geral 1/4*

**Importante:**

* Não serão reajustados lançamento(s) de parcela(s) onde tenhamos boleto(s) com status *"Baixado"* ou "Cancelado", exceto para casos onde o parâmetro *"Regerar lançamentos cancelados"* esteja habilitado e o status do(s) boleto(s) sejam *"Cancelado"*;
* Não serão reajustados lançamento(s) de parcela(s) caso o parâmetro *"Permite regerar lançamentos"* não esteja habilitado;
* Não serão reajustados lançamento(s) de parcela(s) com cálculo por crédito;
* Não serão reajustados lançamento(s) de parcela(s) gerados por acordo.

O parâmetro "Reajustar valores de parcelas com lançamentos" está disponível à partir da versão 12.1.34.143

**Lançamentos enviados para cobrança terceirizada:**

Parcelas com lançamentos que foram classificados como enviados para cobrança terceirizada, pelo financeiro, não poderão ter seus valores alterados.

Validação disponível, no Educacional, à partir da versão: 12.1.2302.

Documentação da terceirização: <https://tdn.totvs.com/x/cfADIQ>

---

## Filtros

O processo disponibilizará 3 tipos de filtros:

* Filtro para a seleção de um ou mais contextos;
* Filtro para a seleção dos contratos que terão suas parcelas reajustadas;
* Filtro para a restrição de quais parcelas serão consideradas nos contratos;

Filtro Multi Contexto

No processo, foi disponibilizado o parâmetro *"Habilitar multi contexto"* que permite a definição de um filtro para aplicação do reajuste em mais um contexto.

Caso o parâmetro não seja habilitado, o processo será executado considerando apenas os contratos do contexto atual.

Com a habilitação do parâmetro, será obrigatória a seleção de um filtro que definirá quais serão os contexto utilizados na execução do processo.

**Importante:**

* Somente serão considerados os contextos aos quais o usuário que agendou ou está executando o processo possua permissão;
* Caso sejam definidos os contextos de coligada 4 e 5, no filtro, mas o usuário possua permissão somente na 4, a coligada 5 será desconsiderada;

O parâmetro, por padrão, é disponibilizado para todos os usuário. Caso haja necessidade de restrição, deve-se realizar essa parametrização por perfil, conforme citado na área de permissões.

### Filtro para Contratos

Foram disponibilizados 03 formas de realizar um filtro por contratos:

* Através de um filtro genérico, onde se é utilizado o filtro já utilizado nas visões do sistema;
* Através da seleção do período letivo/matriz aplicada;
* Através de uma consulta SQL já cadastrada no sistema;
  + A consulta utilizada precisa conter os campos: CODCOLIGADA, RA, CODCONTRATO e IDPERLET da tabela SCONTRATO.

A partir da versão **12.1.2302** foi disponibilizado no sistema uma opção, dentro dos filtros por consulta SQL, que possibilita ao usuário escolher se deseja realizar um filtro baseado em Contrato (como era feito anteriormente) ou em Parcela.

Se o usuário optar pelo filtro baseado em Parcela, a consulta utilizada precisa conter os campos: CODCOLIGADA, RA, CODCONTRATO, IDPERLET e IDPARCELA da tabela SPARCELA.

Contudo, **caso haja a utilização do recurso de multi contexto**, será permitida a utilização dos seguintes filtros: ***F****iltro genérico ou Filtro por Consulta SQL***.

Importante

* A definição de um filtro é obrigatória para a execução do processo de reajuste: Filtro Genérico, Período Letivo/Matriz Aplicada ou Consulta SQL.
* O filtro por Consulta SQL está disponível à partir da versão 12.1.34.143

### Filtro de Parcelas

O filtro de parcelas é ***opcional*** e irá funcionar como um segundo filtro que irá restringir quais parcelas serão reajustadas dentro de um contrato.

Poderão ser utilizados os filtros:

* Intervalo do número da parcela e da cota;
* Intervalo da data de vencimento;
* Serviços;

Os filtros que utilizam um intervalo, por parcela e por data de vencimento, não podem ser utilizados ao mesmo tempo.

O filtro por serviço pode ser utilizado sozinho ou com um dos filtros por intervalo. Caso o parâmetro de multi contexto esteja marcado, será permitida a seleção de serviços de outros contextos.

Caso nenhum filtro seja selecionado e nenhum serviço adicionado, serão consideradas todas as parcelas do contrato na realização do reajuste.
