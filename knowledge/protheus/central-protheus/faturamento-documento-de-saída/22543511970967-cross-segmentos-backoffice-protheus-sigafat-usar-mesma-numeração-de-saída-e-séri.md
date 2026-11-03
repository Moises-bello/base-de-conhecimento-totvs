---
article_id: 22543511970967
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 6af156b0f596e2d1af29e5fc80b1f109efb15d331e87a6d0c17f4bb17c5714e8
fetched_at: '2026-06-28T22:38:44.177028+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Usar mesma numeração de saída
  e série na mesma filial
type: support-article
updated_at: '2024-04-04T12:37:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22543511970967-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Usar-mesma-numera%C3%A7%C3%A3o-de-sa%C3%ADda-e-s%C3%A9rie-na-mesma-filial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22543501076503) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como usar mesma numeração de saída e série na mesma filial sem dar erro?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**O Protheus não aceitará a mesma série e numeração exatas, utilizar a mesma numeração e série na mesma filial que já exista uma nota faturado com mesma numeração e série gerará inconsistências e erros.

**Solução 1:**  
É necessário criar uma nova série com o mesmo código da série anterior sufixando ou prefixo com uma pontuação, exemplo:

* A série que quer usar a mesma numerações é a série "1", deve ser criado e utilizado a série ".1" (com ponto na frente)

A) Faça a série no configurador como ".1" (ponto na frente) e use as numerações desejadas. A SEFAZ tem tratamento para retirada de pontuações e caracteres especiais das séries e numerações.  
  
B) Assim, ".1" será diferente de "1" e não dá erros!

**Solução 2:**

A) Criar uma nova filial e faturar com a numeração e série desejados.

**OBSERVAÇÃO:** Para a solução 1, importante ressaltar que dentro do sistema Protheus já está sendo esperado e tratado isso para que não haja problemas, e a SEFAZ remove pontuações indevidas no meio do caractere, (quando sair do Protheus e ir para o servidor da SEFAZ).

**Saiba mais:**

[FAQ - Como incluir notas fiscais com mesmo número, série, código e loja de fornecedor/cliente?](https://tdn.totvs.com/x/WnoNLw)

[Cross Segmentos -TOTVS Backoffice (Linha Protheus) - SIGAFAT - Criação de série de NFs para utilizar em Documentos de Saída](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020162851-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Cria%C3%A7%C3%A3o-de-s%C3%A9rie-de-NFs-para-utilizar-em-Documentos-de-Sa%C3%ADda)
