---
article_id: 1500005726641
category: Integrações Nativas
content_hash: 62f77beb479bc4614b2a3b9a6c0b8f425bad19778eeade3f750edce29da6339a
fetched_at: '2026-06-28T22:42:35.522820+00:00'
product: protheus
section_id: 360012117933
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Produto Mão de Obra
type: support-article
updated_at: '2026-01-05T16:44:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005726641-Manufatura-Linha-Protheus-MNT-Produto-M%C3%A3o-de-Obra
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37449730120471)** Tempo aproximado para leitura: **00:02:10 min**  
  
**Dúvida**  
Quais processos são relacionados ao **Produto Mão de Obra** e quais produtos são utilizados no custeio no **Manutenção de Ativos - SIGAMNT**?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integrações Nativas - Versão 12  
  
**Solução**  
Os processos do **Produto Mão de Obra** são divididos em dois, **MOD** **- Mão de obra** e **PRODMOD - Produto mão-de-obra**:  
  
**MOD**  
Este trata-se do conceito padrão de produto para custos de mão de obra. Sempre que cadastrado um novo **Funcionário - MNTA020**é gerado de forma automática o **Produto - SB1**constituído pelo código **MOD + Centro de Custo** do **Funcionário**. Este produto assume como custo inicial o valor informado no campo **Salário - T1\_SALARIO**e posteriormente é tratado como os demais produtos da tabela sofrendo ajustes com o recalculo do custo médio.  
  
**PRODMOD**  
Ao realizar o cadastro de um **Funcionário - MNTA020**é possível informar o campo **Prod. MO - T1\_PRODMO**vinculando o funcionário a um produto, desta forma sempre que este funcionário for reportado como mão de obra em uma ordem de serviço, serão geradas movimentações e custeios calculados com base no produto indicado. Este conceito, porém, não é obrigatório. Trata-se de uma alternativa para o conceito**MOD**, sendo que sem parametrizar a sua utilização será mantido o comportamento atual.  
Para o produto poder ser utilizado para esta finalidade, deve-se possuir o parâmetro **MV\_PRODMOD - Utilização de Produto Mão de Obra** habilitado, igual a **T - True**, e o campo **C.C. p/ Custo - B1\_CCCUSTO**devidamente informado no **Cadastro do Produto - MATA010**.  
  
**Saiba mais**  
Para ter acesso a documentação deste processo, acesse o *link*: [Produto Mão de Obra](https://tdn.totvs.com/pages/viewpage.action?pageId=569476718)
