---
article_id: 360016330151
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: c99fa6906445bedd6a1fe6c6b164cd4b1870022f15f22b96e87605e11c65404b
fetched_at: '2026-06-28T22:42:05.173886+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Devolução de venda no Regime Não Cumulativo
type: support-article
updated_at: '2023-01-04T13:31:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016330151-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Devolu%C3%A7%C3%A3o-de-venda-no-Regime-N%C3%A3o-Cumulativo
---

**Dúvida**Devolução de venda no Regime Não Cumulativo.  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80.  
  
**Solução**  
 Segue abaixo as configurações para as Devoluções de venda (**Formulário próprio** = Sim).   
Afim de solucionar essa dúvida, realize os seguintes passos:  
  
 1. Para as devoluções de venda de dentro do período, a base de cálculo da nota fiscal original (venda) será reduzida no registro **C170**. Para notas fiscais de períodos anteriores ao da geração do arquivo txt, o valor será levado para Bloco M - registros **M220** e **M620**.  
  
2. Configure o **TES** da seguinte forma, para **Formulário próprio** = Sim:  
**F4\_PISCOF** = Não considera;  
**F4\_PISCRED** = Não calcula;  
**F4\_CSTPIS** = 98;  
**F4\_CSTCOF** = 98.  
  
Segue abaixo as configurações para as Devoluções de venda (**Formulário próprio** = Não).   
Afim de solucionar essa dúvida, realize os seguintes passos:  
  
1. Tanto para devoluções de dentro do período, quanto para devoluções de notas fiscais de venda de períodos anteriores ao da geração do arquivo, será gerado um registro **C100** e **C170** para a nota fiscal de Devolução. Também será gerado o registro **M100** para PIS e **M500** para COFINS com os valores de crédito.  
  
2. Configure o **TES** da seguinte forma, para **Formulário próprio** = Não.  
**F4\_PISCOF** = Ambos;  
**F4\_PISCRED** = Credita;  
**F4\_CSTPIS** = 50;  
**F4\_CSTCOF** = 50.
