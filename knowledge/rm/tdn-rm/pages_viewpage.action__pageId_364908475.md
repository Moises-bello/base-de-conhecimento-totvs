---
content_hash: 16b1bc139ec6c3428eaa2100eef938fbce008ebfd5c373939b1ca32a011b78e9
fetched_at: '2026-06-29T00:08:59.607511+00:00'
page_id: '364908475'
product: rm
source: tdn-rm
title: S-2220 - Monitoramento da Saúde do Trabalhador
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364908475
version: 19
---

O evento S-2220 detalha as informações relativas ao monitoramento da saúde do trabalhador, durante todo o vínculo laboral com o empregador/contribuinte/órgão público, por trabalhador, no curso do vínculo ou do estágio, bem como os exames complementares aos quais o trabalhador foi submetido.

O evento deve ser enviado até o dia 07 (sete) do mês subsequente ao da realização do correspondente exame. Essa regra não altera o prazo legal para a realização dos exames, que devem seguir o previsto na legislação, sendo que somente o registro da informação no eSocial é permitido até o dia 07 (sete) do mês subsequente.

**Pré-requisitos**: Envio dos eventos “S-2200 - Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador” ou “S-2300 - Trabalhadores Sem Vínculo Emprego/Estatutário – Início”.

Para atender ao evento S-2200, foram realizadas as seguintes modificações no produto:

1) Em Cadastros| Profissional de Saúde, os campos "CPF" e "NIT" foram incluídos como opcionais.

 2) Em PCMSO | Responsável pela Monitoração Biológica foi incluindo o campo "UF de expedição do CRM/COREN".

**Observação:**

* O campo "NIT" não é mais obrigatório.
* No XML, o campo "Reg. Cons. Classe" será truncado, exibindo apenas os primeiros 10 caracteres, seguindo o leiaute do eSocial.

3) Em PCMSO | Prontuário Médico, ao adicionar o resultado do exame, foi incluído o campo "Procedimento Diagnóstico". Os dados inseridos neste campo estão relacionados à Tabela 27 do eSocial.

4) No assistente de lançamento de exames, foi adicionado o campo "Data de Emissão Aso", que será ativado apenas quando o tipo de procedimento for consulta médica ocupacional. Este campo é agora obrigatório para a geração do XML.

Procedimentos para gerar o evento S-2220

1) Em PCMSO| Prontuário Médico - Cadastrar uma consulta/exame.

2) Em PCMSO | Assistente de Lançamento de Exames:

 3) Em PCMSO | Assistente de Importação de Resultado de Exames

Exemplo de um arquivo XML para importação:

**Geração do gatilho S-2220:**

Através dos processos listados acima, será gerado um gatilho na Fila de Eventos para o evento S-2220 com o status 0 – Pendente. O usuário poderá visualiza-lo através do menu eSocial| Fila de Eventos.

**Geração do XML gatilho S-2220:**

Deverá executar o processo “Gerar XML” para que o evento fique no status 1 – Gerado.

XML referente ao Tipo de Procedimento: Consulta Médica Ocupacional:

Para que o envio seja realizado corretamente, são considerados os seguintes campos da Consulta/Exame:

Consulta

* Data da consulta
* Tipo da consulta/Tipo da consulta para o eSocial
* Data de emissão ASO
* Situação
* Serviço de Saúde Responsável
* Código do Médico

Exame

* Data do exame
* Procedimento Diagnóstico
* Observação

Veja mapeamento dos campos que serão informados: [Evento S-2220](http://tdn.totvs.com/display/public/LRM/Evento+S-2220).

**Integrar evento S-2220 com o TAF:**

Deverá executar o processo “Integrar TAF” para que o evento fique no status 3 – Enviado para o TAF.

**Enviar os eventos gerados na fila para o Totvs Automação Fiscal (TAF):**

Acesse o produto TOTVS Automação Fiscal (TAF) e realize o procedimento para envio das informações do TOTVS Folha de Pagamento para o TAF.

**Atualizar status integração Totvs Automação Fiscal (TAF):**

Para atualizar o status da integração do TAF, você terá as seguintes opções:

* Na fila de eventos, selecione "Processos" e, em seguida, "Atualizar Status Integração TAF". Ou
* No Totvs Folha de Pagamento, acesse "eSocial", clique em "Processos" e, em seguida, em "Atualizar Status Integração TAF".

**Observações:**

* A partir do layout 2.0 da NDE 01/2018, lançado em 14/09/2018, os resultados dos exames toxicológicos são enviados no evento S-2221.
* Quando o Tipo de Atendimento é classificado como “Atendimento Ambulatorial”, não é acionado o evento S-2220.

Veja mapeamento dos campos que serão informados: Evento [S-2220](http://tdn.totvs.com/display/LRM/Evento+S-2220).
