---
content_hash: 9d583915d00412935085471395d45b829fe65d839cbac2e4b81f9f6be9616203
fetched_at: '2026-06-29T00:09:10.899064+00:00'
page_id: '403735152'
product: rm
source: tdn-rm
title: S-2230 - Quais ações no sistema podem gerar um evento de afastamento temporário?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=403735152
version: 1
---

Todas as vezes que um processo do sistema cria um registro no histórico de afastamento ou período aquisitivo de férias, automaticamente é gerado um gatilho do evento S-2230.

Esses processos são:

1 - Inclusão de um atestado (afastamento) pelo TOTVS Gestão de Pessoas (Vitae);

2 - Alteração da situação do funcionário através da edição do funcionário no TOTVS Folha de pagamento;

3 - Inclusão de registro diretamente no histórico de afastamento do cadastro do funcionário;

4 - Inclusão/aprovação de Férias cadastradas pelo Portal RH;

5 - Cadastro de férias individual ou coletivas/globais;

6 - Cadastro de férias realizado através do período aquisitivo do cadastro do funcionário;

7 - Importação do histórico de férias ou período de gozo.

Ao executar as ações acima, o sistema gera de forma automática gatilhos do evento S-2230 na fila de eventos. Deverá realizar a geração desses XML's, integrá-los ao TAF e transmití-los ao governo.
