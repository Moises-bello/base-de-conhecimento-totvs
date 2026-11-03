---
article_id: 360045356294
category: GESTOR
content_hash: a7bf9f154a06b27093bfcf6b2e0acdd30a9428a913966a097ecaed4cd2dd9df6
fetched_at: '2026-06-28T22:44:35.618861+00:00'
product: protheus
section_id: 10299702833303
source: central-protheus
title: RH - Linha Protheus - MEU RH - Mesmo zerando todas solicitações o sininho do
  Gestor permanece indicado solicitações pendentes
type: support-article
updated_at: '2026-06-19T17:24:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045356294-RH-Linha-Protheus-MEU-RH-Mesmo-zerando-todas-solicita%C3%A7%C3%B5es-o-sininho-do-Gestor-permanece-indicado-solicita%C3%A7%C3%B5es-pendentes
---

**Ocorrência**Mesmo zerando todas solicitações o sininho do Gestor permanece indicado solicitações pendentes.  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Causa**Esse erro normalmente ocorre quando é efetuado alguma alteração indevida no cadastro de **Departamento**, principalmente quando o **Departamento** alterado tem **Solicitações Pendentes** de aprovação.  
  
Nessa situação a maior ocorrência é que a **Chave de busca (QB\_KEYINI)** do cadastro do **Departamento** está errada ou repetida para mais de um **Departamento**, quando esse código está repedido o Sistema se perde e pode demonstrar **Solicitações** ou alertas de outro **Departamento**.  
  
 **Solução**Antes de corrigir é necessário fazer uma análise, então acesse o módulo "07 - SIGAGPE" e busque no menu as opções "Consultas > Cadastros > Genéricos", na opção de pesquisa busque pela SQB e verifique se não há mais de um **Departamento** com o mesmo código de **Chave de busca (QB\_KEYINI)** ou se existem Departamentos com esse código **errado** ou **vazio/em branco**.   
  
Essa opção também está disponível no cadastro do **Departamento**, porém terá que visualizar todos os cadastros um de cada vez.  
  
![](https://totvssuporte.zendesk.com/attachments/token/WocHV3dTMOOJ0Xi0DSZm889d0/?name=inline1227129730.png)  
  
![](https://totvssuporte.zendesk.com/attachments/token/xzkddyPxxnNwDEpSmMg78hJQj/?name=inline-216592557.png)​/  
  
![](https://totvssuporte.zendesk.com/attachments/token/wILTDi6ITSohm19bCmhgGZvpn/?name=inline1051858073.png)  
  
Segue um modelo de como esse código é gerado:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096021714)  
  
Siga os passos abaixo caso haja um ou mais **Departamentos** com a **Chave de busca (QB\_KEYINI)** em uma das situações informadas acima:  
  
**1º PASSO:** Atualize o ambiente de acordo com a sua release do Protheus, recentemente foram publicados diversos ajustes e melhorias nesse processo:  
  
**[MP - GPE - Pacote de acumulado do RH no Portal de Cliente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115015741848)  
[MP - MEU RH - Onde baixo a versão mais recente e como atualizar os arquivos do Portal Meu RH?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729034)**  
  
**2º PASSO:** É obrigatório aprovar ou rejeitar todas **Solicitações Pendentes** (Status 1-EM APROVAÇÃO ou 4- EFETIVAÇÃO RH), de modo que não fique nada Pendente na rotina de "Efetivar **Solicitação** do Portal (TCFA040)".  
  
Você pode seguir os passos do artigo abaixo caso tenha alguma **Solicitação** alocada no Aprovador errado:  
[**MP - MEU RH - Como substituir um Aprovador de solicitações pendentes?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051632134)  
  
**Observação:** A rotina "Efetivar **Solicitação** do Portal (TCFA040)" está disponível em vários módulos, porém, cada um demonstrará as **Solicitações** que lhe forem pertinentes, por exemplo, no módulo "16 - SIGAPON" você verá as Solicitações de marcação de ponto e no módulo "07 - SIGAGPE" você verá as **Solicitações** de Férias.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360064212533)  
  
**3º PASSO:** Após a finalização de todas as **Solicitações**, tente alterar a matrícula aprovadora de algum **Departamento**, apontando para outro aprovador. Caso ainda existam **Solicitações Pendentes**, o sistema gerará uma mensagem como validação. Isto servirá como uma certificação de que não há nenhuma **Solicitação Pendente**;  
  
**4º PASSO:** Certificado de que não tenha nenhuma **Solicitação Pendente**, via tabela SQB, limpe o conteúdo do campo **Chave de busca (QB\_KEYINI)**;  
  
**IMPORTANTE:** Já temos melhorias em andamento para automatizar esse processo ou permitir que seja realizado dentro do Protheus.  
  
**5º PASSO:** Por fim, acesse à rotina de **Departamento** para que seja recarregada as informações do campo **Chave de busca (QB\_KEYINI)** sem duplicação (somente acessando à rotina já carregará as informações).  
  
**Saiba Mais**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
