---
article_id: 28596229245975
category: Gestão de Transportes (TMS)
content_hash: a846605a5bc5adad54f60452171414edfcacc93028d1138cfdf88ae3c316d25b
fetched_at: '2026-06-28T22:45:29.454600+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Não é possível determinar o Frete Mínimo
type: support-article
updated_at: '2026-02-23T19:59:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28596229245975-Log%C3%ADstica-Linha-Protheus-TMS-N%C3%A3o-%C3%A9-poss%C3%ADvel-determinar-o-Frete-M%C3%ADnimo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28596204753175) Tempo aproximado para leitura: **00:02:20 min**  
  
**Dúvida**  
O que fazer quando ocorrer o *help* **Não é possível determinar o Frete Mínimo** ao integrar com a **Pamcard** e como funciona o cálculo do **Frete Mínimo**?   
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões.  
  
**Solução**  
A [PORTARIA Nº 20, DE 28 DE AGOSTO DE 2023](https://www.in.gov.br/en/web/dou/-/portaria-n-20-de-28-de-agosto-de-2023-506347574) especifica a **Tabela de Frete Mínimo do Transporte Rodoviário de Cargas** a ser utilizada, considerando Tipo de Carga, Coeficiente de custo, Unidade e Número de eixos carregados do veículo combinado.  
  
A mensagem **Não é possível determinar o Frete Mínimo** ocorre de maneira informativa quando não há valor definido na **Tabela de Frete Mínimo do Transporte Rodoviário de Cargas** para a operação, considerando o **Tipo de Carga** e **Número de eixos carregados dos veículos combinados.**  
  
Por exemplo, a viagem possui apenas um veículo de 3 eixos e o tipo de carga é Granel sólido. Nesse cenário, não há um valor mínimo definido na tabela da ANTT, então a consulta de frete mínimo não encontrará valores, e irá apresentar a mensagem **Não é possível determinar o frete mínimo** para o usuário em caráter informativo apenas, essa mensagem não impede a continuidade do processo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37114828778007)

No **Protheus** **TMS**, o Tipo de Carga é definido pelo **TMSA039 - Cadastro de Tipo de Operação da Viagem**, o qual é vinculado a viagem pelo campo **DTQ\_TPOPVG - Tipo de Operação da** **Viagem**, especificamente no campo **DLO\_CODTPC - Cod.Tp.Carga**.  
  
O número de eixos carregados do veículo combinado é a soma de eixos dos veículos utilizados na viagem. Cada veículo possui a quantidade de eixos em seu cadastro no campo **DA3\_QTDEIX - Qtde.Eixos** e a soma dos eixos dos veículos na viagem são gravados no campo **DTR\_QTDEIX - Qtde.Eixos** da viagem.  
  
**Saiba mais**  
Documentação do Frete Mínimo: [Frete Mínimo Pamcard (SIGATMS) - Exemplo de utilização](https://tdn.totvs.com/pages/releaseview.action?pageId=573202032)  
Documentação do Tipo de Operação da Viagem: [DT Tipo de Operação da Viagem](https://tdn.totvs.com/pages/releaseview.action?pageId=425443149)
