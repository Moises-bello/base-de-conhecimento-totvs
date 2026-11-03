---
article_id: 32230282927127
category: TAE
content_hash: e66dc83db33741843b0717426b27e11e466295e76560975400df235ca57022b1
fetched_at: '2026-06-28T22:44:30.157595+00:00'
product: protheus
section_id: 32238506930583
source: central-protheus
title: RH - Linha Protheus - Meu RH - O que verificar quando o documento é enviado
  do Protheus ao TAE e, no Meu RH não aparece para assinatura
type: support-article
updated_at: '2025-09-16T17:12:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32230282927127-RH-Linha-Protheus-Meu-RH-O-que-verificar-quando-o-documento-%C3%A9-enviado-do-Protheus-ao-TAE-e-no-Meu-RH-n%C3%A3o-aparece-para-assinatura
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32230269854615) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**O que verificar quando o documento é enviado do Protheus ao TAE e, no Meu RH não aparece para assinatura?  
  
**Ambiente**TOTVS RH (Linha Protheus) - MEU RH - Todas as versões  
  
**Solução**A causa do erro pode ser quem sendo um único usuário integrado para envio de documento no TAE, este usuário possui **cadastro de funcionário e participante somente na Empresa 01**, ou seja, o *e-mail* que acessa o TAE para envio do documento e, consequentemente, o e-mail que está no **parâmetro MV\_RHTAEUS encontra-se somente na Empresa 01 na SRA e na RD0 do Grupo 01.**  
  
Por tecnologia do Protheus, quem envia o documento dentro do TAE (usuário admin do TAE), precisará estar na **SRA e na RD0 daquele Grupo de Empresa**, ou seja, vamos tomar como exemplo, o *e-mail* [usuario\_tae@gmail.com](mailto:usuario_tae@gmail.com)\*, este e-mail pertence a algum funcionário/participante do Grupo 01, mas no Grupo 02 e no 03, este *e-mail* não está associado a nenhum funcionário/participante, portanto, este funcionário de *e-mail* [usuario\_tae@gmail.com](mailto:usuario_tae@gmail.com)\* só vai conseguir subir os documentos **para os funcionários do Grupo 01, o Grupo que ele está cadastrado como funcionário/participante, SRA e RD0 respectivamente.  
\**e-mail* [usuario\_tae@gmail.com](mailto:usuario_tae@gmail.com) apenas fictício**  
  
Ou seja, para que possamos subir um documento no TAE **para os funcionários do Grupo 02** assinarem, precisa ser um *login* e senha com *e-mail* de um funcionário que está **cadastrado na SRA020 e na RD0020**, e consequentemente, para que eu possa subir um documento na TAE para os **funcionários do Grupo 03**, precisa ser um *e-mail* de *login* atrelado a um funcionário/participante, que esteja **cadastrado na SRA030 e na RD0030**, senão, pela tecnologia implementada Protheus x Meu RH x TAE não será possível subir os documentos.  
  
O *e-mail* do funcionário que receberá o documento para assinar, **precisa estar na RD0 e na SRA daquele Grupo de Empresa**, por exemplo, o funcionário do **Grupo de Empresa 02** que receberá o documento para assinar no Meu RH do **Grupo de Empresa 02,** precisará ter o e-mail cadastrado na **SRA020 e na RD0020**, e assim sucessivamente, para cada Grupo de Empresa.  
  
Verificar se o parâmetro **MV\_MRHTAE** em todas as Empresas está como .T.  
Esse parâmetro faz referência à integração TAE x Meu RH.  
**[Integração da ferramenta TAE com o Meu RH para assinatura de documentos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16786087683351)**  
Verifique inicialmente esse parâmetro, altere para .T. reinicie o serviço e teste novamente.  
  
Quando um documento é enviado do Protheus para o TAE, haverá dentro do TAE um campo Autenticação, como na imagem abaixo.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32230269854999)  
  
Este campo, **não poderá estar como *Login* no Sistema**, precisará obrigatoriamente estar como **"Verificação de Código via e-mail"** , conforme lhe demonstro no *print*.  
  
Autenticação do tipo 1 (**login direto no sistema**). Nesse modelo, não é gerada public key, temos uma validação no meu rh que só irá subir os doumentos caso o public key seja diferente de '0000-00000-000000000-0000'. A autenticação tem que ser 2 (**Verificação de Código via e-mail**).  
  
Também é recomendado verificar se o **CNPJ da Empresa no SIGAMAT do Protheus é igual ao CNPJ do contrato do TAE.**  
  
Outra verificação são os parâmetros **MV\_RHTAEUS e MV\_RHTAEPW**, estes precisam ser cadastrados dentro da rotinas no Protheus, de **Controle de Espelho de Ponto no módulo SIGAPON ou na rotina de Cálculo de Férias no SIGAGPE.****Saiba Mais  
[Integração Meu RH x TAE - Protheus](https://tdn.totvs.com/pages/viewpage.action?pageId=741337177)**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
