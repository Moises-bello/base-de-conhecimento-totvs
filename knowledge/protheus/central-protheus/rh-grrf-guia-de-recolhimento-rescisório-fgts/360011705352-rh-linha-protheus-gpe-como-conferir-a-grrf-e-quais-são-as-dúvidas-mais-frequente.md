---
article_id: 360011705352
category: RH - GRRF (Guia de Recolhimento Rescisório - FGTS)
content_hash: c867ffa592939070a2ce1874f2475b7d61021d51257efb3d952db9153d8cb144
fetched_at: '2026-06-28T22:43:32.334781+00:00'
product: protheus
section_id: 360010781714
source: central-protheus
title: RH - Linha Protheus - GPE - Como conferir a GRRF e quais são as dúvidas mais
  frequentes
type: support-article
updated_at: '2025-10-20T12:30:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011705352-RH-Linha-Protheus-GPE-Como-conferir-a-GRRF-e-quais-s%C3%A3o-as-d%C3%BAvidas-mais-frequentes
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33069473043223) Tempo aproximado para leitura: **00.03:00 min**

**Dúvida**Como conferir a GRRF e quais são as dúvidas mais frequentes.  
Orientações gerais sobre como conferir valores do relatório GRRF.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**

**GRRF - Guia de Recolhimento Rescisório do FGTS**, é a guia utilizada para o recolhimento das importâncias relativas à multa rescisória, aviso prévio indenizado, quando for o caso, aos depósitos do FGTS do mês da rescisão e do mês imediatamente anterior, caso ainda não tenham sido efetuados, acrescidos das contribuições sociais, instituídas pela Lei Complementar nº. 110/2001, quando devidas.

No Protheus, **Manutenção de tabelas> Tipo de Rescisões S043,** os campos **FGTS mês Anterior** e **FGTS mês** estão com **Sim** o sistema entende que estes valores de FGTS devem ser recolhidos em GRRF ao invés de recolher na SEFIP.  
Demissão sem Justa Causa por parte do Empregador e término de contrato no prazo são tipos de rescisões em que o funcionário saca o FGTS, por este motivo, o acerto dos valores , ou seja, os depósitos de FGTS pendentes, devem ser recolhidos no mesmo prazo de pagamento de da rescisão para que os valores já estejam na conta do FGTS do funcionário quando o ele for efetuar o saque do FGTS e multa.  
**Numa GRRF são recolhidos os valores de:**  
-> Multa dos 40% (calculada com base no valor de FGTS depositado no decorrer da vida do funcionário na empresa, Total \* 40%)  
-> FGTS sobre os valores pagos em rescisão (Verbas com “S” para FGTS).  
-> FGTS sobre os valores pagos em rescisão referente ao Aviso Prévio quando houver.

Campos: No log de ocorrência da GRRF temos os seguintes campos:

