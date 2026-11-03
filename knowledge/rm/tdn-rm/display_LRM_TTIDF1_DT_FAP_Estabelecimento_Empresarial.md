---
content_hash: e4e760484138cdb8975b417f878a7bbafca854994d6b160baaa066676e26d011
fetched_at: '2026-06-29T00:06:20.722553+00:00'
page_id: '223152420'
product: rm
source: tdn-rm
title: TTIDF1_DT_FAP_Estabelecimento_Empresarial
type: documentation
url: https://tdn.totvs.com/display/LRM/TTIDF1_DT_FAP_Estabelecimento_Empresarial
version: 1
---

# FAP ESTABELECIMENTO EMPRESARIAL

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projeto* |
| **Módulo:** | *Folha de Pagamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Anexo de Seção FAP por Estabelecimento* | FopFAPEstabelecimentoAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Folha Analítica** | *FopFolhaAnaliticaAction* | | *Guia de INSS* | FopRelGuiaINSSAction | | Troca Código de Seção | FopTrocaCodigoSecaoAction | | Reestruturação de Seção | FopPropostaReestruturacaoSecaoAction | | Fórmula FAP por Estabelecimento Chapa e Data | FAPCHAPADATA | | Liberação de Competência | FopRotinasLibCompetenciaAction | |  |  | |
| **Cadastros Iniciais:** | Cadastro de seções com as seções centralizadas de CNPJ informadas. |
| **Parâmetro(s):** | *Definido o parâmetro  "Código de Quebra para CNPJ" informado em Parametrizador / 06.04 - RH - Máscaras e Quebras* |
| **Ponto de Entrada:** | *Anexo "FAP por Estabelecimento Empresarial" da seção centralizadora de CNPJ* |
| **Chamados Relacionados** | *TTCSDP.* |
| **Requisito (ISSUE):** | FAP ESTABELECIMENTO EMPRESARIAL |
| **País(es):** | *Brasil.* |
| **Banco(s) de Dados:** | *Homologados para linha RM* |
| **Tabelas Utilizadas:** | PSECAOFAPESTABELECIMENTO: Armazena as vigência para cada Seção centralizadora de CNPJ PSECAOFAPALIQUOTA: Armazena as alíquotas para o FAP em sua própria vigência correspondente a vigência para a seção centralizadora |
| **Sistema(s) Operacional(is):** | *Homologados para linha RM* |
| **Versões/Release:** | *11.82.42* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

## Descrição

De acordo com resolução CNPS nº 1.327 de 24/09/2015 publicada no Diário Oficial de 25/09/2015, o FAP (Fator Acidentário de Prevenção), o qual estabelece que o cálculo da GPS em 2016 deverá ser determinado por estabelecimento, ou seja, poderemos ter casos de FAP diferentes entre Matriz e Filiais de uma mesma Coligada.

Para atender a resolução CNPS nº 1.327 foi criado o anexo "FAP por estabelecimento empresarial" no cadastro de seção.

Deve ser informado a vigência em que o estabelecimento terá o FAP diferenciado. Após efetuar este cadastro deve relacionar a vigência para Alíquota com o seu valor.

Conforme descrito acima, para o controle do FAP por estabelecimento, a duas vigências: Uma para definir o período em que o estabelecimento usará FAP diferenciado do Valor fixo, e outra para definir uma ou mais alíquota dentro da vigência principal.

Com estas duas vigências informada o sistema poderá identificar se utilizará o FAP do valor fixo ou do anexo da seção.

Nos módulos que utilizam o FAP como Folha Analítica, GUIA de INSS o sistema irá identificar a seção centralizadora de CNPJ do funcionário está sendo processado e verificará se no primeiro dia da competência informada a vigência para o FAP por estabelecimento, caso haja irá buscar a alíquota, caso não haja irá buscar a alíquota no valor fixo. Porém caso haja vigência para o FAP por estabelecimento, mas não tendo vigência para alíquota. O sistema não processará o funcionário ou seção, informando no log as seções e ou funcionários que não foram processadas.

O sistema irá consistir o cadastro para o FAP por estabelecimento empresarial, a saber:

* O FAP deverá ser informado nas seções centralizadoras de CNPJ de acordo com o informado no parâmetro "Código de Quebra para CNPJ". Será emitida uma mensagem de alerta caso a seção não seja centralizadora de CNPJ;
* As datas de início e fim de vigências são obrigatórias;
* A data final deverá ser maior ou igual a data inicial;
* Não será permitido informar vigências em que o intervalo de datas tenha interseção com vigência já cadastradas;
* A vigência do FAP deverá englobar todas as vigências de suas respectivas alíquotas;
* O valor da alíquota dever ser maior que zero.
* Ao Excluir uma vigência para o FAP por estabelecimento todas as suas alíquotas também serão excluídas.

