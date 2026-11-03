---
content_hash: eaaf2fbe6df8b5cd65b78fdbf8b550c2ca26ff22b3a04a6abf72bb776b78c39e
fetched_at: '2026-06-29T00:10:31.013645+00:00'
page_id: '520659263'
product: rm
source: tdn-rm
title: Contrato de Locação - Dados Gerais - Contabilidade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520659263
version: 18
---

**Estamos evoluindo toda a contabilização referente ao módulo de aluguel. A parametrização abaixo está descontinuada a partir da versão 12.1.2406**

**Para entender e parametrizar o sistema e realizar a contabilização a partir dos lançamentos financeiros, consulte o passo a passo [CLICANDO AQUI](https://tdn.totvs.com/pages/viewpage.action?pageId=728658149).**

* A contabilização poderá ocorrer para todo o período do contrato ou mês a mês, conforme definição dos parâmetros da coligada e/ou do contrato de locação.
* O processo de contabilização irá possibilitar informar qual o período da contabilização, com data inicial e final a ser definida pelo usuário, conforme definido nos parâmetros da coligada ou do contrato de locação.
* Diferente dos demais dados do contrato de locação, as configurações de contabilização ficarão disponíveis para serem alteradas, mesmo que o contrato já esteja efetivado.
* Os processos de contabilização, respeitarão as configurações atuais, mesmo que sejam períodos passados e tenha havido mudanças destes parâmetros.

**Somente será gerada contabilização quando houver evento financeiro gerado na competência da contabilização. Caso não existam lançamentos gerados, não será possível gerar a contabilização.**

* Os parâmetros do contrato, da aba Contabilidade, estarão presentes também no modelo de contrato.
* **Evento Contábil:** deve ser informado o evento contábil responsável pela contabilização do Contrato de Locação. Este evento definirá a contabilização do contrato que também poderá ser executado também via processo.
* **Executar para:** Definirá a aplicação do evento contábil informado, pode ser executado ao efetivar o **"Contrato de Locação"** e/ou na **"Geração de lançamentos financeiros"**.
  + Para o sistema atualizar os lançamentos contábeis quando os lançamentos financeiros forem alterados (por exemplo reajuste, escalonamento, etc), a opção executar para geração de lançamentos financeiros deverá ser selecionada em conjunto com o parâmetro de Aluguel **Contabilização automática**.
* O Escalonamento irá contabilizar utilizando o mesmo evento contábil do contrato de locação, pois como a alteração é no valor base, não será realizado nenhum ajuste, será refeita a contabilização para o período do escalonamento.
* A exclusão ou alteração do escalonamento irá refazer a contabilização do período do escalonamento de acordo com configuração contábil (por período ou processando até o fim do contrato)
* A contabilização ao cadastrar ou excluir escalonamentos apenas irá ser realizada caso o contrato de locação esteja efetivado.
* **Período de contabilização do contrato:** Irá definir o período das contabilizações dos contratos. Ao criar o contrato será buscado o valor default informado na parametrização contábil da coligada e ficará desabilitado caso o parâmetro de coligada "Bloqueia edição do período no contrato" esteja marcado. As parametrizações de contabilização do período são:
* + Todo período do contrato
  + Informar período: Exibirá uma tela para que o período seja informado

* **Inclusão de campos e definições de "defaults":** Para flexibilizar o evento contábil, foram criados novos "Defaults Contábeis" associados aos seguintes cadastros:

* + Contrato de Locação
  + Modelo de Contrato
  + Tipo de Contrato
  + Parâmetro de Integração Financeira
  + Tipo de Evento Financeiro
  + Imóvel

* **Competência dos lançamentos:** A competência dos lançamentos contábeis será definida de acordo com parâmetro **"Tipo de pagamento"** existente no cadastro **"[Tipo de contrato de locação](https://tdn.totvs.com/pages/viewpage.action?pageId=435105420)"**.

  |  |  |  |
  | --- | --- | --- |
  | **Destinação** | **Tipo de pagamento** | **Descrição** |
  | Arrendamento Mercantil | Mês vencido | Não depende de cobrança e tem início a partir de data base que pode ser início da vigência, início da locação, data do contrato ou outra data informada. |
  | Locação Anual | Mês vencido | Mês anterior a cobrança |
  | Locação Anual | Mês vincendo | No mês da cobrança (art. 42, lei 8.245) |
  | Locação por Temporada | Valor fechado antecipado | Em caso de adiantamento não há provisão, assim a contabilização ocorre no pagamento financeiro (baixa) |
  | Locação por Temporada | Mês vencido | Mês anterior a cobrança |
  | Locação por Temporada | Mês vincendo | A definir |

**Considerações acerca períodos não contabilizados e valor final do contrato**

---

Quando existe uma situação onde um determinado período não é contabilizado o sistema irá emitir mensagem de aviso, informando que não houve contabilização para a competência.

Este cenário pode ocorrer quando, por exemplo o primeiro período possuir uma data de carência superior a trinta dias, englobando vários meses num mesmo período.

Exemplo

* Contrato com inicio de locação em 01/01/2020;
* Carência 90 dias;
* Final do primeiro período em 29/04/2020;
* Ao gerar contabilização para este contrato não teremos contabilização gerada para as competências do mês 02/20 e 03/20.
* A contabilização se iniciará na competência do mês 04, visto os 90 dias de carência.

### Itens de Evento Contábil

---

 No cadastro do item de evento contábil, na guia de **Dados Complementares,**o campo Histórico pode ser configurado com algumas variáveis já pré-definidas no sistema.

Para que essas variáveis sejam exibidas corretamente com o seu respectivo valor no lançamento contábil,  é necessário adiciona-las ao campo Complemento do Histórico.

Importante

O complemento do histórico também funciona mesmo sem preencher o histórico.

**Mnemônicos aceitos para nosso produto:**

[CODCONTLOC],  
[NUMCONTLOC],  
[DTCONTRATOLOC],  
[DTLOCACAOINICONTLOC],  
[DTVIGENCIAINICONTLOC],  
[DTVIGENCIAFINCONTLOC],  
[DATALANORIG],  
[CODIMOVEL],  
[DESCIMOVEL],  
[NOMELOCATARIO],  
[DESCEVENTFIN]

### Interromper processo quando houver inconsistência no período informado

---

Visando ter um processo de contabilização mais dinâmico, implementamos o parâmetro "Interromper processo quando houver inconsistência no período informado" na tela de contabilização a partir da versão 12.1.34.

Este parâmetro, quando marcado, irá interromper a geração da contabilização quando num determinado período existir algum tipo de inconsistência, como por exemplo, uma contabilização já enviada ao lote 0.

Caso o parâmetro seja desmarcado o sistema irá processar a contabilização de forma que mesmo com um erro em determinado período, o processo irá continuar a ser executado onde existir contabilidade válida.

Lembrando que, caso o parâmetro seja desmarcado e existir uma inconsistência em algum período, o processo terminará com alerta, mostrando no log as parcelas inconsistentes.