![](https://tdn.totvs.com/download/attachments/244420185/image2016-7-21%2014%3A36%3A40.png?version=1&modificationDate=1469124631000&api=v2)

**Rem. Ant. Resc. =>** Este campo deve estar preenchido quando a rescisão acontece do dia 1 ao dia 6 do mês, quando o valor do FGTS da folha do mês anterior ainda não foi recolhido. Como na dispensa pelo empregador (sem justa causa) ou no término de contrato no prazo, no dia do pagamento da rescisão o valor de tudo que a empresa deve ao funcionário deve estar quitado, o valor do recolhimento é direcionado para a guia de GRRF. A verba que compõe este campo é o ID 0017, o sistema vai buscá-la no acumulado do mês anterior (SRD).

**Rem. Mês. Resc.=>** Este campo é composto da seguinte forma:

Ids. 0293 e 0294 exceto os valores referentes ao Aviso Prévio.

São os Ids do aviso prévio:

| ID | Descrição |
| --- | --- |
| 0111 | Aviso Indenizado |
| 0115 | 13º Sobre o Aviso Prévio |
| 0250 | Média sobre Aviso Prévio |
| 0252 | Média de férias sobre aviso prévio |
| 0253 | Média de 13º salário sobre aviso prévio |
| 0230 | Férias sobre Aviso Prévio |
| 0231 | 1/3 Férias sobre Aviso Prévio |
| 1683 | Periculosidade Aviso Prévio |
| 1685 | Periculosidade 13º Aviso |
| 1695 | Insalubridade Aviso Prévio |
| 1697 | Insalubridade 13º Aviso |
| 1707 | ATS Aviso Prévio |
| 1709 | ATS 13º Aviso |
| 1713 | Adicional Transferência Aviso Prévio |
| 1715 | Adicional Transferência 13. Aviso |
| 1719 | Adicional Confiança Aviso Prévio |
| 1721 | Adicional Confiança 13. Aviso |

Sendo assim, o cálculo para composição do campo é:

**“Rem. Mês. Resc.”  =** (Id 0293 + Id 0294) – (Id 0111 + Id 0115 + Id 0250 + id 0252 + id 0253 + id 0230 + Id 0231 Id 1683 + Id 1685 + Id 1695 + Id 1697 + Id 1707 + Id 1709 + Id 1713 + Id 1715 + Id 1719 + Id 1721)

Os identificadores 0111, 0115, 0250, 0252, 0253, 0230, 0231, 1683, 1685, 1695, 1697, 1707, 1709, 1713, 1715, 1719 e 1721 correspondem as verbas relacionadas com o aviso prévio, porém é importante lembrar que os valores calculados nestas verbas só irão para GRRF se estiverem com SIM no campo RV\_FGTS, caso não esteja apenas será calculado na rescisão não devendo ser abatidos na formula acima.  
  
**Observação: Nos casos em que não houver base 13º ou quando a base for negativa. Considerar a orientação conforme documentação abaixo:**

[Preenchimento da Guia de Recolhimento Rescisório do FGTS (GRRF), em relação ao campo “27 – Remuneração - Mês Rescisão” e campo 28 – “Aviso Prévio Indenizado”, na dispensa sem justa causa com o tipo de aviso indenizado](https://tdn.totvs.com/pages/viewpage.action?pageId=185759634)

**Av. Prévio =>** Este campo é composto pelos Ids. Relacionados ao aviso, ou seja, os mesmos que excluímos do campo anterior,

Cálculo **Av. Prévio =** Id 0111 + Id 0115 + Id 0250 + id 0252 + id 0253 + id 0230 + Id 0231 + Id 1683 + Id 1685 + Id 1695 + Id 1697 + Id 1707 + Id 1709 + Id 1713 + Id 1715 + Id 1719 + Id 1721  
  
**Vl. Pensão=>** Este campo só deverá estar preenchido caso na ação judicial do funcionário o juiz tenha determinado que deve pagar ao filho pensão sobre o saldo do FGTS. Este pagamento é definido no cadastro do Beneficiários.  
  
**Saldo para Fins Rescisórios=>** Neste campo deve conter o valor  total do FGTS depositado da verba com o Id. De cálculo 0118 para que seja levado para a GRRF eletrônica.e somado com os valores referente a rescisão, porém essa soma é realizada dentro do aplicativo, como demostra a imagem abaixo:

![](https://tdn.totvs.com/download/attachments/244420185/image2018-8-2_15-26-40.png?version=1&modificationDate=1533234401000&api=v2)

Observe que no validador foi importado somente o valor do saldo e os demais foram somados para que fosse calculado a multa rescisória

![](https://tdn.totvs.com/download/attachments/244420185/image2018-8-2_15-27-8.png?version=1&modificationDate=1533234429000&api=v2)

**O que é exatamente recolhido na GRRF?**

8% Mês da Rescisão

8% do FGTS do Aviso

Multa de 40% sobre o saldo total

**Como compor o saldo total do FGTS depositado?**

O saldo depositado, é o valor que está na conta do funcionários, que conseguimos por meio do extrato da conta do FGTS, só que para calcular a multa, precisamos também incluir nesta “base de calculo da multa” o FGTS que ainda será depositado.

Por este motivo, para calcular a multa devemos somar:  ID 0118 de FGTS digitado + Id 0214 de FGTS 13º na rescisão + Id 0117 de FGTS mês anterior

**Dúvidas Frequentes:**

**Quais os valores são levados para GRRF quando ela é por motivo de dissídio?**

Quando existe uma GRRF por motivo de rescisão complementar por dissídio, apenas os valores de Aviso prévio e multa são levados para a GRRF, porque não é tudo recolhido na GRRF?

 Porque na GRRF são recolhidos apenas os encargos que só existiriam se houvesse rescisão. Se não houvesse rescisão, as diferenças dos outros valores, como 13º, Férias, Salário, Horas extras não iriam ter suas diferenças pagas em folha da mesma forma? Sim. Por isso vão para a SEFIP.

**Ainda sobre o dissídio, como são recolhidos estes valores que não serão recolhidos na GRRF?**

Os valores são recolhidos na SEFIP, feita no código 650. Especial para valores provenientes de dissídio.

**Desta forma, como fazer então para conferir se a SEFIP está correta?**

Para conferir a SEFIP, devemos então considerar:

Remuneração sem 13º:  (Id. 0293 de Base FGTS)  -  ( Id. 0111 de Aviso Prévio + 0250 de Média Aviso Prévio)

Remuneração sobre 13º: (Id. 0294 de Base FGTS 13º)  -  (0115 – 13º Sobre o Aviso, 253 – Média de 13º salário sobre aviso indenizado)  
  
**Observação**O MV\_SOMAVIS não tem nenhum impacto sobre a GRRF, por não ser referir a valores de FGTS e sim a valores de base de INSS. Este parâmetro está relacionado apenas à soma do aviso prévio para declaração e recolhimento dos valores à previdência social. Terá impacto apenas na SEFIP.

**Saiba mais:**

[RH GRRF (Guia de Recolhimento Rescisório FGTS)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010781714-RH-GRRF-Guia-de-Recolhimento-Rescis%C3%B3rio-FGTS)
