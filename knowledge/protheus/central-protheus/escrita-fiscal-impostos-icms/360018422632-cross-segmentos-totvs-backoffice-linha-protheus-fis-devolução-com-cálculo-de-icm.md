---
article_id: 360018422632
category: Escrita Fiscal - Impostos - ICMS
content_hash: 2bef477106971da406cb2aed509b4a5d720ff9d3cfddfbbf206ba1c57d42262e
fetched_at: '2026-06-28T22:39:25.638238+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Devolução com cálculo
  de ICMS ST
type: support-article
updated_at: '2023-09-22T17:39:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018422632-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Devolu%C3%A7%C3%A3o-com-c%C3%A1lculo-de-ICMS-ST
---

**Dúvida:**Como fazer a devolução de compras com calculo do icms st   
  
**Ambiente:**Protheus - Faturamento - A partir da versão 11.80  
  
**Solução:**

A nota fiscal de devolução é espelho da NF de origem, sendo assim, o ICMS ST deve ser calculado na nota fiscal de entradas.

**Cadastro de produtos:**  
Solid entrada= preenchido com o % de margem de lucro usado para o cálculo do icms St, se não estiver no Danfe consultar a Nfe através da chave eletronica que na descrição dos itens consta a margem usada no cálculo.

**TES**  
Calcula icms = sim  
L. fiscal icms = de acordo com a sua necessidade  
Agrega valor = sim  
Agrega solid = sim  
MKP icm comp = Não  
marg solid = em branco ou configuração.

Após o lançamento da nota fiscal verifique se os campos abaixo foram gravados na SD1

D1\_aliqsol

D1\_margem

D1\_ bricms

D1\_icmsret

Dessa forma o sistema grava o cálculo do ICMS ST para posterior devolução.

Para devolução da nota fiscal com cálculo do ICMS ST  
Faça

**Cadastro de produtos**  
Solid saidas = preenchido com o % de margem de lucro usado para o cálculo do icms St

TES  
Calcula icms = sim  
L. fiscal icms = de acordo com a sua necessidade  
Agrega valor = sim  
Agrega solid = sim  
MKP icm comp = Não  
marg solid = em branco ou configuração

Dev. par prop.= sim

Verifique o parâmetro:  
MV\_TPSOLCF= "S,F,R"

Ao consultar a planilha financeira o valor do ICMS ST estará calculado, correto.  
O icms st faz parte do valor da Nota Fiscal e deve ser calculado.

MV\_ICSTDEV = .F. = o valor do icms st será impresso na coluna despesas acessórias na Tag Voutros

MV\_ICSTDEV (ICMS ST para notas de devolução), onde:  
.F. - O ICMS ST será destacado no campo Outras despesas e informação complementar do danfe.  
.T. - O ICMS ST será destacado no campo próprio.

Para impressão do Danfe quanto ao valor do icms st, abrir um chamado junto a equipe de NFE.
