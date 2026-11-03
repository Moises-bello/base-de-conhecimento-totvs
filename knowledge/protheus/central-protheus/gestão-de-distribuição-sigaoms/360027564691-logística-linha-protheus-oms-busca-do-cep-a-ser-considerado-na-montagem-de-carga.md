---
article_id: 360027564691
category: Gestão de Distribuição (SIGAOMS)
content_hash: f6d2c1b88a1faa9b36064e16777185cfcf723e1b390464fc514d3d4fa1876af9
fetched_at: '2026-06-28T22:45:49.542966+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Busca do CEP a ser considerado na Montagem
  de Carga
type: support-article
updated_at: '2025-05-24T13:07:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027564691-Log%C3%ADstica-Linha-Protheus-OMS-Busca-do-CEP-a-ser-considerado-na-Montagem-de-Carga
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19205868263575)** Tempo aproximado para leitura: **00:01:48 min** **Dúvida**Como o Sistema realiza a busca do **CEP** a ser considerado na **Montagem de Carga - OMSA200**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões.  
  
**Solução**O cadastro de **Clientes - MATA030** possui mais de um campo que armazena a informação de **CEP.**  
No **SIGAOMS**, a **busca do CEP** a ser considerado para trazer a rota correta durante a montagem de uma carga, ocorre de acordo com a configuração adotada para o parâmetro **MV\_ROTCEP**, sendo:  
 **Valor 1** - Considera apenas o **CEP** padrão do cadastro do cliente, campo **CEP - A1\_CEP**;  
**Valor 2** - Prioriza o **CEP de Entrega**, campo **Cep Entr - A1\_CEPE**. Caso não tenha sido informado um **CEP** de entrega,  considera o campo **CEP - A1\_CEP** padrão do cadastro do cliente;  
**Valor 3** - Considera apenas o **CEP de Entrega**, campo **Cep Entr - A1\_CEPE**.  
  
Exemplo de utilização:  
  
No cadastro de **Clientes - MATA030**, o **CEP** é a forma de diferenciar o **Endereço Principal** do **Endereço de Entrega**. Utilize os campos abaixo:

* **CEP - A1\_CEP** : Endereço Principal
* **Cep Entr - A1\_CEPE**: Endereço de Entrega

Ao utilizar o parâmetro **MV\_ROTCEP igual a 1**, será apresentado o **CEP do Endereço Principal**, segue resultado na **Montagem de Carga**:

![exemplo 1.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/19209000212631)

Ao utilizar o parâmetro **MV\_ROTCEP igual a 2**, será apresentado o **CEP do Endereço de Entrega**, segue resultado na **Montagem de Carga**:

![exemplo 2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/19209000252695)

**Saiba mais**Mais informações poderão ser acessadas no *link* [Montagem de Carga - OMSA200](https://tdn.totvs.com/pages/viewpage.action?pageId=551446517)   
  
**Glossário****CEP** - Código de Endereçamento Postal  **SIGAOMS** - Gestão da Distribuição
