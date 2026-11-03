---
article_id: 4409641611415
category: eSocial - Relatórios
content_hash: ca0e0af1f3d8452f85475a60a3b229e56995215503d685eccdfefdc0aa5c9cc4
fetched_at: '2026-06-28T22:47:04.912773+00:00'
product: rm
section_id: 1500000861002
source: central-rm
title: RH - RM - FOP - eSocial - Gerar bases de INSS/FGTS/IRRF no relatório comparativo
  TAF eSocial do futuro
type: support-article
updated_at: '2024-12-23T14:44:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409641611415-RH-RM-FOP-eSocial-Gerar-bases-de-INSS-FGTS-IRRF-no-relat%C3%B3rio-comparativo-TAF-eSocial-do-futuro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23659920678423) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como gerar as bases de INSS/FGTS no relatório do eSocial do futuro (TAF do Futuro)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**Exclusivamente para clientes do **TOTVS Folha de Pagamento** (Linha RM), por não ser uma prática comum o envio de verbas informativas para as bases de cálculo, foi liberada uma configuração complementar para que o TAF faça a leitura da base do RM no momento de geração do relatório, fazendo assim a geração completa das informações. Para realizar as configurações, siga os passos abaixo:

**TOTVS RM**

1. Realize a configuração do **DefaultDB**. Informações em: [Configurando DefaultDB](https://tdn.totvs.com/display/LRM/Configurando+DefaultDB);  
2. Acesse o menu **Serviços Globais | Segurança | Perfis**;  
2.1. Selecione o sistema **Folha de Pagamento**;  
2.2. Edite o perfil desejado, clique em **Acesso a Menus** e permita o acesso **09.06.01 Api's Relatório Conferência INSS/FGTS.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409640892311)

**TOTVS AUTOMAÇÃO FISCAL (TAF) - SIGACFG**

1. Após configurar o RM, acesse o módulo **SIGACFG**;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409641136535)

2. Acesse **Ambiente | Cadastros | Parâmetros**;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409627488279)

2.1. Cadastre as informações nos [parâmetros](https://tdn.totvs.com/pages/releaseview.action?pageId=306857908) abaixo.

* **MV\_TAFRHLG:** Informar o **usuário** do sistema de RM
* **MV\_TAFRHPW:** Informar a **senha do usuário** do sistema RM preenchido no parâmetro acima
* **MV\_TAFRHUR:** Informar a **URL do software** do sistema RM. Este endereço, geralmente composto por **IP** + **ApiPort** do host, será responsável por armazenar a **API** que será consumida para o produto obter as bases dos valores do relatório. Formato http://servidor:porta

**TOTVS AUTOMAÇÃO FISCAL (TAF) - SIGATAF**

1. Após realizar as configurações acima e após o evento de remuneração ser aceito pelo governo, acesse o módulo **SIGATAF**;

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409627681303)

2. Acesse **Miscelânea | eSocial | eSocial do Futuro**;

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409641340567)

2.1. Gere o relatório normalmente para obter as informações desejadas. 

**Importante**  
Para a utilização do novo relatório é imprescindível ter o TAF atualizado e ter configurado os novos painéis do **TAF do Futuro**.

Nas versões e patches iguais e superiores a 12.1.28.147, 12.1.27.237 e 12.1.26.255 é imprescindível a execução do sistema **RM.Atualizador.exe** para a criação da tabela **PESOCIALTOTALIZADORESAUTONOMOS**, que será utilizada no relatório de conferência de INSS para comparação dos autônomos cadastrados no **TOTVS Gestão Financeira** ou autônomos externos. A partir da 12.1.29 não é necessário executar o RM.Atualizador.exe.  
  
**Saiba mais**  
Para mais informações, acesse:  
     - [Como configurar os novos painéis do TAF do Futuro?](https://tdn.totvs.com/pages/releaseview.action?pageId=528452172)  
     - [Painel de Conferência de INSS](https://tdn.totvs.com/pages/releaseview.action?pageId=528452133)  
     - [Painel de Conferência de FGTS](https://tdn.totvs.com/pages/releaseview.action?pageId=528452163)  
     - [TAF - Como gerar as bases de INSS/FGTS/IRRF no relatório do eSocial do futuro?](https://tdn.totvs.com/pages/releaseview.action?pageId=546249442)
