---
content_hash: 5d08df37ac0ea0a8b028af731b345cb2c1f1f54877ae503ed2e3eb10babb19fd
fetched_at: '2026-06-29T00:08:59.623844+00:00'
page_id: '364908522'
product: rm
source: tdn-rm
title: S-2298 – Reintegração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364908522
version: 13
---

S-2298 – Reintegração

* São as informações de reintegração, em sentido amplo, de empregado/servidor previamente desligado do empregador/ Órgão Público. Integram o conceito de reintegração, para fins do eSocial, todos os atos que restabelecem o vínculo tornando sem efeito o desligamento.
* Quem está obrigado: Todo empregador/ Órgão Público que, por decisão administrativa/judicial, tenha que reintegrar o trabalhador.
* Deverá ser enviado  até o dia 07 (sete) do mês seguinte a que se refere a reintegração, desde que não ultrapasse a data do envio do evento “S-1200 - Remuneração de Trabalhador vinculado ao Regime Geral de Previdência Social vinculado ao Regime Geral de Previdência Social”, e o “S-1202 – Remuneração do servidor vinculado a Regime Próprio de Previdência Social”, para o trabalhador a que se refere.
* Deverá ter sido enviado o evento “S-2299 – Desligamento” ou S-2200 com o campo dtDeslig preenchido.

Procedimentos para geração do evento S-2298 – Reintegração

1º Passo: Incluir um colaborador em Administração de Pessoal | Cadastros |Funcionários com tipo de Admissão - I -Reintegração.

Será gerado gatilho na fila de eventos para o evento S-2298 – Reintegração com status 0-pendente.

2ºPasso:Gerar XML:

O usuário deverá processar a  Geração do  XML para que o evento fique no status 1-Gerado .

Para isso deverá selecionar o evento e clicar Gerar XML dentro da fila de eventos ou através do menu esocial | Eventos de tabelas |Não Periódicos | Gerar XML.

3ºPasso:Integrar evento com o TAF

Para isso deverá selecionar o evento e clicar Integrar TAF.

Neste momento o status do evento será alterado para 3-Enviado  para o TAF.

4ºPasso:Enviar os eventos gerados na fila para o Totvs Automação Fiscal (TAF):

5ºPasso: Atualizar status da integração TAF:

Para atualizar o status da integração do TAF terá as seguintes opções: Na fila de eventos selecionar   " Processos" |Atualizar Status integração TAF ou através do menu Processos | Atualizar Status Integração TAF.

Veja mapeamento dos campos informados:
