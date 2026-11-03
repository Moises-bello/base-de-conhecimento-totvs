---
article_id: 21829540916247
category: Gestão de Distribuição (SIGAOMS)
content_hash: a3ebd322540c0d14f083f778fbcbd52d751de553e9fc7d24b4038f1456ca5431
fetched_at: '2026-06-28T22:45:49.640435+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Como converter unidade de medida do Sistema
  para unidade em Quilo - Kg
type: support-article
updated_at: '2025-05-24T13:16:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21829540916247-Log%C3%ADstica-Linha-Protheus-OMS-Como-converter-unidade-de-medida-do-Sistema-para-unidade-em-Quilo-Kg
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21829540868375) Tempo aproximado para leitura: **00:02:00min** **Dúvida** Como converter unidade de medida do Sistema para unidade em **Quilo - Kg**, utilizando o programa **OMSA140 - Fator de Conversão**?  
  
**Ambiente**  
TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) – Todas as versões.  
**Solução**No envio dos Pedidos de Venda ao **TOL/TRE**, existem validações por conta do Portal do **TOL/TRE**, as quais não permitem quantidades de produtos com valores com casas decimais. A única unidade de medida aceita é o quilo. Portanto, a integração disponibiliza o cadastro **OMSA140 - Fator de Conversão** para ser utilizado em qualquer unidade de medida do Sistema para converter na unidade quilo. Este cadastro é exclusivo da integração do **TOTVS OMS** com **o TOL/TRE**.  
  
Para que o **TOTVS OMS** envie o valor convertido é necessário cadastrar as unidades de medidas utilizadas e associar seu valor em quilo, na unidade **Kg**.  
Para realizar o cadastro, acesse **SIGAOMS** > **Atualizações** > **TOTVS Otimização Logística** > **Fator de Conversão - OMSA140**, sendo necessário realizar esse cadastro para todas as unidades de medidas dos produtos que serão utilizadas na integração, cuja relação de peso não seja em **Kg**.  
  
Exemplo de cadastro: **OMSA140 - Fator de Conversão**Campo **Unidade - DK2\_CODUM:** TL - tonelada  
Campo **Peso em KG - DK2\_PESOKG:** 1000.  
Significa que a cada **uma tonelada** são **1000 Kg**.

![omsa140.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/21830341548183)

![omsaa140 2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/21830341562903)

**Importante**Temos um arquivo com explicação sobre o **Tipo e o Fator de Conversão**. Nele contém alguns exemplos com diversas unidades de medida do Sistema convertendo para **quilo - Kg**.  
  
**Saiba mais**Mais informações sobre a rotina **OMSA140** e a integração do **TOTVS OMS****com o TOL/TRE**, consulte os *links*:  
[Fator de Conversão - OMSA140](https://tdn.totvs.com/pages/viewpage.action?pageId=572013656)   
[Integração TOTVS OMS x TOTVS Otimização Logística](https://tdn.totvs.com/pages/viewpage.action?pageId=268801735)**Anexo**
