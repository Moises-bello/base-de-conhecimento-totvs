---
article_id: 17158274344727
category: Materiais - Compras (SIGACOM)
content_hash: 40a32649111a1f2398676c736a83b8f94cd3a342e33af8916e7b8c5c4ba26a58
fetched_at: '2026-06-28T22:41:20.232661+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Protheus - SIGACOM - Na inclusão de um CTE
  o sistema exibe o help A103VLDATF
type: support-article
updated_at: '2024-12-27T19:32:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17158274344727-Cross-Segmentos-TOTVS-Backoffice-Protheus-SIGACOM-Na-inclus%C3%A3o-de-um-CTE-o-sistema-exibe-o-help-A103VLDATF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17158306494743) Tempo aproximado para leitura: **00:04:00 min****Dúvida**Na inclusão de um CTE pela rotina MATA103, documento de entrada,  o sistema exibe o help  **A103VLDATF**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - a partir da 12.1.33

**Causas**

O sistema exibe o help A103VLDATF, quando o tipo da nota é Normal, o parâmetro **MV\_AGVLATF = T**,  a espécie = **CTE**, e o TES possui o campo **F4\_ATUATF = 'S'.** Isso ocorre porque, por conta do parametro  MV\_AGVLATF estar T, o sistema tenta aglutinar o valor do CTE ao ativo da nota de origem, porém no típo da nota Normal não conseguimos por padrão vincular a origem, logo o sistema exibe o help informando que não localizou as informações da nota do Bem de origem.

**Solução**

**Com o parâmetro MV\_AGVLATF = T,** para que haja a aglutinação do valor do CTE ao ativo de origem ( nota de compra ), é necessário que o tipo da nota de entrada, seja **C ( complemento ) e o Tipo do Complemento Frete,** para que a nota de origem possa ser vinculada à nota do CTE. **Por mais que os dados da nota de origem sejam preechidos manualmente no item da nota do CTE, o sistema não as reconhece, pois ele necessita que o vínculo seja efetuado por ele. E esse vínculo, por padrão do sistema só ocorre quando o tipo da nota de entrada é Complemento.**

**Para notas de CTE com o tipo Normal, não conseguimos vincular à origem, logo não há aglutinação de valores no ativo da nota de compra/origem, a qual o CTE se refere.**

**Para entrada de CTE com o tipo da nota igual a normal, verificar cenário 3 do documento abaixo :**

**[CTE com ativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11901702933655-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Ocorr%C3%AAncia-na-Integra%C3%A7%C3%A3o-com-Ativo-Este-documento-n%C3%A3o-ser%C3%A1-gravado-devido-a-inconsist%C3%AAncias-na-grava%C3%A7%C3%A3o-do-ativo-fixo?source=search)**

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
