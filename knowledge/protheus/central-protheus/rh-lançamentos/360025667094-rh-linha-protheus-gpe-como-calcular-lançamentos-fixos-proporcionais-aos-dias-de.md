---
article_id: 360025667094
category: RH - Lançamentos
content_hash: f36db1f2555ae4df64a66400d9241bf6bd91f285608285dfad0c6f56058c5d1d
fetched_at: '2026-06-28T22:43:31.433705+00:00'
product: protheus
section_id: 360010781734
source: central-protheus
title: RH - Linha Protheus - GPE - Como Calcular Lançamentos Fixos Proporcionais aos
  dias de Férias
type: support-article
updated_at: '2025-07-24T17:03:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025667094-RH-Linha-Protheus-GPE-Como-Calcular-Lan%C3%A7amentos-Fixos-Proporcionais-aos-dias-de-F%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33692741797655) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como Calcular Lançamentos Fixos Proporcionais aos dias de Férias?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Para que um valor seja calculado proporcionalmente aos dias de Férias, a verba informada nos Lançamentos Fixos deve ter o campo **Ref. Férias** (RV\_REFFER) preenchido com **Sim,** e ter uma verba de **mês seguinte** relacionada a **verba lançada.** Com esta configuração, o valor será proporcionalizado **entre** as verbas de **Mês** e **Mês seguinte.**

**Exemplo 1:**  
Lançamento fixo no valor de R$3000,00.  
Cálculo de férias de 20 dias, sendo 12 dias no mês e 8 dias no mês seguinte.

→ Verba **lançada não** possui referência para férias ou verba de mês seguinte associada:  
Neste caso será gerado **uma** única verba no valor de R$2000,00, referente aos 20 dias de férias totalizados.

→ Verba **lançada possui** referência para férias e existe verba de mês seguinte associada:  
Neste caso será gerada a **verba principal** com o valor de R$1200,00, referente aos **12 dias** de férias no mês e uma **segunda verba** com o valor de R$800,00 referente aos **8 dias** de férias mês seguinte.

O mesmo tratamento foi efetuado para a divisão do abono, neste caso foi criado o campo **RV\_CODABO**, que está disponível **apenas** a partir da versão **12.1.23.** Caso queira utilizar a melhoria em versão anterior, faça a criação **manual** do campo, conforme definição no fim deste documento.

Ao preencher o campo RV\_CODABO em uma verba que possua referência para férias e que seja incluída nos Lançamentos Fixos com proporcionalização ativada, a verba poderá ser dividida em **Férias**, **Férias Mês Seguinte**, **Abono** e **Abono Mês Seguinte**.

**Exemplo 2:**Lançamento fixo de R$3000,00.  
Cálculo de férias de 20 dias = 10 dias de abono, sendo 10 dias no mês e 10 dias no mês seguinte.

→ Verba Prêmio Mês 10 dias = R$1000,00  
→ Verba Prêmio Mês Seguinte 10 dias = R$1000,00  
→ Verba Prêmio Abono Mês Seguinte 10 dias = R$1000,00

Abaixo segue orientações para a criação do campo **RV\_CODABO** na tabela SRV - Verbas:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039894474)

Para mais informações acesse: <http://tdn.totvs.com/pages/releaseview.action?pageId=397380408#id-2937335DRHPAG-19090DTLan%C3%A7amentosfixosnasf%C3%A9rias-SX3>
