---
article_id: 360027070511
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: bffdd5fd96ffe3e68582b5f1e261e48e0a3fb92dfef6113d9078f49260397b7c
fetched_at: '2026-06-28T22:40:44.305726+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECD - Erro na inclusão
  de dados nas tabelas CSA e (ou) CSB VIA PROCEDURE
type: support-article
updated_at: '2026-04-28T16:52:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027070511-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-Erro-na-inclus%C3%A3o-de-dados-nas-tabelas-CSA-e-ou-CSB-VIA-PROCEDURE
---

Durante a criação do SPED Contábil (ECD) e/ou FCONT no TOTVS Protheus, pode ocorrer o erro "Erro na inclusão de dados no CSA e/ou CSB via procedure". As causas principais são: procedure 34 desatualizada ou incompatível, exigindo atualização do pacote de procedures, ou o parâmetro MV\_CTBSPRC ativado com campos de tamanhos incompatíveis, especialmente entre "Hist Lanc (CT2\_HIST)" e "Desc Hist CT8\_DESC", que requer ajuste no Configurador (SIGACFG) para evitar truncamento.

**Ocorrência**  
Durante o processo de criação do SPED Contábil (ECD) e/ou FCONT, o sistema apresenta a seguinte mensagem de erro: "Erro na inclusão de dados no CSA e/ou CSB via procedure. A inclusão será feita pelo processo padrão."

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40074803954583)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial (SIGACTB) - A partir da versão 12

**Solução**  
Esta situação pode ocorrer por dois motivos principais. Siga as orientações abaixo conforme o seu cenário:

1. **Procedure** **34 desinstalada****, incompatível ou desatualizada:**  
     
   A rotina depende de stored procedures atualizadas no banco de dados para a execução da inclusão. Para corrigir essa inconsistência, é necessário realizar a atualização do pacote de Procedures no ambiente.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40074803956503)

   Para atualização da procedure, seguir os passos da documentação:  
   [Cross Segmento - Backoffice Linha Protheus - SIGACTB - SIGAATF - SIGAPCO - Procedure Desatualizada ou Incompatível](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30076556464023-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-SIGAATF-SIGAPCO-Procedure-Desatualizada-ou-Incompat%C3%ADvel)
2. **Parâmetro MV\_CTBSPRC ativado com campos de tamanhos incompatíveis:**  
     
   Quando o parâmetro `MV_CTBSPRC` está configurado como `.T.` (ativando o uso de *procedure* dinâmica no ambiente), o erro ocorre se um dos campos que o sistema está alimentando possui tamanho menor que o conteúdo recebido.  
     
   Para identificar o campo divergente, é necessário analisar o Trace do DBAccess (TOP Connect), que registrará os campos utilizados no processo. O cenário mais comum ocorre com o campo `Desc Hist (CT8_DESC)`, que recebe o conteúdo do campo `Hist Lanc (CT2_HIST)`. Se o campo `Desc Hist (CT8_DESC)`estiver com tamanho menor que o `Hist Lanc (CT2_HIST)`, a mensagem será exibida.  
   1. Acesse o módulo Configurador (SIGACFG).
   2. Acesse a rotina de Base de Dados (CFGX031).
   3. Localize os campos `Hist Lanc (CT2_HIST)`e `Desc Hist (CT8_DESC)`.
   4. Ajuste para que o campo `Hist Lanc (CT2_HIST)`tenha o mesmo tamanho do campo `Desc Hist (CT8_DESC)`.

> **Atenção:** Não é aconselhável diminuir o tamanho dos campos para evitar o risco de truncar o conteúdo. Caso seja estritamente necessário, realize uma análise de base e backup prévio.

**Saiba Mais**  
[Procedure desatualizada ou incompatível.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30076556464023-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-SIGAATF-SIGAPCO-Procedure-Desatualizada-ou-Incompat%C3%ADvel)   
[Habilitar procedures dinâmicas na geração da ECD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007132632-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Habilitar-procedures-din%C3%A2mica-na-gera%C3%A7%C3%A3o-da-ECD)
