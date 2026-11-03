---
article_id: 23501513457047
category: Originação de Grãos (OG)
content_hash: e72f07d28554094f6f5ab3f89a8afee978f9ccec63c1ae6ef1c726b183803c18
fetched_at: '2026-06-28T22:45:43.741141+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Procedimento para o Controle de Contratos por
  Qtd Física ou Fiscal
type: support-article
updated_at: '2025-07-12T10:54:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23501513457047-Agro-Linha-Protheus-AGR-Procedimento-para-o-Controle-de-Contratos-por-Qtd-F%C3%ADsica-ou-Fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23501513443735) Tempo aproximado para leitura: **00:05:10 min****Dúvida**Qual é o **Procedimento para Controle do Contratos por Qtd Física ou Fiscal**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

**1. CONFIGURAÇÃO DE PARÂMETROS PROTHEUS:**

No **Configurador (SIGACFG)**, acesse **Ambientes/Cadastros/Parâmetros (CFGX017)**. Crie/configure o(s) parâmetro(s) a seguir:

|  |  |
| --- | --- |
| **Itens/Pastas** | **Descrição** |
| **Nome:** | MV\_AGOCLAS |
| **Tipo:** | *Logico* |
| **Título** | Utiliza classificação por local(Origem/Destino). |
| **Opções** | .T.=Sim;.F.=Não |
| **Cont. Por.:** | F |
| **Descrição:** | Indica se utiliza classificação por local(Origem/Destino). |

**2. Contrato de Compra OGA280:**Para cadastrar o **contrato de compras**, deve-se informar qual classificação **1-Destino ou 2-Origem**, ela deve ser considerada no momento do cálculo dos descontos do romaneio.

![CADS.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23501579585047)

**3. Contrato de Vendas OGA290:**

Para cadastrar o **contrato de vendas**, deve-se informar qual classificação **1-Destino ou 2-Origem** deve ser considerada no momento do cálculo dos descontos do romaneio.

![CADS1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23511363556631)

 **4.** **Romaneio c\ pesagem OGA250:**

```
No romaneio, se utilizar classificação por local ativo (MV_AGOCLAS), então é apresentada na tela dois grupos de exames (origem/destino).
```

Os itens da tabela de desconto serão mostrados um para origem e outro para destino;

![CADS2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23511367136791)

 No momento da atualização do romaneio o Sistema verifica qual classificação deve ser considerada no momento do cálculo dos descontos conforme o último contrato selecionado; 

Se a classificação do contrato selecionado for igual a **2-Origem**, o Sistema obriga o usuário a preenche o campo **Peso Origem**:

![CADS3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23511363578391)

 No momento da atualização, o Sistema verifica quais itens da classificação são obrigatórios e obriga o usuário a informa-los;  
Os cálculos dos descontos são feitos de acordo com as classificações informadas conforme o último contrato vinculado ao romaneio.  
  
**5. Relatório classificações do Contrato:**

Foi desenvolvido um novo relatório para melhor analise das classificações por romaneio.

As informações são agrupadas primeiramente por **Entidade**, **Contrato**, **Produto**, **Safra e Tipo do contrato**:

![](https://tdn.totvs.com/download/attachments/274308830/image2017-4-25%2017%3A20%3A12.png?version=1&modificationDate=1494502194000&api=v2)

Depois outro agrupador são o **Romaneio**, **Data**, **Peso origem**, **Peso destino**, **Peso liquido e Total desconto**:

![](https://tdn.totvs.com/download/attachments/274308830/image2017-4-25%2017%3A21%3A30.png?version=1&modificationDate=1494502194000&api=v2)

E por fim, são apresentados os resultados das classificações conforme descrição dos itens da tabela de classificação por **Destino e Origem**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23511367164311)

**6. Impressão de romaneio:**

Na impressão do romaneio foram adicionados os campos que indicam a classificação que foi considerada para os descontos, e o **peso aferido** na origem do romaneio:

![CADS4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23511363594263)

**7.** **Movimento Romaneio/ Classificações:**Na tela de **Movimento Romaneio/ Classificações** foi adicionada a coluna **Classificado** que indica a classificação que foi considerada para os descontos do romaneio, os dados das classificações mostradas em seguida são referentes a classificação do romaneio **1-Destino/2-Origem**:

![CADS5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23511363611287)
