---
article_id: 360052624673
category: RH - Arquivos Bancarios
content_hash: 074a05d5722c4aaf2f3342a97d111d2cb30a3f1be51b1c407c495d9548f436b8
fetched_at: '2026-06-28T22:43:38.258555+00:00'
product: protheus
section_id: 360004833673
source: central-protheus
title: RH - Linha Protheus - GPE - Como conferir o resultado do Relatório de Líquidos
  quando utilizamos os totalizadores por Banco e por Filial/Unidade de Negócio/Empresa
type: support-article
updated_at: '2026-06-25T20:19:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052624673-RH-Linha-Protheus-GPE-Como-conferir-o-resultado-do-Relat%C3%B3rio-de-L%C3%ADquidos-quando-utilizamos-os-totalizadores-por-Banco-e-por-Filial-Unidade-de-Neg%C3%B3cio-Empresa
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32325843497367)**Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**  
Como conferir o resultado do Relatório de Líquidos quando utilizamos os totalizadores por Banco e por Filial/Unidade de Negócio/Empresa?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**  
**Cenário A -** Iremos utilizar como exemplo duas empresas diferentes - D MG 01,M SP 01

Na rotina **Líquidos - GPER020**, que pode ser acessada pelo menu **Relatórios** / **Periódicos,** ajuste no grupo de perguntas o item **Totaliza por Banco** igual a 'Sim'.

1. Formato - Analítico

   **Totalizar por Filial/Um.Neg/Empresa igual a ‘Sim**’:  
   Note que o direcionador da quebra foi a GESTÃO CORPORATIVA.  
     
   ![](https://tdn.totvs.com/download/attachments/556370738/image2020-7-22_10-29-20.png?version=1&modificationDate=1595425099550&api=v2)

   **Totalizar por Filial/Un.Neg/Empresa igual a ‘Não**’:  
   Note que o direcionador da quebra foi o BANCO.  
     
   ![](https://tdn.totvs.com/download/attachments/556370738/image2020-7-22_10-30-12.png?version=1&modificationDate=1595425099513&api=v2)
2. Formato Sintético

   **Totalizar por Filial/Um.Neg/Empresa igual a ‘Sim**’:  
   Note que o direcionador da quebra foi a GESTÃO CORPORATIVA.  
     
   ![](https://tdn.totvs.com/download/attachments/556370738/image2020-7-22_10-37-7.png?version=1&modificationDate=1595425099477&api=v2)

   **Totalizar por Filial/Un.Neg/Empresa igual a ‘Não’**:  
   Note que o direcionador da quebra foi o BANCO.  
     
   ![](https://tdn.totvs.com/download/attachments/556370738/image2020-7-22_10-38-6.png?version=1&modificationDate=1595425099403&api=v2)

**Cenário B -** Iremos utilizar como exemplo a mesma empresa - D MG 01, D RJ 02

Considere no grupo de perguntas o item **Totaliza por Banco** igual a 'Sim'.

1. Formato - Analítico

   **Totalizar por Filial/Um.Neg/Empresa igual a ‘Sim**’:  
   Note que o direcionador da quebra foi a GESTÃO CORPORATIVA.  
     
   ![](https://tdn.totvs.com/download/attachments/556370738/image2020-7-22_11-1-10.png?version=1&modificationDate=1595426470770&api=v2)

   **Totalizar por Filial/Un.Neg/Empresa igual a ‘Não**’:  
   Note que o direcionador da quebra foi o BANCO.  
   ![](https://tdn.totvs.com/download/attachments/556370738/image2020-7-22_11-1-51.png?version=1&modificationDate=1595426511203&api=v2)
2. Formato Sintético

   **Totalizar por Filial/Um.Neg/Empresa igual a ‘Sim**’:  
   Note que o direcionador da quebra foi a GESTÃO CORPORATIVA.  
     
   ![](https://tdn.totvs.com/download/attachments/556370738/image2020-7-22_11-2-37.png?version=1&modificationDate=1595426557617&api=v2)

   **Totalizar por Filial/Un.Neg/Empresa igual a ‘Não**’:

   Note que o direcionador da quebra foi o BANCO.  
   ![](https://tdn.totvs.com/download/attachments/556370738/image2020-7-22_11-3-48.png?version=1&modificationDate=1595426628760&api=v2)

   **Saiba Mais**  
   [RH - Arquivos Bancários](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833673-RH-Arquivos-Bancarios)
