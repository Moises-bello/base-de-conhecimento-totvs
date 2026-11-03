---
content_hash: 511801a6ee417e33a9f0c62429886af33f6726583b0af0cbe66b3a1f916b39b3
fetched_at: '2026-06-29T00:10:53.905879+00:00'
page_id: '589761956'
product: rm
source: tdn-rm
title: Código de Cálculo 445 - ATESTADO MÉDICO SEM INCIDÊNCIA EM INSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=589761956
version: 18
---

Provento do tipo valor.

De acordo com Jurisprudência consolidada do STJ, [Parecer SEI Nº 16120/2020/ME](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes-producao-empresas-e-ambiente-de-testes/#7-23----29-12-2020----parecer-sei-n--16120-2020-me--como-deve-ser-tratada-a-incid-ncia-tribut-ria-nos-15-primeiros-dias-de-afastamento-que-antecedem-o-benef-cio-de-aux-lio-doen-a-), veja maiores informações em .

**Atenção:**

Devido a alteração posterior no Parecer SEI Nº 16120/2020/ME, os  eventos com o Código de Cálculo 445 - ATESTADO MÉDICO SEM INCIDÊNCIA EM INSS, na aba Inc. Proventos, não deverão ter marcadas as flags INSS e Incidência exclusiva do segurado.

**Observação:**

01 - Para que o sistema lance corretamente o evento com código de cálculo 445 - ATESTADO MÉDICO SEM INCIDÊNCIA EM INSS, deverá ser marcada a flag ' Afastamento pela previdência social', disponível em RM | RH | Folha de Pagamento | Administração de Pessoal | Funcionários | Anexos | Históricos | Histórico de Afastamento.

02 - Não será lançado o código de cálculo 145 existente no parametrizador,  via lançamento de grupo de eventos, caso exista o código de cálculo 445 no envelope do funcionário. Os dois códigos de cálculo deverão ser lançados manualmente, caso haja necessidade de lançamento simultâneo.

Por exemplo:

Atestado de 15 dias por acidente de trabalho no inicio do mês e lançamento de atestado por doença, Previdência, maior que 15 dias no final do mês.

03 - A entrada de dados, a inclusão de evento no envelope e o lançamento de grupo de eventos com o parâmetro "Lança o evento de atestado médico via grupo de eventos" marcado, são tratados como controle manual do usuário e com isso o evento com código de cálculo 145 será lançado no movimento mesmo que exista o código de cálculo 445 já lançado.

Mais informações
