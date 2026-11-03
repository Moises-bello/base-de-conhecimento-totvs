---
article_id: 18857889773975
category: RH - 13º salário
content_hash: 643e124394dde00b0ea801eeebc1b85360db6e25c128e4cb55d2b6584977dda7
fetched_at: '2026-06-28T22:44:00.583234+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Como Conferir o IRRF de 13º Salário no Modelo Simplificado
type: support-article
updated_at: '2025-08-20T13:19:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18857889773975-RH-Linha-Protheus-GPE-Como-Conferir-o-IRRF-de-13%C2%BA-Sal%C3%A1rio-no-Modelo-Simplificado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18857833407127) Tempo aproximado para leitura: **00:03:00 min****Dúvida**MP-1.171/2023 - Como Conferir o IRRF de 13º Salário no Modelo Simplificado?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Foi publicado no Diário Oficial da União a **[MEDIDA PROVISÓRIA nº 1.171, de 30 de ABRIL de 2023](https://www.in.gov.br/en/web/dou/-/medida-provisoria-n-1.171-de-30-de-abril-de-2023-480184173)**, que altera o cálculo de Imposto de Renda.

Efetuado a alteração no cálculo do IRRF, no roteiro 132 para a 2ª parcela do 13º salário para verificar o desconto simplificado mensal (correspondente a 25% (vinte e cinco por cento) do valor máximo da faixa com alíquota zero da tabela progressiva mensal).

O sistema efetuará o cálculo do IRRF tanto no modelo de tributação completo quanto no modelo de tributação simplificado e irá gerar o desconto de IR de acordo com o **modelo de tributação que for mais vantajoso ao empregado**, isto é, o que tiver menor valor.  
  
Para solucionar essa dúvida, realize os seguintes passos:

1.  Verifique a nova tabela de IRRF acessando Atualizações / Definições Cálculo /Manutenção de Tabelas (GPEA320):

![ir.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27988225507607)

2. Para facilitar a conferência, inclua as verbas com Identificadores 1917, 1918 e 1923:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18857859122583)

**Importante**: Todos os IDs acima são para auxílio na conferência do cálculo, portanto não são obrigatórios.

Caso deseje cadastrá-los, deverão ser criadas verbas do tipo de código "4" (Base (Desconto), sem quaisquer incidência para folha e e-social (verificar qual código vigente no leiaute atual, para Rendimento com tributação isenta), Natureza e-social informativa "9989" (verificar possíveis alterações na vigência da natureza no leiaute atual do e-social).  
  
Exemplo de Cálculo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27988194350487)

Memória de Cálculo:

**>Cálculo Simplificado:** Verbas com Sim para o IRRF - 564,80 x Alíquota de IRRF - Valor à deduzir.  
5.200,00 - 564,80 = 4.635,20  
4.635,20 x 22,50% = 1.042,92  
1.042,92 - 662,77 = **380,15****>Cálculo Completo:** Verbas com Sim para o IRRF - INSS x Alíquota de IRRF - Valor à deduzir.  
5.200,00 - 546,81 = 4.653,19  
4.653,19 x 22,50% = 1.046,97  
1.406,97 - 662,77 = **384,20**

**Observações:**  
**-**Na verba 712 - Base de IRRF de 13º (Id 0027) e 424 - Desconto de IRRF de 13º (Id 0071), será apresentado na coluna "**Trib. IR**" o modelo mais benéfico de desconto do IRRF.  
  
**-**Nas verbas de 619 - Base de IRRF Outro Modelo (Id 1917) e 618 - Desconto de IRRF Outro Modelo (Id 1918) será apresentado o valor da Base e Desconto de IRRF que foi desprezado, por ser menos benéfico ao funcionário.

**Saiba Mais**  
Para adquirir maior conhecimento acesse os *links* abaixo  
[Documentação Técnica](https://tdn.totvs.com/pages/releaseview.action?pageId=756458638)   
[RH - 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)
