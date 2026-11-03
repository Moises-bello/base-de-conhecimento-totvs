---
content_hash: f6ed9983d1229aeba5bf0944c8fe73201eb672b6d15b1e730eff3d354aa7df6a
fetched_at: '2026-06-29T00:11:40.462475+00:00'
page_id: '794392909'
product: rm
source: tdn-rm
title: Alterações - S-2500 - S-1.2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=794392909
version: 26
---

false

**A partir das Versões:**

* 12.1.2302.235
* 12.1.2306.182
* 12.1.2310.116 e superiores

**CONTEÚDO**

IMPORTANTE!

---

## **01. VISÃO** **GERAL**

Este documento visa apresentar as mudanças no evento S-2500 para atender o Leiaute do eSocial versão S-1.2.

## **02. INCLUSÕES E ALTERAÇÕES REALIZADAS**

### **02.01.****Criado os campos pensAlim, percAliment e vrAlim no grupo infoDeslig:**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {infoDeslig}: incluído campo (pensAlim) | - | Preenchimento obrigatório e exclusivo se o vínculo for celetista (em S-2200 = [1]). |
| Grupo {infoDeslig}: incluído campo (percAliment) | - | Deve ser maior que 0 (zero) e menor ou igual a 100 (cem). Informação obrigatória e exclusiva se pensAlim = [1, 3]. |
| Grupo {infoDeslig}: incluído campo (vrAlim) | - | Deve ser maior que 0 (zero). Informação obrigatória e exclusiva se pensAlim = [2, 3]. |

**Alteração:** Campo **Indicativo de pensão alimentícia para fins de retenção de FGTS** e seus respectivos, serão habilitados ao selecionar o **tipo de regime trabalhista** igual a 1.

### **02.02. Grupo {unicContr}**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {infoContr}: Alterada condição do grupo (unicContr) | O (se indUnic = [S]; N (nos demais casos) | O (se infoContr/tpContr = [9]); N (nos demais casos) |

**Alteração:**Grupo passou a ser obrigatório se Tipo de Contrato for igual à 9.

Ao selecionar o Tipo de Contrato 9, os campos relacionados ao vinculo serão habilitados.

### **02.03.****GRUPO** **<infoVlr> - INFORMAÇÕES DOS PERIODOS E VALORES DECORRENTES DE PROCESSO TRABALHISTA**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {infoVlr}: incluído campo (indReperc) | - | **Valores válidos:** **1** - Decisão com repercussão tributária e/ou FGTS **2** - Decisão sem repercussão tributária ou FGTS **3** - Decisão com repercussão exclusiva para declaração de rendimentos para fins de Imposto de Renda |
| Grupo {infoVlr}: incluído campo (indenSD) | - | Houve decisão para pagamento da indenização substitutiva do seguro-desemprego? **Valores válidos:** **S** - Sim |
| Grupo {infoVlr}: incluído campo (indenAbono) | - | Houve decisão para pagamento da indenização substitutiva de abono salarial? **Valores válidos:** **S** - Sim |

**Alteração:** Criado os campos **indReperc, indenSD e indenAbono** no cadastro de informações do período.

Campo indicativo de repercussão deve ser preenchido, já os demais são opcionais.

### **02.04.** **GRUPO****<abono> - INDENIZAÇÃO SUBSTITUTIVA DE ABONO SALARIAL**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {abono}: incluído campo (anoBase) | - | O (se indenAbono = [S]); N (nos demais casos) |

**Alteração:** Criado a **tag <anoBase>** para informar o ano-base que houve indenização substitutiva do abono salarial.  
Será habilitado quando o campo **Houve decisão para pagamento da indenização substitutiva de abono salarial?** for preenchido.

### **02.05.** **GRUPO****<idePeriodo> - IDENTIFICAÇÃO DO PERIODO AO QUAL SE REFEREM AS BASES DE CÁLCULO**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {idePeriodo}: incluído campo (perRef) | O (se repercProc = [1]); OC (nos demais casos) | O (se indReperc = [1]); N (nos demais casos) |

****Alteração: Campo será obrigatório quando o indicativo de repercussão for preenchido.****

### **02.06.** **GRUPO****<baseCalculo> -****BASES DE CÁLCULO DA CONTRIUIÇÃO PREVIDENCIARIA**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {baseCalculo}: incluído campo (vrBcCpMensal,vrBcCp13) | O | OC |

