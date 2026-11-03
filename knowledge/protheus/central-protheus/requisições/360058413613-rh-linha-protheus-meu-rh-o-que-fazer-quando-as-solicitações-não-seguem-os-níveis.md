---
article_id: 360058413613
category: REQUISIÇÕES
content_hash: 99ac96697e957ca61f2d3481bddb73475a57257f71f0b7708ac3630cb3b1b0e1
fetched_at: '2026-06-28T22:44:37.652378+00:00'
product: protheus
section_id: 10299632459799
source: central-protheus
title: RH - Linha Protheus - MEU RH - O que fazer quando as Solicitações não seguem
  os Níveis ou Fluxo de aprovação desejado
type: support-article
updated_at: '2026-06-25T02:43:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058413613-RH-Linha-Protheus-MEU-RH-O-que-fazer-quando-as-Solicita%C3%A7%C3%B5es-n%C3%A3o-seguem-os-N%C3%ADveis-ou-Fluxo-de-aprova%C3%A7%C3%A3o-desejado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24769601531671)Tempo aproximado para leitura: 00:03:00 min**  
  
**Dúvida**  
O que fazer quando as Solicitações não seguem os Níveis ou Fluxo de aprovação desejado?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Causa**  
Esse erro normalmente ocorre quando é efetuado alguma alteração indevida no cadastro de **Departamento**, principalmente quando o **Departamento** alterado tem **Solicitações Pendentes** de aprovação.  
  
Nessa situação a maior ocorrência é que a **Chave de busca (QB\_KEYINI)** do cadastro do **Departamento** está errada ou repetida para mais de um **Departamento**, quando esse código está repedido o Sistema se perde e pode demonstrar **Solicitações** ou alertas de outro **Departamento**.  
  
**Solução**  
Antes de corrigir é necessário fazer uma análise, então acesse o módulo "07 - SIGAGPE" e busque no menu as opções "Consultas > Cadastros > Genéricos", na opção de pesquisa busque pela SQB e verifique se não há mais de um **Departamento** com o mesmo código de **Chave de busca (QB\_KEYINI)** ou se existem Departamentos com esse código **errado** ou **vazio/em branco**.   
  
Essa opção também está disponível no cadastro do **Departamento**, porém terá que visualizar todos os cadastros um de cada vez.  
![](https://totvssuporte.zendesk.com/attachments/token/WocHV3dTMOOJ0Xi0DSZm889d0/?name=inline1227129730.png)  
  
![](https://totvssuporte.zendesk.com/attachments/token/xzkddyPxxnNwDEpSmMg78hJQj/?name=inline-216592557.png)​  
  
![](https://totvssuporte.zendesk.com/attachments/token/wILTDi6ITSohm19bCmhgGZvpn/?name=inline1051858073.png)  
  
Segue um modelo de como esse código é gerado:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24769601538711)  
  
Siga os passos abaixo caso haja um ou mais **Departamentos** com a **Chave de busca (QB\_KEYINI)** em uma das situações informadas acima:  
  
**1º PASSO:** Atualize o ambiente de acordo com a sua release do Protheus, recentemente foram publicados diversos ajustes e melhorias nesse processo:  
[**MP - GPE - Pacote de acumulado do RH no Portal de Cliente**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115015741848)  
[**MP - MEU RH - Onde baixo a versão mais recente e como atualizar os arquivos do Portal Meu RH?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729034)  
  
**2º PASSO:** É obrigatório aprovar ou rejeitar todas **Solicitações Pendentes** (Status 1-EM APROVAÇÃO ou 4- EFETIVAÇÃO RH), de modo que não fique nada Pendente na rotina de "Efetivar **Solicitação** do Portal (TCFA040)".  
  
Você pode seguir os passos do artigo abaixo caso tenha alguma **Solicitação** alocada no Aprovador errado:  
[**MP - MEU RH - Como substituir um Aprovador de solicitações pendentes?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051632134)  
  
**Observação:** A rotina "Efetivar **Solicitação** do Portal (TCFA040)" está disponível em vários módulos, porém, cada um demonstrará as **Solicitações** que lhe forem pertinentes, por exemplo, no módulo "16 - SIGAPON" você verá as Solicitações de marcação de ponto e no módulo "07 - SIGAGPE" você verá as **Solicitações** de Férias.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24769593517975)  
  
**3º PASSO:** Após a finalização de todas as **Solicitações**, tente alterar a matrícula aprovadora de algum **Departamento**, apontando para outro aprovador. Caso ainda existam **Solicitações Pendentes**, o sistema gerará uma mensagem como validação. Isto servirá como uma certificação de que não há nenhuma **Solicitação Pendente**;  
  
**4º PASSO:** Certificando-se de que não tenha nenhuma **Solicitação Pendente**, acesse o Cadastro de todos os Departamento que precisarão refazer o campo de Chave de Busca - **QB\_KEYINI,**com isso, será necessário deletar todos os campos, menos a descrição, e salvar.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26424653313559)  
**Importante**: Realize este processo **para todos os Departamentos envolvidos**, os quais precisarão ser refeito o código de Chave de Busca no campo **QB\_KEYINI.**  
  
**5º PASSO:** Por fim, se nos passos acima não gerar os registros corretamente no QB\_KEYINI, faça back Up da SQB e recadastre todos os **Departamentos novamente, tendo como início o Departamento do topo da hierarquia, até o mais inferior,** para que seja recarregada as informações do campo **Chave de busca (QB\_KEYINI)** corretamente.  
  
**Saiba Mais**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
