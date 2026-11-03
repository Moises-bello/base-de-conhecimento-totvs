---
article_id: 360038120993
category: RH - Dissídio
content_hash: 4110f63890b5fca878cd2fa4a90b3523dc591efd19e81cbe67e73da409c560b0
fetched_at: '2026-06-28T22:43:44.272142+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Não é demonstrado a verba de adicional dentro do
  cálculo de dissídio, deixando as demais verbas negativas
type: support-article
updated_at: '2025-08-20T14:30:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038120993-RH-Linha-Protheus-GPE-N%C3%A3o-%C3%A9-demonstrado-a-verba-de-adicional-dentro-do-c%C3%A1lculo-de-diss%C3%ADdio-deixando-as-demais-verbas-negativas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34317157679767) Tempo aproximado para leitura: 00:01:30 min**

**Dúvida**Ao realizar o calculo de dissídio não é demonstrado a verba de adicional (periculosidade, insalubridade, tempo de serviço, confiança e transferência), ainda que exista o pagamento na folha. Como consequência todas as verbas calculadas sobre salário + adicional demonstram valores de diferença negativos.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12  
  
**Solução**1. Verifique através do cadastro de funcionário se o mesmo ainda possuí direito ao adicional:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360050251873)  
  
2. Verifique se o sindicato vinculado a esse funcionário tem a aba de adicional configurada, nesse exemplo estamos utilizando o adicional de insalubridade:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360050251973)  
  
Se em algum momento houve alteração no seu cadastro de sindicato, nos campos localizados dentro das abas de adicionais e principalmente nos meses que serão recalculados na rotina de dissídio, a mesma terá influência direta no cálculo gerado. Veja a documentação abaixo:  
<https://tdn.totvs.com/x/hB4MEQ>  
  
3. Verifique se a verba de adicional foi devidamente calculada na folha do funcionário, a origem da verba irá informar se a mesma foi calculada pelo sistema ou foi informada pelo usuário. A letra **C** indica que o cálculo foi realizado pelo sistema:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049364294)  
  
Caso a folha esteja fechada, o valor pode ser consultado através do recibo de pagamento (GPEA630) ou acumulados (GPEA120).  
  
4. Cálculo do dissídio:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049364694)  
  
Para execução do cálculo de dissídio é necessário seguir todos os passos do manual abaixo:  
[MP - GPE - Manual do dissídio retroativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034578653-MP-GPE-Manual-do-diss%C3%ADdio-retroativo-?source=search)  
  
5. Complemento do passo número 1 e **principal causa do erro**:  
Quando o conteúdo de algum campo é alterado dentro do cadastro de funcionário (GPEA010) essa alteração é gravada dentro da tabela SR9 de acordo com a **data base do sistema**. Para o cálculo de dissídio a primeira tabela consultada pelo sistema é a SR9 para saber exatamente em que momento o funcionário teve alteração cadastral.  
O funcionário que utilizei como exemplo foi admitido já com o adicional de insalubridade, por esse motivo, assim que confirmei o cadastro foi gerado 4 linhas relacionada aos campos de adicional, sinalizados na imagem do passo número 1. A tabela SR9 ficou dessa forma:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360050253233)  
  
Nessa imagem podemos ver que no dia 01/01/2019 o funcionário **não**tinha o adicional de insalubridade (linhas não sinalizadas) e no mesmo dia **adquiriu** o adicional de insalubridade (linhas sinalizadas).  
Caso o funcionário adquirisse qualquer adicional meses depois da data de sua admissão as linhas sinalizadas, teriam uma data diferente.  
  
5.1 Caso o funcionário não tenha nenhuma informação relacionada ao adicional dentro da tabela SR9:  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049365554)  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360050254013)  
  
Não existindo informação de alteração cadastral (SR9) a próxima tabela consultada pelo sistema é a SRA - Cadastro de funcionário, que, como pode ser visto no primeiro passo tem os campos de adicional preenchido.  
  
5.2 Caso não exista a informação que o funcionário adquiriu o adicional a partir de X data:  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360050254033)  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049365974)  
  
Como dito anteriormente o sistema abre a tabela SR9 e encontra apenas a informação que o funcionário não tem direito ao adicional, então ainda que exista a verba dentro da folha de pagamento, o sistema entende que o funcionário não tem direito ao adicional pois não foi informado a partir de quando (data) o mesmo adquiriu.  
  
5.3 Caso as datas estejam incorretas dentro da tabela SR9:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049377194)  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360050267593)  
  
Com essas informações o sistema entende que no dia 20/12/2018 o funcionário adquiriu o adicional de insalubridade, porém a partir do dia 01/01/2019 não teve mais o direito. Como essa é a última alteração até o mês 10/2019 - mês que será recalculado o dissídio, o sistema entende que não deve calcular o adicional dentro do dissidio.  
  
**Importante:**  
Dentro de alguns cenários é possível corrigir as informações dentro da tabela SR9 pelo próprio sistema, retroagindo a data base do sistema anterior ao mês calculado na rotina de dissídio e realizando a alteração dentro do cadastro do funcionário.  
  
**Saiba Mais**  
Tem outra dúvida? Consulte além do manual, o link abaixo:  
  [https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio](https://www.google.com/url?q=https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%25C3%25ADdio&sa=D&source=hangouts&ust=1572529678699000&usg=AFQjCNFW7PMX5N2Z4WRgKDwi8PLEi62E2g)
