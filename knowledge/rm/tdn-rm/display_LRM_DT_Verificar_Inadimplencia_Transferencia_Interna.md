---
content_hash: 6c70c9a69237bec70dc28658d0f6fe17c2deb278c3b6c3464888b9716f78cfee
fetched_at: '2026-06-29T00:08:10.901051+00:00'
page_id: '241699676'
product: rm
source: tdn-rm
title: DT_Verificar_Inadimplencia_Transferencia_Interna
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Verificar_Inadimplencia_Transferencia_Interna
version: 111
---

# Transferência interna - verificação de inadimplência

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Transferência interna | Transferência interna (na mesma filial e entre filiais) | | Transferência interna entre coligadas | Transferência interna entre coligadas | |
| **Requisito (ISSUE):** | EDUEDU001-69 |
| **País(es):** | Todos |

## Descrição

Esta implementação tem por objetivo dissociar a validação de inadimplência dos processos de matrícula com a validação dos processos de transferências interna dos alunos (seja essa dentro da mesma filial, entre filiais ou entre coligadas).

## **Parâmetros gerais do TOTVS Educacional**

Para configuração da validação de inadimplência o TOTVS Educacional dispõe de alguns parâmetros importantes, que devem ser definidos de acordo com a necessidade de operação da instituição de ensino, para tanto basta acessar **Configurações | Parâmetros** e configurar os seguintes itens:

* **Matrícula - Bloquear matrícula para inadimplentes** - responsável por definir se o sistema executará a validação de inadimplência.
* **Matrícula - Bloquear mudança de situação de matrícula para inadimplentes** - responsável por definir se o sistema executará a validação de inadimplência quando o cenário for de alteração da situação de matrícula.
* **Tesouraria - Verificar débitos do aluno em outras coligadas** - determina se a validação de inadimplência será apenas no âmbito da coligada corrente ou levará em consideração todas as coligadas do sistema.
* **Tesouraria - Número de dias de carência para inadimplência** -  determina a partir de quantos dias de atraso no pagamento o sistema passa a considerar como inadimplência.
* **Tesouraria - Valor máximo de tolerância  para inadimplência** - determina um valor teto para que o aluno ainda não seja considerado inadimplente.
* **Tesouraria - Valor máximo da conta corrente de tolerância para inadimplência** - de forma similar ao item anterior no entanto com relação aos valores da conta corrente do aluno.

Estes parâmetros configurados definem a forma que o sistema irá se comportar para verificar a validação de inadimplência.

## **Definição de permissões especiais para os perfis de usuário**

Basta acessar**Serviços Globais | Segurança | Perfis**, selecionar o sistema "**Educacional**" e em seguida no perfil desejado acessar o anexo **"Parâmetros educacionais"** e parametrizar os seguintes itens:

* **Aba: Matrícula/Rematrícula/Transferência - Matricular alunos inadimplentes** - com este parâmetro marcado todos os usuários associados ao perfil poderão matricular alunos inadimplentes mesmo que o parâmetro geral esteja definido para bloquear a matrícula. (comportamento atual do sistema)
* **Aba: Matrícula/Rematrícula/Transferência - Permitir transferência de alunos inadimplentes** - com este novo parâmetro todos os usuários associados ao perfil poderão transferir alunos inadimplentes dentro da mesma filial, entre filiais ou entre coligadas mesmo que o parâmetro geral esteja definido para bloquear a matrícula.

## Processos de transferência interna (na mesma filial, entre filiais e entre coligadas)

**Comportamento do sistema antes da alteração**

As transferências internas sem a alteração proposta possuíam o seguinte comportamento:

* Se o parâmetro do TOTVS Educacional “**Bloquear matrícula de inadimplentes**” estiver desmarcado a transferência é realizada com sucesso mesmo o aluno estando inadimplente.
* Se o parâmetro do TOTVS Educacional “**Bloquear matrícula de inadimplentes**” estiver marcado e o usuário possuir em seu perfil a opção “**Matricular alunos inadimplentes**” marcada, a transferência é realizada com sucesso mesmo o aluno estando inadimplente.
* Se o parâmetro do TOTVS Educacional “**Bloquear matrícula de inadimplentes**” estiver marcado e o usuário possuir em seu perfil a opção “**Matricular alunos inadimplentes**” desmarcada, a transferência não é realizada e o sistema exibe ao final do processo a informação de inadimplência do aluno.

**Comportamento do sistema após a alteração**

Os processos de transferência interna passam a disponibilizar na aba de **"Dados de Destino**" um novo parâmetro para que o usuário com a permissão adequada possa definir se a validação de inadimplência deverá ou não ser um impeditivo para a transferência. A  nova opção é: "**Transferir alunos inadimplentes**", este novo campo só ficará disponível para alteração quando o parâmetro do TOTVS Educacional "**Bloquear matrícula de inadimplentes**" e o parâmetro do perfil do usuário **"Permitir transferência de alunos inadimplentes**" estiverem marcados.

Com a implementação do parâmetro  “**Permitir transferência de alunos inadimplentes**” no perfil do usuário do TOTVS Educacional e do parâmetro "**Transferir alunos inadimplentes**" nos processos de transferências, o sistema passa a ter o seguinte comportamento:

* Parâmetro do TOTVS Educacional “**Bloquear matrícula de inadimplentes**” estiver desmarcado a transferência é realizada com sucesso mesmo o aluno estando inadimplente. Neste cenário o parâmetro "**Transferir alunos inadimplentes****"** é apresentado desabilitado nos processos de transferência interna.
* Parâmetro do TOTVS Educacional “**Bloquear matrícula de inadimplentes**” estiver marcado e o usuário possuir em seu perfil a opção “**Permitir transferência de alunos inadimplentes**” marcada, neste cenário é exibido nos processos de transferência interna o parâmetro "**Transferir alunos inadimplentes****":**
  + Se estiver desmarcado a inadimplência é verificada e se o aluno estiver inadimplente a transferência não é realizada.
  + Se estiver marcado a inadimplência é verificada e a transferência é realizada mesmo o aluno estando inadimplente.
* Parâmetro do TOTVS Educacional “**Bloquear matrícula de inadimplentes**” estiver marcado e o usuário possuir em seu perfil a opção “**Permitir transferência de alunos inadimplentes**” desmarcada, a inadimplência é verificada e se o aluno estiver inadimplente a transferência não é realizada. Neste cenário o parâmetro "**Transferir alunos inadimplentes****"**é apresentado desabilitado nos processos de transferência interna.

**Importante:**

* O comportamento relacionado a verificação de inadimplência para os processos de matrículas presenciais, via portal e processos seletivos não sofreu nenhum tipo de alteração.
* Quando houver uma transferência de um aluno de **A (período letivo 2016/1) para B (período letivo 2016/1)**e em outro momento for realizada a **operação inversa** o parâmetro do TOTVS Educacional a ser avaliado não mais será o “**Bloquear matrícula de inadimplentes**” e sim o "**Bloquear mudança de situação de matrícula para inadimplentes**".  O motivo da utilização do parâmetro "**Bloquear mudança de situação de matrícula para inadimplentes**" é que neste cenário não está sendo realizada uma matrícula e sim uma alteração de situação de matrícula.

divs
