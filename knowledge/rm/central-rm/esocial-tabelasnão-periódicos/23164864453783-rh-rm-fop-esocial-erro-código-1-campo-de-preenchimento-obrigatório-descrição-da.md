---
article_id: 23164864453783
category: eSocial - Tabelas/Não Periódicos
content_hash: 4ec3ed458c1ecb0fdba6cf304c504f5c16b524cfc6221277a4634bc3ba1f2749
fetched_at: '2026-06-28T22:47:10.413280+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro código 1: Campo de preenchimento obrigatório:
  Descrição da dependência.'
type: support-article
updated_at: '2024-12-30T14:41:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23164864453783-RH-RM-FOP-eSocial-Erro-c%C3%B3digo-1-Campo-de-preenchimento-obrigat%C3%B3rio-Descri%C3%A7%C3%A3o-da-depend%C3%AAncia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23164813680023) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao realizar o envio dos eventos S-2200, S-2300 ou S-2205 ocorre o erro: **Erro código 1: Campo de preenchimento obrigatório: Descrição da dependência.**  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**Este erro ocorre quando a descrição da dependência não foi devidamente preenchida no sistema para os dependentes que retornam na tag <tpDep>99</tpDep> no eventos supracitados acima.

Validação leiaute eSocial S-1.2 [eSocial versão S-1.2 - Leiautes (cons. até NT 02/2024 rev.)](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s-1-2-cons-nt-02-2024-rev-29-02-2024/index.html#1210_ideBenef_infoIRComplem_infoDep_tpDep)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24006653805591)

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse o cadastro do funcionário, localize os dependentes que retornaram no XML com <tpDep>99</tpDep> conforme exemplo abaixo e realize o preenchimento do campo descrição da dependência;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24006653820183)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24006649547287)

2. Após realizar o devido preenchimento, basta gerar o XML novamente.