**Alteração:** Campos serão habilitados se indicativo de repercussão for preenchido igual à **1- Decisão com repercussão tributária e/ou FGTS.**

## 

## **03. EXCLUSÕES REALIZADAS**

### **03.01.** **GRUPO <dependente> - EXCLUIDO GRUPO E SEUS RESPECTIVOS CAMPOS**

```

```

### **03.02. TAG** **<indUnic> - INDICATIVO RECONHECIMENTO DE UNICIDADE CONTRATUAL**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {infoContr}: excluído campo (indUnic) | Indicativo se houve reconhecimento de unicidade contratual (declaração da continuidade do contrato de trabalho, considerando como único dois ou mais vínculos sucessivos informados no eSocial). **Valores válidos:** **S** - Sim **N** - Não **Validação:** Deve ser igual a [N] se o grupo  for informado. | Excluído |

### **03.03. GRUPO** **<infoVlr> - INFORMAÇÕES DOS PERIODOS E VALORES DECORRENTES DE PROCESSO TRABALHISTA**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {infoVlr}: excluído campo (repercProc) | Repercussão do processo trabalhista ou de demanda submetida à CCP ou ao NINTER. **Valores válidos:** **1** - Decisão com pagamento de verbas de natureza remuneratória **2** - Decisão sem pagamento de verbas de natureza remuneratória | Excluído |
| Grupo {infoVlr}: excluído campo (vrRemun) | Valor total das verbas remuneratórias a serem pagas ao trabalhador. **Validação:** Se repercProc = [1], deve ser maior que 0 (zero). Se repercProc = [2], deve ser igual a 0 (zero). | Excluído |
| Grupo {infoVlr}: excluído campo (vrAPI) | Valor do aviso prévio indenizado pago ao empregado. **Validação:** Deve ser maior ou igual a 0 (zero). | Excluído |
| Grupo {infoVlr}: excluído campo (vr13API) | Valor da projeção do aviso prévio indenizado sobre o 13º salário. **Validação:** Deve ser maior ou igual a 0 (zero). | Excluído |
| Grupo {infoVlr}: excluído campo (vrInden) | Valor total das demais verbas indenizatórias a serem pagas ao trabalhador. **Validação:** Deve ser maior ou igual a 0 (zero). | Excluído |
| Grupo {infoVlr}: excluído campo (vrBaseIndenFGTS) | Valor da base de cálculo para recolhimento da indenização compensatória (multa rescisória) do FGTS, para geração de guia. Preencher este campo somente quando o valor da indenização compensatória (multa rescisória) do FGTS for objeto de transação. **Validação:** Deve ser maior ou igual a 0 (zero). | Excluído |
| Grupo {infoVlr}: excluído campo (pagDiretoResc) | A indenização compensatória (multa rescisória) do FGTS transacionada foi paga diretamente ao trabalhador mediante decisão/autorização judicial? **Valores válidos:** **S** - Sim **N** - Não **Validação:** Informação obrigatória e exclusiva se vrBaseIndenFGTS  estiver preenchido. | Excluído |

### **03.04. GRUPO****<baseCalculo> - BASES DE CÁLCULO DE COTRIUIÇÃO PREVIDENCIARIA E FGTS DECORRENTES DE PROCESSO TRABALHISTA**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {baseCalculo}: excluído campo (vrBcFgts) | Valor da base de cálculo do FGTS sobre a remuneração do trabalhador (sem 13° salário). **Validação:** Deve ser maior ou igual a 0 (zero). | Excluído |
| Grupo {baseCalculo}: excluído campo (vrBcFgts13) | Valor da base de cálculo do FGTS sobre a remuneração do trabalhador sobre o 13º salário. **Validação:** Deve ser maior ou igual a 0 (zero). | Excluído |

### **03.05. GRUPO****<infoFGTS> - EXCLUIDO TODOS OS CAMPOS EXISTENTES NO S-1.1 E CRIADOS NOVOS CAMPOS**

## **04. MAPEAMENTO DO EVENTO**

Acesse o mapeamento do evento clicando no link abaixo:

* + [Evento S-2500](https://tdn.totvs.com/display/LRM/Evento+S-2500#Leiautes-2)
