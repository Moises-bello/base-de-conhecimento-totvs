---
article_id: 1500004317881
category: SIGAEST - MOVIMENTAÇÕES
content_hash: a16d7e07b1325c5cb85d77db4ed2254d3015a2a64e4035965bd021be80627ace
fetched_at: '2026-06-28T22:38:58.593371+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: MP - SIGAEST - MATA175 - Validação do HELP NOPRD01 na Baixa de CQ
type: support-article
updated_at: '2021-11-23T14:26:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004317881-MP-SIGAEST-MATA175-Valida%C3%A7%C3%A3o-do-HELP-NOPRD01-na-Baixa-de-CQ
---

**Ocorrência**Ao tentar efetuar a Baixa de C.Q (MATA175) ocorre o HELP NOPRD01 - Produto não encontrado no arquivo de notas fiscais.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005436982/mceclip0.png)  
  
**Ambiente**Microsiga Protheus – Estoque/Custos – A partir da versão 11.80  
  
**Causa**Este problema ocorre normalmente quando a rotina faz uma varredura e não encontra registro de Entrada que gerou o envio do produto ao Centro de Qualidade (C.Q), gerando este HELP.  
  
**Solução**

Vamos elencar a investigação do problema/correção em passos:

**1° Passo** - Precisamos entender qual o movimento levou o produto ao C.Q.

Movimentos padronizados que levam ao Produto ao C.Q (MV\_CQ) são: Documento de Entrada (MATA103) e Apontamento de Produção (MATA250). Qualquer outro movimento que levou o produto ao armazém de C.Q pode ter sido pelo fato de haver alguma customização ou, o MV\_CQ ter mudado de armazém.

**2° Passo** - Este HELP é chamado também pelo Ponto de Entrada **[A175GRV](https://tdn.totvs.com/display/public/PROT/A175GRV)**

Avalie se possui este P.E em ambiente. Se sim, desabilite via tabela XX7 -> XX7\_STATUS = 2. Em seguida tente efetuar a baixa de C.Q.

**3° Passo** - Avalie de houve mudança de armazém de C.Q (MV\_CQ)

Num cenário onde, por algum motivo, houve mudança do Armazém de CQ e o novo MV\_CQ tinha algum saldo preso, provavelmente gerará o HELP também.

**4° Passo** - Avaliar alternativas paliativas caso nenhuma das anteriores atendam.

* Caso o saldo realmente fique preso no C.Q é: Alterar o MV\_CQ para realizar uma movimentação interna ou transferência e depois retornar novamente;
* Se o saldo foi para o C.Q por meio de alguma movimentação/transferência, avaliar o campo D3\_NUMSEQ, deixando-o igualado com as demais tabelas para tentar dar a Baixa do CQ;

Caso nenhuma dar alternativas anteriores resolva o problema, acione o Suporte Técnico através do Portal de Atendimento TOTVS.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
