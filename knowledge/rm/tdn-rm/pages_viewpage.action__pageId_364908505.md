---
content_hash: b9000d04f743fe47e03fa7bc2fef4191f3fc41777c9cd8964308b3f35fe94009
fetched_at: '2026-06-29T00:08:59.618486+00:00'
page_id: '364908505'
product: rm
source: tdn-rm
title: S-2250 – Aviso Prévio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364908505
version: 8
---

* Este evento tem como objetivo registrar a comunicação e o possível cancelamento do aviso prévio de iniciativa do empregador ou do empregado
* Este evento deve ser enviado em até 10 (dez) dias de sua comunicação

Procedimentos para geração do evento S-2250 – Aviso Prévio.  
  
1º Passo: Cadastrar um Aviso prévio  .  
Acessar Administração de pessoal | Funcionários e clicar no ícone "Aviso prévio".

Será gerado gatilho na fila de eventos  para o evento com status 0-Pendente.

2º Passo:Gerar XML:

O usuário deverá processar a  Geração do  XML para que o evento fique no status 1-Gerado .

Para isso deverá selecionar o evento e clicar Gerar XML dentro da fila de eventos ou através do menu esocial | Eventos de tabelas |Não Periódicos | Gerar XML.

3ºPasso:Realizar o processo de Integração do evento com o TAF:

 Para isso deverá selecionar o evento e clicar Integrar TAF.

Neste momento o status do evento será alterado para 3-Enviado  para o TAF.

4º Passo: Enviar os eventos gerados na fila para o Totvs Automação Fiscal (TAF):

* Acesse o produto Totvs Automação Fiscal (TAF)  e realize  o processamento para envio das informações do Totvs Folha de pagamento para o TAF.

5ºPasso: Atualizar status da integração TAF:

 Para atualizar o status da integração do TAF terá as seguintes opções:  
Na fila de eventos selecionar   " Processos" |Atualizar Status integração TAF ou através do menu Processos | Atualizar Status Integração TAF.

  

Veja mapeamento dos campos que serão informados:
