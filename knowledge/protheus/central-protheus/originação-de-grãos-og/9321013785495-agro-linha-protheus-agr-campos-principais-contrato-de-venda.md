---
article_id: 9321013785495
category: Originação de Grãos (OG)
content_hash: 904ea67d7bbb0ae7a3ab57d9175c55bd85c7199c70c0203be8711c647d1454a7
fetched_at: '2026-06-28T22:45:37.425661+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Campos Principais - Contrato de Venda
type: support-article
updated_at: '2025-06-23T15:54:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9321013785495-Agro-Linha-Protheus-AGR-Campos-Principais-Contrato-de-Venda
---

*****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18365375892759)***** Tempo aproximado para leitura: **00:02:40 min****Dúvida**  
Como identificar os Principais Campos num Contrato de Venda?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) -Versão 12  
  
**Solução**  
Para solucionar essa dúvida, efetue os seguintes passos:  
1. Verifique o Contrato de Venda quando a inclusão é realizada por meio da rotina clássica de comercialização **MV\_AGRO002** com conteúdo igual .F, possui os principais campos citados abaixo;

* [Dados Básicos](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142)
* [Quantidades](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142)
* [Dados Negócio / Financeiro](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142)
* [Logística](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142)
* [Previsão de Entrega](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142)
* [Financeiro](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142)
* [Corretoras](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142)
* [Recebimento](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142)

Nesse espaço são definidos os itens principais do contrato de venda como: cliente, safra, produto e TES.

| Campo | Descrição |
| --- | --- |
| Entidade | Código do cliente para quem destina-se a venda. |
| Safra | Código da Safra na qual o commodities se refere. |
| Produto | Código do produto que será comercializado no contrato de venda. |
| TES | Tipo de Entrada/Saída. A TES é responsável pela correta classificação tributária dos documentos fiscais de entrada e saída registrados no sistema. |
| Operação | Permite informar o código da operação. Esse dado é apenas informativo. O cadastro da operação é realizada por meio do programa **[OGA310 - Operações](https://tdn.totvs.com/pages/viewpage.action?pageId=547867348).** |

2. Verifique o Contrato de Venda quando gerado por meio da rotina da Nova Comercialização **MV\_AGRO002** com conteúdo igual .T, possui os principais campos citados abaixo;

* [Dados Básicos](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Quantidades](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Logística](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Previsão de Entrega](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Financeiro](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Corretoras](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Exportação](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [PEPRO](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Recebimento](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)

Nesse espaço são definidos os itens principais do contrato de venda como: cliente, safra, produto e TES.

| Campo | Descrição |
| --- | --- |
| Entidade | Código do cliente para quem destina-se a venda. |
| Safra | Código da Safra na qual o commodities se refere. |
| Produto | Código do produto que será comercializado no contrato de venda. |
| TES | Tipo de Entrada/Saída. A TES é responsável pela correta classificação tributária dos documentos fiscais de entrada e saída registrados no sistema. |
| Tipo Embalagem | Tipo de embalagem. Quando definido no Cadastro de Produto na pasta de Logística o preenchimento é automático. |
| Bolsa referência | Indica o código da Bolsa de Referência utilizada para buscar a cotação e exibir nos componentes vinculados a bolsa selecionada. |
| Moeda de Faturamento | Indica a moeda utilizada para buscar a cotação para faturamento. Esse campo somente é habilitado para situação de comercialização para Mercado Interno e Moeda Estrangeira definida no [Registro de Negócio](https://tdn.totvs.com/pages/viewpage.action?pageId=485869656). |
| Referência | Indica a referência de recebimento. Esse campo somente é habilitado para situação de comercialização para Mercado Interno e Moeda Estrangeira definida no [Registro de Negócio](https://tdn.totvs.com/pages/viewpage.action?pageId=485869656). Os valores aceitos são:  **1 - Faturamento.** Esta opção quando selecionada utilizará a cotação da moeda de faturamento para faturar e gerar a previsão financeira. **2 - Pagamento**. Esta opção quando selecionada utilizará a cotação da moeda de faturamento para faturar enquanto não houver o pagamento. E a previsão financeira será gerada na cotação futura da moeda de pagamento. |
| Moeda de Pagamento | Indica a moeda utilizada para buscar a cotação para geração da previsão financeira e faturamento após o recebimento. Esse campo somente é habilitado quando a Referência é do tipo 2 - Pagamento. |
| Qtd Dias | Indica a quantidade de dias para considerar na cotação. Exemplo: Se a previsão financeira foi gerada para o dia04/02/2019 e o campo Qtd Dias for informado "2" a cotação a ser considerada será06/02/2019 . Essa situação é válido tanto para a moeda de faturamento como de pagamento. |

3. Verifique na tela principal Outra Ações.

* [Regras Fiscais](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Demonstrativo de Preço](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Composição de Preço](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Romaneios](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Importar Regra Ágio/Deságio](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Consultar Negociação](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)

Permite manutenir as regras fiscais do contrato.

Por meio dessa opção é possível alterar os dados de uma regra fiscal como dividi-la e criando novas regras fiscais.

Atenção

4. Veja que essa opção está disponível apenas para o conceito da Nova Comercialização **MV\_AGRO002**[.](https://tdn.totvs.com/pages/viewpage.action?pageId=370616326)

* [Confirmar](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Conhecimento](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Cancelar](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Finalizar](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Reabrir](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Excluir](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Imprimir](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Contrato](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Histórico](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Autorizações](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Adic / Supres](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Status - Assinaturas](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Romaneios](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Vínculo Contrato](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Imprimir Word](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)

5. Confirme o Contrato de Venda. A confirmação somente é permitida para contratos com situação Prevista. A aprovação pode ocorrer automaticamente caso o parâmetro **MV\_AGRO033.** Indica se o contrato será aprovado automaticamente após alterações, esteja ligado.

6. Analise o Browser em **Outras Ações > Exclusivas > Nova Comercialização**.

* [Blocos e Fardos Vinculados](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Blocos e Fardos BCI](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Consultar Negociação](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Precificação](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Gerar Previsão Financeira](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Consulta de Previsões](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Fixação de Preço](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Iniciar Workflow da Minuta](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Emitir NF Operação Futura](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Extrato do Contrato](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Despesas Logísticas](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Painel de Instrução](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)
* [Qualidade](https://tdn.totvs.com/pages/releaseview.action?pageId=497468142#)

Permite consultar ou remover os blocos e fardos vinculados ao contrato de venda quando a commodities é Algodão.  
Essa opção de menu está disponível somente quando o parâmetro **MV\_AGRO001** está habilitado.
