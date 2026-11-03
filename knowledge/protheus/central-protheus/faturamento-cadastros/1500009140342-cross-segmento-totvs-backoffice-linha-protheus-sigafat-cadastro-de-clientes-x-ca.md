---
article_id: 1500009140342
category: Faturamento - Cadastros
content_hash: 6eaf81cea73932b84638cc494a4032166127a15fdfc4fa0f9f1f19677583c26b
fetched_at: '2026-06-28T22:38:35.246877+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Cadastro de
  Clientes x CAROL (Integração via API)
type: support-article
updated_at: '2024-07-11T12:10:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009140342-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Cadastro-de-Clientes-x-CAROL-Integra%C3%A7%C3%A3o-via-API
---

**Dúvida**Como funciona a integração via **API da Carol** com a rotina de Cadastro de Clientes ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento - A partir da versão 12  
  
**Solução**A integração API entre o Cadastro de Clientes e a CAROL, visa facilitar o processo do cadastramento dos Clientes no Protheus®. Os campos básicos/obrigatórios padrões do Cadastro de Clientes são preenchidos automaticamente.

Para isso é necessário:

* Parâmetro **MV\_APICCGC**
* Gatilho no campo **A1\_CGC** no **Dicionário de Dados de Gatilhos** (**SX7**) que será o responsável por executar a integração API com a CAROL. Este gatilho, mesmo criado no ambiente, somente terá efeito se o novo parâmetro **MV\_APICCGC** estiver configurado como ativo (**.T.**).
* Para o correto funcionamento da API é necessário **liberar o endereço** (**https://app.carol.ai/api**) no **firewall** da rede.

Assista a gravação do evento realizado sobre esse tema: **<https://youtu.be/Wwm1Wab05dA>**

O pacote de Acumulados contendo o dicionário de Gatilhos está disponível em: **[Pacotes de Atualização - Faturamento](https://tdn.totvs.com/x/Iw4dHw)**

**Observações:**

**1 -** Para a atualização do fonte **APIFORCLI.PRW** para uso na integração , atualize com o **pacote de expedição contínua de FATURAMENTO com data a partir de 23/08/2021**, antes dessa data, o arquivo só constava no pacote de expedição contínua de Compras: **[Pacotes de Atualização - Compras](https://tdn.totvs.com/x/20EdHw)**

Em caso dúvidas do funcionamento da API Carol no Cadastro do Fornecedor, contate nossa equipe de Atendimento de Compras.

**2 -** A **API Carol** somente funciona para inclusão de Cadastro de Cliente **manualmente**, caso utilize **execauto** ou **Integração EAI** a API Carol **não irá funcionar**.

**Saiba mais**:

* **[DSERFAT-19186 DT Cadastro de Clientes x CAROL (Integração via API)](https://tdn.totvs.com/x/UcBRIw)**
* **[Integração TOTVS API CAROL - Preenchimento automático do cadastro de Fornecedor](https://tdn.totvs.com/x/E7CuIg)**
* **[Cross Segmentos - Backoffice Protheus - Faturamento - Integração Carol com Cadastro de Clientes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4430116320151-Cross-Segmentos-Backoffice-Protheus-Faturamento-Integra%C3%A7%C3%A3o-Carol-com-Cadastro-de-Clientes-?source=search)**
