---
article_id: 360036232713
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 5247484172563ad0bb9cdb33be19b0f02efdd47a82641a01d02fc35fee2ca637
fetched_at: '2026-06-28T22:42:45.889768+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Requisitar componentes em operação
  específica
type: support-article
updated_at: '2022-08-18T16:44:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036232713-Manufatura-Linha-Protheus-SIGAPCP-Requisitar-componentes-em-opera%C3%A7%C3%A3o-espec%C3%ADfica
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)* Tempo aproximado para leitura: **00:01:22 min****Dúvida**É possível requisitar componentes em operações específicas?   
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**Por meio do **PCPA200 - Estrutura (nova Versão)** ou do **MATA637 - Operações x Componente** é possível vincular cada **componente** a uma **operação** do **roteiro**. Desse modo, ao realizar o apontamento de uma **operação** através do **MATA681 - Produção PCP Mod2** ou do **MATA680 -** **Produção PCP Mod1**, o Sistema realiza a requisição dos materiais vinculados àquela **operação**.  
  
Para realizar a amarração no **PCPA200**:

1. Acesse o **PCPA200** ;
2. Selecione o **produto** e clique em **Outras Ações > Operação x Componente**;
3. Informe o roteiro;
4. Clique em **Alterar**;
5. Informar a **operação** e o **Componente**;

Para realizar a amarração no **MATA637**:

1. Acesse o **MATA637**;
2. Clique em **Incluir**;
3. Informe o **produto** e o **roteiro** nos respectivos campos;
4. Informe a **operação** e o **componente** que serão relacionados.

**Importante**  
Caso a operação não esteja relacionada a nenhum componente, o componente será requisitados apenas na última operação do roteiro.
