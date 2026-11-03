---
article_id: 360051284794
category: RH - Arquivos Bancarios
content_hash: 7b812430d35c75ac49a78f5e93e9b3db7fa5bd58042f89b0a152785fb2b69111
fetched_at: '2026-06-28T22:43:38.367802+00:00'
product: protheus
section_id: 360004833673
source: central-protheus
title: RH - Linha Protheus - GPE - Passo a Passo para Geração do relatório de líquidos
  - GPER020
type: support-article
updated_at: '2021-04-26T16:34:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051284794-RH-Linha-Protheus-GPE-Passo-a-Passo-para-Gera%C3%A7%C3%A3o-do-relat%C3%B3rio-de-l%C3%ADquidos-GPER020
---

**Dúvida**Passo a Passo para Geração do relatório de líquidos - GPER020  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**  
**Acesse:** Relatórios -> Periódicos -> Líquidos  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081610853/mceclip1.png)  
  
**Procedimento:** Informe qual o roteiro que será utilizado para impressão do relatório.   
  
**Qto a Cta. Corrente:** Apresenta funcionários com conta corrente cadastrada, sem conta corrente cadastrada ou ambos.  
  
**Filial:** Selecione as filiais que deseja incluir na geração do relatório.

**Importante:** Para **definir intervalos de dados sequenciais utilizar hífen (1-3)** e **para os não sequenciais, ponto e vírgula (3;5;1).** Utilizar aspas simples somente para desconsiderar hifens nos conteúdos. (Ex: '00001-1'-'00004-9';00006;,00008-'00009-8').   
Obs: Essa condição se aplica as configurações das perguntas:  
-> Filial  
-> Matrícula  
-> Banco/Agência  
-> Matrícula  
-> Nome  
-> Conta Corrente  
  
**Dica:** Caso não tenha intervalo de impressão, nas mesmas configurações de perguntas descritas acima,  utilize -ZZZZZZZZ ou deixe o campo em branco, de modo que considere todas as filiais, centro de custos, banco/agência, nome e conta corrente.  
  
**Centro de custos:** Selecione os C.Custos que deseja incluir na geração do relatório.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081616933/mceclip2.png)  
  
**Banco/Agência:** Informe banco e agência para impressão do relatório.  
  
**Matrícula:** Informe o intervalo de matrículas que deseja considerar para impressão do relatório.   
  
**Nome:** Informe o intervalo de nomes de funcionários que deseja considerar para impressão do relatório.   
  
**Conta Corrente:** Informe a conta  corrente.  
  
**Situações:** Selecione as situações do funcionário para filtro dos dados.   
**Obs:** A situação para filtro fará a busca no cadastro de funcionário (Situação Normal / Afastado / Demitido / Férias / Transferido)  
  
**Totaliza por filial/UN/Emp:** Informe se totaliza por filial, unidade de negócio ou empresa.  
  
**![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080906014/mceclip5.png)****Filial/Un/Emp em outra página:** Informe se imprime Filial / Unidade / empresa em outra página. **Nome dos Funcionários:** Informe se imprime nome do funcionário. **Data de pagamento De:** Data de pagamento inicial.**Data de pagamento Até:** Data de pagamento final. **Importante:** Informe os campos de busca de pagamento de acordo com a data do cálculo realizado. Sempre verifique se a data gravada na cálculo é compatível com a data informada. **Agência Outra Pág:** Informe se imprime agência em outra página.  
 **Totaliza por Agência:** Informe se totaliza por agência.

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081999033/mceclip4.png)**

**Tipo de relação:** Informe se deseja imprimir o relatório de forma analítica (detalhes), ou se deseja imprimir Sintética (resumo) dos valores.   
  
**Imprimir:** Informe se deseja imprimir Funcionários, Beneficiários ou Ambos.   
  
**Categorias:** Informe ou selecione as categorias do Funcionário que deseja imprimir.  
  
**Seleção de Processos:** Selecione os processos que possuem cálculo e que deverão compor o relatório.  
  
**Totaliza por banco:** Exibe o relatório com total dos valores com quebra de banco.
