---
article_id: 4406631332119
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: d0899ffcdf3a627ed088acb1d61df76ff0cfeb206b1890fe92024355b04576da
fetched_at: '2026-06-28T22:37:20.260018+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Protheus - SIGAGCT  - O que fazer quando
  ocorrer o Help CNT120ESTMDREV ao Tentar Estornar a Nova Medição?
type: support-article
updated_at: '2025-09-24T12:02:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406631332119-Cross-Segmentos-TOTVS-Backoffice-Protheus-SIGAGCT-O-que-fazer-quando-ocorrer-o-Help-CNT120ESTMDREV-ao-Tentar-Estornar-a-Nova-Medi%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22178306461207) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**

O que fazer quando ocorrer o Help CNT120ESTMDREV ao Tentar Estornar a Medição do Contrato?   
  
**Ambiente**

Microsiga Protheus – Gestão de Contratos – A partir da versão 12

**Causa**

Quando o Parâmetro MV\_CNREVMD está com conteúdo .F. a cada Revisão Realizada no Contrato é atualizado o campo CND\_REVISA com o número da Revisão atual, relacionado com a Planilha, nas medições realizadas antes da Inclusão da Revisão.

Medições geradas em revisões diferentes à do contrato com o parâmetro **MV\_CNREVMD** desativado, não poderão ser estornadas.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406631494935)

Ao tentar estornar uma Medição com o parâmetro **MV\_CNREVMD** desativado será apresentado o Help **CNT120ESTMDREV**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406631277975)

**Solução**

Para que o estorno ocorra corretamente, faz-se necessário desfazer a(s) revisão(s), até a revisão original, ou seja, que a revisão vigente do contrato seja a revisão em que a medição em qeustão foi incluida.

Lembrando que para se desfazer uma revisão, esta revisão não pode ter nenhuma medição realizada ou em aberto, necessitando também se estornar as medições desta revisão que se deseja "desfazer".

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406663057943)

***Observação:***

Para os contratos que foram incluídos com o parâmetro **MV\_CNREVMD** desativado, temos uma rotina que foi disponibilizada para realizar esse ajuste dos campos **CND\_REVGER**para possibilitar o estorno da medição.

Vale ressaltar que o processamento do ajuste só **é feito na filial logada**, e é **imprescindível que inicialmente esse programa seja executado em uma base de testes para validar seu correto funcionamento.**

Para configurar a rotina, seguir os passos abaixo:

1- Acesse o **Configurador(SIGACFG)**

No menu selecionar Ambiente → Cadastros → Menus;

Na tela gerada, desmarque a opção **"Todos os menus";**

Marque a opção **Gestão de Contratos** e selecione o botão **"ok".**

**![](https://tdn.totvs.com/download/attachments/644304405/image2021-10-13_10-25-36.png?version=1&modificationDate=1634133149683&api=v2)**

2- Na tela gerada, selecione o botão "**Adicionar"**

**![](https://tdn.totvs.com/download/attachments/644304405/image2021-10-13_10-27-21.png?version=1&modificationDate=1634133149640&api=v2)**

Utilize a barra de rolagem para encontrar a opção **"Contratos";**

Selecione a opção **Contratos;**

Selecione a opção **Novo Item;**

**![](https://tdn.totvs.com/download/attachments/644304405/image2021-10-13_10-31-21.png?version=1&modificationDate=1634133149593&api=v2)**

3- Na tela de configuração do item, preencha conforme os dados a seguir:

**Desc. Português:** Atualizar tabela CND;

**Programa:** GCTAjstCND;

**Status:** Habilitado;

**Módulo:** Gestão de Contratos;

**Tipo:** Função Protheus;

Selecione a opção Ok

![](https://tdn.totvs.com/download/attachments/644304405/image2021-10-13_10-35-21.png?version=1&modificationDate=1634133149550&api=v2)

4- Após incluir o novo Item no Menu, selecione a opção **Gerar.**

Na janela Gerar Menu, digite no campo o valor **SIGAGCT.**

Selecione a opção **Gerar.**

![](https://tdn.totvs.com/download/attachments/644304405/image2021-10-13_10-41-42.png?version=1&modificationDate=1634133149507&api=v2)

Confirme a geração do Menu.

![](https://tdn.totvs.com/download/attachments/644304405/image2021-10-13_10-42-54.png?version=1&modificationDate=1634133149460&api=v2)

Confirme a substituição do Menu.

![](https://tdn.totvs.com/download/attachments/644304405/image2021-10-13_10-43-31.png?version=1&modificationDate=1634133149413&api=v2)

5- Acesse a Rotina de Atualização no módulo Gestão de Contratos;

Menu: Atualizações → Contratos→Atualizar tabela CND.

Será exibida a seguinte tela de aviso:

![](https://tdn.totvs.com/download/attachments/644304405/image2021-10-13_10-47-17.png?version=1&modificationDate=1634133149333&api=v2)

**Opções:**

**Imprimir** - Realiza a impressão de um relatório com a relação das medições que terão o campo CND\_REVGER ajustados com o conteúdo do campo CND\_REVISA, sem processar a atualização. Essa opção realiza apenas a consulta do que será atualizado.

**Processar** - Realiza de fato o processamento da atualização. Como dito antes, o processamento atualiza as informações dos dados **na filial logada.**No momento de realizar o processo, é imprescindível que o mesmo inicialmente seja feito em uma base de testes para garantir sua correta funcionalidade.

**Cancelar** - Fecha a tela de atualização.

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Qual o conceito do parâmetro MV\_CNREVMD - Revisão para Medições ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022468051-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Qual-o-conceito-do-par%C3%A2metro-MV-CNREVMD-Revis%C3%A3o-para-Medi%C3%A7%C3%B5es)

[DT Ao tentar estornar medição é gerado a mensagem CNT120ESTMDREV](https://tdn.totvs.com/x/FU5nJg)

[Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
