---
article_id: 360022074392
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: fa140640822ab7fff9ca71754d968f6968dee4778eddb0b95e73199533d90b68
fetched_at: '2026-06-28T22:41:48.322431+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - AO TENTAR EXCLUIR NOTA
  QUE ALIMENTA O ATIVO É APRESENTADA MENSAGEM AF240CLASS
type: support-article
updated_at: '2024-11-01T20:41:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022074392-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-AO-TENTAR-EXCLUIR-NOTA-QUE-ALIMENTA-O-ATIVO-%C3%89-APRESENTADA-MENSAGEM-AF240CLASS
---

**Dúvida**

Qual procedimento deve ser realizado ao apresentar alerta AF240CLASS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019249692)  
**Ambiente**  
Microsiga Protheus – ativo Fixo – A partir da versão 11.80

**Solução:**

Excluir uma nota fiscal de entrada que alimenta o CIAP e o Ativo Fixo

Mesmo que o bem não tenha sofrido apropriações, caso ele já tenha sido classificado no módulo Ativo Fixo (**SIGAATF**), a exclusão da nota fiscal ou do item na Manutenção CIAP (**MATA905**) e no Ativo Fixo não será permitida, sendo necessário os ajustes abaixo:

1. **Bens sem movimentações**:

   * Para bens que ainda não passaram por movimentações, como depreciação, baixas ou transferências, é possível realizar a desclassificação do item usando a rotina **ATFA240**, na opção "***Outras Ações > Cancelamento da Classificação***".
   * Após a desclassificação ser concluída, o sistema permitirá a exclusão da nota de entrada.  
       
     Veja detalhes da funcionalidade: [Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA240 - Cancelamento da classificação do bem](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006848432-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA240-Cancelamento-da-classifica%C3%A7%C3%A3o-do-bem)
2. **Bens com movimentações**:

   * Nos casos em que o bem já teve movimentações, é necessário primeiro realizar a baixa do bem no módulo Ativo Fixo. Esta ação atualizará automaticamente o item na Manutenção CIAP (MATA905), permitindo assim a exclusão desejada.

Saiba Mais: [Procedimento\_Realizado\_ao\_Apresentar\_Alerta\_AF240CLASS](https://tdn.totvs.com/display/public/PROT/CIA0013_Procedimento_Realizado_ao_Apresentar_Alerta_AF240CLASS)
