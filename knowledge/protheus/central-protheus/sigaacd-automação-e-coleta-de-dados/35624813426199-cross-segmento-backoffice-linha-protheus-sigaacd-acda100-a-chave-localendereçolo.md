---
article_id: 35624813426199
category: SIGAACD - Automação e Coleta de Dados
content_hash: 5ec40da9c1134e6b3a013e225e47077c845c3da67ece8d31d0191aa08993910b
fetched_at: '2026-06-28T22:39:11.187442+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - ACDA100 - A chave
  Local+Endereço+lote+Sublote+Num.Serie já foi informada em outra linha
type: support-article
updated_at: '2025-10-30T11:28:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35624813426199-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDA100-A-chave-Local-Endere%C3%A7o-lote-Sublote-Num-Serie-j%C3%A1-foi-informada-em-outra-linha
---

Ao alterar empenhos via ACDA100 no TOTVS Protheus, ocorre erro de chave duplicada impedindo salvar mesmo sem saldos a informar. A correção permite sair da rotina ao salvar se não houver saldos. Atualize para versões 12.1.2210, 12.1.2310, 12.1.2410 ou 12.1.2510 e realize backup antes da atualização.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35624813413015) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Ao alterar o empenho via ACDA100 ocorre "A chave Local+Endereço+lote+Sublote+Num.Serie já foi informada em outra linha"  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.   
  
**Solução**  
Ao alterar os empenhos de um item de uma Ordem de Separacao, e exibida a validacao de existencia da chave, quando o botao Salvar e acionado. E isso impede o usuario de sair da rotina, mesmo quando nao ha saldos a ser informados para separacao.

Implementada na validacao da chave se ha existencia de saldo a informar para validacao. Caso nao haja saldos, sera permitido sair da rotina de Altera Empenhos utilizando do botao Salvar.

12.1.2210:<https://r.totvs.io/p/1203589> ;

12.1.2310:<https://r.totvs.io/p/1203590> ;

12.1.2410:<https://r.totvs.io/p/1203588> ;

12.1.2510:<https://r.totvs.io/p/1203591> ;

É importante atualizar seu produto constantemente, mantendo-o sempre na última versão disponível no Portal de Clientes ([Central de Download](https://suporte.totvs.com/portal/p/10098/download#000006/all/)), a fim de contemplar todas as melhorias e correções disponibilizadas.  
  
Efetuar o Backup antes da atualização.  
Todos os procedimentos devem ser realizados primeiro em ambiente TESTE atualizado.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
