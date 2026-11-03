---
article_id: 26335953529239
category: Gestão de Transportes (TMS)
content_hash: 7eec89ea5240a5e4e6fe6f8d5b66a3243f150510c9f49bd919b2bf66ca0bd96c
fetched_at: '2026-06-28T22:45:27.758812+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Existe Integração do TMS x GPE para o Contrato
  de Carreteiro?
type: support-article
updated_at: '2024-09-13T11:55:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26335953529239-Log%C3%ADstica-Linha-Protheus-TMS-Existe-Integra%C3%A7%C3%A3o-do-TMS-x-GPE-para-o-Contrato-de-Carreteiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26335953500439) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Existe Integração do **TMS - Gestão de Transportes** x **GPE - Gestão de Pessoal** para o Contrato de Carreteiro?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões.  
  
**Solução**O Protheus **TMS** não possui integração do contrato de carreteiro com o **GPE**.  
Ao gerar o contrato de carreteiro, caso a natureza utilizada no cadastro do fornecedor esteja configurada para calcular os impostos, os títulos referentes aos mesmos serão gerados no **Financeiro**.  
Dentro do módulo **Financeiro**, existe a possibilidade de integração destes títulos com o **GPE**.  
Além da natureza de operação, deve ser avaliado dentro do **TMS** o parâmetro **MV\_TMSVDEP - Valor por Dependente**.  
  
Para vincular a matrícula do funcionário do **GPE** com o cadastro do motorista no **TMS**, as informações que existirem nos dois módulos o Sistema integra. Entretanto, a integração acontece somente na primeira inserção da matrícula, se após a inserção for necessário realizar uma alteração, é preciso alterar em ambos os cadastros.  
Quando a alteração está sendo realizada no **TMS**, não podemos alterar essa informação no **GPE**, pois o cadastro do **GPE** é o mais atualizado no Sistema. Caso necessário, alterar a informação no **TMS**, porém quando houver alteração no **GPE** favor utilizar o ponto de entrada **GP010VALPE.**  
  
**Saiba mais**  
Para mais detalhes de como funciona a integração dos títulos no **Financeiro** para o **GPE**, verifique a documentação  [Geração de Dados SEFIP (FINA402A)](https://tdn.totvs.com/pages/releaseview.action?pageId=315890750)  
Para mais informações sobre o Ponto de Entrada **GP010VALPE**, verifique a documentação [GP010VALPE - InclusãoAlteração de Funcionários](https://tdn.totvs.com/pages/releaseview.action?pageId=6079099)
