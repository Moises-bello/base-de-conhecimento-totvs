---
article_id: 360016520832
category: ADVPL - Classe e Função
content_hash: bcde36164c340931702cbd8d6de31f16757167e0481faaff5439729e34c9ef97
fetched_at: '2026-06-28T22:40:19.340042+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Função fgeraverba
  gera erro em variável DDATAATE
type: support-article
updated_at: '2022-01-10T17:34:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016520832-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-fgeraverba-gera-erro-em-vari%C3%A1vel-DDATAATE
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Temos uma verba específica em folha, e desenvolvemos uma rotina para inserir estes descontos através da função **fgeraverba**. No entanto estamos recebendo o erro:

```
THREAD ERROR ([10400], Focus, R430-APP) 26/09/2018 08:15:58   
variable does not exist DDATAATE on FMATRIZ(GPEXCALC.PRX) 
```

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) - ADVPL – A partir da versão 11.80  
  
**Solução**Não é possível utilizar a função **Fgeraverba** fora do roteiro de calculo, conforme documentação O erro ocorre devido a **ddataate** ser uma variável do sistema e é alimentada no roteiro de calculo.  
" Incluir ou Alterar uma Verba no Movimento durante o cálculo."  
  
**Saiba mais**  
[Roteiro - Função FGeraVerba - Parâmetros e Exemplo](http://tdn.totvs.com/pages/releaseview.action?pageId=6079039)  
[GPE026FORMU\_EXEMPLO FGERAVERBA\_\_P12](http://tdn.totvs.com/display/PROT/GPE026FORMU_EXEMPLO+FGERAVERBA__P12)
