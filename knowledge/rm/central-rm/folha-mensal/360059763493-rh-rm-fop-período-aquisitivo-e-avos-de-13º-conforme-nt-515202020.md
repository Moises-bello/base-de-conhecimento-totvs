---
article_id: 360059763493
category: Folha Mensal
content_hash: 06f8b96ef4f12febd64150a7005d4c9de13eb9e8d64635849f7a5b4110f9e84a
fetched_at: '2026-06-28T22:46:59.480886+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Período aquisitivo e avos de 13º conforme NT 51520/2020
type: support-article
updated_at: '2025-03-07T13:59:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059763493-RH-RM-FOP-Per%C3%ADodo-aquisitivo-e-avos-de-13%C2%BA-conforme-NT-51520-2020
---

**Dúvida**

Quais as adequações no sistema devem ser realizadas conforme a regra contida Nota Técnica do Ministério da Economia 51520/2020?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

* 12.1.26.259
* 12.1.27.241
* 12.1.28.150
* 12.1.29.1

**Solução**

O MPT possui um entendimento baseado na literalidade da lei e do princípio do *in dubio* pro operário ao definir que tanto nos casos de suspensão do contrato de trabalho quanto de redução de jornada/salário não há influência no cálculo nem do décimo terceiro salário[,](https://www.contabeis.com.br/trabalhista/decimo_terceiro_salario/) tampouco do período aquisitivo de férias.  
  
Desse modo temos os seguintes cenários:  
  
**Redução de jornada**

Durante o ano, o funcionário teve uma redução de jornada, consequentemente diminuindo o salário. Como será o pagamento do 13° Salário?

Exemplo: Salário até Junho era R$2000,00 e Jornada 220 (Salário Hora: 9,09). Em julho, a jornada foi reduzida para 180 e salário alterado para 1636,36 (Salário Hora: 9,09). (Desse modo no sistema foi alterado o salário no campo Cadastro do Funcionário | Salário/Jornada).

Quando o funcionário tem redução de salario e jornada, para que seja realizado o pagamento referente as férias e o 13º salário com o salario antigo até a data da redução da jornada, terá que fazer a rescisão resilição, onde o funcionário irá receber os avos proporcionais ao salario antigo.

Caso não seja realizado essa rescisão, em dezembro, o funcionário irá receber os 12 avos de 13º salário sobre o salário reduzido, pois o sistema não proporcionaliza os avos com o salário antigo.

Documentação do processo:

[Resilição](https://tdn.totvs.com/pages/releaseview.action?pageId=284854431)  
  
**Obs:** Caso o salário se mantenha o mesmo, e apenas feita a redução lançando o evento de desconto para realizar o desconto no Líquido do funcionário como foi orientado pelo material [MP 936 - Redução Proporcional de Jornada de Trabalho e Salário](https://tdn.totvs.com/pages/releaseview.action?pageId=545621517), o procedimento é o padrão para lançamento da primeira e segunda parcela do 13º, onde não terá nenhuma mudança.

Segue documentação:

[RM - FOP - 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020075531-RM-FOP-13%C2%BA-Sal%C3%A1rio?source=search)

**Suspensão temporária de contrato**

O sistema já contempla a rotina localizada em Configurações | Parametrizador | Folha de Pagamento | Folha Normal | Afastamento 2/2 onde pode-se parametrizar o comportamento tanto para férias quanto para 13º salário, cabendo ao usuário somente utilizar conforme a necessidade e entendimento.  
  
**Parametrizando para a Suspensão Temporária manter o período aquisitivo de férias e os avos do 13º salário:**  
**![](https://tdn.totvs.com/download/attachments/545621865/image2020-7-30_19-5-39.png?version=1&modificationDate=1596146739647&api=v2)**  
Marcando esses parâmetros e informando o motivo de afastamento que será utilizado no afastamento do funcionário, serão mantidos o cálculo do período aquisitivo de férias e os avos de direito ao 13º salário para o período afastado pelo motivo C – Contrato Suspensão.  
  
**Exemplo:** 

Mês competência 05/2020 – Parâmetros marcados e motivo preenchido com 1 – Com perda de avos  
  
Funcionário 1 – Período aquisitivo de 02/01/2020 a 01/01/2021 – Afastamento de 01/03/2020 a 29/04/2020 – 60 dias - Motivo de afastamento 1 – Com perda de avos  
  
Funcionário 2 – Período aquisitivo de 02/01/2020 a 01/01/2021 – Afastamento de 01/03/2020 a 29/04/2020 – 60 dias - Motivo de afastamento 2 – Sem perda de avos  
  
**Executando o acerto de período aquisitivo:**

Funcionário 1 – Período aquisitivo de 02/01/2020 a 02/03/2021 – Período estendido porque o motivo de afastamento era o mesmo do parametrizador.  
  
Funcionário 2 – Período aquisitivo de 02/01/2020 a 01/01/2021 – Período não foi estendido porque o motivo de afastamento não era o mesmo do parametrizador.  
  
**Calculando 13º salário em dezembro/2020:**

Funcionário 1 – 10 avos – Perda de 2 avos porque o motivo de afastamento era o mesmo do parametrizador.  
  
Funcionário 2 – 12 avos – Avos completos porque o motivo de afastamento não era o mesmo do parametrizador.  
  
Para a rescisão contratual deverá ser executado o acerto de período aquisitivo primeiro, pois assim o período aquisitivo estará correto no momento do cálculo. E o cálculo do 13º salário rescisão seguirá da mesma forma que o 13º salário normal.

Caso o período aquisitivo já tenha sido executado e estendido adicionando os avos de Suspensão a data fim, segue o link para realizar os ajustes: [RM - FOP - Período Aquisitivo estendido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058298973-RM-FOP-Per%C3%ADodo-Aquisitivo-estendido)  
  
**Saiba mais:**

[Nota Técnica SEI nº 51520/2020/ME](https://tdn.totvs.com/pages/releaseview.action?pageId=572731699)
