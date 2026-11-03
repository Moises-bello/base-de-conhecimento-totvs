---
content_hash: 41dd1af73a0484f4184620c0e224d362db034a0e821c2cf1baaf83f221d5bc7e
fetched_at: '2026-06-29T00:10:31.148824+00:00'
page_id: '520671442'
product: rm
source: tdn-rm
title: Folha analítica e GPS - Incidência Exclusiva do segurado no 13° salário.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520671442
version: 4
---

false

**A partir das Versões:**

* 12.1.24.236
* 12.1.25.174
* 12.1.26.122

# Objetivo:

---

Apresentar os tratamentos que foram realizados na GPS e Folha analítica para a nova incidência (**Incidência exclusiva do segurado**) no cadastro de eventos.

---

1true1Execução do scriptExecução do script

Para a liberação a criação do novo parâmetro **Incidência exclusiva do segurado**será necessário executar o script através do sistema RM.Atualizador.exe.

1Cadastro dos eventosCadastro dos eventos

Segue abaixo parametrização realizada no cadastro de evento para realização do teste:

* Evento 7777 - MEDIA COMISSÃO: provento do tipo valor, com a Incidência exclusiva do segurado marcada.

* Evento 7776 - DESC EXCLUSIVA SEGURADO 13° : desconto do tipo valor, com a Incidência exclusiva do segurado marcada.

  
true1Geração dos relatórios Geração dos relatórios 

No envelope de pagamento foi lançado a segunda parcela décimo terceiro salário e os eventos criados anteriormente (aba "Cadastro de Eventos") com os seguintes valores:

* Na aba Incidências o sistema está considerando o valor dos eventos que tem incidência de **INSS 13° Salário** + **Incidência exclusiva do segurado =** 2.500,00 (13º SALARIO 2ª PARCELA) + 13.652,92 (MEDIA COMISSÃO) - 50,00 (DESC EXCLUSIVA SEGURADO 13°)= 16102,92

* Ao gerar a GPS, o sistema irá considerar como **Base de INSS** o valor dos eventos que tem incidência de **INSS 13° Salário****=**2.500,00 (13º SALARIO 2ª PARCELA) = 2.500,00

* Na Folha analítica criamos um novo campo (**Base INSS 13°- Envelope**) e adaptamos o calculo do campo **Base INSS 13°** que passou a ser chamado de **Base INSS 13° - GPS**.

Segue abaixo exemplo do relatório gerado para o envelope demonstrado acima:

* **Base INSS 13° - GPS**: o sistema considerou o valor dos eventos que tem incidência de **INSS 13° Salário****=**2.500,00 (13º SALARIO 2ª PARCELA) = 2.500,00
* **Base INSS - Envelope**:  o sistema considerou o valor dos eventos que tem incidência de **INSS 13° Salário** + **Incidência exclusiva do segurado =** 2.500,00 (13º SALARIO 2ª PARCELA) + 13.652,92 (MEDIA COMISSÃO) - 50,00 (DESC EXCLUSIVA SEGURADO 13°)= 16102,92
