---
article_id: 1500002547841
category: SIGAEST - MOVIMENTAÇÕES
content_hash: ea18e0e6f0018715c8661b801d435d53116ab6c351316734d30acf30cc49f558
fetched_at: '2026-06-28T22:38:53.960145+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como realizar a Transferência
  de Saldos entre Armazéns?
type: support-article
updated_at: '2025-11-19T16:57:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002547841-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-realizar-a-Transfer%C3%AAncia-de-Saldos-entre-Armaz%C3%A9ns
---

O artigo explica como realizar a Transferência de Saldo de Produtos entre Armazéns no TOTVS Protheus usando a rotina Transferência Múltipla (MATA261). O processo permite transferir saldos entre armazéns, códigos de produtos, lotes e endereços. O usuário deve acessar a rotina, incluir os dados de origem e destino, e salvar a transferência, quando nunca movimentado saldo em determinado Armazém pode criar saldo automaticamente no armazém de destino ajustando o parâmetro MV\_VLDALMO para N.

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36446327879959)** Tempo aproximado para leitura: **00:05:00 min**

[**How To | MP - SIGAEST – Transferências entre Armazéns (MATA261)**](https://www.youtube.com/watch?v=-C05diWV9D4)

**Dúvida**

Como realizar a Transferência de Saldo de Produtos entre Armazéns?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Esse processo, no padrão pode ser realizado pela rotina **Transferência Múltipla (MATA261)** que permite ao usuário transferir Saldo dos Produtos com as seguintes opções padrões:

 - Transferência de Saldos**entre Armazéns;**

 - Transferência de Saldos de **um Código de Produto para outro Código Produto;**

**-**Transferência de Saldos de um**Lote para outro Lote de determinado Código de produto ou mesmo para Códigos de Produtos diferentes;**

**-**Transferência de Saldos entre **Endereços quando Produto controla Localização (B1\_LOCALIZ=S)**

**Exemplo prático abaixo efetuando a Transferência entre Armazéns**

**- Vídeo com exemplo na prática:**[**How To | SIGAEST – Transferências entre Armazéns (MATA261)**](https://www.youtube.com/watch?v=-C05diWV9D4)

Também abaixo um passo a passo sobre esse processo:

**- 1° -** Para efetuar, basta acessar à rotina de Transferência entre Transferência entre Armazéns Múltiplas (MATA261), através do caminho: **Atualizações -> Movimentações -> Internas -> Transferência Múltipla**

**- 2° -** Nesta documentação usaremos o exemplo acessando à Transferência Simples, ou seja, MATA261.

![MATA261 01.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/36446327881367)

- 3° - Clique em "Incluir"

![MATA261 02.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/36446327885975)

**- 4° -** Se o armazém de destino nunca teve saldo para o produto e deseja que seja criado automaticamente o saldo no ato da transferência sem incluir Saldo Inicial alterar o parâmetro **MV\_VLDALMO para N**, veja [***neste link***](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020863311-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-%C3%89-poss%C3%ADvel-criar-saldo-do-produto-no-armaz%C3%A9m-de-destino-na-Transfer%C3%AAncia-de-Produtos) a funcionalidade desse parâmetro.

**- 5° -** Na rotina MATA261, após clicar em "Incluir" na janela para definir a transferência. Basta inserir o produto na Origem e Destino, além do Armazém Origem e Destino com a Quantidade a ser transferida, No print abaixo demonstramos uma Transferência somente de Saldo de Saldo físico quantidade 10 do Armazém 01 para o Armazém 02 do mesmo código de produto:

![MATA261 03.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/36446327888663)

**- 6° -** Após clicar em Salvar, basta conferir se o saldo foi transferido como desejado. Veja o resultado por exemplo no print abaixo, onde transferiu o Saldo de quantiade 10 do Armazém 01 para o Armazém 02:

![MATA261 04.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/36446327890071)

**Saiba mais:**

[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)

[**How To | MP - SIGAEST – Transferências entre Armazéns (MATA261)**](https://www.youtube.com/watch?v=-C05diWV9D4)
