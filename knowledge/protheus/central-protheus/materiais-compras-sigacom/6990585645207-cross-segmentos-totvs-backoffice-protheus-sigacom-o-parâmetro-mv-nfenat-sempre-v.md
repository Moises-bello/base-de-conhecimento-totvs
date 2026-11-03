---
article_id: 6990585645207
category: Materiais - Compras (SIGACOM)
content_hash: 8b123ede6ef601e25fe3c9925a51634a5feb7aff6d8262589916bc3d82c24004
fetched_at: '2026-06-28T22:41:21.965322+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - O parâmetro MV_NFENAT
  sempre valida a obrigatoriedade do preenchimento da natureza no documento de entrada
  ? '
type: support-article
updated_at: '2022-07-25T12:30:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6990585645207-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-O-par%C3%A2metro-MV-NFENAT-sempre-valida-a-obrigatoriedade-do-preenchimento-da-natureza-no-documento-de-entrada
---

**Dúvida**O parâmetro MV\_NFENAT sempre valida a obrigatoriedade do preenchimento da natureza no documento de entrada ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - A partir da versão 12  
  
**Solução**

A resposta para essa pergunta é **Sim.** Sempre que o parâmetro **MV\_NFENAT** estiver com conteúdo **= T** a validação ocorrerá das seguintes formas :

**1-)** *Quando há uma natureza informada no cadastro do fornecedor. Podemos verificar de duas formas*.

**1A-**) Utilizando um formulário próprio = Sim e deletando a natureza que o sistema sugerirá vinda do cadastro do fornecedor. Vide prints abaixo :

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6989963192599/mceclip0.png)

Por algum motivo essa natureza foi deletada no documento de entrada.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6989973161751/mceclip1.png)

Como o formulário próprio está igual a Sim, enquanto o sistema busca a tela para escolher qual o número e série, o campo é novamente preenchido com a natureza que está no cadastro do fornecedor.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6990361640855/mceclip2.png)

**1B-)** Quando o formulário próprio for = Não e mesmo apagando a natureza sugerida do cadastro do fornecedor, ao salvar a nota, o campo ficará preenchido.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6990367915415/mceclip3.png)

Ao salvar a nota e visualizá-la o campo natureza apresentará a natureza informada no cadastro do fornecedor.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6990425316631/mceclip4.png)

**2-**)  *Quando não há uma natureza informada no cadastro do fornecedor e por algum motivo o campo natureza ficar em branco, sem preenchimento ao salvar o documento de entrada o sistema emitirá o help A103NATURE, não permitindo a inclusão da nota sem a informação da natureza.*

*![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6990521035415/mceclip5.png)*

***Saiba Mais :***

***[PÁGINA CENTRALIZADORA DO COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)***

***[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)***
