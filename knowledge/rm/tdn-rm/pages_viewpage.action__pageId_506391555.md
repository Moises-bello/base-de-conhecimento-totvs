---
content_hash: 063f485b76afe8e15430474521a1adb26307913153acc0b9aa2c69d9d8f6e30d
fetched_at: '2026-06-29T00:10:25.897166+00:00'
page_id: '506391555'
product: rm
source: tdn-rm
title: Lançamento Fiscal (Anexo Evento Periódico)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=506391555
version: 12
---

O eventos com origem dos Lançamentos Fiscais são:

* **R-2010** – Retenção Contribuição Previdenciária - Serviços Tomados;
* **R-2020** – Retenção Contribuição Previdenciária - Serviços Prestados;
* **R-2050** – Comercialização da Produção por Produtor Rural PJ/Agroindústria;
* **R-4010** – Pagamentos/Créditos a Beneficiário Pessoa Física;
* **R-4020** – Pagamentos/Créditos a Beneficiário Pessoa Jurídica;
* **R-4080** – Retenção no Recebimento;

Para os eventos cuja a origem dos dados é o Lançamento Fiscal, no anexo serão apresentados os seguintes campos:

* Série;
* Número do Documento;
* Cliente/Fornecedor;
* Código da Filial do Lançamento;
* Data de emissão;

Em lançamentos que possui mais de um tributo que referem-se a eventos diferentes, será apresentado no anexo de cada evento, "Origens do Evento", o lançamento de origem, ou seja, será apresentado o mesmo lançamento nos anexos dos eventos correspondentes. Segue exemplo:

Exemplo

No exemplo abaixo o evento R-2010 possui como origem dois lançamentos 443322 e 443321, no segundo print é possível verificar que o evento R-4020 também possui como origem os mesmos lançamentos 443322 e 443321. Esse cenário ocorre pois os lançamentos possuem os tributos INSS (no item) correspondente ao evento R-2010 e o tributo IRRF-PJ (no lançamento) correspondente ao evento R-4020.
