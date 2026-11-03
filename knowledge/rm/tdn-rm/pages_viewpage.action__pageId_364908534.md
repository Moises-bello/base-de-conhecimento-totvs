---
content_hash: 3c9403393a44f2bef6efa927cf279e95ca81835b7ddc5b6ad40fc85eb99231dd
fetched_at: '2026-06-29T00:08:59.628743+00:00'
page_id: '364908534'
product: rm
source: tdn-rm
title: S-2300 – Trabalhador Sem Vínculo de Emprego/Estatutário - Início
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364908534
version: 6
---

* São as informações utilizadas para a atualização dos dados contratuais relativos aos trabalhadores que não possuem vínculo emprego/estatutário com a empresa/órgão público. Quem está obrigado:  a empresa/órgão público que utilizam mão de obra de trabalhador sem vínculo de emprego/estatutário informando no evento “S-2300 - Trabalhador Sem Vínculo de Emprego/Estatutário – Início”.
* Este evento deve ser enviado até o dia 07 (sete) do mês seguinte à ocorrência da alteração, ou antes, do envio do evento “S-1299 – Fechamento de Eventos Periódicos”, o que ocorrer primeiro. Pré-requisitos: envio do evento S-2300 - Trabalhador Sem Vínculo de Emprego/Estatutário - Início.

Para a geração do evento S-2300 – Trabalhador Sem Vínculo de Emprego/Estatutário - Início o usuário  deverá seguir os seguintes passos:

1º Passo:Cadastre um funcionário através do menu Administração de Pessoal | Funcionários sem vínculo empregaticio.

O sistema irá validar o campo Codigo da categoria eSocial.

Será  gerado gatilho na Fila de eventos para o evento S-2300 – Trabalhador Sem Vínculo de Emprego/Estatutário - Início,  com status 0-Pendente.

O Usuário poderá visualizá-lo através do menu eSocial | Eventos de tabelas/ Não Periódicos.

2ºPasso:-Gerar XML:

Deverá executar o processo de Geração do  XML para que o evento fique no status 1-Gerado .

Para isso deverá selecionar o evento e clicar Gerar XML dentro da fila de eventos ou através do menu esocial | Eventos de tabelas |Não Periódicos | Gerar XML.

3ºPasso:-Realizar o processo de integração do evento com o TAF:

Para isso deverá selecionar o evento e clicar Integrar TAF.Neste momento o status do evento será alterado para 3-Enviado  para o TAF.

4ºPasso:-Enviar os eventos gerados na fila para o Totvs Automação Fiscal (TAF):

* Acesse o produto Totvs Automação Fiscal (TAF)  e realize  o processamento para envio das informações do Totvs Folha de pagamento para o TAF.

5ºPasso: Atualizar status da integração TAF:

Para atualizar o status da integração do TAF Terá as seguintes opções:

* Na fila de eventos selecionar   " Processos" |Atualizar Status integração TAF ou através do menu Processos | Atualizar Status Integração TAF.

Veja mapeamento dos campos que serão informados:
