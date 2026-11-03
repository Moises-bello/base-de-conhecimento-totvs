---
article_id: 22925020835991
category: eSocial - Gerar XML/ Integração Evento
content_hash: 3c88933afb82d31f2c469b495e690debb9af5e0396e9d0be87dfd42c3f158eb4
fetched_at: '2026-06-28T22:47:11.879771+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial -  Cálculo utilizado para preenchimento da tag <vrSalFx>
  para salário composto de funcionário horistas XML  S-2206 e S-2306
type: support-article
updated_at: '2026-05-26T20:25:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22925020835991-RH-RM-FOP-eSocial-C%C3%A1lculo-utilizado-para-preenchimento-da-tag-vrSalFx-para-sal%C3%A1rio-composto-de-funcion%C3%A1rio-horistas-XML-S-2206-e-S-2306
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22925020827927)**Tempo aproximado para leitura: **00:02:10 min****Dúvida**Como o sistema calcula o salário composto para alimentar a tag **<vrSalFx> de funcionários horistas** na geração dos eventos S-2206 e S-2306?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**Com base na data da alteração registrada no evento S-2206 e S-2306, o sistema verificará no histórico salarial do funcionário todos os registros com datas anteriores a essa data. 

O sistema irá validar se consta em **Configurações | Parametrizador | eSocial | Configurações Gerais 3/7** se a opção abaixo habilitada

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22925452292631)

* **Com a opção marcada** o sistema validará o maior Salário Hora do Histórico Salarial;
* **Com a opção desmarcada** o sistema realizará o seguinte cálculo:  
  1. No Histórico Salarial validará quais são os últimos Números de Salários Preenchidos, com números distintos e com valores diferentes de 0;2. Após somará os Salários e, as Jornadas identificadas com o Número de Salários acima (cada um individualmente);3. Do resultado obtido de cada soma acima, o sistema fará Soma Salário / Soma Jornada (R1);4. O resultado desta divisão (R1) será multiplicado por 60 minutos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22925489112983)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22925452316311)

**Saiba mais**  
Para mais informações acesse:  
- [TAG vrSalFx - Parâmetro Considerar maior valor de salário-hora na tag vrSalFx para professores/horistas](https://tdn.totvs.com/pages/releaseview.action?pageId=521641736)   
- [Configurações Gerais 3/7](https://tdn.totvs.com/pages/releaseview.action?pageId=452719328)
