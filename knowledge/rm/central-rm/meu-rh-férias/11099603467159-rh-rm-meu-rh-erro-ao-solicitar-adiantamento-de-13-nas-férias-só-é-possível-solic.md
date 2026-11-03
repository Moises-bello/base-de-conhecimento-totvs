---
article_id: 11099603467159
category: Meu RH - Férias
content_hash: 1f0f6e976d4e5aaf5b387d39ffe2a25355b8b28b93eb1e94237364990c0f564f
fetched_at: '2026-06-28T22:47:31.645676+00:00'
product: rm
section_id: 1500000835241
source: central-rm
title: 'RH - RM - Meu RH - Erro ao solicitar adiantamento de 13° nas férias: Só é
  possível solicitar a primeira parcela do 13º entre as competências X à Y'
type: support-article
updated_at: '2024-11-12T17:00:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11099603467159-RH-RM-Meu-RH-Erro-ao-solicitar-adiantamento-de-13-nas-f%C3%A9rias-S%C3%B3-%C3%A9-poss%C3%ADvel-solicitar-a-primeira-parcela-do-13%C2%BA-entre-as-compet%C3%AAncias-X-%C3%A0-Y
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:07:00 min****Ocorrência**Ao solicitar adiantamento da 1ª parcela de 13º salário nas férias via Meu RH é apresentado o seguinte erro: **Só é possível solicitar a primeira parcela do 13º entre as competências X à Y.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11099438959511)**  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todos os releases.  
  
**Causa**Esse incidente ocorre, pois a parametrização da Folha de Pagamento está incorreta para a solicitação do adiantamento do 13º salário nas férias.  
  
**Solução**Para solucionar esta situação, realize os seguintes passos:  
  
1. Acesse: **Configurações | Parametrizador | RM Portal | Grupo de Acesso:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11099493912215)  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11099548682903)**2. Em Férias II, o parâmetro deverá estar marcado **Permite solicitar 1° parcela 13° salário**.  
Deverá também ser **configurado corretamente** os campos para indicar o mês inicial e final para realizar o pagamento do adiantamento, vamos detalhar a seguir o funcionamento desses parâmetros:  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11099610743703)  
  
Os parâmetros da primeira coluna, chamados **Mês inicial para solicitar** e **Mês final para solicitar** serão para validar o mês em que o funcionário está solicitando as férias, enquanto aos parâmetros da 2° coluna, **Mês inicial para pagar** e **Mês final para pagar** são para validar o mês inicial de gozo das férias do funcionário.  
  
Para um melhor entendimento, seguem dois cenários de exemplo:  
  
**1° Cenário:**  
-Na Empresa XYZ, somente em **Janeiro** é liberado aos funcionários a solicitar o Adiantamento de 13° salário nas Férias, é liberado as férias que se iniciarem entre Fevereiro à Outubro. Para atender essa necessidade, é necessário configurar os parâmetros da seguinte forma:  
  
- Informado o valor 1 no campo **Mês inicial para solicitar.**- Informado o valor 1 no campo **Mês final para solicitar.**- Informado o valor 2 no campo **Mês inicial para pagar.**- Informado o valor 10 no campo **Mês final para pagar.**Com a configuração acima, quando estiver no mês de **Janeiro**, será liberado a opção de Adiantar 13° das Férias via Meu RH, porém só será permitido, caso a data das férias sugeridas, se iniciar entre os meses de **Fevereiro a Outubro**, diferente disso será retornado o erro mencionado no início dessa documentação.  
  
A partir de **Fevereiro**, será **bloqueado** a opção de adiantamento do 13° nas férias.  
  
**2° Cenário:**  
-Na Empresa ABC, os funcionários podem solicitar o adiantamento do 13° salário em qualquer mês, desde que as férias se iniciem entre **Janeiro à Outubro**. Configuração necessária:  
  
- Informado o valor 1 no campo **Mês inicial para solicitar.**- Informado o valor 12 no campo **Mês final para solicitar.**- Informado o valor 1 no campo **Mês inicial para pagar.**- Informado o valor 10 no campo **Mês final para pagar.**Resultado, independente do mês que estivermos, o funcionário conseguirá solicitar o 13° nas férias, desde que a data de inicio esteja entre **Janeiro á Outubro**, diferente disso será retornado o erro mencionado no início dessa documentação. **Observação:** Caso o funcionário já tenha recebido o adiantamento de 13° salário e solicite novamente o adiantamento em outra sugestão de férias, **o produto não pagará novamente**, sendo um comportamento automático.
