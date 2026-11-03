---
content_hash: f3e03f8186aae78dfcdaa7a4f33d9731c7b722f8dddb2967ea16f4a29aa3d33b
fetched_at: '2026-06-29T00:11:32.741162+00:00'
page_id: '747326475'
product: rm
source: tdn-rm
title: CERC - Contrato - Cessão de Direito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=747326475
version: 5
---

Ao efetuar uma cessão de direito para o contrato, quando o processo de enviar os dados para a registradora for executado, será verificado se o empreendimento já foi certificado (Finalizado/Registrado) e se a renegociação foi efetuada no mesmo mês/ano que o processo está sendo executado e ainda não foi enviado as informações do aditivo.

**Regras definidas para o envio:**  
   1 - Empreendimento deve estar ativo na base da CERC.  
   2 - Aditivo tem que ter ocorrido no mesmo Mês/Ano da execução do processo de integração.  
   3 - Cessão de Direito é a ultima do mês e ainda não foi enviado para a CERC.

Ao enviar um contrato que sofreu cessão de direito para a cerc, será enviado um Json com o campo tipoOperacao igual a "AC" e o campo idCercContratoSubAt com o valor do contrato que será substituido no portal da CERC.   
No entanto, o TCGI não gera um novo contrato para substituir o anterior, com isso, será enviado neste campo o mesmo código do contrato que teve a cessão de direito efetuada e para que seja gerado um novo contrato no sistema da certificadora o campo referenciaExternaContrato com o valor da "coligada-numeroContrato-numeroAditivoCessao" para que na CERC possa ser identificado como um novo contrato, mas para o TCGI o contrato continua o mesmo.

As parcelas serão todas canceladas para o contrato de cessão de direito e as novas parcelas serão enviadas para o contrato com o novo código.
