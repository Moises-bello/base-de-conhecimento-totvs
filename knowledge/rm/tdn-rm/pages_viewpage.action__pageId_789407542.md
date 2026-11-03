---
content_hash: 0cc1a01541e0581beb1e772e2ab6f947b77808b86925eef76770d1ffb638274f
fetched_at: '2026-06-29T00:11:39.760935+00:00'
page_id: '789407542'
product: rm
source: tdn-rm
title: Alterações - S-2200 - S-1.2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=789407542
version: 27
---

false

**A partir das Versões:**

* 12.1.2302.235
* 12.1.2306.182
* 12.1.2310.116 e superiores

**CONTEÚDO**

IMPORTANTE!

---

## **01. VISÃO GERAL**

Este documento visa apresentar as mudanças no evento S-2200 para atender o Leiaute do eSocial versão S-1.2.

## **02. ALTERAÇÕES REALIZADAS**

### **02.01.** **TAG <descrDep> - DESCRIÇÃO DA DEPENDÊNCIA**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {dependente}: incluído campo (descrDep) | - | Informar a descrição da dependência. **Validação:** Informação obrigatória e exclusiva se tpDep = [99]. |

**Alteração:** Criado o campo "**Descrição da Dependência**" no cadastro de dependentes do funcionário, que, quando preenchido, resultará na geração da tag <**descrDep**>.  
Quando selecionada a opção "9 - Outros" no campo "Grau de Parentesco", o campo "**Descrição da Dependência"** será habilitado para preenchimento.

O campo "**Descrição da Dependência**" se tornará obrigatório quando o IRRF estiver marcado na aba de incidência.

 

 Quando houver um preenchimento ou alteração no campo "**Descrição da Dependência**", um gatilho S-2205 será gerado.

### **02.02.** **GRUPO <aprend> - APRENDIZ**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {aprend}: alterada regra dos grupos, dos campos existentes e incluído novos campos | **N** (se codCateg for diferente de [103]); **OC** (se codCateg = [103] e se grupo desligamento não estiver preenchido); **F** (nos demais casos) | **N** (se codCateg for diferente de [103]); **O** (se codCateg = [103] e se dtAdm >= [2024-01-22]); **OC** (se codCateg = [103], se dtAdm < [2024-01-22] e se grupo desligamento não estiver preenchido); **F** (nos demais casos) |

**Alteração:** Criação de uma aba específica para inserir os dados do aprendiz, de acordo com o leiaute especificado.

No cadastro do funcionário, ao selecionar o código de categoria eSocial "103 - Empregador - Aprendiz", uma nova aba chamada "**Dados do Aprendiz**" será habilitada no menu lateral "Registro".

Nesta tela você poderá informar:

* + **Modalidade de Contratação** (<indAprend>) - Direta ou Indireta, sendo:

1 - **Contratação direta**: contratação do aprendiz efetivada pelo estabelecimento cumpridor da cota de aprendizagem  
2 - **Contratação indireta**: contratação do aprendiz efetivada por entidades sem fins lucrativos ou por entidades de prática desportiva a serviço do estabelecimento cumpridor da cota 

* + CNPJ do estabelecimento onde estão sendo realizadas as **atividades práticas** (<cnpjPrat>), quando ocorrer uma das situações abaixo:

a) Modalidade alternativa de cumprimento de cota de aprendizagem (neste caso, informar o CNPJ da entidade concedente da parte prática);  
b) Realização das atividades práticas na empresa contratante do serviço terceirizado;  
c) Centralização das atividades práticas em estabelecimento da própria empresa, diverso do estabelecimento responsável pelo cumprimento da cota. 

* + CNPJ da **Entidade Qualificadora** (<cnpjEntQual> - no caso de contratação direta) ou CPF/CNPJ do **empregador cotista** (<nrInsc> - no caso de contratação indireta)

Exemplo de geração do XML:

* + Contratação **direta**

* + Contratação **indireta**

**DICA!** É possível preencher os campos de forma global através do menu Administração de Pessoal | Alterações Cadastrais | Alteração Campos do Cadastro.

**Saiba mais**  
Veja mais detalhes sobre a contratação de aprendiz em:

* + [Contratação de Aprendiz - Leiaute S-1.2](https://tdn.totvs.com/pages/viewpage.action?pageId=795092070)

## **03. MAPEAMENTO DO EVENTO**

Acesse o mapeamento do evento clicando no link abaixo:

* + - [Evento S-2200](https://tdn.totvs.com/display/LRM/Evento+S-2200)
