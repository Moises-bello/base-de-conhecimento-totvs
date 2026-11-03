---
article_id: 360022787972
category: RH - Contabilização
content_hash: c93b1860c7ba5ed158ad91156b7f14487b0fe02b8df1615acd01d94303421d9f
fetched_at: '2026-06-28T22:43:46.031133+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Processo de Contabilização da rotina GPEM110 gerando
  apenas totalizadores e não movimentando dados da SRZ para a CT2
type: support-article
updated_at: '2025-07-31T19:04:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022787972-RH-Linha-Protheus-GPE-Processo-de-Contabiliza%C3%A7%C3%A3o-da-rotina-GPEM110-gerando-apenas-totalizadores-e-n%C3%A3o-movimentando-dados-da-SRZ-para-a-CT2
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33856732985239)** Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**Ao solicitar geração do processo de **Contabilização** de folha de pagamento e provisão através da rotina **GPEM110**, o sistema cria apenas informações de totalizadores na tabela **SRZ**, não demonstrando informações por matrículas ou centros de custos e não gerando dados na tabela **CT2****Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Causa**Configuração incorreta na estrutura **SX2** referente ao compartilhamento das tabelas envolvidas no processo de **Contabilização**.  
  
**Solução**Para solucionar essa ocorrência, seguir os passos abaixo:  
1. Acessar via **Configurador**, **Base de Dados**, as tabelas: **SRA**, **SRC** e **SRD**;  
2. Ajustar o modo de compartilhamento das tabelas para exclusivo por **Empresa**, **Unidade de Negócio** e **Filial**;  
3. Realizar tratamento dos dados gravados sem que estão sem o campo filial preenchido;  
4. Validar processo de **Contabilização**.

Segue compartilhamento das tabelas:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068196433)  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068194793)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067125674)  
  
  
**Saiba Mais**  
[Artigos Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)
