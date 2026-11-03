---
content_hash: 3b5eb15e10c1890a5918246d47d7896f48362a05938cbee571db13a133f4184f
fetched_at: '2026-06-29T00:10:04.836316+00:00'
page_id: '452719260'
product: rm
source: tdn-rm
title: Gestão de Metas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719260
version: 2
---

**Gestão de Metas**

 A Gestão de Metas tem como objetivo definir o caminho (metas) a ser cumprido pelos funcionários para se chegar a um objetivo. Utilizando o Totvs Portal, gestores podem acompanhar as metas de todos os seus participantes. Pontos de impacto da Gestão de Metas:

1) PDI: Utiliza a estrutura de metas e seu acompanhamento para criar as ações e lançamentos de completude.

2) Requisitos de Acesso: Realiza a concessão de requisitos de acesso, ao realizar o cumprimento das metas.

**1 – Cadastro da meta**

Acessar Acompanhamento| Gestão de Metas para criar um novo registro.

Nome: campo descritivo para nomear a Gestão de Metas;

Status: campo que conterá o status da Gestão de Metas. Este não é editável e pode conter somente os seguintes valores: Aberta, Em planejamento, Suspensa/Replanejamento, Cancelada e Finalizada; \*\***Somente metas com o Status Aberta são visualizadas no Totvs Portal.**

Descrição: campo descritivo para maiores explicações sobre a meta;

Data início/Data fim: campo que controla a data de início/fim da meta. Se a data fim for menor que a data de acesso do avaliador no Totvs Portal, a meta não é visualizada;

Grupo da meta: campo que define em qual grupo as metas serão vinculadas;

**1.1 – Cadastro da meta tipo agrupadora**

Tipo: campo que define qual será o tipo da meta:

- Agrupadora Composição de metas:

aba para definição da composição das metas. A composição pode conter "Meta valor" e "Meta agrupadora".

**Observações:**

Incluir metas com o status planejamento ou suspenso/replanejamento.

- Cada meta vinculada terá um percentual de participação na "meta pai". O percentual deverá ser um valor numérico entre 0 e 100.

- Se o valor do somatório dos percentuais for maior que 100, será emitido um alerta para o usuário revisar os percentuais definidos.

- Somente poderá ser alterada a composição de metas com o status "Em planejamento" ou "Suspenso / Replanejamento", e somente metas neste mesmo status poderão ser incluídas na composição de metas. Atribuições:

- Avaliador: um funcionário ou um externo. Apenas uma opção deve ser preenchida;

- Avaliados: uma seção, uma equipe, um funcionário ou um externo. Apenas uma opção deve ser preenchida;

Somente poderá ser alterada a atribuição de metas com o status "Em planejamento" ou "Suspenso / Replanejamento".

**1.2 – Cadastro da meta tipo valor**

Tipo: campo que define qual será o tipo da meta:

- Valor Configuração Tipo de valor

- Valor de referência - Faixa de valores: aba para definição das faixas de valores a serem utilizadas na apuração das metas. Será pelo enquadramento de faixas que será possível verificar o cumprimento de uma meta.

**Observações:**

- O cadastro de faixas permitirá que o usuário crie faixas que cubram todos os valores possíveis, utilizando para isso os operadores <, <=, >, >= e =.

- A faixa que estiver com o campo "Meta Cumprida quando estiver nesta faixa" marcado, define a faixa onde a meta estará cumprida.

- O campo "Fator Multiplicador" é utilizado no cálculo da remuneração variável utilizando metas.

Para calcular o valor a ser pago para determinada meta, deve ser aplicado o fator da faixa de atingimento da meta. Para maiores informações consulte: Valorização| Benefícios e Remuneração Variável| Passo a passo para cálculo da Remuneração Variável utilizando Metas.

Valor de referência - Valor referência: valor base para cumprimento da meta. - Cumprimento da meta     Acima do valor de referência     Abaixo do valor de referência

Forma de avaliação - Somatório dos lançamentos - Último lançamento

Opções Avaliado visualiza meta: campo que define que quando o avaliado acessar o Totvs Portal, suas metas serão visualizadas.

Exige aceite dos avaliados: campo que define que o avaliador pode solicitar o aceite da meta ao avaliado pelo Totvs Portal. Ao solicitar o aceite, o avaliado recebe email com a informação de pendência de aceite. Este campo somente será habilitado se o campo "Avaliado visualiza meta" estiver marcado.

Avaliado pode lançar resultado: campo que define que quando o avaliado acessar o Totvs Portal é permitido realizar lançamento de resultados nas metas. Este campo somente será habilitado se o campo "Avaliado visualiza meta" estiver marcado.

Lançamento exige aprovação do avaliador: campo que define que quando o avaliado incluir um lançamento através do Totvs Portal, o lançamento ficará pendente até a aprovação do avaliador. Este campo somente será habilitado se o campo "Avaliado pode lançar resultado" estiver marcado.

Avaliado pode solicitar aprovação do lançamento: campo que define que quando o avaliado incluir um lançamento através do Totvs Portal, ele pode solicitar a aprovação do lançamento para o avaliador. Ao solicitar a aprovação, o avaliador recebe email com a informação da aprovação. Este campo somente será habilitado se o campo "Lançamento exige aprovação do avaliador" estiver marcado.

Envio automático de e-mail após lançamento: campo que define que quando o lançamento da meta for realizado no Totvs Portal, um email será enviado ao avaliador.

Atribuições

- Avaliador: um funcionário ou um externo. Apenas uma opção deve ser preenchida;

- Avaliados: uma seção, uma equipe, um funcionário ou um externo. Apenas uma opção deve ser preenchida;

Somente poderá ser alterada a atribuição de metas com o status "Em planejamento" ou "Suspenso / Replanejamento".

**Atenção:**

- Uma meta só poderá ser excluída ou ter sua atribuição e sua composição alteradas se estiver com o status "Planejamento".

- Uma meta agrupadora que for "meta pai" numa composição de metas, não poderá ser alterada para "meta valor".

- O resultado de uma meta se refere diretamente a ela e não à atribuição. Portanto a apuração do resultado não será feita por membros, mas sim em relação à meta.  
   
**2 – Lançamento de resultados de metas**

Acessar Acompanhamento| Gestão de Metas e selecionar uma meta do tipo Valor. Aba Lançamentos: aba que permite que o usuário registre os resultados de uma determinada meta.

**Observações:**

- O campo "Data alteração" por padrão insere a data atual e esta nunca pode ser maior que ela.

- Pode ser preenchido o campo "Valor" ou "Comentário", ou se desejar os dois campos simultaneamente. - Somente metas com o status "Aberta" permitem a inclusão, exclusão e edição de lançamentos de resultados.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Requisitos de Acesso vinculados  
Cadastro de Targets

|  |  |
| --- | --- |
|  | Como Fazer |

---

Trocar status de metas  
Planejamento de metas  
Lançamento de resultados de metas Vincular/Desvincular Requisitos de Acesso e Metas  
   
   
Gestão de Metas no Totvs Portal
