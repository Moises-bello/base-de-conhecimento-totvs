---
article_id: 37856390101783
category: eSocial - Eventos Totalizadores
content_hash: ede3356c6eaef53fca90888aac350f08ac6dd8381e1937e2068d804012310819
fetched_at: '2026-06-28T22:47:06.958414+00:00'
product: rm
section_id: 1500000834481
source: central-rm
title: RH - RM - FOP- eSocial - Divergência de Previdência Oficial do Relatório de
  Conferência IRRF S-5002
type: support-article
updated_at: '2026-05-08T18:25:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37856390101783-RH-RM-FOP-eSocial-Diverg%C3%AAncia-de-Previd%C3%AAncia-Oficial-do-Relat%C3%B3rio-de-Confer%C3%AAncia-IRRF-S-5002
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37856390090647) Tempo aproximado para leitura: **00:03:00min**  
  
**Ocorrência**  
Ao gerar o **Relatório de Conferência IRRF S-5002**, pode aparecer uma diferença entre os valores da folha e do governo no campo **Previdência Oficial** e/ou **Previdência Oficial 13º**, como mostrado na imagem abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37856368736023)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**  
O campo **Previdência oficial** leva em consideração os seguintes códigos de incidência de IRRF (*codIncIRRF*) informados através do evento S-1010: **41** - Previdência Social Oficial - PSO - Remuneração mensal; **43** - PSO - Férias. Já o campo **Previdência oficial 13º** leva em consideração a seguinte incidência de IRRF (*codIncIRRF*): **42** - PSO - 13º salário.

Sendo assim, geralmente ocorrem divergências no relatório quando tais incidências estão **incorretas** e/ou **diferentes** entre Folha e Governo.

