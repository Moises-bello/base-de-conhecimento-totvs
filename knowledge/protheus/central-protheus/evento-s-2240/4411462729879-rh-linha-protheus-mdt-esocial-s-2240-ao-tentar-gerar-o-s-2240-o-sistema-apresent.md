---
article_id: 4411462729879
category: Evento S-2240
content_hash: 929c7e882f1ef9da60f5fa790989402e92721ce75ab0a4b378160bf5400f04dd
fetched_at: '2026-06-28T22:45:23.456411+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: 'RH - Linha Protheus - MDT - eSocial - S-2240 - Ao tentar gerar o S-2240 o
  sistema apresenta o aviso: "Os funcionários abaixo não foram comunicados devido
  terem suas categorias definidas no parâmetro MV_NTSV"'
type: support-article
updated_at: '2025-03-03T18:06:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411462729879-RH-Linha-Protheus-MDT-eSocial-S-2240-Ao-tentar-gerar-o-S-2240-o-sistema-apresenta-o-aviso-Os-funcion%C3%A1rios-abaixo-n%C3%A3o-foram-comunicados-devido-terem-suas-categorias-definidas-no-par%C3%A2metro-MV-NTSV
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372484350487)**Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao tentar gerar o S-2240 o sistema apresenta o aviso: "Os funcionários abaixo não foram comunicados devido terem suas categorias definidas no parâmetro **MV\_NTSV**".  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**Isso ocorre porque para categorias de trabalhadores eSocial vinculadas no parâmetro **MV\_NTSV** não existe S-2300. Via de regra são categorias de trabalhadores sem vínculos onde não existe a obrigação de ter um S-2300 no governo, e como não existe o S-2300 governo não é possível gerar o S-2240 para esse trabalhador.  
  
**Solução**Essa mensagem não trata-se exatamente de um erro, mas de um aviso, e para solucionar deve ser analisado as regras de utilização dos Parâmetros **MV\_NTSV** ou **MV\_NG2NENV**.  
Acesse o link: **[Condições em que os Eventos de SST não serão Enviados ao Governo](https://tdn.totvs.com/x/FE9uJQ)**  
  
**Observação**  
Em caso de duvidas na geração dos eventos temos vídeos de exemplo: **[RH - Linha Protheus - MDT - eSocial - Existe vídeos com o passo a passo de geração dos eventos SST (Medicina e Segurança do Trabalho) no eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410314804631)**  
 **Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
