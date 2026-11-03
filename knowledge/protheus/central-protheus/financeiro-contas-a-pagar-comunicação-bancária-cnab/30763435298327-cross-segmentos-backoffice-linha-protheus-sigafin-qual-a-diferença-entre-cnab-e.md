---
article_id: 30763435298327
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 457e4e20dc4897762c7b81ba9a66e9a08b315f66a9b4b460f59048ed4a42bb93
fetched_at: '2026-06-28T22:37:55.080550+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Qual a diferença entre
  CNAB e API
type: support-article
updated_at: '2026-01-07T18:49:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30763435298327-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Qual-a-diferen%C3%A7a-entre-CNAB-e-API
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30763450957207) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Qual a diferença entre CNAB e API?   
  
**Ambiente**  
[Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – Todas as versões  
  
**Solução**

O **CNAB** e a **API** possuem o mesmo objetivo, porém apresentam configurações e processos distintos.

**Comunicação Bancária CNAB**

Trata-se de um recurso da **FEBRABAN** que viabiliza a transferência de informações bancárias entre instituições financeiras e sistemas de pagamento.

No **Protheus**, o **CNAB** refere-se ao envio de títulos para o banco por meio de arquivos de remessa. Após a validação das informações, o banco gera um arquivo de retorno com os dados atualizados dos registros, os quais são utilizados para realizar a baixa no sistema. Contudo, no padrão do **Protheus**, **o boleto não é gerado**; essa operação é realizada exclusivamente pelo sistema bancário.

**Documentação**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Principais configurações e dúvidas para uso do CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7778595184407-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Principais-configura%C3%A7%C3%B5es-e-d%C3%BAvidas-para-uso-do-CNAB)

**Comunicação Bancária API**

A **API** é um conjunto de protocolos e ferramentas que permite a comunicação entre diferentes sistemas de software, com transações realizadas em tempo real e de maneira automatizada.

A **API de Cobrança** executa todas as funções desempenhadas por um **CNAB de cobrança**, porém de forma automática por meio de um **JOB**, eliminando a necessidade de enviar e importar o arquivo do banco.

Através do processo da **API**, **o boleto é gerado diretamente no** **Protheus** por intermédio do **novo painel gestor**.

**Documentação**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - Envio Boleto Online API](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17858265704727-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Envio-Boleto-Online-API)

**Importante**

A **API de retorno** está disponível até o momento apenas para o **Banco do Brasil**. Para os demais bancos, o retorno será realizado por meio do **CNAB**.

**Saiba mais**

[Contas a receber (Comunicação bancária online)](https://tdn.totvs.com/pages/releaseview.action?pageId=612548392)

[Comunicação bancária CNAB](https://tdn.totvs.com/display/public/PROT/CNAB)
