---
article_id: 1500012177821
category: ERRORLOG
content_hash: 5ce7eb67224919efdd19fb4f76b0ff061614abce40b3134da87328bdf62465e6
fetched_at: '2026-06-28T22:44:39.498134+00:00'
product: protheus
section_id: 10299583475863
source: central-protheus
title: RH - Linha Protheus - MEU RH - Chave duplicada tabelas RH3, RH4 e ou ACB após
  reiniciar o license server
type: support-article
updated_at: '2025-12-08T14:28:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012177821-RH-Linha-Protheus-MEU-RH-Chave-duplicada-tabelas-RH3-RH4-e-ou-ACB-ap%C3%B3s-reiniciar-o-license-server
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24830241228311) Tempo aproximado para leitura: 00:03:00 min**  
  
**Ocorrência**  
Chave duplicada tabelas RH3, RH4 e ou ACB após reiniciar o license server  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - MEU RH - Todas as versões  
  
**Causa**  
A numeração das tabelas em *License Server* é armazenada em memória, enquanto o *License Server* está ativo.   
  
Quando o serviço do *License Server* é parado, é criado um arquivo chamado **LSNumber.val** na pasta do ***Application Server***. Neste arquivo são gravadas as últimas sequências das chaves em uso no *License*, das tabelas que possuem numeração automática.   
  
Quando o *License* é reiniciado, esses dados são lidos desse arquivo e carregados em memória novamente, para dar continuidade na sequência da numeração automática.  
  
Caso o *License Server* seja parado de forma inesperada, como uma queda de energia ou fechamento inadequado, **o arquivo não é gerado, e não há reinicialização do** ***License***, as informações da última numeração são lidas diretamente das tabelas no banco e carregadas em memória.  
  
**Solução**  
1. Para que não ocorra a  perda do controle de numerações, deve ser configurado a **tag SpecialKey** no **appserver.ini** e apontando para os respectivos ambientes, pois as sequencias do *License* são obtidas por meio da *tag*, junto ao ID da Tabela.  
  
**Para saber mais como realizar essa configuração acesse:**  
[**Numeração sequencial via License Server**](https://tdn.totvs.com/pages/viewpage.action?pageId=567740107)  
  
Após verificar no console do rest ou do *dbaccess* em qual tabela esta ocorrendo a chave duplicada. depois deve ser realizado o ajuste do controle de numeração pelo Configurador(SIGACFG) através da rotina [**APCFG110.**](https://tdn.totvs.com/pages/viewpage.action?pageId=309411140#Numera%C3%A7%C3%A3oautom%C3%A1ticapeloLicenseServer-APCFG110)  
  
Obs: Quando o erro apontar nas tabelas RH3 ou RH4 o processo de alteração abaixo deve ser feito SEMPRE na tabela RH3, Nunca na RH4. Quando ocorrer o erro na tabela ACB o processo deve ser feito na tabela ACB.  
  
Próximos números**:**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27567738024471)**  
  
Números gravados no banco:  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27567727192343)**  
  
**Para saber mais como realizar esse ajuste acesse:**  
[**Ajuste de Numeração automática**](https://tdn.totvs.com/pages/releaseview.action?pageId=235570751)  
  
**IMPORTANTE:** Caso entenda que o comportamento do MEU RH deva ser diferente sugerimos que realize a solicitação de uma melhoria através da [**Central Colaborativa TOTVS**](https://centraldeatendimento.totvs.com/hc/contributions/posts?locale=pt-br)**.**  
  
É possível acompanhar as funcionalidades já disponíveis e o planejamento do que está por vir através do [**ROADMAP MEU RH - PROTHEUS**](https://tdn.totvs.com/display/public/NPR/Roadmap+-+Protheus)**.**  
  
Para saber como criar uma sugestão de melhoria clique [AQUI](https://www.youtube.com/watch?v=LTqWbDsBb6s&list=PLYQXMbUS13r-xtKThVYHMFsLK3ezvpo3q&index=13), e para cadastrar uma nova sugestão**,**[**AQUI**](https://centraldeatendimento.totvs.com/hc/contributions/posts?locale=pt-br)**.**  
  
**Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
