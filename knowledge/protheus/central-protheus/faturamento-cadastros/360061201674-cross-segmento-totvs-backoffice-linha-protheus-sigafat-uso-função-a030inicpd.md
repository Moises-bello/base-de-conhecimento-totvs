---
article_id: 360061201674
category: Faturamento - Cadastros
content_hash: 0aa4641ef5cb9a2f6220db44ff48a2dedb1dd0473bafba6b0dc21fc07337d7cc
fetched_at: '2026-06-28T22:38:35.374144+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT- Uso Função A030INICPD()
type: support-article
updated_at: '2022-09-20T20:29:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061201674-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Uso-Fun%C3%A7%C3%A3o-A030INICPD
---

**Dúvida**

Qual a finalidade de uso da Função **A030INICPD**(),pois ao colocá-la no inicializador do campo a1\_cod, o sistema não traz a numeração automática.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - todas as versões.  
  
**Solução**

**A030INICPD** - Trata a inicialização do campo **A1\_COD** com integração de **RM Classis.**

**MV\_RMCLASS:** Parâmetro de ativação da integração do Protheus x RM Classis Net (RM Sistemas).

Quando existir a integração do Protheus x RM Classis Net (RM Sistemas), o campo (Cod. do Cliente) não será mais editável. Será buscado o código sequencial na tabela de controle de numeração do RM Classis Net (RM Sistemas) através da função **M030PrRMCli()**.  
  
Ou seja, é um tratamento para o código do cliente caso exista integração com o RM Sistemas, o que depende da configuração do parâmetro **MV\_RMCLASS**, se você não tem esta integração,  a função terá efeito no seu processo.  
  
Por padrão, o código do cliente deve ser digitado manualmente, alguns clientes utilizam validações para trazer a próxima numeração automaticamente, como o uso do **GETSXENUM**, porém como o fonte não esta preparado para tratar essas validações pode ocorrer vários erros como pular numeração, chave duplicada e não trazer a próxima numeração.  
  
O procedimento orientado pela TOTVS é o de uso do ponto de entrada para criar uma validação de busca da numeração: **[CriaSXE - Controle de Numeração](https://tdn.totvs.com/pages/releaseview.action?pageId=6815179)**

**Saiba mais sobre controle de numeração :**

**[FAT0046 Ajuste de Numeração automática dos Formulários (Tabelas / ALIAS) no Protheus](https://tdn.totvs.com/pages/viewpage.action?pageId=235570751)**

**[FAT0049 Controle de Numeração de Documento de Saída no Protheus](https://tdn.totvs.com/pages/viewpage.action?pageId=329024579)**

**[Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Como utilizar a função GetSXENum](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018810731-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-utilizar-a-fun%C3%A7%C3%A3o-GetSXENum?source=search)**
