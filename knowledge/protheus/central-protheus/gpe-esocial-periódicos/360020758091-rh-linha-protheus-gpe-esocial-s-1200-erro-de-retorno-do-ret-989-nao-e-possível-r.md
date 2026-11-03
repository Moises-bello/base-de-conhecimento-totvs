---
article_id: 360020758091
category: GPE - eSocial - Periódicos
content_hash: 6fcf6d95cae17bad6ae9f0d6e2099a61292481e127c87ab7e10e4c503cd168b9
fetched_at: '2026-06-28T22:45:08.609835+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200 - Erro de retorno do RET 989 -
  Nao e possível retificar o evento. Existe evento de pagamento associado que sera
  impactado pelo evento retificador
type: support-article
updated_at: '2025-07-21T16:20:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020758091-RH-Linha-Protheus-GPE-eSocial-S-1200-Erro-de-retorno-do-RET-989-Nao-e-poss%C3%ADvel-retificar-o-evento-Existe-evento-de-pagamento-associado-que-sera-impactado-pelo-evento-retificador
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33533730163351) Tempo aproximado para leitura: 00:03:00 min**

**Ocorrência**Erro de retorno do *RET* **989** - Não é possível retificar o evento. Existe evento de pagamento associado que sera impactado pelo evento retificador.  
  
**Exemplo** Recibos impactados: **2320180820201808ADI**.   
  
Ação Sugerida: Retificar ou excluir o evento de Pagamento que contenha o demonstrativo de pagamento que esta causando a inconsistência e tentar enviar o evento novamente.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Causa**   
O governo retorna esse erro quando o usuário está tentando retificar um evento S-1200 já transmitido, porem a retificação pode causar impacto no S-1210 que está no RET.  
  
**Solução**Conforme ação sugerida pelo retorno do *RET,* deve ser **retificado ou excluído o evento de pagamento que contenha o demonstrativo de pagamento que está causando a inconsistência**, ou seja, deve ser excluído via S-3000 ou retificado o evento S-1210 que contenha o número de recibo apresentado no erro.  
  
Para realizar a exclusão do evento S-1210, sugerimos verificar o artigo abaixo:  
[MP - GPE - eSocial - S-3000 - Como realizar a exclusão de um Evento Periódico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027742231-MP-GPE-eSocial-S-3000-Como-realizar-a-exclus%C3%A3o-de-um-Evento-Peri%C3%B3dico?source=search)  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
