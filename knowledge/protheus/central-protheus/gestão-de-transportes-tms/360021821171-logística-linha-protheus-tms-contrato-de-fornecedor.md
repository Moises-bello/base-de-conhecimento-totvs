---
article_id: 360021821171
category: Gestão de Transportes (TMS)
content_hash: a191b9642577cd6338eee498067290fcb7c933389ae3e7d4bb92982bc097ad5f
fetched_at: '2026-06-28T22:45:27.591109+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Contrato de Fornecedor
type: support-article
updated_at: '2021-08-02T14:42:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021821171-Log%C3%ADstica-Linha-Protheus-TMS-Contrato-de-Fornecedor
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:40 min**

**Dúvida**Como preparar o processo para utilização de Contrato de Fornecedor?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Para utilização do processo de Contrato de Fornecedor, devemos executar os seguintes processos cadastrais:

* Cadastrar uma **Configuração de Tabela de Frete - TMSA130**, e definir:
  + Nome para a tabela de frete;
  + Selecionando a opção **2 - Frete a pagar** no campo **Categ. Tab DTL\_CATTAB**;
  + Selecionando o componente que deseja usar: No exemplo, usaremos um componente relacionado a peso da mercadoria.
* Cadastrar uma **Tabela de Frete a Pagar** - **TMSA790**, e apontar:
  + Tabela de frete cadastrada no item 1;
  + Origem e Destino da Prestação do Serviço de Transporte;
  + Na aba referente ao componente selecionado, informar o peso e valor;
  + Quando houver excedente, preencher até quantos kg deve ser cobrado o excedente, o valor acrescido e a fração, no caso Peso, que deve ser calculado, como no exemplo:

![](https://totvssuporte.zendesk.com/attachments/token/745TBPiwgiDnXEqujNB51AbMM/?name=inline992570027.png)

* Cadastrar a Fornecedor a ser utilizado no **MATA020 -  Cadastro de Fornecedores**.
* Criar um **Contrato de Fornecedor** - **TMSA800**, e vincular:
  + Fornecedor cadastrado **DUJ\_CODFOR**, **DUJ\_LOJFOR**;
  + Vigência do contrato **DUJ\_INIVIG**, **DUJ\_FIMVIG**;
  + Serviço de Transporte **DVG\_SERTMS;**
  + Tipo do Transporte **DVG\_TIPTRA**;
  + Tabela de Frete **DVG\_TABFRE**.
