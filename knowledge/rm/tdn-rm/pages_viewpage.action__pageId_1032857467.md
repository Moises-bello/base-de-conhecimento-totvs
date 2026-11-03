---
content_hash: 87c9f48083bf86ff5cdfa547c97cb5ce4ccc0770371bb02f73098550ca9dd438
fetched_at: '2026-06-29T00:05:48.876899+00:00'
page_id: '1032857467'
product: rm
source: tdn-rm
title: Campo Período da Matrícula do Período Letivo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1032857467
version: 3
---

# **Conteúdo**

Índice

# Descrição

Ao realizar a rematrícula ou matrícula, o sistema executa algumas validações para determinar o próximo período do aluno que será automaticamente alimentado na matrícula (SMATRICPL.PERIODO). O cálculo dele sempre será o maior valor do período de todas as matrículas no período letivo do aluno mais **1**. Entretanto este valor não poderá passar da quantidade total de períodos da .

Entretanto algumas parametrizações são necessárias para que essas validações aconteçam corretamente e o período seja carregado de forma apropriada.

1. Se não existir nenhuma matrícula no período letivo para a matriz aplicada em questão o valor deste campo sempre será **1**.
2. Se existir matrículas em outros períodos letivos para a matriz aplicada em questão, o sistema irá ordenar todas as matrículas no período letivo em ordem **decrescente**, posicionando a matrícula mais recente no topo. A partir daí o sistema irá pegar o **período**desta matrícula e fará as checagens na situação de matrícula (aba período letivo) desta matrícula no período letivo informadas abaixo. Caso alguma condição abaixo seja **verdadeira** o **período** será o da matrícula mais recente. Agora, se todas forem **falsas** o **período** será o da matrícula mais recente **mais 1**.
   1. **Aluno ativo** - desmarcado
   2. **Indica trancamento** - marcado
   3. **Cancela contrato financeiro** - marcado

Por fim, a última validação será checar se o período retornado é maior que a quantidade total de períodos da , se sim, o sistema irá limitar neste valor, caso contrário seguirá com o período calculado anteriormente.

Alterar data de matrícula no período letivo

Vale ressaltar que é possível alterar a data de matrícula no período letivo pelo próprio cadastro, mas é condicionado à uma permissão especial no perfil do usuário.

Segue alguns exemplos.

#### **Exemplo 1**

Curso tem: **8** períodos.

Aluno cursou: **3** períodos letivos.

| Data da matrícula | Período letivo | Período | Situação de matrícula | Aluno ativo | Indica trancamento | Cancela contrato financeiro |
| --- | --- | --- | --- | --- | --- | --- |
|  | 2024/1 | 1 | Aprovado | Sim | Não | Não |
|  | 2024/2 | 2 | Aprovado | Sim | Não | Não |
|  | 2025/1 | **3** | Aprovado | Sim | Não | Não |

Próximo período: 3 + 1 = **4º período.**

#### **Exemplo 2**

Curso tem: **8** períodos.

Aluno cursou: **8** períodos letivos, mas não concluiu todas as disciplinas.

| Data da matrícula | Período letivo | Período | Situação de matrícula | Aluno ativo | Indica trancamento | Cancela contrato financeiro |
| --- | --- | --- | --- | --- | --- | --- |
|  | 2022/1 | 1 | Aprovado | Sim | Não | Não |
|  | 2022/2 | 2 | Aprovado | Sim | Não | Não |
|  | 2023/1 | 3 | Aprovado | Sim | Não | Não |
|  | 2023/2 | 4 | Aprovado | Sim | Não | Não |
|  | 2024/1 | 5 | Aprovado | Sim | Não | Não |
|  | 2024/2 | 6 | Aprovado | Sim | Não | Não |
|  | 2025/1 | 7 | Aprovado | Sim | Não | Não |
|  | 2025/2 | **8** | Aprovado | Sim | Não | Não |

Próximo período: 8 + 1 = 9º Período → **Extrapolou**a quantidade total de períodos, portando o **próximo período** será **8º período.**

#### **Exemplo 3**

Curso tem: **8** períodos.

Aluno cursou: **3** períodos letivos.

| Data da matrícula | Período letivo | Período | Situação de matrícula | Aluno ativo | Indica trancamento | Cancela contrato financeiro |
| --- | --- | --- | --- | --- | --- | --- |
|  | 2024/1 | 1 | Aprovado | Sim | Não | Não |
|  | 2024/2 | 2 | Aprovado | Sim | Não | Não |
|  | 2025/1 | **3** | Cancelado | **Não** | Não | Não |

Próximo período: **3º Período.**Porque a matrícula do período letivo 2025/1 **não** indica aluno ativo, **portanto** não irá somar **mais 1** no período.

#### **Exemplo 4**

Curso tem: **8** períodos.

Aluno cursou: **3** períodos letivos.

| Data da matrícula | Período letivo | Período | Situação de matrícula | Aluno ativo | Indica trancamento | Cancela contrato financeiro |
| --- | --- | --- | --- | --- | --- | --- |
|  | 2024/1 | 1 | Aprovado | Sim | Não | Não |
|  | 2025/1.1 | **2** | Aprovado | Sim | Não | Não |
|  | 2025/1 | 3 | Aprovado | Sim | Não | Não |

Próximo período: 2 + 1 = **3º período.**Porque a matrícula do período letivo 2025/1.1 é mais recente, logo o período dela é **2** **soma-se 1 = 3º período.** Neste caso o correto é alterar a data de matrícula do período letivo **2025/1.1** ou trocar os períodos, ou seja, em 2025/1.1 será **3º período**e 2025/1 será **2º período**. Fazendo isso o próximo período letivo será **4**.
