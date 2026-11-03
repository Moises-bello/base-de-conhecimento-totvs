---
article_id: 360036282533
category: RH - Funcionários
content_hash: a84d39f8283dfd07bdf3349e561587c789264d05f3326ea1784b9a982829ff21
fetched_at: '2026-06-28T22:43:28.606320+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Não é possível selecionar mais de um Adicional
  no campo RA_ADTPOSE - Adicional por tempo de Serviço
type: support-article
updated_at: '2025-08-28T17:24:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036282533-RH-Linha-Protheus-GPE-N%C3%A3o-%C3%A9-poss%C3%ADvel-selecionar-mais-de-um-Adicional-no-campo-RA-ADTPOSE-Adicional-por-tempo-de-Servi%C3%A7o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31942172818711) Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida**Não é possível selecionar mais de um Adicional no campo RA\_ADTPOSE - Adicional por tempo de Serviço  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Isso ocorre normalmente por conta do tamanho do campo RA\_ADTPOSE. Para ajustar, realize os seguintes passos:  
  
1. Acesse o programa **SIGACFG > Base de Dados > Dicionário > Arquivos**;  
2. Localize a tabela **SRA**, busque pelo campo **RA\_ADTPOSE** e clique em **Editar**;  
3. Ajuste as configurações do campo, principalmente o tamanho, seguindo as configurações abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31942203564439)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31942172821527)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31942203574551)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31942172822551)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31942172824343)  
  
4. Após ajustar as configurações, clique em **Salvar**;  
5. Clique em **Confirmar** - ![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046754114)  
6. Clique em **Atualizar base de dados** - ![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046754314)  
7. Avance as telas para que o sistema efetive o ajuste.  
  
Após esse processo, poderá selecionar mais de uma opção neste campo, no cadastro do funcionário.  
  
**Saiba mais:**

[RH - Linha Protheus - GPE - Como adicionar campos na visualização do Browse na rotina Cadastro de Funcionários - GPEA010](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004088522-RH-Linha-Protheus-GPE-Como-adicionar-campos-na-visualiza%C3%A7%C3%A3o-do-Browse-na-rotina-Cadastro-de-Funcion%C3%A1rios-GPEA010)  
[RH - Linha Protheus - GPE - Tamanho do campo de Descrição da Função - RJ\_DESC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407267796247-RH-Linha-Protheus-GPE-Tamanho-do-campo-de-Descri%C3%A7%C3%A3o-da-Fun%C3%A7%C3%A3o-RJ-DESC)

[RH - Linha Protheus - GPE - Configuração para que determinados usuários possam visualizar ou não um campo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059356113-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-para-que-determinados-usu%C3%A1rios-possam-visualizar-ou-n%C3%A3o-um-campo)
