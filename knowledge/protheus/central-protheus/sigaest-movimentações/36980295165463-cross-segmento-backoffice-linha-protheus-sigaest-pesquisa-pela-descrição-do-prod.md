---
article_id: 36980295165463
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 0573e76112939be933352770ffcefcb1aaeda5d0e0ec0f9718c1448c661807e6
fetched_at: '2026-06-28T22:38:58.540034+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento – Backoffice (Linha Protheus) – SIGAEST – Pesquisa pela descrição
  do produto na rotina MATA225 não está retornando resultados
type: support-article
updated_at: '2025-12-12T19:25:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36980295165463-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Pesquisa-pela-descri%C3%A7%C3%A3o-do-produto-na-rotina-MATA225-n%C3%A3o-est%C3%A1-retornando-resultados
---

O problema na busca pela descrição do produto na rotina saldo atual pode ocorrer devido ao compartilhamento incorreto da tabela SB1, que deve ser ajustado via Configurador. Essa falha afeta a rotina MATA225 e outras que utilizam campos virtuais, podendo causar efeitos indesejáveis no sistema. Para mais detalhes, consulte o boletim indicado pela TOTVS.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36980295157399) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Ao buscar a descrição do produto na rotina saldo atual, não retorna o resultado esperado na busca. Como corrigir?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Ao fazer a busca pela descrição é necessário avaliar o compartilhamento das tabelas SB1 e SB2, um exemplo de configuração incorreta:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36980298313879)

Na imagem acima, o compartilhamento da tabela SB1 se encontra indevido, o que pode causar falha na busca da descrição pela rotina Saldo Atual (MATA225).

O Problema aparece na rotina MATA225 devido esta usar a tabela SB1 e SB2 em conjunto para carga da descrição do produto, porém outras rotinas e tabelas, que possuem campos virtuais, também podem reproduzir o problema, caso o compartilhamento seja feito indevidamente.

**Abaixo demonstramos o compartilhamento padrão da tabela SB1:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36980371918359)

Observação:

A mudança no compartilhamento da tabela deve ser realizado via Configurador.

O campo de busca no browser é de domínio da equipe de framework e é utilizado em todo o sistema, existe uma hierarquia a ser observada e seguida na configuração dos compartilhamentos de tabelas, que é validada ao pelo configurador, caso sejam feitas de outra forma, isso pode resultar em efeitos indesejáveis em várias rotinas do sistema.

Para maiores informações avaliar esse boletim:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Quais os impactos de alterar compartilhamento de tabelas do Estoque?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17736177052695-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Quais-os-impactos-de-alterar-compartilhamento-de-tabelas-do-Estoque)

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
