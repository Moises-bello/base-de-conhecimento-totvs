---
article_id: 115009236627
category: ADVPL - Classe e Função
content_hash: 20ee8f5bd0b38bc7ff29edaba5339408a56461d556ed31f5aa12ed1f4de2be6a
fetched_at: '2026-06-28T22:40:14.146402+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Erro invalid macro
  source
type: support-article
updated_at: '2021-09-01T14:49:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115009236627-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-invalid-macro-source
---

**Dúvida**Error log invalid macro source, como corrigir?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL – Todas versões  
  
**Solução**O erro específico "invalid macro source (SSYacc0105e: Error token failed, no valid token) :(STATICCALL(#**FUNCAO\_DO\_USUARIO**,MenuDef)) on FWLOADMENUDEF(PROTHEUSFUNCTIONMVC.PRX)" começou a ocorrer após as atualizações de lib, disponibilizadas no inicio de 2017. O motivo é que foi realizado uma alteração no fonte FWLOADMENUDEF para, no caso de não estar como usuário administrador, macroexecutar as funções afim de validá-las, e como a função de usuário começa com '#' ele gera o erro. Anteriormente a essa alteração já havia sido implementado o TYPE 03, que é específico para funções de usuário, não mais utilizando o '#' para essa finalidade.  
Para que não gere mais o erro verifique nos arquivos XNU a chamada de uma função de usuário se está com # ((#**FUNCAO\_DO\_USUARIO**) e TYPE como 01(função Protheus), retire o '#' e altere o TYPE para 03 conforme instruções a seguir:

Errado:  
<Function>#**FUNCAO\_DO\_USUARIO**</Function>  
<Type>01</Type>

Certo:  
<Function>**FUNCAO\_DO\_USUARIO**</Function>  
<Type>03</Type>

Observação  
Caso persista verifique se o nome do fonte está com caractere especial ou iniciando por número.  
  
**Saiba mais**  
[ADV0013 Erro invalid macro source](http://tdn.totvs.com/display/PROT/ADV0013_FUN_Erro_invalid_macro_source)
