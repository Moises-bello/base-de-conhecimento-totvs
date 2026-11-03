---
article_id: 29119319340311
category: Financeiro - Conciliador Backoffice
content_hash: 8819f2dae5d96b6c773bb4dc4add305c95b2e795871c928a84c98ad54570be52
fetched_at: '2026-06-28T22:37:47.069175+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - CTBA940 - Conciliação Automática
  efetivar tarifa bancária
type: support-article
updated_at: '2025-03-19T19:09:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29119319340311-Cross-Segmentos-Backoffice-Linha-Protheus-CTBA940-Concilia%C3%A7%C3%A3o-Autom%C3%A1tica-efetivar-tarifa-banc%C3%A1ria
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29119319312535) Tempo aproximado para leitura: **00:08 min****Dúvida**Como adicionar tarifas bancarias na conciliação automática?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - 12.1.2210  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

A efetivação é o procedimento de incluir um movimento bancário que está presente no extrato, mas que não está registrado no sistema bancário.  
Normalmente utilizado em **tarifas, imposto sobre transações financeiras (IOF) e outros**.

Clicar em **Ações → Efetivação**, uma janela será aberta com as informações de natureza, histórico e informações contábeis do movimento que está sendo criado.

![Gravar_2025_01_10_13_59_51_472.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/29124963216919)

Após validar o procedimento de Efetivação, teremos:

Registro das transações bancárias nas tabelas do sistema (FK5/SE5);  
Transferência dos dados para a pasta Dados da Conciliação, utilizando o tipo de correspondência Manual.

```
Atenção  
Este processo permite que vários registros sejam selecionados e efetivados com apenas uma   
ação. Caso tenha selecionado 2 registros na tabela de extratos (SIG) e confirmar a   
efetivação, serão gerados 2 registros nas tabelas Movimentos Bancários (FK5).  
  
Neste momento, os registros estão preparados para a conciliação, ou seja, existe um   
registro na Tabela de Extratos (SIG) e um registro nas tabelas de Movimentação Bancária   
(FK5) com match. Apenas ao clicar no botão Aplicar Conciliação (canto superior direito  
 da tela) é que o processo de conciliação será gravado efetivamente.
```

* **Cancelar efetivação**

O processo de Cancelar Efetivação é o processo de excluir os movimentos bancários efetivados através do processo de Efetivação.  
Ao selecionar um ou mais registros e clicar no botão Ações → Cancelar Efetivação, o processo cancelará os movimentos efetivados nas tabelas de Movimentação Bancária do sistema (FK5/SE5).

```
Atenção  
  
Esse processo não permite que registros que já estavam no sistema anteriormente e   
realizados por outros processos (movimento bancário manual, baixas, etc.) sejam excluídos.
```

Caso o registro se encontre na aba Dados da Conciliação, basta:

* Posicionar sobre o registro desejado, clicar em (à esquerda na aba, dados da Conciliação)
* Ao se abrir uma caixa de opções, clicar em Cancelar Match.

![Gravar_2025_01_10_14_00_42_419.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/29124963222935)

Após esta ação, os registros terão seus matches cancelados e retornarão para a aba Dados não encontrados, permitindo a aplicação do processo de Cancelar Efetivação

**Saiba mais**

[Conciliador BackOffice - Conciliação Bancária Automática](https://tdn.totvs.com.br/pages/releaseview.action?pageId=753654798)
