---
article_id: 360051098734
category: Gestão de Transportes (TMS)
content_hash: ea6e7f758e5d1d03848d52331864e43e57de0199dab69b53e160cfc631444ae4
fetched_at: '2026-06-28T22:45:33.457216+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Valor Informado no Frete a Receber
type: support-article
updated_at: '2025-02-24T11:16:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051098734-Log%C3%ADstica-Linha-Protheus-TMS-Valor-Informado-no-Frete-a-Receber
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20884234088983)**Tempo aproximado para leitura:**00:02:10 min**  
**Dúvida**Como utilizar o componente de frete do tipo **07 - Valor Informado** no frete a receber **TOTVS Logística TMS**?   
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões  
  
**Solução**O componente de frete do tipo **07 -** **Valor Informado** é utilizado para quantidades que não podem ser previstas, tais como: ajudantes, diárias, etc. O valor deste componente é configurado na **Tabela de Frete** e no momento de entrada da nota fiscal do cliente, determinamos sua quantidade manualmente. Essa quantidade informada pelo usuário, será multiplicada pelo valor inserido na **Tabela de Frete.**Se deseja gerar um documento que o valor final seja apenas o valor digitado, deve-se utilizar a funcionalidade de **Frete Informado**.  
  
Para utilizar o componente de valor informado, é necessário efetuar os seguintes cadastros:

* Em **Atualizações/Comercial/ Componentes Frete - TMSA030**, inclua o componente de frete e preencha os campos **Calc. Sobre - DT3\_TIPFAI,** **Faixa por - DT3\_FAIXA**como **07 - Valor Informado, Agrupa Vl.Nf -  DT3\_AGRVAL = 2 - Não** e **Fração - DT3\_FRACAO = 1 - Percentual.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25934707476759)

* Em **Atualizações/Comercial/Config. Tab. Frete - TMSA130**, inclua uma configuração de tabela de frete que possua os componentes desejados e o componente de valor informado. Se não deseja utilizar o componente de **Valor Informado** em todos os cálculos, pode definir o campo **Comp. Obrig. - DVE\_COMOBR**como **2 - Não.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079689374)

* Em **Atualizações/Comercial/ Tab. Frete - TMSA010**, inclua uma tabela de frete para as regiões desejadas utilizando a configuração de tabela de frete incluída anteriormente. No componente de Valor Informado, informe os valores desejados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25934693176343)

* Em **Atualizações/Comercial/Contrato Cliente - TECA250**, informe a tabela de frete cadastrada no serviço que irá utilizar nos campos **Tab. Frete - DDA\_TABFRE** e **Tp. Tab. Frete - DDA\_TIPTAB.**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079690414)

* Em **Atualizações/ Recebimento/ Entrada de Documentos - TMSA050**, ao incluir um documento do cliente, acesse a opção **Outras Ações/ Val. Inf.**para informar o quantidade desejada que será multiplicada pelo Valor do componente de **Valor Informado** informado na **Tabela de Frete.**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080769993)

* Após preencher o Valor Informado e todos os outros campos necessários para a inclusão de um documento, pode acessar a opção **Outras Ações/Vis.Frete** e visualizar que o componente de **Valor Informado**já está incluso no cálculo. Neste exemplo, o Sistema multiplicou a qtde 200 pelo Valor 1 configurado na **Tabela de Frete**.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080770253)

**Saiba mais**Documentação sobre a funcionalidade de **Frete Informado:**[Logística - Linha Protheus - TMS - Frete Informado para Frete a Receber](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027399631-Log%C3%ADstica-Linha-Protheus-TMS-Frete-Informado-para-Frete-a-Receber)
