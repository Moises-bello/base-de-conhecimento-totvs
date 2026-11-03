---
article_id: 360060340633
category: Financeiro - Contabilização
content_hash: d6ac24ada6d70f51a1759eaada749862ce4fc994eb1df9dcc01e8ca9453c565c
fetched_at: '2026-06-28T22:38:05.335675+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBAFIN - Contabilização
  LP532 - com campo CT5_HIST trazendo numero do Borderô
type: support-article
updated_at: '2024-09-05T12:58:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060340633-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBAFIN-Contabiliza%C3%A7%C3%A3o-LP532-com-campo-CT5-HIST-trazendo-numero-do-Border%C3%B4
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26156032336279)**Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como efetuar a contabilização do LP 532 com campo CT5\_HIST trazendo numero do Borderô ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
****Solução****No Módulo (06) FINANCEIRO -> rotina **CTBA080->**  **Atualização** -> **Cadastro** -> **Lançamento Padrão ->**  **Incluir**

CT5\_LANPAD = 532 - Contas a Pagar - Baixas de Títulos por Borderô de Pagamento   
CT5\_SEQUEN = 001  
CT5\_DC = 3 - partida dobrada  
CT5\_DEBITO = SE2->E2\_DEBITO  
CT5\_CREDIT = SE2->E2\_CREDIT  
CT5\_VALOR = SE5->E5\_VALOR  
CT5\_HIST = "Pagamento do titulo "+ SE2→E2\_NUM+SE2→E2\_PREFIXO+ " no borderô" + SE2→E2\_NUMBOR   
  
**Exemplo**

- Incluir dois títulos no **Contas a Pagar** no valor de 1.000.  
- Colocar os **títulos em borderô**  
- Baixar os títulos do borderô pela rotina [FINA091 baixa automática de multi-filiais](https://tdn.totvs.com/x/GUCbEg) com contabiliza online =  **NÃO  
-** Acessar a rotina de **Contabilização OFF-LINE** (**CTBAFIN)** e parametrizar as perguntas **Separar por ? = "Documento"**

**Histórico do Borderô**

Caso necessário resgatar o **número do borderô** e informar no histórico no momento da contabilização, deverá ser utilizada a variável **STRLCTPAD.**

**Importante**

**Borderôs:**Para títulos normais o **lançamento padrão será o 532**, já para **títulos de adiantamento** o **lançamento padrão é o 513.**  
Os impostos com fato gerador "**Caixa" (na baixa)** **gerados pelo borderô**, deverão ser contabilizados **pelo LP 530**.

Caso o parâmetro **"Contabiliza por?"** esteja configurado como **"Borderô/borderô" o LP 513** não será contabilizado.

**Demais Informações;**- [Contabilização CNAB LP530 e LP532](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027015252-MP-SIGAFIN-CNAB-FINA430-Os-lan%C3%A7amentos-padr%C3%B5es-530-e-532-contabiliza-o-Retorno-de-Pagamento)  
[- Diferença entre os LP's 521 e 532](https://tdn.totvs.com/x/XFkMEQ)  
  
**Variáveis Contábeis Disponíveis;  
  
VALOR -** Variável totalizadora dos valores de pagamentos efetuados sobre os títulos do borderô.  
**STRLCTPAD -** Contém o(s) número(s) do(s) borderô(s).  
  
**Tabelas Utilizadas;  
  
[FK2 - Baixas a Pagar](https://tdn.totvs.com/x/74DzCg)**   
**SE2 - Contas a  pagar**  
**SEA - Titulos enviados ao banco**  
**SE5 - Movimentação  bancaria - [Em processo de descontinuação](https://tdn.totvs.com/x/epLYCg).**  
**CT2 - Lançamentos contábeis**  
**CT5 - Lançamentos padrões**

**Saiba mais:**<https://tdn.totvs.com/display/public/PROT/532+Baixas+de+Titulos+por+Bordero+de+Pagamento>
