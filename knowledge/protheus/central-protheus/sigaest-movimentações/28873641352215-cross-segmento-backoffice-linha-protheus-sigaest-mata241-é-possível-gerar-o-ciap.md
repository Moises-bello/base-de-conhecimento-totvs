---
article_id: 28873641352215
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 403df0a579baaecab3da9a9cbec1ae7824d7c0cfd4c22e19d731d2ce74ceb37f
fetched_at: '2026-06-28T22:38:56.947411+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA241 - É possível
  gerar o CIAP para ativos pela Movimentação interna?
type: support-article
updated_at: '2025-01-02T11:57:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28873641352215-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA241-%C3%89-poss%C3%ADvel-gerar-o-CIAP-para-ativos-pela-Movimenta%C3%A7%C3%A3o-interna
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28873641322647) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**É possível gerar o código CIAP utilizando a rotina de Movimentações Múltiplas MATA241 utilizando uma TM vinculada a uma TES que gera ativo, quando na entrada do produto (MATA103) foi utilizado uma TES que não atualiza ativo?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**O CIAP, só será gerado no processo de transposição do ativo em estoque realizado pela MATA241, se a nota fiscal selecionada para esse vínculo tiver ICMS creditado no momento da entrada, ou seja, se a TES utilizada na entrada estiver configurada para controlar e creditar ICMS conforme exemplo:

**TES na Entrada do produto:**

Credita ICMS = Sim

Atualiza Ativo = Não

Calcula ICMS = Sim

Livro Fiscal de ICMS = Outros

Sit trib icm = 90

Após dar entrada com uma TES conforme configuração acima, será necessário incluir uma nova TES com as mesmas configurações, porém com o campo Atualiza Ativo = Sim, exatamente conforme mostrado na documentação: [CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Gerar CIAP vinculado com ativo pelo documento de entrada?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022696171-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Gerar-CIAP-vinculado-com-ativo-pelo-documento-de-entrada)

![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28873610369687)

![Screenshot_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28873641326487)

Após a inclusão dessa nova TES, incluir uma TM na rotina MATA230 que gera ativo(F5\_GERAATF = Sim), e  vincular a ela a nova TES configurada para gerar o ativo, pelo campo F5\_TEATF:

![Screenshot_24.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28873610372503)

Ao validar na rotina Atualização de Ativos Imobilizados (ATFA012) após movimentação na MATA241:

![Screenshot_4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28885846012311)

**OBSERVAÇÃO:** O código CIAP via MATA241, somente será gerado caso na entrada do produto, a TES esteja configurada a parte do ICMS conforme primeiro exemplo desse artigo. Caso seja utilizado uma TES que não esteja configurada para creditar o ICMS no momento da entrada desse produto, mesmo que seja informado uma TM que esteja vinculada a uma TES que esteja configurada para gerar CIAP na rotina MATA241, o CIAP não será gerado. Pois o que determina é o ICMS no momento da entrada do produto. 

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
