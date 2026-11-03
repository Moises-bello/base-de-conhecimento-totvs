---
article_id: 360015905712
category: MDFe - Manifesto de Carga
content_hash: 724fb678033fdb85eeebd57de11c5dd765905bba8434da43ec502cae48ae1015
fetched_at: '2026-06-28T22:40:08.221349+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE -  Requisitos
  para filtrar nota na rotina
type: support-article
updated_at: '2025-06-17T18:52:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015905712-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-Requisitos-para-filtrar-nota-na-rotina
---

**Dúvida**Quais são os requisitos para filtrar nota na rotina SPEDMDFE ?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões

**Solução**

1- Na inclusão do MDFe os campos precisam estar preenchidos **F2\_ESPECIE ou F1\_ESPECIE, F3\_ESPECIE e FT\_ESPECIE = SPED**

2- O campo **F2\_CHVNFE ou F1\_CHVNFE** deverá estar com a chave preenchida.

3- No documento de saída ao menos um dos três campos deve estar preenchido **F2\_VEICUL1, F2\_VEICUL2, F2\_VEICUL3.**

4- Gere notas que tenham veículo vinculado no pedido de venda pelo campo C5\_VEÍCULO ou poderá ir em **Faturamento > Atualizações > Faturamento > Expedição > Consulta NF > Manutenção**.

* Ao preencher o campo **C5\_VEÍCULO no pedido de venda** será preenchido o **F2\_VEICUL1.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360011615372)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360011615291)

1- Para notas de entrada os campos do veículo são **F1\_VEICUL1, F1\_VEICUL2, F1\_VEICUL3.**

2- Para gravar esses campos no documento de entrada informações adicionais tem que ser preenchido algum dos campos o **veiculo 1, veiculo 2 e veiculo 3.**

3- Nesses campos **F1\_VEICUL1, F1\_VEICUL2, F1\_VEICUL3** deve ser informado o código do veículo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360011615331)

* **Saiba mais**

Na rotina SPEDMDFE é possível fazer o MDFe como notas de outras filiais para isso habilitar o filtro Todas Filiais = 1- Sim

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360011615351)

[Requisitos para filtrar na rotina](http://tdn.totvs.com/display/PROT/MDF0005_Requisitos_para_filtrar_nota_na_rotina?preview=/235311303/415695361/image2018-9-19_8-58-54.png)
