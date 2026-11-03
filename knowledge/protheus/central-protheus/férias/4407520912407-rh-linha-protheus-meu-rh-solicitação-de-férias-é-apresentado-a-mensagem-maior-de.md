---
article_id: 4407520912407
category: FÉRIAS
content_hash: 19cbbb54e40b95c85cc1bd78af2b92fd702c16fdeb14eb069c492d8b51201c79
fetched_at: '2026-06-28T22:44:34.571308+00:00'
product: protheus
section_id: 10299705719575
source: central-protheus
title: 'RH - Linha Protheus - MEU RH - Solicitação de férias é apresentado a mensagem:
  Maior de 50 anos, deve tirar férias em período único'
type: support-article
updated_at: '2026-06-19T14:33:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407520912407-RH-Linha-Protheus-MEU-RH-Solicita%C3%A7%C3%A3o-de-f%C3%A9rias-%C3%A9-apresentado-a-mensagem-Maior-de-50-anos-deve-tirar-f%C3%A9rias-em-per%C3%ADodo-%C3%BAnico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24770392920471) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Solicitação de férias é apresentado a mensagem: Maior de 50 anos, deve tirar férias em período único!  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - MEU RH - Todas as versões  
  
**Causa**  
Com a aprovação da **Reforma Trabalhista,** o profissional com **50 anos** ou mais passou a ter os mesmos direitos que os demais colaboradores, ou seja, ele passa a ter o direito de fracionar suas **férias** em até três períodos.  
  
Esse erro ocorre quando a reforma trabalhista não esta ativa no sistema.  
  
**Solução**  
Para que seja aceito as férias fracionadas para maiores de 50 anos, o parâmetro **MV\_REFTRAB** deve possuir seu conteúdo de acordo com a reforma trabalhista, exemplo:  
  
O conteúdo do parâmetro **MV\_REFTRAB** será igual a **"FSRI"** sem aspas.  
**F** = Férias;  
**S**= Contribuição Sindical;  
**R**= Regime Parcial;  
**I** = Insalubridade Gestante.   
  
Se, por exemplo, o conteúdo do parâmetro **MV\_REFTRAB** esteja "**SRI**", ao solicitar as férias no MEU RH para trabalhadores com 50 anos ou mais irá apresentar a mensagem informando que o trabalhador deve tirar férias em período único.  
  
**IMPORTANTE:** Caso entenda que o comportamento do MEU RH deva ser diferente sugerimos que realize a solicitação de uma melhoria através da [**Central Colaborativa TOTVS**](https://centraldeatendimento.totvs.com/hc/contributions/posts?locale=pt-br)**.**  
  
É possível acompanhar as funcionalidades já disponíveis e o planejamento do que está por vir através do [**ROADMAP MEU RH - PROTHEUS**](https://tdn.totvs.com/display/public/NPR/Roadmap+-+Protheus)**.**  
  
Para saber como criar uma sugestão de melhoria clique [**AQUI**](https://www.youtube.com/watch?v=LTqWbDsBb6s&list=PLYQXMbUS13r-xtKThVYHMFsLK3ezvpo3q&index=13), e para cadastrar uma nova sugestão**,**[**AQUI**](https://centraldeatendimento.totvs.com/hc/contributions/posts?locale=pt-br)**.**  
  
**Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
