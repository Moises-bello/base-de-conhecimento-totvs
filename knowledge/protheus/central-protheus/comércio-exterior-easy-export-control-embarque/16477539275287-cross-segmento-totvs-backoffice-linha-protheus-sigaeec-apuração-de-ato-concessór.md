---
article_id: 16477539275287
category: Comércio Exterior - Easy Export Control - Embarque
content_hash: adf902d3bcc72d54b07163669f59f7f9d612beed24a4eeb9dd723cad84526024
fetched_at: '2026-06-28T22:36:56.527612+00:00'
product: protheus
section_id: 1500001549322
source: central-protheus
title: ' Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Apuração de
  Ato Concessório - Drawback'
type: support-article
updated_at: '2023-08-02T16:41:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16477539275287--Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Apura%C3%A7%C3%A3o-de-Ato-Concess%C3%B3rio-Drawback
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16477548107031) Tempo aproximado para leitura: **10:00 min** **Dúvida**É possível associar Atos Concessórios aos itens que serão exportados dentro do SIGAEEC?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**A apuração do Ato Concessório é a rotina do módulo de exportação que possibilita, na fase de Embarque, associar Atos Concessórios aos itens que serão exportados.

Ao associar o Ato Concessório, as quantidades envolvidas serão reservadas no Ato Concessório para seja efetivamente baixadas ao exportar as mercadorias (registro de DUE e embarque efetivo).

A associação do Ato Concessório envolve duas etapas, a definição do Ato Concessório e a avaliação dos saldos do Ato Concessório a ser associado.  
  
**Apuração de Ato Concessório:****- Associação Automática:**

Neste cenário, o sistema irá buscar automaticamente os Atos Concessórios que melhor se enquadram aos itens do Embarque, de acordo com as opções de apropriação definidas.

Para executar a busca automática é necessário selecionar a tela de itens do Embarque (**Outras Ações \ Pedidos**) e então executar a associação a partir da opção **Apuração do Ato Concessório**, disponível no menu **Outras Ações**.

Após acessar esta opção, será exibida a tela de definição de "**Opções de Apropriação Automática"**, conforme abaixo:

