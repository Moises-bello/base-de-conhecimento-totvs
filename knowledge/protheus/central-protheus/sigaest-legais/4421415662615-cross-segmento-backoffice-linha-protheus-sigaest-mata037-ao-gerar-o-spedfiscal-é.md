---
article_id: 4421415662615
category: SIGAEST - LEGAIS
content_hash: ddf6e64f738a978fadbc3cd06bfe783e15cf53b20c8713aa06e1d253102b25d8
fetched_at: '2026-06-28T22:38:51.697654+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA037 - Ao gerar
  o SPEDFISCAL é apresentando a mensagem: ''Inconsistência no bloco K, Verificar saldo
  de terceiros a Distribuir MATA037'''
type: support-article
updated_at: '2026-05-27T13:54:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421415662615-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA037-Ao-gerar-o-SPEDFISCAL-%C3%A9-apresentando-a-mensagem-Inconsist%C3%AAncia-no-bloco-K-Verificar-saldo-de-terceiros-a-Distribuir-MATA037
---

**Ocorrência**

Ao processar o SPEDFISCAL é apresentando o HELP: ***"Foi lançado Ordem de Produção com tipo E (Externa). Será necessário, através da rotina MATA037, apontar de qual terceiro é esta Produção."***. Como proceder para continuar o processamento do SPEDFISCAL?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16179048761751)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**

A mensagem ocorre quando a OP(Ordem de Produção) está selecionada com o campo C2\_OPTERCE = SIM, dessa forma o Protheus entende que a OP é destinado a terceiro e para a geração do SPEDFISCAL é necessário que realize o apontamento do cliente via rotina MATA037. Caso o campo C2\_OPTERCE  tenha sido preenchido de forma incorreta, deve-se acessar a OP(MATA650) e alterar o campo C2\_OPTERCE para NÃO.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4421420085271)

**Solução**

Para esse cenário pode identificar pela rotina [***DIAGNÓTICO DO BLOCO K (MATC300)***](https://tdn.totvs.com/pages/releaseview.action?pageId=442045336) as Ordens de Produções que estão com inconsistências.

Procedimento para realizar o apontamento de produção de terceiros via MATA037:

**Cadastrar produção terceiros na rotina MATA037**

***- 1 -*** Acessar o modulo Estoque/Custos

***- 2 -*** Acessar o Menu > Movimentações > Internas >Produção > Produção de Terceiros (MATA037)

***- 3 -*** Selecione a Ordem de Produção

***- 4 -*** Clique em Carregar

***- 5 -*** Posicione no produto acabado na grid de produtos

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4421420287383)

***- 6 -*** Na grid de clientes informe os clientes envolvidos  
![](https://tdn.totvs.com/download/attachments/259560085/image2018-10-17_11-19-25.png?version=1&modificationDate=1539785964950&api=v2)

***- 7 -*** Posicione na matéria prima na grid de produtos  
![](https://tdn.totvs.com/download/attachments/259560085/image2018-10-16_10-51-30.png?version=1&modificationDate=1539697889060&api=v2)

***- 8 -*** Na grid de clientes informe os clientes envolvidos  
![](https://tdn.totvs.com/download/attachments/259560085/image2018-10-17_11-20-22.png?version=1&modificationDate=1539786022390&api=v2)

***- 9 -*** Clique em Confirmar

**Importante**: Caso tenha OP's pendentes de apontamento na MATA037, mesmo que elas sejam referentes a períodos anteriores à geração do SPED, elas também irão impactar, neste caso deverá apontar todas elas para que o SPED seja gerado sem erros.

**Saiba mais:**

[*Guia de Referência do Bloco K - TDN*](https://tdn.totvs.com/pages/releaseview.action?pageId=235589625)

[*Link para download do Guia Prático da Escrituração Fiscal Digital - EFD na última versão*](http://sped.rfb.gov.br/pasta/show/1573)

[*MP - SIGAEST- Como definir um tipo de produto que não seja padrão do sistema para que seja considerado no Bloco K (K200)?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033136554-MP-SIGAEST-Como-definir-um-tipo-de-produto-que-n%C3%A3o-seja-padr%C3%A3o-do-sistema-para-que-seja-considerado-no-Bloco-K-K200-?source=search)

[*Clique aqui e veja mais artigos sobre Legais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)
