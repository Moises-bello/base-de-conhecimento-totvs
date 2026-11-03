---
article_id: 360053939854
category: ' RH - Funcionários'
content_hash: e4711b663a24e2d7bf994487ca6758be02f2c487469ab250853da382dc4355c9
fetched_at: '2026-06-28T22:44:48.213219+00:00'
product: protheus
section_id: 32419218165783
source: central-protheus
title: RH - Linha Protheus - PON - Como cadastrar uma exceção por período para trocar
  o horário e regra de apontamento
type: support-article
updated_at: '2026-01-23T19:02:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053939854-RH-Linha-Protheus-PON-Como-cadastrar-uma-exce%C3%A7%C3%A3o-por-per%C3%ADodo-para-trocar-o-hor%C3%A1rio-e-regra-de-apontamento
---

**Dúvida**Como cadastrar uma exceção por período para trocar o horário e regra de apontamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Para cadastrar uma Exceção por Período para alterar o Horário que deve ser cumprido ou a Regra de Apontamento que o (os) funcionário (os) deve (m) ser submetido (s), deve ser seguido o exemplo abaixo:  
  
1 - Nesta Exceção, estou informando ao sistema que para todas as matrículas que estão sob o turno 02, o dia 12.09.2020 será trabalhado, com horário diferente do que está cadastrado na Tabela de Horário Padrão (iremos informar na próxima aba) e todos estes funcionários serão vinculados neste dia para a Regra de Apontamento 02:  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360090741274)  
  
2 - Na aba de Horário, informo o horário que estes funcionários precisarão cumprir neste dia:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360090740494)  
  
3 - Por fim, na aba de Intervalos informo que a primeira saída deve ser considerara como Intervalo:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360092875633)  
  
As demais abas que não foram mencionadas, não devem ter nenhuma alteração.  
  
Com esse cadastro, se acessarmos a Consulta de Horários (através das rotinas de Integrados ou Marcações) de um funcionário que esteja sob o turno 02, veremos as alterações:  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360090740894)  
  
Veja que ele foi mantido no mesmo turno, porém, apenas no dia 12.09.2020 está previsto um horário diferente (conforme informamos na Exceção) e a Regra de Apontamento foi alterada também.  
  
**Importante**: Vale ressaltar que para o [Cálculo Mensal(PONM070)](https://tdn.totvs.com/pages/releaseview.action?pageId=635988738), a regra que foi trocada via exceção não será validada, a regra validada no cálculo mensal sempre será a que estiver vinculada ao cadastro do funcionário, Aba relógio registrador, onde contém o campo REGRA.   
  
**Saiba mais,**[Cálculo Mensal(PONM070)](https://tdn.totvs.com/pages/releaseview.action?pageId=635988738)[RH - Linha Protheus - PON - Como fazer e qual a finalidade do Cálculo Mensal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051550453-RH-Linha-Protheus-PON-Como-fazer-e-qual-a-finalidade-do-C%C3%A1lculo-Mensal)
