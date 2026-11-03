---
content_hash: 60a7b87248adb357d7a150208ebb9453b4ae5d280f52313530842a3e7ef1d48a
fetched_at: '2026-06-29T00:10:53.020193+00:00'
page_id: '574369796'
product: rm
source: tdn-rm
title: Validações Guia de Resumo de Internação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=574369796
version: 1
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Caso existam Guias de Resumo de Internação para o atendimento, as seguintes validações serão executadas:

* Confere se o tipo de acomodação foi preenchido, caso não, retorna a mensagem de erro “Falta definir o tipo de acomodação. Verifique a correlação do tipo de acomodação da ANS no cadastro de tipos de acomodações e verifique se o plano do convênio do paciente possui acomodação preenchida.”
* Confere se o tipo de internação foi preenchido, caso não, retorna a mensagem de erro "Falta definir o tipo de internação. Registre as informações necessárias de acordo com a guia informada."
* Confere se o regime de internação foi preenchido, caso não, retorna a mensagem de erro "Falta definir o regime de internação. Registre as informações necessárias de acordo com a guia informada."
* Confere se o indicador de acidente foi preenchido, caso não, retorna a mensagem de erro "Falta informar o Indicador de acidente. Registre as informações necessárias de acordo com a guia informada através do botão outras informações (TISS) da função de registro de atendimento."
* Confere se o motivo da alta foi preenchido, caso não e houver mais que uma parcial que não esteja confirmada, retorna a mensagem de erro "Falta definir o motivo da alta. Registre as informações necessárias de acordo com a guia informada."
* Confere se o indicador de acidente é compatível com a versão TISS, caso não, retorna a mensagem de erro, "Indicador de acidente está incompatível com a versão {0} do padrão TISS - ANS. Registre as informações necessárias de acordo com a guia informada."
* Confere se o motivo da alta está nos tipos definidos pela ANS para a versão TISS, caso não, retorna a mensagem de erro, "O motivo de saída do paciente não esta nos tipos definidos pela ANS para a versão {0}. Registre as informações necessárias de acordo com a guia informada através do botão outras informações (TISS) da função de registro de atendimento."

## **02. EXEMPLO DE UTILIZAÇÃO**

## **03. TABELAS UTILIZADAS**

* SZATENDAUTORIZ
* SZANSATEND
* SZPLANOSCONVENIO
* SZTIPOACOMODACAO
* SZPARCIALATEND
* SZANSINDACID

]]>
