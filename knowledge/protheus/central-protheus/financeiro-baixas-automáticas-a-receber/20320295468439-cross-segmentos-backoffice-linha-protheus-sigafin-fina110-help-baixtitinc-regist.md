---
article_id: 20320295468439
category: 'Financeiro - Baixas Automáticas a Receber '
content_hash: bccf37d6e8af9297350cb0a6c7a89f318f2755e2b6835d3d21f6ec392d1f1a3b
fetched_at: '2026-06-28T22:37:38.788336+00:00'
product: protheus
section_id: 35057325714199
source: central-protheus
title: 'Cross Segmentos - BackOffice Linha Protheus - SIGAFIN - FINA110 - HELP: BAIXTITINC
  (registro com filial diferente na SE5)'
type: support-article
updated_at: '2026-01-19T14:31:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20320295468439-Cross-Segmentos-BackOffice-Linha-Protheus-SIGAFIN-FINA110-HELP-BAIXTITINC-registro-com-filial-diferente-na-SE5
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20320295436311) Tempo aproximado para leitura: **03:00 min**  
  
**Dúvida**  
Título a receber SE1 registrado em uma filial, foi realizado baixa automática através da rotina FINA110, gerou movimento de baixa na SE5 em outra filial?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

**Help: BAIXTITINC**

**Problema:** Ao baixar este título ocorreu algum problema (queda de energia, etc.) que impossibilitou a gravação no arquivo SE5. Contate o **SUPORTE MICROSIGA** e informe a ocorrência desse problema.

**Solução:** Verifique alguns dos fatores citados e refaça a operação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20320295445655)

1. Verificar se o campo **E5\_SEQ** referente à última baixa foi gravado com a sequência correta.  
   Como exemplo, a sequência esperada seria **02**, porém consta registrada como **01**.

Para validação, recomenda-se consultar a tabela **SE5** e identificar a gravação da sequência incorreta, comparando-a com um título que não apresentou erro e que possua as mesmas movimentações.

Dessa forma, é possível analisar como a sequência foi corretamente registrada e compará-la com o título que gerou o chamado (Help).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20320295443991)

2) - Para verificar se tem um problema de base, poderá executar "FINC040 - Posição de Títulos a receber"

E verificar se irá apresentar a baixa a receber na posição. Caso não tenha a linha vermelha abaixo irá apresentar o  **Help: BAIXTITINC**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37776486155031)

A empresa terá que verificar se a chave (filial + prefixo + numero + parcela + tipo + cliente + loja) se estão interligadas corretamente entre as tabela SE1 e SE5

Segue uma documentação que orienta como poderá efetuar a validação

**Observação:** A documentação abaixo faz a validação entre SE2 com a SE5, e neste documento por se tratar de contas a receber a validação terá que ser feita entre as tabelas SE1 e SE5.

[**FINA080 - Help: TITNAOXADO ao cancelar a baixa do título**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053001473-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Help-TITNAOXADO-ao-cancelar-a-baixa-do-t%C3%ADtulo)

**Saiba Mais**

[**FINA110 -Baixa Automática de Títulos a Receber**](https://tdn.totvs.com/pages/releaseview.action?pageId=312167132)
