---
article_id: 1500004461822
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 7b93c5536facbe582fac91c84f77a9f1810f89841422b72c937fb02a184e872f
fetched_at: '2026-06-28T22:38:56.917278+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA240/MATA241 -
  Campo D3_OBS não aparece mais. Como resolver?
type: support-article
updated_at: '2022-07-15T20:07:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004461822-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA240-MATA241-Campo-D3-OBS-n%C3%A3o-aparece-mais-Como-resolver
---

**Dúvida**Ao acessar às rotinas de Movimentação Simples - MATA240 ou Movimentação Múltipla - MATA241, o campo D3\_OBS não aparece mais. Como resolver para reaparecer o campo?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**O campo D3\_OBS tem uma finalidade especifica para ser usado em rotinas com o módulo **DCL (Distribuidores de Combustíveis e Lubrificantes)** implantado e isso foi alterado nas últimas atualizações das rotinas de Movimentação Simples e Múltipla, por esse motivo não aparece mais o campo em tela para o visualização e edição por parte do usuário.  
  
A mudança tem embasamento na documentação abaixo;

**[9215415 DMANMAT01-29509 DT Proteger campo D3\_OBS para uso apenas no DCL](https://tdn.totvs.com/display/public/PROT/9215415+DMANMAT01-29509+DT+Proteger+campo+D3_OBS+para+uso+apenas+no+DCL)**

**Existe forma para habilitar o campo novamente?**

Para continuar utilizando o campo, seria necessário deixar o parâmetro **MV\_DCLNEW = .T.**  
Porém, ao ativá-lo, o sistema vai apresentar alguns campos como obrigatórios, como por exemplo o campo C5\_MODANP na rotina Pedido de Venda - MATA241

**Observação**: Caso não tenha o módulo de DCL e ative este parâmetro, pode-se causar outros erros devido estar ativando um modulo que a empresa não utiliza.

**Existe alguma outra alternativa para preencher Observação em Movimentações?**

Recomendamos que passe a utilizar o campo **D3\_OBSERVA**no lugar do **D3\_OBS**, desta forma não terá a necessidade de habilitar o parâmetro MV\_DCLNEW e consequentemente evitará problemas/erros/retrabalhos derivados da ativação deste parâmetro em outros processos/rotinas.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