![](https://tdn.totvs.com/download/attachments/306855356/image2021-7-14_17-48-18.png?version=1&modificationDate=1626295699280&api=v2)

Nesta tela, é possível informar o tipo de saldo a ser utilizado e as regras de apropriação, conforme abaixo:

**- Escolha do saldo a ser utilizado na apropriação:**A escolha do saldo a ser utilizado na apropriação define qual tipo de saldo do Ato Concessário será utilizado para verificar se existe saldo disponível para associação aos itens do Embarque, sendo possível escolher entre:

1. **Saldo a exportar do compromisso de exportação:** Nesta opção, o sistema irá considerar o saldo a exportar do compromisso total de exportação do Ato Concessório, ou seja, o quanto já foi exportado frente ao compromisso original. Neste caso, a quantidade a ser considerada na associação será a quantidade que está sendo exportada.
2. **Saldo a exportar do insumo no Ato Concessório:** Nesta opção, o sistema irá considerar o saldo a exportar referente ao saldo de insumos já importados no Ato Concessório, ou seja, o quanto ainda é necessário exportar para comprovar os insumos que já foram importados. Neste caso, a quantidade a ser considerada na associação será a maior quantidade necessária para comprovar o saldo de insumos já importados. Ou seja, caso o saldo a exportar seja menor do que a quantidade efetivamente exportada, ao associar o sistema irá dividir o item do embarque em dois, um com a associação do Ato Concessório e a quantidade correspondente, e o outro com o saldo não associado.

**- Escolha da regra de apropriação:**A escolha da regra de apropriação determina como a rotina irá se comportar diante da identificação de Atos Concessórios disponíveis para vinculação, de acordo com o tipo de saldo informado. É possível escolher entre quatro regras, conforme abaixo:

1. **Apropria automaticamente quando há comprovação para todos os insumos:** Neste caso, o sistema somente irá associar um ato concessório caso exista comprovação de importação para todos os insumos associados. Caso não haja importação (com saldo) de todos os insumos associados à quantidade exportada, o Ato Concessório será desconsiderado.
2. **Exibe tela de confirmação quando não há comprovação para todos os insumos:** Caso exista comprovação de importação parcial dos insumos envolvidos, ou seja, alguns insumos tenham comprovação de importação (com saldo) e outros não, será exibida tela de confirmação para que o usuário avalie os saldos dos insumos e confirme ou cancele a associação do Ato Concessório.
3. **Apropria automaticamente quando há comprovação para ao menos um insumo:** Caso ao menos um dos insumos associados ao produto exportado possua comprovação de importação (com saldo), a associação do Ato Concessório é feita automaticamente, sem exibição de tela de confirmação para que o usuário confirme ou cancele a associação do Ato Concessório.
4. **Sempre exibe tela de confirmação:** Sempre será exibida a tela de confirmação para que o usuário confirme ou cancele a associação do Ato Concessório, independente da existência ou não de comprovação de importação (com saldo) dos insumos associados ao item exportado.

**- Busca pelo Ato Concessório:**Após a definição das opções de associação automática, o sistema irá iniciar a busca pelos Atos Concessórios para cada item do embarque. Assim que um Ato Concessório for identificado, caso ele se enquadre em alguma regra de associação automática ele será associado ao item correspondente ou, caso tenha sido escolhida alguma opção de exibição de tela de confirmação, e ele se enquadre na regra escolhida, será exibida a tela de confirmação, com detalhes dos insumos envolvidos, para que o usuário confirme ou cancele a associação.  
Neste caso, se o usuário cancelar a associação, o sistema irá seguir buscando outros Atos Concessórios até que o usuário confirme a associação de um deles ou não restem Atos Concessórios disponíveis na base de dados.  
  
**- Associação Manual:**Para efetuar a associação manualmente, na tela de edição dos itens do Embarque, é possível digitar o número do Ato Concessório desejado no campo "**Ato Concess.**" (**EE9\_ATOCON**) e a sequência do item no Ato Concessório no campo "**Seq. AC**" (**EE9\_SEQED3**), ou então, selecionar o Ato Concessório desejado e sua sequência na consulta padrão disponível no campo "**Ato Concess.**" (**EE9\_ATOCON**).

Após associar um Ato Concessório manualmente, ao confirmar a manutenção nos dados do item, o sistema irá exibir a tela de escolha de opções de apropriação, com as mesmas opções disponíveis na opção de busca automática. Caso o Ato Concessório informado não atenda às configurações definidas, a associação será cancelada e os dados do Ato Concessório serão removidos do item.  
  
**- Definição automática das opções de apropriação:**É possível parametrizar o sistema para que as opções de apropriação sejam definidas automaticamente, sem que a tela de configuração seja exibida. Para isso, é necessário configurar os parâmetros abaixo de acordo com as opções desejadas.

|  |  |  |  |
| --- | --- | --- | --- |
| **Parâmetro** | **Tipo** | **Descrição** | **Opções de Conteúdo** |
| **MV\_EEC0004** | Numérico | Define o tipo de saldo a ser considerado na Apropriação do Ato Concessório | **1**=Saldo a exportar do compromisso de exportação  **2**=Saldo a exportar do insumo no Ato Concessório |
| **MV\_EEC0005** | Numérico | Define a regra de apropriação do Ato Concessório aos itens do Embarque | **1**=Apropria automaticamente quando há comprovação para todos os insumos  **2**=Exibe tela de confirmação quando não há comprovação para todos os insumos  **3**=Apropria automaticamente quando há comprovação para ao menos um insumo  **4**=Sempre exibe tela de confirmação |

Com estes parâmetros definidos, a tela de configuração de opções de apropriação deixará de ser exibida, e as regras definidas nos parâmetros irão valer para todos os usuários.  
  
**Saiba mais: [Apuração de Ato Concessório - Drawback (EECAE101 - SIGAEEC)](https://tdn.totvs.com/pages/releaseview.action?pageId=306855356)**
