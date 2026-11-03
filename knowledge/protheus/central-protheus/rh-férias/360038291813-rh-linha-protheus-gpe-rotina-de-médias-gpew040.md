---
article_id: 360038291813
category: RH - Férias
content_hash: 675f17266c51d934289bfc230fab1a7fb5437e19dc8dfe8c2eeb56b67245a947
fetched_at: '2026-06-28T22:43:59.213489+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Rotina de Médias (GPEW040)
type: support-article
updated_at: '2025-09-02T18:05:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038291813-RH-Linha-Protheus-GPE-Rotina-de-M%C3%A9dias-GPEW040
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31721037792663)** Tempo aproximado para leitura: **00:02:30 min  
  
Dúvida**Configuração para utilizar a nova **rotina de médias (GPEW040)**, onde será apresentado o cadastro centralizado das parametrizações/ configurações que interferem na apuração de médias, contemplando informações de sindicato, parâmetros relacionados às médias (SX6) e mnemônicos.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução****1. Configuração dos menus**No Configurador (SIGACFG), acesse Ambientes/Cadastro/Menu (CFGX013). Informe a nova opção de menu do SIGAGPE, conforme instruções a seguir:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360050500613)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049611734)  
  
Clicar no botão **OK,** clique no botão **Gerar** e digite **Sigagpe**. Após isso clique em **Gerar**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360051774194)

**2. Acesso à rotina**  
Ao entrar no módulo SIGAGPE e acessar Atualizações> Área de Trabalho> Médias, será apresentada a tela abaixo:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049611854)  
  
  
Neste cadastro haverá as seguintes informações:  
**Sindicato:** Apresentará o conteúdo da aba “Medias” do cadastro de sindicatos, permitindo sua manipulação;  
**Verbas:** Apresentará o conteúdo da aba “Medias” do cadastro de verbas, permitindo alteração;  
**Mnemônicos:** São três etapas:  
    1. Conversão dos parâmetros (SX6) referentes a médias em mnemônicos (carregará o conteúdo padrão dos mnemônicos com o conteúdo dos parâmetros SX6. Caso realize alteração, poderá modificar diretamente o mnemônico e o parâmetro será inutilizado;  
    2. Criado o agrupador (RCA\_PROCES == M) de médias no cadastro de mnemônicos, utilizando-o para identificar todos os mnemônicos referentes às médias;  
    3. Filtro na nova rotina apenas os mnemônicos com a nova classificação.  
  
O conteúdo default dos novos mnemônicos é a leitura do conteúdo do seu respectivo parâmetro, mas caso altere o valor, o parâmetro deixa de ser considerado.  
  
  
**Saiba Mais**

[Reestruturação de Médias](https://tdn.totvs.com/pages/viewpage.action?pageId=515701094)  
[RH - Linha Protheus - GPE - Cálculo de médias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050726154-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-m%C3%A9dias)  
[RH - Linha Protheus - GPE - Como gerar o demonstrativo de Médias para Férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7726351592855-RH-Linha-Protheus-GPE-Como-gerar-o-demonstrativo-de-M%C3%A9dias-para-F%C3%A9rias)  
[RH - Linha Protheus - GPE - Como demonstrar o Salário Incorporado no Relatório de Médias de Férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008859921-RH-Linha-Protheus-GPE-Como-demonstrar-o-Sal%C3%A1rio-Incorporado-no-Relat%C3%B3rio-de-M%C3%A9dias-de-F%C3%A9rias)  
[Manual de Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=941247504)
