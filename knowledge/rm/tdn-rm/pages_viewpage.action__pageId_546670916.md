---
content_hash: 373196c0370e2e7f1450ba8a33d9100c8b88398ef36713ed6423b9e8b9f2432f
fetched_at: '2026-06-29T00:10:41.777819+00:00'
page_id: '546670916'
product: rm
source: tdn-rm
title: Código de Cálculo 436 - ATESTADO MÉDICO DE AFASTAMENTO POR COVID-19
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546670916
version: 3
---

Evento do tipo Base de Cálculo, sem nenhuma incidência.

No Parametrizador, pasta Folha Normal/Afastamento, deve ser informado "Motivo de afastamento por Covid 19".

Quando o afastamento for do tipo P e com o mesmo motivo informado no Parametrizador, esse código de cálculo será lançado no envelope.

O CC 436 será lançado automaticamente junto com os CC's 1 ou 2 ou 145 e deve considerar somente o afastamento por Covid-19, já o “Código de cálculo 145 - Atestado Médico Afastado por Previdência” deve considerar todos.

Esse evento com o CC 436 que será lançado no envelope de pagamento será considerado para eSocial, GPS e SEFIP. 

O valor do CC 436 será limitado ao teto máximo da tabela de INSS.

**Observações:**

* Se o afastamento iniciar em um mês e terminar no mês seguinte, o CC 436 considerará somente os dias da competência atual.
* Se o valor total ultrapassar o teto máximo, no segundo mês será lançado o complemento que falta para atingir o teto.

**Exemplo de lançamento do evento com código de cálculo 436**  
Informado o motivo "01 - Afastamento por COVID-19" no Parametrizador | pasta Folha Normal/Afastamento;  
Funcionário afastado pelo Tipo ‘P' e motivo 01 - Afastamento por COVID-19;  
No envelope de pagamento será lançado o evento tipo base código de cálculo 436 – Atestado Médico de Afastamento por COVID-19, criado previamente.

---

Códigos de Cálculo
