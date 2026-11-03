---
content_hash: e494068410adbff16b2766d011f47517286e320bf785345caf8036469aa4aa2b
fetched_at: '2026-06-29T00:10:58.284063+00:00'
page_id: '605020052'
product: rm
source: tdn-rm
title: Consultar Autorização de Evento (TSSWSREINF.ConsultarEventos)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=605020052
version: 13
---

Ao consultar a autorização ou cancelamento de um Evento da Reinf, o sistema realiza uma integração com o TSS através do  e através dos dados retornados pelo TSS para o RM irá interprestar o resultado da consulta de autorização do Evento. Neste caso será carregado o XML retornado no campo **XMLRETEVEN** e através do XML carregado iremos recuperar o campo **nrRecArqBase** do Grupo **infoTotal.**O Evento será atualizado conforme abaixo:

* Autorizado: o Evento será considerado Autorizado sempre que
  + o campo **STATUS** for retornado com o código **6**; e
  + o xml retornado no campo **XMLRETEVEN**for um xml válido e dentro deste xml o campo **nrRecArqBase** estiver preenchido com o Protocolo retornado pela RFB.

    - Em uma situação da qual o campo **nrRecArqBase** estiver vazio, o sistema irá verificar se no **TSS**o evento possui número de **Recibo** e o **Status**igual a Autorizado, caso ambas as condições sejam verdadeiras, o campo **nrRecArqBase** será preenchido com **Recibo** informado no **TSS** e o evento no RM será **Autorizado**.

Retorno do "ConsultarEventos"XML do campo XMLRETEVEN 

* Pendente: o Evento permanecerá com status Pendente sempre que
  + o campo **STATUS** for retornado com o código **1** ou **2** ou **4** ou"**em branco**"; ou
  + o campo **STATUS** retornar um código **diferente** dos conhecidos (**1,2,3,4,5,6,7**); ou
  + o campo **STATUS** retornar **6**, mas o **Protocolo** não for encontrado no campo **nrRecArqBase** (vide regra Autorizado "XML do campo XMLRETEVEN").

    - Nesta situação, o sistema verifica se no **TSS**o evento possui número de **Recibo** e o **Status**igual a Autorizado, caso ambas as condições não sejam verdadeiras o status do evento no RM se manterá como **Pendente**.

Imagem

* Rejeitado: o Evento será considerado Rejeitado sempre que
  + o campo STATUS for retornado com o código **5** ou **3** ou **7**.
  + No caso do Evento ser rejeitado o RM irá consultar o retorno das informações do campo **regOcorrs** para apresentar o log de erro ao usuário.
  + Imagem
