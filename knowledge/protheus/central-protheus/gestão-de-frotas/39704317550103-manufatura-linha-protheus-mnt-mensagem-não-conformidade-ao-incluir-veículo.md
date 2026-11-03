---
article_id: 39704317550103
category: Gestão de Frotas
content_hash: 6b3d542d35b055ccf79512166db028cc1f2d183676b3207578baa7dbd2b7250f
fetched_at: '2026-06-28T22:42:39.514579+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Mensagem NÃO CONFORMIDADE ao incluir veículo
type: support-article
updated_at: '2026-04-13T16:39:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39704317550103-Manufatura-Linha-Protheus-MNT-Mensagem-N%C3%83O-CONFORMIDADE-ao-incluir-ve%C3%ADculo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39704317545239) Tempo aproximado para leitura: **00:01:40 min**  
  
**Ocorrência**  
Ao tentar incluir um cadastro de **Veículo - MNTA084**, o **Sistema** apresenta a mensagem **Help: NAO CONFORMIDADE Problema: Problema no processo de integração com backoffice**.  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas - Todas as versões  
  
**Causa**  
Este incidente ocorre porque o processo de integração de Bens do **SIGAGFR - Gestão de Frotas** está condicionado ao conteúdo do parâmetro **MV\_NGINTMB** **-** **Indica integração do processo de mobilidade: sincronismo de equipamentos, parte diária e custos/apontamentos. Informe 1=Sim;2=Não**. Quando este parâmetro está preenchido com o valor **1**, a integração do processo de mobilidade fica ativa, e o **Sistema** permite a inclusão e o cadastro dos bens exclusivamente por meio do **Backoffice RM**.  
  
**Solução**  
Para solucionar essa ocorrência, caso a empresa não utilize o projeto de **Mobilidade**, realize os seguintes passos:  
1. Acesse o **SIGACFG - Configurador** e localize o parâmetro **MV\_NGINTMB**;  
2. Altere o valor do parâmetro para **2**;  
3. Salve a configuração  
4. Acesse novamente a rotina de **Cadastro de Veículos** e realize a inclusão do bem.  
  
**Importante**  
A integração de bens via mensagem única é enviada pelo Sistema sempre que o cadastro de um **Bem** for incluído, alterado ou inativado. As condições necessárias para o funcionamento pleno dessa **Integração de Bens** são o parâmetro **MV\_NGINTMB** preenchido com **1** e o campo **Sincronismo** configurado como **Sim**. A exclusão de bens não é permitida com o processo de mobilidade ativo.  
  
**Saiba mais**  
Para informações complementares a respeito do tema: [Projeto Mobilidade](https://tdn.totvs.com/display/public/PROT/TTIEX8_DT_Projeto_Mobilidade)
