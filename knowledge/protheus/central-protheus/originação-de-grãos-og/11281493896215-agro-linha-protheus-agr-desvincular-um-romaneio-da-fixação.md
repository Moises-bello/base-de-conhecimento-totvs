---
article_id: 11281493896215
category: Originação de Grãos (OG)
content_hash: b65f0aaef71cc480c0d2f8de98e7ec4178ba5f77a3fa3b2b3f35003352ed9347
fetched_at: '2026-06-28T22:45:39.023264+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Desvincular um romaneio da fixação
type: support-article
updated_at: '2025-06-23T15:55:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11281493896215-Agro-Linha-Protheus-AGR-Desvincular-um-romaneio-da-fixa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20351216577303) Tempo aproximado para leitura: **00:01:55 min** **Dúvida**Como **desvincular** um **romaneio** da **fixação**, que não tenha havido ajuste de pendencia?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**Para **desvincular** o **romaneio** da **fixação**, não pode ter havido o ajuste da pendência, por padrão não temos função para desfazer o processo de ajuste de pendencia permitindo **desvincular** o **romaneio** da **fixação**.  
Caso seja necessário **desvincular** após ajuste de pendencia, é necessário analisar qual ajuste de pendencia foi realizado, e realizar o processo inverso, desfazendo os ajustes e inclusões realizados.  
É Recomendado a analise de um consultor.  
Abaixo segue um resumo do processo de ajuste, mas pode ter mais tabelas envolvidas como por exemplo, o **titulo tenha sido processado**, **tenha havido devolução da NF romaneio ajustado**, **tenha ordem de pagamento recebimento.**  
  
Ajuste de Pendencia de **fixação**, **Gestor de entidade - OGA450** e  **OGA430A - Ajuste de Pendencia**   
Quando vincula o **romaneio** na **fixação**, gera registro na tabela **Fixacao x Entregas - NNC**, e a partir desta tabela lista os **romaneio** na grid de entregas da **fixação**.

**NNC\_STATUS = 5 - VR Fixação a menor, Requer ajuste Financeiro - OGA430D** verifica a tabela **NNC**  
Se **venda** altera via **Contas a Receber - FINA040**, ajustando **Contas a Receber -** **SE1 E1\_DECRESC - Valor do Decrescimo** com o valor de ajuste - tabela **Cabeçalho das NF de Entrada - SF1**, **SE1** ...  
Se **compra** altera via **Contas a Pagar - FINA050**, ajustando **Contas a Pagar - SE2 E2\_DECRESC - Valor do Descrescimo** com o valor de ajuste - tabela **Cabeçalho das NF de Saída -** **SF2**, **SE2** ...

- Inclui registro tabela **DOCTOS AJUSTE DIFS. NA FIXACAO - NKC**  
- ajusta registro tabela **Fixacao x Entregas - NNC** com o valor do ajuste

**NNC\_STATUS = 1**  **Requer NF complemento Próprio - OGA430B** verifica a tabela **NNC**  
**Se venda**, gerar NF de complemento gerando pedido e NF - tabelas **Pedidos de Venda - SC5**, **Itens dos Pedidos de Venda - SC6**, **Cabeçalho das NF de Saída -** **SF2**   
**Se compr**, incluir documento de entrada - tabelas **Cabeçalho das NF de Entrada - SF1**, **Itens das NF de Entrada -** **SD1**, **Contas a Pagar - SE2**  
- Incluir registro tabela **NKC**  
- Ajustar registro tabela **NNC**

**NNC\_STATUS = 2** - **Requer NF complemento Produtor - OGA430C**  verifica a tabela NNC  
- Busca as NF de complemento que tem como nota de origem as notas do **romaneio** com pendencia para listar na tela - tabela **SD1** - é necessário que a nota de origem tenha sido incluída via **Documento de Entrada - MATA103**  
- No ajuste gera o **romaneio** simbólico com a nota de complemento - tabelas do **Romaneio - NJJ**, **Dados Fiscais do Romaneio - NJM**, **Classificacoes do Romaneio -** **NJK** etc...  
- Incluir registro tabela **NKC**  
-Ajusta registro tabela **NNC**
