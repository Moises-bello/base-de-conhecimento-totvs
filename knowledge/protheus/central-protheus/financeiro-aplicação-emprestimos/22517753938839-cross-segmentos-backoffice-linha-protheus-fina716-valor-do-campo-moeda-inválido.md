---
article_id: 22517753938839
category: Financeiro - Aplicação / Emprestimos
content_hash: 02474cee437702378969fe85b27298d9efd56a9eb1b40c222e1cb40ea4c6b1b3
fetched_at: '2026-06-28T22:37:59.347976+00:00'
product: protheus
section_id: 1500001550542
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - FINA716 - Valor do campo Moeda
  * inválido ou não aparece para a seleção
type: support-article
updated_at: '2026-02-12T14:20:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22517753938839-Cross-Segmentos-Backoffice-Linha-Protheus-FINA716-Valor-do-campo-Moeda-inv%C3%A1lido-ou-n%C3%A3o-aparece-para-a-sele%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22517753921303) Tempo aproximado para leitura: **00:05 min**  
  
**Ocorrência**  
Na rotina Aplicação e Empréstimo, ao incluir um contrato, apresenta a mensagem: 'Valor do campo Moeda \* inválido'.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22517748836375)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da versão 12.1.22.10.  
  
**Causa**  
Esse incidente ocorre, pois não possui conteúdo no parâmetro **MV\_SIMB1.**  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o módulo **Configurador** -> **Base de Dados** -> **Dicionário** -> **Bases de Dados.**  
2. Ajuste o parâmetro sem conteúdo **MV\_SIMB1.**

**Exemplo:**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/22518749655703)**

3. Após a alteração, foi possível a inclusão da **Aplicação/Empréstimo**.  
 ![](https://centraldeatendimento.totvs.com/hc/article_attachments/22518749671191)

4. Caso a moeda não apareça para a seleção no campo moeda, mesmo estando cadastrada no cadastro de moedas.

Verifique o conteúdo do parâmetro para a moeda em questão.

**MV\_SIMB1 - Moeda 1**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38354380558359)

**MV\_SIMB2 - Moeda 2**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38354373680279)

**MV\_SIMB3 - Moeda 3**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38354380564375)

**MV\_SIMB4 - Moeda 4**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38354373681559)

**MV\_SIMB5 - Moeda 5**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38354380565271)

Caso o conteúdo esteja em branco, a moeda não vai aparecer para seleção.

**Saiba mais**  
[Aplicações e empréstimos - FINA716 - Financeiro P12](https://tdn.totvs.com/pages/releaseview.action?pageId=680254799)  
[MV\_SIMB - Símbolo utilizado pela moeda 1 do sistema](https://tdn.totvs.com/pages/releaseview.action?pageId=6085230)
