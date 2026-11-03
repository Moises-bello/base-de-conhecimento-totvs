---
article_id: 1500002030622
category: Manutenção de Ativos (SIGAMNT)
content_hash: 93ad2c23893083d8bd8d225c5f76dfa5c502e0078b3eb14b8d82038462236d6e
fetched_at: '2026-06-28T22:42:34.298908+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Pagamento de Multas Manutenção de Ativos
  não integrado ao Financeiro
type: support-article
updated_at: '2021-09-09T21:28:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002030622-Manufatura-Linha-Protheus-MNT-Pagamento-de-Multas-Manuten%C3%A7%C3%A3o-de-Ativos-n%C3%A3o-integrado-ao-Financeiro
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:01:45** **min**  
**Dúvida**Como efetuar o pagamento de multas quando o **Manutenção de Ativos - SIGAMNT** não está integrado ao **Financeiro - SIGAFIN**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**Primeiramente é necessário configurar os parâmetros: **MV\_NGMNTFI - Integração Manutenção (MNT) com Financeiro (FIN) = N - Não**;   
**MV\_NGMNTFR - Indica se a empresa ira utilizar o Gestão de Frota  = S - Sim**.

* Cadastros prévios:

1. Em **Atualizações / Controle de Oficina / Bens / Família de Bens**, incluir uma família;
2. Em **Atualizações / Controle de Oficina / Bens / Modelos**, incluir um modelo;
3. Em **Atualizações / Controle de Oficina / Bens / Fabricantes**, incluir fabricante;
4. Em **Atualizações / Controle de Oficina / Cadastros Básicos / Calendário**, incluir um calendário;
5. Em **Atualizações / Controle de Oficina / Cadastros Básicos / Centros de Custos**, incluir um centro de custo;
6. Em **Atualizações / Controle de Oficina / Cadastros Básicos / Fornecedores**, incluir um fornecedor;
7. Em **Atualizações / Controle de Oficina / Bens / Bens**, incluir um bem do tipo não integrado ao tms, com contador próprio e placa.
8. Em **Atualizações / Controle de Riscos / Multas / Infrações Trans**., incluir uma infração de trânsito;
9. Em **Atualizações / Controle de Riscos / Multas / Org. Autuadores**, incluir um órgão autuador.

* Incluindo uma multa de trânsito:

1. Em **Atualizações / Controle de Riscos / Multas / Multas**, incluir uma multa do tipo trânsito;
2. Na aba **Cadastro da Multa**, informar os campos conforme *help* de campo;
3. Na aba **Pagamento**, verificar que possui o campo **Pagamento - TRX\_PAGTO**, preencher com o conteúdo **1=Sim**, preencher os demais campos conforme *help*;
4. Confirmar.
5. Visualizar e verificar que a multa está como paga.
