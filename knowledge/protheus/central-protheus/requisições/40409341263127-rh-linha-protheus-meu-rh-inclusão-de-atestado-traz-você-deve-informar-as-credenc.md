---
article_id: 40409341263127
category: REQUISIÇÕES
content_hash: 300866eb2c7bd2d69d15d92fbe358b0ef27a022eacb2dca4f293558374c9ef3e
fetched_at: '2026-06-28T22:44:37.515738+00:00'
product: protheus
section_id: 10299632459799
source: central-protheus
title: 'RH - Linha Protheus - Meu RH - Inclusão de atestado traz: Você deve informar
  as credenciais corretas de acesso (usuário e senha) e possuir acesso a filial desejada'
type: support-article
updated_at: '2026-05-12T14:59:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40409341263127-RH-Linha-Protheus-Meu-RH-Inclus%C3%A3o-de-atestado-traz-Voc%C3%AA-deve-informar-as-credenciais-corretas-de-acesso-usu%C3%A1rio-e-senha-e-possuir-acesso-a-filial-desejada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40409341243031) Tempo aproximado para leitura: **00:02:00 min**  
  
**Título:**   
Ao solicitar atestado ocorre a mensagem: **Você deve informar as credenciais corretas de acesso (usuário e senha) e possuir acesso a filial desejada**  
  
**Dúvida**  
Ao tentar realizar a solicitação de um atestado médico através do portal ou aplicativo Meu RH, integrado ao Quirons, o sistema apresenta a mensagem de erro: "Você deve informar as credenciais corretas de acesso (usuário e senha) e possuir acesso a filial desejada".  
  
**Ambiente**  
RH (Linha Protheus) - Meu RH - Todas as versões  
  
**Solução**  
Esta mensagem de erro indica uma **inconsistência na comunicação entre o Protheus e a plataforma** ***Quirons*****,** geralmente relacionada às credenciais de integração ou permissões de acesso do usuário configurado.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40409395541399)  
  
Para correção, siga os passos abaixo:

1. Acesse o módulo **Configurador (SIGACFG)**;
2. Vá em **Ambiente > Cadastros > Parâmetros**;
3. Localize e revise o conteúdo dos seguintes parâmetros:

   * **MV\_EMAILQR**: Deve conter o e-mail do usuário administrador ou de serviço cadastrado no Quirons;
   * **MV\_SENHAQR**: Deve conter a senha correta para o usuário informado no parâmetro acima;
4. Valide se este usuário possui acesso à **Filial/Empresa** que o colaborador está logado no Meu RH dentro da plataforma Quirons;
5. Verifique se o cadastro da Filial/Empresa em questão existe e está ativo no ambiente do Quirons;
6. Certifique-se de que os dados de login não possuem espaços em branco ou caracteres especiais não suportados no conteúdo do parâmetro.

**Saiba Mais**  
[DT Integração Meu RH x Quirons para envio de atestado](https://www.google.com/search?q=https://tdn.totvs.com/pages/viewpage.action%3FpageId%3D991880224)  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
