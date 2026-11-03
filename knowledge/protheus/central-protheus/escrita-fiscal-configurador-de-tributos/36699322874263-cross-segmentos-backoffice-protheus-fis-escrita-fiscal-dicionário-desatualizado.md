---
article_id: 36699322874263
category: Escrita Fiscal - Configurador de Tributos
content_hash: fbd0ec8ac73ba96af329de17fc8545281e0099a71d2f1c84d86fdc05570e6034
fetched_at: '2026-06-28T22:39:17.630427+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Escrita Fiscal - Dicionário desatualizado,
  favor verificar atualizações do motor de cálculo fiscal
type: support-article
updated_at: '2025-12-01T18:47:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36699322874263-Cross-Segmentos-Backoffice-Protheus-FIS-Escrita-Fiscal-Dicion%C3%A1rio-desatualizado-favor-verificar-atualiza%C3%A7%C3%B5es-do-motor-de-c%C3%A1lculo-fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36699322842903) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao acessar o Configurador de de Tributos (**FISA170**) e clicar na aba "**Tabela cClassTrib-IBS/CBS**" ocorre a mensagem:

**Dicionário desatualizado, favor verificar atualizações do motor de cálculo fiscal.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/36699382900247)**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.2410**  
  
**Causa**  
O incidente ocorre ao não possuir a tabela **CKB** no dicionário de dados do seu ambiente.  
  
**Solução**

**1** - Aplique a **expedição contínua** abaixo de acordo com sua versão **Protheus**:

<https://tdn.totvs.com/pages/releaseview.action?pageId=525823851#issues-17>

**2** - Descompacte o arquivo baixado e adicione o arquivo "**sdfbra**" na pasta **systemload** do seu serviço.

**3** - Execute o **UPDDISTR** e garanta que a CKB foi criada no banco de dados.

Após isso, reinicie os serviços e faça novos testes.
