---
content_hash: 28fc86d76f1d3b38efee25015fe6470118cb9a9568a6e01106f25713fc4c54e7
fetched_at: '2026-06-29T00:09:49.304705+00:00'
page_id: '435105277'
product: rm
source: tdn-rm
title: Contrato de Locação - Processo - Contabilização do Contrato de Locação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105277
version: 5
---

* Serão obedecidas as configurações de contabilização parametrizada na coligada e no contrato de locação.
* Serão contabilizados apenas os processos do contrato de locação que possuírem Evento Contábil associado. A contabilização será de forma automática caso o parâmetro de coligada **"Contabilização Automática"** estiver marcado.
  + Observação: Mesmo que esteja configurado para contabilização Automática, caso não haja evento contábil associado não haverá contabilização e não será exibida nenhuma mensagem.
* A contabilização poderá ser manual se o parâmetro de coligada "Contabilização Automática" estiver desmarcado.
* O Lote contábil, usado para cada contabilização será criado automaticamente, considerando sempre o próximo ID disponível, e após a criação, será sempre utilizado para cada processo.
* Cada processo que disparar a contabilização utilizará um Lote contábil distinto.
* Todas as visões e edições que tenham necessidade de contabilização (Contrato de locação, Finalizar / Rescindir contrato) possuem um processo **"Contabilizar"** que executará a contabilização do evento correspondente. Este processo será usado sempre que a contabilização não for automática e não for usado o **processo global de contabilização** de locação ou seu agendamento.
* Caso o evento associado ao processo do contrato não esteja preenchido, o processo de contabilização não será executado.
* Não será possível realizar contabilizações de contratos para períodos superiores à data de Encerramento / Rescisão.

**Processos que podem disparar a contabilização**

* **Efetivação do contrato:**

* + Realizará a contabilização conforme **"evento contábil"** definido no contrato para **"Contrato de locação"**.
  + Deverá respeitar o parâmetro de coligada **"Contabilização automática"** e contabilizar automaticamente os processos do contrato.
  + Será contabilizado, apenas se o parâmetro **"Executar automaticamente para"** estiver com a opção **"Efetivação do contrato"** marcada.
  + O período será considerado para processamento de acordo com as definições dos parâmetros **"Data para início da contabilização"** e **"Período de contabilização do contrato".**

* **"Incluir / alterar / excluir" escalonamento:**

* + Executará a contabilização do evento do contrato, pois não há um evento específico para o escalonamento.
  + A contabilização se dará para o período do escalonamento, respeitando o período parametrizado para início da contabilização.
  + Apenas será executada a contabilização se o contrato estiver com a situação **"Efetivado"** e o parâmetro da coligada **"Contabilização Automática"** estiver marcado.
  + A contabilização do escalonamento ocorrerá apenas se o contrato de locação possuir evento contábil.

* **Gerar lançamentos:**

* + Realizará a contabilização conforme **"evento contábil"** definido no contrato para **"Contrato de locação"**.
  + Deverá respeitar o parâmetro de coligada **"Contabilização automática"** e contabilizar automaticamente os processos do contrato.
  + A contabilização se dará para o período definido no processo de Gerar Lançamentos.
  + Será contabilizado, apenas se o parâmetro **"Executar automaticamente para"** estiver com a opção **"Geração de lançamentos"** marcada.
  + Apenas os **Lançamentos a Receber** serão considerados para a contabilização.

* **Efetivar aditivo de Renegociação, Efetivar aditivo de prorrogação, Efetivar aditivo de alteração de locatário e Reajustar contrato de locação:**

* + Irá fazer a chamada para a contabilização do Evento Contábil definido para o Contrato de locação.
  + Respeitará o parâmetro de **"Contabilização Automática"** e irá contabilizar automaticamente o contrato após a efetivação dos aditivos.
  + O período considerado para processamento terá a data de início igual à data do aditivo ou reajuste e a data de termino será de acordo com as definições dos parâmetros **"Período de contabilização do contrato"** e poderá ser **"Período do contrato"** ou **"Informar períodos"**.

* **Finalizar / Rescindir contrato:**

