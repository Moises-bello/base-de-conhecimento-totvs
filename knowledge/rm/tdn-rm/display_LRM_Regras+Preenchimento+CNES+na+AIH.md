---
content_hash: bd59cbf3dc813f0521ca5a808c74a02109e6f710be7ea3823859b983d80a2893
fetched_at: '2026-06-29T00:05:46.992929+00:00'
page_id: '1003989849'
product: rm
source: tdn-rm
title: Regras Preenchimento CNES na AIH
type: documentation
url: https://tdn.totvs.com/display/LRM/Regras+Preenchimento+CNES+na+AIH
version: 4
---

## **CONTEÚDO**

2CONTEÚDO

## **01. Visão Geral**

O campo **CNES (Cadastro Nacional de Estabelecimentos de Saúde)** identifica o local de execução do procedimento informado na AIH (Autorização de Internação Hospitalar).

No **TOTVS RM Saúde**, o campo é preenchido automaticamente no momento da **inclusão do registro do procedimento** dentro da AIH, de acordo com as configurações definidas nos **Parâmetros SUS**, no **cadastro do prestador** e nas **informações do hospital** (prestador principal).

O preenchimento do CNES ocorre **no momento da inclusão do item** (procedimento) na AIH, seja pela tela de **Elaboração da AIH** ou pela tela de **Registro de Informações de Cirurgias**.

O correto preenchimento desse campo é essencial para garantir a consistência dos dados enviados ao **DATASUS**, evitando rejeições indevidas no **SIHD2** (Sistema de Informações Hospitalares Descentralizado).

Informações

* O campo **CNES do executante não é obrigatório** conforme o layout DATASUS.
* O **CNES do hospital** continua sendo obrigatório.
* A nova regra garante compatibilidade com o **SIHD2**, evitando rejeições de profissionais autônomos sem vínculo CNES.
* A alteração é aplicada apenas na **inclusão de novos registros**, não alterando itens já gravados.

## **02.** **Obrigatoriedade no Layout SISAIH01**

Segundo o **layout oficial do SISAIH01 – DATASUS**, o campo **CNES do executante** **não é de preenchimento obrigatório**.

> O CNES é obrigatório apenas para o *estabelecimento principal (hospital)* informado no cabeçalho da AIH.

O CNES do executante deve ser informado **somente quando o profissional possuir vínculo formal com o CNES cadastrado**.

Quando o prestador for **autônomo (Pessoa Física)** e **não possuir vínculo CNES**, o campo **deve permanecer vazio**.

### **Motivo**

O envio indevido do CNES do hospital para prestadores autônomos pode gerar rejeições no **SIHD2**, como:

> *“PROFISSIONAL NÃO VINCULADO AO CNES COM O CBO INFORMADO”*

Portanto, a ausência do CNES do executante **é válida e aceita pelo DATASUS**.

## **03.** **Locais de Configuração**

O campo **CNES do executante** é preenchido automaticamente no momento da inclusão do procedimento na AIH.

A regra segue a hierarquia: **Faixa** → **Prestador** → **Hospital**

Essas configurações garantem que o arquivo gerado não seja rejeitado pelo **SIHD2**, que valida o vínculo entre **Profissional + CBO + CNES**.

| Campo | Descrição | Origem / Regra de Preenchimento |
| --- | --- | --- |
| **CNES por Faixa** | CNES configurado por faixa de código do procedimento nos Parâmetros SUS (Aba AIH). | Se existir faixa com CNES preenchido, esse valor é priorizado. |
| **CNES do Prestador** | CNES informado no cadastro do prestador executante. | Utilizado quando não há faixa aplicável com CNES. |
| **CNES do Hospital** | Parâmetro que define o comportamento quando o prestador executante não possui CNES. | *Ligado:* usa CNES do hospital. *Desligado:* CNES vazio. |

### **03.01. CNES por Faixa**

**Local: P****arâmetros SUS → Aba AIH**

Permite configurar **faixas de procedimentos** com o CNES específico da execução.

* + Se o procedimento da AIH estiver dentro da faixa configurada, o sistema prioriza o **CNES dessa faixa**.
  + Campo: *CNES (Estabelecimento de Execução)*.

### **03.02. CNES do Prestador**

