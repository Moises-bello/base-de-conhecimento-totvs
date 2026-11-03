---
content_hash: 1aab14a3ee5244095b7b02f0631e58b59612e8d4eabab652610d603e1f222fe4
fetched_at: '2026-06-29T00:10:10.521770+00:00'
page_id: '452719863'
product: rm
source: tdn-rm
title: E-social -S-2230 - Afastamento Temporário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719863
version: 2
---

Evento utilizado para informar os afastamentos temporários dos empregados/servidores e trabalhadores avulsos, por quaisquer dos motivos elencados na tabela 18 – Motivos de Afastamento, bem como eventuais alterações e prorrogações.

**Observações:**

* Inclui-se nesse evento os períodos de afastamento cujo motivo seja o gozo de férias.
* Caso a coligada seja integrada com o Totvs Segurança e Medicina do Trabalho, e seja lançado atestado que gere afastamento, será criado um gatilho S-2230 na fila de eventos para esse funcionário.
* Ao afastar um funcionário onde a data final do afastamento seja superior a data de hoje acrescida de 15 dias, será gerado dois gatilhos, um com a data inicio do afastamento e outro com a data final.
* Ao afastar um funcionário onde a data final do afastamento seja inferior a data de hoje acrescida de 15 dias, será gerado 1 gatilho com a data de inicio e fim no mesmo XML.
* Caso o usuário altere o início de afastamento ou o fim NÃO ultrapassando a quantidade de 15 dias será gerado os gatilhos da seguinte forma:

* Status integrado com TAF: Vai ser gerado gatilho de "Operação Retificação"
* Status (Pendente ,Gerado, Gerado com Erro, Rejeitado TAF e Rejeitado RET)o registro volta para pendente.

-Caso o usuário altere o início de afastamento ou o fim ultrapassando a quantidade de 15 dias será gerado os gatilhos da seguinte forma:

* Status integrado com o TAF: Vai ser gerado um Gatilho S-3000 excluindo a operação inclusão,e gera dois registros  um de inicio e outro de termino.
* Status (Pendente ,Gerado, Gerado com Erro, Rejeitado TAF e Rejeitado RET)o gatilho com operação inclusão é deletado e inclui dois registros sendo um inicio e outro termino.

[**Mapeamento das informações do evento**](http://tdn.totvs.com/display/LRM/Evento+S-2230)  
  

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Eventos Não Periódicos
