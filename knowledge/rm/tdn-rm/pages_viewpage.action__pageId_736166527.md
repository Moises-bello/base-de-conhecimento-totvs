---
content_hash: c87dba66b07cd5a361ec7aa4fff7b80532429f91f372a26f5c82087ecc613970
fetched_at: '2026-06-29T00:11:29.294508+00:00'
page_id: '736166527'
product: rm
source: tdn-rm
title: Integração CERC (Registradora Recebíveis) - Processos - Integrar com Registradora
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=736166527
version: 11
---

Para possibilitar o envio das informações referentes à Resolução **[N](https://www.in.gov.br/web/dou/-/resolucao-cmn-n-4.909-de-27-de-maio-de-2021-322967965)[º](https://www.in.gov.br/web/dou/-/resolucao-cmn-n-4.909-de-27-de-maio-de-2021-322967965) [4.909, DE 27 DE MAIO DE 2021](https://www.in.gov.br/web/dou/-/resolucao-cmn-n-4.909-de-27-de-maio-de-2021-322967965)**, do Conselho Monetário Nacional, CMN, que foi atualizada através da  Resolução CMN Nº 5055 DE 15 DE DEZEMBRO DE 2022,

A integração com a registradora CERC envolve envio de dados do [Empreendimento](https://tdn.totvs.com/display/LRM/CERC+-+Empreendimento), [Unidades](https://tdn.totvs.com/display/LRM/CERC+-+Unidades), [Subunidade](https://tdn.totvs.com/display/LRM/CERC+-+Subunidades)s, Contratos, Comprador Principal, Parcelas e dados da integração Bancária.

Importante:

Para acessar este Processo é preciso dar Permissão ao Menu ***01.02.01.25 - Integrar com Registradora*** (acessível em *Perfil | Acesso a Menus | Gestão de Imóveis | 01 - Venda | 01.02 - Manutenção de Empreendimentos | 01.02.01 - Empreendimento*).

A integração com a registradora pode ser filtrada por: (não deve-se utilizar utilizar data fixas ou parâmetros nos filtros para a execução do mesmo)

* **Empreendimento:** Que filtrará todas as unidades, subunidades e contratos dos empreendimentos selecionados no filtro; ou
* **Unidade:** Que filtrará todas as unidades, subunidades e seus contratos dos empreendimentos/unidades selecionados no filtro; ou
* **Subunidade:** Que filtrará todas as subunidades e seus contratos dos empreendimentos/unidades/subunidades selecionados no filtro; ou

Atenção!

É extremamente importante que, além dos parâmetros aplicados nos campos descritos acima, o Usuário crie um **Filtro** adequando para tratar esses Registros, uma vez que não será possível selecionar nenhum deles especificamente ser integrado, todos os que estão na grid serão tratados conforme a **Ação** especificada, ao se acionar o botão Executar.

As ações de integração com a registradora pode ser:

* **Incluir/Modificar:** Configurado essa ação, os registros filtrados de empreendimento, unidade, subunidade, contrato, comprador e parcelas serão incluídos/atualizados na registradora;
* **Deletar:** Configurado essa ação, os registros filtrados de subunidades, contratos, compradores e parcelas serão deletados na registradora, porem o empreendimento e unidade serão deletados se não houver outras subunidades vinculadas as mesmas;

Agendamento

* Esta funcionalidade é concebida para ser executada de forma autônoma e recorrente (vide a documentação do Agendador de Tarefas); e
* Para manter os dados sincronizados dos valores de parcelas devido o reajuste mensal, o processo deverá ser agendado mês a mês para manter esse sincronismo e sempre após o reajuste.

Importante

É obrigatório a definição do campo [***Tipo Registradora***](https://tdn.totvs.com/display/LRM/CERC+-+Empreendimento) no empreendimento para o envio de dados para a registradora correta, mesmo que deseje enviar apenas uma subunidade.

As informações tratadas neste Processo são apresentadas ao Usuário das seguintes formas:

* **Log de execução deste processo no JOB:** Que apresenta em detalhes a **Ação,** o *Empreendimento*, a *Unidade*, a *Subunidade*, o *Contrato de Venda*, a *Data da Venda*, a *Situação* deste Contrato (Efetivado, Quitado), a *Coligada*, o *Comprador* e os detalhes de cada uma das *Parcelas* do *Plano de Financiamento* da Venda, como: *Grupo*, *Tipo de Parcela*, *Número da Parcela*, *Data de Vencimento*, *Valor*, *Número de Referência* (Idlan) e *Situação/Status* destas Parcelas; e
* Através das **Tabelas** anexos das seguintes Entidades abaixo e que são sobrescritas a cada execução deste processo, conforme a **Ação** aplicada:
  + No **Empreendimento:** XREGISTRADORAEMPREENDIMENTO
  + Na **Unidade:** XREGISTRADORAUNIDADE
  + Na **Subunidade:** XREGISTRADORASUBUNIDADE
