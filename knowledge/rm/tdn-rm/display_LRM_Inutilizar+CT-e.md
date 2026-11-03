---
content_hash: 777418e758a2de4600f0ba96ece26caf2767dc9255f77c948361d3b759a1a462
fetched_at: '2026-06-29T00:09:24.632748+00:00'
page_id: '423937975'
product: rm
source: tdn-rm
title: Inutilizar CT-e
type: documentation
url: https://tdn.totvs.com/display/LRM/Inutilizar+CT-e
version: 2
---

Esse processo envia a inutilização de um CT-e com status Inconsistente ou Rejeitado selecionado. Após o envio o status do CT-e fica como Inutilização Pendente. No cadastro da filial, em anexo, CT-e Inutilizados são exibidos todos os CT-es Inutilizados. No envio, o status fica como Inutilização Pendente.  
 Pode ser enviado também uma numeração de CT-e para inutilizar, não existindo movimento para ela, sendo que nessa situação o sistema exibe a tela para preenchimento dos dados da numeração de CT-e a ser inutilizada.  
 **Filial:** Filial do CT-e  
 **Série:** Série do movimento de CT-e  
 **Faixa Inicial:** Número do primeiro CT-e a ser inutilizado. (Pode enviar movimentos dentro de um intervalo de números  
 **Faixa Final:** Número do último CT-e a ser enviado. (Pode enviar movimentos dentro de um intervalo de números)  
 **Observação:** Inserir informação sobre a inutilização.

***Observação***: Quando utilizado o Client Neogrid, para cada envio de inutilização de CT-e enviado é gerado um XML, que primeiro vai para a pasta OUT e após processamento da ferramenta, é enviado para a pasta SENT, e assim será enviado para a Neogrid. Essas pastas ficam no diretório onde o Client Neogrid está instalado.
