---
article_id: 360020604251
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 101550ea741e1906d017653395e67b970d0fa61ac5ed29b0eecba6fbefdd7e26
fetched_at: '2026-06-28T22:38:54.014601+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Habilitando o Controle
  de Rastreabilidade no Protheus
type: support-article
updated_at: '2022-07-14T13:18:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020604251-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Habilitando-o-Controle-de-Rastreabilidade-no-Protheus
---

**Dúvida**Como habilitar o controle de Rastreabilidade no *Protheus*?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
**Solução**

Siga os passos abaixo para conseguir habilitar o controle de Rastreabilidade

**1.** Via Configurador (SIGACFG), abra a tela de Parâmetros e habilite o MV\_RASTRO (deixando com conteúdo **S**)

![Sem_t_tulo.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016549291/Sem_t_tulo.png)

**2.** Acessando o *Protheus*, na rotina MATA010 (Cadastro de Produtos) será cadastrado o produto com a informação que o mesmo controla rastreabilidade, por meio do campo "Rastro" (B1\_RASTRO)

![Sem_t_tulo.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016549851/Sem_t_tulo.png)

Para utilizar o Controle de Rastreabilidade por Lote, basta configurar o campo com conteúdo **L**, caso trabalhe com Rastreabilidade de Sub-lote, configure o campo com conteúdo **S**.

Informações adicionais:

Caso a configuração acima não seja feita corretamente, o sistema apresentar[a a mensagem abaixo:

![Sem_t_tulo.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016499152/Sem_t_tulo.png)

**Como habilitar o Controle de Rastreabilidade para produto que já possui saldo?**

Partindo da premissa que o parâmetro MV\_RASTRO esteja habilitado (ou seja, esteja com conteúdo **S**), basta efetuar os seguintes passos:

- Acessar à rotina de Cadastro de Produtos (MATA010);

- Localizar o produto e clicar em "Alterar";

- No campo "Rastro" (B1\_RASTRO), alterar para L (para Lote) ou S (Para Sub-lote);

- Acessar à rotina Manutenção de Lotes (MATA390) para distribuir **todo o saldo** do produto para Lote(s) ou Sub-lote(s) específicos.

Com isso, o produto passa a controlar além do saldo físico e financeiro o saldo por lote. Com isso, todo saldo que for movimentado ou requisitado deve ser informado o lote e atualizará as tabelas referenciadas, abaixo segue o fluxo de movimentação dos saldos.

|  |  |  |
| --- | --- | --- |
|  | ***Saldo*** ***físico******e*** ***Financeiro*** | ***Saldo por***  ***Rastreabilidade (Lote)*** |
| ***Saldo Inicial*** | **SB9** | **SBJ** |
| ***Movimentos*** | **SD1, SD2, SD3** | **SD5** |
| ***Saldo Atual*** | **SB2** | **SB8** |
| ***Empenhos e Bloqueios*** | **SD4** | **B8\_EMPENHO** |

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
