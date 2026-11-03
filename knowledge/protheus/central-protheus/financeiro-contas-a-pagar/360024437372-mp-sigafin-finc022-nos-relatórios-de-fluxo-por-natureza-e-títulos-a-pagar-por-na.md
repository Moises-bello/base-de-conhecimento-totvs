---
article_id: 360024437372
category: Financeiro - Contas a Pagar
content_hash: 7e4d25b8a75478a18a59a96368ed196fc83a46cc39a38a884d259b963dd5299a
fetched_at: '2026-06-28T22:38:09.930361+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'MP - SIGAFIN - FINC022 - Nos relatórios de Fluxo Por Natureza e Títulos a
  Pagar Por Natureza não exibe todos os lançamentos '
type: support-article
updated_at: '2021-04-28T15:18:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024437372-MP-SIGAFIN-FINC022-Nos-relat%C3%B3rios-de-Fluxo-Por-Natureza-e-T%C3%ADtulos-a-Pagar-Por-Natureza-n%C3%A3o-exibe-todos-os-lan%C3%A7amentos
---

**Ocorrência**No módulo Financeiro, ao tentar emitir os relatórios **FINC022** -Fluxo Por Natureza e **FINR158** -Títulos a Pagar Por Natureza não exibe todos os lançamentos.   
   
 **Ambiente**Microsiga Protheus – Financeiro – FINC022 - A partir da versão 11.80  
   
 **Causa**Esse incidente ocorre, pois a parametrização do sistema está incorreta para o parâmetro **MV\_NATSINT** **.**

**Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:  
  
 1. É possível organizar a consulta em Analíticas e Sintéticas ao preencher o parâmetro **Exibi****Nat. Sintéticas?** como **Sim** e configurar o parâmetro **MV\_NATSINT** com o conteúdo em 1.  
Após a ativação deste parâmetro, o campo **ED\_PAI** no cadastro da **Natureza** estará habilitado para uso e desta forma o relatório irá exibir os lançamentos relacionados as Naturezas.
