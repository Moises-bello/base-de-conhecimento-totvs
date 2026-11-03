---
article_id: 7053451996055
category: SIGAEST - MOVIMENTAÇÕES
content_hash: ce5fccb993beffb95fc14dcbdb151d741e877e88a3abeaf5d9692955b3be3333
fetched_at: '2026-06-28T22:38:55.654511+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA103 - "Atenção:  O
  saldo do Produto ficará negativo após a Exclusão"'
type: support-article
updated_at: '2025-10-14T16:38:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7053451996055-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA103-Aten%C3%A7%C3%A3o-O-saldo-do-Produto-ficar%C3%A1-negativo-ap%C3%B3s-a-Exclus%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35624544797975) Tempo aproximado para leitura: **00****:01:18 min** **Dúvida**

O que fazer quando, ao Excluir um Documento de Entrada, for exibida a mensagem "Atenção: O saldo do Produto ficará negativo após a Exclusão"?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7053142558359)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Essa situação é bem comum ocorrer, seja com produtos **sem ou com controle de Lote e/ou Endereçamento**, onde, o **Saldo Disponível** (que pode ser consultado através do atalho [F4] do teclado - detalhes **[clicando aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-MP-SIGAEST-Consulta-F4-cadastro-de-produtos)**) eventualmente esteja comprometido por outros saldos de empenhos, reservas ou até mesmo **movimentações posteriores àquela Entrada**.

**Como descobrir se houveram movimentações de saída após aquela Nota de Entrada?**

Neste caso, a recomendação inicial é de que seja verificado o **[Kardex do Produto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011930291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR900-Como-configurar-corretamente-o-relat%C3%B3rio-Kardex-para-an%C3%A1lise-de-Custos-e-Movimenta%C3%A7%C3%B5es-)**, para entender se houveram movimentações de saída posteriores àquela Entrada, pois este é o caso mais comum, e se for, realmente o Sistema impedirá o usuário de excluir esta nota pois seu saldo já foi utilizado/consumido.

**O que causa este Help?**

O fonte faz a validação do parâmetro **[MV\_ESTNEG](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406452757399)** que permite ou não movimentações ou exclusões de entrada negativarem o saldo físico do Produto com base no saldo disponível do estoque. Cabe uma análise interna da empresa com base na regra de negócio para averiguação de qual maneira o parâmetro se enquadra melhor.

**Situação relacionada:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Utilização do parâmetro MV\_TPSALDO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013215531-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Utiliza%C3%A7%C3%A3o-do-par%C3%A2metro-MV-TPSALDO?source=search)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
