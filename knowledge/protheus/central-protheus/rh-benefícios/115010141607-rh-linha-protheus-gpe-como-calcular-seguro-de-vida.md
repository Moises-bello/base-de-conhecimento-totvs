---
article_id: 115010141607
category: RH - Benefícios
content_hash: 0c239efc9841f24f70f86b5504dd3615b0c6ea2bff6d6efe5affe9fedf4706a3
fetched_at: '2026-06-28T22:44:03.734360+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular Seguro de Vida
type: support-article
updated_at: '2025-09-25T12:06:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115010141607-RH-Linha-Protheus-GPE-Como-calcular-Seguro-de-Vida
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32618272646807)****Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**Como realizar cálculo de Seguro de Vida na rotina de Outros Benefícios?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**Para o cálculo de seguro de Vida, realize os seguintes passos:

1. Acesse o **cadastro de Verbas** em **Atualizações/ Definições de Cálculo/ Verbas**  
2. Ajuste as verbas com Identificador de cálculo 0153 e 0154 conforme *prints* abaixo:

![CADASTRO DE VERBAS 1.jpg](https://tdn.totvs.com.br/download/attachments/235580457/CADASTRO%20DE%20VERBAS%201.jpg?version=1&modificationDate=1461285183000&api=v2)

![](https://tdn.totvs.com.br/download/attachments/235580457/CADASTRO%20DE%20VERBAS%202.jpg?version=1&modificationDate=1461285185000&api=v2)

![](https://tdn.totvs.com.br/download/attachments/235580457/CADASTRO%20DE%20VERBAS%203.jpg?version=2&modificationDate=1461285186000&api=v2)

![](https://tdn.totvs.com.br/download/attachments/235580457/CADASTRO%20DE%20VERBAS%204.jpg?version=1&modificationDate=1461285187000&api=v2)  
  
3. Acesse a **Definição de Benefícios** em **Atualizações/ Benefícios/ Outros Benefícios/ Definições de Benefícios;**  
  
4. Informe dados de acordo com o Benefício de sua organização e clique em salvar;

![](https://tdn.totvs.com.br/download/attachments/235580457/defini%C3%A7%C3%A3o%20de%20beneficio%201.jpg?version=1&modificationDate=1461285189000&api=v2)  
![](https://tdn.totvs.com.br/download/attachments/235580457/defini%C3%A7%C3%A3o%20de%20beneficio%202.jpg?version=1&modificationDate=1461285190000&api=v2)  
  
Preenchimento dos campos:  
  
**Código:** Defina um código de identificação do benefício.  
**Descrição:** Atribua uma descrição ao benefício.  
**Salário Até ou Quantidade de Salário Mínimo:** Informe o valor de salário limite para o recebimento do benefício, escolhendo entre salário até ou quantidade de salário mínimo.  
**Tipo Referência:** Escolha entre três tipos de cálculo para o benefício: valor fixo, percentual salário base ou percentual salário mínimo.  
**Referência:**Informe o valor de referência que será utilizado no cálculo  
**% Pagamento Funcionário:** Informe o percentual de pagamento do funcionário (Com base no campo Referência)  
**Tipo de Desconto:**Selecione entre as opções de Percentuais (Benefício, Salário Base e Salário Mínimo)  
**Desconto do Funcionário:** Defina o percentual de desconto do funcionário   
**Cód Verba:** Informe a verba de pagamento (se houver)  
**Verba Desc.:** Informe a verba de desconto funcionário (se houver)  
**Verba Empres:** Informe a verba parte empresa (se houver)  
**Proporc:** Informe se o valor do benefício será calculado baseado nos dias trabalhados no mês  
**Pag. Falta:** Informe se haverá o pagamento do benefício quando houver faltas  
  
**Importante:** O campo **% Pgto Func** é obrigatório. Caso não preencha o sistema não realiza o calculo.

5. Acesse a **Manutenção de Benefícios** em **Atualizações/ Benefícios/ Outros Benefícios/ Manutenção;**  
  
6. Selecione funcionário que receberá o benefício, insira informações e clique em confirmar;

![](https://tdn.totvs.com.br/download/attachments/235580457/manuten%C3%A7%C3%A3o%20de%20benef%C3%ADcios.jpg?version=1&modificationDate=1461285195000&api=v2)

7. Acesse a rotina de **Cálculos** em **Atualizações/ Benefícios/ Outros Benefícios/ Cálculo:**  
  
8. Informe parâmetros de cálculo para roteiro **BEN** e clique em ok;

![](https://tdn.totvs.com.br/download/attachments/235580457/calculo.jpg?version=1&modificationDate=1461285188000&api=v2)

9. Visualize o cálculo de duas formas:  
  
**-**Individualmente, acessando: **Atualizações/ Benefícios/ Outros Benefícios/ Manutenção**, selecione o funcionário desejado e clique **Outras Ações/ Visualização do Cálculo.**  
-Em Relatório, acessando: **Atualizações/Benefícios/Outros Benefícios/Relatório Cálculo  
![ben02.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/115017019948)**

10. Realize a integração do roteiro BEN na Folha de Pagamento em **Atualizações/ Benefícios/ Outros Benefícios/ Integração com a Folha;**

![](https://tdn.totvs.com.br/download/attachments/235580457/integra%C3%A7%C3%A3o.jpg?version=1&modificationDate=1461285192000&api=v2)

11. Confira a **integração** em **A****tualizações/ Lançamentos/ Por Funcionário:**

![](https://tdn.totvs.com.br/download/attachments/235580457/lan%C3%A7amento%20mensal.jpg?version=1&modificationDate=1461285193000&api=v2)

**Identificadores de Cálculo**0153 - SEGURO VIDA GRUPO     
0154 - BASE PART EMP SEG VID  
0155 - BASE SEGURO VIDA

**Exemplos de Cálculo:**

**Salario Base**% Pgto func = 5,00  
Salário do empregado = R$ 2.800,00  
Valor do Benefício = 2.800,00 \* 5% = 140,00     
Este valor ficará no Campo **Valor do Benefício** no relatório.  
  
**Salario Mínimo**% Pgto func = 5,00  
Salário Mínimo definido em Manutenção de Tabelas = R$ 1.045,00  
Valor do Benefício = 2.800,00 \* 5% = 52,25     
Este valor ficará no Campo **Valor do Benefício** no relatório.

**Valor Fixo**  
Exemplo % Pgto func = 99,99  
Valor fixo = 10,70  
Valor do Benefício = 10,70 \* 99,99% =  10,70  
Este valor ficará no Campo **Valor do** **Benefício** no relatório.

**Saiba Mais**[Documentação técnica](https://tdn.totvs.com.br/pages/releaseview.action?pageId=235580457)  
[RH - Linha Protheus - GPE - Seguro de vida 100% pago pela empresa](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063687013-RH-Linha-Protheus-GPE-Seguro-de-vida-100-pago-pela-empresa?source=search)  
[RH - Linha Protheus - GPE - Como parametrizar o mnemônico P\_SALOUBEN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050645454-RH-Linha-Protheus-GPE-Como-parametrizar-o-mnem%C3%B4nico-P-SALOUBEN?source=search)  
[RH - Linha Protheus - GPE - Como fazer o cadastro de Outros Benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058024473-RH-Linha-Protheus-GPE-Como-fazer-o-cadastro-de-Outros-Benef%C3%ADcios?source=search)  
[RH - Linha Protheus - GPE - É possível realizar o cálculo de 1 benefício quando o funcionário tem 2 cadastrados no Sistema](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051664373-RH-Linha-Protheus-GPE-%C3%89-poss%C3%ADvel-realizar-o-c%C3%A1lculo-de-1-benef%C3%ADcio-quando-o-funcion%C3%A1rio-tem-2-cadastrados-no-Sistema?source=search)