Na Folha Analítica os campos que utilizam o FAP são: "INSSTotalEmpSatJustTerc" e "INSS (Emp+SATAju+Terc)". Quando a seção centralizadora de CNPJ possui vigência cadastrada para FAP por Estabelecimento no primeiro dia da competência, mas não possui vigência para alíquota o sistema não processa a seção e informa no Log a mensagem: "Seção {1} Não foi processado. Seção centralizadora de CNPJ Não possui Alíquota para FAP por Estabelecimento".

Na Guia de INSS o campo "Acidente Trabalho" e consequentemente os que são impactado por ele utilizaram o FAP por estabelecimento ou pelo valor fixo seguindo as mesmas regras citadas para Folha Analítica.  Quando a seção centralizadora de CNPJ possui vigência cadastrada para FAP por Estabelecimento no primeiro dia da competência, mas não possui vigência para alíquota o sistema não processa a seção e informa no Log a mensagem: "Coligada {0} Seção {1} Não foi processada. Seção centralizadora de CNPJ Não possui Alíquota para FAP por Estabelecimento em dd/mm/aaaa".

O SEFIP o FAP é informado no aplicativo do governo e por isso não foi necessários ajustes quanto ao FAP.

A Liberação de Competência irá estender a vigência do FAP por estabelecimento assim como é feito para o valor fixo, desde de que o campo "Atualiza final de vigência na liberação de competência" tenha sido marcado. No  Log do debug é informado "Atualizando vigência para FAP por Estabelecimento".

Os novos cadastros foram contemplados no processo de "Troca código de seção".

Foi criado a formula "FAPCHAPADATA" que recebe como parâmetros a data e a chapa do funcionário, a seção centralizadora é obtida pela histórico de seção do funcionário. A formula retora 0 (Zero) se a seção centralizadora de CNPJ não tem cadastrado vigência de FAP por estabelecimento, -1 quando possui vigência para o FAP mas não possui alíquota na data informada, ou o valor da alíquota referente ao FAP.

## Procedimento para Implantação

Para versões que exige conversão de dados deverá rodar o script "ExecSql.TOTVSFolhadePagamento.FAPEstabelecimento.zip" no portal do cliente.

" constante na instalação em "".

Depois de rodar o script proceder a instalação  da versão conforme o script de instalação

## Procedimento para Utilização

1. **Acessar a visão ou dialogo da seção centralizadora de CNPJ e clicar no anexo FAP por Estabelecimento Empresarial.**
2. **Será mostrado a visão com as vigências do FAP por Estabelecimento Empresarial;**
3. **Ao incluir ou editar uma vigência do FAP é mostrado o formulário de cadastro em que é solicitado os campos:**
   1. Início de Vigência do FAP
   2. Fim de Vigência do FAP
   3. Descrição
   4. Atualiza final de vigência na liberação de Competência
4. **Após informar os campos acima click no botão "Salvar" no canto inferior direito desta tela**
5. **Com a vigência do FAP cadastrada pode-se incluir as vigências e valores das alíquotas na visão das Alíquotas para o FAP**
6. **Ao clicar nos botões de incluir ou editar é apresentado o formulário para edição das vigência e valor para alíquota em que solicitado os campos:**

   1. **Início de Vigência da Alíquota**
   2. **Fim de Vigência da Alíquota**
   3. **Valor**
7. **Após informar os dados para vigência da alíquota click em salvar.**
8. **Se todas as regras de validação forem atendidas a vigência para alíquota será gravada no banco de dados. Caso ocorra alguma inconsistência ao clicar no botão "Salvar" ou "Ok" localizados no canto inferior direito do formulário para vigência do FAP será emitida as mensagens com as regras de validação que não foram satisfeita.**

**Efetuar o cadastro da vigência para o FAP por Estabelecimento Empresarial e salvar. Em seguida cadastrar a vigência e o valor para a(s) alíquota(s).**

## Ponto de Entrada

|  |  |
| --- | --- |
| **Descrição:** | *Anexo da seção centralizadora de CNPJ* |
| **Localização:** | *Visão ou dialogo da seção* |
| **Eventos:** | *FAP por Estabelecimento Empresarial* |
| **Programa Fonte:** | FopFAPEstabelecimentoAction |
| **Função:** | Folha Analítica Guia de INSS Troca Código de Seção Reestruturação de Seção Fórmula FAP por Estabelecimento Chapa e Data FAPCHAPADATA Liberação de Competência |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | **Alíquota do FAP** | decimal | **Alíquota do FAP** | Não | |  |  |  |  | |  |  |  |  | |

divs
