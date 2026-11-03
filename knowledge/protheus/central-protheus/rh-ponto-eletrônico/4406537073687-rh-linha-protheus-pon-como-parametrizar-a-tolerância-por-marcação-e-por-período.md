---
article_id: 4406537073687
category: RH - Ponto Eletrônico
content_hash: 7e4973cba87e9cbe5c4de35eef6dd3e4d6bd305855457bc4fce40bbe8f429751
fetched_at: '2026-06-28T22:44:58.225552+00:00'
product: protheus
section_id: 206956208
source: central-protheus
title: RH - Linha Protheus - PON - Como parametrizar a tolerância por marcação e por
  período corretamente ?
type: support-article
updated_at: '2026-06-09T19:27:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406537073687-RH-Linha-Protheus-PON-Como-parametrizar-a-toler%C3%A2ncia-por-marca%C3%A7%C3%A3o-e-por-per%C3%ADodo-corretamente
---

**Dúvida**  
Como parametrizar a tolerância por marcação e por período corretamente ?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Para parametrizar as tolerâncias por marcação e por período deverá seguir o procedimento abaixo:  
Acesse o módulo **SIGAPON,** em **Atualizações>Cadastro do Ponto>Regras Apontamento**, filtre a regra desejada e clique em Alterar, na aba Tolerâncias, veja que os campos de tolerância por marcação são **Tol. Atra. S. An** e **Tol. H. Extra**.   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35870079762071)  
  
Veja maiores detalhes abaixo sobre os campos tolerância por batidas:  
O **Tol. Atra. S.** correspondente a tolerância por atrasos e saídas antecipadas de acordo com o horário estipulado na Tabela de Horário padrão. Neste caso o sistema tem como limite 5 minutos por marcação.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406536343703)  
O **Tol. Atra. S.** correspondente a tolerância de hora extra de acordo com o horário estipulado na Tabela de Horário padrão. Neste caso o sistema tem como limite 5 minutos por marcação.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406528369047)  
Já os campos de tolerância por período são **Tol. Ad. Not.**, **Tol. Ad. Nt. He.**, **Tol. H. Ex. Per.,** **Tol. Atr. Per., Tol. S. Per., Tol Faltas, Tol. H.E.D.** Quando estes campos estão preenchidos o sistema calcula todos os valores excedentes da jornada de trabalho, neste caso 0,10 minutos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35870096182167)

O campo **Tol. Hr. NReal** trata os eventos de absenteísmo, como se fosse a junção de atraso e saída antecipada no expediente, este campo só pode ser preenchido se os campos **Tol. Atr. Per.** e **Tol. S. Per.** estiverem com valor 0,00.  
  
**Importante:**

Quando configuradas tolerâncias **por batida** e **por período**, o sistema valida da seguinte forma:  
**Primeiro**, verifica a **tolerância por batida**.  
Se ultrapassada, o sistema gera o apontamento e **não** valida a tolerância por período.  
**Segundo**, se estiver **dentro da tolerância por batida**, o sistema valida o **período total**.

**Exemplo:**  
Entrada com 4 minutos e saída com 5 minutos de tolerância → total de 9 minutos dentro da tolerância por batida e por período → **não gera apontamento**.  
A aplicação da tolerância depende da configuração na aba **Horário Móvel**:  
Se houver **mobilidade**, o sistema considera a **tolerância por período**.  
Se estiver configurado **somente por batida**, o sistema aplica a tolerância **apenas na última batida (saída do expediente)**.

Veja maiores detalhes sobre tolerância para horário móvel ou fixo:  
[RH - Linha Protheus - PON - Tolerâncias Hora Extra e Descontos, para horário móvel limitado ou horário fixo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012555721-RH-Linha-Protheus-PON-Toler%C3%A2ncias-Hora-Extra-e-Descontos-para-hor%C3%A1rio-m%C3%B3vel-limitado-ou-hor%C3%A1rio-fixo?source=search)  
  
**Informações complementares**  
Boletim Técnico: <https://tdn.totvs.com/pages/releaseview.action?pageId=496398394>  
Pacote de Expedição Contínua do RH: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>  
  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
