---
article_id: 4417221376535
category: FÉRIAS
content_hash: b1e9791b9f4443cb09ba8eae1f7edf290aa4c2205697ea7e5c890731bbc449e1
fetched_at: '2026-06-28T22:44:34.566230+00:00'
product: protheus
section_id: 10299705719575
source: central-protheus
title: RH - Linha Protheus - MEU RH - Existe a possibilidade de ocultar o abono pecuniário
  na tela de solicitação de férias
type: support-article
updated_at: '2026-06-19T15:00:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417221376535-RH-Linha-Protheus-MEU-RH-Existe-a-possibilidade-de-ocultar-o-abono-pecuni%C3%A1rio-na-tela-de-solicita%C3%A7%C3%A3o-de-f%C3%A9rias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19232263967127)**Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Existe a possibilidade de ocultar o abono pecuniário na tela de solicitação de férias?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - MEU RH - Todas as versões  
  
**Solução**  
Foi implementado o parâmetro **MV\_MRHFEAB** para que seja possível ocultar a pergunta do abono pecuniário na tela de solicitação de férias.  
  
O parâmetro deverá ser criado e habilitado manualmente na base de dados, conforme as informações no artigo abaixo:  
[**Permissão para exibir o abono pecuniário na solicitação de férias**](https://tdn.totvs.com/pages/viewpage.action?pageId=615402367)  
  
Caso o parâmetro esteja desabilitado (valor .F.), as telas abaixo **não** serão apresentadas durante o processo de solicitação de férias:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417227654807)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417242472599)  
  
  
Caso o parâmetro não exista, ou esteja configurado com .T., as telas acima serão apresentadas normalmente.  
  
Segue demonstração de como é apresentada a solicitação de férias no MEU RH ao deixar o parâmetro **MV\_MRHFEAB=.F.** -"Permite solicitar abono pecuniário durante o processo de solicitação de férias onde **.T.** permite e **.F.** não permite":![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8903738597783)  
  
  
![Abono_pecuni_rio_n_o_aparece.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/8903698806679)  
  
**Saiba Mais:**  
[**RH - Linha Protheus - MEU RH - Como registrar a solicitação de Férias através do MEU RH?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058418633)  
[**RH - Linha Protheus - MEU RH - Existe a possibilidade de não apresentar a opção adiantamento do 13° salário na solicitação de férias**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035679793)  
[**CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)
