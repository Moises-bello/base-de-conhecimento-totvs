---
content_hash: 0289d937c5a270bdac7af3318ee5d3fa7224f86cebce4316db90031272a39da3
fetched_at: '2026-06-29T00:09:33.148916+00:00'
page_id: '425458928'
product: rm
source: tdn-rm
title: Geração de Movimento por Regime de Caixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458928
version: 77
---

---

📌 Novidades: Reforma Tributária (IBS / CBS) - Adequações na Geração de Movimento – TOTVS Educacional

As regras abaixo atendem às exigências da **Reforma Tributária (IBS/CBS)** e se aplicam à **Geração de Movimento** para emissões a partir de **janeiro de 2026**

✅Data de Competência e Emissão 

A **data de competência do movimento** passa a utilizar a **mesma parametrização definida para a data de emissão**. Com isso, os campos **Data de Emissão** e **Data de Competência** passam a receber **a mesma data**.

Essa alteração foi implementada para atendimento às regras do **layout nacional da NFS-e**, que exige o **envio obrigatório da data de competência**, além de **não permitir que essa data seja posterior à data de emissão**.

**Patches disponíveis**: 12.1.2502.241, 12.1.2506.189, 12.1.2510.122

⚙️ Parametrização Obrigatória – Regra Tributária

É **mandatório** o preenchimento da **Regra Tributária** nos **Parâmetros de Integração (Educacional × Fiscal)**.  
Sem esse vínculo, o sistema **não calcula IBS e CBS** e **não gera o movimento fiscal**.

**Caminho:**  
Ambientes → Parâmetros → Educacional → Integração → Fiscal → *Fiscal 2/2 – Regra Tributária para Geração de Movimento*

**Patches disponíveis**: 12.1.2502.248 · 12.1.2506.199 · 12.1.2510.131

**Nova hierarquia de definição**

**A partir das versões:** 12.1.2502.264 · 12.1.2506.224 · 12.1.2510.154

Foi disponibilizado o campo **Regra Tributária** no cadastro de **Serviço** (**Financeiro / Contábil → Serviço**)

**📐 Hierarquia de Prioridade**

1. Serviço
2. Parâmetros de Integração (Educacional × Fiscal)

Quando **não houver informação em nenhum nível**, o sistema **não gera o movimento**.

O preenchimento no **Serviço** torna-se necessário quando **não existir vínculo nos Parâmetros de Integração**, garantindo o correto tratamento tributário.

🧭 Validação de Cursos e Local da Operação

O sistema valida a **Modalidade / Tipo de Curso** para definir automaticamente o **Local da Operação** (município de incidência do imposto).

🎓 Ensino Superior

* Campo **Modalidade** torna-se **obrigatório**  
  *(EAD, Presencial, Semipresencial)*

#### 📍 Regras

* **EAD:** Município do **Aluno**
* **Presencial:** Município da **Filial**
* **Semipresencial:**

  + Obrigatório preencher **Regra de Emissão da NF**
  + Opções: *EAD* ou *Presencial*

🏫 Ensino Básico

* Sempre considerado **Presencial**
* **Local da operação:** Município da **Filial**

