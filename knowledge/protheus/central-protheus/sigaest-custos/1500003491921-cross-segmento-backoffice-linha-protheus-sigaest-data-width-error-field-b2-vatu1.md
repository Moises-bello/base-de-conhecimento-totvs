---
article_id: 1500003491921
category: SIGAEST - CUSTOS
content_hash: fef61f499b0b32f3cac063ca87e30245fffd12e59eed8b72331aefd81c2b603d
fetched_at: '2026-06-28T22:39:00.883038+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Data Width error
  - Field: B2_VATU1/2/3/4/5 Como resolver?'
type: support-article
updated_at: '2026-02-27T22:22:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003491921-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Data-Width-error-Field-B2-VATU1-2-3-4-5-Como-resolver
---

O erro "Data width error" nos campos B2\_VATU1 a B2\_VATU5 no Protheus ocorre quando o valor excede o limite do campo. Para resolver, remova moedas não utilizadas do parâmetro MV\_MOEDACM ou ajuste o valor/custo negativo via movimentação valorizada. Alternativamente, aumente o tamanho dos campos no configurador para evitar o estouro.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38426654984855) Tempo aproximado para leitura: **00:04:15 min**

**Dúvida**

Em rotinas de processamentos como o Recálculo do Custo Médio - MATA330, ocorre o error.log apontando *"Data Width error - Field: B2\_VATU1 / B2\_VATU2 / B2\_VATU3 / B2\_VATU4 / B2\_VATU5 / B2\_VFIM1 / B2\_VFIM2 / B2\_VFIM3 / B2\_VFIM4 / B2\_VFIM5".* Como resolver este problema de estouro de campo em outras moedas?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Normalmente o erro "Data width error - Field: B2\_VATU2" (por exemplo se o estouro fosse neste campo) ocorre quando o sistema está tentando gravar um valor maior que a configuração do campo pode suportar.

**Como resolver?**

O primeiro passo é validar se utiliza por padrão aquela moeda.

Se não utilizar a moeda cujo campo aponta o estouro, basta removê-lo do parâmetro [**MV\_MOEDACM.**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087443)

Se por exemplo o estouro for no campo B2\_VATU2 e a Moeda 2 não for utilizada no seu ambiente, basta acessar ao parâmetro MV\_MOEDACM e retirar o valor 2 da relação das moedas.

Caso tenha resíduos de moedas**,** [**clique aqui e saiba como limpá-los**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016789291)

**Caso utilize a moeda ao qual apontou o estouro do campo:**

**1° Proposta de Solução:** Ajuste de Estoque por Movimento Valorizado para acerto do custo negativo

Normalmente estes erros ocorrem quando o custo está extremamente negativo. Vamos usar o exemplo o erro abaixo:

***Data width error - Field: B2\_VATU2 Value: -1022318108.853568 on B2ATUCOMD2(SIGACUSA.PRX)***

Neste caso, criamos um Tipo de Movimentação (TM) valorizada, através da rotina MATA230

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003692161)

Acessamos à rotina MATA240 para criar a Movimentação do ajuste do valor de -1022318108.853568 no Custo na 2° moeda:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003692301)

**Obs**: Note que o campo "Custo" refere-se à Moeda 1. Como não é possível criar Movimento com Custo na Moeda 1 = 0,00, basta inserir 1 centavo para que consiga prosseguir com a movimentação.

Conclusão: desta forma, o custo na Moeda 2 é zerado e o processamento não gerará mais o estouro.

**2° Proposta de Solução:** Aumentar o tamanho do(s) campo(s) referido(s).

Acesse o módulo "Configurador (SIGACFG) >> Base de Dados >> Dicionário >> Base de Dados" para coletar qual grupo o campo referido pertence.

No exemplo abaixo, usamos o campo B2\_VATU1:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38700268463383)

Após coletar o grupo, deve-se realizar o processo descrito na documentação abaixo, para que seja alterado o tamanho do grupo (alterando assim também todos os campos relacionados):  

[Grupo de Campos Numéricos](https://tdn.totvs.com/x/JVo9L)

Com o ajuste do tamanho do grupo, ele não dará o mesmo erro de outrora.

**Observação**: As mesmas propostas de soluções valem para campos de Quantidade (B2\_QATU, B2\_QFIM), precisando apenas em se atentar à efetuar os procedimentos no grupo numérico relacionado à quantidade).

***Saiba mais:***

[**Clique aqui e veja artigos sobre Processamentos no Estoque**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033442-SIGAEST-PROCESSAMENTOS)

[**Clique aqui e veja artigos sobre Custos no Estoque**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000049222-SIGAEST-CUSTOS)

[**MP - SIGAEST - Data width error - Estouro de campo de Valor em outras moedas**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016789291-MP-SIGAEST-Data-width-error-Estouro-de-campo-de-Valor-em-outras-moedas?source=search)

[**MATA330 - Como aumentar a quantidade de Casas Decimais para os campos de CUSTOS**](https://tdn.totvs.com/x/ziwNF)

[**Precisao de calculo - Custo médio**](https://tdn.totvs.com/x/HhYCMQ)

[**Grupo de Campos Numéricos**](https://tdn.totvs.com/x/JVo9L)
