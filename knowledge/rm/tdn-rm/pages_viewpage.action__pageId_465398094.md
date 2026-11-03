---
content_hash: 21255fec4bbdac1942b00d5683780365342cb57255f65e7730dda59fc71591ae
fetched_at: '2026-06-29T00:10:15.994096+00:00'
page_id: '465398094'
product: rm
source: tdn-rm
title: Integração TOTVS Captação Sustentável
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=465398094
version: 13
---

Importante

Essa integração está disponível a partir da release 12.1.24.

## Visão geral

A cada avanço de etapa do Processo Seletivo os dados do interessado são atualizados no TOTVS Captação Sustentável. Assim que o interessado finaliza a inscrição com sucesso é atualizado no cadastro do TOTVS Captação Sustentável o novo código de usuário do Processo Seletivo.

O pré-requisito desta integração é a visibilidade do campo e-mail. Este campo será a chave temporária do interessado.

São 6 eventos passíveis de atualização:

1. Primeiro formulário de inscrição (mini-formulário);
2. Primeira etapa do formulário principal de inscrição;
3. Segunda etapa do formulário principal de inscrição;
4. Terceira etapa do formulário principal de inscrição ( finalização da inscrição );
5. Nova inscrição pela central do candidato;
6. Tentativa de inscrição em um novo processo seletivo com um candidato que já existe na base de dados.

Assim que realizado a seleção da atividade ofertada será atualizado o TOTVS Captação Sustentável.  
  
**Sistemas Envolvidos**

* TOTVS Processo Seletivo - O módulo Processo Seletivo gerencia toda a execução de um processo seletivo da Instituição, desde a inscrição, classificação, convocação e pré-matrícula.
* TOTVS Captação de Alunos - O TOTVS Captação de Alunos gerencia toda a automação de marketing e régua de relacionamento com candidatos e alunos.

**Integração**

O TOTVS Processo Seletivo pode ser configurado para integrar com o TOTVS Captação de Alunos, para isso é necessário configurar em cada processo seletivo os eventos que serão enviados.

**Escopo**

As entidades e os pontos de integração que farão parte do escopo dessa integração são:

|  |  |
| --- | --- |
| **Entidade** | **Ponto de Integração** |
| SPSUSUARIO | Dados pessoais |
| SPSUSUARIOTIPORELAC | Responsáveis do candidato |
| SPSINSCRICAOAREAOFERTADA | IDAREAINTERESSE , CODCOLIGADA |
| SPSOPCAOINSCRITO | IDAREAINTERESSE, CODCOLIGADA |
| SPSPROCESSOSELETIVO | NOME, IDPS, CODCOLIGADA, DTINIINSCRICAO, DTFIMINSCRICAO |
| SPSAREAINTERESSE | IDAREAINTERESSE, NOME |
| SPSAREAOFERTADA | NUMMININSCRIOES, NUMEROVAGAS |
| SHABILITACAOFILIAL | CODCOLIGADA, CODFILIAL |
| SHABILITACAOFILIALPL | DTINICIOALTERACAOPROGRAMA, DTFIMALTERACAOPROGRAMA |
| SGRADE | DTINICIO |
| SCURSO | CURPRESDIST, NOME, CODMODALIDADECURSO, CODCURSO |
| SMODALIDADE | DESCRICAO |
| SPARCPLANO | VALOR |

Parametrização, Simulaçãopasso1,passo2yespasso1

Durante a implantação do TOTVS Captação Sustentável, favor realizar a parametrização da Integração.

Os dados de acesso são gerados exclusivamente no TOTVS Captação Sustentável incluindo as informações de curso e oferta, sendo que o curso no formato (CODCOLIGADA-CODCURSO), sendo o CODCURSO vinculado a matriz aplicada ofertada na área de interesse ofertada do processo seletivo, no caso da oferta deve seguir o padrão (CODCOLIGADA-IDPS-IDAREAINTERESSE).

Os campos de Tipos de Eventos representam os códigos chave do cadastro de Tipo de Evento do TOTVS Captação Sustentável.

A parametrização é realizada por Processo Seletivo.

Para conseguir os dados de integração siga os passos abaixo no TOTVS Captação de Alunos:

**Endereço API, Token e Código Origem**

**Códigos do eventos**

Informe o nome do evento e copie seu código na URL.

nopasso2

Simulação do envio dos dados ao TOTVS Captação Sustentável ao avançar a primeira etapa do formulário principal do TOTVS Processo Seletivo.

## **Etapa por etapa**:

**Inscrição (dados básicos):**

Nessa etapa, será enviado dados do candidato em dois pontos do sistema:

1. Caso o e-mail esteja parametrizado no critério de busca e o candidato o preencha no mini formulário ao avançar, seus dados iniciais preenchido serão enviados ao TOTVS Captação Sustentável.

      2. Ao preencher os dados no formulário completo e avançar, esses dados também serão enviados ao TOTVS Captação Sustentável.

**Inscrição (responsáveis)**

Quando o processo seletivo está parametrizado para preencher responsáveis do candidato, assim que os dados dos responsáveis forem preenchidos ao avançar para a etapa de dados do curso, será realizar uma interação com o TOTVS Captação Sustentável.

Será vinculado todos os responsáveis do candidato, pai, mãe, responsável financeiro, responsável a acadêmico e responsável pela inscrição caso o processo seletivo esteja configurado para utilizar.

**Inscrição (dados curso):**

Assim que o candidato escolhe seu curso e finaliza a inscrição, será realizado uma interação com o TOTVS Captação Sustentável.

**Nova inscrição (central do candidato)**

Quando o candidato, que já possuí login e senha, acessa a central do candidato e clica no botão "Nova inscrição"  será realizado uma interação com o TOTVS Captação Sustentável.

**Nova Inscrição (candidato existente):**

Quando um candidato, que já existe na base, tenta realizar uma nova inscrição, porém no mesmo curso onde já está inscrito naquele processo seletivo, é realizado a interação com o TOTVS Captação Sustentável.