* + Realizará a contabilização conforme **"evento contábil"** definido no contrato para **"Finalizar / Rescindir contrato"**.
  + Deve respeitar o parâmetro de **"Contabilização Automática"**.
  + Excluirá as contabilizações posteriores à data de finalização / rescisão.
    - Caso não seja possível excluir tais contabilizações, uma mensagem será exibida, informando-o que deverá primeiramente resolver junto à contabilidade, estornando ou excluindo os lançamentos contábeis posteriores, para apenas depois finalizar o contrato.
  + Este é o único Evento Contábil do contrato de locação que pode ser contabilizado após da data de rescisão.
  + Apenas a Rescisão irá processar a contabilização. O Encerramento não permite incluir Eventos Financeiros e, consequentemente, não poderá ser contabilizado.

* **Contabilização de Lançamentos Financeiros:**

* + A contabilização dos lançamentos financeiros será realizada através do sistema financeiro.
  + Na geração de lançamentos, será informado ao sistema financeiro qual o efeito contábil a ser considerado para este lançamento.
  + Os eventos contábeis serão considerados conforme parametrizações do financeiro, de acordo com o tipo de documento ou tabelas opcionais.

* As contabilizações realizadas poderão ser visualizadas através do anexo "Lançamentos contábeis do Contrato de Locação", onde serão exibidos os campos "Data de competência" e "Operação contábil". Apenas serão exibidos os períodos que possuem contabilização válida.
* Caso existam apenas contabilizações excluídas ou estornadas, os respectivos períodos e operações não serão exibidos nesta tela, sendo necessário utilizar o módulo contábil para visualiza-los.

****Incluir Lançamentos Contábeis****

* O processo permite ao usuário selecionar um período para geração dos lançamentos contábeis.
* O processo de incluir lançamentos contábeis faz a proporcionalização, do valor a contabilizar no mês, de modo a refletir o valor do aluguel cobrado naquela competência.
* O processo também considera os dias de carência para geração dos lançamentos contábeis proporcionais.

**Log da Contabilização**

* Será possível, para os casos em que a contabilização for executada pelo processo **"Incluir Lançamentos Contábeis"** e o parâmetro de coligada **"Exibe tela de contabilização"** estiver marcado, visualizar na tela de eventos o Log da contabilização.
* O log da contabilização poderá ser habilitado no processo **"Ativar / Desativar Log do Evento Contábil"**.

**Contabilização de Eventos financeiros avulsos**

* A contabilização de eventos financeiros avulsos se dará através dos lançamentos financeiros gerados ou em sua baixa, no próprio módulo financeiro.

**Processos de cancelamento da contabilização**

* **Exclusão da contabilização:**

* + A exclusão da contabilização será realizada sempre que um processo for desfeito e somente se o parâmetro da coligada "Contabilização Automática" estiver marcado.

* + - Serão Excluídas apenas as contabilizações criadas pelo processo que está sendo cancelado no momento.
    - Caso a exclusão não possa ser realizada, será exibida mensagem solicitando que seja feito o estorno ou seja reaberto o período e todo o processo será cancelado.

* + Em todas as visões e edições que possuem contabilização (Contrato de locação, Encerrar/Rescindir contrato) existirá o processo **"exclusão de lançamentos contábeis"** que irá executar a exclusão da contabilização do evento correspondente.

* + - O processo de "exclusão de lançamentos contábeis" nunca estará disponível para as coligadas configuradas para Contabilização automática.
    - O processo de "exclusão de lançamentos contábeis" só ficará visível caso o usuário tenha permissão.
    - Caso o evento associado ao processo do contrato não esteja preenchido, o processo de exclusão não será executado.

* + Caso a exclusão da contabilização seja processada para um período não contabilizado, o sistema exibirá no Log do processo informando que não existe contabilização a ser cancelada.
  + Caso a exclusão da contabilização não seja executada com sucesso em virtude de integralização ou fechamento de período, o processo retornará mensagem de erro informando que não pode ser excluída e a mensagem orientará sobre as opções de reabrir o período contábil ou a necessidade de estornar.
  + Os processos que podem disparar a exclusão da contabilização, de forma automática, caso o parâmetro **"Contabilização Automática"** estiver marcado, são:

