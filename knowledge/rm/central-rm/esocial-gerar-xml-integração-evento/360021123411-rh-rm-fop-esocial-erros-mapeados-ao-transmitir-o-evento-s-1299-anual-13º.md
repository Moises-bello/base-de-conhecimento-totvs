---
article_id: 360021123411
category: eSocial - Gerar XML/ Integração Evento
content_hash: 05139e788c79c5a43d867f1426bc926f64d2bccb5c9a0ea2922426258cdf8a9f
fetched_at: '2026-06-28T22:47:13.002544+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Erros mapeados ao transmitir o evento S-1299 anual 13º
type: support-article
updated_at: '2026-04-17T18:09:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021123411-RH-RM-FOP-eSocial-Erros-mapeados-ao-transmitir-o-evento-S-1299-anual-13%C2%BA
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24456686937239)**Tempo aproximado para leitura: **00:02:10 min**  
  
**Dúvida**  
Quais são os erros mapeados ao transmitir o evento S-1299 anual 13º e como ajustá-los?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**  
Ao realizar a transmissão do evento S-1299 referente ao período de apuração anual 13º, algumas mensagens podem ser retornadas pelo RET. Selecione o código do erro para verificar as validações necessárias:

• [**Erro 162**](http://tdn.totvs.com/pages/viewpage.action?pageId=445660823#MensagensdeErro-S-1299-2136880021)

O Trabalhador com CPF : XXXXXXXXXXX e Matricula : XXXXXXXXXXXXXX consta na base de dados do Ambiente Nacional do eSocial, mas não foi informada sua remuneração. Ação Sugerida: Verificar se a falta de informação e decorrente de dificuldades operacionais ou se e possível efetuar a regularização.

•[**Erro 163**](http://tdn.totvs.com/pages/viewpage.action?pageId=445660823#MensagensdeErro-S-1299-2136880022)

O Trabalhador sem vinculo com Nome : XXXXXXXXXXXX , CPF : XXXXXXXXXXX, NIS : XXXXXXXXXXX e Categoria : XXX consta na base de dados do Ambiente Nacional do eSocial, mas não foi informada sua remuneração. Ação Sugerida: Verificar a situação do trabalhador e efetuar a regularização.

• [**Erro 424**](http://tdn.totvs.com/pages/viewpage.action?pageId=445660823#MensagensdeErro-S-1299-2136882782)

Rubrica não permitida em folha de decimo terceiro.

• [**Erro 761**](http://tdn.totvs.com/pages/viewpage.action?pageId=445660823#MensagensdeErro-S-1299-2136885786)

Não foi localizada a remuneração do trabalhador CPF: XXXXXXXXXXX Matricula XXXXXXXXXX no período.

**Saiba mais**  
Para mais informações acesse:  
      • [Regra de Validação do Fechamento](https://tdn.totvs.com/pages/viewpage.action?pageId=445660823)
