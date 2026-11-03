---
content_hash: 2ef474ef16a0177158c79ee328c388dd2e2f24a0c800628faf57f85238ccd16d
fetched_at: '2026-06-29T00:11:38.768739+00:00'
page_id: '784778381'
product: rm
source: tdn-rm
title: Alteração da Data de Vencimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=784778381
version: 8
---

A funcionalidade "Alterar Data de Vencimento", localizada no menu 'Processos - Manutenção de Boletos', visa definir uma nova data de vencimento para o boleto e os lançamentos vinculados a ele.

Existem algumas regras no sistema que não permite o usuário alterar a data de vencimento do boleto. São elas:

* Boletos com QRCode PIX gerado e em processo de pagamento;
* Boletos com status diferente de "Em aberto" e "Parcialmente Baixado";
* Boletos baixado parcialmente e com código de barras gerado;
* Boletos com status de remessa diferente de "Não remetido", "Recusado", "Pendente de Remessa".
* Boletos com status de remessa PIX diferente de "Não remetido", "Recusado" e "Pendente de Remessa";

Será permitido alterar a data de vencimento para boletos com status "Registrado online" no qual o Banco possui um serviço de alteração da data de vencimento para boleto registrado. Caso seja um boleto não parcial cujo código de barras seja gerado baseado no valor líquido ou parcial, não será possível alterar a data de vencimento caso o valor calculado para o boleto na nova data seja diferente do atual. Os Bancos que possuem o serviço e que estão homologados pelo TOTVS Gestão Financeira são:

* Itaú (modelo API Cash v2)
* Banco do Brasil (modelo v2)
* SICOOB (modelo v2)
* CREFISA (AutBank)
* Santander (modelo v2)

### Parâmetro "Alterar Data do Prazo Limite de Pagamento"

Caso no momento do registro online do boleto tenha sido definido o prazo limite para pagamento através do layout de registro online, então será necessário marcar esse parâmetro para que o prazo limite de pagamento também seja prorrogado conforme o vencimento.

Esse parâmetro só será visível para os bancos abaixo que possuem o serviço e que estão homologados pelo TOTVS Gestão Financeira:

* SICOOB (modelo V2)

**Observação: Para os bancos que permitem alterar online o vencimento e prazo limite, pode ser que essa alteração ocorra de 15 a 20 minutos para ser registrada na Câmara Interbancária de Pagamentos CIP, com isso, caso tente pagar antes desse tempo, pode ser que a data de vencimento e prazo limite estejam com as datas antigas.**
