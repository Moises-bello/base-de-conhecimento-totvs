---
article_id: 235078628
category: Gestão de Armazenagem (WMS)
content_hash: c65e3961e18158e3b01bea650987376223067a6a641b3a7e486ee2ae324f4a1f
fetched_at: '2026-06-28T22:45:47.954010+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Distribuição - Linha Protheus - WMS - Otimizar o processo de expedição no armazém
  de WMS
type: support-article
updated_at: '2025-10-31T20:06:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/235078628-Distribui%C3%A7%C3%A3o-Linha-Protheus-WMS-Otimizar-o-processo-de-expedi%C3%A7%C3%A3o-no-armaz%C3%A9m-de-WMS
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35447481586455)**Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Como otimizar o processo de expedição no armazém de **WMS - *Warehouse Management System***?  
  
**Ambiente**  
TOTVS Distribuição - TOTVS WMS (Linha Protheus) - Gestão de Armazenagem (WMS) – A partir da versão 11.80  
  
**Solução**Existem algumas configurações que podem ser feitas no **WMS** que podem auxiliar no processo de expedição, a fim de agilizar o processo e oferecer ganho de produtividade na separação dos produtos no armazém.  
  
Durante a geração das atividades de separação é possível juntar ou aglutinar atividades semelhantes, desde que separem de um mesmo produto e rastrode um mesmo endereço. Este processo fará com que as coletas nestes endereços sejam minimizadas.   
  
Recomendamos esta configuração nos casos onde será realizada uma conferência posterior, dos pedidos separados ou dependendo da escolha da aglutinação, onde não importa que numa mesma carga, produtos de pedidos diferentes sigam numa mesma embalagem ou palete, por exemplo, quando direcionados para um mesmo cliente ou destino.   
  
A aglutinação é configurada no cadastro de **Tarefas X Atividades - WMSA080**, através do campo **Tipo de Aglut - DC6\_TPAGLU.** Os valores possíveis para o campo são:

1. Não Aglutina
2. Documento
3. Cliente/Fornecedor
4. Carga
5. Carga/Cliente
6. Produto

Além da aglutinação, é possível minimizar a movimentação do operador de separação dentro do armazém, forçando o mesmo a executar várias separações de forma consecutiva, sem ter a necessidade de fazer uma movimentação de cada quantidade separada para a doca.   
  
Para isto, podem ser utilizados para esta situação os parâmetros **MV\_RFENDDE - Solicita Confirmação Endereço Destino Separação** e **MV\_WMSMTEA - Permite Selecionar Múltiplas Atividades**, no caso do **WMS** atual. Já para o novo **WMS** estes dois parâmetros foram descontinuados. E devido a isto, é no cadastro **Serviços X Tarefas - WMSA070**, no campo **Mult. Ativ. - DC5\_MLTATI** que a configuração deverá ser efetuada.  
  
Para minimizar ainda mais o esforço necessário para realizar a separação dentro do armazém de **WMS**, pode ser criada uma regra de convocação de sequenciamento de endereços, a fim de ordenar a separação do documento para o operador, de forma que ele siga um caminho sequencial ao invés de ficar se movimentando de lado a lado no armazém.   
  
**Saiba mais**  
Mais informações a respeito da regra de convocação podem ser obtidas no **Documento de Referência** da rotina [Regras de Convocação - WMSA350](https://tdn.totvs.com/pages/viewpage.action?pageId=569501806), na seção Exemplos de Utilização.  
Também assista ao *Webinar* sobre o cadastro **Serviços** **Vs** **Tarefas** e conheça todas as configurações disponíveis: [Webinar TOTVS | Serviços](https://www.youtube.com/watch?v=f1K8WBRCUUc) [Vs Tarefas #TOTVS\_Logística\_Linha\_Protheus](https://www.youtube.com/watch?v=f1K8WBRCUUc)
