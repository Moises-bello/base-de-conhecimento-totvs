---
article_id: 360019923012
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 0820b1bd59a313272b15eee16ce783c8c7994a896c34cb8bbd3c175fa3df4869
fetched_at: '2026-06-28T22:38:45.070875+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Controle de
  numeração da nota de saída via SD9 (MV_TPNRNFS = 3)
type: support-article
updated_at: '2025-12-30T14:26:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019923012-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Controle-de-numera%C3%A7%C3%A3o-da-nota-de-sa%C3%ADda-via-SD9-MV-TPNRNFS-3
---

**Dúvida**

Controle de numeração da nota de saída com uso de SD9 (MV\_TPNRNFS = 3).

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT- todas as versões.  
  
**Solução**

Recomendado quando há grande volume de Faturamento para evitar lock de registro por concorrência; e para Organizações que possuem duas ou mais Filiais com mesmo CNPJ. Esta opção possui um controle individual de cada numeração, impedindo a reutilização e evitando saltos/ lacunas.

O controle de numeração por **SD9** foi desenvolvido baseado no modelo de **Talão de Notas**. São criados na SD9 um Lote de **5.000** numerações (ou "formulários" teoricamente) para serem utilizados/consumidos no faturamento.

Atendendo à esta proposta, não é disponibilizada a opção de alterar manualmente a numeração, bem como, não reutiliza numerações já utilizadas. Uma vez tendo utilizado a numeração ("preenchido o formulário de nota") o registro é preenchido na SD9 e mesmo que a nota seja cancelada / excluída; é sugerida a numeração seguinte.  
  
**Importante**  
  
Ao criar uma nova serie verifique se a numeração inicial da emissão da primeira NF está correta na caixa de seleção de séries na emissão da NF (a mesma numeração inserida no MATA012 e na tabela 01 da SX5)  
  
Se houver divergência e a empresa utilizar MDFe, a numeração da MDFe poderá seguir esta numeração apresentada na caixa de seleção ao gravar o registro na tabela CC0

**Vídeo do processo: [MP - SIGAFAT - Controle de Numeração via SD9 #TOTVS\_Backoffice\_Linha\_Protheus](https://www.youtube.com/watch?v=3CUmcFtV2d4)**

**Saiba mais:** **[Controle de sequência automática da numeração para Documento de Saída - Faturamento](http://tdn.totvs.com/pages/viewpage.action?pageId=329024579#FAT0049ControledeNumera%C3%A7%C3%A3odeDocumentodeSa%C3%ADdanoProtheus-Controledesequ%C3%AAnciaautom%C3%A1ticadanumera%C3%A7%C3%A3oparaDocumentodeSa%C3%ADda-Faturamento)**
