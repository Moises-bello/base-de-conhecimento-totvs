---
article_id: 4914049476503
category: Materiais - Compras (SIGACOM)
content_hash: 1b1a1395d3c583c7b0e0feacf89a85d6ced65078071038cc4ecec4e66a34b300
fetched_at: '2026-06-28T22:41:17.623053+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Protheus - SIGACOM - Erro log cadastro de
  fornecedor (MATA020) variable is not an object  on MODELDEF(MATA020MBRA.PRW).
type: support-article
updated_at: '2022-03-21T18:52:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4914049476503-Cross-Segmentos-TOTVS-Backoffice-Protheus-SIGACOM-Erro-log-cadastro-de-fornecedor-MATA020-variable-is-not-an-object-on-MODELDEF-MATA020MBRA-PRW
---

**Ocorrência**Ao fazer alteração ou incluir um fornecedor aparece o erro log de início:

variable is not an object on MODELDEF(MATA020MBRA.PRW)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões  
  
**Causa**[Exemplo:  
Esse incidente ocorre, pois a parametrização do sistema está incorreta para o Cálculo da Substituição Tributária na entrada de NF.]  
  
**Solução**

Efetue o procedimento abaixo:  
  
Favor verificar se não existe nenhum fonte chamado **MATA020**.**PRW** em seu repositório.  
  
Caso tenha, por favor, descompile o mesmo, pois no repositório deve existir somente o **MATA020.PRX** com o nome de **MATA020**.  
  
Se não tiver o arquivo MATA020.PRW em seu projeto para descompilar (excluir), basta criar um novo arquivo em branco no TDS ou IDE, salvá-lo com o nome de MATA020.PRW, jogar no seu projeto e descompilar.

Após este procedimento de descompilação (caso seja necessário), faça uma nova validação e veja se o erro foi corrigido.

Segue link do TDN com explicação: [Pontos de Entrada MVC MATA020 na P12](http://tdn.totvs.com/display/PROT/ADV0044_PE_MVC_MATA020_P12)

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
