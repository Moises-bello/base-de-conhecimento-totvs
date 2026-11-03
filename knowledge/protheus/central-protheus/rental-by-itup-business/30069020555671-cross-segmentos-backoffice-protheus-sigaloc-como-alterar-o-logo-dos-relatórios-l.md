---
article_id: 30069020555671
category: Rental by ItUp Business
content_hash: f36cfce3a2d1f9b282886c9a25faccf14852a36a433289435e38fdfbeac0be76
fetched_at: '2026-06-28T22:36:20.510671+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Como alterar o logo dos relatórios
  LOCR037 e LOCR038.
type: support-article
updated_at: '2026-04-09T12:54:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30069020555671-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Como-alterar-o-logo-dos-relat%C3%B3rios-LOCR037-e-LOCR038
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30069066838167) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como alterar o logo dos relatórios LOCR037 e LOCR038.  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - A partir da versão P12.1.2310  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

1. Acesse o configurador (**SIGACFG**) >> **Ambiente** >> **Cadastro** >> **Parâmetros**;

2. Localize o parâmetro **MV\_LOCXLOG**;

3. Coloque o caminho para buscar o novo logo do relatório.

```
Observação quando ao Logotipo.

Regra: Pode-se configurar o parâmetro MV_LOCXLOG com a imagem que deseja no logo tipo do 
relatório (exemplo: MV_LOCXLOG = "itup\img\logo.jpg" dentro da pasta raiz "SYSTEM" 
do ambiente). A imagem deve estar no tamanho de 338 x 103 pixels para uma boa apresentação, 
poderá estar no formato BMP,JPG ou PNG.

Caso não esteja configurado o parâmetro ou a imagem não exista será considerada a imagem que
está configurada para a empresa na pasta System (exemplo: (grl01.bmp) ou para empresa 
(lgrl.bmp), seguindo a ordem acima da preferência.
```
