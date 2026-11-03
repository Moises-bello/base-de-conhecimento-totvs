---
article_id: 360049591434
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 2a5b9adaa364a0c11119e183e1d7d514a5160fa542f641672c8acf891e46c645
fetched_at: '2026-06-28T22:38:45.163636+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: MP - FAT - Desoneração - Criação da Tabela SV5
type: support-article
updated_at: '2021-04-28T15:13:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049591434-MP-FAT-Desonera%C3%A7%C3%A3o-Cria%C3%A7%C3%A3o-da-Tabela-SV5
---

**Dúvida**

Desoneração - Criação da Tabela SV5  
  
**Ambiente**

Microsiga Protheus -  todas as versões.  
  
**Solução**A tabela **SV5** será criada/alimentada após  rodar a rotina **GPEM013** (Ambiente Folha de Pagamento) mediante as informações e cadastros abaixo:

**1-Ambiente Faturamento**  
  
Notas Fiscais no período apurado (tabela **SF2**);  
  
**2- Ambiente Folha**  
  
***2.1 - Manutenção da Tabela S037:***

Verificar se o campo Filial está preenchido,se estiver em branco atenderá a todas as filiais, e se recolhe sobre o Faturamento.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074600414/mceclip2.png)  
  
***2.2-Cadastro de Períodos***

Verificar os períodos e se estão ativos.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075814693/mceclip3.png)  
  
***2.3-Rotina GPEM013***

Observar a ***Filial***, se a rotina Integra com o Faturamento e se está dentro do período.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074597894/mceclip0.png)  
***Importante*** :  
  
Para que não haja duplicidade na tabela SV5 é necessário que o campo V5\_ITEMNF possua tamanho 4  
  
Caso a Desoneração não seja gerada, verificar configurações e cadastro de matricula na Filial que não está gerando a Desoneração.  
  
O sistema considera movimentação de folha na Filial para poder validar a desoneração.  
  
Para dúvidas sobre configurações e cadastro de matricula na Filial, favor verificar com Suporte de Recursos Humanos - Folha de Pagamento.