* + - **Excluir lançamentos:** Excluirá da contabilização dos lançamentos financeiros criados pela geração de lançamentos financeiros, para o período informado.
    - **Finalizar / Rescindir contrato:** Excluirá das contabilizações posteriores à data da rescisão e realizar os demais tratamentos descritos para o processo na sessão "Processos De Contabilização".
    - **Desfazer Rescisão:** Excluirá da contabilização do evento de rescisão e irá executar a contabilização do contrato e aditivos, considerando para isso as parametrizações do sistema / contrato (se todo o período, se usuário define período)
    - **Exceção: Reabrir o contrato (voltar situação):** Excluirá a contabilização, independente do parâmetro "Contabilização automática", pois não temos como garantir que o contrato será efetivado novamente.
    - **Desfazer aditivo de Renegociação, Desfazer aditivo de prorrogação, Desfazer aditivo de alteração de locatário e Desfazer Reajuste do contrato de locação:**

* + - * Irá fazer a chamada para a contabilização do Evento Contábil definido para o Contrato de locação.
      * Deve respeitar o parâmetro de "Contabilização Automática".
      * O período considerado para processamento terá a data de início igual à data do aditivo ou reajuste e a data de termino será de acordo com as definições dos parâmetros "Período de contabilização do contrato" e poderá ser "Período do contrato" ou "Informar períodos".

* **Estorno da contabilização**

* + O estorno da contabilização será sempre executado de forma **"manual"** pelo processo de estorno e permite que a data de estorno seja definida.
  + A data de estorno é por default a mesma data do lançamento que está sendo estornado.
  + Todas as visões e edições que realizam contabilização (Contrato de locação, Encerrar/Rescindir contrato) possuem o processo **"Estornar lançamentos contábeis"** que irá executar o estorno da contabilização do evento correspondente.

* + - O processo de estorno só ficará visível caso o usuário tenha permissão.
    - Este processo pode ser utilizado para os casos em que a contabilização precisa ser estornada, de acordo com a necessidade.
    - Caso o evento associado ao processo do contrato não esteja preenchido, o processo de estorno não será executado.

* + O campo Histórico padrão, no processo de estorno do lançamento contábil, irá considerar o histórico padrão utilizado na contabilização, concatenando a palavra "Estorno:" no início do histórico.

* + - Será disponibilizado um lookup com históricos no modelo padrão cadastrados previamente.

* + Ao estornar os lançamentos, a operação contábil será mantida para que seja possível rastrear os lançamentos contábeis através do IdOperação.

* **Histórico padrão**

* + Foram criadas novas variáveis que poderão ser utilizadas no cadastro dos Históricos Padrões. Opções de mnemônicos:

* + - **[CODIMOVEL] - Código do imóvel:** concatena quando mais de um ou se estiver "aplicando" por "Item do contrato de locação" busca apenas o imóvel do Contexto;
    - **[DESCIMOVEL] - Descrição do imóvel:** concatena quando mais de um ou se estiver "aplicando" por "Centro de Custo" busca apenas o Centro de custo do Contexto;
    - **[NUMCONTLOC] - Número do contrato de locação;**
    - **[CODCONTLOC] - Código do contrato de locação;**
    - **[DTCONTRATOLOC] - Data do contrato;**
    - **[DTLOCACAOINICONTLOC] - Data de Início da Locação;**
    - **[DTVIGENCIAINICONTLOC] - Vigência Inicial do contrato de locação;**
    - **[DTVIGENCIAFINCONTLOC] - Vigência Final do contrato de locação;**
    - **[NOMELOCATARIO] - Nome do Locatário:** concatena se mais de um;
    - **[DATALANORIG] - Data do Lançamento Original no Estorno:** corresponde a data original do lançamento contábil gerado. Esta variável será utilizada nos históricos de estorno contábil;
    - **[DESCEVENTFIN] - Descrição do Evento Financeiro;**

Informações Complementares

---



Recursos Adicionais

---