**📄 Acesse: [Guia de Cadastro do Curso](https://tdn.totvs.com/display/LRM/Cursos)**

**Patches disponíveis:** 12.1.2502.264 · 12.1.2506.224 · 12.1.2510.154

👤Destinatário do Serviço 

**Patches disponíveis:** 12.1.2502.264 · 12.1.2506.224 · 12.1.2510.154

O movimento **não será gerado** se o aluno não possuir:

* Nome Completo
* Endereço
* CPF válido

📄 **Acesse:**[Guia de Cadastro do Aluno](https://tdn.totvs.com/display/LRM/Alunos)

📄 **Acesse:**[Guia do destinatário do serviço](https://tdn.totvs.com/pages/releaseview.action?pageId=1012511875)

false📩 Envio de Dados do Destinatário do Serviço

**Patches disponíveis:** 12.1.2506.308 · 12.1.2510.234 · 12.1.2602.149

A partir das versões listadas, o sistema passa a validar o envio das informações do Destinatário do Serviço para o movimento financeiro com base nas seguintes condições:

**1. Quando o Aluno é o próprio Responsável Financeiro:**

* Os dados do Destinatário do Serviço **nunca** serão enviados ao movimento, uma vez que as informações do tomador já correspondem ao próprio aluno/responsável.

**2. Quando o Aluno NÃO é o próprio Responsável Financeiro:** O envio dependerá de uma combinação de parâmetros:

* **No Cadastro do Aluno:** O campo **"Envia dados do destinatário do serviço na geração do movimento"** deve estar marcado. Se estiver desmarcado, os dados não serão enviados.
* **No Processo de Geração de Movimento:** Caso o parâmetro do aluno esteja marcado, o sistema ainda verificará se a opção **"Envia dados do destinatário do serviço"** foi selecionada durante a execução do processo.

A partir dos patches 12.1.2506.299 · 12.1.2510.224 · 12.1.2602.142 , os dados do destinatário do serviço serão enviados apenas nos casos em que o aluno e o responsável financeiro **não forem a mesma pessoa**.

Importante

A partir dos patches 12.1.2506.326, 12.1.2510.256 e 12.1.2602.170:

* Os alunos cadastrados com mais de um endereço de e-mail e separados por ponto e vírgula terão somente o primeiro endereço enviado para o cadastro do destinatário do serviço.
false🌍 Estudantes Estrangeiros

Para alunos **não brasileiros**, o CPF **não é obrigatório.** A validação ocorre pela **nacionalidade** do cadastro.

**📄 NIF - Número de Identificação Fiscal**

* O campo **NIF** é exibido **exclusivamente para destinatários do exterior**.
* **Atualmente**, o TOTVS Educacional **envia automaticamente** a opção:  
  **“0 – Não informada na nota de origem”**, independentemente de preenchimento manual.
* Esse comportamento será mantido **até que o campo de NIF seja disponibilizado no cadastro do aluno** para preenchimento direto da informação.
* Para **destinatários nacionais (Brasil)**, o **NIF não é exigido**.

**Patches disponíveis**: 12.1.2502.248 · 12.1.2506.199 · 12.1.2510.131

⚠️ Código Indicador da Operação – Layout Nacional

O **Código Indicador da Operação**, obrigatório no layout nacional, **passa a ser preenchido no movimento** respeitando a seguinte regra:

| Regra | Código Indicador da Operação |
| --- | --- |
| Curso Presencial | **030101** |
| Educação a Distância (EAD) / Aluno | **030102** |

\*O Curso Semipresencial seguirá de acordo com a regra selecionada no campo: **Regra de Emissão da NF**

**Patches disponíveis:** 12.1.2502.292 · 12.1.2506.262 · 12.1.2510.181 · 12.1.2602.105

🛠️Parâmetro “Validar campos do layout nacional”

foi implementado o parâmetro **'Validar campos do layout nacional'** no processo de geração de movimento.

* Quando **desmarcado**, os campos obrigatórios do layout **não serão exigidos**
* Este parâmetro será **descontinuado** quando IBS e CBS se tornarem obrigatórios na NFS-e

**Patches disponíveis**: 12.1.2502.268 · 12.1.2506.229 · 12.1.2510.158

📄 NFS-e Para Alunos Estrangeiros 

**📦 Exportação de Serviços**

O sistema envia automaticamente para o Gestão de Estoque, Compras e Faturamento as informações necessárias para exportação de serviços quando o aluno for estrangeiro.

**Patches disponíveis**: 12.1.2510.166 · 12.1.2506.242 · 12.1.2502.277

**⚠️ Restrição Temporária de Parâmetro**

Durante o período de adequação às regras da **Reforma Tributária**, o parâmetro
**“Gerar um movimento para cada lançamento do boleto”**
ficará **temporariamente bloqueado para edição**.

**Comportamento padrão:**  
Será gerado **um movimento para cada lançamento financeiro**, garantindo a
**rastreabilidade fiscal**.

* O **agrupamento de boletos** será mantido, sem alterações.
* O **agrupamento de NFS-e** ficará temporariamente indisponível.
* A liberação ocorrerá após a conclusão dos ajustes na geração de movimento e definição
  dos **cenários fiscais elegíveis**.
