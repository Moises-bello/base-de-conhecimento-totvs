---
content_hash: 08699fb418d2bad53f92f6955404f6b69f8e0dabca47c2a7415f6948c7929c60
fetched_at: '2026-06-29T00:11:31.387130+00:00'
page_id: '737555053'
product: rm
source: tdn-rm
title: Empreendimentos - Processos - Integrar com Registradora
type: documentation
url: https://tdn.totvs.com/display/LRM/Empreendimentos+-+Processos+-+Integrar+com+Registradora
version: 8
---

O Processo **Integrar com Registradora** é utilizado para enviar às Registradoras de Recebíveis, as informações referentes à Resolução **[N](https://www.in.gov.br/web/dou/-/resolucao-cmn-n-4.909-de-27-de-maio-de-2021-322967965)[º](https://www.in.gov.br/web/dou/-/resolucao-cmn-n-4.909-de-27-de-maio-de-2021-322967965)[4.909, DE 27 DE MAIO DE 2021](https://www.in.gov.br/web/dou/-/resolucao-cmn-n-4.909-de-27-de-maio-de-2021-322967965)**, do Conselho Monetário Nacional, CMN, que foi atualizada através da  Resolução CMN Nº 5055 DE 15 DE DEZEMBRO DE 2022,

Premissas para a Execução deste Processo

* Os **campos obrigatórios** detalhados neste [documento](https://tdn.totvs.com/pages/viewpage.action?pageId=729222653#Integra%C3%A7%C3%A3oCERC-1933069771) devem estar preenchidos.
* Como a CERC segue uma legislação, o TCGI precisa garantir que as informações sejam integralizadas conforme a sua competência, o TCGI precisa garantir a fidedignidade das informações integradas, em relação ao fechamento financeiro e contábil do sistema.

Assim, ao executar o processo para Integrar com Registradora, caso tenha algum **Aditivo de Renegociação de Contrato** ou de **Troca de Comprador,** ou **Distrato** efetivado para uma competência posterior à *Data de Integração* selecionada para o envio das informações (*Mês Anterior ou Mês Atual*), o sistema irá apresentar uma exceção solicitando ao usuário que volte a situação deste aditivo ou distrato para Em Preparação, para que este processo seja executado com sucesso.

O TCGI não integra nenhuma parcela com a CERC que tenha:

* + Situação diferente de em Aberto; e
  + Parcelas do Tipo A  Receber.

Para acessá-lo, após dar Permissão ao Menu ***01.02.01.25 - Integrar com Registradora*** (acessível em *Perfil | Acesso a Menus | Gestão de Imóveis | 01 - Venda | 01.02 - Manutenção de Empreendimentos | 01.02.01 - Empreendimento*), basta acessar a aba de *Vendas | Manutenção de Empreendimentos | Integrar com a Registradora*:

Ao acessar este processo é exibida a tela abaixo para se parametrizar a sua execução, não sendo recomendado a utilização de filtros com datas fixas e nem parâmetros pelo fato deste processo ser responsável por enviar/integrar e manter as informações sempre atualizadas na Registradora.

**Integrar com a Registradora de Todos(as) os(as) Lote(s) filtrado(s) por:** As informações a serem integradas neste processo podem ser filtrada pelas entidades abaixo:

* **Empreendimento:** Que filtrará todas as unidades, subunidades e contratos dos empreendimentos selecionados no filtro; ou
* **Unidade:** Que filtrará todas as unidades, subunidades e seus contratos dos empreendimentos/unidades selecionados no filtro; ou
* **Subunidade:**Que filtrará todas as subunidades e seus contratos dos empreendimentos/unidades/subunidades selecionados no filtro; ou

As **Ações** de integração com a registradora pode ser:

* **Incluir/Modificar:**Configurado essa ação, os registros filtrados de empreendimento, unidade, subunidade, contrato, comprador e parcelas serão incluídos/atualizados na registradora;
* **Deletar:**Configurado essa ação, os registros filtrados de subunidades, contratos, compradores e parcelas serão deletados na registradora, porem o empreendimento e unidade serão deletados se não houver outras subunidades vinculadas as mesmas;

**Data Integração:** Selecione qual a competência, em relação ao fechamento financeiro e contábil, das informações a serem integradas/atualizadas com a Registradora. Sendo que ao selecionar uma das opções abaixo o TCGI irá integrar essas informações com a data do último dia do mês selecionado, em relação à data de execução deste processo, alimentando o campo Data Registro das Tabelas de Log da Registradora:

* **Mês Anterior:** Selecione esta opção para que as informações sejam integradas com o último dia do **mês anterior**. Esta opção é a mais indicada pois permite que os dados integrados estejam consolidados através do fechamento financeiro e contábil do mês anterior; ou
* **Mês Atual:** Selecione esta opção para que as informações sejam integradas com o último dia do **mês atual**. Esta opção pode ser utilizada na carga inicial dos dados, ou em algum outro cenário no qual se faça necessário integrar as informações desta forma.

Atenção!

Uma das Regras para o envio de informações das parcelas para a CERC é que, independente da periodicidade definida pela incorporadora para envio dos dados, o sistema exigirá que até o 5º dia corrido de cada mês, exista um evento de manutenção de registro, com data base equivalente ao último dia útil do mês imediatamente anterior.

É extremamente importante que, além dos parâmetros aplicados nos campos descritos acima, o Usuário crie um **Filtro** adequando para tratar esses registros, uma vez que não será possível selecionar nenhum deles especificamente na grid de resultado, para ser integrado separadamente. Todos os registros que estão na grid serão tratados conforme a **Ação** especificada, ao se acionar o botão Executar deste processo.

Agendamento

* Esta funcionalidade é concebida para ser executada de forma autônoma e recorrente (vide a documentação do Agendador de Tarefas); e
* Para manter os dados sincronizados dos valores de parcelas devido o reajuste mensal, o processo deverá ser agendado mês a mês para manter esse sincronismo e sempre após o reajuste.

Importante!

É obrigatório a definição do campo [***Tipo Registradora***](https://tdn.totvs.com/display/LRM/CERC+-+Empreendimento) no empreendimento para o envio de dados para a registradora correta, mesmo que deseje enviar apenas uma subunidade.

As informações tratadas neste Processo são apresentadas ao Usuário das seguintes formas:

* **Log de execução deste processo no JOB:** Que apresenta em detalhes a **Ação,** o *Empreendimento*, a *Unidade*, a *Subunidade*, o *Contrato de Venda*, a *Data da Venda*, a *Situação* deste Contrato (Efetivado, Quitado), a *Coligada*, o *Comprador* e os detalhes de cada uma das *Parcelas* do *Plano de Financiamento* da Venda, como: *Grupo*, *Tipo de Parcela*, *Número da Parcela*, *Data de Vencimento*, *Valor*, *Número de Referência* (Idlan) e *Situação/Status* destas Parcelas; e
* Através das **Tabelas** anexos das seguintes Entidades abaixo e que são sobrescritas a cada execução deste processo, conforme a **Ação** aplicada:
  + No **Empreendimento:** XREGISTRADORAEMPREENDIMENTO, XREGISTRADORADOMICILIOBANCARIO
  + Na **Unidade:** XREGISTRADORAUNIDADE
  + Na **Subunidade:**XREGISTRADORASUBUNIDADE
  + Na **Venda**: XREGISTRADORACONTRATO, XREGISTRADORAMUTUARIO, XREGISTRADORACONTRATOPARCELA,
  + No **Cliente**: XREGISTRADORACONTATOMUTUARIO, XREGISTRADORACONTRATOMUTUARIO
