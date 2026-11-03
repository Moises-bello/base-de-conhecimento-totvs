---
article_id: 6278328204823
category: LOGIN
content_hash: 2c681a3ac90d285c5beab9042fbb6e016f72b70bf1b1809ed5f99e8fe0a98434
fetched_at: '2026-06-28T22:44:40.558410+00:00'
product: protheus
section_id: 10299559916567
source: central-protheus
title: RH - Linha Protheus - MEU RH - É possível efetuar o login no MEU RH integrado
  com o Active Directory
type: support-article
updated_at: '2026-06-19T17:12:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6278328204823-RH-Linha-Protheus-MEU-RH-%C3%89-poss%C3%ADvel-efetuar-o-login-no-MEU-RH-integrado-com-o-Active-Directory
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17987686689943) Tempo aproximado para leitura: 00:05:00 min****Dúvida**É possível efetuar o login no MEU RH integrado com o Active Directory?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – Todas as versões  
  
**Solução**O Protheus já possui recursos que possibilitam acesso ao ERP a partir de um usuário da rede por meio da integração do Protheus com o *Active* *Directory*, que é o servidor de domínio da Microsoft.  
E agora será possível acessar o Meu RH a partir de um usuário e senha válidos no Protheus, ou por meio de um usuário do *Active* *Directory*, ou seja, um usuário e senha válidos no domínio da empresa.  
  
Para que isso seja possível, será necessário realizar a configuração do sistema, bem como dos usuários do Meu RH, seguindo todos os 5 passos abaixo:  
  
**1 - Atualização do dicionário de dados e configuração do parâmetro MV\_LOGINT**Está sendo disponibilizado o novo parâmetro **MV\_LOGINT,** para que seja possível definir se o acesso ao Meu RH será feito na forma padrão (atual), ou se o *login* será feito por meio da integração Protheus/*Active Directory*.  
  
Abaixo os dados do novo parâmetro:

| Campo | Conteúdo |
| --- | --- |
| Nome da variável (X6\_VAR): | **MV\_LOGINT** |
| Tipo (X6\_TIPO): | L - (Lógico) |
| Descrição (X6\_DESCRIC): | Login do Meu RH Integrado ao Protheus e *Active* |
| Descrição 1 (X6\_DESC1): | *Directory* |
| Descrição 2 (X6\_DESC2): |  |
| Valor Padrão (X6\_CONTEUD): | .F. |

**Observação:** O novo parâmetro estará disponível à partir da versão 12.1.2210, contudo, pode-se criá-lo manualmente, conforme a necessidade para os releases anteriores.  
  
Quando esse parâmetro estiver definido com valor verdadeiro (.T.) o acesso ao Meu RH passa a ser feito conforme a configuração da política de acesso ao Protheus, definida no módulo Configurador. É a definição da política que indicará se o acesso será: ou feito por meio de um usuário do Protheus, ou por meio de um usuário do ***Active Directory***.

**2 - Definição da política de acesso ao Protheus**

Essa configuração é obrigatória apenas para a integração com o *Active Directory*. Caso o acesso ao Meu RH seja feito apenas por meio de um usuário do Protheus, basta seguir para o passo seguinte.  
  
A política de acesso ao Protheus integrada ao *Active Directory*, de forma obrigatória ou opcional, precisa estar devidamente configurada no módulo Configurador. Maiores informações a respeito desse login integrado podem ser obtidas acessando os links abaixo: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026238652-MP-FRAME-Login-no-Protheus-com-Active-Directory>  
  
**3 - Criação de 1 usuário do Protheus para cada um dos funcionários da empresa que irão acessar o Meu RH**Será necessário criar um usuário do Protheus para cada funcionário que acessa o Meu RH. Ou seja, caso a empresa possua 10 funcionários que acessam o Meu RH, então será necessário criar 10 novos usuários do Protheus  
  
**4 - Criação do vínculo entre o Funcionário e o usuário do Protheus**Conforme foram adicionados novos usuários do Protheus para cada um dos funcionários, então é necessário estabelecer o vínculo entre cada Funcionário e Usuário correspondente no módulo Configurador.  
  
O vínculo é feito no cadastro de usuários, na guia Parametrização/Vínculo Funcional, informando o Grupo, a Filial, e a Matrícula. Caso o login seja integrado ao *Active Directory*, o domínio e o nome do usuário devem ser informado na guia: Usuário/*Active Directory.***5 - Definir a *REST URL* nos dispositivos móveis**Para que o acesso ao Meu RH em dispositivos móveis seja feito com sucesso é obrigatório informar no campo *REST URL* o endereço do servidor *REST*.  
Importante: o login Integrado em dispositivos móveis exige o aplicativo Meu RH em versão igual ou superior a 2.5.1 nas lojas *Google Play e Apple Store.***IMPORTANTE:**Quando se utiliza o login integrado, o processo de acesso é composto por duas requisições: a chamada inicial do Meu RH, e uma outra exclusiva da Framework API, exclusiva para a validação do usuário e da integração. Ou seja, são feitas duas requisições em paralelo, o que exige pelo menos uma thread adicional para cada usuário, em comparação com a configuração existente, caso ocorra uma migração de acesso do padrão para o integrado.  
  
Segue abaixo, a documentação relacionada: ***Login* integrado com AD (*Active Directory*) *Windows***<https://tdn.totvs.com/display/NPR/Login+do+Meu+RH+Integrado+ao+Protheus+e+Active+Directory>   
  
No artigo abaixo, podem ser acompanhadas as funcionalidades disponibilizadas para o MEU RH e também acessar o *Roadmap* com as implementações futuras do MEU RH Protheus:  
[RH - Linha Protheus - MEU RH - Quais são as funcionalidades disponibilizadas no Meu RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5540795734807)  
  
**Saiba Mais:  
[RH - Linha Protheus - MEU RH - Configuração para Login no MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044227453)  
[RH - Linha Protheus - MEU RH - Como utilizar senha criptografada no MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008005201)**  
**[CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)** **Anexo Video com detalhes do processo**
