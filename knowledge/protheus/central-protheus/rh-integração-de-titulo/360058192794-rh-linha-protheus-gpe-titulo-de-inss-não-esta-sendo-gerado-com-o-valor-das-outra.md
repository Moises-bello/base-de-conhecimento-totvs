---
article_id: 360058192794
category: RH - Integração de Titulo
content_hash: 721a68fee83e1cd4721a56cfaa75e8cc8ba2e8b82aa325399ed719d37528a042
fetched_at: '2026-06-28T22:43:37.244634+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Titulo de INSS não esta sendo gerado com o valor
  das Outras Entidades
type: support-article
updated_at: '2025-08-12T12:27:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058192794-RH-Linha-Protheus-GPE-Titulo-de-INSS-n%C3%A3o-esta-sendo-gerado-com-o-valor-das-Outras-Entidades
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34118779825943) Tempo aproximado para leitura: **00:01:30 min****

**Ocorrência**Titulo de INSS não esta sendo gerado com o valor das Outras Entidades  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Causa**Esse incidente ocorre, devido a parametrização da tabela S038 - Outras Entidades da rotina Manutenção de Tabelas - GPEA320, caso seja informando um percentual para outras entidades o Sistema passa a gerar os valores nas respectivas verbas destas entidades, deixando de gerar na verba com identificador de cálculo 0149.

![OUTRAS_ENTIDADES.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360098589154)  
  
**Solução**Optando por informar apenas o campo %terceiros que englobará o total da soma de todos os demais campos, o Sistema apresentará o conteúdo no Relatório da **Folha de Pagamento -** **GPER040,** na Guia de Previdência Social  **GPS/GRPS - GPER240** para recolhimento e no Título de INSS (Instituto Nacional do Seguro Social). Para que o ajuste tenha impacto no respectivo mês, deverá ser executado o cálculo da Folha de Pagamento (roteiro FOL).

**Saiba Mais**  
[Artigos sobre Integração de Título](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)  
[RH - Linha Protheus - GPE - Outras entidades não estão sendo geradas na guia GPS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014263931-MP-GPE-Outras-entidades-n%C3%A3o-est%C3%A3o-sendo-geradas-na-guia-GPS)
