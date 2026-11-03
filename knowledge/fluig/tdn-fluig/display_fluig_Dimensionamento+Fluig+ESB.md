---
content_hash: 96d224185cdfd704490b5c02fff24060ff548625d564221dc94e337380a274a7
fetched_at: '2026-06-28T21:35:27.884095+00:00'
page_id: '6066522'
product: fluig
source: tdn-fluig
title: Dimensionamento Fluig ESB
type: documentation
url: https://tdn.totvs.com/display/fluig/Dimensionamento+Fluig+ESB
version: 12
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**. 

* O Fluig ESB é um produto que tem seu hardware dimensionado de acordo com a integração que está sendo utilizada.
* É necessário que o serviço do TOTVS ESB esteja em uma máquina dedicada sem outros serviços como ERP ou LS para que tenha o funcionamento correto.

Abaixo, segue um exemplo de **dimensionamento mínimo** para um servidor dedicado:

|  |  |  |
| --- | --- | --- |
| Memória RAM | 1.000 mensagens por hora. | 8 GB |
| 100.000 Mensagens por hora. | 16 GB |
| Processador | Bits | 64 Bits |
| Core | Mínimo 2 núcleos |
| Disco | Velocidade | Mínimo 7200 RPM |
| Taxa de transferência | Mínimo 1 Gb/s |
| Espaço requerido para instalação | 4 GB |
| Espaço requerido para banco de dados | O espaço em banco de dados é relativo ao número de mensagens e a configuração de limpeza do histórico. Consulte-nos. |

**Servidores virtuais - VM - não estão homologados para a execução do Fluig ESB.**

Para ambientes de **alta disponibilidade** ou **missão crítica**, a equipe de produto TOTVS deverá ser acionada através do e-mail: [esb@totvs.com.br](mailto:esb@totvs.com.br).
