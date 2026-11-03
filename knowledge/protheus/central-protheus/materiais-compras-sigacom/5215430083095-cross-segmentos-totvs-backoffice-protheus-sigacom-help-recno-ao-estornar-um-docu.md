---
article_id: 5215430083095
category: Materiais - Compras (SIGACOM)
content_hash: 82f4d50ba3db375c5e4e6a074f06448f0ef523f67669abad1cc93aa86ac0dbbe
fetched_at: '2026-06-28T22:41:18.963470+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help RECNO ao Estornar
  um Documento de Entrada
type: support-article
updated_at: '2022-05-16T22:45:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5215430083095-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-RECNO-ao-Estornar-um-Documento-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ao estornar um Documento de Entrada (MATA103) é apresentado o help RECNO  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12  
  
**Solução**O help RECNO ocorre quando o sistema não encontra algum registro relacionado à esta nota no banco de dados.   
  
Alguma manutenção ou alteração na base efetuou tal divergência, a rotina MATA103 se trata de uma tela "Modelo 3" isso significa que a tela é composta por duas tabelas.  
  
No caso, é preciso verificar as tabelas SF1 e SD1, pois as duas perderam o vinculo, a análise/manutenção deve ser efetuada diretamente na base ou inserir novamente os registros.

Após essa verificação, também confirme os dados da Nota, com a origem das seguintes tabelas:  
   
SE2 - Arquivo de Contas a Pagar. Grava os dados da(s) duplicata(s).         
SA2 - Arquivo de Fornecedores. Consultado ou atualizado via [F3].           
SB1 - Arquivo de Descrição Genérica do Produto.                             
SB2 - Arquivo de Saldos Físico e Financeiro.                                   
SC7 - Arquivo com os itens dos Pedidos de Compra.                           
SF3 - Registros Fiscais.                                                   
SF4 - Cadastro de Tipos de Entradas e Saídas (TES).                         
SI1 - Cadastro Plano de Contas.                           
SA1 - Cadastro de Clientes.                                                   
SB6 - Controle de Poder de Terceiros.                                       
SB8 - Arquivo de saldos por lotes. Verificado na operação de exclusão.       
SD5 - Arquivo de requisição por lotes. Verificado na operação de exclusão.  
SM2 - Arquivo de moedas. Verificado na gravação da nota.                     
SD3 - Arquivo de movimentação interna. Verificado na operação de exclusão.  
SF6 - Arquivo de resumo de movimentação da DIPI.                                                                      
SED - Arquivo de Naturezas. Verificado na operação de gravação.  
SEV - Arquivo de Múltiplas Naturezas por Título.  
SRK - Lançamentos Futuros  
SDE - Rateios da Nota Fiscal

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