**Local: C****adastro de Prestador**

Campo: *CNES do Prestador*.

* + Usado quando o procedimento não se enquadra em nenhuma faixa configurada nos Parâmetros SUS.
  + Aplica-se tanto para profissionais Pessoa Física quanto Jurídica.

### **03.03. CNES do Hospital**

**Local: Parâmetros SUS → Aba AIH**

* + Controla se, na ausência de CNES no prestador, o sistema deve ou não utilizar o CNES do prestador da unidade de faturamento do hospital.
  + A regra varia conforme o estado desse parâmetro (ligado/desligado).

## **04. Regras para Procedimentos com Equipe**

Para procedimentos que exigem **equipe** (ex.: parto, vasectomia, laqueadura, neonatal etc.), o sistema cria registros separados para cada prestador da equipe.

* + Cada prestador terá seu CNES calculado individualmente, conforme as regras acima.
  + Caso o procedimento não exija equipe, o executante padrão será o hospital.

## **05. Exportação para o SISAIH01**

Na geração do arquivo TXT da AIH (SISAIH01):

* + O campo **CNES** do item será exportado com o valor calculado conforme as regras acima.
  + Quando o campo estiver **vazio**, será exportado **em branco**, sem preenchimento automático com o CNES do hospital.
  + Esse comportamento está em conformidade com o **layout oficial do DATASUS**.

## **06.** **Exemplo de Configuração**

**Passos para configuração e uso:**

1. 1. Acesse **Faturamento > SUS > Parâmetros SUS > Aba AIH**.
   2. Configure uma **Faixa de Procedimentos** com o CNES do local de execução, se aplicável.
   3. Inclua um procedimento na AIH:

      * Se o código do procedimento estiver **dentro da faixa configurada com CNES**, o sistema utilizará esse valor.
      * Se **não houver faixa configurada**, o sistema buscará o **CNES do prestador executante** (cadastro do profissional).
      * Se o prestador **não tiver CNES cadastrado**:

        + Se o parâmetro **CNES do Hospital”** estiver **ligado**, o sistema usará o **CNES do hospital**.
        + Se o parâmetro estiver **desligado**, o **CNES ficará vazio**.

Dica

Para prestadores autônomos (Pessoa Física sem vínculo CNES), mantenha o campo CNES do cadastro em branco. O arquivo SISAIH01 aceitará o CNES vazio sem gerar rejeição.

### **Exemplo 1 – Procedimento dentro da Faixa configurada**

| Tipo de configuração | Valor |
| --- | --- |
| Faixa 040801010–040801020 | CNES = 3218813 |
| Prestador executante | Dr. João (sem CNES) |
| Parâmetro "CNES do Hospital” | Ligado |

**Resultado:** CNES = 3218813  
**Origem:** Faixa de Procedimentos.

---

### **Exemplo 2 – Fora da faixa, prestador com CNES**

| Tipo de configuração | Valor |
| --- | --- |
| Sem faixa aplicável | — |
| Prestador executante | CNES = 1234567 |
| Parâmetro "CNES do Hospital” | Qualquer |

**Resultado:** CNES = 1234567  
**Origem:** Cadastro do Prestador.

---

### **Exemplo 3 – Fora da faixa, prestador sem CNES, parâmetro ligado**

| Tipo de configuração | Valor |
| --- | --- |
| Sem faixa aplicável | — |
| Prestador executante | CNES vazio |
| Parâmetro "CNES do Hospital” | Ligado |

**Resultado:** CNES = CNES do Hospital  
**Origem:** Parâmetro ativo.

---

### **Exemplo 4 – Fora da faixa, prestador sem CNES, parâmetro desligado**

| Tipo de configuração | Valor |
| --- | --- |
| Sem faixa aplicável | — |
| Prestador executante | CNES vazio |
| Parâmetro "CNES do Hospital” | Desligado |

**Resultado:** CNES = (vazio)  
**Origem:** Parâmetro inativo.

---

### **Exemplo 5 – Sem prestador executante informado**

| Tipo de configuração | Valor |
| --- | --- |
| Prestador executante | Não informado |
| Parâmetro "CNES do Hospital” | Qualquer |

**Resultado:** CNES = (vazio)  
**Origem:** Ausência de executante.
