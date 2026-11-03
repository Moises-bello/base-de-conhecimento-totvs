---
content_hash: 19b8e1e6b20d6341eebe831f70b795d89886f69e1fc7a027c9ac8efc003d1fe0
fetched_at: '2026-06-29T00:09:18.670802+00:00'
page_id: '421388741'
product: rm
source: tdn-rm
title: FIN - Conciliação Bancária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388741
version: 41
---

A **conciliação bancária** é um processo essencial para garantir a **precisão das informações financeiras,** **redução de erros manuais**, e **maior eficiência** operacional.  
Isso melhora a **gestão de fluxo e [gestão de caixa](https://tdn.totvs.com/pages/viewpage.action?pageId=840773775)**, facilita a **auditoria**e **reduz custos**, proporcionando um controle financeiro mais **seguro**e **confiável**.

## **01****. Visão Geral**

O **objetivo** da Conciliação Bancária é realizar, de forma automatizada, a **conciliação** entre as **informações fornecidas pelos bancos** das contas correntes e dos dados de **extrato de caixa** cadastrados no sistema.

## **02****. Passo a Passo**

* #### **Importar o extrato bancário (manual e em lote)**

É possível importar o extrato bancário de **vários bancos**. Os tipos de arquivos importados são: [CNAB](https://tdn.totvs.com/pages/viewpage.action?pageId=421388581) e [OFX](https://tdn.totvs.com/pages/viewpage.action?pageId=853311029).  
No momento da importação do arquivo bancário, caso o sistema identifique apenas uma conta/caixa com as mesmas informações de banco, agência e conta/corrente do arquivo que está sendo importado, a conta/caixa é identificada e selecionada automaticamente.  
  
À partir da release 12.1.**2502** o sistema dispõe da opção "Importar Arquivos de Conciliação em Lote", visando reduzir tempo e esforço no processo de importação dos extratos e posteriormente a conciliação**\***, evitando a importação de um arquivo por vez e por coligada, tornando toda a operação mais ágil. Através desta opção o sistema permitirá ao usuário informar um diretório para leitura dos arquivos, um para cada tipo: '.ofx' e CNAB ('.ret' ou '.txt').

480360

Este processo poderá ser executado de forma agendada e recorrente em qualquer coligada e o sistema importará os registros conforme a coligada da conta corrente associada a conta/caixa de cada banco. Por esta razão, a definição do parâmetro relacionado a conciliação global (item 3 desta página) é desconsiderada. Obs: Neste processo de importação de arquivos em lote o sistema considera o Padrão CNAB240 para os arquivos CNAB.

* **Buscar os arquivos de retorno na máquina local**

  Marque essa opção caso o caminho da pasta de leitura dos arquivos de retorno a ser considerada esteja em sua máquina local, trazendo diferença no processamento principalmente quando tratarmos de ambiente em 3 camadas ou Cloud.

* #### **Conciliar automaticamente após importação**

**\* Novidade**: À partir do patch 12.1.**2602.123** o sistema dispõe da opção "Conciliar automaticamente após importação" no processo de importação de arquivos de conciliação **em lote**, possibilitando ao operador financeiro conciliar os extratos bancários e os extratos de caixa logo após realizar a importação do (s) arquivo (s) do (s) banco (s). Vale ressaltar que os critérios para conciliação (data e/ou número do documento) são os mesmos da conciliação automática que já existia no sistema, e detalhado no próximo item da documentação. Caso o operador financeiro deixe desmarcadas as opções 'Data' e 'Número do Documento', o sistema irá considerar apenas o valor do título para efeito de busca e comparação entre o extrato bancário e o extrato de caixa para realizar a conciliação.

* #### **Conciliar as movimentações**

Concilie de forma [automática ou manual](https://tdn.totvs.com/pages/viewpage.action?pageId=421388551) as informações importadas através do **extrato bancário**, com as informações de **extrato de caixa** gerados através do recebimentos e pagamentos no sistema.

* #### **Incluir extratos correspondentes**

Caso seja identificada uma movimentação bancária importada através do extrato que não é proveniente de recebimentos ou pagamentos, como é o caso das **tarifas bancárias**, pode ser incluído de forma ágil um [extrato correspondente](https://tdn.totvs.com/display/LRM/Incluir+Extrato+Correspondente) aos dados importados.

* #### **Salvar conciliação**

Depois de **concluído** o processo de conciliação, é necessário salvar as conciliações já realizadas. Neste momento, os extratos bancários serão marcados como conciliados e ficarão disponíveis para conciliação apenas as movimentações pendentes de conciliação. Este processo permite que a conciliação possa ser realizada de **forma gradual**.

## **03****. Conciliação Global**

No caso das empresas que possuem muitas coligadas, e precisam de **agilidade no processo** de conciliação, é possível [parametrizar a coligada](https://tdn.totvs.com/display/LRM/FIN+-+Contas+a+pagar) para permitir a visualização e conciliar os extratos de **todas as coligadas**.

Atenção

A importação manual dos arquivos para conciliação e o processo de inclusão de extrato correspondente precisam ser executados pontualmente na coligada responsável pela conta.
