---
article_id: 4414035327639
category: Gestão de Frotas
content_hash: 672c8d710adfacf140617e931732af1409f08176c846a0317f98db269ac715b4
fetched_at: '2026-06-28T22:42:39.594136+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Saída de Combustível - MNTA657
type: support-article
updated_at: '2021-11-26T12:49:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414035327639-Manufatura-Linha-Protheus-MNT-Sa%C3%ADda-de-Combust%C3%ADvel-MNTA657
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:01:30 min****Dúvida**Para que serve a rotina **Saída de Combustível - MNTA657**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas - Todas as versões  
  
**Solução**Esta rotina permite registrar as saídas indevidas de combustíveis como evaporação, vazamento, drenagem, etc. Esta que pode ou não ser relacionada com a **Aferição de Bomba - MNTA630** mediante parametrização. Todos lançamentos geram automaticamente um reporte na tabela **TTV -** **Contador da Bomba de Combustível**.  
Se para o motivo de saída que foi informado estiver indicado como sim no campo **TTX\_MOTTTH -** **Atu. Estoque** no cadastro de **Motivos de Saída - MNTA658** ao confirmar o registro será gerado um registro na tabela **SD3 - Movimentação de Estoque**, assim atualizando o saldo em estoque. Caso indicado não, o Sistema não efetua a movimentação e baixa do estoque.  
O objetivo da rotina é possibilitar a realização dos processos de inclusão, alteração, visualização e exclusão de reportes de**Saída de Combustível**.  
  
**Importante**Só será efetuada a movimentação e baixa do estoque se o módulo de **Gestão de Frotas** estiver integrado com **Estoque** por meio do parâmetro **MV\_NGMNTES - Integração com o Estoque**, e caso no registro de saída de combustível o motivo de saída informado indicar a atualização de estoque.  
  
**Saiba mais**Acesse a documentação completa da rotina no *link* [Saída de Combustível - MNTA657](https://tdn.totvs.com/pages/releaseview.action?pageId=552090434)[.](https://tdn.totvs.com/pages/releaseview.action?pageId=544703386)
