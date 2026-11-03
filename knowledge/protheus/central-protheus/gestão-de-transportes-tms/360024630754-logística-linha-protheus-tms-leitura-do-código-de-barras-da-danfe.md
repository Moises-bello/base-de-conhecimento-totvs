---
article_id: 360024630754
category: Gestão de Transportes (TMS)
content_hash: 8ac61f46eb30eb65f3ef6274461032ef81e606bbe8209efb17b564d6d07e1823
fetched_at: '2026-06-28T22:45:29.383923+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Leitura do Código de Barras da DANFE
type: support-article
updated_at: '2022-06-20T14:43:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024630754-Log%C3%ADstica-Linha-Protheus-TMS-Leitura-do-C%C3%B3digo-de-Barras-da-DANFE
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:02:30 min**  
**Dúvida**Como carregar as notas fiscais importadas via **EDI - *Electronic Data Interchange***na inclusão de documentos?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Disponibilizada a melhoria na rotina **Entrada Dc.Cliente - TMSA050**, que permite realizar a inclusão do documento do cliente, por meio da Leitura do **Código de Barras da DANFE - Documento Auxiliar de Nota Fiscal Eletrônica**. O beneficio desta melhoria é a agilidade adquirida para realizar o cadastro de um Documento de Entrada do Cliente.  
  
Para utilizar a Leitura do **Código de Barras da DANFE**, é necessário que conste Notas Fiscais cadastradas no **EDI**:  
  
1. Em **Gestão de Transportes - SIGATMS**, acesse **Atualizações / EDI / Nota Fiscal - TMSAE55**.  
  
2. Clique em **Incluir**.  
  
3. Inclua uma nova Nota Fiscal e preencha o campo **Chave NF-e - DE5\_NFEID.**

**![lcb1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360037999094/lcb1.PNG)**

Com este campo preenchido, na Leitura do Código de Barras na **Entrada Dc.Cliente - TMSA050**, o Sistema consegue localizar a nota fiscal.  
  
4. Acesse **Atualizações / Recebimento / Entrada Dc.Cliente - TMSA050.**  
  
5. Clique em **Incluir**.  
  
6. Clique na opção **Outras Ações/ Leitura por Cod.Barras** ou pressione a tecla de atalho **F2**.

![lcb2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360037999194/lcb2.PNG)

7. Informe a Chave de **NF-e - Nota Fiscal Eletrônica**.  
  
8. O Sistema preenche automaticamente os demais campos de acordo com as informações presentes na Nota Fiscal.

![lcb3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360038840533/lcb3.PNG)

**Importante**  
A tela **Leitura por código de barras** fica disponível para inserir as demais notas fiscais no documento, porém os próximos documentos precisam possuir o mesmo Remetente e Destinatário.  
  
Caso seja disponibilizada uma **NF-e** com Remente ou Destinatário diferentes da primeira nota, o Sistema detecta e apresenta um *Help* informando o ocorrido.  
  
Ao colocar um número de **NF-e** inválido, o Sistema apresenta a mensagem: **Número de Documento não encontrado.**
