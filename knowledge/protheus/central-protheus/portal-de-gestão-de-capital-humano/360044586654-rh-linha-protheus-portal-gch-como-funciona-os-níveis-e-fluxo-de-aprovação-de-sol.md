---
article_id: 360044586654
category: Portal de Gestão de Capital Humano
content_hash: 7cb6e20a72079ab5ee2cc7e2a1c677b42aea135cefe16fd068a269036c2db291
fetched_at: '2026-06-28T22:42:59.256654+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus - PORTAL GCH - Como funciona os Níveis e Fluxo de aprovação
  de Solicitações Sem Visão
type: support-article
updated_at: '2021-04-07T13:21:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044586654-RH-Linha-Protheus-PORTAL-GCH-Como-funciona-os-N%C3%ADveis-e-Fluxo-de-aprova%C3%A7%C3%A3o-de-Solicita%C3%A7%C3%B5es-Sem-Vis%C3%A3o
---

**Dúvida**Como funciona os Níveis e Fluxo de aprovação de Solicitações Sem Visão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Portal Gestão do Capital Humano – Todas as versões  
  
**Solução**Todas as solicitações realizadas através do Portal Gestão do Capital Humano são encaminhadas para aprovação do RH da Empresa, essas solicitações ficam disponíveis nos módulos envolvidos em 'Miscelânea > Portal Protheus > Efetivar Solicitação Portal'.  
  
Por exemplo, meu Trabalhador solicita uma marcação de ponto, ela só será efetivada no Protheus se a pessoa do RH da Empresa acessar o módulo '16 - SIGAPON' e for no menu nas opções 'Miscelânea > Portal Protheus Efetivar Solicitação' e aprovar tal solicitação.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061860373/mceclip0.png)  
  
Neste caso é possível configurar o Sistema para que haja um ou mais níveis de aprovação antes da Solicitação chegar ao RH da Empresa.  
  
Na configuração 'Sem Visão', o parâmetro 'MV\_ORGCFG' deve estar com conteúdo '0' (sem aspas).  
  
Desta forma, basta acessar o cadastro do Departamento no módulo '07 - SIGAGPE' através do caminho 'Atualizações > Cadastros > Departamento' e informar uma Matrícula Responsável.  
  
Obs.: Todas solicitações realizadas por Trabalhadores alocados nesse departamento serão encaminhadas para aprovação do Trabalhador associado a Matrícula Responsável.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060949554/mceclip1.png)  
  
É possível incluir mais de um Nível de Aprovação, basta informar o Departamento Superior, no exemplo abaixo, após a aprovação da Matrícula Responsável 000023 do Departamento 000000005 a aprovação será direcionada a Matrícula Responsável do Departamento 000000004 e assim sucessivamente, até que, após todos aprovarem, a solicitação será encaminhada ao RH da Empresa.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060949674/mceclip3.png)  
  
Além da amarração de Departamento Superior, há como definir quantos Níveis uma solicitação terá de aprovação configurando essa informação na configuração de menu do módulo '18 - SIGATCF' através do caminho 'Atualizações > Configurações > Menus'.  
  
No caminho indicado posicione a seleção sobre o Portal RH e pressione 'Outras Ações > Menu'.  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060950134/mceclip5.png)  
  
Busque a Solicitação desejada e clique em 'editar'.  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060950194/mceclip6.png)  
  
No campo 'Nivs Aprovac' você informa a quantidade de Níveis de Aprovação que essa Solicitação passará até chegar ao RH, se estiver preenchido com '0' ela subirá todos os Níveis de Aprovação do cadastro de Departamento, ou seja, subindo para todo Departamento Superior.  
  
No exemplo abaixo, quando preencho com '1', basta a Matrícula Responsável do primeiro Departamento aprovar que na sequência ela será encaminhada ao RH da Empresa.  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060950274/mceclip7.png)  
  
Também é possível definir a partir de qual Nível as aprovações vão iniciar, basta informar o Nível Inicial na configuração do menu.  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061882313/mceclip8.png)  
  
**Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o Portal GCH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)
