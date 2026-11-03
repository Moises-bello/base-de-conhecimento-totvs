---
article_id: 20821023569175
category: LOGIN
content_hash: afd8a88acb019bee27bfba1349629078feb1341e7e5d4094f62df6aba52fa238
fetched_at: '2026-06-28T22:44:40.436123+00:00'
product: protheus
section_id: 10299559916567
source: central-protheus
title: RH - Linha Protheus - MEU RH - Login Inválido. Verifique se o usuário e senha
  foram digitados corretamente
type: support-article
updated_at: '2026-02-16T19:29:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20821023569175-RH-Linha-Protheus-MEU-RH-Login-Inv%C3%A1lido-Verifique-se-o-usu%C3%A1rio-e-senha-foram-digitados-corretamente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20821023559959) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Ao realizar o *login* no Portal Meu RH é apresentada a mensagem: "*Login* Inválido. Verifique se o usuário e senha foram digitados corretamente" mesmo com os dados corretos.  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - MEU RH - Todas as versões  
  
**Solução**  
Esse incidente pode ocorrer por mais de um motivo:

**1. Falta de atualização dos arquivos do Portal e Acumulado do RH**  
É importante **manter** o **acumulado do RH** assim como os **arquivos do Portal** **atualizados**, pois pode existir diferenças na estrutura do *login* gerando o erro.

**Arquivos do Portal:**  
[RH - Linha Protheus - MEU RH - Onde baixo a versão mais recente e como atualizar os arquivos do Portal Meu RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729034)  
  
**Acumulado do RH:**  
[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus#:~:text=Para%20fazer%20o%20download%20do,com%20seu%20release%20do%20Protheus.&text=Nesse%20pacote%2C%20n%C3%A3o%20temos%20dispon%C3%ADveis,segue%20abaixo%2C%20link%20para%20download.)

**2- Falta do vinculo do Usuário do Portal no Cadastro de Participantes**  
Para associar o Usuário do Portal ao Cadastro de Participante acesso no Protheus o módulo **18 - SIGATCF - Terminal de Consulta do funcionário no menu Atualizações -> Configurações -> Usuários -> Cadastro de Participante**  
  
Na rotina edite um Cadastro de Participante e no campo "**Usuar. Portal**" informe o Usuário do Portal, e no campo "**F. Usr.Portal**" informe a filial do usuário do portal.  
![1WtLtEPJB3.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/20820993743511)  
  
**3- Falta do complemento** ***setting/companySettings*** **no** ***appserver.ini*** **do serviço** ***Rest***  
Ao possuir os Arquivos do Portal com versão de **30/05/2023** ou superior é necessário realizar a configuração no serviço ***Rest*** como demonstrado abaixo:  
<https://tdn.totvs.com/pages/viewpage.action?pageId=757238802>  
  
Na seção do serviço ***Rest***, na chave ***Public*** precisará acrescentar o serviço ***setting/companySettings******:***  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20821023562647)  
Obs.: Caso seu ambiente se encontre em nossa **infraestrutura*****Cloud***, é necessário **abrir um chamado** para a **equipe*****Cloud***, informando a necessidade de realização deste procedimento acima, no serviço responsável por manter a execução do *App* Meu RH.  
  
**4 - Informação incorreta no** ***QRCode*** **configurado no** ***Smartphone***  
Nos arquivos do Portal MEU RH existe um arquivo chamado **qr-codegenerator.html** que pode ser utilizado para geração do ***QRCODE*** de configuração do APP no celular. Segue abaixo um exemplo de como a ***URL***deve estar configurada para configurar o meu ambiente:  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21050738878231)  
  
**Atenção**: a ***Rest URL*** não é opcional, é preciso preencher com o link de acesso ao ***Rest***.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21050738892823)  
Outro ponto importante é o complemento: ***/?restPort*** que é a ***query*** para para informar a **porta** do **serviço** ***REST:*** **/?restPort=8082** (cuidado com a diferenciação entre letras **minúsculas** e **maiúsculas** no momento de definição da ***URL*** de acesso, pois caso existam erros no preenchimento podem ocorrer no aplicativo realizar o ***login***. Como por exemplo, escrever erradamente "***Restport***" ou deixar de colocar o ponto de interrogação na ***URL***).  
  
**5 - Verificar se o usuário interno criado no Configurador e, atrelado ao cadastro do usuário genérico, não está bloqueado:**  
Esses casos ocorrem por problemas do usuário do **SIGACFG** estar **bloqueado**, configuração do appserver.ini ou do properties.json.

Relacionado ao usuário, entrar no **módulo 18 - SIGATCF > Atualizações > Configurações > Usuários > Genéricos** para saber qual é o **código do usuário do SIGACFG** vinculado conforme *print* abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24297677502871)  
Sabendo qual o código do usuário entrar no **módulo 99 - SIGACFG > Usuário > Senhas > Usuários > Alterar** e confirmar se realmente o mesmo esta bloqueado ou não conforme print abaixo. Caso esteja seria a causa do erro, avalie se deve desbloquear o usuário ou definir outro usuário no **cadastro de Usuários Genéricos** do **módulo 18 - SIGATCF** conforme citado nos passos acima.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24297667572247)  
  
**6 - Estiver acessando com LOGIN de CPF porém o parâmetro MV\_ACESSPP configurado como** ***e-mail*** **ou vice-versa.**  
MV\_ACESSPP = 1 O usuário será o e-mail (RD0\_EMAIL).  
MV\_ACESSPP = 0 ou qualquer outro valor diferente de 1 o usuário será o CPF (RD0\_CIC)  
  
**7 - Verifique se o seu parâmetro MV\_LOGINT não estaria ativo indevidamente**.   
Caso o parâmetro **MV\_LOGINT**estiver com **.T.** mas não for utilizada a configuração com o [**Active Directory**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6278328204823-RH-Linha-Protheus-MEU-RH-%C3%89-poss%C3%ADvel-efetuar-o-login-no-MEU-RH-integrado-com-o-Active-Directory) altere o mesmo para **.F.** 

**8 - Poderá ter havido alguma perda no relacionamento do funcionário com o participante, por isso, orientamos que seja reconfigurado o vínculo, se seguinte maneira:**  
Abaixo, compartilhamos dois vídeos postados no canal da TOTVS no *Youtube*, os quais demonstram num passo a passo o deverá ser realizado.  
  
***How To*** **| MEU RH Como corrigir o vínculo do participante - Parte 1/2**  
[**https://youtu.be/SjH-bc\_pTac**](https://youtu.be/SjH-bc_pTac)  
***How To*** **| MEU RH Como corrigir o vínculo do participante - Parte 2/2**  
[**https://youtu.be/n6vBE8ZSn0w**](https://youtu.be/n6vBE8ZSn0w)  
  
**9 - Se todos os passos acima ainda não funcionar valide se no console do rest do meu rh esta gerando erro -100.**  
**/restmeurht6/data/profile/summary/{current}/?encodeEmployeeId=true] [TP: 6] [C] Fail to write response, the context will be closed. Error: -100**  
  
[**Seguir a documentação em questão**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30488238936343-RH-Linha-Protheus-Meu-RH-Erro-Invalid-return-of-selector-Fail-to-write-response-the-context-will-be-closed-Error-100)

**Saiba Mais**  
[**RH - Linha Protheus - MEU RH - Aprenda sobre o MEU RH e como fazer a implantação**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036164214)  
[**CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI para acessar a documentação de referência sobre o MEU RH**](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
