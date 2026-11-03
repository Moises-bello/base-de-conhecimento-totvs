---
article_id: 360052767993
category: SIGAEST - PODER DE TERCEIROS
content_hash: adbd2497817774c88c2b2adac11fd0b2841ab0abc1c2e839de8ebb6d3f8c96d4
fetched_at: '2026-06-28T22:39:03.280049+00:00'
product: protheus
section_id: 1500001538881
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus -SIGAEST - É possível requisitar
  ou consumir Saldo de Terceiro no meu Estoque?
type: support-article
updated_at: '2024-05-27T18:36:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052767993-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEST-%C3%89-poss%C3%ADvel-requisitar-ou-consumir-Saldo-de-Terceiro-no-meu-Estoque
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23769699094679) Tempo aproximado para leitura: 00:01:30 min**

**Dúvida**Consta o Saldo de Terceiro (B2\_QTNP) no estoque, é possível requisitar ou movimentar esse saldo?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084420093)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

É possível requisitar e movimentar Saldo de Terceiro em nosso poder, abaixo mostraremos como efetuar:

**Rotinas MATA260 e MATA261**

Deve-se, ao acessar tais rotinas, revisar o parâmetro F12 relacionado ao Saldo de Terceiros, abaixo um exemplo na rotina MATA261 ou MATA260. O parâmetro **"Subtrai Saldo Terce. N. Poder"** deve estar configurado igual a **"Não"**.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083265054)

**Exemplo:**

**1° - Possuímos o produto PA10. Com isso, daremos um Saldo Inicial (MATA220) de 100 unidades no armazém 01;**  
**2° - Recebemos uma remessa DE terceiros de 50 no armazém 01;**  
**3° - Com isso ficamos, no armazém 01, com B2\_QATU = 150 e B2\_QTNP = 50(saldo de terceiros compondo o Saldo Atual);**  
**4° - Então, queremos levar esses 50 DE terceiros do meu armazém 01 para o armazém 02;**  
**5° - Então iremos na rotina de Transferência (MATA260/MATA261) e no F12, no campo "Subtrai Saldo Terc. N. Poder?" deixaremos com conteúdo "Não";**  
**6° - Faremos então a transferência de 50 unidades do Armazém 01 para o Armazém 02 do meu PA10;**  
**7° - Com isso, ficará assim:**

**Arm 01: B2\_QATU = 100 e B2\_QTNP = 50**

**Arm 02: B2\_QATU = 50 e B2\_QTNP = 0**

**Isso quer dizer que, a transferência em si não vai manipular o campo B2\_QTNP. Porém, isso não vai impedir de usar estes 50 na devolução.**

**8° - Ao fazer a devolução ao terceiro, por meio da rotina MATA410, selecionaremos o produto conforme a entrada, TES de devolução para o terceiro e seleciono o Armazém 02. Salvo e preparo o documento de saída normalmente;**  
**9° -Ao fazer o processo acima (baixa de terceiro), ficará assim:**

**Arm 01: B2\_QATU = 100 e B2\_QTNP = 0**

**Arm 02: B2\_QATU = 0 e B2\_QTNP = 0**

**Ou seja, o sistema permite devolver o saldo utilizando o armazém 02 e baixou o B2\_QTNP do armazém 01.**

**Rotinas MATA240 e MATA241**

Outro exemplo é nas rotinas MATA241 ou MATA240. O parâmetro **"Cons. Saldo De 3º N/Poder?"** deve estar configurado igual a **"Sim"**.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083270174)

Destas formas, é possível requisitar saldos de terceiro em nosso poder.

**Observação:**é importante se atentar pois, um saldo de terceiro em nosso poder, em algum momento provavelmente voltará ao terceiro. Neste caso, ao fazer a devolução ao terceiro, avaliar se utilizará uma TES que atualiza estoque ou não, para não gerar uma inconsistência no saldo do estoque.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Poder de Terceiros no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012199513-SIGAEST-PODER-DE-TERCEIROS)*
