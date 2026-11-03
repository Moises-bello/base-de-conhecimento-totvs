---
article_id: 360007974992
category: RH - Cálculos
content_hash: 60c08a939e4f640ee693bc6de69d345205c2aad96adaefb932e273685e65ce78
fetched_at: '2026-06-28T22:44:51.586854+00:00'
product: protheus
section_id: 32419138773655
source: central-protheus
title: RH - Linha Protheus  - PON - Funcionalidade da pergunta Agrupa Eventos no Cálculo
  Mensal
type: support-article
updated_at: '2025-06-13T18:45:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007974992-RH-Linha-Protheus-PON-Funcionalidade-da-pergunta-Agrupa-Eventos-no-C%C3%A1lculo-Mensal
---

**Dúvida:**Funcionalidade da pergunta Agrupa Eventos no Cálculo Mensal.  
  
**Ambiente:**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução:**Essa pergunta foi criada para, quando o cliente escolher realizar cálculo mensal semanal por exemplo, sempre sendo determinante a opção selecionada na pergunta Agrupa Eventos:  
  
**1º cenário:**Agrupar Eventos = SIM  
Ao selecionar "SIM", caso a verba que esteja sendo calculada já tenha sido gerada anteriormente, as informações de valor e referência serão somadas.Esta opção deve ser utilizada para realizar o cálculo mensal por partes, por exemplo:  
Período do ponto : 25/03 a 24/04;  
Calcule do dia 25/03 a 31/03 com a data base do sistema com data de 24/04 e depois em outro momento calcular do dia 01/04 a 24/04 com data base do sistema com data de 24/04 também, assim os eventos serão somados e não substituídos.  
Observação:A cada cálculo realizado é efetuado o incremento dos resultados, ou seja, não haverá sobreposição de lançamentos mesmo que pertencentes ao mesmo período.  
Por isso, nesse caso, oriento que nunca repitam dias que já foram anteriormente calculados.  
  
**2º cenário:**Agrupar Eventos = NÃO  
Ao escolher a opção NÃO, o sistema se comportará sem alterações, ou seja, toda vez que realizar o cálculo o resultado será substituído pelo novo valor.  
Nessa opção, recomendo sempre utilizar a parametrização do período de apontamento completo, no caso do nosso exemplo de 25/03 a 24/04.  
  
**Saiba Mais:**Agrupa Eventos: <http://tdn.totvs.com/pages/releaseview.action?pageId=382538588>
