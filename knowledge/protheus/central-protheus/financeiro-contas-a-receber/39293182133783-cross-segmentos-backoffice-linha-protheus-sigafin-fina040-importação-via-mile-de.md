---
article_id: 39293182133783
category: Financeiro - Contas a Receber
content_hash: 58979145db40dd56e2b317171502356d5664ced0cdae3f4018001868a43ff5bf
fetched_at: '2026-06-28T22:38:12.627285+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA040 - Importação
  via Mile de Contas a Receber - Modelo para Rateio de Multiplas Naturezas X Centro
  de Custo
type: support-article
updated_at: '2026-03-25T19:52:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39293182133783-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA040-Importa%C3%A7%C3%A3o-via-Mile-de-Contas-a-Receber-Modelo-para-Rateio-de-Multiplas-Naturezas-X-Centro-de-Custo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39293182118295) Tempo aproximado para leitura: **00:15:00 min**  
  
**Dúvida**  
Como realizar importação de títulos a receber via MILE com rateio de múltiplas naturezas X centro de custo?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**

Para realizar a importação dos dados na rotina **FINA040 - Contas a Receber** utilizando o MILE, são necessárias algumas configurações adicionais conforme veremos a seguir.

Basicamente, o MILE funciona da seguinte forma: para cada canal criado, será enviado sequencialmente para a rotina em questão um array como parâmetro, seguido do **nOpc** de 3 de inclusão.

Ao realizar a chamada da **MsExecAuto** da rotina **FINA040**, será enviado da seguinte forma:

Se tivermos 1 canal (1 Master):

* **FMile040(vetor[1], 3)**

Se tivermos 2 canais:

* **FMile040(vetor[1], vetor[2], 3)**

E assim por diante.

**Importante**

A rotina FINA040 possui suporte ao tipo de Adapter **Função** (Veja no documento de referência o item - tópico [Composição do Layout - Geral](https://tdn.totvs.com/display/public/framework/MILE+-+Model+Integrator+Layout+Engine#MILEModelIntegratorLayoutEngine-Geral))

O parâmetro **MV\_MULNATR** deve estar habilitado **.T.**para que os registros sejam importados com sucesso.

1- Acessar o módulo Configurador **(SIGACFG)** - Acessar o caminho **Ambiente >> Aceleradores >> Mile >> Layouts;**

Baixar o layout que consta no link a seguir:

[FINA040 Importação via Mile de Contas a Receber - Modelo para Rateio de Multiplas Naturezas X Centro de Custo](https://tdn.totvs.com/pages/releaseview.action?pageId=732684425)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39293930680215)

2- Clicar em Outras ações >> **Layouts >>Importar**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39293930681623)

3- Após importação, validar se todos os campos estão iguais ao da documentação do TDN referenciado acima, caso sim, pode seguir ao passo 4.

4- Iremos utilizar uma **User Function** para execução do **Adapter, na qual está também na documentação TDN do produto, conforme print a seguir.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39293922296471)

Precisa copiar todo conteúdo deste exemplo e compilar em seu RPO.Custom do ambiente onde será executado a inclusão via **MILE**.

No campo "ADAPTER", precisa constar o nome da **User Function, exemplo.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39293922297367)

5- Criar o arquivo **TXT** no qual precisa ser preenchido com base nas informações que deseja inserir no contas a receber, e precisam ser dados que existam em seu ambiente, como natureza, centro de custo, código do cliente e loja.

**EXEMPLO DE ARQUIVO DE IMPORTAÇÃO - TXT**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39293922298135)

6- Acessar o módulo Configurador **(SIGACFG)** - Acessar o caminho **Ambiente >> Aceleradores >> Mile >> Layouts;**

Dentro da rotina, **Outras ações > Proc. TXT**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39293930684055)

Selecionar o arquivo **.TXT**gravado e realizar a Importação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39293930684695)

7- Tela de Processamento para informar se foi concluído com sucesso ou se apresentou algum incidente na importação, após isso é possível validar o registro no contas a receber caso não tenha ocorrido incidentes.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39293930685847)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39293922302999)

**Saiba mais:**

[**FINA040 Importação via Mile de Contas a Receber - Modelo para Rateio de Multiplas Naturezas X Centro de Custo**](https://tdn.totvs.com/pages/releaseview.action?pageId=732684425)

[Framework - Linha Protheus - MILE: Model Integrator Layout Engine](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028814432-Framework-Linha-Protheus-MILE-Model-Integrator-Layout-Engine)

[Mile Importação e Exportação do Layout](https://tdn.totvs.com/pages/releaseview.action?pageId=423932458)
