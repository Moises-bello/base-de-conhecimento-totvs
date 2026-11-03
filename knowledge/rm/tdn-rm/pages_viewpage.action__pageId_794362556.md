---
content_hash: d04edad8d7f6de5851322742d09b8c358dfba1ea101413733f0ec26501e72d09
fetched_at: '2026-06-29T00:11:40.074977+00:00'
page_id: '794362556'
product: rm
source: tdn-rm
title: Alterações - S-2206 - S-1.2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=794362556
version: 13
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

Este documento visa apresentar as mudanças no evento S-2206 para atender o Leiaute do eSocial versão S-1.2.

## **02. ALTERAÇÕES REALIZADAS**

### **02.01.** **GRUPO <aprend> - APRENDIZ**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {aprend}: alterada regra dos grupos, dos campos existentes e incluído novos campos | **OC** (se codCateg = [103]); **N** (nos demais casos) | **O** (se codCateg = [103] e se dtAlteracao >= [2024-01-22]); **OC** (se codCateg = [103] e se dtAlteracao < [2024-01-22]); **N** (nos demais casos) |

**Alteração:** Criação de uma aba específica para inserção dos detalhes do aprendiz, conforme as especificações do leiaute.

No cadastro do funcionário, menu lateral "**Registro**", ao informar o código de categoria eSocial como "**103 - Empregador - Aprendiz**", o sistema irá habilitar uma nova aba chamada "**Dados do Aprendiz**".

Nesta tela você poderá informar:

* + **Modalidade de Contratação** (<indAprend>) - Direta ou Indireta, sendo:

1 - **Contratação direta**: contratação do aprendiz efetivada pelo estabelecimento cumpridor da cota de aprendizagem  
2 - **Contratação indireta**: contratação do aprendiz efetivada por entidades sem fins lucrativos ou por entidades de prática desportiva a serviço do estabelecimento cumpridor da cota 

* + CNPJ do estabelecimento onde estão sendo realizadas as **atividades práticas** (<cnpjPrat>), quando ocorrer uma das situações abaixo:

a) Modalidade alternativa de cumprimento de cota de aprendizagem (neste caso, informar o CNPJ da entidade concedente da parte prática);  
b) Realização das atividades práticas na empresa contratante do serviço terceirizado;  
c) Centralização das atividades práticas em estabelecimento da própria empresa, diverso do estabelecimento responsável pelo cumprimento da cota. 

* + CNPJ da **Entidade Qualificadora** (<cnpjEntQual> - no caso de contratação direta) ou CPF/CNPJ do **empregador cotista** (<nrInsc> - no caso de contratação indireta)

Ao realizar uma alteração nas telas do cadastro, o sistema irá gerar um gatilho do S-2206 para envio ao eSocial.

Exemplo de geração de XML:

* + Contratação **direta**

* + Contratação **indireta**

**DICA!** É possível realizar a alteração dos dados através do menuAdministração de Pessoal | Alterações Cadastrais | Alteração Campos do Cadastro.

**Saiba mais**  
Veja mais detalhes sobre a contratação de aprendiz em:

* + [Contratação de Aprendiz - Leiaute S-1.2](https://tdn.totvs.com/pages/viewpage.action?pageId=795092070)

## **03. MAPEAMENTO DO EVENTO**

Acesse o mapeamento do evento clicando no link abaixo:

* + [Evento S-2206](https://tdn.totvs.com/display/LRM/Evento+S-2206)
