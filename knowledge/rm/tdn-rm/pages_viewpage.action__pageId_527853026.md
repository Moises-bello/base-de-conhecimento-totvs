---
content_hash: 1990d5558b3d82193a05fc6ab1cfb41d775c600112319413626f7b2219eef66b
fetched_at: '2026-06-29T00:10:32.749692+00:00'
page_id: '527853026'
product: rm
source: tdn-rm
title: Nota Técnica 16/2019 - "Contrato de Trabalho Verde e Amarelo"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=527853026
version: 31
---

Esta Nota Técnica tem como objetivo disponibilizar os ajustes nos leiautes do eSocial decorrentes da Medida Provisória (MP) nº 905, de 11/11/2019.

Encontra-se disponível nas versões:

**RM:**12.1.27.100, 12.1.26.153, 12.1.25.210 e 12.1.24.267

**TAF/TSS:**

[https://suporte.totvs.com/portal/p/10098/download?e=695527](https://www.google.com/url?q=https://suporte.totvs.com/portal/p/10098/download?e%3D695527&sa=D&source=hangouts&ust=1578503585216000&usg=AFQjCNFlhL5laIFvBL6vORK5TRxmin5EjQ)  
[https://suporte.totvs.com/portal/p/10098/download?e=695524](https://www.google.com/url?q=https://suporte.totvs.com/portal/p/10098/download?e%3D695524&sa=D&source=hangouts&ust=1578503585216000&usg=AFQjCNF_CQxNnqEB8F4tMA2Y0ZXx5VzFew)   

Esse contrato foi instituído pela Medida Provisória nº 905/2019 de 11/11/2019, e os trabalhadores contratados nessa modalidade serão representados por duas novas categorias:

* 107 - Empregado - Contrato de trabalho Verde e Amarelo - sem acordo para antecipação mensal da multa rescisória do FGTS
* 108 - Empregado - Contrato de trabalho Verde e Amarelo - com acordo para antecipação mensal da multa rescisória do FGTS

Atenção

É necessário executar o RM.Atualizador.exe e alterar a Versão do Layout para 2.5.00 NT 16/2019 para que as categorias 107 e 108 sejam criadas e disponibilizadas no Cadastro de Funcionários.

**Funcionário | Registros**

**Observação:**

Para que o funcionário seja participante do "Contrato de Trabalho Verde e Amarelo", deverá ter idade entre 18 a 29 anos, a data de admissão deverá ser a partir de 01/01/2020 e deverá ter a categoria 107 ou 108.

**Alterações Contempladas nesta Nota Técnica:**

**S-1200 -** **Remuneração de trabalhador vinculado ao Regime Geral de Previd. Social**

| Grupo | Descrição do Grupo | Alteração |
| --- | --- | --- |
| infoComplCont | Informações complementares contratuais do trabalhador | O ((se {codCateg} <> [101,102, 103, 104, 105, 106, 107, 108, 111, 301, 302, 303, 306, 307, 309]) E (se para o trabalhador não houver evento S-2300 ativo)); N (nos demais casos). |

**S-2200- Cadastramento Inicial do Vínculo e Admissão/ingresso de Trabalhado**

| Grupo | Descrição do Grupo | Alteração |
| --- | --- | --- |
| tpRegPrev | Tipo de Regime Previdenciário | Tipo de regime previdenciário conforme opções abaixo: 1 - Regime Geral da Previdência Social - RGPS; 2 - Regime Próprio de Previdência Social - RPPS; 3 - Regime de Previdência Social no Exterior. Validação: Se {codCateg} = [104], deve ser preenchido com [1]. Se {codCateg} = [101, 102, 103, 105, 106, 107, 108, 111], não pode ser preenchido com [2]. Valores Válidos: 1, 2, 3. |

**S-2206 - Alteração de Contrato de Trabalho**

| Grupo | Descrição do Grupo | Alteração |
| --- | --- | --- |
| tpRegPrev | Tipo de Regime Previdenciário | Tipo de regime previdenciário conforme opções abaixo: 1 - Regime Geral da Previdência Social - RGPS; 2 - Regime Próprio de Previdência Social - RPPS; 3 - Regime de Previdência Social no Exterior. Validação: Se {codCateg} = [104], deve ser preenchido com [1]. Se {codCateg} = [101, 102, 103, 105, 106, 107, 108, 111], não pode ser preenchido com [2]. Valores Válidos: 1, 2, 3. 23 infoRegimeTrab altContratual G - 1-1 - - Informações do regime trabalhista |

**Relatórios:**

Tratamento nos relatórios S-5001, S-5002, S-5003, S-5011 e S-5013, veja detalhes em
