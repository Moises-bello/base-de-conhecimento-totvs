---
article_id: 360051811934
category: ADVPL - Classe e Função
content_hash: bafc69340983eeb462e501d1a277c74641a829f9ff90125e92d0d72281cc436d
fetched_at: '2026-06-28T22:40:14.544643+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Caracteres especiais:Como
  validar '
type: support-article
updated_at: '2025-12-09T14:26:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051811934-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Caracteres-especiais-Como-validar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como validar a existência de um carácter especial, por exemplo "º"?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução****Não existem** uma função que tenha essa responsabilidade.  
Para isso, pode-se criar um *loop* iterando cada caractere da string e verificar assim se trata-se do caractere especial que se deseja, utilizando por exemplo a função **SubStr** para pegar somente um caractere da string.  
A verificação pode ser feita diretamente com o dado obtido, ou convertendo o mesmo para numérico, com a função **Asc**, depende de forma de implementação e resultado que deseje ser obtido.
