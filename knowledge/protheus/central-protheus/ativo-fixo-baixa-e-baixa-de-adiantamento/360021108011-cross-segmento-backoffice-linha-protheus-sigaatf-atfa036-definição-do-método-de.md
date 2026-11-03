---
article_id: 360021108011
category: Ativo Fixo - Baixa e Baixa de Adiantamento
content_hash: 2b3eb7ecba70cb157b838bd163055fe476764339285215a0a0e17928139ba528
fetched_at: '2026-06-28T22:41:55.518678+00:00'
product: protheus
section_id: 1500001535901
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA036 - DEFINIÇÃO
  DO MÉTODO DE DEPRECIAÇÃO NA BAIXA
type: support-article
updated_at: '2025-08-08T16:52:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021108011-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA036-DEFINI%C3%87%C3%83O-DO-M%C3%89TODO-DE-DEPRECIA%C3%87%C3%83O-NA-BAIXA
---

**Dúvida**

* Como deixar o campo FN6\_DEPREC com default opção 0 (zero) para não depreciar na baixa?
* Depreciação na baixa

**Ambiente**

Protheus – SIGAATF – A partir da versão 12  
  
  
**Solução**

O campo FN6\_DEPREC  irá assumir como default a configuração que esta definida no parâmetro MV\_ATFDPBX

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002854562)

**0 = Não deprecia na baixa**  
**1=Depreciação proporcional na baixa**  
**2=Depreciação total no mês da baixa**[**3=Não Deprecia Baixa/Posteriormente**](https://tdn.totvs.com/pages/releaseview.action?pageId=566481522)

Na rotina de baixa no campo FN6\_DEPREC, permite selecionar se irá ocorrer o calculo da depreciação proporcional ou total, ou não haverá calculo de depreciação

* Selecionando a opção Não **Deprecia na baixa**, não irá ocorrer a depreciação do bem na baixa, porem no calculo da depreciação ao final do mês a depreciação do bem que foi baixado será calculada.
* Selecionando as opções **Deprecia proporcional** ou **Deprecia total na baixa**, será gerada a depreciação do bem no momento da baixa, e ao final do mês no calculo de depreciação não haverá depreciação para este bem(s) baixado(s)
* Selecionando as opções **[Não Deprecia Baixa/Posteriormente](https://tdn.totvs.com/pages/releaseview.action?pageId=566482856)** , não será mais possível deprecia-lo e também não deprecia na baixa do bem

Exemplo:

Bem com valor original de 982 reais.  
  
Com o campo FN6\_DEPREC = 0:  
​![](https://totvssuporte.zendesk.com/attachments/token/ollkf3MKLuFzyydoU5mebuLoi/?name=inline1072997644.png)​  
  
Com o campo FN6\_DEPREC = 1:  
![](https://totvssuporte.zendesk.com/attachments/token/ADU2C4wIfg8sXbAjMTTdfO0op/?name=inline740416281.png)

Veja também o parâmetro [MV\_TIPDEPR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007812091-MP-SIGAATF-ATFA050-Deprecia%C3%A7%C3%A3o-de-Ativo?source=search) referente a periodicidade para o cálculo da depreciação:

0 = Proporcional  
1 = Mês cheio  
2 = Próximo Mês.

 Saiba mais :

* [Bem para venda - CPC31](https://tdn.totvs.com/x/qNfDIQ)
* [MP - SIGAATF - ATFA036: Visualização de Baixas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014647352-MP-SIGAATF-ATFA036-Visualiza%C3%A7%C3%A3o-de-Baixas-?source=search)
* [MP - SIGAATF - BAIXA DE ATIVO - ATFA036](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018556171-MP-SIGAATF-BAIXA-DE-ATIVO-ATFA036?source=search)
* [MP - SIGAATFA - Sistema grava a data base na rotina ATFA036](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024412092-MP-SIGAATFA-Sistema-grava-a-data-base-na-rotina-ATFA036?source=search)
* [Configuração LP para o cálculo da depreciação proporcional, quando está não ocorrer no momento da baixa do Ativo Fixo](https://tdn.totvs.com/pages/releaseview.action?pageId=513411423)
* [DSERCTR1-23008 DT Calculo mensal não realiza o cálculo proporcional do mês depois da baixa](https://tdn.totvs.com/pages/releaseview.action?pageId=510494671)
