---
content_hash: 29b07ade9115349ba86b9da83b9f29560ba2d90e8b8bd32ec6d7bab2a7647d02
fetched_at: '2026-06-29T00:11:32.739284+00:00'
page_id: '747324212'
product: rm
source: tdn-rm
title: CERC - Contrato - Aditivo Renegociação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=747324212
version: 5
---

Ao renegociar um contrato, quando o processo de enviar os dados para a registradora for executado, será verificado se o empreendimento já foi certificado (Finalizado/Registrado) e se a renegociação foi efetuada no mesmo mês/ano que o processo está sendo executado e ainda não foi enviado as informações do aditivo.

**Regras definidas para o envio:**  
   1 - Empreendimento deve estar ativo na base da CERC.  
   2 - Aditivo tem que ter ocorrido no mesmo Mês/Ano da execução do processo de integração.  
   3 - Renegociação é a ultima do mês e ainda não foi enviado para a CERC.  
  
Atendendo ao critério descrito acima, será enviado os dados no formato Json e o campo tipoOperacao será "AR", onde na plataforma da CERC poderá ser visualizado este contrato com a informação da data de renegociação e as parcelas do fluxo sendo todas canceladas e um novo fluxo de pagamento para o contrato com as parcelas que possam ter permanecido e as novas parcelas constando como aberta para o pagamento. As parcelas já quitadas permanecem sem nenhuma alteração.
