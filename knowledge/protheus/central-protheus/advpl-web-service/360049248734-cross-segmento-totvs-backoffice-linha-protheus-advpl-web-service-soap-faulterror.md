---
article_id: 360049248734
category: ADVPL - Web Service
content_hash: 42bfeb0e9f7e1145f8b3cc004304065b035db684fbb5fc88bdf7922c7fcc217b
fetched_at: '2026-06-28T22:40:10.325871+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Web service soap
  FaultError
type: support-article
updated_at: '2021-05-06T19:10:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049248734-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Web-service-soap-FaultError
---

**Dúvida**  
Quais variáveis ou funções que pode ser tratado para não dar a mensagem **FaultError**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas versões  
  
**Solução**Não é possível disponibilizar funções ou variáveis que tratam a mensagem **FaultError**, uma vez que é definido o objeto de entrada em um ***WebService*****Soap** padrão a informação do **XML** recebido é validada, pois é necessário garantir a integridade do serviço.  
Neste caso pode criar uma estrutura que recebe uma string no formato **XML**, e a validação deste conteúdo passa a ser do cliente. Um exemplo deste tipo de utilização é o serviço do *ea* (*eaiservice*). Ele possui um único atributo de entrada (***inMsg***) que recebe uma string no formato **XML**, e é validado internamente.  
Também pode criar um **WS** **REST**, recebendo qualquer tipo de parâmetro e tratando internamente.
