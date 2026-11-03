---
content_hash: 9c89a3751bbdd5fe9597a37dc4b6fda1d71fa03344b0e1bb8cd1630eabde0fcf
fetched_at: '2026-06-29T00:09:31.965662+00:00'
page_id: '425458802'
product: rm
source: tdn-rm
title: Alterar data de vencimento do Boleto
type: documentation
url: https://tdn.totvs.com/display/LRM/Alterar+data+de+vencimento+do+Boleto
version: 6
---

---

Este processo permite que a data de vencimento dos boletos seja alterada.

Selecione o(s) boleto(s) desejado(s) e execute o processo, em seguida indique a nova data de vencimento. Se desejar que a data de vencimento do(s) lançamento(s) financeiro(s) referente(s) ao(s) boleto(s) também seja alterada, marque a opção 'Alterar data de vencimento do lançamento', caso esta opção não seja marcada, somente a data de vencimento do(s) boleto(s) será alterada.  
   
Vale lembrar que a data de vencimento das parcelas dos contratos dos alunos não sofrerá alteração com a execução deste processo, pois esta alteração refletirá somente na parte financeira.

**Atenção**

Não será possível alterar a data de vencimento para o(s) boleto(s) que possuir(erem) QR Code PIX gerado em que o status da transação seja:

* + Leitura de Pagamento Confirmado;
  + Leitura de Pagamento Efetuado;
  + Pagamento Autorizado;
  + Pagamento Concluído;
  + Pagamento Confirmado;
  + Pagamento Solicitado.

A permissão para execução deste processo é habilitada no sistema financeiro, por tanto, para que o usuário do TOTVS Educacional tenha permissão para alterar a data de vencimento dos boletos e/ou lançamentos é necessário habilitar a opção 'Alterar data de vencimento boleto' dentro do perfil associado ao seu usuário no sistema TOTVS Gestão Financeira.
