---
article_id: 360034954614
category: Configurador
content_hash: 3c7a8a90e1f4af2efa538bf41e8c06f75cbcc4ab36774f6c01ddacaee174edd4
fetched_at: '2026-06-28T22:42:19.045770+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: Framework - Linha Protheus  - Directory (\Spool\*.rel) exceeded 10000 files
type: support-article
updated_at: '2024-05-08T12:00:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034954614-Framework-Linha-Protheus-Directory-Spool-rel-exceeded-10000-files
---

**[Remover as instruções entre colchetes]**  
 **Ocorrência**Ao analisar console.log do appserver é exibida a mensagem no log directory (\Spool\\*.rel) exceeded 10000 files.  
 **Ambiente**MP – Configurador – A partir da versão 11.8  
   
 **Causa**Conforme documentação abaixo :

<https://tdn.totvs.com/display/tec/Directory>

A função Directory tem uma limitação de apresentar apenas os primeiros 10.000 arquivos, sendo qualquer excedente ignorado.

Portanto qualquer pasta do sistema que contenha mais de 10.000 arquivos causara uma falha onde o sistema não conseguirá exibir todos os arquivos, no caso da pasta spool onde o sistema armazena arquivos de relatórios impressos (\*.rel, \*.html, \*.xml etc.) estes podem ser excluídos pois tratam-se de arquivos temporários do sistema.

Para exclusão dos arquivos não é necessário parar os serviços do ambiente e pode ser realizado com outros usuários utilizando o sistema.

O intuito destes arquivos é serem utilizados em todas as rotinas do sistema no menu miscelâncea -> Spoll, onde será possível imprimir novamente qualquer relatório que já tenha sido impresso anteriormente

**Solução**Executar a limpeza da pasta exibida no erro, deixando a mesma com uma quantidade menor do que 10.000 arquivos.

Artigos relacionados:

<https://tdn.totvs.com/display/tec/Directory>

<https://tdn.totvs.com/pages/releaseview.action?pageId=224455444>
