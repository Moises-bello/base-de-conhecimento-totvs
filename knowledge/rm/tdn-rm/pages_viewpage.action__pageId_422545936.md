---
content_hash: 91d4ceea9aa05f471145efc703a1dd602dfc1926af2126244c082fa3f8255433
fetched_at: '2026-06-29T00:09:21.975437+00:00'
page_id: '422545936'
product: rm
source: tdn-rm
title: Bloco L - Lucro Líquido
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545936
version: 5
---

Neste bloco estão as informações da apuração do Lucro Líquido do declarante. É gerado quando o regime de apuração é o Lucro Real. Este bloco é composto pelos seguintes registros:

BLOCOLleftL001 L001 

**Abertura do Bloco L**

Esteé um registro de controle gerado automaticamente pelo processo da rotina que informa se existe ou não movimentação no bloco L.

L030 L030 

**Identificação dos Períodos de Forma de Apuração do IRPJ e da CSLL no ano-calendário**

Este registro será gerado de acordo com a periodicidade dos Períodos de Apuração cadastrados e encerrados para os tributos IRPJ e CSLL.

L100L100

**Balanço Patrimonial**

Este registro não será gerado pelo processo da ECF pois ele será gerado automaticamente pelo PVA através da recuperação do arquivo da ECD com base no mapeamento do Plano de Contas X Plano Referencial.

L200L200

**Método de Avaliação de Estoque Final**

Para a geração deste registro foi disponibilizado no TOTVS Gestão Contábil nos Parâmetros da ECF na aba Lucro Real o item Método de Avaliação do Estoque Final. As opções disponíveis são:   
1 - Custo Médio Ponderado  
2 - PEPS (Primeiro que entra, primeiro que sai)  
3 - Arbitramento - art.296, Inc. I e II, do RIR/99  
4 - Inventário Periódico

Este campo será disponibilizado conforme o valor informado no parâmetro Período de Apuração do IRPJ/CSLL que é informado nos parâmetros da ECF no TOTVS Gestão Fiscal, ou seja, se for Anual será apresentado apenas um campo para o método de avaliação do estoque final. Se for Trimestral serão apresentados quatro campos.

L210L210

**Informativo da Composição dos Custos**

Este registro é declarada a composição dos custos dos produtos de fabricação própria vendidos e os custos dos serviços prestados no período para as empresas que utilizam o inventário permanente.

Este registro é representado pela tabela dinâmica do bloco L210 da ECF. Estas informações serão tratadas pelo TOTVS Gestão Contábil pelo recurso do Plano Paralelo e mapeamento de Contas Contábeis. As informações para a geração deste registro serão calculadas e geradas com base nas informações das Contas Contábeis associadas aos registros deste Plano Paralelo. A exatidão e veracidade das informações dependente da correta associação das Contas Contábeis que deverá ser feita pelo próprio contribuinte.

Para agilizar o cadastro foi disponibilizado no portal do cliente o arquivo L210\_Informativo de Composição de Custos.txt contendo os itens da tabela dinâmica do registro L210 que poderá ser importado pelo  usuário utilizando o processo de [Importação de Contas Paralelas](http://tdn.totvs.com/pages/viewpage.action?pageId=423938510) via arquivo texto disponível na visão de planos paralelos no TOTVS Gestão Contábil.

***Dicas***:

* Cadastra a capa do Plano de Contas Paralelo com a máscara ##
* Ao importar desmarcar a opção Identificar/Atualizar máscara automaticamente
* Marcar a opção Não validar níveis da máscara
* Na opção Instituição Responsável do cadastro de Planos de Contas Paralelo escolher a opção Outras Estrutura.

Para a geração do registro após cadastra o plano e importar as contas deve-se:

1. Mapear as Contas Contábeis com a respectiva Conta Paralela que representa a composição do custo conforme características de sua empresa.
2. Nos parâmetros da ECF no anexo do Cadastro da Filial, Parâmetros Contábeis aba Lucro Real no item Informativo de Composição de Custos informar o Plano de Contas Paralelo criado para a composição de saldos do estoque.

Para a geração da ECF o processo irá calcular o valor a ser gerado baseando-se nos saldo das Contas Contábeis associadas às Contas Paralelas que representem o informativo de composição de custo. O saldo considerado será o de antes do encerramento. Para tanto serão desconsiderados todos os lançamentos com históricos de fechamento.

L300L300

**Demonstração do Resultado do Exercício**

Este registro não será gerado pelo processo da ECF pois na importação ou recuperação da ECD o PVA irá gera-lo automaticamente conforme o mapeamento do Plano de Contas X Plano de Contas Referencial.

L990L990

**Encerramento do Bloco L**

Este é um registro de controle gerado automaticamente pelo processo da rotina para o encerramento do bloco L.
