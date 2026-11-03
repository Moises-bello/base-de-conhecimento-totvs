---
content_hash: e81f6f35817ea786090fae5d8e3bb01d55cd9eb0b7451a29db2ac95898cea32b
fetched_at: '2026-06-29T00:11:36.949731+00:00'
page_id: '773900723'
product: rm
source: tdn-rm
title: DT - Envelope - Botão 'Eventos Zerados'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=773900723
version: 5
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Envelope de Pagamento |
| País: | Brasil |
| Story | [DRHCALCRM-4600](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-4600) |

## **01.** **VERSÕES**

**A partir da Versão:**

* + **12.1.2310.1**

## **02. SITUAÇÃO/REQUISITO**

Para que o usuário, visualize os eventos com valores zerados no envelope, hoje, é necessário ter acesso ao parâmetro global '**Visualização de eventos com valores zerados no envelope**', disponível em **RM | RH | Folha de Pagamento | Configurações | Folha de Pagamento | Folha Normal | Ficha Financeira**. Porém, por se tratar de parâmetros de funcionamento do sistema, por segurança, as empresas não permitem aos usuários finais esse acesso, fazendo esse bloqueio nas permissões dos usuários.

O cliente solicitou ter uma forma de acesso a esta funcionalidade sem que seja necessário dar essa permissão de acesso aos usuários finais com o imtuito de garantir a segurança aos parâmetros do sistema.

## **03. SOLUÇÃO**

Foi criado o botão **"Eventos Zerados"** no Envelope de Pagamento do funcionário. Ao clicar no '**botão**' serão apresentados os eventos com valores zerados no envelope.

## **07. EXEMPLO**

Vamos considerar o Envelope de Pagamento do funcionário com os eventos abaixo lançados/calculados e com o parâmetro global '**Visualização de eventos com valores zerados no envelope**', disponível em **RM | RH | Folha de Pagamento | Configurações | Folha de Pagamento | Folha Normal | Ficha Financeira, Marcado:**

Neste caso, o usuário tinha permissão de acesso aos parâmetros globais e fazia o controle da exibição dos eventos com valor zerado, através do parâmetro global.

Neste outro exemplo, vamos considerar o Envelope de Pagamento do funcionário com os eventos abaixo lançados/calculados e com o parâmetro global '**Visualização de eventos com valores zerados no envelope**', disponível em **RM | RH | Folha de Pagamento | Configurações | Folha de Pagamento | Folha Normal | Ficha Financeira, Desmarcado:**

Neste caso, o usuário não tinha permissão de acesso aos parâmetros globais e fazia o controle da exibição dos eventos com valor zerado, através do botão '**Eventos Zerados**', que foi apresentado no envelope, após desmarcar o parâmetro global.

## **05. DEMAIS INFORMAÇÕES**

Para que seja apresentado o botão no envelope de pagamento, o parâmetro '**Visualização de eventos com valores zerados no envelope**', disponível em **RM | RH | Folha de Pagamento | Configurações | Folha de Pagamento | Folha Normal | Ficha Financeira**,deverá estar **desmarcado**.

## **06. ASSUNTOS RELACIONADOS**

* [Envelope de Pagamento](https://tdn.totvs.com/display/LRM/Envelope+de+Pagamento)
* [Parametrizador - Ficha Financeira](https://tdn.totvs.com.br/display/LRM/Ficha+Financeira)
