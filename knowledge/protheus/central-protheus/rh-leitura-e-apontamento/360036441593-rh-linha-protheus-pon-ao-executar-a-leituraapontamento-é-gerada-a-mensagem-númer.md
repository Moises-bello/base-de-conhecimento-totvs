---
article_id: 360036441593
category: RH - Leitura e Apontamento
content_hash: 776ae9598ee8a0c7b7d82a190431982d760b6c14077c54b82fd0468523d32ad4
fetched_at: '2026-06-28T22:44:45.872948+00:00'
product: protheus
section_id: 32419281460119
source: central-protheus
title: RH - Linha Protheus - PON -  Ao executar a Leitura/Apontamento, é gerada a
  mensagem - Número de Marcações divergentes do Totalizador
type: support-article
updated_at: '2026-04-01T11:31:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036441593-RH-Linha-Protheus-PON-Ao-executar-a-Leitura-Apontamento-%C3%A9-gerada-a-mensagem-N%C3%BAmero-de-Marca%C3%A7%C3%B5es-divergentes-do-Totalizador
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31782435345175) Tempo aproximado para leitura: 00:01:00 min****

**Dúvida**Ao executar a Leitura/Apontamento, é gerada a mensagem no log de ocorrências: **Número de Marcações divergentes do Totalizador:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047846553)****Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Na Leitura/Apontamento, a mensagem é apresentada quando o arquivo TXT gerado pelo relógio está com **divergência no totalizador** de marcações, que trata-se da última linha do arquivo.   
Este totalizador exibe quantas linhas do arquivo possuem marcação de ponto, desconsiderando cabeçalho, rodapé e demais movimentações do funcionário como inclusões e exclusões do cadastro do relógio.  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20801411226135)  
  
Nestes casos, como o arquivo TXT é extraído através de ***software* do fabricante** do relógio, o problema deve ser verificado diretamente com o fabricante.  
Se necessário, encaminhe o seu TXT  juntamente com a Portaria [1510](https://www.trt2.jus.br/geral/tribunal2/ORGAOS/MTE/Portaria/ANEXOI_PORT_1510_MTE.pdf) e/ou [671](https://in.gov.br/en/web/dou/-/portaria-359094139) do MTE que informa qual *layout* deve ser seguido.  
  
  
**Saiba Mais:**[Layout - Portaria 671](https://in.gov.br/en/web/dou/-/portaria-359094139)  
[Layout - Portaria 1510](https://www.trt2.jus.br/geral/tribunal2/ORGAOS/MTE/Portaria/ANEXOI_PORT_1510_MTE.pdf)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