Veja na documentação abaixo outras possíveis causas do erro:  
     - [**Middleware - Como validar divergências no Relatório de Conferência (IRRF) - Informações Complementares**](https://tdn.totvs.com/pages/viewpage.action?pageId=1062889046)  
  
**Solução**  
Em 2023, com a inclusão do IRRF no eSocial, foi necessário realizar **uma revisão nos valores de incidência** de INSS (*codIncCP*) e IRRF (*codIncIRRF*) no evento S-1010. Essa revisão foi aplicada a partir dos patches 12.1.2302.240, 12.1.2306.187, 12.1.2310.121.

Sendo assim, verifique no Governo, em **Tabelas | Rubricas**, se o valor da incidência **está correto conforme detalhamento abaixo**:

|  |  |
| --- | --- |
| **CÓDIGO DE CÁCULO** | **CODINCIRRF****VALOR CORRETO** |
| [3 - I.N.S.S.](https://tdn.totvs.com/pages/viewpage.action?pageId=452718215) | **41** |
| [11 - I.N.S.S. de 13º Salário](https://tdn.totvs.com/pages/viewpage.action?pageId=452718209) | **42** |
| [68 - INSS DE DIFERENÇA SALARIAL](https://tdn.totvs.com/pages/viewpage.action?pageId=452718219) | **41** |
| [82 - I.N.S.S. Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=452718205) | **43** |
| [85 - I.N.S.S. calculado pelo usuário](https://tdn.totvs.com/pages/viewpage.action?pageId=452718201) | **41** |
| [92 - Restituição de I.N.S.S.](https://tdn.totvs.com/pages/viewpage.action?pageId=452719626) | **41** |
| [103 - I.N.S.S. 2ª parc. 13º Salário](https://tdn.totvs.com/pages/viewpage.action?pageId=452718233) | **42** |
| [108 - INSS DE DIF SALARIAL DE 13º](https://tdn.totvs.com/pages/viewpage.action?pageId=452718958) | **42** |
| [110 - INSS DE DIF SALARIAL DE FÉRIAS](https://tdn.totvs.com/pages/viewpage.action?pageId=452718218) | **43** |
| [141 - INSS Férias no mês (informado)](https://tdn.totvs.com/pages/viewpage.action?pageId=452718223) | **43** |
| [153 - Restituição de I.N.S.S. 13º](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718762) | **42** |
| [159 - INSS de férias outro emprego](https://tdn.totvs.com/pages/viewpage.action?pageId=452718222) | **9** |
| [171 - INSS 13º Sal descontado p/ previd ref lic maternide](https://tdn.totvs.com/pages/viewpage.action?pageId=452718206) | **42** |
| [185 - INSS DE FÉRIAS PROXIMO MÊS OUTRO EMPREGO](https://tdn.totvs.com/pages/viewpage.action?pageId=452719942) | **9** |
| [193 - INSS DE FÉRIAS MÊS ANTERIOR OUTRO EMPREGO](https://tdn.totvs.com/pages/viewpage.action?pageId=452719896) | **9** |
| [205 - INSS Descontado RRA](https://tdn.totvs.com/pages/viewpage.action?pageId=452718220) | **9** |
| [209 - INSS Descontado RRA Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=452719900) | **9** |
| [213 - INSS Descontado RRA 13º Salário](https://tdn.totvs.com/pages/viewpage.action?pageId=452719681) | **9** |
| [89 - I.N.S.S. com alíquota normal](https://tdn.totvs.com/pages/viewpage.action?pageId=452718204) | **9** |
| [90 - I.N.S.S. Férias com alíquota normal](https://tdn.totvs.com/pages/viewpage.action?pageId=452718959) | **9** |
| [91 - I.N.S.S. 13º c/ alíquota normal](https://tdn.totvs.com/pages/viewpage.action?pageId=452718212) | **9** |
| [137 - I.N.S.S. Fér. Próx. mês c/ alíq. normal](https://tdn.totvs.com/pages/viewpage.action?pageId=452718228) | **9** |
|  |  |
| **CÓDIGO DE CÁCULO** | **CODINCCP****VALOR CORRETO** |
| [142 - INSS Férias próx. mês (informado)](https://tdn.totvs.com/pages/viewpage.action?pageId=452718227) | **0** |
| [153 - Restituição de I.N.S.S. 13º](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718762) | **32** |

A mesma validação deve ser realizada nas verbas informadas em [**Configurações | Parametrizador | eSocial | Configurações Gerais 6/7**](https://tdn.totvs.com/pages/viewpage.action?pageId=540899121), e [**Configurações | Parametrizador | eSocial | Configurações Gerais 7/7**](https://tdn.totvs.com/pages/releaseview.action?pageId=645896860)  conforme abaixo:

|  |  |  |
| --- | --- | --- |
| **CAMPOS PARAMETRIZADOR** | **CODINCCP****VALOR CORRETO** | **CODINCIRRF****VALOR CORRETO** |
| Evento INSS Férias envelope | **31** | **9** |
| Evento INSS Férias Próximo Mês envelope | **00** | **9** |
| Evento INSS Antecipação de Férias (Desconto) | **00** | **43** |

|  |  |
| --- | --- |
| **CÓDIGO DE CÁCULO** | **CODINCIRRF****VALOR CORRETO** |
| [Código de Cálculo 130 - INSS Férias Próximo Mês](https://tdn.totvs.com/pages/viewpage.action?pageId=452718229) | **43** |
| [Código de Cálculo 131 - INSS Férias Desconto Mês Anterior](https://tdn.totvs.com/pages/viewpage.action?pageId=452718225) | **9** |
| [Código de Cálculo 349 - INSS Férias no Terceiro Mês](https://tdn.totvs.com/pages/viewpage.action?pageId=452719459) | **43** |

Verifique se seu ambiente está atualizado e siga o processo apresentado na documentação abaixo caso seja **necessário ajustar a incidência de alguma das verba**s:

* [FAQ - Como ajustar os valores das tags <codIncCP> e <codIncIRRF> para Conferência da DIRF no eSocial](https://tdn.totvs.com/pages/viewpage.action?pageId=1037965223)

**Saiba mais**  
Veja também a documentação abaixo:

* [Mapeamento de eventos - S-1010](https://tdn.totvs.com/display/LRM/Evento+S-1010)
