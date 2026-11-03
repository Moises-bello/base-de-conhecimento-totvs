---
article_id: 35382911911447
category: LOGIN
content_hash: 41e6785b3fcac86450f5b714df95be919e90a54aaec9267be31632698367b181
fetched_at: '2026-06-28T22:44:40.357760+00:00'
product: protheus
section_id: 10299559916567
source: central-protheus
title: RH - Linha Protheus - Meu RH - Porque é necessário vincular um usuário válido
  do Configurador no Cadastro de Usuário Genérico do Meu RH, da tabela AI3
type: support-article
updated_at: '2026-06-19T15:58:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35382911911447-RH-Linha-Protheus-Meu-RH-Porque-%C3%A9-necess%C3%A1rio-vincular-um-usu%C3%A1rio-v%C3%A1lido-do-Configurador-no-Cadastro-de-Usu%C3%A1rio-Gen%C3%A9rico-do-Meu-RH-da-tabela-AI3
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35382911890967) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Porque é necessário vincular um usuário válido do Configurador no Cadastro de Usuário Genérico do Meu RH, da tabela AI3   
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**  
**As APIs do Meu RH** possuem natureza privada e restrita, não sendo expostas de forma pública ou anônima. Dessa forma, o acesso a esses serviços exige autenticação obrigatória por meio de um **usuário válido do ERP**, que servirá como **credencial de segurança para estabelecer a comunicação**.  
  
No contexto do **App Meu RH**, os usuários disponíveis correspondem basicamente aos registros de funcionários **(tabelas como RD0, AI3, entre outras entidades relacionadas).** Assim, quando se dispõe de um funcionário devidamente cadastrado e ativo, em conjunto com um usuário válido do ERP, **torna-se possível e necessário realizar a autenticação com sucesso** e, consequentemente, **consumir as APIs privadas do Meu RH.**  
  
Esse mecanismo garante que apenas usuários autorizados e vinculados à base do ERP tenham acesso aos recursos, preservando a segurança, rastreabilidade e integridade dos dados corporativos.  
  
É importante destacar que **não deve ser utilizado o usuário admin nem qualquer outro usuário com privilégios administrativos, pois estes são irrestritos**. Isso ocorre porque tais usuários, por sua natureza, não estão sujeitos a políticas de segurança ou controles granulares de permissões, o que inviabiliza a aplicação de restrições, auditorias e boas práticas de governança.  
  
Por esse motivo, orienta-se que seja criado e utilizado **um novo usuário específico, que não pertença ao grupo admin nem seja o próprio admin**, mas que possua todas as permissões e rotinas necessárias para o correto funcionamento do consumo das APIs. Essa abordagem garante maior segurança, rastreabilidade, segregação de funções e conformidade com as diretrizes de segurança da informação.  
  
**Saiba Mais:**  
[**Como cadastrar o Usuário do Configurador para vínculo no Usuário Genérico da AI3 ?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729194)  
  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
