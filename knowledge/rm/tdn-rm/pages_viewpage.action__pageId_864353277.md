---
content_hash: eece01964edac4253d0d1b84c016e957b9630d71fe87606c800ad41bc8229415
fetched_at: '2026-06-29T00:11:55.895617+00:00'
page_id: '864353277'
product: rm
source: tdn-rm
title: Condições Diferenciadas de Trabalho
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=864353277
version: 4
---

No menu Funcionários | Anexos | Segurança e Medicina foi disponibilizado o anexo Condições Diferenciadas de Trabalho.

O cadastro lista os seguintes tipos de condições diferenciadas de trabalho conforme o layout do evento S-2360:

* 01 – Insalubridade
* 02 – Periculosidade
* 03 – Fator de Risco
* 04 – Membro SESMT
* 05 – Designado CIPA
* 06 – Trabalhador treinado para utilização de material de primeiros socorros
* 07 – Autorizado a trabalhar em instalações elétricas
* 08 – Autorizado a operar e intervir em máquinas
* 09 – Responsável Técnico pela Segurança em Espaço Confinado

### 

Através deste anexo, será possível visualizar as condições diferenciadas geradas automaticamente pelo sistema. Além disso, o usuário poderá incluir manualmente as seguintes condições diferenciadas:

* 06 – Trabalhador treinado para utilização de material de primeiros socorros
* 07 – Autorizado a trabalhar em instalações elétricas
* 08 – Autorizado a operar e intervir em máquinas
* 09 – Responsável Técnico pela Segurança em Espaço Confinado

Os demais itens da lista de Condições Diferenciadas de Trabalho serão gerados automaticamente pelo sistema no anexo "Condições Diferenciadas de Trabalho":

* **01 – Insalubridade**
* **02 – Periculosidade**

As condições diferenciadas relacionadas à Insalubridade e Periculosidade são definidas através do módulo TOTVS Segurança e Medicina do Trabalho, no menu "Reconhecimento e Avaliação de Risco".

No Cadastro de Reconhecimento e Avaliação de Riscos, foi inserida uma nova aba denominada “Insalubridade/Periculosidade”. Nessa aba, o usuário deverá indicar se um determinado Reconhecimento de Risco irá proporcionar aos funcionários uma condição de trabalho de Periculosidade e/ou Insalubridade.

Os campos "Exposição a Periculosidade" e "Exposição a Insalubridade" deverão ser marcados para indicar as situações correspondentes. O usuário também deverá preencher os respectivos campos de Laudo.

Ao marcar "Exposição a Insalubridade", o campo "Fator de Insalubridade" será habilitado, permitindo ao usuário especificar o grau insalubre (Máximo, Médio ou Mínimo) ao qual o funcionário está exposto.

A geração automática das Condições Diferenciadas de Trabalho, que serão visualizadas no anexo do cadastro de funcionários, depende da geração da Avaliação do Risco.

**ATENÇÃO**: O campo também pode ser preenchido pela integração via API com a Quirons, permitindo o envio do valor correspondente por grau. Para acessar a versão disponível do novo campo, [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=864353887), veja as configurações abaixo:

**Insalubridade**:

* + - Grau 0: Não há
    - Grau 1: 10%
    - Grau 2: 20%
    - Grau 3: 40%

**Periculosidade**:

* + - 1: Sim (30%)
    - 2: Não

**03 – Fator de Risco**  
Quando uma Avaliação de Risco é realizada, a Condição Diferenciada de Trabalho por Fator de Risco é gerada automaticamente no anexo do cadastro de funcionário. Se a Avaliação incluir situações de Periculosidade e/ou Insalubridade, essas condições também serão adicionadas ao cadastro.

**04 – Membro SESMT**  
Serão considerados membros do SESMT os funcionários cadastrados como Responsáveis pelos Registros Ambientais SESMT no TOTVS Segurança e Medicina do Trabalho | PPRA | Resp. Reg. Ambientais.

 E também aqueles cadastrados como Responsáveis pelas Monitorações Biológicas SESMT, realizadas em TOTVS Segurança e Medicina do Trabalho | PCMSO | Resp. Monitoração Biológica.

**05 – Designado CIPA**  
Funcionários identificados como Representantes ou Suplentes da CIPA, seja eleitos pelos empregados ou indicados pelo empregador, serão automaticamente classificados com a condição diferenciada de trabalho "Designado da CIPA".

**OBSERVAÇÃO**: As condições diferenciadas de trabalho geradas automaticamente pelo sistema não poderão ser editadas ou excluídas no anexo do Cadastro de Funcionários.
