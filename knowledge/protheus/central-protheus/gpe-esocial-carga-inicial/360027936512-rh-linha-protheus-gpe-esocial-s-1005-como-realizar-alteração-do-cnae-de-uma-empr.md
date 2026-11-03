---
article_id: 360027936512
category: GPE - eSocial - Carga Inicial
content_hash: f1987bc619545b2fc35dca733af68a97162d95a5411ad3d742035100fd99e5ee
fetched_at: '2026-06-28T22:45:03.193859+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1005 - Como realizar alteração do CNAE
  de uma Empresa no Protheus e enviar ao eSocial
type: support-article
updated_at: '2024-11-25T11:45:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027936512-RH-Linha-Protheus-GPE-eSocial-S-1005-Como-realizar-altera%C3%A7%C3%A3o-do-CNAE-de-uma-Empresa-no-Protheus-e-enviar-ao-eSocial
---

**Dúvida**Como realizar alteração do CNAE de uma Empresa no Protheus e enviar ao eSocial?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**Através da **INSTRUÇÃO NORMATIVA RFB Nº 1867, DE 25 DE JANEIRO DE 2019** a Receita Federal trouxe novos **CNAEs** e alterou outros já existentes, mas no eSocial essa mudança ocorreu após a publicação da **NOTA TÉCNICA Nº 11/2019 DE AJUSTES DO LEIAUTE VERSÃO 2.5** e isso está impactando os fechamentos do mês no eSocial para quem tem tentou enviar o evento **S-1299** nos últimos dias.  
  
Nas Empresas afetadas o **RET (Governo)** retornou a **inconsistência 234** para os eventos **S-1299** mencionando que o código do CNAE informado no estabelecimento X deve constar no Anexo I da **IN RFB 971/2009**, com as alterações da **IN RFB 1867/2019**.

No Protheus essa informação fica no **SIGAMAT** e pode ser alterada através do Configurador (**SIGACFG**) acessando no Menu as opções Ambiente > Empresas > Filial.  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028148131/mceclip0.png)**No **SIGAGPE** essa informação também pode existir e ser alterada no cadastro do **Centro de Custo**, mas isso dependendo do **Tipo de Lotação Tributária**, no exemplo abaixo é o caso de uma Obra de Construção Civil.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028152532/mceclip1.png)  
  
No Protheus ao realizar a alteração do **CNAE** com o Parâmetro **MV\_RHTAF** habilitado o Sistema já realizará o envio de um novo evento **S-1005**, mas a **data de inicio de validade** deste evento será a de acordo com a **Data Base** preenchida ao acessar o Protheus, caso necessite de efeito anterior ao período atual você deve retroagir a **Data Base** antes da alteração.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028152712/mceclip2.png)  
  
No casos em que o evento **S-1005** não é enviado automaticamente você pode acessar a rotina de **Carga Inicial** para fazer o envio ao TAF, mas a data de inicio de validade deste evento será a de acordo com a **Data de Referência** preenchida na rotina.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028148611/mceclip3.png)  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[Artigos S-1005](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050822873)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)
