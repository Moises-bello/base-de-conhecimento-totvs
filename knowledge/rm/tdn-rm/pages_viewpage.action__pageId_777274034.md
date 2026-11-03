---
content_hash: abb1b2cd06ae482f566938c0033631a4e892a6b8438363cd3a19aee31f573e51
fetched_at: '2026-06-29T00:11:37.401608+00:00'
page_id: '777274034'
product: rm
source: tdn-rm
title: Alterações - S-2205 - S-1.2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=777274034
version: 26
---

false

**A partir das Versões:**

* 12.1.2302.233
* 12.1.2306.181
* 12.1.2310.115 e superiores

**CONTEÚDO**

IMPORTANTE!

---

## **01. VISÃO GERAL**

Este documento visa apresentar as mudanças no evento S-2205 para atender o Leiaute do eSocial versão S-1.2.

## **02. ALTERAÇÕES REALIZADAS**

### **02.01.** **GERAÇÃO GATILHO S-2205**

**Alteração:** Ao marcar ou desmarcar os campos da aba "**Incidências**" no cadastro do dependente, sistema irá gerar gatilho do evento S-2205

Ao marcar ou desmarcar os campos "**Assistência Médica**" e/ou "**Pensão**" da aba "**Incidências**" no cadastro do dependente, o sistema irá gerar um gatilho do evento S-2205 para atender as mudanças no leiaute S-1.2 do evento S-1210:

Também foi incluído o evento S-2205 no processo de "**Geração de gatilho em lote**":

**Observação:** Ao selecionar o evento S-2205, o usuário poderá gerar o gatilho especifico deste evento para os dependentes que já possuem "Incide Pensão" e "Incide Assistência Médica". Dessa forma, as informações desses dependentes serão atualizadas corretamente no ambiente do governo, garantindo a conformidade dos dados de acordo com as exigências do eSocial no evento S-1210.

Segue exemplo de seleção de funcionários com dependentes que já possuem incidência de pensão ou assistência médica:

*SELECT CHAPA*  
*FROM PFUNC*  
*WHERE CODCOLIGADA = 1*  
*AND CHAPA IN(SELECT DISTINCT CHAPA*  
*FROM PFDEPEND*  
*WHERE PFUNC.CODCOLIGADA = PFDEPEND.CODCOLIGADA*  
*AND PFUNC.CHAPA = PFDEPEND.CHAPA*  
*AND (INCASSISTMEDICA = 1 OR INCPENSAO = 1))*

### **02.01.****TAG <descrDep> - DESCRIÇÃO DA DEPENDÊNCIA**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {dependente}: alteração campo (descrDep) | - | Informar a descrição da dependência. **Validação**: Informação obrigatória e exclusiva se tpDep = [99]. |

**Alteração:**Criado o campo "**Descrição da Dependência**" no cadastro de dependentes que, ao ser preenchido, será gerando a tag <***descrDep***>.

Ao informar no campo "**Grau de parentesco**" a opção "**9-Outros**", será habilitado o campo "**Descrição da Dependência**".

O campo "**Descrição da Dependência**" será obrigatório quando na aba incidência estiver marcado IRRF:

Ao preencher ou alterar o campo "**Descrição da Dependência**"  será gerado um gatilho S-2205.

Aviso

Após a instalação do patch, é importante executar o processo **eSocial | Outros Processos | Gerar Gatilhos em Lote**. 

Recomendamos que esse processo seja executado antes do envio do evento S-1210 e de outros eventos relacionados. Dessa forma, todas as informações ficarão completas e atualizadas antes do envio dos eventos ao governo.

## **03. MAPEAMENTO DO EVENTO**

Acesse o mapeamento do evento clicando no link abaixo:

* + [Evento S-2205](https://tdn.totvs.com/display/LRM/Evento+S-2205)
