---
article_id: 21039485236247
category: Originação de Grãos (OG)
content_hash: 17dc31788314fc53bd03c2f40f6a4f9f385f3f96b9a281becd6d1b709d9087ef
fetched_at: '2026-06-28T22:45:38.997963+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Definição de uma tabela de serviços
type: support-article
updated_at: '2025-06-11T21:20:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21039485236247-Agro-Linha-Protheus-AGR-Defini%C3%A7%C3%A3o-de-uma-tabela-de-servi%C3%A7os
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21039485210903) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**  
No módulo **Comercialização (Linha Protheus) - Originação de Grãos (OG)**, ao realizar o processo para criar um **serviço** é apresentada a ocorrência **Definição de uma tabela de serviços**.  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Causa**  
Esse incidente ocorre, pois é preciso realizar o processo para criar um **serviço** no Sistema.  
  
**Solução**  
Para solucionar essa ocorrência, verifique a rotina na tabela de **Serviços - OGA135**, pois ela permite definir uma tabela de **serviço** com data de vigência, e vincular itens de serviços de armazenagem. Este registro da tabela de serviços é informado no contrato de **Deposito de Terceiro - OGA260**, que posteriormente conforme parametrização será usado para realizar os **Cálculos de Serviços - OGA262** de armazenagem que incidem sobre o contrato.  
Após cadastrar a tabela de **serviço OGA135** definindo o período em que ela estará ativa, é possível via opção do menu **Outras Ações - Serviços**, incluir um ou mais registros para os itens da **Tabela de Serviço OGA135I**.  
Entre os campos de parametrização podemos citar:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21039485212055)  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21039485212695)

O cadastro de serviços também permite definir tarifa por resultado de análise. Esses dados podem ser informados na tabela inferior do cadastro. Deve-se informar o código do desconto, a faixa % da **análise** e o **valor da tarifa** ou **percentual de retenção**.
