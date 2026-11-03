---
article_id: 18738178366999
category: RH - Folha de Pagamento
content_hash: f3e8f2fbad86bb3e245baef9be0e69b845077cd9898ef4327715be67ef327bfc
fetched_at: '2026-06-28T22:44:12.099198+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de IR para funcionários com múltiplos vínculos
  autônomo carreteiro/ freteiro não considera o modelo de desconto correto.
type: support-article
updated_at: '2024-09-02T20:26:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18738178366999-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-IR-para-funcion%C3%A1rios-com-m%C3%BAltiplos-v%C3%ADnculos-aut%C3%B4nomo-carreteiro-freteiro-n%C3%A3o-considera-o-modelo-de-desconto-correto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18738226984215) Tempo aproximado para leitura: **02:00:00 min****Dúvida**Cálculo de IR para funcionários com múltiplos vínculos autônomo carreteiro/ freteiro não considera o modelo de desconto correto.

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões]  
  
**Solução**  
  
1. Inicialmente verifique o conteúdo do parâmetro **P\_TPAPUIR**;

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052285974-RH-Linha-Protheus-GPE-Apura%C3%A7%C3%A3o-de-IR-no-novo-c%C3%A1lculo-de-m%C3%BAltiplos-v%C3%ADnculos>

Neste caso ele foi definido com 1.

2. Verifique se em seu cadastro de verbas foi cadastrado o identificador de cálculo 1951:<https://tdn.totvs.com/pages/releaseview.action?pageId=763260474>

3. Verifique em seu cadastro de períodos se as datas de pagamento nas filiais correspondentes aos vínculos estão na mesma competência, pois o cálculo do IR considera essa questão.

Filial 01 - processo 00003;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18738178321943)

Filial 02 - processo 00020;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18738238140695)

4. Acesse a rotina GPEM930 para realização do cálculo dos dois vínculos após o lançamento da verba de ID 0218 pela rotina de lançamentos / por funcionários e clique em calcular:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18738218413591)

5. Será gerado um log de cálculo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18738178326935)

6. Conferência de cálculo:

Vínculo 01:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18738210954263)

Vínculo 02:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18738218418199)

Desmembramento de cálculo:

Total de RPA: 35.308,10

IRRF 10%: 3530,81

Total INSS: 776,78

Base de cálculo: 2754,03

Desconto de IR: 48,15

Após seguir esses passos, o sistema considerou o modelo de IR completo conforme esperado para o caso em questão.

**Saiba Mais:**

[RH - Calculo Autonomo/Prolabore](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983113-RH-Calculo-Autonomo-Prolabore)

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

**[RH - Linha Protheus - GPE - Como configurar o cálculo de múltiplos vínculos na versão 12:](http://tdn.totvs.com/pages/viewpage.action?pageId=270911833)<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027693112?source=search>**
