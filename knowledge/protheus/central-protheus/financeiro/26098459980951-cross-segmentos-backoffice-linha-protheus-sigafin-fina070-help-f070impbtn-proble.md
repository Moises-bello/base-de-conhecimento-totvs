---
article_id: 26098459980951
category: Financeiro
content_hash: b117d26fa9a94ea1c4fc7410e955d639e82c13e91eaaa08ef247859cd1563efb
fetched_at: '2026-06-28T22:38:02.973475+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA070 - Help: F070IMPBTN
  Problema: A funcionalidade de acerto de impostos deve ser utiliza em títulos cujo
  cliente e natureza estejam configurados para o cálculo dos impostos PIS, COFINS
  e CSLL'
type: support-article
updated_at: '2024-09-03T15:35:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26098459980951-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA070-Help-F070IMPBTN-Problema-A-funcionalidade-de-acerto-de-impostos-deve-ser-utiliza-em-t%C3%ADtulos-cujo-cliente-e-natureza-estejam-configurados-para-o-c%C3%A1lculo-dos-impostos-PIS-COFINS-e-CSLL
---

**[Remover as instruções entre colchetes e altere o tempo aproximado para leitura]**  
![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26098465423255) Tempo aproximado para leitura: **00:10:00 min** **Dúvida**Help: F070IMPBTN Problema: A funcionalidade de acerto de impostos deve ser utiliza em títulos cujo cliente e natureza estejam configurados para o cálculo dos impostos PIS, COFINS e CSLL  
  
**Ambiente**Exemplo:  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Financeiro - Todas as versões  
  
**Causa:**

[MV\_IMPBXCR = 2](https://tdn.totvs.com/display/public/PROT/FIN0020_CREC_Botao_impostos_baixas_a_receber)

[MV\_MT10925 = 1](https://tdn.totvs.com/pages/releaseview.action?pageId=6076816)

FINA070 - Ao clicar em "Baixar" e clicar em "Outras Ações > Impostos"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26098459959703)

Irá apresentar o HELP

Help: F070IMPBTN Problema: A funcionalidade de acerto de impostos deve ser utiliza em títulos cujo cliente e natureza estejam configurados para o cálculo dos impostos PIS, COFINS e CSLL

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26098465426839)

**Solução:**

A mensagem apresenta quando:

**1)** O sistema não encontrar o código na natureza na tabela SED (pode ser pelo motivo de compartilhamento estar diferente entre na tabela SX2 e a tabela SED)

**2)** Os campos abaixo estarem diferentes de '**S**'  
ED\_CALCPIS  
ED\_CALCCSL  
ED\_CALCCOF

A1\_RECPIS

A1\_RECCSLL

A1\_RECCOFI

Para que o sistema calcule os impostos (ex: PCC Pis, Cofins e Csll) de forma automática, é necessário que os campos acima estejam com o conteúdo '**S**'

**3)** Verificar se está utilizando o ponto de entrada [Fa070Imp](https://tdn.totvs.com/display/public/mp/Ponto+de+Entrada+FA070IMP)

Sabia Mais:

[FIN0020\_CREC\_Botao\_impostos\_baixas\_a\_receber](https://tdn.totvs.com/display/public/PROT/FIN0020_CREC_Botao_impostos_baixas_a_receber)
