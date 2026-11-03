---
article_id: 1500008005201
category: LOGIN
content_hash: d9b5cbddf196b6f770412aaf769e885c84e79f59b4b2294f7e054c503484d54a
fetched_at: '2026-06-28T22:44:40.564611+00:00'
product: protheus
section_id: 10299559916567
source: central-protheus
title: RH - Linha Protheus - MEU RH - Como utilizar senha criptografada no MEU RH
type: support-article
updated_at: '2026-06-18T19:43:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008005201-RH-Linha-Protheus-MEU-RH-Como-utilizar-senha-criptografada-no-MEU-RH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27473741459735) Tempo aproximado para leitura: 00:04:00 min****Dúvida**Como utilizar senha criptografada no MEU RH?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**Implementado a possibilidade de utilização de senha criptografada na base de dados para o aplicativo Meu RH, como primeira etapa de construção para o desenvolvimento de uma nova política de segurança.  
  
**Disponível em todos os *releases* do Protheus,** visto a necessidade da existência do campo **RD0\_SENHAC (Tabela RD0 - Cadastro de Participantes)** no dicionário de dados.  
  
Criado um novo parâmetro para a liberação dessa funcionalidade, este poderá ser criado e habilitado manualmente em sua base de dados, conforme as informações abaixo.   
  
Observe também, em seguida, as regras de funcionamento que envolvem a utilização da **senha criptografada.**  
  
1. Caso não tenha o **parâmetro MV\_POLSEG** no ambiente, realize a criação conforme abaixo:

|  |  |
| --- | --- |
| **Campo** | **Conteúdo** |
| Nome da variável (X6\_VAR): | MV\_POLSEG |
| Tipo (X6\_TIPO): | N - (Numérico) |
| Descrição (X6\_DESCRIC): | 0=Não utiliza Politica de Segurança; 1=Não utiliza |
| Descrição 1 (X6\_DESC1): | para o Portal GCH e utiliza APP MeuRH; |
| Valor Padrão (X6\_CONTEUD): | 0 |

2. Ao habilitar o modelo de utilização da senha criptografada para o app Meu RH, ativando o parâmetro **MV\_POLSEG com o conteúdo 1**, as novas senhas criptografadas serão registradas no campo **RD0\_SENHAC da tabela RD0(Cadastro de Participantes)**, deixando de gravar a senha no campo **RD0\_SENHA**, também poderá ter **mais de 6 caracteres**, diferentemente do campo de senha (RD0\_SENHA) utilizado pelo Portal GCH que são somente 6 caracteres.  
  
A utilização dessa funcionalidade irá gerar **senhas distintas de *login*** para o Portal Protheus GCH (Gestão do Capital Humano) e aplicativo Meu RH, por exemplo:

* Quando o parâmetro for habilitado para criptografia, e seu colaborador realizar o *login* no App Meu RH pela primeira vez o **campo criptografado RD0\_SENHAC** será atualizado automaticamente com a senha atual, evitando que algum processo de atualização necessite ser executado.
* Entretanto, caso o colaborador realize alguma alteração de senha dentro do App Meu RH, a nova senha **não será atualizada por questões de segurança, para o campo de senha padrão (RD0\_SENHA)**, sendo assim, a partir desse momento o colaborador seguirá com senhas distintas para cada produto.

Inicialmente, o novo campo de senha permitirá somente letras e números, quando o processo de politica de segurança estiver completo o cliente poderá permitir a utilização e definição de caracteres especiais.  
  
**BOLETIM TÉCNICO: <https://tdn.totvs.com/display/NPR/RHMOBILE01-10077+DT+Criptografia+de+Senha+no+Login>**  
  
**Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
