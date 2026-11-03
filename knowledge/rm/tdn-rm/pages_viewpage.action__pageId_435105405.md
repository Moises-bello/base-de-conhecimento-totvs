---
content_hash: afee1467f01eb2a0873333febe0d1ad547c236e8fd9d81e74f4210fce310efdf
fetched_at: '2026-06-29T00:09:50.119010+00:00'
page_id: '435105405'
product: rm
source: tdn-rm
title: Processo global de contabilização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105405
version: 1
---

**Processo global de contabilização**   
O processo foi criado para permitir que a contabilização possa ser disparada de acordo com o que foi selecionado, entre outras coisas, quais os processos serão contabilizados (Contrato de locação e/ou Encerramento/Rescisão) para o período definido. Na execução desse processo, o parâmetro do contrato de locação **"Período de contabilização do contrato"** não será considerado e será processado o período selecionado. Será considerado, entretanto, a **"Data para início da contabilização"** e a data de término ou rescisão do contrato.

* O processo segue a parametrização informada na coligada e no contrato de locação.
* Exibirá a opção de qual período deverá ser processado, com data inicial e final de processamento.
* Irá executar o processamento dos eventos contábeis para os processos selecionados, dentre as opções: Contrato de locação e Finalizar / Rescindir contrato
* É um processo multi-coligadas e permite que o usuário selecione as coligadas que possui permissão e destas, os contratos que serão processados.
* O processo permite agendamento de execução e recorrências.
