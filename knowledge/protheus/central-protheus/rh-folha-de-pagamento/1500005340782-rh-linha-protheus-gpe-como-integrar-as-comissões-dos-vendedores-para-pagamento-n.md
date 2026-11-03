---
article_id: 1500005340782
category: RH - Folha de Pagamento
content_hash: 7607b78bbb2054fe8bb2a87b15cfd3b53b0692dbeaf3405688fbcc0f8e18c2b6
fetched_at: '2026-06-28T22:44:11.826850+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE -  Como integrar as comissões dos Vendedores para
  pagamento  no módulo Gestão de Pessoal
type: support-article
updated_at: '2025-08-12T12:50:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005340782-RH-Linha-Protheus-GPE-Como-integrar-as-comiss%C3%B5es-dos-Vendedores-para-pagamento-no-m%C3%B3dulo-Gest%C3%A3o-de-Pessoal
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26329381870103) Tempo aproximado para leitura: 00:04:00 min**

**Dúvida**Como integrar as comissões dos **Vendedores - MATA040** para pagamento no módulo Gestão de Pessoal?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para que os valores de comissionamento sejam integrados para quitação na Folha de Pagamento módulo **Gestão de Pessoal**, o Vendedor deve estar vinculado a um registro de **Funcionário - GPEA010**. As comissões a serem pagas devem ser apuradas e integradas através da rotina  **Atualização de Pagamento de Comissões - MATA530**.  
  
1 - Efetue o cadastro do Vendedor como Funcionário na rotina **GPEA010 - Funcionários** no módulo **Gestão de Pessoal**.  
No menu, acesse **Atualizações** -> **Funcionários** -> **Funcionários**: e efetue o cadastro, não é obrigatório  vincular o mesmo a Categoria de Comissionado no campo **Cat. Func** - RA\_CATFUNC, podendo ser Mensalista, Horista ou Autônomo.   
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007301661)  
  
2 - Verifique na rotina **Verbas - GPEA040** se os identificadores de cálculo relacionados abaixo estão devidamente cadastrados:  
0121 - Comissões Rescisão   
0122 - DSR Sobre Comissões Rescisão   
0165 - Comissões  
0166 - DSR Sobre Comissões  
No menu, acesse **Atualizações** -> **Definições de Cálculo** -> **Verbas.**  
  
3 - No modulo 05 - **Faturamento** efetue o cadastro do Vendedor na rotina **Vendedores - MATA040**  
No menu, acesse **Atualizações** -> **Cadastros** -> **Vendedores**: localize a aba **Pagamento de Comissão** e relacione este cadastro com o registro de funcionário do mesmo através do campo **Funcionário**.  
No campo **Forma Pgto**, informe que o pagamento das comissões será realizada pela Folha de Pagamento, portanto selecione a opção **F - Folha de Pagamento**, depois de preencher as outras informações essenciais da rotina clique em **Salvar**.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007307741)  
  
4 - Para que as comissões apuradas pelo Faturamento sejam integradas, execute a rotina **Atualização de Pagamento de Comissões - MATA530,** informe todos os parâmetros que delimitam o cálculo de comissões, no item **Habilita interface pagamento?** selecione **Sim**. A comissão gerada pode ser observada na rotina **Manutenção de Comissões -****MATA490**.  
Ambas rotinas podem ser encontradas no Menu do Faturamento acessando -> **Atualizações** -> **Diversos**  
  
5 - Os valores de comissionamento depois de integrados, podem ser consultados na rotina de **Valores Futuros - GPEA110**.  
Acesse **Atualizações** -> **Lançamentos** -> **Valores Futuros**Para adquirir mais conhecimento acesse o(s) *link*(s) abaixo:  
[FAT0052 Configuração das Comissões dos Vendedores](https://tdn.totvs.com/pages/viewpage.action?pageId=235598457)  
[FAT0120\_Comissão\_integrada\_à\_Folha\_de\_Pagamento](https://tdn.totvs.com/pages/releaseview.action?pageId=244939939)

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
