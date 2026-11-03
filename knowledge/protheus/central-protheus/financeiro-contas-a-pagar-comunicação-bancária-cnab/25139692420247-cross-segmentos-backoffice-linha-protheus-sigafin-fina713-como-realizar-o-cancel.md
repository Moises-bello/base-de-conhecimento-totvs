---
article_id: 25139692420247
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 3a41e1158a17b9deb7868e124b26afd592b3b5aa095bc822793288746498362f
fetched_at: '2026-06-28T22:37:56.317528+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - Como realizar
  o cancelamento do boleto
type: support-article
updated_at: '2025-05-20T17:21:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25139692420247-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Como-realizar-o-cancelamento-do-boleto
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25139905993495)** Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**  
Como realizar o cancelamento do boleto?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Importante**

Apenas os bancos Banco do Brasil e Itaú permitem o cancelamento. Para outros bancos, é necessário remover o título do borderô e cancelar o boleto através do site do banco correspondente.

**Solução**

Para cancelar o boleto, é necessário remover o título do borderô através da rotina de **Manutenção de** **Borderô** (**FINA590**). Após remover o **título do borderô**, será registrado um novo registro na tabela **FI2** com os campos **FI2\_BORAPI** = S e **FI2\_OPEAPI** = A

Ao executar o job **FINA713**, o cancelamento será transmitido, poderá acompanhar o status por meio do **Monitor de Boletos com Pendências - FINA710**.

![Gravar_2024_07_24_15_10_39_169.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/25139683153687)

**Importante**

O título não pode ser excluído até que o banco registre a ocorrência de cancelamento. Enquanto isso, será exibida a seguinte mensagem:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25965531832855)

Ressalta-se que para cada banco é estipulado um prazo específico para a aceitação do cancelamento.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25965554491031)**

No entanto, a ocorrência pode ser excluída para permitir a exclusão da nota fiscal, sendo necessário realizar o processo de estorno do boleto diretamente no site do banco.

**Importante**

**É necessário aguardar um prazo de 30 minutos a até 24 horas, conforme o banco, para o envio das instruções de cobrança.**  
Esse intervalo se deve à existência de uma fila de transmissões e à solicitação dos próprios bancos, que requerem esse tempo para realizar os ajustes necessários nos boletos já transmitidos.

Exemplo:

* **Banco do Brasil:** exige um intervalo mínimo de **30 minutos** entre alterações e cancelamentos dos títulos já enviados.
* **Banco Itaú:** requer um intervalo de **24 horas** para alterações e cancelamentos dos títulos previamente transmitidos.

Referente ao demais banco validar no manual do banco o prazo para receber o retorno do cancelamento.

**Saiba mais**

[Contas a receber (Comunicação bancária online) - FINA713](https://tdn.totvs.com/pages/releaseview.action?pageId=612548392#Contasareceber(Comunica%C3%A7%C3%A3obanc%C3%A1riaonline)-Altera%C3%A7%C3%A3o/cancelamentodeboletosareceber)

[SIGAFIN - FINA590 - Manutenção de títulos em borderô](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028291032-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA590-Manuten%C3%A7%C3%A3o-de-t%C3%ADtulos-em-border%C3%B4)

[Monitor de Boletos com Pendências - FINA710](https://tdn.totvs.com/pages/releaseview.action?pageId=619123545#A%C3%A7%C3%B5es-passo2)
