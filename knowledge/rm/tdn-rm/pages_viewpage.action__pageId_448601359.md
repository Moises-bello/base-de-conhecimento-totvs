---
content_hash: 6758f2a5b2260eb9af1a7aa43e07347e4acfc209b944f0e3352b7a236186b7d0
fetched_at: '2026-06-29T00:09:55.644018+00:00'
page_id: '448601359'
product: rm
source: tdn-rm
title: 4562810 PORTALMOBILE01-6434 DT Mensagem de envio de e-mail após inscrição no
  processo seletivo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=448601359
version: 1
---

# Mensagem de envio de e-mail após inscrição no processo seletivo

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | TOTVS Educacional |
| **Módulo:** | Processo Seletivo |
| **Função:** | Inscrição |
| **Situação/Requisito:** | Cliente informa que, após a finalização de uma inscrição no processo seletivo, a mensagem "Mais detalhes foram enviados para o e-mail:..." é exibida, mesmo sem um e-mail de confirmação de cadastrado, isso está confundindo alguns responsáveis que estão ligando no colégio questionando o não recebimento do e-mail. Foi solicitado que a mensagem só apareça caso o sistema esteja parametrizado para realizar o envio de e-mail da confirmação de inscrição. |
| **Solução/Implementação:** | Foi realizado ajuste para tratar melhor a exibição da mensagem acima mencionada. Ficou definida a seguinte regra:  Caso exista o e-mail preenchido no formulário de inscrição, do candidato (ensino superior) ou do responsável pela inscrição (ensino básico), e o processo seletivo possua configuração para envio de e-mail de confirmação da inscrição (anexos - mensagens de notificação), então a mensagem mencionada pelo cliente será exibida ao final da inscrição. Caso essas condições não sejam atendidas, a mensagem não será exibida. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
