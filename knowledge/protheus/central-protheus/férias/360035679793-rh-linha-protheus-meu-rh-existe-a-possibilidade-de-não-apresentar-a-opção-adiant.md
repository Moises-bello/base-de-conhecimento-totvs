---
article_id: 360035679793
category: FÉRIAS
content_hash: b6e8453ce9d03f5e4036cde413d47ad096a9039fa7a1038376b0bf890c67eb54
fetched_at: '2026-06-28T22:44:34.601352+00:00'
product: protheus
section_id: 10299705719575
source: central-protheus
title: RH - Linha Protheus - MEU RH - Existe a possibilidade de não apresentar a opção
  adiantamento do 13° salário na solicitação de férias
type: support-article
updated_at: '2026-06-19T14:36:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035679793-RH-Linha-Protheus-MEU-RH-Existe-a-possibilidade-de-n%C3%A3o-apresentar-a-op%C3%A7%C3%A3o-adiantamento-do-13-sal%C3%A1rio-na-solicita%C3%A7%C3%A3o-de-f%C3%A9rias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30619871832599)**Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Existe a possibilidade de não apresentar a opção **Adianta 13°** **salário** na solicitação de férias?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - MEU RH - Todas às versões  
  
**Solução**  
Foi implementado o parâmetro **MV\_MRHFE13** para que seja possível ocultar o 13º salário na tela de solicitação de férias.  
  
Se não houver no dicionário de dados, o parâmetro deverá ser criado e habilitado manualmente na base de dados, conforme as informações no artigo abaixo:  
[Permissão para exibir o 13º salário na solicitação de férias](https://tdn.totvs.com/pages/viewpage.action?pageId=615586243)  
  
Caso o parâmetro esteja desabilitado (valor .F.), as telas abaixo não serão apresentadas durante o processo de solicitação de férias.

![](https://tdn.totvs.com/download/attachments/615586243/2.png?version=1&modificationDate=1620672767853&api=v2)  
  
Caso o parâmetro não exista, ou esteja configurado com .T., a tela acima será apresentada normalmente.  
  
Segue demonstração de como é apresentada a solicitação de férias no MEU RH ao deixar o parâmetro **MV\_MRHFE13 = .F. - "Não permite solicitar 13º salário durante o processo de solicitação de férias":**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8892273414807)  
  
![Fer_Sem_13.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/8892570872727)  
  
**Saiba Mais:**  
[**RH - Linha Protheus - MEU RH - Como registrar a solicitação de Férias através do MEU RH?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058418633)  
[**RH - Linha Protheus - MEU RH - Existe a possibilidade de ocultar o abono pecuniário na tela de solicitação de férias**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417221376535)  
[**CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH**](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
