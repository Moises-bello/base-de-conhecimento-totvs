---
article_id: 360033892693
category: IMPLANTAÇÃO
content_hash: 61646480154c220889686ec5f19b3be3841c2186b0e6cc04cb7f8cbaa1545dda
fetched_at: '2026-06-28T22:44:33.467856+00:00'
product: protheus
section_id: 10299929290007
source: central-protheus
title: RH - Linha Protheus - MEU RH - Configuração de permissão de acesso as funcionalidades
  e menu do MEU RH
type: support-article
updated_at: '2026-06-22T18:14:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033892693-RH-Linha-Protheus-MEU-RH-Configura%C3%A7%C3%A3o-de-permiss%C3%A3o-de-acesso-as-funcionalidades-e-menu-do-MEU-RH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19285588493719)**Tempo aproximado para leitura: **00:05:00 min**  
 **Dúvida**Configuração de permissão de acesso as funcionalidades e menu do MEU RH  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução  
1.** No **Configurador (SIGACFG),**acesse **Ambientes -> Cadastro -> Menu (CFGX013)**. Informe a nova opção de menu do **SIGATCF**, conforme instruções a seguir

|  |  |
| --- | --- |
| **MENU** | **SIGATCF** |
| **Módulo** | Terminal de Consulta do Funcionário |
| **Nome da Rotina** | Permissões Meu RH |
| **Programa** | TCFA006 |
| **Submenu** | Atualizações/Configurações/Usuários |
| **Tipo** | Função Protheus |

  
Saiba mais sobre permissões e Release liberado acessando o link: [Permissão de funcionalidades do Meu RH - Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=494805578#:~:text=Configurar%20permiss%C3%A3o%2Frestri%C3%A7%C3%A3o%20acesso%20%C3%A0s,SIGATCF%2C%20conforme%20instru%C3%A7%C3%B5es%20a%20seguir)  
  
**2.** Avalie se o compartilhamento e o conteúdo do campo filial da tabela **AI3** e **RJD** estão iguais;  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19285635742487)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19285635746583)  
  
Campo filial:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19285635748119)  
  
**3.** Acesse o módulo **18 - Terminal de Consulta do Funcionário (SIGATCF)** e acesse no menu o caminho que foi colocado a rotina **TCFA006**, no exemplo citado acima foi colocado no menu **Atualizações -> Configurações -> Usuários -> Permissões Meu RH**.  
  
A rotina irá apresentar todos os usuários que foram cadastrados no menu **Atualizações -> Configurações -> Usuários -> Genéricos**, porém essa rotina é para definir as permissões.  
  
![Permiss_es_MEU_RH.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/7542086765335)  
  
**4.** No módulo **53 (SIGAAPD)** acesse o menu **Atualizações -> Participantes -> Cadastros** e verifique se para o participante/funcionário que está acessando o aplicativo, está vinculado com este usuário da rotina TCFA006.  
  
![Cad_Participante_MEURH.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/7542141885207)  
  
**5.** Após realizar a configuração, realize um teste de acesso ao **MEU RH** e verifique se foi apresentado corretamente as opções de acordo com a configuração das permissões.  
  
![Acesso_MEU_RH_Gestor.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/7542155021335)  
  
**Saiba Mais  
[Permissão de funcionalidades do Meu RH - Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=494805578#:~:text=Configurar%20permiss%C3%A3o%2Frestri%C3%A7%C3%A3o%20acesso%20%C3%A0s,SIGATCF%2C%20conforme%20instru%C3%A7%C3%B5es%20a%20seguir)**  
**[RH - Linha Protheus - MEU RH - Quais são as funcionalidades disponibilizadas no Meu RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5540795734807)**[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
