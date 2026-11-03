---
article_id: 1500004222161
category: Inspeção de Entradas (SIGAQIE)
content_hash: c715768beeafbe7733f44ba88058c8ea9498bb939a4a80b01a989da531e5bbda
fetched_at: '2026-06-28T22:42:26.875639+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Armazém 98
type: support-article
updated_at: '2025-06-04T21:05:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004222161-Manufatura-Linha-Protheus-SIGAQIE-Armaz%C3%A9m-98
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32594754566679)** Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**Para qual armazém é enviado o produto que possui integração com o módulo **SIGAQIE - Inspeção de Entradas**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Todas as versões  
  
**Solução**Quando o produto possui integração com o **SIGAQIE**, ou seja, quando na rotina **MATA010 - Cadastro de Produtos** na aba **CQ** o campo **Tipo de CQ** está como **Q - SigaQuality** é verificado qual é o armazém informado no parâmetro **MV\_CQ - Local(Almoxarifado) Controle de Qualidade**. Se o parâmetro estiver em branco, é considerado o armazém padrão da **Qualidade**, sendo o código **98**.  
Também não é possível que para um mesmo produto, independente da parametrização, com integração com o **SIGAQIE**, para determinado documento de entrada enviar para o armazém **01**, por exemplo, e em outros documentos, para o armazém **98**.  
Existindo integração com o **SIGAQIE**, sempre será enviado para o armazém **98**, e no momento da **Baixa de CQ** pela rotina **QIEA215 - Inspeção de Resultados**, é transferido para outro armazém.  
  
**Observação**  
Quando há registro na **MATA103 - Documento de Entradas** e o **Local** informado for **igual** ao conteúdo do parâmetro **MV\_CQ**, no momento da movimentação (transferência) na rotina **QIEA215 - Resultados**, na aba **Baixa do CQ**, irá trazer o **armazém padrão** cadastrado na rotina **MATA010 - Produto**. Caso o conteúdo entre **Local** e **MV\_CQ** seja **diferente**, irá **respeitar o armazém cadastrado na rotina MATA103.**
