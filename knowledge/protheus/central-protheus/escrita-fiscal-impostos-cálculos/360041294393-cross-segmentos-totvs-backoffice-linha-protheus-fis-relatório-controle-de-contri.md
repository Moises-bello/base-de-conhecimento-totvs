---
article_id: 360041294393
category: Escrita Fiscal - Impostos - Cálculos
content_hash: bc27ed241019f2053d39c1ef0a5caef25b3fd37ead82965a88bc414f173489e5
fetched_at: '2026-06-28T22:39:31.141728+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Relatório Controle
  de Contribuição de Seguridade Social
type: support-article
updated_at: '2021-07-29T14:19:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041294393-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Relat%C3%B3rio-Controle-de-Contribui%C3%A7%C3%A3o-de-Seguridade-Social
---

**Dúvida**Qual o relatório para Controle de Contribuição de Seguridade Social?  
   
 **Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 12  
  
**Solução**

Foi implementado o relatório Controle de Contribuição de Seguridade Social (MATR945) que permite a geração de dados consolidados por CNPJ, atendendo à gestão corporativa.

A contribuição previdenciária prevista pela Lei nº 8.540/92, que tem como base de cálculo o valor da comercialização da produção rural do empregador rural, pessoa natural, visa recolher contribuições destinadas ao financiamento da previdência social dos trabalhadores rurais.

A rotina aqui descrita gera um relatório de controle com entradas e saídas realizadas, que devidamente parametrizadas, irão gerar os valores de cálculo de contribuição em cada documento. O sistema trata exclusivamente das informações referentes às Notas Fiscais relativas aos produtos que tenham saído ou entrado no estabelecimento.

Para atendimento a esta funcionalidade, foi criada a pergunta Seleciona Filiais?, permitindo que o usuário selecione as filiais que possuem o mesmo CNPJ e estejam no mesmo grupo de empresas, e foi criada a pergunta Aglutina por CNPJ?, a qual permite que o usuário realize a geração das informações dessas filiais de forma consolidada, totalizando a movimentação de várias filiais na mesma divisão do relatório.

**Importante**

A seleção de filiais estará disponível apenas para as filiais dentro do mesmo grupo de empresas corrente.  
A pergunta **Aglutina por CNPJ?** somente terá funcionalidade se a pergunta **Seleciona Filiais?** estiver configurada com o conteúdo igual a **Sim**.  
A pergunta **Aglutina por CNPJ?** somente terá funcionalidade para ambientes dbAccess.  
A pergunta **Considera Filiais?, Filial De? e Filial Até?** somente terá funcionalidade para ambientes *CodeBase* (somente quando existir a pergunta na rotina).  
Quando utilizada a opção de seleção de filiais, a janela de seleção de filiais será ordenada por CNPJ + I.E.

**Procedimento para Implementação**

1. No **Configurador (SIGACFG)**, acesse **Ambiente/Cadastros/Parâmetros** e verifique ou crie os parâmetros a seguir:![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054762693/mceclip0.png)
2. No **Configurador (SIGACFG)**, acesse **Base de Dados/Dicionário/Base de Dados**, verifique os campos dos parâmetros a seguir ou crie-os, caso não existam:

           Tabela **SB1 – Cadastro de Produtos**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053912814/mceclip0.png)**

#### **Importante**

 Para o recolhimento da obrigação é necessário que, além do campo do cadastro de produtos citado acima, o campo **Gera Duplicata?** referente à TES dos itens das notas de entrada e saída movimentados estejam preenchidos com “Sim”, caso contrário o sistema não realizará o controle da obrigação.

#### **Procedimentos para utilização**

 No **Livros Fiscais (SIGAFIS)**, acesse **Relatórios/List.Conferência/Contr.Segur.Social (MATR945)**. Observe o preenchimento dos parâmetros conforme instruções a seguir:   
  
**Data Emissão De?** Informe a data inicial de emissão para o movimento de notas fiscais de entrada e saída.   
  
**Data Emissão Até?** Informe a data final de emissão para o movimento de notas fiscais de entrada e saída.  
  
**Movimentos?**   
Selecione a opção referente à operação desejada:   
       • Entradas – Listará somente as notas fiscais de entrada;   
       • Saídas – Listará somente as notas fiscais de saída;   
       • Ambos – Listará as notas fiscais de entrada e saída  
  
**Data de Digitação De?**   
Informe a data inicial de digitação para o movimento de notas fiscais de entrada. Não influencia no movimento de notas fiscais de saída.   
  
**Data de Digitação Até?**   
Informe a data final de digitação para o movimento de notas fiscais de entrada. Não influencia no movimento de notas fiscais de saída.   
  
**Seleciona Filiais?**   
Determina se apresenta uma tela posterior ao assistente para que sejam selecionadas algumas filiais para processamento, filiais que componham um grupo que não obedeça à ordem seqüêncial e por isso não podem ser indicadas num intervalo de/até. Ex.: Gerar o arquivo das filiais 01, 05, 10 e 13.   
  
**Aglutina por CNPJ?**   
Indica se deve agrupar o movimento das filiais por CNPJ, considerando as filiais com mesmo CNPJ como se fossem apenas uma filial no sistema.   
    **SIM** – Ao selecionar o agrupamento, o sistema apresentará os totais consolidados por dia, somando a movimentação de todas as filiais.   
**NÃO** – Ao selecionar que não aglutine, o sistema apresentará os totais separados por cada data e filial origem da movimentação.

#### **Importante**

O sistema somente fará a emissão com os totais consolidados por dia se o parâmetro **Seleciona Filiais?** estiver preenchido com **“SIM”** e o parâmetro **Aglutina por CNPJ?** estiver preenchido com **“SIM”**.   
As demais combinações serão apresentadas com os totais separados por filial origem e data da movimentação.

Confira os dados e **confirme.**

#### 

#### **Importante**

Para alterações da alíquota Funrural de 2.3% para 0,02%, conforme ações judiciarias movidas por alguns produtores e empregadores rurais, cuja causa tem sido aceita por inconstitucionalidade do Art. 25 da Lei nº 8.212/91.  
Usar ponto de entrada **[MTR94501](http://tdn.totvs.com/pages/viewpage.action?pageId=189302567)**

Informações adicionais:**<https://tdn.totvs.com/pages/releaseview.action?pageId=189302879>**
