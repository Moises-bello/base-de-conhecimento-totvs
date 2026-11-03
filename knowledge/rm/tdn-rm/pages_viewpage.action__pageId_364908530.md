---
content_hash: 8d2b00120ab46442db601a70cf99e74359da842273825ccdd48a5e49295def23
fetched_at: '2026-06-29T00:08:59.626341+00:00'
page_id: '364908530'
product: rm
source: tdn-rm
title: S-2299 – Desligamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364908530
version: 6
---

* São as informações destinadas a registrar o desligamento do trabalhador da empresa/órgão público.
* As informações de desligamento de empregados devem ser enviadas até 10 (dez) dias seguintes à data do desligamento, desde que não ultrapasse a data do envio do evento “S-1200 – Remuneração”, para o empregado a que se refere o desligamento. Para servidores de regime jurídico estatutário e regime administrativo especial, deverá ser observada a data do envio do evento “S-1200 – Remuneração de Trabalhador Vinculado ao Regime Geral de Previdência Social” e “S-1202 Remuneração de servidor vinculado a Regime Próprio de Previdência Social”. No caso de desligamento por sucessão.
* O  prazo de envio é até o dia 7 do mês seguinte ao do desligamento.

Procedimentos para geração do evento S-2299 – Desligamento:

1º Passo:Cadastrar e calcular uma rescisão.

Será  gerado gatilho na Fila de eventos para o evento S-2299 com status 0-Pendente.

O Usuário poderá visualizá-lo através do menu eSocial | Eventos de tabelas/ Não Periódicos.

2ºPasso:-Gerar XML:

Deverá executar o processo de Geração do  XML para que o evento fique no status 1-Gerado .

Para isso deverá selecionar o evento e clicar Gerar XML dentro da fila de eventos ou através do menu esocial | Eventos de tabelas |Não Periódicos | Gerar XML.

3ºPasso:-Realizar o processo de integração do evento com o TAF:

Para isso deverá selecionar o evento e clicar Integrar TAF.Neste momento o status do evento será alterado para 3-Enviado  para o TAF.

4ºPasso:Enviar os eventos gerados na fila para o Totvs Automação Fiscal (TAF):

* Acesse o produto Totvs Automação Fiscal (TAF)  e realize  o processamento para envio das informações do Totvs Folha de pagamento para o TAF.

5ºPasso: Atualizar status da integração TAF:

Para atualizar o status da integração do TAF Terá as seguintes opções:

* Na fila de eventos selecionar   " Processos" |Atualizar Status integração TAF ou através do menu Processos | Atualizar Status Integração TAF.

Veja mapeamento dos campos que serão informados :
